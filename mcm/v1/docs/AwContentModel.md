# AwContentModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 
**content_id** | **str** | The Unique Identifier for the File. | [optional] 
**name** | **str** | Content name. | [optional] 
**description** | **str** | Description of the file. | [optional] 
**mime_type** | **str** | Mime type of the file. | [optional] 
**is_active** | **bool** | Active status of file. | [optional] 
**importance** | **str** | Content importance value. | [optional] 
**location_group_id** | **int** | Content locationgroupId. | [optional] 
**created_on** | **datetime** | The creation date of content. | [optional] 
**created_by** | **str** | Content created by user. | [optional] 
**modified_on** | **datetime** | Content modified on datetime. | [optional] 
**modified_by** | **str** | Content created by user. | [optional] 
**categories** | [**list[SearchCategoryModel]**](SearchCategoryModel.md) | Categories for the file. | [optional] 
**content_version** | [**AwContentVersionModel**](AwContentVersionModel.md) | Content version object. | [optional] 
**security_settings** | [**SecuritySettingsModel**](SecuritySettingsModel.md) | Security settings object. | [optional] 
**deployment_settings** | [**DeploymentSettingsModel**](DeploymentSettingsModel.md) | Deployment settings object. | [optional] 
**assignment_settings** | [**AssignmentSettingsModel**](AssignmentSettingsModel.md) | Assignment settings object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


