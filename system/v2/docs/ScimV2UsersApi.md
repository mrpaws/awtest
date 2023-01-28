# systemv2.ScimV2UsersApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scim_v2_users_get_user_by_uuid**](ScimV2UsersApi.md#scim_v2_users_get_user_by_uuid) | **GET** /scim/v2/Users/{uuid} | New - Get a user by UUID


# **scim_v2_users_get_user_by_uuid**
> UserResponse scim_v2_users_get_user_by_uuid(uuid)

New - Get a user by UUID

Get the user by UUID.

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
api_instance = systemv2.ScimV2UsersApi(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier of an user(Required)

try:
    # New - Get a user by UUID
    api_response = api_instance.scim_v2_users_get_user_by_uuid(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScimV2UsersApi->scim_v2_users_get_user_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier of an user(Required) | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

