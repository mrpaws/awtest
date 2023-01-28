# systemv1.DeviceWipesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_wipes_create_device_wipe_log_report_async**](DeviceWipesApi.md#device_wipes_create_device_wipe_log_report_async) | **POST** /groups/{organizationGroupUuid}/device-wipes/reports | New - Creates the report for device wipe log.
[**device_wipes_get_device_wipe_events_async**](DeviceWipesApi.md#device_wipes_get_device_wipe_events_async) | **GET** /groups/{organizationGroupUuid}/device-wipes | New - Gets the list of device wipe events for the specified organization group.
[**device_wipes_get_wipe_lock_state_async**](DeviceWipesApi.md#device_wipes_get_wipe_lock_state_async) | **GET** /groups/{organizationGroupUuid}/device-wipe-lock | New - Gets the state of the wipe lock.
[**device_wipes_reset_wipe_lock_async**](DeviceWipesApi.md#device_wipes_reset_wipe_lock_async) | **PUT** /groups/{organizationGroupUuid}/device-wipe-lock | New - Resets the wipe lock to allow scheduled wipe actions to proceed.
[**device_wipes_update_wipe_actions_async**](DeviceWipesApi.md#device_wipes_update_wipe_actions_async) | **POST** /groups/{organizationGroupUuid}/device-wipes | New - Performs the specified action on the selected wipe actions.


# **device_wipes_create_device_wipe_log_report_async**
> device_wipes_create_device_wipe_log_report_async(organization_group_uuid, device_wipe_request)

New - Creates the report for device wipe log.

Creates the report for device wipe log in CSV or XLSX format.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.DeviceWipesApi(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | The unique identifier of the organization group.(Required).
device_wipe_request = systemv1.DeviceWipeRequestV1() # DeviceWipeRequestV1 | The request parameter to filter out the data for export.(Required).

try:
    # New - Creates the report for device wipe log.
    api_instance.device_wipes_create_device_wipe_log_report_async(organization_group_uuid, device_wipe_request)
except ApiException as e:
    print("Exception when calling DeviceWipesApi->device_wipes_create_device_wipe_log_report_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| The unique identifier of the organization group.(Required). | 
 **device_wipe_request** | [**DeviceWipeRequestV1**](DeviceWipeRequestV1.md)| The request parameter to filter out the data for export.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_wipes_get_device_wipe_events_async**
> DeviceWipeResponseModel device_wipes_get_device_wipe_events_async(organization_group_uuid, search_text=search_text, start_date=start_date, end_date=end_date, wipe_type=wipe_type, wipe_source=wipe_source, wipe_status=wipe_status, ownership=ownership, page=page, page_size=page_size, sort_column=sort_column, sort_direction=sort_direction)

New - Gets the list of device wipe events for the specified organization group.

Gets the list of device wipe events for devices enrolled in the organization group.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.DeviceWipesApi(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | The unique identifier of the organization group.(Required).
search_text = '' # str | The search text string which the device wipe results will be filtered by. (optional) (default to )
start_date = '' # datetime | The start of the date range which the results will be filtered by. (optional) (default to )
end_date = '' # datetime | The end of the date range which the results will be filtered by. (optional) (default to )
wipe_type =  # object | The wipe action type which the results will be filtered by. Supported values are DEVICE_WIPE, ENTERPRISE_WIPE. (optional) (default to )
wipe_source =  # object | The source of the wipe action by which the results will be filtered. Supported values are UNKNOWN, OTHER, DEVICE_DENYLIST_ACTION, COMPLIANCE, USER_DISABLED, ADMIN_ACTION, ADMIN_BULK_ACTION, SELF_SERVICE_PORTAL, DEVICE_SYNC, SMART_GROUP_EDIT, BULK_API_ACTION, DEVICE_UNENROLLMENT_REQUESTED, ADMIN_ACTION_DELETE_DEVICE, ADMIN_BULK_ACTION_DELETE_DEVICE, BULK_ADMIN_API_ACTION_DELETE_DEVICE, SINGLE_ADMIN_API_ACTION_DELETE_DEVICE. (optional) (default to )
wipe_status =  # object | The status of the wipe action by which the results will be filtered. Supported values are APPROVED, HELD, QUEUED, ABORTED. (optional) (default to )
ownership =  # object | The comma seperated device ownership types by which the results will be filtered. Supported values are UNKNOWN, CORPORATE_DEDICATED, EMPLOYEE_OWNED, CORPORATE_SHARED. (optional) (default to )
page = 56 # int | The page number being requested. (optional)
page_size = 56 # int | The maximum records per page. Default 50, Maximum page size is 500. (optional)
sort_column =  # object | The name of the column the results should be ordered by. Supported values are DATE, DEVICE_FRIENDLY_NAME, USER, ORGANIZATION_GROUP. Default is DATE (optional) (default to )
sort_direction =  # object | The sort order by direction. Supported values are ASC, DESC. Default ASC. (optional) (default to )

try:
    # New - Gets the list of device wipe events for the specified organization group.
    api_response = api_instance.device_wipes_get_device_wipe_events_async(organization_group_uuid, search_text=search_text, start_date=start_date, end_date=end_date, wipe_type=wipe_type, wipe_source=wipe_source, wipe_status=wipe_status, ownership=ownership, page=page, page_size=page_size, sort_column=sort_column, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceWipesApi->device_wipes_get_device_wipe_events_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| The unique identifier of the organization group.(Required). | 
 **search_text** | **str**| The search text string which the device wipe results will be filtered by. | [optional] [default to ]
 **start_date** | **datetime**| The start of the date range which the results will be filtered by. | [optional] [default to ]
 **end_date** | **datetime**| The end of the date range which the results will be filtered by. | [optional] [default to ]
 **wipe_type** | [**object**](.md)| The wipe action type which the results will be filtered by. Supported values are DEVICE_WIPE, ENTERPRISE_WIPE. | [optional] [default to ]
 **wipe_source** | [**object**](.md)| The source of the wipe action by which the results will be filtered. Supported values are UNKNOWN, OTHER, DEVICE_DENYLIST_ACTION, COMPLIANCE, USER_DISABLED, ADMIN_ACTION, ADMIN_BULK_ACTION, SELF_SERVICE_PORTAL, DEVICE_SYNC, SMART_GROUP_EDIT, BULK_API_ACTION, DEVICE_UNENROLLMENT_REQUESTED, ADMIN_ACTION_DELETE_DEVICE, ADMIN_BULK_ACTION_DELETE_DEVICE, BULK_ADMIN_API_ACTION_DELETE_DEVICE, SINGLE_ADMIN_API_ACTION_DELETE_DEVICE. | [optional] [default to ]
 **wipe_status** | [**object**](.md)| The status of the wipe action by which the results will be filtered. Supported values are APPROVED, HELD, QUEUED, ABORTED. | [optional] [default to ]
 **ownership** | [**object**](.md)| The comma seperated device ownership types by which the results will be filtered. Supported values are UNKNOWN, CORPORATE_DEDICATED, EMPLOYEE_OWNED, CORPORATE_SHARED. | [optional] [default to ]
 **page** | **int**| The page number being requested. | [optional] 
 **page_size** | **int**| The maximum records per page. Default 50, Maximum page size is 500. | [optional] 
 **sort_column** | [**object**](.md)| The name of the column the results should be ordered by. Supported values are DATE, DEVICE_FRIENDLY_NAME, USER, ORGANIZATION_GROUP. Default is DATE | [optional] [default to ]
 **sort_direction** | [**object**](.md)| The sort order by direction. Supported values are ASC, DESC. Default ASC. | [optional] [default to ]

### Return type

[**DeviceWipeResponseModel**](DeviceWipeResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_wipes_get_wipe_lock_state_async**
> WipeLockStateModel device_wipes_get_wipe_lock_state_async(organization_group_uuid)

New - Gets the state of the wipe lock.

Returns the current state of the device wipe threshold lock.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.DeviceWipesApi(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | The unique identifier of the organization group.(Required).

try:
    # New - Gets the state of the wipe lock.
    api_response = api_instance.device_wipes_get_wipe_lock_state_async(organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceWipesApi->device_wipes_get_wipe_lock_state_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| The unique identifier of the organization group.(Required). | 

### Return type

[**WipeLockStateModel**](WipeLockStateModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_wipes_reset_wipe_lock_async**
> device_wipes_reset_wipe_lock_async(organization_group_uuid)

New - Resets the wipe lock to allow scheduled wipe actions to proceed.

Unlocks the wipe actions that were placed in held status because of the wipe threshold setting.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.DeviceWipesApi(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | The unique identifier of the organization group.(Required).

try:
    # New - Resets the wipe lock to allow scheduled wipe actions to proceed.
    api_instance.device_wipes_reset_wipe_lock_async(organization_group_uuid)
except ApiException as e:
    print("Exception when calling DeviceWipesApi->device_wipes_reset_wipe_lock_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| The unique identifier of the organization group.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_wipes_update_wipe_actions_async**
> device_wipes_update_wipe_actions_async(organization_group_uuid, device_wipe_uuids, action)

New - Performs the specified action on the selected wipe actions.

Approves or rejects the specified wipe actions for further processing.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.DeviceWipesApi(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | The unique identifier of the organization group.(Required).
device_wipe_uuids = [systemv1.list[str]()] # list[str] | The list of uuids for the wipe action records.(Required).
action =  # object | Specifies what action should be taken. Suppored actions are APPROVE, REJECT.(Required) (default to )

try:
    # New - Performs the specified action on the selected wipe actions.
    api_instance.device_wipes_update_wipe_actions_async(organization_group_uuid, device_wipe_uuids, action)
except ApiException as e:
    print("Exception when calling DeviceWipesApi->device_wipes_update_wipe_actions_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| The unique identifier of the organization group.(Required). | 
 **device_wipe_uuids** | **list[str]**| The list of uuids for the wipe action records.(Required). | 
 **action** | [**object**](.md)| Specifies what action should be taken. Suppored actions are APPROVE, REJECT.(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

