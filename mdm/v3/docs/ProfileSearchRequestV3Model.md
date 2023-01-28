# ProfileSearchRequestV3Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_group_uuid** | **str** | Organization group uuid based on which we will search the profiles. If not provided it will search based on Admin Organization group. | [optional] 
**platform** | **int** | Filter based on the platform. | [optional] 
**configuration_types** | **list[int]** | Profile configuration type, default value DEVICE. | [optional] 
**status** | **str** | Profile status, default value ACTIVE, supported value ACTIVE, INACTIVE.. | [optional] 
**payloads** | **list[str]** | Payload based on we will search the profile where payload has been configured.  Search is performed based on payload names for all platforms, however search will be performed on basis of GlobalizationKey as well for macOS platform. | [optional] 
**search_text** | **str** | Search text based on profile name. | [optional] 
**context** | **int** | Profile context. | [optional] 
**exclude_child_organization_group** | **bool** | Exclude the child OG profile. | [optional] 
**exclude_compliance_profile** | **bool** | Exclude the compliance profile. | [optional] 
**exclude_interactive_profile** | **bool** | Exclude the compliance profile. | [optional] 
**page_size** | **int** | Page size of search result. Default value 20, and maximum value 50. | [optional] 
**page_number** | **int** | Page number of search result. | [optional] 
**sort_by** | **str** | Sort by column, currently supported profile name and ModifiedOn. | [optional] 
**sort_order** | **str** | Sort order, Currenty suppored ASC and DESC, default value ASC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


