# IRequestQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_query_params** | **dict(str, str)** | Gets or sets Query Parameters. For e.g. any query string parameters will be extracted to key,value pair and stored here. | [optional] 
**tenant_context** | [**ITenantContext**](ITenantContext.md) | Gets or sets IAwTenantContext. Will hold the tenant details, which will be filled as part of the tenant validation handler. | [optional] 
**request_method** | [**HttpMethod**](HttpMethod.md) | Gets or sets RequestMethod. Will be used to write custom rules. | [optional] 
**action_name** | **str** | Gets or sets ActionName. | [optional] 
**allowed_uri_query_chars** | **list[str]** | Gets or sets allowed Characters in Query String. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


