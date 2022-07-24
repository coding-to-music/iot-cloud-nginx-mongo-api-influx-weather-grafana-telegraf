# iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf

# 🚀 IotCloud is a platform where you can automate your house easily and in an inexpensive way. 🚀

https://github.com/coding-to-music/iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf

From / By Cesar Sanz https://github.com/csanz91

https://github.com/csanz91/IotCloud

## Environment variables:

```java

```

## GitHub

```java
git init
git add .
git remote remove origin
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:coding-to-music/iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf.git
git push -u origin main
```

# IotCloud

IotCloud is a platform where you can automate your house easily and in an inexpensive way.

## Secrets

```
secrets:
  modules_secrets:
      file: ./python-modules/secrets
```

## How to run:

```
docker-compose up
```

# How to stop

```
docker-compose down
```

Output:

```java
WARNING: Service "backup-manager" uses an undefined secret file "/mnt/volume_nyc1_01/iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf/backup-manager/secrets/gdrive_backup_folder", the following file should be created "/mnt/volume_nyc1_01/iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf/backup-manager/secrets/gdrive_backup_folder"
Stopping nginx-proxy-letsencrypt                                               ... done
Stopping iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_telegraf_1  ... done
Stopping iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_mongodb_1   ... done
Stopping iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_mosquitto_1 ... done
Stopping iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_influxdb_1  ... done
Stopping monitoring                                                            ... done
Stopping ota                                                                   ... done
Stopping nginx-proxy                                                           ... done
Removing nginx-proxy-letsencrypt                                               ... done
Removing iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_telegraf_1  ... done
Removing iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_mongodb_1   ... done
Removing iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_mosquitto_1 ... done
Removing iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_influxdb_1  ... done
Removing monitoring                                                            ... done
Removing ota                                                                   ... done
Removing nginx-proxy                                                           ... done
Removing network iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_default
```
