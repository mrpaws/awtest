# DeploymentByCriteriaModel1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria_type** | **str** | Gets or sets criteria type. Supported values: AppExists &#x3D; 1, AppDoesNotExist &#x3D; 2, FileExists &#x3D; 3, FileDoesNotExist &#x3D; 4, RegistryExists &#x3D; 5, RegistryDoesNotExist &#x3D; 6. | [optional] 
**app_criteria** | [**AppCriteriaModel1_**](AppCriteriaModel1_.md) | Gets or sets application criteria. | [optional] 
**file_criteria** | [**FileCriteriaModel1_**](FileCriteriaModel1_.md) | Gets or sets file criteria. | [optional] 
**registry_criteria** | [**RegistryCriteriaModel1_**](RegistryCriteriaModel1_.md) | Gets or sets registry criteria. | [optional] 
**logical_condition** | **str** | Gets or sets logical condition. Supported values : End &#x3D; 1, And &#x3D; 2, Or &#x3D; 3. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


