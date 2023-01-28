# DeviceHealthDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | [**EntityId_**](EntityId_.md) | Gets or sets device Identifier. | [optional] 
**udid** | **str** | Gets or sets device UDID. | [optional] 
**serial_number** | **str** | Gets or sets device Serial Name. | [optional] 
**asset_number** | **str** | Gets or sets device AssetNumber. | [optional] 
**friendly_name** | **str** | Gets or sets device Friendly name. | [optional] 
**organization_group_id** | **int** | Gets or sets id of the Organization Group at which current device is enrolled or registered. | [optional] 
**username** | **str** | Gets or sets enrollemnt Username. | [optional] 
**available_disk_space** | **int** | Gets or sets available free disk space on Device (MB). | [optional] 
**total_memory** | **int** | Gets or sets total memory on device (MB). | [optional] 
**device_network_info** | [**list[DeviceNetworkInfo]**](DeviceNetworkInfo.md) | Gets or sets network information of the current device. | [optional] 
**gps_coordinates** | [**ProductGpsCoordinate_**](ProductGpsCoordinate_.md) | Gets or sets last known GPS coordinate. | [optional] 
**custom_attributes** | [**list[ProductCustomAttribute]**](ProductCustomAttribute.md) | Gets or sets custom Attributes details that are assigned to current device. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


