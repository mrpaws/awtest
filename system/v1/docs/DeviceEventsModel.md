# DeviceEventsModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment** | **bool** | Gets or sets a value indicating whether indicates whether an outbound event has been triggered to set the enrollment status of a device. | [optional] 
**unenrolled_enterprise_wipe** | **bool** | Gets or sets a value indicating whether indicates whether an outbound event has been triggered to unenroll and perform an enterprise wipe on a device. | [optional] 
**wipe** | **bool** | Gets or sets a value indicating whether indicates whether an outbound event has been triggered to wipe a device. | [optional] 
**compromised_status_change** | **bool** | Gets or sets a value indicating whether indicates whether an outbound event has been triggered for a change in the setting of a compromised device. | [optional] 
**delete** | **bool** | Gets or sets a value indicating whether indicates whether an outbound event has been triggered for a deletion of the device. | [optional] 
**compliance_status_change** | **bool** | Gets or sets a value indicating whether indicates whether an outbound event has changed the compliance status for a device. | [optional] 
**check_out_check_in** | **bool** | Gets or sets a value indicating whether indicates whether an outbound event has been triggered for device checked in and checked out by user. | [optional] 
**device_attributes** | [**DeviceAttributesModel**](DeviceAttributesModel.md) | Gets or sets device attribute properties that have been changed. These properties are triggered by an outbound event call. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


