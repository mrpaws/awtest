# mdmv1.RemoteManagementV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remote_management_v1_get_device_rm_registration_status**](RemoteManagementV1Api.md#remote_management_v1_get_device_rm_registration_status) | **GET** /remote-management/devices/{deviceUuid} | New - Gets the device&#39;s RM registration information.
[**remote_management_v1_initiate_rm_session**](RemoteManagementV1Api.md#remote_management_v1_initiate_rm_session) | **POST** /remote-management/devices/{deviceUuid}/session | New - Initiates a Remote Management session.
[**remote_management_v1_register_device_for_rm**](RemoteManagementV1Api.md#remote_management_v1_register_device_for_rm) | **POST** /remote-management/devices/{deviceUuid} | New - Registers the device with RM4 server.


# **remote_management_v1_get_device_rm_registration_status**
> DeviceRegistrationResponseV1Model remote_management_v1_get_device_rm_registration_status(device_uuid)

New - Gets the device's RM registration information.

Gets the information about device registration with the RM4 server, i.e, if the device is registered or not.

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
api_instance = mdmv1.RemoteManagementV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Unique identifier for the Device.(Required)

try:
    # New - Gets the device's RM registration information.
    api_response = api_instance.remote_management_v1_get_device_rm_registration_status(device_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteManagementV1Api->remote_management_v1_get_device_rm_registration_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Unique identifier for the Device.(Required) | 

### Return type

[**DeviceRegistrationResponseV1Model**](DeviceRegistrationResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_management_v1_initiate_rm_session**
> RemoteManagementSessionResponseV1Model remote_management_v1_initiate_rm_session(device_uuid)

New - Initiates a Remote Management session.

Initiates a Remote Management session with the device and gets the session URL.

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
api_instance = mdmv1.RemoteManagementV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Unique identifier for the Device.(Required)

try:
    # New - Initiates a Remote Management session.
    api_response = api_instance.remote_management_v1_initiate_rm_session(device_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteManagementV1Api->remote_management_v1_initiate_rm_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Unique identifier for the Device.(Required) | 

### Return type

[**RemoteManagementSessionResponseV1Model**](RemoteManagementSessionResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_management_v1_register_device_for_rm**
> RegisterDeviceResponseV1Model remote_management_v1_register_device_for_rm(device_uuid)

New - Registers the device with RM4 server.

Registers the device to the RM4 server for remote session capability.

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
api_instance = mdmv1.RemoteManagementV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Unique identifier for the Device.(Required)

try:
    # New - Registers the device with RM4 server.
    api_response = api_instance.remote_management_v1_register_device_for_rm(device_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteManagementV1Api->remote_management_v1_register_device_for_rm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Unique identifier for the Device.(Required) | 

### Return type

[**RegisterDeviceResponseV1Model**](RegisterDeviceResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

