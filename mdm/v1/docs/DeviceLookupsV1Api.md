# mdmv1.DeviceLookupsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_lookups_v1_get_lookup_bundle_async**](DeviceLookupsV1Api.md#device_lookups_v1_get_lookup_bundle_async) | **GET** /users/{userUuid}/devices/{deviceUuid}/lookups | New - GetLookupBundle


# **device_lookups_v1_get_lookup_bundle_async**
> list[Lookup] device_lookups_v1_get_lookup_bundle_async(user_uuid, device_uuid)

New - GetLookupBundle

An API endpoint to Lookup server-side device / user attributes not available on the device.

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
api_instance = mdmv1.DeviceLookupsV1Api(mdmv1.ApiClient(configuration))
user_uuid = 'user_uuid_example' # str | Uuid of the user.(Required)
device_uuid = 'device_uuid_example' # str | Uuid of the device.(Required)

try:
    # New - GetLookupBundle
    api_response = api_instance.device_lookups_v1_get_lookup_bundle_async(user_uuid, device_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceLookupsV1Api->device_lookups_v1_get_lookup_bundle_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | [**str**](.md)| Uuid of the user.(Required) | 
 **device_uuid** | [**str**](.md)| Uuid of the device.(Required) | 

### Return type

[**list[Lookup]**](Lookup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

