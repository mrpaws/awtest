# DeviceSensorUpdateV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the device sensor. | [optional] 
**platform** | **int** | Platform for which the device sensor will be created. | [optional] 
**query_type** | **int** | Query type of the script. | [optional] 
**trigger_type** | **int** | Trigger type of the script. | [optional] 
**execution_context** | **int** | Execution context under which the script would be run on device. | [optional] 
**execution_architecture** | **int** | Execution architecture under which the script would be run on device. | [optional] 
**script_data** | **str** | Script to be executed on device. | [optional] 
**timeout** | **int** | Defines timeout for the script execution in seconds. | [optional] 
**event_trigger** | **list[int]** | Event triggers defining the trigger for the data collection. | [optional] 
**schedule_trigger** | **int** | Schedule trigger(in hours) defining the trigger for the data collection. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


