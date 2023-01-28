# OSUpdateModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_key** | **str** | The unique product key of the update | [optional] 
**human_readable_name** | **str** | The common name of the update | [optional] 
**product_name** | **str** | The product name of the update | [optional] 
**version** | **str** | The version of the update | [optional] 
**build** | **str** | The build number of the update | [optional] 
**is_preview** | **bool** | Preview or beta version of the update | [optional] 
**download_size** | **float** | Storage size needed to download the software update. Floating point number of bytes. | [optional] 
**install_size** | **float** | Storage size needed to install the software update. Floating point number of bytes. | [optional] 
**is_critical** | **bool** | Set to true if this update is considered critical. Defaults to false. | [optional] 
**is_configuration_data_update** | **bool** | Set to true if this is an update to a configuration file. Defaults to false (macOS only). | [optional] 
**is_firmware_update** | **bool** | Set to true if this is an update to firmware. Defaults to false (macOS only). | [optional] 
**restart_required** | **bool** | Set to true if the device restarts after this update is installed. Defaults to false. | [optional] 
**allows_install_later** | **bool** | Set to true if the update is eligible for InstallLater. Defaults to true. | [optional] 
**app_identifiers_to_close** | **list[str]** | Each entry represents an app identifier that is closed to install this update (macOS only). | [optional] 
**device_update_name** | **str** | The name of the device update | [optional] 
**release_date** | **datetime** | Indicates the release date of the corresponding device update | [optional] 
**expiation_date** | **datetime** | Indicates the expiration date of the corresponding device update | [optional] 
**download_percent_complete** | **float** | Indicates the percentage of download that is complete. Floating point number (0.0 to 1.0) | [optional] 
**status** | **str** | Indicates the status of the update | [optional] 
**sample_time** | **datetime** | Indicates the sample time of the update | [optional] 
**status_time** | **datetime** | Indicates the status time of the device update | [optional] 
**device_update_version** | **str** | Indicates the version for iOS device updates | [optional] 
**device_update_uuid** | **str** | Indicates update UUID for corresponding iOS device update | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


