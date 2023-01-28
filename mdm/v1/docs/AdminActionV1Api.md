# mdmv1.AdminActionV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_action_v1_bulk_admin_action_async**](AdminActionV1Api.md#admin_action_v1_bulk_admin_action_async) | **POST** /devices/admin-actions/{adminAction} | New - Executes the admin action for the set of devices after performing necessary checks like command accessibility, device enrollment status, support for command on device etc.


# **admin_action_v1_bulk_admin_action_async**
> admin_action_v1_bulk_admin_action_async(admin_action, body)

New - Executes the admin action for the set of devices after performing necessary checks like command accessibility, device enrollment status, support for command on device etc.

Execute Admin Action for specified set of devices

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
api_instance = mdmv1.AdminActionV1Api(mdmv1.ApiClient(configuration))
admin_action = 'admin_action_example' # str | The command to execute [ENTERPRISE_WIPE, DEVICE_WIPE, REBOOT, SUSPEND, WAKEUP,SYNC_DEVICE,SHUTDOWN, DEVICE_INFORMATION,SEND_MESSAGE,REQUEST_DEVICE_LOG].(Required).
body = mdmv1.BulkAdminActionsV1Request() # BulkAdminActionsV1Request | Model containing the command XML passed to the API.(Required).

try:
    # New - Executes the admin action for the set of devices after performing necessary checks like command accessibility, device enrollment status, support for command on device etc.
    api_instance.admin_action_v1_bulk_admin_action_async(admin_action, body)
except ApiException as e:
    print("Exception when calling AdminActionV1Api->admin_action_v1_bulk_admin_action_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_action** | **str**| The command to execute [ENTERPRISE_WIPE, DEVICE_WIPE, REBOOT, SUSPEND, WAKEUP,SYNC_DEVICE,SHUTDOWN, DEVICE_INFORMATION,SEND_MESSAGE,REQUEST_DEVICE_LOG].(Required). | 
 **body** | [**BulkAdminActionsV1Request**](BulkAdminActionsV1Request.md)| Model containing the command XML passed to the API.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

