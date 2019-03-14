import logging
import logging.config
import os
from collections import defaultdict
import paho.mqtt.client as mqtt

import influx
from docker_secrets import getDocketSecrets
import utils
import max_list
import thermostat_gw
import totalizer_gw
from cache_decorator import clear_cache

# Logging setup
logger = logging.getLogger()
handler = logging.handlers.RotatingFileHandler('../logs/influx_gateway.log', mode='a', maxBytes=1024*1024*10, backupCount=2)
formatter = logging.Formatter('%(asctime)s <%(levelname).1s> %(funcName)s:%(lineno)s: %(message)s')
logger.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)


# Mqtt callbacks
def onValue(client, userdata, msg):
    # Avoid string values as mathematical operations cant
    # be made afterwards
    try:
        value = utils.parseFloat(msg.payload)
        tags, _ = utils.decodeTopic(msg.topic)
        sensorHash = utils.calculateSensorHash(msg.topic)
    except:
        logger.error('The message: "%s" cannot be processed. Topic: "%s" is malformed. Ignoring data' % (msg.payload, msg.topic))
        return

    try:
        valueRange = max_list.getValueRange(influxDb, tags['locationId'], tags['sensorId'])
    except:
        logger.error("It was not possible to calculate the values range", exc_info=True)
        valueRange = None

    try:
        lastValues[sensorHash].addValueSafe(value, valueRange)
    except ValueError:
        return

    fields = {"value": value}
    tagsToSave =  ["locationId", "sensorId"]
    measurement = "sensorsData"
    influxDb.writeData(measurement, utils.selectTags(tagsToSave, tags), fields, retentionPolicy="raw")

def onState(client, userdata, msg):
    try:
        state = utils.decodeBoolean(msg.payload)
        tags, _ = utils.decodeTopic(msg.topic)
    except:
        logger.error('The message: "%s" cannot be processed. Topic: "%s" is malformed. Ignoring data' % (msg.payload, msg.topic))
        return

    fields = {"state": state}
    tagsToSave =  ["locationId", "sensorId"]
    measurement = "sensorsData"
    influxDb.writeData(measurement, utils.selectTags(tagsToSave, tags), fields, retentionPolicy="3years")

def onStatus(client, userdata, msg):
    try:
        status = utils.decodeStatus(msg.payload)
        tags, _ = utils.decodeTopic(msg.topic)
    except:
        logger.error('The message: "%s" cannot be processed. Topic: "%s" is malformed. Ignoring data' % (msg.payload, msg.topic))
        return

    fields = {"status": status}
    tagsToSave =  ["locationId", "deviceId"]
    measurement = "sensorsData"
    influxDb.writeData(measurement, utils.selectTags(tagsToSave, tags), fields, retentionPolicy="3years")

def onIP(client, userdata, msg):
    try:
        IP = msg.payload
        tags, _ = utils.decodeTopic(msg.topic)
    except:
        logger.error('The message: "%s" cannot be processed. Topic: "%s" is malformed. Ignoring data' % (msg.payload, msg.topic))
        return

    fields = {"IP": IP}
    tagsToSave =  ["locationId", "deviceId"]
    measurement = "devicesIPs"
    influxDb.writeData(measurement, utils.selectTags(tagsToSave, tags), fields, retentionPolicy="raw")

def init(influxDb):
    """
    From the docs: If you attempt to create a retention policy identical to one that 
        already exists, InfluxDB does not return an error. If you attempt to create a 
        retention policy with the same name as an existing retention policy but with 
        differing attributes, InfluxDB returns an error.
    -i.e. If we want to edit some of the following values, do it in the Influx cli.

    The values received will be stored for 45 days at their original resolution, 
        and they are aggregated every:
            -hour and stored for 1 year,
            -day and stored for 3 years,
    """
    # Setup the retention policies
    influxDb.client.create_retention_policy('raw', '45d', 1, default=True)
    influxDb.client.create_retention_policy('1year', '365d', 1)
    influxDb.client.create_retention_policy('3years', '1080d', 1)

    influxDb.client.query(""" CREATE CONTINUOUS QUERY "sensorsData_1h" ON %s BEGIN
                                SELECT mean("value") AS "value"
                                INTO "1year"."downsampled_sensorsData_1h"
                                FROM "raw"."sensorsData"
                                GROUP BY time(1h), *
                              END
                          """ % os.environ['INFLUXDB_DB'])

    influxDb.client.query(""" CREATE CONTINUOUS QUERY "sensorsData_1d" ON %s BEGIN
                                SELECT mean("value") AS "value"
                                INTO "3years"."downsampled_sensorsData_1d"
                                FROM "1year"."downsampled_sensorsData_1h"
                                GROUP BY time(1d), *
                              END
                            """ % os.environ['INFLUXDB_DB'])

logger.info("Starting...")

# Influx databse setup
influxDb = influx.InfluxClient('influxdb', database=os.environ['INFLUXDB_DB'], username='', password='')

# Initialize the database
init(influxDb)

# Global values
lastValues = defaultdict(lambda: max_list.MaxSizeList(10))

# Constants
clear_cache()

# MQTT constants
version = 'v1'
topicHeader= "{version}/+/+/".format(version=version)
valuesTopic = topicHeader + "+/value"
stateTopic = topicHeader + "+/state"
statusTopic = topicHeader + "status"
IPTopic = topicHeader + "ip"

# Setup MQTT client
mqttclient = mqtt.Client()
token = getDocketSecrets('mqtt_token')
mqttclient.username_pw_set(token, "_")

def onConnect(self, mosq, obj, rc):
    # Setup subscriptions
    mqttclient.subscribe(valuesTopic)
    mqttclient.message_callback_add(valuesTopic, onValue)

    mqttclient.subscribe(stateTopic)
    mqttclient.message_callback_add(stateTopic, onState)

    mqttclient.subscribe(statusTopic)
    mqttclient.message_callback_add(statusTopic, onStatus)

    mqttclient.subscribe(IPTopic)
    mqttclient.message_callback_add(IPTopic, onIP)   

    thermostat_gw.onConnect(mqttclient, influxDb)
    totalizer_gw.onConnect(mqttclient, influxDb)
    
mqttclient.on_connect = onConnect

# Connect
mqttclient.connect('mosquitto')
mqttclient.loop_forever(retry_first_connection=True)

influxDb.close()

logger.info("Exiting...")