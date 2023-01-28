# mdmv1.DeviceAttributesV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_attributes_v1_load_device_model_details_async**](DeviceAttributesV1Api.md#device_attributes_v1_load_device_model_details_async) | **POST** /devices/model-details | New - Load device model details for given device manufacturers.


# **device_attributes_v1_load_device_model_details_async**
> DeviceModelDetailsSearchResponseV1Model device_attributes_v1_load_device_model_details_async(device_model_details_search_request)

New - Load device model details for given device manufacturers.

Return the list of device models available in UEM for the given device manufacturers.

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
api_instance = mdmv1.DeviceAttributesV1Api(mdmv1.ApiClient(configuration))
device_model_details_search_request = mdmv1.DeviceModelDetailsSearchRequestV1Model() # DeviceModelDetailsSearchRequestV1Model | Request model to search the device model details.(Required).

try:
    # New - Load device model details for given device manufacturers.
    api_response = api_instance.device_attributes_v1_load_device_model_details_async(device_model_details_search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceAttributesV1Api->device_attributes_v1_load_device_model_details_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_model_details_search_request** | [**DeviceModelDetailsSearchRequestV1Model**](DeviceModelDetailsSearchRequestV1Model.md)| Request model to search the device model details.(Required). | 

### Return type

[**DeviceModelDetailsSearchResponseV1Model**](DeviceModelDetailsSearchResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

