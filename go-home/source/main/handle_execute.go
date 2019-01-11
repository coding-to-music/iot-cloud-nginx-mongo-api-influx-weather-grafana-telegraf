package main

import (
	"encoding/json"
	"fmt"
	"model"
	"mqtt"
	"net/http"
	"strconv"
	"strings"
)

// Aux function to add an ID to a response
func addID(responseModel model.ResponseCommandsModel, ID string) model.ResponseCommandsModel {
	ids := responseModel.Ids
	ids = append(ids, ID)
	responseModel.Ids = ids
	return responseModel
}

func handleDeviceExecute(w http.ResponseWriter, r *http.Request, dfReq model.DeviceRequest, input model.InputModel) {

	responseCommands := []model.ResponseCommandsModel{}
	for _, command := range input.Payload.Commands {
		if err := requestedDeviceExist(r, command.Devices); err != nil {
			model.ReturnAPIErrorDeviceNotFound(w, dfReq.RequestID)
			return
		}
		responsesModels := map[string]model.ResponseCommandsModel{}

		responsesModels["pending"] = model.ResponseCommandsModel{
			Status: "PENDING",
		}
		responsesModels["protocolError"] = model.ResponseCommandsModel{
			Status:    "ERROR",
			ErrorCode: "protocolError",
		}
		responsesModels["deviceOffline"] = model.ResponseCommandsModel{
			Status:    "ERROR",
			ErrorCode: "deviceOffline",
		}
		responsesModels["safetyShutOff"] = model.ResponseCommandsModel{
			Status:    "ERROR",
			ErrorCode: "safetyShutOff",
		}

		for _, execution := range command.Execution {
			for _, device := range command.Devices {
				ID := device.ID
				logger.Printf(ID)
				subIds := strings.Split(ID, "$")
				deviceID := subIds[0]
				sensorID := subIds[1]
				locationID := device.CustomData["locationId"].(string)
				deviceType := device.CustomData["type"].(string)

				// First check the status
				status, err := mqtt.GetStatus(deviceID)
				if err != nil {
					status = false
				}
				if !status {
					responsesModels["deviceOffline"] = addID(responsesModels["deviceOffline"], ID)
					continue
				}

				// If the device is a thermostat, check the alarm status
				if deviceType == "thermostat" {
					auxValues, err := mqtt.GetAux(deviceID, sensorID)
					if err != nil {
						continue
					}
					alarm, err := strconv.ParseBool(auxValues["alarm"])
					if err == nil && alarm {
						responsesModels["safetyShutOff"] = addID(responsesModels["safetyShutOff"], ID)
						continue
					}
				}

				// Set device state
				if execution.Command == "action.devices.commands.OnOff" {
					newState := execution.Params["on"].(bool)
					if err := mqtt.SetState(locationID, deviceID, sensorID, newState); err == nil {
						responsesModels["pending"] = addID(responsesModels["pending"], ID)
					} else {
						responsesModels["protocolError"] = addID(responsesModels["protocolError"], ID)
					}
					// Thermostat setpoint
				} else if deviceType == "thermostat" && execution.Command == "action.devices.commands.ThermostatTemperatureSetpoint" {
					setpoint := execution.Params["thermostatTemperatureSetpoint"].(float64)
					if err := mqtt.SetAux(locationID, deviceID, sensorID, "setpoint", fmt.Sprintf("%.2f", setpoint)); err == nil {
						responsesModels["pending"] = addID(responsesModels["pending"], ID)
					} else {
						responsesModels["protocolError"] = addID(responsesModels["protocolError"], ID)
					}

				} else if deviceType == "thermostat" && execution.Command == "action.devices.commands.ThermostatSetMode" {
					thermostatMode := execution.Params["thermostatMode"].(string)
					newState := thermostatMode == "heat" || thermostatMode == "on"
					if err := mqtt.SetState(locationID, deviceID, sensorID, newState); err == nil {
						responsesModels["pending"] = addID(responsesModels["pending"], ID)
					} else {
						responsesModels["protocolError"] = addID(responsesModels["protocolError"], ID)
					}

				} else {
					model.ReturnAPIErrorNotSupported(w, dfReq.RequestID)
					return
				}
			}
		}
		// Add response to the list
		for _, responseModel := range responsesModels {
			if responseModel.Ids != nil {
				responseCommands = append(responseCommands, responseModel)
			}
		}
	}

	json.NewEncoder(w).Encode(model.DeviceResponseExecute{
		RequestID: dfReq.RequestID,
		Payload: model.ResponsePayloadExecute{
			Commands: responseCommands,
		},
	})
}
