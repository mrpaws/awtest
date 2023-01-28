# systemv2.AdminsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admins_v2_add_role_to_user**](AdminsV2Api.md#admins_v2_add_role_to_user) | **PUT** /groups/{organizationGroupUuid}/admins/{adminUserUuid}/roles/{roleUuid} | New - Adds a role to the specified admin user.
[**admins_v2_change_password**](AdminsV2Api.md#admins_v2_change_password) | **PUT** /admins/{uuid}/password | New - Changes the specified admin user&#39;s password.
[**admins_v2_create**](AdminsV2Api.md#admins_v2_create) | **POST** /admins | New - Creates a new admin user.
[**admins_v2_delete**](AdminsV2Api.md#admins_v2_delete) | **DELETE** /admins/{uuid} | New - Deletes the specified admin user.
[**admins_v2_get**](AdminsV2Api.md#admins_v2_get) | **GET** /admins/{uuid} | New - Retrieves information about the specified admin user.
[**admins_v2_remove_role_from_user**](AdminsV2Api.md#admins_v2_remove_role_from_user) | **DELETE** /groups/{organizationGroupUuid}/admins/{adminUserUuid}/roles/{roleUuid} | New - Removes a role from the specified admin user.
[**admins_v2_search_async**](AdminsV2Api.md#admins_v2_search_async) | **GET** /admins/search | New - Searches for Admin users using the query information provided.
[**admins_v2_update**](AdminsV2Api.md#admins_v2_update) | **PUT** /admins/{uuid} | New - Updates the specified admin user.


# **admins_v2_add_role_to_user**
> admins_v2_add_role_to_user(organization_group_uuid, admin_user_uuid, role_uuid)

New - Adds a role to the specified admin user.

Performs necessary checks and add an role for an existing admin.

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
api_instance = systemv2.AdminsV2Api(systemv2.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Location group UUID string (Required).
admin_user_uuid = 'admin_user_uuid_example' # str | Admin user UUID (Required).
role_uuid = 'role_uuid_example' # str | Role UUID to be added (Required).

try:
    # New - Adds a role to the specified admin user.
    api_instance.admins_v2_add_role_to_user(organization_group_uuid, admin_user_uuid, role_uuid)
except ApiException as e:
    print("Exception when calling AdminsV2Api->admins_v2_add_role_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Location group UUID string (Required). | 
 **admin_user_uuid** | [**str**](.md)| Admin user UUID (Required). | 
 **role_uuid** | [**str**](.md)| Role UUID to be added (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v2_change_password**
> admins_v2_change_password(uuid, adminuser=adminuser)

New - Changes the specified admin user's password.

Performs necessary checks and update the password for an existing admin.

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
api_instance = systemv2.AdminsV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | The admin user udid (Required).
adminuser = systemv2.AdminUser_() # AdminUser_ | The admin user details. (optional)

try:
    # New - Changes the specified admin user's password.
    api_instance.admins_v2_change_password(uuid, adminuser=adminuser)
except ApiException as e:
    print("Exception when calling AdminsV2Api->admins_v2_change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The admin user udid (Required). | 
 **adminuser** | [**AdminUser_**](AdminUser_.md)| The admin user details. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v2_create**
> EntityId admins_v2_create(admin)

New - Creates a new admin user.

Performs necessary checks and Create a new Admin.

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
api_instance = systemv2.AdminsV2Api(systemv2.ApiClient(configuration))
admin = systemv2.AdminV2Model() # AdminV2Model | The admin user resource to create (Required).

try:
    # New - Creates a new admin user.
    api_response = api_instance.admins_v2_create(admin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminsV2Api->admins_v2_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin** | [**AdminV2Model**](AdminV2Model.md)| The admin user resource to create (Required). | 

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v2_delete**
> admins_v2_delete(uuid)

New - Deletes the specified admin user.

V2.

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
api_instance = systemv2.AdminsV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Admin user UUID to be deleted(Required).

try:
    # New - Deletes the specified admin user.
    api_instance.admins_v2_delete(uuid)
except ApiException as e:
    print("Exception when calling AdminsV2Api->admins_v2_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Admin user UUID to be deleted(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v2_get**
> AdminUser admins_v2_get(uuid)

New - Retrieves information about the specified admin user.

Performs necessary checks and get all the information of the Admin based on admin udid.

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
api_instance = systemv2.AdminsV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Admin user UUID(Required).

try:
    # New - Retrieves information about the specified admin user.
    api_response = api_instance.admins_v2_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminsV2Api->admins_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Admin user UUID(Required). | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v2_remove_role_from_user**
> admins_v2_remove_role_from_user(organization_group_uuid, admin_user_uuid, role_uuid)

New - Removes a role from the specified admin user.

Performs necessary checks and remove an role from an existing admin.

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
api_instance = systemv2.AdminsV2Api(systemv2.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Location group UUID string (Required).
admin_user_uuid = 'admin_user_uuid_example' # str | Admin user UUID (Required).
role_uuid = 'role_uuid_example' # str | Role UUID to be deleted (Required).

try:
    # New - Removes a role from the specified admin user.
    api_instance.admins_v2_remove_role_from_user(organization_group_uuid, admin_user_uuid, role_uuid)
except ApiException as e:
    print("Exception when calling AdminsV2Api->admins_v2_remove_role_from_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Location group UUID string (Required). | 
 **admin_user_uuid** | [**str**](.md)| Admin user UUID (Required). | 
 **role_uuid** | [**str**](.md)| Role UUID to be deleted (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v2_search_async**
> AdminSearchResultV2 admins_v2_search_async(firstname=firstname, lastname=lastname, email=email, organizationgroupid=organizationgroupid, role=role, username=username, orderby=orderby, page=page, pagesize=pagesize, sortorder=sortorder, status=status)

New - Searches for Admin users using the query information provided.

Performs necessary checks and search for the admin users based on the request query.

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
api_instance = systemv2.AdminsV2Api(systemv2.ApiClient(configuration))
firstname = '' # str | The First name to search for. (optional) (default to )
lastname = '' # str | The Last name to search for. (optional) (default to )
email = '' # str | The Email Address to search for. (optional) (default to )
organizationgroupid = 56 # int | The Organization Group Id to search for. (optional)
role = '' # str | The Role name to search for. (optional) (default to )
username = '' # str | The User name to search for. (optional) (default to )
orderby = '' # str | Order the results by this attribute. (optional) (default to )
page = 56 # int | The specific page number to get. (optional)
pagesize = 56 # int | Maximum records per page. (optional)
sortorder = '' # str | Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. (optional) (default to )
status = '' # str | The admin status. Allowed values are Active or Inactive. Defaults to all, if this attribute is not specified. (optional) (default to )

try:
    # New - Searches for Admin users using the query information provided.
    api_response = api_instance.admins_v2_search_async(firstname=firstname, lastname=lastname, email=email, organizationgroupid=organizationgroupid, role=role, username=username, orderby=orderby, page=page, pagesize=pagesize, sortorder=sortorder, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminsV2Api->admins_v2_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firstname** | **str**| The First name to search for. | [optional] [default to ]
 **lastname** | **str**| The Last name to search for. | [optional] [default to ]
 **email** | **str**| The Email Address to search for. | [optional] [default to ]
 **organizationgroupid** | **int**| The Organization Group Id to search for. | [optional] 
 **role** | **str**| The Role name to search for. | [optional] [default to ]
 **username** | **str**| The User name to search for. | [optional] [default to ]
 **orderby** | **str**| Order the results by this attribute. | [optional] [default to ]
 **page** | **int**| The specific page number to get. | [optional] 
 **pagesize** | **int**| Maximum records per page. | [optional] 
 **sortorder** | **str**| Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. | [optional] [default to ]
 **status** | **str**| The admin status. Allowed values are Active or Inactive. Defaults to all, if this attribute is not specified. | [optional] [default to ]

### Return type

[**AdminSearchResultV2**](AdminSearchResultV2.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v2_update**
> admins_v2_update(uuid, admin=admin)

New - Updates the specified admin user.

Performs necessary checks and Update the Admin properties based on Id.

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
api_instance = systemv2.AdminsV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | The admin user UUID(Required).
admin = systemv2.AdminV2Model() # AdminV2Model | The updated admin user details. (optional)

try:
    # New - Updates the specified admin user.
    api_instance.admins_v2_update(uuid, admin=admin)
except ApiException as e:
    print("Exception when calling AdminsV2Api->admins_v2_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The admin user UUID(Required). | 
 **admin** | [**AdminV2Model**](AdminV2Model.md)| The updated admin user details. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

