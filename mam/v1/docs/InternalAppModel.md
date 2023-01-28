# InternalAppModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | Gets or sets the name of the application. | [optional] 
**app_id** | **str** | Gets or sets the bundle id of the app. | [optional] 
**actual_file_version** | **str** | Gets or sets the actual file version of the app. | [optional] 
**build_version** | **str** | Gets or sets the build version of the app. | [optional] 
**airwatch_app_version** | **str** | Gets or sets airWatch internal application version. | [optional] 
**status** | **str** | Gets or sets status of the App. | [optional] 
**managed_by** | **str** | Gets or sets the managed by Organization Group of the app. | [optional] 
**managed_by_uuid** | **str** | Gets or sets managed By Organization Group Uuid. | [optional] 
**app_provisioning_profile_uuid** | **str** | Gets or sets app Provisioning UUID. | [optional] 
**assume_management_of_user_installed_app** | **str** | Gets or sets a value indicating whether the management of user installed apps should be assumed. | [optional] 
**platform** | **str** | Gets or sets the platform. | [optional] 
**supported_models** | [**list[ApplicationSupportedModelsModel]**](ApplicationSupportedModelsModel.md) | Gets or sets The supported models of the app. | [optional] 
**minimum_operating_system** | **str** | Gets or sets minimum Operating System Version of the application. | [optional] 
**app_size_in_kb** | **int** | Gets or sets the size of the application in kilo bytes. | [optional] 
**category_list** | [**list[ApplicationCategoriesModel]**](ApplicationCategoriesModel.md) | Gets or sets the application category list. | [optional] 
**comments** | **str** | Gets or sets the comments for the application. | [optional] 
**application_url** | **str** | Gets or sets the URL of the application. | [optional] 
**sdk** | **str** | Gets or sets A value indicating whether the application uses AirWatch Software Development Kit. | [optional] 
**sdk_profile_id** | **int** | Gets or sets the SDK profile id of the app if it uses SDK Profile. | [optional] 
**sdk_profile_uuid** | **str** | Gets or sets sdk Profile Uuid of the App if it uses SDK Profile. | [optional] 
**devices_assigned_count** | **int** | Gets or sets the number of devices to which current application is Assigned. | [optional] 
**devices_installed_count** | **int** | Gets or sets devices on which current application is installed. | [optional] 
**devices_not_installed_count** | **int** | Gets or sets number of devices to which current application is assigned, but not installed. | [optional] 
**rating** | **int** | Gets or sets user rating of the app. | [optional] 
**change_log** | **str** | Gets or sets the change log for the application. | [optional] 
**renewal_date** | **datetime** | Gets or sets expiration date of the Device Provisioning Profile. | [optional] 
**assignments** | [**list[ApplicationAssignmentModel]**](ApplicationAssignmentModel.md) | Gets or sets app configs. | [optional] 
**excluded_smart_group_ids** | **list[int]** | Gets or sets the Smart group Ids to be excluded from receiving the application. | [optional] 
**excluded_smart_group_guids** | **list[str]** | Gets or sets the Unique Guid values of the excluded smart groups. | [optional] 
**msi_deployment_parameters** | [**MsiDeploymentParameterModel_**](MsiDeploymentParameterModel_.md) | Gets or sets msi deployment param model. This is valid only for MSI files when Software Distribution is not enabled. | [optional] 
**deployment_options** | [**AppDeploymentOptionsModel_**](AppDeploymentOptionsModel_.md) | Gets or sets application deployment options for software distribution. | [optional] 
**files_options** | [**AppFilesOptionsModel_**](AppFilesOptionsModel_.md) | Gets or sets application files options. | [optional] 
**mac_os_software_deployment_summary** | [**MacOsSoftwareDeploymentSummaryModel_**](MacOsSoftwareDeploymentSummaryModel_.md) | Gets or sets macOs software package summary. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


