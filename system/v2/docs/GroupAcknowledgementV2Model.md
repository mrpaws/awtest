# GroupAcknowledgementV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_results** | **int** | The total number of results returned by the list or query operation. | [optional] 
**items_per_page** | **int** | The number of groups returned. | [optional] 
**add_count_in_current_page** | **int** | Total members pending to be added to group. | [optional] 
**remove_count_in_current_page** | **int** | Total members pending to be removed from the group. | [optional] 
**add_list** | [**list[MembershipDetailModel]**](MembershipDetailModel.md) | User details for which changes are pending. | [optional] 
**remove_list** | [**list[MembershipDetailModel]**](MembershipDetailModel.md) | User details for which changes are pending. | [optional] 
**merge_status** | **str** | Status as retrieved for group. | [optional] 
**last_sync_on_time** | **datetime** | Last sync On Time | [optional] 
**access_token** | **str** | Access token for the merge action. | [optional] 
**links** | [**dict(str, JsonHalLinkModel)**](JsonHalLinkModel.md) | Gets a list of JSON HAL links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


