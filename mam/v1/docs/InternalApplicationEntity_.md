# InternalApplicationEntity_

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | Gets or sets application Name. | [optional] 
**bundle_id** | **str** | Gets or sets package id. | [optional] 
**app_version** | **str** | Gets or sets app version. | [optional] 
**actual_file_version** | **str** | Gets or sets actual file version of the app. | [optional] 
**app_type** | **str** | Gets or sets app type includes Public, Internal, Purchased. | [optional] 
**status** | **str** | Gets or sets application Status can be Active or InActive. | [optional] 
**platform** | **int** | Gets or sets platform is the type of device. ex: Unknown &#x3D; 0, WindowsMobile &#x3D; 1, Apple &#x3D; 2, Android &#x3D; 5,. | [optional] 
**supported_models** | [**ApplicationSupportedModels1_**](ApplicationSupportedModels1_.md) | Gets or sets collection of supported Application Models. | [optional] 
**assignment_status** | **str** | Gets or sets assignment status. Can be Assigned or Unassigned. | [optional] 
**application_size** | **str** | Gets or sets application size. | [optional] 
**category_list** | [**ApplicationCategories1_**](ApplicationCategories1_.md) | Gets or sets represents the various categories that are associated to an application. Represented by the category Id and Description. | [optional] 
**comments** | **str** | Gets or sets comments of the application. | [optional] 
**is_reimbursable** | **bool** | Gets or sets a value indicating whether indicates whether the particular application can be reimbursed. | [optional] 
**application_url** | **str** | Gets or sets download URL for the application. | [optional] 
**application_source** | **int** | Gets or sets the application source. | [optional] 
**location_group_id** | **int** | Gets or sets organization Group Id. | [optional] 
**root_location_group_name** | **str** | Gets or sets root Location Group Name. | [optional] 
**organization_group_uuid** | **str** | Gets or sets organization Group UUID. | [optional] 
**external_id** | **str** | Gets or sets external Store Id. | [optional] 
**large_icon_uri** | **str** | Gets or sets large Icon URL. | [optional] 
**medium_icon_uri** | **str** | Gets or sets medium Icon URL. | [optional] 
**small_icon_uri** | **str** | Gets or sets small Icon URL. | [optional] 
**push_mode** | **int** | Gets or sets push Mode for the application - Auto, On-Demand. | [optional] 
**app_rank** | **int** | Gets or sets application Rank. | [optional] 
**assigned_device_count** | **int** | Gets or sets number of device to which current application is Assigned. | [optional] 
**installed_device_count** | **int** | Gets or sets number of device on which current application is Installed. | [optional] 
**not_installed_device_count** | **int** | Gets or sets number of device to which current application is Assigned, but not installed. | [optional] 
**msi_deployment_parameters** | [**MsiDeploymentParamModel1_**](MsiDeploymentParamModel1_.md) | Gets or sets msi deployment param model. This is valid only for MSI files when Software Distribution is not enabled. | [optional] 
**files_options** | [**ApplicationFilesOptionsModel1_**](ApplicationFilesOptionsModel1_.md) | Gets or sets application files options. | [optional] 
**content_gateway_id** | **int** | Gets or sets content Gateway Id. | [optional] 
**icon_file_name** | **str** | Gets or sets the name of the uploadeed icon file. | [optional] 
**application_file_name** | **str** | Gets or sets the name of the uploaded application file. | [optional] 
**metadata_file_name** | **str** | Gets or sets the name of the uploaded metadata file. | [optional] 
**version_identifier** | **str** | Gets or sets the version identifier of the application. | [optional] 
**icon_blob_uu_id** | **str** | Gets or sets uuid of the uploaded icon blob data. | [optional] 
**ear_app_update_mode** | **int** | Gets or sets EAR App update preference. | [optional] 
**id** | [**EntityId_**](EntityId_.md) |  | [optional] 
**uuid** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


