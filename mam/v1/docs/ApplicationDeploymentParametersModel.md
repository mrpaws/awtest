# ApplicationDeploymentParametersModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smart_group_id** | **int** | Gets or sets smart group id. | [optional] 
**assignment_id** | **int** | Gets or sets the assignment entity map IdSmart group id. | [optional] 
**push_mode** | **str** | Gets or sets push mode for the application. | [optional] 
**effective_date** | **datetime** | Gets or sets effective date for  the application. | [optional] 
**remove_on_un_enroll** | **bool** | Gets or sets whether the application should be removed on unenrollment. | [optional] 
**application_backup** | **bool** | Gets or sets whether application backup is enabled. | [optional] 
**auto_update_devices_with_previous_version** | **bool** | Gets or sets whether the newest version of the app should be pushed to devices that have already downloaded the app. | [optional] 
**adaptive_management** | **bool** | Gets or sets whether device should enrolled to get the app - Only applicable for WorkspaceOne. | [optional] 
**is_per_app_vpn_enabled** | **bool** | Gets or sets whether per app vpn flag is enabled. | [optional] 
**vpn_profile_id** | **int** | Gets or sets vpn profile id associated with the application. | [optional] 
**afw_vpn_profile_id** | **int** | Gets or sets the ID of the AFW VPN Profile applicable to the devices in this assignment. | [optional] 
**send_application_config** | **bool** | Gets or sets whether custom application configuration keys and values should be sent to the device. | [optional] 
**whitelisted_domains** | **str** | Gets or sets whiteListed domains for the tunnel server. | [optional] 
**nsx_security_groups** | **int** | Gets or sets security group id for nsx. | [optional] 
**application_configurations** | [**list[ApplicationConfigurationModel]**](ApplicationConfigurationModel.md) | Gets or sets app config entries. | [optional] 
**application_transform_ids** | **list[int]** | Gets or sets application Transforms Ids attached to the application. | [optional] 
**allow_management** | **bool** | Gets or sets flag to enable assume management for user installed iOS Apps. | [optional] 
**mac_os_desired_state_management** | **bool** | Gets or sets flag to enable or disable desired state management for macOS apps. | [optional] 
**requires_approval** | **bool** | Gets or sets a value indicating whether [requires approval]. | [optional] 
**visible_in_app_catalog** | **bool** | Gets or sets a value indicating whether gets or sets the value whether to display in app catalog. | [optional] 
**app_config_blob_id** | **int** | Gets or sets blob ID for the office app configuration values. | [optional] 
**send_application_attributes** | **bool** | Gets or sets whether custom application attributes keys and values should be sent to the app. | [optional] 
**prevent_removal** | **bool** | Gets or sets whether prevent removal application attributes key and value should be sent to the app. | [optional] 
**application_attributes** | [**list[ApplicationConfigurationModel]**](ApplicationConfigurationModel.md) | Gets or sets app attribute entries. | [optional] 
**app_attributes_blob_id** | **int** | Gets or sets blob ID for the application attributes. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


