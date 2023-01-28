# systemv1.AppContentApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_content_get_app_content_storage_info**](AppContentApi.md#app_content_get_app_content_storage_info) | **GET** /groups/{ogid}/storage | Fetches Application and Content storage informations for Organization Group.


# **app_content_get_app_content_storage_info**
> AppContentStorageEntity app_content_get_app_content_storage_info(ogid)

Fetches Application and Content storage informations for Organization Group.

Provides application and content storage information for the specified Organization Group.

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
api_instance = systemv1.AppContentApi(systemv1.ApiClient(configuration))
ogid = 56 # int | The Organization Group ID.(Required).

try:
    # Fetches Application and Content storage informations for Organization Group.
    api_response = api_instance.app_content_get_app_content_storage_info(ogid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppContentApi->app_content_get_app_content_storage_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ogid** | **int**| The Organization Group ID.(Required). | 

### Return type

[**AppContentStorageEntity**](AppContentStorageEntity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

