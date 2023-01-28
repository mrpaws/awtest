# BulkCommandsV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uuids** | **list[str]** | List of Device Uuids. | [optional] 
**unlock_pin** | **int** | Applicable only for macOS devices. Unlock PIN code is required for Lock and DeviceWipe commands. Warning - This device cannot be unlocked remotely and can only be unlocked using 6-digit pin entered. Write this PIN down and store it in a safe place. If you forget your PIN you must contact Apple to unlock your device. | [optional] 
**message** | **str** | Applicable only for macOS devices. Message is optional for Lock Command. Max allowed length is 256 chars. | [optional] 
**sensor_name** | **str** | Applicable only for macOS and Linux platform and it is required for the SyncSensors command. | [optional] 
**rebuild_kernel_cache** | **bool** | If true, the kernel cache is rebuilt during a device restart. If BootstrapTokenAllowedForAuthentication is true in the SecurityInfoResponse. SecurityInfo response, the device requests the Bootstrap Token from the MDM prior to executing this command. This value is available in macOS 11 and later. | [optional] 
**kext_paths** | **list[str]** | If RebuildKernelCache is true, this value specifies the paths to kexts to add to the auxiliary kernel cache since the last kernel cache rebuild. If not present, the system only adds previously-discovered kexts to the kernel cache. This value is available in macOS 11 and later. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


