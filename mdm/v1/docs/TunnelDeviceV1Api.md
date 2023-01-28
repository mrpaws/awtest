# mdmv1.TunnelDeviceV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tunnel_device_v1_get_device_details_async**](TunnelDeviceV1Api.md#tunnel_device_v1_get_device_details_async) | **GET** /tunnel/devices/udid/{udid} | New - Retrieves list of devices that are clients to Airwatch Tunnel.
[**tunnel_device_v1_get_devices_details_async**](TunnelDeviceV1Api.md#tunnel_device_v1_get_devices_details_async) | **GET** /tunnel/devices | New - Retrieves list of devices that are clients to Airwatch Tunnel.


# **tunnel_device_v1_get_device_details_async**
> DevicesDataV2Model tunnel_device_v1_get_device_details_async(udid)

New - Retrieves list of devices that are clients to Airwatch Tunnel.

This retrieves list of devices that are clients to Airwatch Tunnel.

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
api_instance = mdmv1.TunnelDeviceV1Api(mdmv1.ApiClient(configuration))
udid = 'udid_example' # str | Device udid.

try:
    # New - Retrieves list of devices that are clients to Airwatch Tunnel.
    api_response = api_instance.tunnel_device_v1_get_device_details_async(udid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TunnelDeviceV1Api->tunnel_device_v1_get_device_details_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **udid** | **str**| Device udid. | 

### Return type

[**DevicesDataV2Model**](DevicesDataV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/xml;version=1, application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnel_device_v1_get_devices_details_async**
> DevicesDataV2Model tunnel_device_v1_get_devices_details_async(udid=udid, page_number=page_number, page_size=page_size)

New - Retrieves list of devices that are clients to Airwatch Tunnel.

This retrieves list of devices that are clients to Airwatch Tunnel.

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
api_instance = mdmv1.TunnelDeviceV1Api(mdmv1.ApiClient(configuration))
udid = '' # str | The device udid. (optional) (default to )
page_number = 56 # int |  (optional)
page_size = 56 # int | The size of the page. (optional)

try:
    # New - Retrieves list of devices that are clients to Airwatch Tunnel.
    api_response = api_instance.tunnel_device_v1_get_devices_details_async(udid=udid, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TunnelDeviceV1Api->tunnel_device_v1_get_devices_details_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **udid** | **str**| The device udid. | [optional] [default to ]
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**| The size of the page. | [optional] 

### Return type

[**DevicesDataV2Model**](DevicesDataV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/xml;version=1, application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

