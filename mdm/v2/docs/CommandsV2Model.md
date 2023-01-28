# CommandsV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_wipe** | [**DeviceWipeV2Model**](DeviceWipeV2Model.md) | Gets or sets DeviceWipe model | [optional] 
**work_passcode** | **bool** | If set to true then Work Profile side passcode will be cleared on the device. | [optional] 
**allow_pin_at_startup** | **bool** | If set to true then Allow pin at Startup will be enabled for Device Owner Android devices. | [optional] 
**esim_url** | **str** | The carrier&#39;s eSIM server URL to query for iOS 13 (refresh-esim). | [optional] 
**unlock_pin** | **int** | Applicable only for macOS devices. Unlock PIN code is required for Lock and DeviceWipe commands. Warning - This device cannot be unlocked remotely and can only be unlocked using 6-digit pin entered. Write this PIN down and store it in a safe place. If you forget your PIN you must contact Apple to unlock your device. | [optional] 
**message** | **str** | Applicable only for macOS devices. Message is optional for Lock Command. Max allowed length is 256 chars. | [optional] 
**managed_apple_id** | **str** | The username indicating the user to be deleted on a shared Apple device. | [optional] 
**sensor_names** | **list[str]** | The list of sensor names assigned to the device. Applicable only for macOS and Linux platform and it is required for the SyncSensors command. | [optional] 
**reboot_count** | **int** | Number of reboots the BitLocker encryption on the operating system volume is suspended for (value should be between 1 and 15). | [optional] 
**device_restart** | [**DeviceRestartV2Model**](DeviceRestartV2Model.md) | The DeviceRestart command options. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


