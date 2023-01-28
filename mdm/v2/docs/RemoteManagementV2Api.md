# mdmv2.RemoteManagementV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remote_management_v2_initiate_rm_session_async**](RemoteManagementV2Api.md#remote_management_v2_initiate_rm_session_async) | **POST** /remote-management/devices/{deviceUuid}/session | New - Initiates a Remote Management session.


# **remote_management_v2_initiate_rm_session_async**
> RemoteManagementSessionResponseV2Model remote_management_v2_initiate_rm_session_async(device_uuid, request_body)

New - Initiates a Remote Management session.

Initiates a Remote Management session with the device for the specified tool name and gets the Remote Management session URL.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.RemoteManagementV2Api(mdmv2.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Unique identifier for the Device.(Required)
request_body = mdmv2.RemoteManagementSessionRequestV2Model() # RemoteManagementSessionRequestV2Model | Model containing tool name for the Remote Management session.(Required).

try:
    # New - Initiates a Remote Management session.
    api_response = api_instance.remote_management_v2_initiate_rm_session_async(device_uuid, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteManagementV2Api->remote_management_v2_initiate_rm_session_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Unique identifier for the Device.(Required) | 
 **request_body** | [**RemoteManagementSessionRequestV2Model**](RemoteManagementSessionRequestV2Model.md)| Model containing tool name for the Remote Management session.(Required). | 

### Return type

[**RemoteManagementSessionResponseV2Model**](RemoteManagementSessionResponseV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

