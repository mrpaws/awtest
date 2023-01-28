# DeploymentByCriteriaApiModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria_type** | **str** | Gets or sets criteria type. Supported values- AppExists, AppDoesNotExist, FileExists, FileDoesNotExist, RegistryExists, RegistryDoesNotExist. | [optional] 
**app_criteria** | [**AppCriteriaApiModel_**](AppCriteriaApiModel_.md) | Gets or sets application criteria. | [optional] 
**file_criteria** | [**FileCriteriaApiModel_**](FileCriteriaApiModel_.md) | Gets or sets file criteria. | [optional] 
**registry_criteria** | [**RegistryCriteriaApiModel_**](RegistryCriteriaApiModel_.md) | Gets or sets registry criteria. | [optional] 
**logical_condition** | **str** | Gets or sets logical condition. Supported values : End, And, Or. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


