# DeviceDetailsExt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** | Gets or sets device identifier. | [optional] 
**device_uuid** | **str** | Gets or sets device UUID. | [optional] 
**udid** | **str** | Gets or sets the device&#39;s unique identifier. | [optional] 
**serial_number** | **str** | Gets or sets device Serial Name. | [optional] 
**device_friendly_name** | **str** | Gets or sets the friendly name. | [optional] 
**organization_group_id** | **int** | Gets or sets the Organization Group ID the device belongs to. | [optional] 
**organization_group_uuid** | **str** | Gets or sets the Organization Group UUID the device belongs to. | [optional] 
**user_name** | **str** | Gets or sets the user name the device is assigned to. | [optional] 
**last_seen** | **datetime** | Gets or sets the time the device last reported any status with AirWatch. | [optional] 
**enrollment_date** | **datetime** | Gets or sets this gives the Date-Time of last enrollment date. | [optional] 
**compliant** | **bool** | Gets or sets a value indicating whether this gives the DevicePolicyCompliance Status of the device. | [optional] 
**asset_number** | **str** | Gets or sets asset Number of the device. | [optional] 
**enrollment_status** | **str** | Gets or sets enrollment Status of device. | [optional] 
**un_enrolled_date** | **datetime** | Gets or sets this gives the Date-Time of Last Unenrollment. | [optional] 
**device_network_info** | [**list[DeviceNetworkInfo]**](DeviceNetworkInfo.md) | Gets or sets network information of the current device. | [optional] 
**products** | [**list[DeviceProduct]**](DeviceProduct.md) | Gets or sets details of the Products, which are assigned to the Current Device. | [optional] 
**smart_groups** | [**list[DeviceSmartGroup]**](DeviceSmartGroup.md) | Gets or sets details of the SmartGroups, which are assigned to the Current Device. | [optional] 
**custom_attributes** | [**list[DeviceCustomAttribute]**](DeviceCustomAttribute.md) | Gets or sets details of the CustomAttributes, which are assigned to the Current Device. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


