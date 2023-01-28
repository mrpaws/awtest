# systemv1.AdminsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admins_v1_add_role_to_user**](AdminsV1Api.md#admins_v1_add_role_to_user) | **POST** /admins/{id}/addrole | Adds a role to the specified admin user.
[**admins_v1_change_password**](AdminsV1Api.md#admins_v1_change_password) | **POST** /admins/{id}/changepassword | Changes the specified admin user&#39;s password.
[**admins_v1_delete**](AdminsV1Api.md#admins_v1_delete) | **DELETE** /admins/{id}/delete | Deletes the specified admin user.
[**admins_v1_get**](AdminsV1Api.md#admins_v1_get) | **GET** /admins/{id} | Retrieves information about the specified admin user.
[**admins_v1_get_configurations_about_page**](AdminsV1Api.md#admins_v1_get_configurations_about_page) | **GET** /admins/{adminId}/configurationsaboutpage | New - Retrieves the value for showConfigurationsAboutPage.
[**admins_v1_put**](AdminsV1Api.md#admins_v1_put) | **POST** /admins/addadminuser | Creates a new admin user.
[**admins_v1_remove_role_from_user**](AdminsV1Api.md#admins_v1_remove_role_from_user) | **POST** /admins/{id}/removerole | Removes a role from the specified admin user.
[**admins_v1_search_async**](AdminsV1Api.md#admins_v1_search_async) | **GET** /admins/search | Searches for Admin users using the query information provided.
[**admins_v1_update_admin_user**](AdminsV1Api.md#admins_v1_update_admin_user) | **POST** /admins/{id}/update | Updates the specified admin user.
[**admins_v1_update_configurations_about_page**](AdminsV1Api.md#admins_v1_update_configurations_about_page) | **POST** /admins/{adminId}/configurationsaboutpage/{showpage} | New - Updates the value for showConfigurationsAboutPage.


# **admins_v1_add_role_to_user**
> admins_v1_add_role_to_user(id, role)

Adds a role to the specified admin user.

Performs necessary checks and add an role for an existing admin.

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
api_instance = systemv1.AdminsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The admin user ID (Required).
role = systemv1.RoleModel_() # RoleModel_ | The role to add. (Required).

try:
    # Adds a role to the specified admin user.
    api_instance.admins_v1_add_role_to_user(id, role)
except ApiException as e:
    print("Exception when calling AdminsV1Api->admins_v1_add_role_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The admin user ID (Required). | 
 **role** | [**RoleModel_**](RoleModel_.md)| The role to add. (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v1_change_password**
> admins_v1_change_password(id, adminuser)

Changes the specified admin user's password.

Performs necessary checks and update the password for an existing admin.

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
api_instance = systemv1.AdminsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The admin user ID (Required).
adminuser = systemv1.AdminUser_() # AdminUser_ | The admin user details. (Required).

try:
    # Changes the specified admin user's password.
    api_instance.admins_v1_change_password(id, adminuser)
except ApiException as e:
    print("Exception when calling AdminsV1Api->admins_v1_change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The admin user ID (Required). | 
 **adminuser** | [**AdminUser_**](AdminUser_.md)| The admin user details. (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v1_delete**
> admins_v1_delete(id)

Deletes the specified admin user.

Performs necessary checks and delete all the information of the Admin based on admin id.

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
api_instance = systemv1.AdminsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The admin user ID (Required).

try:
    # Deletes the specified admin user.
    api_instance.admins_v1_delete(id)
except ApiException as e:
    print("Exception when calling AdminsV1Api->admins_v1_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The admin user ID (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v1_get**
> AdminUser admins_v1_get(id)

Retrieves information about the specified admin user.

Performs necessary checks and get all the information of the Admin based on admin id.

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
api_instance = systemv1.AdminsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The admin user ID (Required).

try:
    # Retrieves information about the specified admin user.
    api_response = api_instance.admins_v1_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminsV1Api->admins_v1_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The admin user ID (Required). | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v1_get_configurations_about_page**
> ConfigurationsAboutModel admins_v1_get_configurations_about_page(admin_id)

New - Retrieves the value for showConfigurationsAboutPage.

Retrieves the value for showConfigurationsAboutPage which will be used to enable or disable the About page.

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
api_instance = systemv1.AdminsV1Api(systemv1.ApiClient(configuration))
admin_id = 56 # int | Identifier for an admin(Required).

try:
    # New - Retrieves the value for showConfigurationsAboutPage.
    api_response = api_instance.admins_v1_get_configurations_about_page(admin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminsV1Api->admins_v1_get_configurations_about_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**| Identifier for an admin(Required). | 

### Return type

[**ConfigurationsAboutModel**](ConfigurationsAboutModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v1_put**
> EntityId admins_v1_put(admin_user)

Creates a new admin user.

Performs necessary checks and Create a new Admin.

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
api_instance = systemv1.AdminsV1Api(systemv1.ApiClient(configuration))
admin_user = systemv1.AdminUser_() # AdminUser_ | The admin user resource to create (Required).

try:
    # Creates a new admin user.
    api_response = api_instance.admins_v1_put(admin_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminsV1Api->admins_v1_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_user** | [**AdminUser_**](AdminUser_.md)| The admin user resource to create (Required). | 

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v1_remove_role_from_user**
> admins_v1_remove_role_from_user(id, role)

Removes a role from the specified admin user.

Performs necessary checks and remove an role from an existing admin.

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
api_instance = systemv1.AdminsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The admin user ID. (Required).
role = systemv1.RoleModel_() # RoleModel_ | The role to remove. (Required).

try:
    # Removes a role from the specified admin user.
    api_instance.admins_v1_remove_role_from_user(id, role)
except ApiException as e:
    print("Exception when calling AdminsV1Api->admins_v1_remove_role_from_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The admin user ID. (Required). | 
 **role** | [**RoleModel_**](RoleModel_.md)| The role to remove. (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v1_search_async**
> AdminSearchResult admins_v1_search_async(firstname=firstname, lastname=lastname, email=email, organizationgroupid=organizationgroupid, role=role, username=username, orderby=orderby, page=page, pagesize=pagesize, sortorder=sortorder, status=status)

Searches for Admin users using the query information provided.

Performs necessary checks and search for the admin users based on the request query.

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
api_instance = systemv1.AdminsV1Api(systemv1.ApiClient(configuration))
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
    # Searches for Admin users using the query information provided.
    api_response = api_instance.admins_v1_search_async(firstname=firstname, lastname=lastname, email=email, organizationgroupid=organizationgroupid, role=role, username=username, orderby=orderby, page=page, pagesize=pagesize, sortorder=sortorder, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminsV1Api->admins_v1_search_async: %s\n" % e)
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

[**AdminSearchResult**](AdminSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v1_update_admin_user**
> admins_v1_update_admin_user(id, admin_user=admin_user)

Updates the specified admin user.

Performs necessary checks and Update the Admin properties based on Id.

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
api_instance = systemv1.AdminsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The admin user ID (Required).
admin_user = systemv1.AdminUser_() # AdminUser_ | The updated admin user details. (optional)

try:
    # Updates the specified admin user.
    api_instance.admins_v1_update_admin_user(id, admin_user=admin_user)
except ApiException as e:
    print("Exception when calling AdminsV1Api->admins_v1_update_admin_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The admin user ID (Required). | 
 **admin_user** | [**AdminUser_**](AdminUser_.md)| The updated admin user details. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_v1_update_configurations_about_page**
> admins_v1_update_configurations_about_page(admin_id, showpage)

New - Updates the value for showConfigurationsAboutPage.

Updates the value for showConfigurationsAboutPage which will be used to enable or disable the About page.

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
api_instance = systemv1.AdminsV1Api(systemv1.ApiClient(configuration))
admin_id = 56 # int | Identifier for an admin(Required).
showpage = true # bool | true if the About page should be displayed for Configurations(Required).

try:
    # New - Updates the value for showConfigurationsAboutPage.
    api_instance.admins_v1_update_configurations_about_page(admin_id, showpage)
except ApiException as e:
    print("Exception when calling AdminsV1Api->admins_v1_update_configurations_about_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**| Identifier for an admin(Required). | 
 **showpage** | **bool**| true if the About page should be displayed for Configurations(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

