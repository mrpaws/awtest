# DeviceSensorAssignmentRequestV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the device sensor assignment. | 
**smart_group_uuids** | **list[str]** | The list of smart group UUIDs assigned to the sensor | [optional] 
**trigger_type** | **int** | Trigger type for script execution. SCHEDULEANDEVENT trigger type is applicable only for macOS platform. Linux platform supports only SCHEDULE trigger type. | [optional] 
**event_triggers** | **list[int]** | Event triggers defining the trigger for the data collection. The NETWORK_CHANGE trigger is applicable only for macOS platform. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


