# RepositoryTemplateV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Repository template name. | [optional] 
**user_repository_name** | **str** | User repository name for automatic templates. | [optional] 
**template_type** | **int** | To allow routing of requests via content gateway. | [optional] 
**template_links** | [**list[TemplateLink]**](TemplateLink.md) | Repository template endpoint. | [optional] 
**organization_group_uuid** | **str** | Repository template Organization Group uuid. | [optional] 
**enable_certificate_based_authentication** | **bool** | Flag to enable certificate based authentication. | [optional] 
**access_via** | **str** | To allow routing of requests via content gateway. | [optional] 
**content_gateway_configuration_uuid** | **str** | Content Gateway configuration uuid. | [optional] 
**allow_children** | **bool** | Allow inheritance in repository template. | [optional] 
**permissions** | **list[str]** | Repository template permissions. | [optional] 
**allow_delete** | **bool** | Allow delete. | [optional] 
**view_online_only** | **bool** | Flag to allow view online or offline. | [optional] 
**allow_email** | **bool** | Flag to allow email the repository template. | [optional] 
**allow_third_party_export** | **bool** | Flag to allow repository template export to third party apps. | [optional] 
**allow_to_other_repo_export** | **bool** | Flag to allow repsitory template export to other repository template. | [optional] 
**enable_watermark** | **bool** | Flag to allow watermark. | [optional] 
**allow_printing** | **bool** | Flag to allow printing. | [optional] 
**allow_edit** | **bool** | Flag to allow edit. | [optional] 
**device_ownership** | **str** | Defines the device ownership. | [optional] 
**organization_groups** | **list[str]** | List of Organization Groups assigned to repository template. | [optional] 
**user_groups** | **list[str]** | List of user groups assigned to repository template. | [optional] 
**download_method** | **str** | Defines the content download method. | [optional] 
**download_while_roaming** | **bool** | Flag to allow download while roaming. | [optional] 
**content_required** | **bool** | Flag to mark content is required. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


