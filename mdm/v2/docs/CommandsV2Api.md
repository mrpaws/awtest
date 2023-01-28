# mdmv2.CommandsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commands_v2_bulk_execute_async**](CommandsV2Api.md#commands_v2_bulk_execute_async) | **POST** /devices/commands/{commandName} | New - Executes command for multiple devices identified by device uuid
[**commands_v2_execute_async**](CommandsV2Api.md#commands_v2_execute_async) | **POST** /devices/{deviceUuid}/commands/{commandName} | New - Executes a command for device by device uuid
[**commands_v2_execute_by_alternate_id_async**](CommandsV2Api.md#commands_v2_execute_by_alternate_id_async) | **POST** /devices/commands/{commandName}/device/{searchBy}/{id} | New - Executes a command for device by alternate ID


# **commands_v2_bulk_execute_async**
> commands_v2_bulk_execute_async(command_name, bulk_commands_model)

New - Executes command for multiple devices identified by device uuid

Executes command for multiple devices identified by device uuid. Supported commands are Lock, SyncSensors (macOS only), and DeviceWipe.

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
api_instance = mdmv2.CommandsV2Api(mdmv2.ApiClient(configuration))
command_name = 'command_name_example' # str | The command to execute [Lock, DeviceWipe, SyncSensors].(Required)
bulk_commands_model = mdmv2.BulkCommandsV2Model() # BulkCommandsV2Model | Model containing list of device uuids and Unlock PIN.              The **unlock_pin** is applicable only for the macOS devices and it is required for Lock and DeviceWipe commands. Warning - This device cannot be unlocked remotely and can only be unlocked using a 6-digit pin entered. Write this PIN down and store it in a safe place. If you forget your PIN you must contact Apple to unlock your device.              The **sensor_name** is applicable only for macOS and Linux platform and it is required for the SyncSensors command.(Required)

try:
    # New - Executes command for multiple devices identified by device uuid
    api_instance.commands_v2_bulk_execute_async(command_name, bulk_commands_model)
except ApiException as e:
    print("Exception when calling CommandsV2Api->commands_v2_bulk_execute_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_name** | **str**| The command to execute [Lock, DeviceWipe, SyncSensors].(Required) | 
 **bulk_commands_model** | [**BulkCommandsV2Model**](BulkCommandsV2Model.md)| Model containing list of device uuids and Unlock PIN.              The **unlock_pin** is applicable only for the macOS devices and it is required for Lock and DeviceWipe commands. Warning - This device cannot be unlocked remotely and can only be unlocked using a 6-digit pin entered. Write this PIN down and store it in a safe place. If you forget your PIN you must contact Apple to unlock your device.              The **sensor_name** is applicable only for macOS and Linux platform and it is required for the SyncSensors command.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v2_execute_async**
> commands_v2_execute_async(device_uuid, command_name, commands_model)

New - Executes a command for device by device uuid

Executes a command for device by device uuid. Supported commands are Lock, DeviceWipe, logout-user (iOS only), delete-user (iOS only), user-list (iOS only), SyncSensors (macOS only), suspend-bitlocker (Windows only), resume-bitlocker (Windows only).

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
api_instance = mdmv2.CommandsV2Api(mdmv2.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Device Uuid.              Accepted format is **guid**              E.g. 0258902A-9E0C-4DC5-A997-9E079559F75E(Required)
command_name = 'command_name_example' # str | The command to execute [Lock, DeviceWipe, logout-user, delete-user, user-list, SyncSensors, suspend-bitlocker, resume-bitlocker].(Required)
commands_model = mdmv2.CommandsV2Model() # CommandsV2Model | Model containing option values to the API.              The **unlock_pin** is applicable only for the macOS devices and it is required for Lock and DeviceWipe commands. Warning - This device cannot be unlocked remotely and can only be unlocked using a 6-digit pin entered. Write this PIN down and store it in a safe place. If you forget your PIN you must contact Apple to unlock your device.              The **sensor_names** is applicable only for macOS and Linux platform and it is required for the SyncSensors command.(Required)

try:
    # New - Executes a command for device by device uuid
    api_instance.commands_v2_execute_async(device_uuid, command_name, commands_model)
except ApiException as e:
    print("Exception when calling CommandsV2Api->commands_v2_execute_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Device Uuid.              Accepted format is **guid**              E.g. 0258902A-9E0C-4DC5-A997-9E079559F75E(Required) | 
 **command_name** | **str**| The command to execute [Lock, DeviceWipe, logout-user, delete-user, user-list, SyncSensors, suspend-bitlocker, resume-bitlocker].(Required) | 
 **commands_model** | [**CommandsV2Model**](CommandsV2Model.md)| Model containing option values to the API.              The **unlock_pin** is applicable only for the macOS devices and it is required for Lock and DeviceWipe commands. Warning - This device cannot be unlocked remotely and can only be unlocked using a 6-digit pin entered. Write this PIN down and store it in a safe place. If you forget your PIN you must contact Apple to unlock your device.              The **sensor_names** is applicable only for macOS and Linux platform and it is required for the SyncSensors command.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v2_execute_by_alternate_id_async**
> CommandsResponseV2Model commands_v2_execute_by_alternate_id_async(command_name, search_by, id, commands_model)

New - Executes a command for device by alternate ID

Execute commands for specified device ID. Supported commands are ClearPasscode, DeviceWipe, Lock, SyncSensors (macOS only), enable-activation-lock (iOS and macOS only), logout-user (iOS only), delete-user (iOS only), user-list (iOS only), refresh-esim (iOS only), suspend-bitlocker (Windows only), resume-bitlocker (Windows only).

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
api_instance = mdmv2.CommandsV2Api(mdmv2.ApiClient(configuration))
command_name = 'command_name_example' # str | The command to execute [ClearPasscode, DeviceWipe, Lock, SyncSensors, delete-user, enable-activation-lock, logout-user, refresh-esim, user-list, suspend-bitlocker, resume-bitlocker].(Required)
search_by = 'search_by_example' # str | Search by alternate ID type [MacAddress, Udid, SerialNumber, ImeiNumber, EasId].(Required)
id = 'id_example' # str | ID(Required)
commands_model = mdmv2.CommandsV2Model() # CommandsV2Model | Model containing option values to the API.              The **unlock_pin** is applicable only for the macOS devices and it is required for Lock and DeviceWipe commands. Warning - This device cannot be unlocked remotely and can only be unlocked using a 6-digit pin entered. Write this PIN down and store it in a safe place. If you forget your PIN you must contact Apple to unlock your device.              The **message** can be optionally provided for Lock which will be displayed on the device lock screen. Max allowed length is 256 chars.              The **sensor_names** is applicable only for macOS and Linux platform and it is required for the SyncSensors command.(Required)

try:
    # New - Executes a command for device by alternate ID
    api_response = api_instance.commands_v2_execute_by_alternate_id_async(command_name, search_by, id, commands_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsV2Api->commands_v2_execute_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_name** | **str**| The command to execute [ClearPasscode, DeviceWipe, Lock, SyncSensors, delete-user, enable-activation-lock, logout-user, refresh-esim, user-list, suspend-bitlocker, resume-bitlocker].(Required) | 
 **search_by** | **str**| Search by alternate ID type [MacAddress, Udid, SerialNumber, ImeiNumber, EasId].(Required) | 
 **id** | **str**| ID(Required) | 
 **commands_model** | [**CommandsV2Model**](CommandsV2Model.md)| Model containing option values to the API.              The **unlock_pin** is applicable only for the macOS devices and it is required for Lock and DeviceWipe commands. Warning - This device cannot be unlocked remotely and can only be unlocked using a 6-digit pin entered. Write this PIN down and store it in a safe place. If you forget your PIN you must contact Apple to unlock your device.              The **message** can be optionally provided for Lock which will be displayed on the device lock screen. Max allowed length is 256 chars.              The **sensor_names** is applicable only for macOS and Linux platform and it is required for the SyncSensors command.(Required) | 

### Return type

[**CommandsResponseV2Model**](CommandsResponseV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

