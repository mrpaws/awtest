# mdmv1.UsersApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get_device_user_by_alternateid**](UsersApi.md#users_get_device_user_by_alternateid) | **GET** /devices/user | Retrieves the user details of the device identified by the alternate ID.
[**users_get_device_user_by_id**](UsersApi.md#users_get_device_user_by_id) | **GET** /devices/{id}/user | Retrieves the user details of the device identified by device ID.


# **users_get_device_user_by_alternateid**
> users_get_device_user_by_alternateid(search_by=search_by, id=id)

Retrieves the user details of the device identified by the alternate ID.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.UsersApi(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber]. (optional) (default to )
id = '' # str | Device alternate id. (optional) (default to )

try:
    # Retrieves the user details of the device identified by the alternate ID.
    api_instance.users_get_device_user_by_alternateid(search_by=search_by, id=id)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_device_user_by_alternateid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber]. | [optional] [default to ]
 **id** | **str**| Device alternate id. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_device_user_by_id**
> users_get_device_user_by_id(id)

Retrieves the user details of the device identified by device ID.

v1.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.UsersApi(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID.

try:
    # Retrieves the user details of the device identified by device ID.
    api_instance.users_get_device_user_by_id(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_device_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

