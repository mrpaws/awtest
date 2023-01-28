# DeploymentByCriteriaV1Model_

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria_type** | **int** | Gets or sets criteria type. Supported values- AppExists &#x3D; 1, AppDoesNotExist &#x3D; 2, FileExists &#x3D; 3, FileDoesNotExist &#x3D; 4, RegistryExists &#x3D; 5, RegistryDoesNotExist &#x3D; 6. | [optional] 
**app_criteria** | [**AppCriteriaV1Model**](AppCriteriaV1Model.md) | Gets or sets application criteria. | [optional] 
**file_criteria** | [**FileCriteriaV1Model**](FileCriteriaV1Model.md) | Gets or sets file criteria. | [optional] 
**registry_criteria** | [**RegistryCriteriaV1Model**](RegistryCriteriaV1Model.md) | Gets or sets registry criteria. | [optional] 
**logical_condition** | **int** | Gets or sets logical condition. Supported values : End &#x3D; 1, And &#x3D; 2, Or &#x3D; 3. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


