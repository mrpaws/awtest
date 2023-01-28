# systemv1.AndroidWorkApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**android_work_get_android_work_settings**](AndroidWorkApi.md#android_work_get_android_work_settings) | **GET** /groups/{id}/androidwork | Gets the Android Work Settings for Passed Location Group.


# **android_work_get_android_work_settings**
> AndroidWorkSetupModel android_work_get_android_work_settings(id)

Gets the Android Work Settings for Passed Location Group.

Gets the Android Work Settings for Passed Location Group and Settings consists of EnterpriseId, ServiceAccountAdminEmail, ServiceAccountEmail and ServiceAccountClientId.

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
api_instance = systemv1.AndroidWorkApi(systemv1.ApiClient(configuration))
id = 56 # int | LocationGroup Id.

try:
    # Gets the Android Work Settings for Passed Location Group.
    api_response = api_instance.android_work_get_android_work_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AndroidWorkApi->android_work_get_android_work_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| LocationGroup Id. | 

### Return type

[**AndroidWorkSetupModel**](AndroidWorkSetupModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

