# DeviceSensorAssignmentResponseV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Assignment UUID | [optional] 
**smart_group_count** | **int** | The total count of smart groups associated with the assignment. | [optional] 
**ranking** | **int** | Ranking of the assignment. 1 specifies highest ranking. | [optional] 
**name** | **str** | Name of the device sensor assignment. | [optional] 
**assigned_smart_groups** | [**list[DeviceSensorAssignedSmartGroupV1Model]**](DeviceSensorAssignedSmartGroupV1Model.md) | Assigned smart groups to the device sensor. | [optional] 
**trigger_type** | **int** | Trigger type for script execution. SCHEDULEANDEVENT trigger type is applicable only for macOS platform. Linux platform supports only SCHEDULE trigger type. | [optional] 
**event_triggers** | **list[int]** | Event triggers defining the trigger for the data collection. The NETWORK_CHANGE trigger is applicable only for macOS platform. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


