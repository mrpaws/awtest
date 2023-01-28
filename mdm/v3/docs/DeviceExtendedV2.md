# DeviceExtendedV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**udid** | **str** | UDID of the device. | [optional] 
**serial_number** | **str** | Serial number of the device. | [optional] 
**imei** | **str** | IMEI hardware identifier. | [optional] 
**eas_ids** | [**EasIds**](EasIds.md) | Unique identifiers for devices mail client. | [optional] 
**asset_number** | **str** | Asset number of the device. | [optional] 
**device_friendly_name** | **str** | Device friendly name. | [optional] 
**device_reported_name** | **str** | Device reported name. | [optional] 
**organization_group_uuid** | **str** | UUID of the organization group. | [optional] 
**organization_group_name** | **str** | Organization group name the device is enrolled to. | [optional] 
**enrollment_user_name** | **str** | Name of the user the device is enrolled under. | [optional] 
**enrollment_user_uuid** | **str** | UUID of the user the device is enrolled under. | [optional] 
**enrollment_user_email_address** | **str** | E-mail address of the user the device is enrolled under. | [optional] 
**ownership** | **int** | Ownership type of the device. | [optional] 
**platform_name** | **str** | Name of the platform. | [optional] 
**device_type** | **int** | Type of the device. | [optional] 
**model_identifier** | **str** | Device model identifier. | [optional] 
**model** | **str** | Model name of the device. | [optional] 
**operating_system** | **str** | Operating system of the device. | [optional] 
**last_seen** | **datetime** | Time the device last reported any status. | [optional] 
**enrollment_status** | **int** | Enrollment status of the device. | [optional] 
**compliance_status** | **int** | Compliance status of the device. | [optional] 
**compromised_status** | **bool** | Compromised status of the device. | [optional] 
**last_enrolled_on** | **datetime** | This gives the Date-Time of last enrollment date. | [optional] 
**last_compliance_check_on** | **datetime** | This gives the Date-time of when the last compliance check was performed. | [optional] 
**last_compromised_check_on** | **datetime** | This gives the Date-time of when the last compromised data was received. | [optional] 
**is_supervised** | **bool** | Supervised status of the device. | [optional] 
**is_remote_management_enabled** | **str** | Remote management enabled status of the device. | [optional] 
**data_encryption_yn** | **str** | Data encryption status of the device. | [optional] 
**ac_line_status** | **int** | AC line status of the device. | [optional] 
**virtual_memory** | **int** | Virtual memory of the device. | [optional] 
**oem_info** | **str** | Name of the device manufacturer. | [optional] 
**device_capacity** | **int** | Device capacity. | [optional] 
**available_device_capacity** | **int** | Available device capacity. | [optional] 
**last_system_sample_time** | **datetime** | Last System Sample time of the device. | [optional] 
**is_device_dnd_enabled** | **bool** | This gives information about whether the device is in do not disturb mode or not. | [optional] 
**is_device_locator_enabled** | **bool** | This gives information about whether the device locator is enabled or not. | [optional] 
**is_cloud_backup_enabled** | **bool** | This gives information about whether the device cloud backup is enabled or not. | [optional] 
**is_activation_lock_enabled** | **bool** | This gives information about whether the device activation lock is enabled or not. | [optional] 
**is_network_tethered** | **bool** | This gives information about whether the iOS device is network tethered or not. | [optional] 
**battery_level** | **str** | This gives information about the battery level of the iOS device. | [optional] 
**last_network_lan_sample_time** | **datetime** | Last Network LAN Sample time of the device. | [optional] 
**last_bluetooth_sample_time** | **datetime** | Last Bluetooth Sample time of the device. | [optional] 
**managed_by** | **int** | Device managed by. | [optional] 
**data_protection_status** | **int** | Data protection status of the user the device belongs to. | [optional] 
**processor_architecture** | **int** | Information about the processor Architecture reported by the device. | [optional] 
**os_build_version** | **str** | OS build version of the device. | [optional] 
**wifi_ssid** | **str** | WiFi SSID the device is connected to. | [optional] 
**device_cellular_network_info** | [**list[DeviceCellularInfoModelV2]**](DeviceCellularInfoModelV2.md) | Device cellular network information. | [optional] 
**device_network_info** | [**list[DeviceNetworkInfoV2]**](DeviceNetworkInfoV2.md) | Network information of the device. | [optional] 
**time_zone** | **str** | Time Zone in Internet Assigned Numbers Authority (IANA) data base name format. | [optional] 
**compliance_summary** | [**DeviceComplianceSearchResultV2Model**](DeviceComplianceSearchResultV2Model.md) | The compliance details of a device including the overall compliance status and a list of MDM compliance policy information. | [optional] 
**id** | [**EntityId_**](EntityId_.md) |  | [optional] 
**uuid** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

