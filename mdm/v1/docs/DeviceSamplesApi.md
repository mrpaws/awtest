# mdmv1.DeviceSamplesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_samples_save_device_samples_async**](DeviceSamplesApi.md#device_samples_save_device_samples_async) | **POST** /DeviceSamples | New - Saves the device samples


# **device_samples_save_device_samples_async**
> device_samples_save_device_samples_async(device_samples)

New - Saves the device samples

Saves the device samples

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

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
api_instance = mdmv1.DeviceSamplesApi(mdmv1.ApiClient(configuration))
device_samples = NULL # object | (Required)

try:
    # New - Saves the device samples
    api_instance.device_samples_save_device_samples_async(device_samples)
except ApiException as e:
    print("Exception when calling DeviceSamplesApi->device_samples_save_device_samples_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_samples** | **object**| (Required) | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

