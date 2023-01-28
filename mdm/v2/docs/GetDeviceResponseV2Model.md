# GetDeviceResponseV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**udid** | **str** | UDID of the device | [optional] 
**serial_number** | **str** | Serial number of the device | [optional] 
**mac_address** | **str** | MacAddress of the device | [optional] 
**imei** | **str** | Device IMEI hardware identifier | [optional] 
**friendly_name** | **str** | Friendly name of the device | [optional] 
**organization_group_name** | **str** | Device organization group name | [optional] 
**total_storage_bytes** | **str** | Total storage capacity in bytes | [optional] 
**available_storage_bytes** | **str** | Available storage capacity in bytes | [optional] 
**battery_level_percentage** | **str** | Battery level of the iOS device in percentage | [optional] 
**computer_name** | **str** | Desktop name of the device | [optional] 
**supervised** | **bool** | Supervised status of the device | [optional] 
**data_encrypted** | **bool** | Data encryption status | [optional] 
**platform_info** | [**GetPlatformDetailsResponseV2Model**](GetPlatformDetailsResponseV2Model.md) | Contains basic details about the device platform | [optional] 
**carrier_info** | [**GetDeviceCarrierDetailsResponseV2Model**](GetDeviceCarrierDetailsResponseV2Model.md) | Contains carrier details about the device platform | [optional] 
**enrollment_info** | [**GetDeviceEnrollmentDetailsResponseV2Model**](GetDeviceEnrollmentDetailsResponseV2Model.md) | Contains enrollment details of the device | [optional] 
**os_build_version** | **str** | OS build version of the device | [optional] 
**wifi_ssid** | **str** | WiFi SSID which device is connected to | [optional] 
**links** | [**list[Link]**](Link.md) | Gets list of hypermedia link. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


