# DeviceWipeV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_activation_key** | **bool** | If set to true, and Activation Lock is enabled on a supervised iOS device, Activation lock will be cleared. | [optional] 
**disallow_proximity_setup** | **bool** | If set to true, the Proximity Setup screen will be skipped in the Setup Assistant on the next reboot of the device | [optional] 
**preserve_data_plan** | **bool** | If set to true, and a data plan exists on the device, that data plan will be preserved after the device is erased | [optional] 
**wipe_type** | **str** | Type of wipe selected i.e. WIPE, WIPE_PERSIST_PROVISIONED_DATA, WIPE_PROTECTED, WIPE_PERSIST_USER_DATA | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


