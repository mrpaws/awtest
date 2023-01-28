# systemv2.ScimV2GroupsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scim_v2_groups_create_group_async**](ScimV2GroupsApi.md#scim_v2_groups_create_group_async) | **POST** /scim/v2/Groups | New - Create a group.
[**scim_v2_groups_get_user_group_by_uuid**](ScimV2GroupsApi.md#scim_v2_groups_get_user_group_by_uuid) | **GET** /scim/v2/Groups/{uuid} | New - Get the group details by UUID
[**scim_v2_groups_get_user_groups**](ScimV2GroupsApi.md#scim_v2_groups_get_user_groups) | **GET** /scim/v2/Groups | New - Get a group list
[**scim_v2_groups_group_actions_async**](ScimV2GroupsApi.md#scim_v2_groups_group_actions_async) | **PATCH** /scim/v2/Groups/{uuid} | New - Operations on groups.
[**scim_v2_groups_search_groups**](ScimV2GroupsApi.md#scim_v2_groups_search_groups) | **POST** /scim/v2/Groups/.search | New - Search for groups.


# **scim_v2_groups_create_group_async**
> GroupResponse scim_v2_groups_create_group_async(create_group_request)

New - Create a group.

Endpoint to create a group. As of now, we only support importing user groups from  a directory service into Workspace One UEM.   When importing a user group form directory service, one needs to pass externalId.   In case of a directory custom group, its required to pass displayName for the group.

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
api_instance = systemv2.ScimV2GroupsApi(systemv2.ApiClient(configuration))
create_group_request = systemv2.CreateGroupRequest() # CreateGroupRequest | The group to be created.(Required)

try:
    # New - Create a group.
    api_response = api_instance.scim_v2_groups_create_group_async(create_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScimV2GroupsApi->scim_v2_groups_create_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_request** | [**CreateGroupRequest**](CreateGroupRequest.md)| The group to be created.(Required) | 

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scim_v2_groups_get_user_group_by_uuid**
> GroupResponse scim_v2_groups_get_user_group_by_uuid(uuid)

New - Get the group details by UUID

Get the enrollment/admin group details by UUID

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
api_instance = systemv2.ScimV2GroupsApi(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier of an group(Required)

try:
    # New - Get the group details by UUID
    api_response = api_instance.scim_v2_groups_get_user_group_by_uuid(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScimV2GroupsApi->scim_v2_groups_get_user_group_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier of an group(Required) | 

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scim_v2_groups_get_user_groups**
> GroupListResponse scim_v2_groups_get_user_groups(filter=filter, attributes=attributes, excluded_attributes=excluded_attributes, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)

New - Get a group list

Get the group list

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
api_instance = systemv2.ScimV2GroupsApi(systemv2.ApiClient(configuration))
filter = 'filter_example' # str | The filter string used to request a subset of resources. (optional)
attributes = 'attributes_example' # str | A comma separated list of strings indicating the names of resource attributes to return in the response. (optional)
excluded_attributes = 'excluded_attributes_example' # str | A comma separated list of strings indicating the names of resource attributes to be removed from the default set of attributes to return. (optional)
sort_by = 'sort_by_example' # str | A string indicating the attribute to be used to order the returned responses. (optional)
sort_order = 'sort_order_example' # str | A string indicating the order in which the 'sortBy' parameter is applied. (optional)
start_index = 'start_index_example' # str | A 1-based integer indicating the index of the first query result. (optional)
count = 'count_example' # str | An integer indicating the maximum number of query results per page. (optional)

try:
    # New - Get a group list
    api_response = api_instance.scim_v2_groups_get_user_groups(filter=filter, attributes=attributes, excluded_attributes=excluded_attributes, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScimV2GroupsApi->scim_v2_groups_get_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter string used to request a subset of resources. | [optional] 
 **attributes** | **str**| A comma separated list of strings indicating the names of resource attributes to return in the response. | [optional] 
 **excluded_attributes** | **str**| A comma separated list of strings indicating the names of resource attributes to be removed from the default set of attributes to return. | [optional] 
 **sort_by** | **str**| A string indicating the attribute to be used to order the returned responses. | [optional] 
 **sort_order** | **str**| A string indicating the order in which the &#39;sortBy&#39; parameter is applied. | [optional] 
 **start_index** | **str**| A 1-based integer indicating the index of the first query result. | [optional] 
 **count** | **str**| An integer indicating the maximum number of query results per page. | [optional] 

### Return type

[**GroupListResponse**](GroupListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scim_v2_groups_group_actions_async**
> scim_v2_groups_group_actions_async(uuid, body)

New - Operations on groups.

Operations on groups. Currently we support patch operation only on LastSyncOn. Sync will be performed only when the LastSyncOn is passed as mm/dd/yyyy

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
api_instance = systemv2.ScimV2GroupsApi(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier of a group(Required)
body = systemv2.GroupPatchRequest() # GroupPatchRequest | patch operations list(Required)

try:
    # New - Operations on groups.
    api_instance.scim_v2_groups_group_actions_async(uuid, body)
except ApiException as e:
    print("Exception when calling ScimV2GroupsApi->scim_v2_groups_group_actions_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier of a group(Required) | 
 **body** | [**GroupPatchRequest**](GroupPatchRequest.md)| patch operations list(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scim_v2_groups_search_groups**
> GroupResponse scim_v2_groups_search_groups(search_request)

New - Search for groups.

Search for groups.

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
api_instance = systemv2.ScimV2GroupsApi(systemv2.ApiClient(configuration))
search_request = systemv2.SearchRequest() # SearchRequest | The search criteria to returned responses.(Required)

try:
    # New - Search for groups.
    api_response = api_instance.scim_v2_groups_search_groups(search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScimV2GroupsApi->scim_v2_groups_search_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)| The search criteria to returned responses.(Required) | 

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

