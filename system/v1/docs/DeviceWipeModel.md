# DeviceWipeModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The unique identifier of the server action uuid. | 
**device_uuid** | **str** | The unique identifier of the device that the wipe action was scheduled for. | 
**device_type** | **str** | Type of the device. | 
**event_date** | **datetime** | The time stamp of the device wipe event. | 
**device_name** | **str** | The friendly name of the device that the wipe action was scheduled for. | 
**status** | **str** | The status of the device wipe command. | 
**wipe_type** | **str** | The wipe action type. | 
**last_seen** | **datetime** | The timestamp of when the device was last seen. | 
**device_up** | **bool** | A flag indicating whether the device has checked in within the device timeout period. | [optional] 
**organization_group_uuid** | **str** | The unique identifier of the device&#39;s organization group. | 
**organization_group** | **str** | The device&#39;s organization group. | 
**user** | **str** | The enrollment user of the device that the wipe action was scheduled for. | [optional] 
**source** | **str** | The source of the device wipe action. | 
**ownership** | **str** | The display name of the device ownership type. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


