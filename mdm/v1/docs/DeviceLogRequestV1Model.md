# DeviceLogRequestV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_log_source** | **int** | Represents the source of the device logs. Possible values &#x3D; [Agent, System, Network] | [optional] 
**device_log_level** | **int** | Level of the logs requested from the device. Possible values &#x3D; [Error, Warning, Information, Debug, Verbose]. Not applicable for \&quot;Network\&quot; log source. | [optional] 
**device_log_duration** | **int** | Duration of the logs in minutes. Only positive integer values allowed with upper limit of 720. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


