# DeviceUpdateCountDeviceStatusV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_complete** | **int** | The count of devices that have completed the download of the update but are not yet on the specified version | [optional] 
**install_complete** | **int** | The count of devices that have completed installation and are on or above the specified version | [optional] 
**not_started** | **int** | The count of devices that haven&#39;t started the download/install of the specified update | [optional] 
**idle** | **int** | The count of devices where no action is currently being taken on the update | [optional] 
**downloading** | **int** | The count of devices where the update is currently downloading | [optional] 
**download_failed** | **int** | The count of devices where the download has failed for some reason | [optional] 
**download_requires_computer** | **int** | The count of devices where download could not complete because the device must be connected to a computer to download the update (iOS only) | [optional] 
**download_insufficient_space** | **int** | The count of devices where download failed because there is not enough space to download the update | [optional] 
**download_insufficient_power** | **int** | The count of devices where download failed because there is not enough power to download the update | [optional] 
**download_insufficient_network** | **int** | The count of devices where download failed because there is insufficient network capacity to download the update | [optional] 
**installing** | **int** | The count of devices where the update is being installed | [optional] 
**install_insufficient_space** | **int** | The count of devices where there is not enough space to install the update | [optional] 
**install_insufficient_power** | **int** | The count of devices where there is not enough power to install the update | [optional] 
**install_phone_call_in_progress** | **int** | The count of devices where installation has been rejected because a phone call is in progress | [optional] 
**install_failed** | **int** | The count of devices where installation has failed for an unspecified reason | [optional] 
**not_eligible** | **int** | The count of devices where they are not eligible to receive the update | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


