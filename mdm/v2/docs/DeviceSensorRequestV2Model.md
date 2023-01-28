# DeviceSensorRequestV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the device sensor. | 
**description** | **str** | Description of the device sensor. | [optional] 
**platform** | **int** | Platform for which the device sensor will be created. | 
**query_type** | **int** | Query type of the script. | 
**query_response_type** | **int** | Response type of the data. | [optional] 
**organization_group_uuid** | **str** | Organization Group uuid | 
**execution_context** | **int** | Execution context under which the script would be run on device. | [optional] 
**execution_architecture** | **int** | Execution architecture under which the script would be run on device. | [optional] 
**script_data** | **str** | Base64 encoded script to be executed on the device. | 
**timeout** | **int** | Defines timeout for the script execution in seconds. | [optional] 
**script_environment_variables** | [**list[DeviceSensorScriptEnvironmentVariableV1]**](DeviceSensorScriptEnvironmentVariableV1.md) | Key Value pairs for the environment variables used in scripts. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


