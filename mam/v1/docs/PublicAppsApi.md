# mamv1.PublicAppsApi

All URIs are relative to *https://awapi.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_apps_activate_public_app_async**](PublicAppsApi.md#public_apps_activate_public_app_async) | **POST** /apps/public/{applicationid}/activate | Activates the specified public application.
[**public_apps_deactivate_public_app_async**](PublicAppsApi.md#public_apps_deactivate_public_app_async) | **POST** /apps/public/{applicationid}/deactivate | Deactivates the specified public application.
[**public_apps_delete_public_app_async**](PublicAppsApi.md#public_apps_delete_public_app_async) | **DELETE** /apps/public/{applicationid} | Deletes the specified public application.
[**public_apps_get_public_app_by_id_async**](PublicAppsApi.md#public_apps_get_public_app_by_id_async) | **GET** /apps/public/{id} | Gets the details of a public app identified by id.
[**public_apps_get_public_app_installed_or_assigned_devices**](PublicAppsApi.md#public_apps_get_public_app_installed_or_assigned_devices) | **GET** /apps/public/{applicationid}/devices | Provides a list of devices that have the specified public application installed or assigned.
[**public_apps_get_public_app_status_async**](PublicAppsApi.md#public_apps_get_public_app_status_async) | **GET** /apps/public/{applicationid}/status | Indicates the status of the specified public application on a device.
[**public_apps_insert_public_app_async**](PublicAppsApi.md#public_apps_insert_public_app_async) | **POST** /apps/public | Inserts the public application selected by searching for the bundle ID (Android) or external ID (iOS) in the app market.
[**public_apps_install_public_app_on_device_async**](PublicAppsApi.md#public_apps_install_public_app_on_device_async) | **POST** /apps/public/{applicationid}/install | Installs the specified public application on a device.
[**public_apps_remove_public_app_from_device_async**](PublicAppsApi.md#public_apps_remove_public_app_from_device_async) | **POST** /apps/public/{applicationid}/uninstall | Uninstalls the specified public application from a device.
[**public_apps_send_application_configuration_public_apps_async**](PublicAppsApi.md#public_apps_send_application_configuration_public_apps_async) | **POST** /apps/public/SendApplicationConfiguration | New - SendApplicationConfiguration to a given device assigned to a Public App.
[**public_apps_update_public_app_async**](PublicAppsApi.md#public_apps_update_public_app_async) | **PUT** /apps/public/{applicationid} | Updates the public application selected by searching for the bundle ID (Android) or external ID (iOS) in the app market.


# **public_apps_activate_public_app_async**
> public_apps_activate_public_app_async(applicationid)

Activates the specified public application.

Activates the public application identified by the passed in Application ID, and re-installs the app on devices based on existing assignments.

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
api_instance = mamv1.PublicAppsApi(mamv1.ApiClient(configuration))
applicationid = 56 # int | The application Id.

try:
    # Activates the specified public application.
    api_instance.public_apps_activate_public_app_async(applicationid)
except ApiException as e:
    print("Exception when calling PublicAppsApi->public_apps_activate_public_app_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The application Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_apps_deactivate_public_app_async**
> public_apps_deactivate_public_app_async(applicationid)

Deactivates the specified public application.

Deactivates the public application identified by the passed in Application ID, and removes the app from devices.

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
api_instance = mamv1.PublicAppsApi(mamv1.ApiClient(configuration))
applicationid = 56 # int | The Application Id.

try:
    # Deactivates the specified public application.
    api_instance.public_apps_deactivate_public_app_async(applicationid)
except ApiException as e:
    print("Exception when calling PublicAppsApi->public_apps_deactivate_public_app_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The Application Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_apps_delete_public_app_async**
> public_apps_delete_public_app_async(applicationid)

Deletes the specified public application.

Deletes the public application identified by the Application Id passed.

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
api_instance = mamv1.PublicAppsApi(mamv1.ApiClient(configuration))
applicationid = 56 # int | Unique identifier of the app to be deleted.

try:
    # Deletes the specified public application.
    api_instance.public_apps_delete_public_app_async(applicationid)
except ApiException as e:
    print("Exception when calling PublicAppsApi->public_apps_delete_public_app_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Unique identifier of the app to be deleted. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_apps_get_public_app_by_id_async**
> ApplicationEntity_ public_apps_get_public_app_by_id_async(id)

Gets the details of a public app identified by id.

Gets the details of the public application identified by the application Id.

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
api_instance = mamv1.PublicAppsApi(mamv1.ApiClient(configuration))
id = 56 # int | Public App Id is the unique identifier for Public Applications in AirWatch. (Required).

try:
    # Gets the details of a public app identified by id.
    api_response = api_instance.public_apps_get_public_app_by_id_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAppsApi->public_apps_get_public_app_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Public App Id is the unique identifier for Public Applications in AirWatch. (Required). | 

### Return type

[**ApplicationEntity_**](ApplicationEntity_.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_apps_get_public_app_installed_or_assigned_devices**
> DeviceList public_apps_get_public_app_installed_or_assigned_devices(applicationid, status=status, locationgroupid=locationgroupid, page=page, pagesize=pagesize)

Provides a list of devices that have the specified public application installed or assigned.

Returns the list of devices associated(installed/assigned) with the public application identified by the application Id. If the status is unspecified, all the assigned devices are returned.

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
api_instance = mamv1.PublicAppsApi(mamv1.ApiClient(configuration))
applicationid = 56 # int | The application Id.
status = '' # str | status - installed/assigned. (optional) (default to )
locationgroupid = '' # str | The LocationGroup Identifier.. (optional) (default to )
page = '' # str | The Page number. (optional) (default to )
pagesize = '' # str | The Page size. (optional) (default to )

try:
    # Provides a list of devices that have the specified public application installed or assigned.
    api_response = api_instance.public_apps_get_public_app_installed_or_assigned_devices(applicationid, status=status, locationgroupid=locationgroupid, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAppsApi->public_apps_get_public_app_installed_or_assigned_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The application Id. | 
 **status** | **str**| status - installed/assigned. | [optional] [default to ]
 **locationgroupid** | **str**| The LocationGroup Identifier.. | [optional] [default to ]
 **page** | **str**| The Page number. | [optional] [default to ]
 **pagesize** | **str**| The Page size. | [optional] [default to ]

### Return type

[**DeviceList**](DeviceList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_apps_get_public_app_status_async**
> str public_apps_get_public_app_status_async(applicationid, deviceid=deviceid, macaddress=macaddress, serialnumber=serialnumber, udid=udid)

Indicates the status of the specified public application on a device.

Gets the status(Assigned/Installed) of the public application on a device.

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
api_instance = mamv1.PublicAppsApi(mamv1.ApiClient(configuration))
applicationid = 56 # int | The application Id.
deviceid = '' # str | Device Identifier. (optional) (default to )
macaddress = '' # str | Device MAC address. (optional) (default to )
serialnumber = '' # str | Device Serial Number. (optional) (default to )
udid = '' # str | Device UDID. (optional) (default to )

try:
    # Indicates the status of the specified public application on a device.
    api_response = api_instance.public_apps_get_public_app_status_async(applicationid, deviceid=deviceid, macaddress=macaddress, serialnumber=serialnumber, udid=udid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAppsApi->public_apps_get_public_app_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The application Id. | 
 **deviceid** | **str**| Device Identifier. | [optional] [default to ]
 **macaddress** | **str**| Device MAC address. | [optional] [default to ]
 **serialnumber** | **str**| Device Serial Number. | [optional] [default to ]
 **udid** | **str**| Device UDID. | [optional] [default to ]

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_apps_insert_public_app_async**
> ApplicationEntity_ public_apps_insert_public_app_async(application=application)

Inserts the public application selected by searching for the bundle ID (Android) or external ID (iOS) in the app market.

External Id or ApplicationUrl is required in case of Ios apps and for other platforms, Bundle Id or ApplicationUrl is required.

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
api_instance = mamv1.PublicAppsApi(mamv1.ApiClient(configuration))
application = mamv1.ApplicationEntity_() # ApplicationEntity_ | The application entity to be inserted. (optional)

try:
    # Inserts the public application selected by searching for the bundle ID (Android) or external ID (iOS) in the app market.
    api_response = api_instance.public_apps_insert_public_app_async(application=application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicAppsApi->public_apps_insert_public_app_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**ApplicationEntity_**](ApplicationEntity_.md)| The application entity to be inserted. | [optional] 

### Return type

[**ApplicationEntity_**](ApplicationEntity_.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_apps_install_public_app_on_device_async**
> public_apps_install_public_app_on_device_async(applicationid, device_info=device_info)

Installs the specified public application on a device.

Installs the public application identified by the passed in Application Id on a particular device.

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
api_instance = mamv1.PublicAppsApi(mamv1.ApiClient(configuration))
applicationid = 'applicationid_example' # str | The Id of the Application to be installed.
device_info = mamv1.DeviceInfo() # DeviceInfo | The details of the device to install the application on. (optional)

try:
    # Installs the specified public application on a device.
    api_instance.public_apps_install_public_app_on_device_async(applicationid, device_info=device_info)
except ApiException as e:
    print("Exception when calling PublicAppsApi->public_apps_install_public_app_on_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **str**| The Id of the Application to be installed. | 
 **device_info** | [**DeviceInfo**](DeviceInfo.md)| The details of the device to install the application on. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_apps_remove_public_app_from_device_async**
> public_apps_remove_public_app_from_device_async(applicationid, device_info=device_info)

Uninstalls the specified public application from a device.

Uninstalls the public application identified by the application Id from the passed in device.

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
api_instance = mamv1.PublicAppsApi(mamv1.ApiClient(configuration))
applicationid = 56 # int | The application Id.
device_info = mamv1.DeviceInfo() # DeviceInfo | The details of the device from which to uninstall the application. (optional)

try:
    # Uninstalls the specified public application from a device.
    api_instance.public_apps_remove_public_app_from_device_async(applicationid, device_info=device_info)
except ApiException as e:
    print("Exception when calling PublicAppsApi->public_apps_remove_public_app_from_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The application Id. | 
 **device_info** | [**DeviceInfo**](DeviceInfo.md)| The details of the device from which to uninstall the application. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_apps_send_application_configuration_public_apps_async**
> public_apps_send_application_configuration_public_apps_async(send_application_configuration_model=send_application_configuration_model)

New - SendApplicationConfiguration to a given device assigned to a Public App.

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
api_instance = mamv1.PublicAppsApi(mamv1.ApiClient(configuration))
send_application_configuration_model = mamv1.SendApplicationConfigurationModel() # SendApplicationConfigurationModel | Application Configuration Model. (optional)

try:
    # New - SendApplicationConfiguration to a given device assigned to a Public App.
    api_instance.public_apps_send_application_configuration_public_apps_async(send_application_configuration_model=send_application_configuration_model)
except ApiException as e:
    print("Exception when calling PublicAppsApi->public_apps_send_application_configuration_public_apps_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_application_configuration_model** | [**SendApplicationConfigurationModel**](SendApplicationConfigurationModel.md)| Application Configuration Model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_apps_update_public_app_async**
> public_apps_update_public_app_async(applicationid, application_entity=application_entity)

Updates the public application selected by searching for the bundle ID (Android) or external ID (iOS) in the app market.

Updates the public application details such as name, categories etc for the public app identified by the unique identifier applicationid.

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
api_instance = mamv1.PublicAppsApi(mamv1.ApiClient(configuration))
applicationid = 56 # int | Application id to be updated.
application_entity = mamv1.ApplicationEntity_() # ApplicationEntity_ | The application details. (optional)

try:
    # Updates the public application selected by searching for the bundle ID (Android) or external ID (iOS) in the app market.
    api_instance.public_apps_update_public_app_async(applicationid, application_entity=application_entity)
except ApiException as e:
    print("Exception when calling PublicAppsApi->public_apps_update_public_app_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Application id to be updated. | 
 **application_entity** | [**ApplicationEntity_**](ApplicationEntity_.md)| The application details. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

