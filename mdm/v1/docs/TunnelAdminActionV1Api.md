# mdmv1.TunnelAdminActionV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tunnel_admin_action_v1_get_tunnel_admin_actions_info_async**](TunnelAdminActionV1Api.md#tunnel_admin_action_v1_get_tunnel_admin_actions_info_async) | **GET** /tunnel/devices/{deviceUuid}/action | New - Gets the device access information.
[**tunnel_admin_action_v1_perform_console_admin_action_async**](TunnelAdminActionV1Api.md#tunnel_admin_action_v1_perform_console_admin_action_async) | **POST** /tunnel/devices/{deviceUuid}/action | New - Perform the operation on tunnel device.


# **tunnel_admin_action_v1_get_tunnel_admin_actions_info_async**
> TunnelAccessV1Model tunnel_admin_action_v1_get_tunnel_admin_actions_info_async(device_uuid)

New - Gets the device access information.

It is used to get the device access information.

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
api_instance = mdmv1.TunnelAdminActionV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | (Required).

try:
    # New - Gets the device access information.
    api_response = api_instance.tunnel_admin_action_v1_get_tunnel_admin_actions_info_async(device_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TunnelAdminActionV1Api->tunnel_admin_action_v1_get_tunnel_admin_actions_info_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| (Required). | 

### Return type

[**TunnelAccessV1Model**](TunnelAccessV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnel_admin_action_v1_perform_console_admin_action_async**
> tunnel_admin_action_v1_perform_console_admin_action_async(device_uuid, action_request_model)

New - Perform the operation on tunnel device.

It is used to perform the console admin action for tunnel devices.

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
api_instance = mdmv1.TunnelAdminActionV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | (Required).
action_request_model = mdmv1.TunnelConsoleActionRequestModel() # TunnelConsoleActionRequestModel | (Required).

try:
    # New - Perform the operation on tunnel device.
    api_instance.tunnel_admin_action_v1_perform_console_admin_action_async(device_uuid, action_request_model)
except ApiException as e:
    print("Exception when calling TunnelAdminActionV1Api->tunnel_admin_action_v1_perform_console_admin_action_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| (Required). | 
 **action_request_model** | [**TunnelConsoleActionRequestModel**](TunnelConsoleActionRequestModel.md)| (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

