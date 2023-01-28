# systemv1.UserApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_activate_user**](UserApi.md#user_activate_user) | **POST** /users/{id}/activate | Activate the enrollment user.
[**user_add_user_async**](UserApi.md#user_add_user_async) | **POST** /users/adduser | Create a new enrollment user.
[**user_bulk_activate**](UserApi.md#user_bulk_activate) | **POST** /users/activate | Activate a list of enrollment users.
[**user_bulk_de_activate_async**](UserApi.md#user_bulk_de_activate_async) | **POST** /users/deactivate | Deactivate a list of enrollment users.
[**user_bulk_delete_async**](UserApi.md#user_bulk_delete_async) | **POST** /users/delete | Delete a list of enrollment users.
[**user_change_location_group_async**](UserApi.md#user_change_location_group_async) | **POST** /users/{id}/changelocationgroup | Change the organization group of the enrollment user.
[**user_deactivate_user_async**](UserApi.md#user_deactivate_user_async) | **POST** /users/{id}/deactivate | Deactivate the enrollment user.
[**user_delete_async**](UserApi.md#user_delete_async) | **DELETE** /users/{id}/delete | Delete the enrollment user.
[**user_get**](UserApi.md#user_get) | **GET** /users/{id} | Get the enrollment user.
[**user_get_0**](UserApi.md#user_get_0) | **GET** /users | Get the enrollment user authentication result and attributes.
[**user_search_async**](UserApi.md#user_search_async) | **GET** /users/search | Search for the enrollment users.
[**user_update_user_async**](UserApi.md#user_update_user_async) | **POST** /users/{id}/update | Update the enrollment user.
[**user_upload_smime_certificates_async**](UserApi.md#user_upload_smime_certificates_async) | **POST** /users/{id}/uploadsmimecerts | Upload MIME Certificates for the enrollment user.


# **user_activate_user**
> user_activate_user(id)

Activate the enrollment user.

Activate the enrollment user by enrollment user id.  The enrollment user will be activated once the call is complete.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
id = 56 # int | The enrollment user id (Required).

try:
    # Activate the enrollment user.
    api_instance.user_activate_user(id)
except ApiException as e:
    print("Exception when calling UserApi->user_activate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The enrollment user id (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_add_user_async**
> EntityIdModel user_add_user_async(user)

Create a new enrollment user.

Create a new enrollment user with all provided information.  Validation will be performed based on the input data.  The enrollment user will be added to the system once the call is complete.  We have introduced v2 for this API, which includes enhancements, and recommend using v2 going forward.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
user = systemv1.User_() # User_ | New enrollment user to be added (Required).

try:
    # Create a new enrollment user.
    api_response = api_instance.user_add_user_async(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_add_user_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User_**](User_.md)| New enrollment user to be added (Required). | 

### Return type

[**EntityIdModel**](EntityIdModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_bulk_activate**
> BulkResponse user_bulk_activate(bulk_input)

Activate a list of enrollment users.

Activate a list of enrollment users. Enrollment user ids will be taken as input.  The list of enrollment users will be activated once the call is complete.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
bulk_input = systemv1.BulkInput() # BulkInput | A list of enrollment user ids (Required).

try:
    # Activate a list of enrollment users.
    api_response = api_instance.user_bulk_activate(bulk_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_bulk_activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| A list of enrollment user ids (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_bulk_de_activate_async**
> BulkResponse user_bulk_de_activate_async(bulk_input)

Deactivate a list of enrollment users.

Deactivate a list of enrollment users. Enrollment user ids will be taken as input.  The list of enrollment users will be deactivated once the call is complete.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
bulk_input = systemv1.BulkInput() # BulkInput | A list of enrollment user ids (Required).

try:
    # Deactivate a list of enrollment users.
    api_response = api_instance.user_bulk_de_activate_async(bulk_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_bulk_de_activate_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| A list of enrollment user ids (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_bulk_delete_async**
> BulkResponse user_bulk_delete_async(bulk_input)

Delete a list of enrollment users.

Delete a list of enrollment users. Enrollment user ids will be taken as input.  The list of enrollment users will be deleted once the call is complete.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
bulk_input = systemv1.BulkInput() # BulkInput | A list of enrollment user ids (Required).

try:
    # Delete a list of enrollment users.
    api_response = api_instance.user_bulk_delete_async(bulk_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_bulk_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| A list of enrollment user ids (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_change_location_group_async**
> user_change_location_group_async(id, target_lg)

Change the organization group of the enrollment user.

Change the organization group of the enrollment user by enrollment user id.  The organization group will be changed once the call is complete.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
id = 56 # int | The enrollment user id (Required).
target_lg = 56 # int | The new enrollment user organization group id (Required).

try:
    # Change the organization group of the enrollment user.
    api_instance.user_change_location_group_async(id, target_lg)
except ApiException as e:
    print("Exception when calling UserApi->user_change_location_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The enrollment user id (Required). | 
 **target_lg** | **int**| The new enrollment user organization group id (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_deactivate_user_async**
> user_deactivate_user_async(id)

Deactivate the enrollment user.

Deactivate the enrollment user by enrollment user id.  The enrollment user will be deactivated once the call is complete.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
id = 56 # int | The enrollment user id (Required).

try:
    # Deactivate the enrollment user.
    api_instance.user_deactivate_user_async(id)
except ApiException as e:
    print("Exception when calling UserApi->user_deactivate_user_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The enrollment user id (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete_async**
> user_delete_async(id)

Delete the enrollment user.

Delete the enrollment user by enrollment user id.  The enrollment user will be deleted from system once the call is complete.  We have introduced v2 for this API, which includes enhancements, and recommend using v2 going forward.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
id = 56 # int | The enrollment user id (Required).

try:
    # Delete the enrollment user.
    api_instance.user_delete_async(id)
except ApiException as e:
    print("Exception when calling UserApi->user_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The enrollment user id (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> User_ user_get(id)

Get the enrollment user.

Get the enrollment user information by enrollment user id.  The enrollment user information will be present once the call is complete.  We have introduced v2 for this API, which includes enhancements, and recommend using v2 going forward.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
id = 56 # int | The enrollment user id (Required).

try:
    # Get the enrollment user.
    api_response = api_instance.user_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The enrollment user id (Required). | 

### Return type

[**User_**](User_.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_0**
> UserModel user_get_0(attributes=attributes)

Get the enrollment user authentication result and attributes.

Get the enrollment user authentication result and attributes by enrollment user credential and attributes flag.  Enrollment user credential will be used as the authorization header to get enrollment user information.  Attributes will be returned together with authentication result if attributes flag is set to true, otherwise only authentication result is returned.  The enrollment user authentication result and/or attributes will be present once the call is complete.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
attributes =  # bool | Attributes flag indicating whether to return enrollment user attributes. (optional) (default to )

try:
    # Get the enrollment user authentication result and attributes.
    api_response = api_instance.user_get_0(attributes=attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributes** | **bool**| Attributes flag indicating whether to return enrollment user attributes. | [optional] [default to ]

### Return type

[**UserModel**](UserModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_search_async**
> UserSearchResult user_search_async(firstname=firstname, lastname=lastname, email=email, locationgroup_id=locationgroup_id, role=role, username=username, page=page, pagesize=pagesize, orderby=orderby, sortorder=sortorder, status=status)

Search for the enrollment users.

Search for the enrollment users based on search criteria.  FirstName, LastName, Email, LocationGroupID, Role, UserName can be used to search the enrollment users.  Paging is supported together with page number and page size.  Sorting is supported together with order by and sort order.  Supported keywords for sorting are UserName, EmailAddress, FirstName, LastName, Name - Sorts by Organization Group Name, Active, EnrollmentUserID.  A list of enrollment users will be present once the call is complete.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
firstname = '' # str | The enrollment user first name to search for. (optional) (default to )
lastname = '' # str | The enrollment user last name to search for. (optional) (default to )
email = '' # str | The enrollment user email address to search for. (optional) (default to )
locationgroup_id = 56 # int | The enrollment user location group id to search for. (optional)
role = '' # str | The enrollment user role to search for. (optional) (default to )
username = '' # str | The enrollment user username to search for. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)
orderby = '' # str | The attribute sort based on. (optional) (default to )
sortorder = '' # str | The sort order, ASC for ascending and DESC for descending. (optional) (default to )
status = '' # str | The admin status. Allowed values are Active or Inactive. Defaults to all, if this attribute is not specified. (optional) (default to )

try:
    # Search for the enrollment users.
    api_response = api_instance.user_search_async(firstname=firstname, lastname=lastname, email=email, locationgroup_id=locationgroup_id, role=role, username=username, page=page, pagesize=pagesize, orderby=orderby, sortorder=sortorder, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firstname** | **str**| The enrollment user first name to search for. | [optional] [default to ]
 **lastname** | **str**| The enrollment user last name to search for. | [optional] [default to ]
 **email** | **str**| The enrollment user email address to search for. | [optional] [default to ]
 **locationgroup_id** | **int**| The enrollment user location group id to search for. | [optional] 
 **role** | **str**| The enrollment user role to search for. | [optional] [default to ]
 **username** | **str**| The enrollment user username to search for. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 
 **orderby** | **str**| The attribute sort based on. | [optional] [default to ]
 **sortorder** | **str**| The sort order, ASC for ascending and DESC for descending. | [optional] [default to ]
 **status** | **str**| The admin status. Allowed values are Active or Inactive. Defaults to all, if this attribute is not specified. | [optional] [default to ]

### Return type

[**UserSearchResult**](UserSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update_user_async**
> user_update_user_async(id, user)

Update the enrollment user.

Update the enrollment user with all provided information by enrollment user id.  Validation will be performed based on the input data.  The enrollment user will be updated in the system once the call is complete.  We have introduced v2 for this API, which includes enhancements, and recommend using v2 going forward.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
id = 56 # int | The enrollment user id (Required).
user = systemv1.User_() # User_ | The enrollment user to be updated (Required).

try:
    # Update the enrollment user.
    api_instance.user_update_user_async(id, user)
except ApiException as e:
    print("Exception when calling UserApi->user_update_user_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The enrollment user id (Required). | 
 **user** | [**User_**](User_.md)| The enrollment user to be updated (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_upload_smime_certificates_async**
> user_upload_smime_certificates_async(id, certificates)

Upload MIME Certificates for the enrollment user.

Upload MIME certificates for the enrollment user by enrollment user id.  MIME certificates will be uploaded for the enrollment user once the call is complete.

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
api_instance = systemv1.UserApi(systemv1.ApiClient(configuration))
id = 56 # int | The enrollment user id (Required).
certificates = systemv1.SMIMECertificate() # SMIMECertificate | The MIME certificate details (Required).

try:
    # Upload MIME Certificates for the enrollment user.
    api_instance.user_upload_smime_certificates_async(id, certificates)
except ApiException as e:
    print("Exception when calling UserApi->user_upload_smime_certificates_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The enrollment user id (Required). | 
 **certificates** | [**SMIMECertificate**](SMIMECertificate.md)| The MIME certificate details (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

