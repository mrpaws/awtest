# PurchasedApplicationEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | Gets or sets application Name. | [optional] 
**application_size** | **str** | Gets or sets application size. | [optional] 
**application_url** | **str** | Gets or sets itunes URL of the application. | [optional] 
**assignments** | [**list[PurchasedAppAssignment]**](PurchasedAppAssignment.md) | Gets or sets application Assignment List. | [optional] 
**bundle_id** | **str** | Gets or sets package id. | [optional] 
**external_id** | **str** | Gets or sets iD for an external application store (i.e. iTunes ID). | [optional] 
**is_reimbursable** | **bool** | Gets or sets a value indicating whether determines if the app is reimbursable or reimbursable not defined. | [optional] 
**large_icon_uri** | **str** | Gets or sets uRL to an externally hosted icon - large size. | [optional] 
**medium_icon_uri** | **str** | Gets or sets uRL to an externally hosted icon - medium size. | [optional] 
**small_icon_uri** | **str** | Gets or sets uRL to an externally hosted icon - small size. | [optional] 
**location_group_id** | **int** | Gets or sets location Group id where the application is created. | [optional] 
**platform** | **int** | Gets or sets device Type supported by the application. | [optional] 
**redeemable_codes** | [**PurchasedAppRedeemableCodesDetails_**](PurchasedAppRedeemableCodesDetails_.md) | Gets or sets redeemable Codes Details. | [optional] 
**managed_distribution** | [**PurchasedAppManagedDistributionDetials_**](PurchasedAppManagedDistributionDetials_.md) | Gets or sets managed Distribution Details. | [optional] 
**deployment** | [**PurchasedAppDeploymentDetails_**](PurchasedAppDeploymentDetails_.md) | Gets or sets deployment Details. | [optional] 
**app_version** | **str** | Gets or sets app version. | [optional] 
**actual_file_version** | **str** | Gets or sets actual file version of the app. | [optional] 
**app_type** | **str** | Gets or sets app type (public/purchased/internal). | [optional] 
**status** | **str** | Gets or sets status to indicate whether app is active or not. | [optional] 
**supported_models** | [**ApplicationSupportedModels_**](ApplicationSupportedModels_.md) | Gets or sets device Model supported by the app. | [optional] 
**assignment_status** | **str** | Gets or sets assignemt status. | [optional] 
**comments** | **str** | Gets or sets short comments on the app. | [optional] 
**is_auto_update_enabled** | **bool** | Gets or sets a value indicating whether is auto update enabled for the particular device based VPP application. | [optional] 
**categories** | **list[str]** | Gets or sets get or set the Application Categories. | [optional] 
**id** | [**EntityId_**](EntityId_.md) |  | [optional] 
**uuid** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


