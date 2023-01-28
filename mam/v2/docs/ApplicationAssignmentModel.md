# ApplicationAssignmentModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smart_group_id** | **int** | Gets or sets the smart group id. | [optional] 
**smart_group_uuid** | **str** | Gets or sets the Smart Group uuid. | [optional] 
**smart_group_name** | **str** | Gets or sets the smart group name. | [optional] 
**push_mode** | **str** | Gets or sets the push mode for the application. | [optional] 
**effective_date** | **datetime** | Gets or sets the effective date time for the Application. | [optional] 
**remove_on_un_enroll** | **str** | Gets or sets a value indicating whether the appslication should be removed on unenrollment. | [optional] 
**application_backup** | **str** | Gets or sets a value indicating whether application backup is enabled. | [optional] 
**auto_update_devices_with_previous_version** | **str** | Gets or sets a value indicating whether the newest version of the app should be pushed to devices that have already downloaded the app. | [optional] 
**per_app_vpn** | **str** | Gets or sets a value indicating whether the per app VPN flag for iOS devices is enabled. | [optional] 
**vpn_profile_id** | **int** | Gets or sets the VPN profile id associated with the application. | [optional] 
**afw_vpn_profile_id** | **int** | Gets or sets the Android For Work VPN profile id associated with the application. | [optional] 
**vpn_profile_uuid** | **str** | Gets or sets the VPN Profile ID associated with the application. | [optional] 
**rank** | **int** | Gets or sets the application rank. | [optional] 
**app_config** | **str** | Gets or sets a value indicating whether custom application configuration keys and values should be sent to the device. | [optional] 
**app_attribute** | **str** | Gets or sets a value indicating whether custom application attribute keys and values should be sent to the device. | [optional] 
**prevent_removal** | **str** | Gets or sets a value indicating whether prevent application removal attribute keys and values should be sent to the device. | [optional] 
**allow_management** | **str** | Gets or sets flag to enable assume management for user installed iOS Apps. | [optional] 
**app_configs** | [**list[ApplicationConfigurationModel]**](ApplicationConfigurationModel.md) | Gets or sets the app configs. | [optional] 
**app_attributes** | [**list[ApplicationConfigurationModel]**](ApplicationConfigurationModel.md) | Gets or sets the app attributes. | [optional] 
**application_transform_ids** | **list[int]** | Gets or sets The application transforms ids attached to the application. | [optional] 
**visible_in_app_catalog** | **bool** | Gets or sets a value indicating whether gets or sets the value whether to display in app catalog. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


