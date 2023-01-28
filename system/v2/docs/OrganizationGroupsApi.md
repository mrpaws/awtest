# systemv2.OrganizationGroupsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_groups_organization_group_search_async**](OrganizationGroupsApi.md#organization_groups_organization_group_search_async) | **GET** /groups/search | Searches for organization groups using the query information provided.
[**organization_groups_post_async**](OrganizationGroupsApi.md#organization_groups_post_async) | **POST** /groups/{id} | Creates a new organization group.


# **organization_groups_organization_group_search_async**
> OrganizationGroupPagedSearchResultModel organization_groups_organization_group_search_async(name=name, type=type, groupid=groupid, orderby=orderby, page=page, pagesize=pagesize, sortorder=sortorder)

Searches for organization groups using the query information provided.

Search organization by the given parameter.

### Example
```python
from __future__ import print_function
import time
import systemv2
from systemv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv2.OrganizationGroupsApi(systemv2.ApiClient(configuration))
name = '' # str | The OrganizationGroup name, such as \"Global\". (optional) (default to )
type = '' # str | The OrganizationGroup type. (eg. \"Container\",\"Customer\",\"Partner\"). (optional) (default to )
groupid = '' # str | The organization group identifier[Activation code] to search for.[Exact match is performed for this attribute]. (optional) (default to )
orderby = '' # str | Orders the results based on this attribute-value[Valid values are: Id/Name/GroupId/LocationGroupType]. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)
sortorder = '' # str | Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. (optional) (default to )

try:
    # Searches for organization groups using the query information provided.
    api_response = api_instance.organization_groups_organization_group_search_async(name=name, type=type, groupid=groupid, orderby=orderby, page=page, pagesize=pagesize, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationGroupsApi->organization_groups_organization_group_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The OrganizationGroup name, such as \&quot;Global\&quot;. | [optional] [default to ]
 **type** | **str**| The OrganizationGroup type. (eg. \&quot;Container\&quot;,\&quot;Customer\&quot;,\&quot;Partner\&quot;). | [optional] [default to ]
 **groupid** | **str**| The organization group identifier[Activation code] to search for.[Exact match is performed for this attribute]. | [optional] [default to ]
 **orderby** | **str**| Orders the results based on this attribute-value[Valid values are: Id/Name/GroupId/LocationGroupType]. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 
 **sortorder** | **str**| Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. | [optional] [default to ]

### Return type

[**OrganizationGroupPagedSearchResultModel**](OrganizationGroupPagedSearchResultModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_groups_post_async**
> OrganizationGroupResponseModel organization_groups_post_async(id, location_group=location_group)

Creates a new organization group.

Create a new organization group.

### Example
```python
from __future__ import print_function
import time
import systemv2
from systemv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv2.OrganizationGroupsApi(systemv2.ApiClient(configuration))
id = 56 # int | The parent OrganizationGroup Identifier.
location_group = systemv2.OrganizationGroup_() # OrganizationGroup_ | The OrganizationGroup resource to be created. (optional)

try:
    # Creates a new organization group.
    api_response = api_instance.organization_groups_post_async(id, location_group=location_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationGroupsApi->organization_groups_post_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The parent OrganizationGroup Identifier. | 
 **location_group** | [**OrganizationGroup_**](OrganizationGroup_.md)| The OrganizationGroup resource to be created. | [optional] 

### Return type

[**OrganizationGroupResponseModel**](OrganizationGroupResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

