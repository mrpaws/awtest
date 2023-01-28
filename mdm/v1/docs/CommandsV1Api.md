# mdmv1.CommandsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commands_v1_bulk_execute_async**](CommandsV1Api.md#commands_v1_bulk_execute_async) | **POST** /devices/commands/bulk | Executes command for multiple devices identified by alternate ID type.
[**commands_v1_bulk_execute_schedule_os_update**](CommandsV1Api.md#commands_v1_bulk_execute_schedule_os_update) | **POST** /devices/commands/bulk/scheduleosupdate | New - Executes Schedule OS Update command for devices in bulk.
[**commands_v1_change_organization_group_async**](CommandsV1Api.md#commands_v1_change_organization_group_async) | **PUT** /devices/{id}/commands/changeorganizationgroup/{organizationgroupid} | Changes the organization group to which the device is assigned.
[**commands_v1_change_organization_group_by_alternate_id_async**](CommandsV1Api.md#commands_v1_change_organization_group_by_alternate_id_async) | **POST** /devices/commands/changeorganizationgroup | New - Changes the organization group to which the device identified by the alternate ID is assigned.
[**commands_v1_execute_async**](CommandsV1Api.md#commands_v1_execute_async) | **POST** /devices/{deviceid}/commands | New - Executes commands for the specified device.
[**commands_v1_execute_by_alternate_id_async**](CommandsV1Api.md#commands_v1_execute_by_alternate_id_async) | **POST** /devices/commands | New - Executes a command for device by alternate ID.
[**commands_v1_execute_change_container_passcode_by_alternate_id_async**](CommandsV1Api.md#commands_v1_execute_change_container_passcode_by_alternate_id_async) | **POST** /devices/commands/containerpasscode | New - Executes change passcode command for container device matching the filter criteria.
[**commands_v1_execute_change_device_passcode_async**](CommandsV1Api.md#commands_v1_execute_change_device_passcode_async) | **POST** /devices/{id}/commands/changepasscode | Executes change passcode command for device ID.
[**commands_v1_execute_change_device_passcode_by_alternate_id_async**](CommandsV1Api.md#commands_v1_execute_change_device_passcode_by_alternate_id_async) | **POST** /devices/commands/changepasscode | Executes command for change passcode of device by alternate ID.
[**commands_v1_execute_find_device_async**](CommandsV1Api.md#commands_v1_execute_find_device_async) | **POST** /devices/{deviceId}/commands/finddevice | Executes find device command for device by device id.
[**commands_v1_execute_find_device_by_alternate_id_async**](CommandsV1Api.md#commands_v1_execute_find_device_by_alternate_id_async) | **POST** /devices/commands/finddevice | Executes finddevice command for device by alternate id.
[**commands_v1_execute_request_device_log_async**](CommandsV1Api.md#commands_v1_execute_request_device_log_async) | **POST** /devices/commands/requestdevicelog | New - Executes device log request command for device matching the filter criteria.
[**commands_v1_execute_schedule_os_update_by_alternate_id_async**](CommandsV1Api.md#commands_v1_execute_schedule_os_update_by_alternate_id_async) | **POST** /devices/commands/scheduleosupdate | New - Schedule OS Update for supervised DEP devices
[**commands_v1_execute_start_air_play_async**](CommandsV1Api.md#commands_v1_execute_start_air_play_async) | **POST** /devices/{deviceid}/commands/startairplay | Executes start airplay for a specific device.
[**commands_v1_execute_start_remote_view_by_alternate_id_async**](CommandsV1Api.md#commands_v1_execute_start_remote_view_by_alternate_id_async) | **POST** /devices/commands/remoteview | New - Executes start remoteview command for device matching the filter criteria.
[**commands_v1_execute_stop_device_log_async**](CommandsV1Api.md#commands_v1_execute_stop_device_log_async) | **POST** /devices/commands/stopdevicelog | New - Executes stop device log request command for device.


# **commands_v1_bulk_execute_async**
> BulkResponse commands_v1_bulk_execute_async(bulk_input, command, searchby)

Executes command for multiple devices identified by alternate ID type.

Processes the bulk commands mentioned by command type.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
bulk_input = mdmv1.BulkInput() # BulkInput | The bulk input with list of device IDs. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837)(Required).
command = '' # str | The command to execute [EnterpriseWipe, LockDevice, ScheduleOsUpdate, SoftReset, Shutdown].(Required). (default to )
searchby = '' # str | The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber].(Required). (default to )

try:
    # Executes command for multiple devices identified by alternate ID type.
    api_response = api_instance.commands_v1_bulk_execute_async(bulk_input, command, searchby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_bulk_execute_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| The bulk input with list of device IDs. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837)(Required). | 
 **command** | **str**| The command to execute [EnterpriseWipe, LockDevice, ScheduleOsUpdate, SoftReset, Shutdown].(Required). | [default to ]
 **searchby** | **str**| The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber].(Required). | [default to ]

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_bulk_execute_schedule_os_update**
> commands_v1_bulk_execute_schedule_os_update(bulk_input, searchby, installaction)

New - Executes Schedule OS Update command for devices in bulk.

This API will execute schedule OS Update command for multiple devices. For iOS 10.3 and later, devices must be supervised. Prior to iOS 10.3, devices must be supervised and DEP enrolled. (iOS only)

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
bulk_input = mdmv1.BulkInput() # BulkInput | List of device identifiers of the type specified in the searchby parameter.(Required).
searchby = '' # str | Search by alternate id type. Possible values = [Macaddress, Udid, Serialnumber, ImeiNumber] {Formats= Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837}(Required) (default to )
installaction =  # object | Install action type for OS update. Possible Values = [Default, DownloadOnly, InstallASAP](Required) (default to )

try:
    # New - Executes Schedule OS Update command for devices in bulk.
    api_instance.commands_v1_bulk_execute_schedule_os_update(bulk_input, searchby, installaction)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_bulk_execute_schedule_os_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| List of device identifiers of the type specified in the searchby parameter.(Required). | 
 **searchby** | **str**| Search by alternate id type. Possible values &#x3D; [Macaddress, Udid, Serialnumber, ImeiNumber] {Formats&#x3D; Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837}(Required) | [default to ]
 **installaction** | [**object**](.md)| Install action type for OS update. Possible Values &#x3D; [Default, DownloadOnly, InstallASAP](Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_change_organization_group_async**
> commands_v1_change_organization_group_async(id, organizationgroupid)

Changes the organization group to which the device is assigned.

Processes the command to change organization group for the specific device. It will also check if device can be accessed or not.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | The AirWatch device ID. (Required).
organizationgroupid = 56 # int | The new organization group ID. (Required).

try:
    # Changes the organization group to which the device is assigned.
    api_instance.commands_v1_change_organization_group_async(id, organizationgroupid)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_change_organization_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The AirWatch device ID. (Required). | 
 **organizationgroupid** | **int**| The new organization group ID. (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_change_organization_group_by_alternate_id_async**
> commands_v1_change_organization_group_by_alternate_id_async(search_by, id, ogid)

New - Changes the organization group to which the device identified by the alternate ID is assigned.

Processes the command to change the organization group of the device. Performs additional checks on device to find by alternate IDs like udid, imei.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber](Required) (default to )
id = '' # str | Device alternate ID [Formats = {Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837}](Required) (default to )
ogid = 56 # int | The new organization group ID.(Required)

try:
    # New - Changes the organization group to which the device identified by the alternate ID is assigned.
    api_instance.commands_v1_change_organization_group_by_alternate_id_async(search_by, id, ogid)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_change_organization_group_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber](Required) | [default to ]
 **id** | **str**| Device alternate ID [Formats &#x3D; {Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837}](Required) | [default to ]
 **ogid** | **int**| The new organization group ID.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_async**
> commands_v1_execute_async(deviceid, command, custom_command_model=custom_command_model, reason=reason, keep_apps_on_device=keep_apps_on_device)

New - Executes commands for the specified device.

Executes the command for the device after performing necessary checks like command accessibility, device enrollment status, support for command on device etc. Supported commands are Lock, EnterpriseWipe, DeviceWipe, DeviceQuery, ClearPasscode, SyncDevice, StopAirPlay, ScheduleOsUpdate, CustomMdmCommand (iOS, macOS, and tvOS only), InstallPackagedMacOSXAgent (macOS only), SoftReset, Shutdown, EnterpriseReset, SyncSensors (macOS only), OsUpdateStatus (iOS and macOS only), RotateFileVaultKey (macOS only), RotateDEPAdminPassword (macOS only), ResetBiosPassword (WinRT only), UserList (iOS only), SyncWorkflows (macOS and WinRT only), InstallSeededScepProfile (Window only).

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
deviceid = 56 # int | Id of the device on which command is to be executed.(Required).
command = '' # str | The command to execute [Lock, EnterpriseWipe, DeviceWipe, DeviceQuery, ClearPasscode, SyncDevice, StopAirPlay, ScheduleOsUpdate, CustomMdmCommand, InstallPackagedMacOSXAgent, SoftReset, Shutdown, EnterpriseReset, SyncSensors, OsUpdateStatus, RotateFileVaultKey, RotateDEPAdminPassword, ResetBiosPassword, UserList, SyncWorkflows, InstallSeededScepProfile].(Required) (default to )
custom_command_model = mdmv1.CustomCommandModel() # CustomCommandModel | Applicable only for Apple devices. Required if the command type is CustomMdmCommand. Model containing the custom XML for the command. (optional)
reason = '' # str | Applicable only for Chrome Os Devices. Enterprise Wipe reason must be one of the following values - different_model_replacement, retiring_device, same_model_replacement. (optional) (default to )
keep_apps_on_device =  # bool | Applicable only for Windows devices and Enterprise Wipe command. Set this value to true/false to keep or remove apps on the device upon Enterprise Wipe. (optional) (default to )

try:
    # New - Executes commands for the specified device.
    api_instance.commands_v1_execute_async(deviceid, command, custom_command_model=custom_command_model, reason=reason, keep_apps_on_device=keep_apps_on_device)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceid** | **int**| Id of the device on which command is to be executed.(Required). | 
 **command** | **str**| The command to execute [Lock, EnterpriseWipe, DeviceWipe, DeviceQuery, ClearPasscode, SyncDevice, StopAirPlay, ScheduleOsUpdate, CustomMdmCommand, InstallPackagedMacOSXAgent, SoftReset, Shutdown, EnterpriseReset, SyncSensors, OsUpdateStatus, RotateFileVaultKey, RotateDEPAdminPassword, ResetBiosPassword, UserList, SyncWorkflows, InstallSeededScepProfile].(Required) | [default to ]
 **custom_command_model** | [**CustomCommandModel**](CustomCommandModel.md)| Applicable only for Apple devices. Required if the command type is CustomMdmCommand. Model containing the custom XML for the command. | [optional] 
 **reason** | **str**| Applicable only for Chrome Os Devices. Enterprise Wipe reason must be one of the following values - different_model_replacement, retiring_device, same_model_replacement. | [optional] [default to ]
 **keep_apps_on_device** | **bool**| Applicable only for Windows devices and Enterprise Wipe command. Set this value to true/false to keep or remove apps on the device upon Enterprise Wipe. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_by_alternate_id_async**
> commands_v1_execute_by_alternate_id_async(custom_command_model, searchby, id, command, reason=reason)

New - Executes a command for device by alternate ID.

Executes command for the specific device identified using an alternate ID [Macaddress, Udid, Serialnumber, ImeiNumber]. Supported commands are Lock, EnterpriseWipe, DeviceWipe, DeviceQuery, ClearPasscode, SyncDevice, StopAirPlay, ScheduleOsUpdate, CustomMdmCommand (iOS, macOS, and tvOS only), InstallPackagedMacOSXAgent (macOS only), SoftReset, Shutdown, EnterpriseReset, SyncSensors (macOS only), OsUpdateStatus (iOS and macOS only), RotateFileVaultKey (macOS only), RotateDEPAdminPassword (macOS only), InstallSeededScepProfile (Windows Only), ResetBiosPassword (WinRT only).

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
custom_command_model = mdmv1.CustomCommandModel() # CustomCommandModel | Applicable only for Apple devices. Required if the command type is CustomMdmCommand. Model containing the custom XML for the command.(Required).
searchby =  # object | Search by alternate id type(Required) (default to )
id = '' # str | Device id(Required) (default to )
command = '' # str | The command to execute [Lock, EnterpriseWipe, DeviceWipe, DeviceQuery, ClearPasscode, SyncDevice, StopAirPlay, ScheduleOsUpdate, CustomMdmCommand, InstallPackagedMacOSXAgent, SoftReset, Shutdown, EnterpriseReset, SyncSensors, OsUpdateStatus, RotateFileVaultKey, RotateDEPAdminPassword, InstallSeededScepProfile, ResetBiosPassword].(Required) (default to )
reason = '' # str | Applicable only for Chrome Os Devices. Enterprise Wipe reason must be one of the following values - different_model_replacement, retiring_device, same_model_replacement. (optional) (default to )

try:
    # New - Executes a command for device by alternate ID.
    api_instance.commands_v1_execute_by_alternate_id_async(custom_command_model, searchby, id, command, reason=reason)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_command_model** | [**CustomCommandModel**](CustomCommandModel.md)| Applicable only for Apple devices. Required if the command type is CustomMdmCommand. Model containing the custom XML for the command.(Required). | 
 **searchby** | [**object**](.md)| Search by alternate id type(Required) | [default to ]
 **id** | **str**| Device id(Required) | [default to ]
 **command** | **str**| The command to execute [Lock, EnterpriseWipe, DeviceWipe, DeviceQuery, ClearPasscode, SyncDevice, StopAirPlay, ScheduleOsUpdate, CustomMdmCommand, InstallPackagedMacOSXAgent, SoftReset, Shutdown, EnterpriseReset, SyncSensors, OsUpdateStatus, RotateFileVaultKey, RotateDEPAdminPassword, InstallSeededScepProfile, ResetBiosPassword].(Required) | [default to ]
 **reason** | **str**| Applicable only for Chrome Os Devices. Enterprise Wipe reason must be one of the following values - different_model_replacement, retiring_device, same_model_replacement. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_change_container_passcode_by_alternate_id_async**
> commands_v1_execute_change_container_passcode_by_alternate_id_async(passcode, searchby, id)

New - Executes change passcode command for container device matching the filter criteria.

This will change the knox container passcode with the provided new passcode for the device matching the device criteria.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
passcode = mdmv1.ContainerPasscodeV1Model() # ContainerPasscodeV1Model | New container passcode(Required).
searchby =  # object | Search by alternate id type(Required) (default to )
id = '' # str | Device id(Required) (default to )

try:
    # New - Executes change passcode command for container device matching the filter criteria.
    api_instance.commands_v1_execute_change_container_passcode_by_alternate_id_async(passcode, searchby, id)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_change_container_passcode_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **passcode** | [**ContainerPasscodeV1Model**](ContainerPasscodeV1Model.md)| New container passcode(Required). | 
 **searchby** | [**object**](.md)| Search by alternate id type(Required) | [default to ]
 **id** | **str**| Device id(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_change_device_passcode_async**
> commands_v1_execute_change_device_passcode_async(id, passcode)

Executes change passcode command for device ID.

Processes change passcode command for the specific device with passcode provided. Performs necessary checks regarding device ID and its enrollment.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID (Required).
passcode = mdmv1.DevicePasscode() # DevicePasscode | New passcode value which needs to be set in the device. (Required).

try:
    # Executes change passcode command for device ID.
    api_instance.commands_v1_execute_change_device_passcode_async(id, passcode)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_change_device_passcode_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID (Required). | 
 **passcode** | [**DevicePasscode**](DevicePasscode.md)| New passcode value which needs to be set in the device. (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_change_device_passcode_by_alternate_id_async**
> commands_v1_execute_change_device_passcode_by_alternate_id_async(search_by, id, passcode=passcode)

Executes command for change passcode of device by alternate ID.

Processes command for change passcode with device alternate ID. It also performs additional checks if device is enrolled or not.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837) (Required). (default to )
id = '' # str | The alternate ID of the device. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837)(Required). (default to )
passcode = mdmv1.DevicePasscode() # DevicePasscode | The change passcode request. (optional)

try:
    # Executes command for change passcode of device by alternate ID.
    api_instance.commands_v1_execute_change_device_passcode_by_alternate_id_async(search_by, id, passcode=passcode)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_change_device_passcode_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837) (Required). | [default to ]
 **id** | **str**| The alternate ID of the device. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837)(Required). | [default to ]
 **passcode** | [**DevicePasscode**](DevicePasscode.md)| The change passcode request. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_find_device_async**
> commands_v1_execute_find_device_async(device_id, find_device=find_device)

Executes find device command for device by device id.

v1.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
device_id = 56 # int | The AirWatch Device Id.
find_device = mdmv1.FindDevice() # FindDevice | The find device request. (optional)

try:
    # Executes find device command for device by device id.
    api_instance.commands_v1_execute_find_device_async(device_id, find_device=find_device)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_find_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The AirWatch Device Id. | 
 **find_device** | [**FindDevice**](FindDevice.md)| The find device request. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_find_device_by_alternate_id_async**
> commands_v1_execute_find_device_by_alternate_id_async(find_device=find_device, search_by=search_by, id=id)

Executes finddevice command for device by alternate id.

API to Executes finddevice command for device by alternate id as [Macaddress, Udid, Serialnumber, ImeiNumber].

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
find_device = mdmv1.FindDevice() # FindDevice | The find device request. (optional)
search_by = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837). (optional) (default to )
id = '' # str | The alternate id. (optional) (default to )

try:
    # Executes finddevice command for device by alternate id.
    api_instance.commands_v1_execute_find_device_by_alternate_id_async(find_device=find_device, search_by=search_by, id=id)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_find_device_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find_device** | [**FindDevice**](FindDevice.md)| The find device request. | [optional] 
 **search_by** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837). | [optional] [default to ]
 **id** | **str**| The alternate id. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_request_device_log_async**
> commands_v1_execute_request_device_log_async(log_params, searchby, id)

New - Executes device log request command for device matching the filter criteria.

This api will execute deviceLog command on the device matching the filter criteria. The logs will become available to an admin on AirWatch Console.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
log_params = mdmv1.DeviceLogRequestV1Model() # DeviceLogRequestV1Model | Contains parameters for device log request.(Required).
searchby = '' # str | Search by alternate id type. Possible values = [Macaddress, Udid, Serialnumber, ImeiNumber] {Formats= Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837}(Required) (default to )
id = '' # str | Device id(Required) (default to )

try:
    # New - Executes device log request command for device matching the filter criteria.
    api_instance.commands_v1_execute_request_device_log_async(log_params, searchby, id)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_request_device_log_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_params** | [**DeviceLogRequestV1Model**](DeviceLogRequestV1Model.md)| Contains parameters for device log request.(Required). | 
 **searchby** | **str**| Search by alternate id type. Possible values &#x3D; [Macaddress, Udid, Serialnumber, ImeiNumber] {Formats&#x3D; Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837}(Required) | [default to ]
 **id** | **str**| Device id(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_schedule_os_update_by_alternate_id_async**
> commands_v1_execute_schedule_os_update_by_alternate_id_async(osupdateproductkeys, searchby, id, installaction, osupdateproductversion=osupdateproductversion)

New - Schedule OS Update for supervised DEP devices

Executes the Schedule OS Update command on the specified device. For iOS 10.3 and later, devices must be supervised. Prior to iOS 10.3, devices must be supervised and DEP enrolled. For macOS, the device must be DEP enrolled.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
osupdateproductkeys = [mdmv1.list[str]()] # list[str] | List of macOS Update product keys. This field is required and only for macOS devices. Ex. [\"macOSUpdate15D100\"](Required).
searchby = '' # str | Search by alternate id type. Possible values = [Macaddress, Udid, Serialnumber, ImeiNumber, Uuid] {Formats= Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837, Uuid - EFA9E128-DE1B-404A-A3F4-E5824A666681}(Required) (default to )
id = '' # str | Device alternate ID(Required) (default to )
installaction =  # object | Install action type for OS update. Possible Values = [Default, DownloadOnly, InstallASAP, NotifyOnly, InstallLater](Required) (default to )
osupdateproductversion = '' # str | A single iOS Update product version. This field is required and only for iOS devices. Ex. 12.3.1 (optional) (default to )

try:
    # New - Schedule OS Update for supervised DEP devices
    api_instance.commands_v1_execute_schedule_os_update_by_alternate_id_async(osupdateproductkeys, searchby, id, installaction, osupdateproductversion=osupdateproductversion)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_schedule_os_update_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osupdateproductkeys** | **list[str]**| List of macOS Update product keys. This field is required and only for macOS devices. Ex. [\&quot;macOSUpdate15D100\&quot;](Required). | 
 **searchby** | **str**| Search by alternate id type. Possible values &#x3D; [Macaddress, Udid, Serialnumber, ImeiNumber, Uuid] {Formats&#x3D; Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837, Uuid - EFA9E128-DE1B-404A-A3F4-E5824A666681}(Required) | [default to ]
 **id** | **str**| Device alternate ID(Required) | [default to ]
 **installaction** | [**object**](.md)| Install action type for OS update. Possible Values &#x3D; [Default, DownloadOnly, InstallASAP, NotifyOnly, InstallLater](Required) | [default to ]
 **osupdateproductversion** | **str**| A single iOS Update product version. This field is required and only for iOS devices. Ex. 12.3.1 | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_start_air_play_async**
> commands_v1_execute_start_air_play_async(deviceid, start_air_play=start_air_play)

Executes start airplay for a specific device.

AirPlay on specified destination device.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
deviceid = 56 # int | Device id.
start_air_play = mdmv1.StartAirPlay() # StartAirPlay | Start airplay for a device. (optional)

try:
    # Executes start airplay for a specific device.
    api_instance.commands_v1_execute_start_air_play_async(deviceid, start_air_play=start_air_play)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_start_air_play_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceid** | **int**| Device id. | 
 **start_air_play** | [**StartAirPlay**](StartAirPlay.md)| Start airplay for a device. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_start_remote_view_by_alternate_id_async**
> commands_v1_execute_start_remote_view_by_alternate_id_async(searchby, id, remoteview_id)

New - Executes start remoteview command for device matching the filter criteria.

This api will execute remoteview command in device and user can remoteview the device in the destination device.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
searchby = '' # str | Search by alternate id type. Possible values = [Macaddress, Udid, Serialnumber, ImeiNumber] {Formats= Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837}(Required) (default to )
id = '' # str | Device id(Required) (default to )
remoteview_id = 56 # int | Id of the Remoteview destination device(Required)

try:
    # New - Executes start remoteview command for device matching the filter criteria.
    api_instance.commands_v1_execute_start_remote_view_by_alternate_id_async(searchby, id, remoteview_id)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_start_remote_view_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchby** | **str**| Search by alternate id type. Possible values &#x3D; [Macaddress, Udid, Serialnumber, ImeiNumber] {Formats&#x3D; Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837}(Required) | [default to ]
 **id** | **str**| Device id(Required) | [default to ]
 **remoteview_id** | **int**| Id of the Remoteview destination device(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_v1_execute_stop_device_log_async**
> commands_v1_execute_stop_device_log_async(searchby, id)

New - Executes stop device log request command for device.

This api will execute StopDeviceLog command on the device matching the filter criteria. The logs collected till that time will become available to an admin on AirWatch Console.

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
api_instance = mdmv1.CommandsV1Api(mdmv1.ApiClient(configuration))
searchby = '' # str | Search by alternate id type. Possible values = [Macaddress, Udid, Serialnumber, ImeiNumber] {Formats= Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837}(Required) (default to )
id = '' # str | Device id(Required) (default to )

try:
    # New - Executes stop device log request command for device.
    api_instance.commands_v1_execute_stop_device_log_async(searchby, id)
except ApiException as e:
    print("Exception when calling CommandsV1Api->commands_v1_execute_stop_device_log_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchby** | **str**| Search by alternate id type. Possible values &#x3D; [Macaddress, Udid, Serialnumber, ImeiNumber] {Formats&#x3D; Macaddress - 848506B900BA, Udid - 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber - LGH871c18f631a, ImeiNumber - 354833052322837}(Required) | [default to ]
 **id** | **str**| Device id(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

