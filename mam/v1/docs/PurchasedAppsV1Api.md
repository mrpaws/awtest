# mamv1.PurchasedAppsV1Api

All URIs are relative to *https://awapi.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchased_apps_v1_bulk_send_vpp_invites_async**](PurchasedAppsV1Api.md#purchased_apps_v1_bulk_send_vpp_invites_async) | **POST** /apps/purchased/{applicationid}/vppinvite | Sends vpp invitation to the users.
[**purchased_apps_v1_create_purchased_app_assignment_async**](PurchasedAppsV1Api.md#purchased_apps_v1_create_purchased_app_assignment_async) | **POST** /apps/purchased/{applicationid}/assignment | Create new assignments of a VPP licensed application.
[**purchased_apps_v1_delete_vpp_app_async**](PurchasedAppsV1Api.md#purchased_apps_v1_delete_vpp_app_async) | **DELETE** /apps/purchased/{applicationid} | Deletes the specified purchased app.
[**purchased_apps_v1_enable_device_assignment_bulk_applications_async**](PurchasedAppsV1Api.md#purchased_apps_v1_enable_device_assignment_bulk_applications_async) | **PUT** /apps/purchased/device-assignment/organizationgroups/{organizationGroupUuid} | Convert Purchased applications from user based licensing to device based licensing in bulk.
[**purchased_apps_v1_enable_device_assignment_for_vpp_app**](PurchasedAppsV1Api.md#purchased_apps_v1_enable_device_assignment_for_vpp_app) | **PUT** /apps/purchased/EnableDeviceAssignmentForVppApp/{appId} | Enables device-based assignment for the passed app.
[**purchased_apps_v1_get_purchased_app_installed_or_assigned_devices**](PurchasedAppsV1Api.md#purchased_apps_v1_get_purchased_app_installed_or_assigned_devices) | **GET** /apps/purchased/{applicationid}/devices | Provides a list of devices that have the specified purchased application installed or assigned.
[**purchased_apps_v1_get_purchased_app_status_async**](PurchasedAppsV1Api.md#purchased_apps_v1_get_purchased_app_status_async) | **GET** /apps/purchased/{applicationid}/status | Indicates the status of the specified purchased application on a device.
[**purchased_apps_v1_get_user_vpp_invite_status**](PurchasedAppsV1Api.md#purchased_apps_v1_get_user_vpp_invite_status) | **GET** /apps/purchased/{applicationid}/vppinvitestatus/{deviceid} | Gets user&#39;s vpp invitation status.
[**purchased_apps_v1_get_vpp_sync_assets_status**](PurchasedAppsV1Api.md#purchased_apps_v1_get_vpp_sync_assets_status) | **GET** /apps/purchased/GetVppSyncAssetsStatus/{locationGroupId} | Get the status and details for the VPP Sync Assets job at the given organization group.
[**purchased_apps_v1_install_vpp_app_for_device_async**](PurchasedAppsV1Api.md#purchased_apps_v1_install_vpp_app_for_device_async) | **POST** /apps/purchased/{applicationid}/install | Install the purchased application on the device.
[**purchased_apps_v1_load_vpp_licensed_app_allocation**](PurchasedAppsV1Api.md#purchased_apps_v1_load_vpp_licensed_app_allocation) | **GET** /apps/purchased/{applicationid} | Returns VPP licensed Application allocation details by AppId.
[**purchased_apps_v1_remove_purchased_app_from_device_async**](PurchasedAppsV1Api.md#purchased_apps_v1_remove_purchased_app_from_device_async) | **POST** /apps/purchased/{applicationid}/uninstall | Remove the purchased application from the device.
[**purchased_apps_v1_reset_client_context_for_account_async**](PurchasedAppsV1Api.md#purchased_apps_v1_reset_client_context_for_account_async) | **PUT** /apps/purchased/ResetClientContextForAccount/{locationGroupId} | Resets the client context for the account at passed LG.
[**purchased_apps_v1_save_vpp_settings**](PurchasedAppsV1Api.md#purchased_apps_v1_save_vpp_settings) | **POST** /apps/purchased/account | New - Save vpp settings to create vpp account
[**purchased_apps_v1_update_auto_update_flag_for_application_async**](PurchasedAppsV1Api.md#purchased_apps_v1_update_auto_update_flag_for_application_async) | **PATCH** /apps/purchased/{appId} | Sets the value of the auto update flag for a device based VPP application.
[**purchased_apps_v1_update_vpp_application**](PurchasedAppsV1Api.md#purchased_apps_v1_update_vpp_application) | **POST** /apps/purchased/{appId} | Updates the application on devices.
[**purchased_apps_v1_update_vpp_licensed_app_assignment_async**](PurchasedAppsV1Api.md#purchased_apps_v1_update_vpp_licensed_app_assignment_async) | **PUT** /apps/purchased/{applicationid} | Update assignments of a VPP licensed application.
[**purchased_apps_v1_vpp_app_search**](PurchasedAppsV1Api.md#purchased_apps_v1_vpp_app_search) | **GET** /apps/purchased/search | Search and retrieve details for purchased applications.
[**purchased_apps_v1_vpp_sync_assets_async**](PurchasedAppsV1Api.md#purchased_apps_v1_vpp_sync_assets_async) | **PUT** /apps/purchased/VppSyncAssets/{locationGroupId} | Queues up sync assets job for apple vpp applications at the given organization group.


# **purchased_apps_v1_bulk_send_vpp_invites_async**
> BulkResponse purchased_apps_v1_bulk_send_vpp_invites_async(applicationid, bulk_input=bulk_input)

Sends vpp invitation to the users.

For user based purchased app, user needs to accept the invitation and log into app store to install app. This api will send invitations to the users.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | The Application Identifier.
bulk_input = mamv1.BulkInput() # BulkInput | Bulk input containing device IDs. (optional)

try:
    # Sends vpp invitation to the users.
    api_response = api_instance.purchased_apps_v1_bulk_send_vpp_invites_async(applicationid, bulk_input=bulk_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_bulk_send_vpp_invites_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The Application Identifier. | 
 **bulk_input** | [**BulkInput**](BulkInput.md)| Bulk input containing device IDs. | [optional] 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_create_purchased_app_assignment_async**
> purchased_apps_v1_create_purchased_app_assignment_async(applicationid, application=application)

Create new assignments of a VPP licensed application.

Create new assignments of a purchased application with licenses to smart groups, application only with redemption codes  cannot be assigned through this api.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | Application Identifier.
application = mamv1.PurchasedApplicationModel_() # PurchasedApplicationModel_ | Application assignment details. (optional)

try:
    # Create new assignments of a VPP licensed application.
    api_instance.purchased_apps_v1_create_purchased_app_assignment_async(applicationid, application=application)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_create_purchased_app_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Application Identifier. | 
 **application** | [**PurchasedApplicationModel_**](PurchasedApplicationModel_.md)| Application assignment details. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_delete_vpp_app_async**
> purchased_apps_v1_delete_vpp_app_async(applicationid)

Deletes the specified purchased app.

Deletes the specified purchased app and revoke the licenses claimed.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | Application Identifier.

try:
    # Deletes the specified purchased app.
    api_instance.purchased_apps_v1_delete_vpp_app_async(applicationid)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_delete_vpp_app_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Application Identifier. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_enable_device_assignment_bulk_applications_async**
> purchased_apps_v1_enable_device_assignment_bulk_applications_async(organization_group_uuid, action, enable_device_assignment_bulk_applications_model=enable_device_assignment_bulk_applications_model, platform=platform, searchtext=searchtext)

Convert Purchased applications from user based licensing to device based licensing in bulk.

Converts VPP applications from user based licensing to device based in an organization group (including child OGs) based on action type and an optional application list.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group UUID in which to enable device based VPP for applications.(Required)
action =  # object | Action to either include or exclude the app UUIDs specified in the request body. Example - Include action with a list of UUIDs passed in the request will enable DBL for those apps. Exclude action with a list of app UUIDs will enable DBl for all apps in the OG except the ones specified in the list. Exclude action without any app list in the request will enable DBL for all apps in the OG.(Required) (default to )
enable_device_assignment_bulk_applications_model = mamv1.EnableDeviceAssignmentBulkApplicationsModel() # EnableDeviceAssignmentBulkApplicationsModel | Application UUIDs to enable device based licensing OR Application UUIDs to exclude from search criteria. (optional)
platform =  # object | Platform for apps. (optional) (default to )
searchtext = '' # str | Search criteria for application names. (optional) (default to )

try:
    # Convert Purchased applications from user based licensing to device based licensing in bulk.
    api_instance.purchased_apps_v1_enable_device_assignment_bulk_applications_async(organization_group_uuid, action, enable_device_assignment_bulk_applications_model=enable_device_assignment_bulk_applications_model, platform=platform, searchtext=searchtext)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_enable_device_assignment_bulk_applications_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Organization Group UUID in which to enable device based VPP for applications.(Required) | 
 **action** | [**object**](.md)| Action to either include or exclude the app UUIDs specified in the request body. Example - Include action with a list of UUIDs passed in the request will enable DBL for those apps. Exclude action with a list of app UUIDs will enable DBl for all apps in the OG except the ones specified in the list. Exclude action without any app list in the request will enable DBL for all apps in the OG.(Required) | [default to ]
 **enable_device_assignment_bulk_applications_model** | [**EnableDeviceAssignmentBulkApplicationsModel**](EnableDeviceAssignmentBulkApplicationsModel.md)| Application UUIDs to enable device based licensing OR Application UUIDs to exclude from search criteria. | [optional] 
 **platform** | [**object**](.md)| Platform for apps. | [optional] [default to ]
 **searchtext** | **str**| Search criteria for application names. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_enable_device_assignment_for_vpp_app**
> StatusModel purchased_apps_v1_enable_device_assignment_for_vpp_app(app_id)

Enables device-based assignment for the passed app.

Device-based VPP assignment allows you to distribute apps directly to a device without requiring an Apple ID. This will enable device-based assignment for the application.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
app_id = 56 # int | Application id for which device based assignment needs to be enabled (Required).

try:
    # Enables device-based assignment for the passed app.
    api_response = api_instance.purchased_apps_v1_enable_device_assignment_for_vpp_app(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_enable_device_assignment_for_vpp_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| Application id for which device based assignment needs to be enabled (Required). | 

### Return type

[**StatusModel**](StatusModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_get_purchased_app_installed_or_assigned_devices**
> DeviceList purchased_apps_v1_get_purchased_app_installed_or_assigned_devices(applicationid, status, locationgroupid=locationgroupid, page=page, pagesize=pagesize)

Provides a list of devices that have the specified purchased application installed or assigned.

Gets list of devices matching on the input query parameters values.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | The application ID.
status = '' # str | status - installed/assigned (Required). (default to )
locationgroupid = '' # str | The LocationGroup Identifier, for example - 777. (optional) (default to )
page = '' # str | Specific page number to get. 0 based index. (optional) (default to )
pagesize = '' # str | Maximumm records per page. Default 500. (optional) (default to )

try:
    # Provides a list of devices that have the specified purchased application installed or assigned.
    api_response = api_instance.purchased_apps_v1_get_purchased_app_installed_or_assigned_devices(applicationid, status, locationgroupid=locationgroupid, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_get_purchased_app_installed_or_assigned_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The application ID. | 
 **status** | **str**| status - installed/assigned (Required). | [default to ]
 **locationgroupid** | **str**| The LocationGroup Identifier, for example - 777. | [optional] [default to ]
 **page** | **str**| Specific page number to get. 0 based index. | [optional] [default to ]
 **pagesize** | **str**| Maximumm records per page. Default 500. | [optional] [default to ]

### Return type

[**DeviceList**](DeviceList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_get_purchased_app_status_async**
> str purchased_apps_v1_get_purchased_app_status_async(applicationid, deviceid=deviceid, macaddress=macaddress, serialnumber=serialnumber, udid=udid)

Indicates the status of the specified purchased application on a device.

Gets the status if the app is installed/Removed/Pending Install.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | The application Id.
deviceid = '' # str | Device Identifier, for example - 0dfe4a6f25647b8297c15b6a995fa985. (optional) (default to )
macaddress = '' # str | Device MAC address, for example - 0x848506B900BA. (optional) (default to )
serialnumber = '' # str | Device SerialNumber, for example - LGH871c18f631a. (optional) (default to )
udid = '' # str | Device UDID, for example - 6bf0f04c73681fbecfc3eb4f13cbf05b. (optional) (default to )

try:
    # Indicates the status of the specified purchased application on a device.
    api_response = api_instance.purchased_apps_v1_get_purchased_app_status_async(applicationid, deviceid=deviceid, macaddress=macaddress, serialnumber=serialnumber, udid=udid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_get_purchased_app_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The application Id. | 
 **deviceid** | **str**| Device Identifier, for example - 0dfe4a6f25647b8297c15b6a995fa985. | [optional] [default to ]
 **macaddress** | **str**| Device MAC address, for example - 0x848506B900BA. | [optional] [default to ]
 **serialnumber** | **str**| Device SerialNumber, for example - LGH871c18f631a. | [optional] [default to ]
 **udid** | **str**| Device UDID, for example - 6bf0f04c73681fbecfc3eb4f13cbf05b. | [optional] [default to ]

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_get_user_vpp_invite_status**
> UserVppInviteStatus purchased_apps_v1_get_user_vpp_invite_status(applicationid, deviceid)

Gets user's vpp invitation status.

For user based purchased app, user needs to accept the invitation and log into app store to install app. This api will get the user's invitation status for the vpp account containing the application id.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | Vpp Application Identifier.
deviceid = 56 # int | Device Identifier.

try:
    # Gets user's vpp invitation status.
    api_response = api_instance.purchased_apps_v1_get_user_vpp_invite_status(applicationid, deviceid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_get_user_vpp_invite_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Vpp Application Identifier. | 
 **deviceid** | **int**| Device Identifier. | 

### Return type

[**UserVppInviteStatus**](UserVppInviteStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_get_vpp_sync_assets_status**
> GetVppSyncAssetStatusModel purchased_apps_v1_get_vpp_sync_assets_status(location_group_id)

Get the status and details for the VPP Sync Assets job at the given organization group.

Vpp sync assets job will take time to sync applications on the apple server to the airwatch console. This will get the current status of the job.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
location_group_id = 56 # int | Location group id also known as the organization group identifier (Required).

try:
    # Get the status and details for the VPP Sync Assets job at the given organization group.
    api_response = api_instance.purchased_apps_v1_get_vpp_sync_assets_status(location_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_get_vpp_sync_assets_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_group_id** | **int**| Location group id also known as the organization group identifier (Required). | 

### Return type

[**GetVppSyncAssetStatusModel**](GetVppSyncAssetStatusModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_install_vpp_app_for_device_async**
> purchased_apps_v1_install_vpp_app_for_device_async(applicationid, device_info=device_info)

Install the purchased application on the device.

Install the specified purchased application on the device.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 'applicationid_example' # str | Id of the Application to be installed, for example - 123.
device_info = mamv1.DeviceInfo() # DeviceInfo | Details of the device on which the Application to be installed. (optional)

try:
    # Install the purchased application on the device.
    api_instance.purchased_apps_v1_install_vpp_app_for_device_async(applicationid, device_info=device_info)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_install_vpp_app_for_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **str**| Id of the Application to be installed, for example - 123. | 
 **device_info** | [**DeviceInfo**](DeviceInfo.md)| Details of the device on which the Application to be installed. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_load_vpp_licensed_app_allocation**
> PurchasedApplication purchased_apps_v1_load_vpp_licensed_app_allocation(applicationid)

Returns VPP licensed Application allocation details by AppId.

Returns VPP licensed Application allocation details including info about orders and licenses, assignment, and deployment  parameters. Not valid for apps implementing flexible assignment. Should use new version of api.  cannot be updated through this api.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | Application Id.

try:
    # Returns VPP licensed Application allocation details by AppId.
    api_response = api_instance.purchased_apps_v1_load_vpp_licensed_app_allocation(applicationid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_load_vpp_licensed_app_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Application Id. | 

### Return type

[**PurchasedApplication**](PurchasedApplication.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_remove_purchased_app_from_device_async**
> purchased_apps_v1_remove_purchased_app_from_device_async(applicationid, device_info=device_info)

Remove the purchased application from the device.

Remove the specified purchased application from the device.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | The application ID, for example - 123.
device_info = mamv1.DeviceInfo() # DeviceInfo | The details of the device to uninstall the application from. (optional)

try:
    # Remove the purchased application from the device.
    api_instance.purchased_apps_v1_remove_purchased_app_from_device_async(applicationid, device_info=device_info)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_remove_purchased_app_from_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The application ID, for example - 123. | 
 **device_info** | [**DeviceInfo**](DeviceInfo.md)| The details of the device to uninstall the application from. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_reset_client_context_for_account_async**
> StatusModel purchased_apps_v1_reset_client_context_for_account_async(location_group_id)

Resets the client context for the account at passed LG.

Client context contains info about the product that manages vpp account. This will reset the client context to let others able to claim the vpp account.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
location_group_id = 56 # int | Location group id also known as the organization group identifier (Required).

try:
    # Resets the client context for the account at passed LG.
    api_response = api_instance.purchased_apps_v1_reset_client_context_for_account_async(location_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_reset_client_context_for_account_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_group_id** | **int**| Location group id also known as the organization group identifier (Required). | 

### Return type

[**StatusModel**](StatusModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_save_vpp_settings**
> purchased_apps_v1_save_vpp_settings(vpp_settings_v1_model)

New - Save vpp settings to create vpp account

Save vpp settings to create vpp account at a given organization group.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
vpp_settings_v1_model = mamv1.VppSettingsV1Model() # VppSettingsV1Model | Vpp settings including info about description of the vpp account, stoken blob id, whether to send invitation to user and target organization group.(Required)

try:
    # New - Save vpp settings to create vpp account
    api_instance.purchased_apps_v1_save_vpp_settings(vpp_settings_v1_model)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_save_vpp_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpp_settings_v1_model** | [**VppSettingsV1Model**](VppSettingsV1Model.md)| Vpp settings including info about description of the vpp account, stoken blob id, whether to send invitation to user and target organization group.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_update_auto_update_flag_for_application_async**
> purchased_apps_v1_update_auto_update_flag_for_application_async(app_id, purchased_app_auto_update_model=purchased_app_auto_update_model)

Sets the value of the auto update flag for a device based VPP application.

Updates the auto update flag for a device based VPP application. If enabled, the update will be automatically  installed on devices having the application.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
app_id = 56 # int | The application id (Required).
purchased_app_auto_update_model = mamv1.PurchasedAppAutoUpdateModel() # PurchasedAppAutoUpdateModel | The purchased application auto update model. (optional)

try:
    # Sets the value of the auto update flag for a device based VPP application.
    api_instance.purchased_apps_v1_update_auto_update_flag_for_application_async(app_id, purchased_app_auto_update_model=purchased_app_auto_update_model)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_update_auto_update_flag_for_application_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| The application id (Required). | 
 **purchased_app_auto_update_model** | [**PurchasedAppAutoUpdateModel**](PurchasedAppAutoUpdateModel.md)| The purchased application auto update model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_update_vpp_application**
> purchased_apps_v1_update_vpp_application(app_id)

Updates the application on devices.

Updates the application on devices having device based licenses for the application if an update is available.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
app_id = 56 # int | The application id (Required).

try:
    # Updates the application on devices.
    api_instance.purchased_apps_v1_update_vpp_application(app_id)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_update_vpp_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| The application id (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_update_vpp_licensed_app_assignment_async**
> purchased_apps_v1_update_vpp_licensed_app_assignment_async(applicationid, application=application)

Update assignments of a VPP licensed application.

Update assignments of a purchased application with licenses, application only with redemption codes or redemption based assignment  cannot be updated through this api.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | Vpp Licensed Application Id.
application = mamv1.PurchasedApplicationModel_() # PurchasedApplicationModel_ | Application assignment details. (optional)

try:
    # Update assignments of a VPP licensed application.
    api_instance.purchased_apps_v1_update_vpp_licensed_app_assignment_async(applicationid, application=application)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_update_vpp_licensed_app_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Vpp Licensed Application Id. | 
 **application** | [**PurchasedApplicationModel_**](PurchasedApplicationModel_.md)| Application assignment details. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_vpp_app_search**
> PurchasedApplicationSearchResult purchased_apps_v1_vpp_app_search(applicationname=applicationname, isassigned=isassigned, bundleid=bundleid, locationgroupid=locationgroupid, model=model, status=status, platform=platform, page=page, pagesize=pagesize, orderby=orderby)

Search and retrieve details for purchased applications.

Application details, its assignments, deployment parameters are displayed.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
applicationname = '' # str | Application Name, for example - AngryBirds.  (optional) (default to )
isassigned = '' # str | Flag to indicate whether the app is assigned or not, for example - true. (optional) (default to )
bundleid = '' # str | BundleId/PackageId, for example - xyz.Angrybirds.com. (optional) (default to )
locationgroupid = '' # str | LocationGroup Identifier, for example - 777. (optional) (default to )
model = '' # str | Device Model, for example - iPhone. (optional) (default to )
status = '' # str | Application Status, for example - Active. (optional) (default to )
platform = '' # str | The Application Platform, for example - Apple. (optional) (default to )
page = '' # str | Specific page number to get. 0 based index. (optional) (default to )
pagesize = '' # str | Maximumm records per page. Default 500. (optional) (default to )
orderby = '' # str | Orderby column name, for example - applicationname. (optional) (default to )

try:
    # Search and retrieve details for purchased applications.
    api_response = api_instance.purchased_apps_v1_vpp_app_search(applicationname=applicationname, isassigned=isassigned, bundleid=bundleid, locationgroupid=locationgroupid, model=model, status=status, platform=platform, page=page, pagesize=pagesize, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_vpp_app_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationname** | **str**| Application Name, for example - AngryBirds.  | [optional] [default to ]
 **isassigned** | **str**| Flag to indicate whether the app is assigned or not, for example - true. | [optional] [default to ]
 **bundleid** | **str**| BundleId/PackageId, for example - xyz.Angrybirds.com. | [optional] [default to ]
 **locationgroupid** | **str**| LocationGroup Identifier, for example - 777. | [optional] [default to ]
 **model** | **str**| Device Model, for example - iPhone. | [optional] [default to ]
 **status** | **str**| Application Status, for example - Active. | [optional] [default to ]
 **platform** | **str**| The Application Platform, for example - Apple. | [optional] [default to ]
 **page** | **str**| Specific page number to get. 0 based index. | [optional] [default to ]
 **pagesize** | **str**| Maximumm records per page. Default 500. | [optional] [default to ]
 **orderby** | **str**| Orderby column name, for example - applicationname. | [optional] [default to ]

### Return type

[**PurchasedApplicationSearchResult**](PurchasedApplicationSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchased_apps_v1_vpp_sync_assets_async**
> StatusModel purchased_apps_v1_vpp_sync_assets_async(location_group_id)

Queues up sync assets job for apple vpp applications at the given organization group.

Queues up sync assets job at the given organization group to get info about the number of total licenses, licenses assigned to each application.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.PurchasedAppsV1Api(mamv1.ApiClient(configuration))
location_group_id = 56 # int | Location group id also known as the organization group identifier (Required).

try:
    # Queues up sync assets job for apple vpp applications at the given organization group.
    api_response = api_instance.purchased_apps_v1_vpp_sync_assets_async(location_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasedAppsV1Api->purchased_apps_v1_vpp_sync_assets_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_group_id** | **int**| Location group id also known as the organization group identifier (Required). | 

### Return type

[**StatusModel**](StatusModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

