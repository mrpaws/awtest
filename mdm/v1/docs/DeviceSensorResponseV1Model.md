# DeviceSensorResponseV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the device sensor. | [optional] 
**description** | **str** | Description of the device sensor. | [optional] 
**organization_group_name** | **str** | Organization group name the device sensor is managed by. | [optional] 
**is_read_only** | **bool** | Specifies if the sensor is read only with respect to the current organization group. | [optional] 
**organization_group_uuid** | **str** | Identifier of the organization group. | [optional] 
**platform** | **int** | Platform for which the device sensor will be created. | [optional] 
**query_type** | **int** | Query type of the script. | [optional] 
**query_response_type** | **int** | Response type of the data. | [optional] 
**trigger_type** | **int** | Trigger type of the script. | [optional] 
**execution_context** | **int** | Execution context under which the script would be run on device. | [optional] 
**execution_architecture** | **int** | Execution architecture under which the script would be run on device. | [optional] 
**script_data** | **str** | Script to be executed on device. | [optional] 
**timeout** | **int** | Defines timeout(in seconds) for the script execution. | [optional] 
**event_trigger** | **list[int]** | Event triggers defining the trigger for the data collection. | [optional] 
**schedule_trigger** | **int** | Schedule trigger(in hours) defining the trigger for the data collection. | [optional] 
**assigned_smart_groups** | [**list[DeviceSensorAssignedSmartGroupV1Model]**](DeviceSensorAssignedSmartGroupV1Model.md) | Assigned smart groups to the device sensor. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


