# PreviewAdvancedLdapSyncJobResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_ldap_sync_job_uuid** | **str** | The unique identifier for the created advanced ldap sync job which is to be previewed. | [optional] 
**status** | **int** | The status of the advanced ldap sync job process. | [optional] 
**items_per_page** | **int** | The number of users returned. | [optional] 
**modified_user_details** | [**PreviewAdvancedLdapSyncJobDetailsModel**](PreviewAdvancedLdapSyncJobDetailsModel.md) | Advanced ldap sync preview modified data. | [optional] 
**added_user_details** | [**PreviewAdvancedLdapSyncJobDetailsModel**](PreviewAdvancedLdapSyncJobDetailsModel.md) | Advanced ldap sync preview added data. | [optional] 
**removed_user_details** | [**PreviewAdvancedLdapSyncJobDetailsModel**](PreviewAdvancedLdapSyncJobDetailsModel.md) | Advanced ldap sync preview added data. | [optional] 
**total_results** | **int** | Total Number of records. | [optional] 
**additional_info** | [**HypermediaV2Model**](HypermediaV2Model.md) | Gets or sets Hypermedia content for the result. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


