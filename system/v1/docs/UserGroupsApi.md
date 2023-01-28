# systemv1.UserGroupsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_groups_add_user_to_user_group_async**](UserGroupsApi.md#user_groups_add_user_to_user_group_async) | **POST** /usergroups/{usergroupid}/user/{enrollmentuserid}/addusertogroup | Adds the user to custom User Group.
[**user_groups_create_custom_user_group**](UserGroupsApi.md#user_groups_create_custom_user_group) | **POST** /usergroups/createcustomusergroup | Creates a Custom User Group.
[**user_groups_delete_user_group_id_users**](UserGroupsApi.md#user_groups_delete_user_group_id_users) | **DELETE** /usergroups/{usergroupid}/delete | Delete custom User Group.
[**user_groups_remove_user_from_user_group_async**](UserGroupsApi.md#user_groups_remove_user_from_user_group_async) | **POST** /usergroups/{usergroupid}/user/{enrollmentuserid}/removeuserfromgroup | Removes the user from custom User Group.
[**user_groups_retrieve_user_group_id_users**](UserGroupsApi.md#user_groups_retrieve_user_group_id_users) | **GET** /usergroups/{usergroupid}/users | Retrieves list of users from provided custom user group id.
[**user_groups_search**](UserGroupsApi.md#user_groups_search) | **GET** /usergroups/search | Search User Groups.
[**user_groups_search_user_group**](UserGroupsApi.md#user_groups_search_user_group) | **GET** /usergroups/custom/search | Search custom User Group with given parameters.


# **user_groups_add_user_to_user_group_async**
> user_groups_add_user_to_user_group_async(usergroupid, enrollmentuserid)

Adds the user to custom User Group.

Adds user to custom User Group based on its enrollment user id and user group id.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.UserGroupsApi(systemv1.ApiClient(configuration))
usergroupid = 789 # int | User Group identifier (Required).
enrollmentuserid = 789 # int | Enrollment user identifier (Required).

try:
    # Adds the user to custom User Group.
    api_instance.user_groups_add_user_to_user_group_async(usergroupid, enrollmentuserid)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_add_user_to_user_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroupid** | **int**| User Group identifier (Required). | 
 **enrollmentuserid** | **int**| Enrollment user identifier (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_create_custom_user_group**
> EntityIdModel user_groups_create_custom_user_group(usergroup)

Creates a Custom User Group.

Creates a custom User Group using request body containing group name, description, and the id of the              organization group that will manage the User Group.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.UserGroupsApi(systemv1.ApiClient(configuration))
usergroup = systemv1.UserGroup() # UserGroup | The custom User Group resource (Required).

try:
    # Creates a Custom User Group.
    api_response = api_instance.user_groups_create_custom_user_group(usergroup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_create_custom_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroup** | [**UserGroup**](UserGroup.md)| The custom User Group resource (Required). | 

### Return type

[**EntityIdModel**](EntityIdModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_delete_user_group_id_users**
> user_groups_delete_user_group_id_users(usergroupid)

Delete custom User Group.

Deletes a custom User Group based on the user group id.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.UserGroupsApi(systemv1.ApiClient(configuration))
usergroupid = 56 # int | User Group Identifier (Required).

try:
    # Delete custom User Group.
    api_instance.user_groups_delete_user_group_id_users(usergroupid)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_delete_user_group_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroupid** | **int**| User Group Identifier (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_remove_user_from_user_group_async**
> user_groups_remove_user_from_user_group_async(usergroupid, enrollmentuserid)

Removes the user from custom User Group.

Removes the user from custom User Group based on its enrollment user id and user group id.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.UserGroupsApi(systemv1.ApiClient(configuration))
usergroupid = 789 # int | User group identifier (Required).
enrollmentuserid = 789 # int | Enrollment user identifier (Required).

try:
    # Removes the user from custom User Group.
    api_instance.user_groups_remove_user_from_user_group_async(usergroupid, enrollmentuserid)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_remove_user_from_user_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroupid** | **int**| User group identifier (Required). | 
 **enrollmentuserid** | **int**| Enrollment user identifier (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_retrieve_user_group_id_users**
> UserGroupUsers user_groups_retrieve_user_group_id_users(usergroupid, page=page, pagesize=pagesize)

Retrieves list of users from provided custom user group id.

Retrieves a list of users that are members of custom User Group based on the user group id and a request query containing              page number and page size.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.UserGroupsApi(systemv1.ApiClient(configuration))
usergroupid = 56 # int | User Group Identifier (Required).
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Retrieves list of users from provided custom user group id.
    api_response = api_instance.user_groups_retrieve_user_group_id_users(usergroupid, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_retrieve_user_group_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroupid** | **int**| User Group Identifier (Required). | 
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**UserGroupUsers**](UserGroupUsers.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_search**
> user_groups_search(groupname=groupname, organizationgroupid=organizationgroupid, usergrouptype=usergrouptype, syncstatus=syncstatus, mergestatus=mergestatus, page=page, pagesize=pagesize)

Search User Groups.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.UserGroupsApi(systemv1.ApiClient(configuration))
groupname = '' # str | Name of the group. (optional) (default to )
organizationgroupid = 56 # int | Organization Group Identifier. (optional)
usergrouptype = '' # str | User Group Type. (optional) (default to )
syncstatus = '' # str | Sync Status of the User Group. (optional) (default to )
mergestatus = '' # str | Merge Status of the User Group. (optional) (default to )
page = 56 # int | It specifies the page number. (optional)
pagesize = 56 # int | Maximum records per page. (optional)

try:
    # Search User Groups.
    api_instance.user_groups_search(groupname=groupname, organizationgroupid=organizationgroupid, usergrouptype=usergrouptype, syncstatus=syncstatus, mergestatus=mergestatus, page=page, pagesize=pagesize)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupname** | **str**| Name of the group. | [optional] [default to ]
 **organizationgroupid** | **int**| Organization Group Identifier. | [optional] 
 **usergrouptype** | **str**| User Group Type. | [optional] [default to ]
 **syncstatus** | **str**| Sync Status of the User Group. | [optional] [default to ]
 **mergestatus** | **str**| Merge Status of the User Group. | [optional] [default to ]
 **page** | **int**| It specifies the page number. | [optional] 
 **pagesize** | **int**| Maximum records per page. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_search_user_group**
> UserGroups user_groups_search_user_group(groupname, organizationgroupid=organizationgroupid, page=page, pagesize=pagesize)

Search custom User Group with given parameters.

Search for a custom User Group with given request query containing the following parameters:              the group name, the organizaiton group identifier, page number, and page size.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.UserGroupsApi(systemv1.ApiClient(configuration))
groupname = '' # str | Name of User Group (Required). (default to )
organizationgroupid = 56 # int | Organization Group Identifier. (optional)
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Search custom User Group with given parameters.
    api_response = api_instance.user_groups_search_user_group(groupname, organizationgroupid=organizationgroupid, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_search_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupname** | **str**| Name of User Group (Required). | [default to ]
 **organizationgroupid** | **int**| Organization Group Identifier. | [optional] 
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**UserGroups**](UserGroups.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

