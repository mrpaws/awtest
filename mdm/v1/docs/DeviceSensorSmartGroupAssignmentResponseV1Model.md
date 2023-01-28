# DeviceSensorSmartGroupAssignmentResponseV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** | Total number of items count sent for processing. | [optional] 
**accepted_items** | **int** | Number of items accepted for processing. | [optional] 
**failed_items** | **int** | Number of items not accepted for processing. | [optional] 
**activity_id** | **str** | The activity id associated with the response | [optional] 
**failed_sensors** | [**list[DeviceSensorSmartGroupAssignmentFailedResponseV1Model]**](DeviceSensorSmartGroupAssignmentFailedResponseV1Model.md) | A list of failed sensors with error details. | [optional] 
**failed_smart_groups** | [**list[DeviceSensorSmartGroupAssignmentFailedResponseV1Model]**](DeviceSensorSmartGroupAssignmentFailedResponseV1Model.md) | A list of failed smart groups with error details. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


