# mdmv1.DeviceSmartGroupsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_smart_groups_get_smart_groups_assigned_to_device_async**](DeviceSmartGroupsApi.md#device_smart_groups_get_smart_groups_assigned_to_device_async) | **GET** /devices/{id}/smartgroups | Retrieves all the smart groups associated with the device.


# **device_smart_groups_get_smart_groups_assigned_to_device_async**
> SmartGroupsAssignedToDeviceResult device_smart_groups_get_smart_groups_assigned_to_device_async(id)

Retrieves all the smart groups associated with the device.

Retrieves all the smart groups with their respective ID and Name associated to the device identfied by the device identifier.

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
api_instance = mdmv1.DeviceSmartGroupsApi(mdmv1.ApiClient(configuration))
id = 56 # int | Device Identifier (Required).

try:
    # Retrieves all the smart groups associated with the device.
    api_response = api_instance.device_smart_groups_get_smart_groups_assigned_to_device_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSmartGroupsApi->device_smart_groups_get_smart_groups_assigned_to_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device Identifier (Required). | 

### Return type

[**SmartGroupsAssignedToDeviceResult**](SmartGroupsAssignedToDeviceResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

