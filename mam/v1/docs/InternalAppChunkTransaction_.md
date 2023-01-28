# InternalAppChunkTransaction_

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Gets or sets transactionId of the uploaded chunk. | [optional] 
**blob_id** | **int** | Gets or sets id of the uploaded blob data. | [optional] 
**device_type** | **int** | Gets or sets Device Type. Supported values: Apple &#x3D; 2, Android &#x3D; 5, WinRT &#x3D; 12, AppleOSX &#x3D; 10, AppleTv &#x3D; 14, WindowsPhone8 &#x3D; 11. | [optional] 
**application_name** | **str** | Gets or sets application Name. | [optional] 
**supported_models** | [**ApplicationSupportedModels1_**](ApplicationSupportedModels1_.md) | Gets or sets model. | [optional] 
**push_mode** | **int** | Gets or sets push mode of the application (Required). Supported Values: Auto, OnDemand. | [optional] 
**description** | **str** | Gets or sets description of the application. | [optional] 
**support_email** | **str** | Gets or sets support email. | [optional] 
**support_phone** | **str** | Gets or sets support Phone number. | [optional] 
**developer** | **str** | Gets or sets developer Name. | [optional] 
**developer_email** | **str** | Gets or sets email address of developer. | [optional] 
**developer_phone** | **str** | Gets or sets phone number of developer. | [optional] 
**auto_update_version** | **bool** | Gets or sets a value indicating whether auto update version in case of Ondemand mode. | [optional] 
**location_group_id** | **int** | Gets or sets locationGroupId where the application will be created. | [optional] 
**enable_provisioning** | **bool** | Gets or sets a value indicating whether flag to indicate Application will be used for Product Provisioning. Valid values: true, false. | [optional] 
**upload_via_link** | **bool** | Gets or sets a value indicating whether gets or Sets the Value indicating if the blob was uploaded as a link. | [optional] 
**bundle_id** | **str** | Gets or Sets the Value indicating the Application Bundle Id. | [optional] 
**actual_file_version** | **str** | Gets or Sets the Value indicating the Actual File Version of the app. | [optional] 
**app_version** | **str** | Gets or sets app Version. | [optional] 
**build_version** | **str** | Gets or sets the build version. | [optional] 
**file_name** | **str** | Gets or sets name of the Application file along with its extension. | [optional] 
**supported_processor_architecture** | **str** | Gets or sets supported Processor Architecture. Ex: x86, x64. This is valid only for MSI, ZIP, EXE files with software distribution. | [optional] 
**msi_deployment_param_model** | [**MsiDeploymentParamModel1_**](MsiDeploymentParamModel1_.md) | Gets or sets msi deployment param model. This is valid only for MSI files when Software Distribution is not enabled. | [optional] 
**is_dependency_file** | **bool** | Gets or sets a value indicating whether indicates whether uploaded file is a dependency file. | [optional] 
**deployment_options** | [**ApplicationDeploymentOptionsModel1_**](ApplicationDeploymentOptionsModel1_.md) | Gets or sets application deployment options for software distribution. | [optional] 
**files_options** | [**ApplicationFilesOptionsModel1_**](ApplicationFilesOptionsModel1_.md) | Gets or sets application files options. | [optional] 
**carry_over_assignments** | **bool** | Gets or sets a value indicating whether should Assignment Be Carried Over From Older Version Of App.  The default value is true to not break existing contracts. | [optional] 
**icon_blob_uu_id** | **str** | Gets or sets uuid of the uploaded icon blob data. | [optional] 
**application_source** | **int** | Gets or sets the internal application source. Supported Values- AirWatch &#x3D; 1, AndroidWork &#x3D; 2, WindowsPhoneMarketPlace &#x3D; 3, WindowsStore &#x3D; 4, WindowsBusinessStore &#x3D; 5, AndroidAvenger &#x3D; 6, Boxer &#x3D; 7, EnterpriseAppRepository &#x3D; 8. | [optional] 
**criticality** | **int** | Gets or sets the internal application criticality. Known usage is, Flexera SVM sets this for vulnerable apps. Supported Values- NONE, LESS, MODERATE, HIGH, EXTREME. | [optional] 
**category_list** | [**ApplicationCategories1_**](ApplicationCategories1_.md) | Gets or sets the various categories that are associated to an application. Represented by the category Id and Description. | [optional] 
**ear_app_update_mode** | **int** | Gets or sets a EAR app update preference. Supported Values: None &#x3D; 0, Notify &#x3D; 1, AutoUpdate &#x3D; 2. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


