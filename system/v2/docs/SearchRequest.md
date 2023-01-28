# SearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **list[str]** | Schemas used to compose a search request. | [optional] 
**attributes** | **list[str]** | A multi-valued list of strings indicating the names of resource attributes to return in the response. | [optional] 
**excluded_attributes** | **list[str]** | A multi-valued list of strings indicating the names of resource attributes to be removed from the default set of attributes to return. | [optional] 
**filter** | **str** | The filter string used to request a subset of resources. | [optional] 
**sort_by** | **str** | A string indicating the attribute to be used to order the returned responses. | [optional] 
**sort_order** | **int** | A string indicating the order in which the &#39;sortBy&#39; parameter is applied. | [optional] 
**start_index** | **int** | A 1-based integer indicating the index of the first query result. | [optional] 
**count** | **int** | An integer indicating the maximum number of query results per page. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


