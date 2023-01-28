# ContentRepositoryV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Repository name. | [optional] 
**repository_type** | **str** | Repository type. | [optional] 
**link** | **str** | Repository link. | [optional] 
**organization_group_uuid** | **str** | Repository Organization Group Uuid. | [optional] 
**enable_certificate_based_authentication** | **bool** | Flag to enable certificate based authentication. | [optional] 
**access_via** | **str** | To allow routing of requests via content gateway. | [optional] 
**content_gateway_configuration_uuid** | **str** | Content gateway configuration uuid. | [optional] 
**allow_children** | **bool** | Allow inheritance in repository. | [optional] 
**permissions** | **list[str]** | Repository permissions. | [optional] 
**allow_delete** | **bool** | Allow delete. | [optional] 
**authentication_type** | **str** | Repository authentication type. | [optional] 
**user_name** | **str** | Authentication username if authentication set to user. | [optional] 
**password** | **str** | Authentication password if authentication set to user. | [optional] 
**view_online_only** | **bool** | Flag to allow view online or offline. | [optional] 
**allow_email** | **bool** | Flag to allow email the repository. | [optional] 
**allow_third_party_export** | **bool** | Flag to allow repository export to third party apps. | [optional] 
**allow_to_other_repo_export** | **bool** | Flag to allow repsitory export to other repository. | [optional] 
**enable_watermark** | **bool** | Flag to allow watermark. | [optional] 
**allow_printing** | **bool** | Flag to allow printing. | [optional] 
**allow_edit** | **bool** | Flag to allow edit. | [optional] 
**device_ownership** | **str** | Defines the device ownership. | [optional] 
**organization_groups** | **list[str]** | List of Organization Groups assigned to repository. | [optional] 
**user_groups** | **list[str]** | List of user groups assigned to repository. | [optional] 
**download_method** | **str** | Defines the content download method. | [optional] 
**download_while_roaming** | **bool** | Flag to allow download while roaming. | [optional] 
**force_download** | **bool** | Flag to enable force download. | [optional] 
**download_priority** | **str** | Defines the content download priority. | [optional] 
**content_required** | **bool** | Flag to mark content is required. | [optional] 
**content_download_date** | **datetime** | Defines the content download date. | [optional] 
**content_effective_date** | **datetime** | Defines the content effective date. | [optional] 
**content_expiry_date** | **datetime** | Defines the content expiry date. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


