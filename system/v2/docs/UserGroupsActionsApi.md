# systemv2.UserGroupsActionsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_groups_actions_add_missing_users_async**](UserGroupsActionsApi.md#user_groups_actions_add_missing_users_async) | **POST** /user-groups/{userGroupUuid}/actions/add-missing-users | New - Add missing users.
[**user_groups_actions_generate_view_changes_report_async**](UserGroupsActionsApi.md#user_groups_actions_generate_view_changes_report_async) | **POST** /user-groups/{userGroupUuid}/actions/changes/report | New - Report for user group changes before merge.
[**user_groups_actions_merge_changes_async**](UserGroupsActionsApi.md#user_groups_actions_merge_changes_async) | **POST** /user-groups/{userGroupUuid}/actions/merge | New - Merge user group changes.
[**user_groups_actions_sync_async**](UserGroupsActionsApi.md#user_groups_actions_sync_async) | **POST** /user-groups/{userGroupUuid}/actions/sync | New - Sync user group.
[**user_groups_actions_view_changes_async**](UserGroupsActionsApi.md#user_groups_actions_view_changes_async) | **GET** /user-groups/{userGroupUuid}/actions/changes | New - View user group changes.


# **user_groups_actions_add_missing_users_async**
> user_groups_actions_add_missing_users_async(user_group_uuid)

New - Add missing users.

Execute add missing users operation.

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
api_instance = systemv2.UserGroupsActionsApi(systemv2.ApiClient(configuration))
user_group_uuid = 'user_group_uuid_example' # str | Identifier of an user group.(Required).

try:
    # New - Add missing users.
    api_instance.user_groups_actions_add_missing_users_async(user_group_uuid)
except ApiException as e:
    print("Exception when calling UserGroupsActionsApi->user_groups_actions_add_missing_users_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_uuid** | [**str**](.md)| Identifier of an user group.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_actions_generate_view_changes_report_async**
> user_groups_actions_generate_view_changes_report_async(user_group_uuid, order_by=order_by, sort_order=sort_order, type=type, search_text=search_text)

New - Report for user group changes before merge.

Generate a report for changes before merge.

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
api_instance = systemv2.UserGroupsActionsApi(systemv2.ApiClient(configuration))
user_group_uuid = 'user_group_uuid_example' # str | Identifier of an user group.(Required).
order_by =  # object | Order the results by this attribute. (optional) (default to )
sort_order =  # object | Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. (optional) (default to )
type =  # object | Changes type. Users to be added or to be removed. (optional) (default to )
search_text = '' # str | Search text. (optional) (default to )

try:
    # New - Report for user group changes before merge.
    api_instance.user_groups_actions_generate_view_changes_report_async(user_group_uuid, order_by=order_by, sort_order=sort_order, type=type, search_text=search_text)
except ApiException as e:
    print("Exception when calling UserGroupsActionsApi->user_groups_actions_generate_view_changes_report_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_uuid** | [**str**](.md)| Identifier of an user group.(Required). | 
 **order_by** | [**object**](.md)| Order the results by this attribute. | [optional] [default to ]
 **sort_order** | [**object**](.md)| Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. | [optional] [default to ]
 **type** | [**object**](.md)| Changes type. Users to be added or to be removed. | [optional] [default to ]
 **search_text** | **str**| Search text. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_actions_merge_changes_async**
> user_groups_actions_merge_changes_async(user_group_uuid)

New - Merge user group changes.

Execute merge user group changes operation.

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
api_instance = systemv2.UserGroupsActionsApi(systemv2.ApiClient(configuration))
user_group_uuid = 'user_group_uuid_example' # str | Identifier of an user group.(Required).

try:
    # New - Merge user group changes.
    api_instance.user_groups_actions_merge_changes_async(user_group_uuid)
except ApiException as e:
    print("Exception when calling UserGroupsActionsApi->user_groups_actions_merge_changes_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_uuid** | [**str**](.md)| Identifier of an user group.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_actions_sync_async**
> user_groups_actions_sync_async(user_group_uuid)

New - Sync user group.

Execute sync user group operation.

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
api_instance = systemv2.UserGroupsActionsApi(systemv2.ApiClient(configuration))
user_group_uuid = 'user_group_uuid_example' # str | Identifier of an user group(Required).

try:
    # New - Sync user group.
    api_instance.user_groups_actions_sync_async(user_group_uuid)
except ApiException as e:
    print("Exception when calling UserGroupsActionsApi->user_groups_actions_sync_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_uuid** | [**str**](.md)| Identifier of an user group(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_actions_view_changes_async**
> ViewChangesModel user_groups_actions_view_changes_async(user_group_uuid, order_by=order_by, page=page, page_size=page_size, sort_order=sort_order, type=type, search_text=search_text)

New - View user group changes.

View user group changes before merge.

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
api_instance = systemv2.UserGroupsActionsApi(systemv2.ApiClient(configuration))
user_group_uuid = 'user_group_uuid_example' # str | Identifier of an user group.(Required).
order_by =  # object | Order the results by this attribute. (optional) (default to )
page = 56 # int | The specific page number to get. (optional)
page_size = 56 # int | Maximum records per page. (optional)
sort_order =  # object | Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. (optional) (default to )
type =  # object | Changes type. Users to be added or to be removed. (optional) (default to )
search_text = '' # str | Search text. (optional) (default to )

try:
    # New - View user group changes.
    api_response = api_instance.user_groups_actions_view_changes_async(user_group_uuid, order_by=order_by, page=page, page_size=page_size, sort_order=sort_order, type=type, search_text=search_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsActionsApi->user_groups_actions_view_changes_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_uuid** | [**str**](.md)| Identifier of an user group.(Required). | 
 **order_by** | [**object**](.md)| Order the results by this attribute. | [optional] [default to ]
 **page** | **int**| The specific page number to get. | [optional] 
 **page_size** | **int**| Maximum records per page. | [optional] 
 **sort_order** | [**object**](.md)| Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. | [optional] [default to ]
 **type** | [**object**](.md)| Changes type. Users to be added or to be removed. | [optional] [default to ]
 **search_text** | **str**| Search text. | [optional] [default to ]

### Return type

[**ViewChangesModel**](ViewChangesModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

