# PurchasedApplicationModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_by** | **int** | Gets or sets id of the organization group manages the app. | [optional] 
**orders** | [**PurchasedAppOrdersModel_**](PurchasedAppOrdersModel_.md) | Gets or sets order Details [Applicable for PurchasedOnly Apps]. | [optional] 
**licenses** | [**PurchasedAppOrdersModel_**](PurchasedAppOrdersModel_.md) | Gets or sets licenses Details [Applicable for LicensedOnly Apps]. | [optional] 
**assignments** | [**list[PurchasedAppAssignmentModel]**](PurchasedAppAssignmentModel.md) | Gets or sets assignment Details. | [optional] 
**deployment** | [**PurchasedAppDeploymentModel_**](PurchasedAppDeploymentModel_.md) | Gets or sets deployment Details. | [optional] 
**send_application_configuration** | **bool** | Gets or sets a value indicating whether whether send application configuration. | [optional] 
**app_config_list** | [**list[ApplicationConfigurationModel]**](ApplicationConfigurationModel.md) | Gets or sets app configuration details. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


