# mdmv3.CommandsV3Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commands_v3_execute_async**](CommandsV3Api.md#commands_v3_execute_async) | **POST** /devices/{deviceUuid}/commands/{commandName} | New - Executes a command for a device by the device uuid.
[**commands_v3_execute_by_alternate_id_async**](CommandsV3Api.md#commands_v3_execute_by_alternate_id_async) | **POST** /devices/commands/{commandName}/device/{searchBy}/{id} | New - Executes a command for device by alternate identifier.


# **commands_v3_execute_async**
> commands_v3_execute_async(device_uuid, command_name, commands_model)

New - Executes a command for a device by the device uuid.

Executes a command for a device by device uuid. Supported commands are SetRecoveryLock (macOS only), DeviceWipe (macOS only).

### Example
```python
from __future__ import print_function
import time
import mdmv3
from mdmv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv3.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv3.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv3.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv3.CommandsV3Api(mdmv3.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | The Device unique identifier.              Accepted format is **guid**              E.g. 0258902A-9E0C-4DC5-A997-9E079559F75E(Required).
command_name = 'command_name_example' # str | The name of the command to execute. Supported command types [SetRecoveryLock, DeviceWipe].(Required).
commands_model = mdmv3.CommandsV3Model() # CommandsV3Model | Request containing the command options.(Required).

try:
    # New - Executes a command for a device by the device uuid.
    api_instance.commands_v3_execute_async(device_uuid, command_name, commands_model)
except ApiException as e:
    print("Exception when calling CommandsV3Api->commands_v3_execute_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| The Device unique identifier.              Accepted format is **guid**              E.g. 0258902A-9E0C-4DC5-A997-9E079559F75E(Required). | 
 **command_name** | **str**| The name of the command to execute. Supported command types [SetRecoveryLock, DeviceWipe].(Required). | 
 **commands_model** | [**CommandsV3Model**](CommandsV3Model.md)| Request containing the command options.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v3_execute_by_alternate_id_async**
> commands_v3_execute_by_alternate_id_async(command_name, search_by, id, commands_model)

New - Executes a command for device by alternate identifier.

Executes a command for the specified device alternate identifier. Supported commands are SetRecoveryLock (macOS only), DeviceWipe (macOS only).

### Example
```python
from __future__ import print_function
import time
import mdmv3
from mdmv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv3.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv3.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv3.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv3.CommandsV3Api(mdmv3.ApiClient(configuration))
command_name = 'command_name_example' # str | The name of the command to execute. Supported command types [SetRecoveryLock, DeviceWipe].(Required).
search_by = 'search_by_example' # str | Search by Alternate Id type [MacAddress, Udid, SerialNumber, ImeiNumber, EasId].(Required).
id = 'id_example' # str | The Alternate Id.(Required).
commands_model = mdmv3.CommandsV3Model() # CommandsV3Model | Request with command specific options.(Required).

try:
    # New - Executes a command for device by alternate identifier.
    api_instance.commands_v3_execute_by_alternate_id_async(command_name, search_by, id, commands_model)
except ApiException as e:
    print("Exception when calling CommandsV3Api->commands_v3_execute_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_name** | **str**| The name of the command to execute. Supported command types [SetRecoveryLock, DeviceWipe].(Required). | 
 **search_by** | **str**| Search by Alternate Id type [MacAddress, Udid, SerialNumber, ImeiNumber, EasId].(Required). | 
 **id** | **str**| The Alternate Id.(Required). | 
 **commands_model** | [**CommandsV3Model**](CommandsV3Model.md)| Request with command specific options.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

