# mdmv1.DeviceLogV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_log_v1_get_device_log_by_source_async**](DeviceLogV1Api.md#device_log_v1_get_device_log_by_source_async) | **GET** /devices/{deviceUuid}/sources/{sourceUuid}/logs | New - Gets the logs associated with particular source from device.


# **device_log_v1_get_device_log_by_source_async**
> list[DeviceLogResponse] device_log_v1_get_device_log_by_source_async(device_uuid, source_uuid, generated_after=generated_after, generated_before=generated_before, limit=limit, offset=offset, sort_order=sort_order)

New - Gets the logs associated with particular source from device.

Get the logs of device that belong to each source Id.

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
api_instance = mdmv1.DeviceLogV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Unique Identifier for the device.(Required).
source_uuid = 'source_uuid_example' # str | Unique Identifier for the source associated with log.(Required).
generated_after = '' # datetime | Logs generated after the timestamp. (optional) (default to )
generated_before = '' # datetime | Logs generated before the timestamp. (optional) (default to )
limit = 56 # int | Max numbers of records to be retrieved. (optional)
offset = 56 # int | Current position of the result set. (optional)
sort_order =  # object | Sort order. (optional) (default to )

try:
    # New - Gets the logs associated with particular source from device.
    api_response = api_instance.device_log_v1_get_device_log_by_source_async(device_uuid, source_uuid, generated_after=generated_after, generated_before=generated_before, limit=limit, offset=offset, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceLogV1Api->device_log_v1_get_device_log_by_source_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Unique Identifier for the device.(Required). | 
 **source_uuid** | [**str**](.md)| Unique Identifier for the source associated with log.(Required). | 
 **generated_after** | **datetime**| Logs generated after the timestamp. | [optional] [default to ]
 **generated_before** | **datetime**| Logs generated before the timestamp. | [optional] [default to ]
 **limit** | **int**| Max numbers of records to be retrieved. | [optional] 
 **offset** | **int**| Current position of the result set. | [optional] 
 **sort_order** | [**object**](.md)| Sort order. | [optional] [default to ]

### Return type

[**list[DeviceLogResponse]**](DeviceLogResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

