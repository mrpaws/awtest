# DeviceResponseV3Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**udid** | **str** | UDID of the device. | [optional] 
**serial_number** | **str** | Serial number of the device. | [optional] 
**mac_address** | **str** | MAC Address of the device. | [optional] 
**imei** | **str** | Device IMEI hardware identifier. | [optional] 
**friendly_name** | **str** | Friendly name of the device. | [optional] 
**device_reported_name** | **str** | Device reported name. | [optional] 
**organization_group_name** | **str** | Device organization group name. | [optional] 
**total_storage_bytes** | **str** | Total storage capacity in bytes. | [optional] 
**available_storage_bytes** | **str** | Available storage capacity in bytes. | [optional] 
**total_physical_memory_bytes** | **str** | Total physical memory capacity in bytes. | [optional] 
**available_physical_memory_bytes** | **str** | Available physical memory capacity in bytes. | [optional] 
**total_external_storage_bytes** | **str** | Total external storage capacity in bytes. | [optional] 
**available_external_storage_bytes** | **str** | Available external storage capacity in bytes. | [optional] 
**battery_level_percentage** | **str** | Battery level of the iOS device in percentage. | [optional] 
**computer_name** | **str** | Desktop name of the device. | [optional] 
**supervised** | **bool** | Supervised status of the device. | [optional] 
**data_encrypted** | **bool** | Data encryption status. | [optional] 
**platform_info** | [**PlatformDetailsResponseV3Model**](PlatformDetailsResponseV3Model.md) | Contains basic details about the device platform. | [optional] 
**carrier_info** | [**DeviceCarrierDetailsResponseV3Model**](DeviceCarrierDetailsResponseV3Model.md) | Contains carrier details about the device platform. | [optional] 
**enrollment_info** | [**DeviceEnrollmentDetailsResponseV3Model**](DeviceEnrollmentDetailsResponseV3Model.md) | Contains enrollment details of the device. | [optional] 
**os_build_version** | **str** | OS build version of the device. | [optional] 
**wifi_ssid** | **str** | WiFi SSID device is connected to. | [optional] 
**last_reboot** | **datetime** | Last reboot time reported by the device in ISO 8601 format. | [optional] 
**security_patch_date** | **datetime** | Security Patch Date reported by the device in ISO 8601 format. | [optional] 
**system_update_received_time** | **datetime** | Pending System Update received time reported in ISO 8601 format. | [optional] 
**is_security_patch_update** | **bool** | Indicates whether Security Patch Update is true when there is a Security Patch update available. | [optional] 
**hardware_device_identifier** | **str** | Hardware Device Identifier for device. | [optional] 
**processor_architecture_name** | **str** | Name of the CPU Architecture the device is using. | [optional] 
**links** | [**list[Link]**](Link.md) | Gets list of hypermedia link. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


