# mdmv1.DevicesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_bulk_delete_devices_async**](DevicesApi.md#devices_bulk_delete_devices_async) | **POST** /devices/bulk | New - Deletes multiple devices identified by device id or alternate id.
[**devices_bulk_get_devices_by_alternate_id_async**](DevicesApi.md#devices_bulk_get_devices_by_alternate_id_async) | **POST** /devices | New - Retrieves information about multiple devices identified by the specified id type.
[**devices_delete_async**](DevicesApi.md#devices_delete_async) | **DELETE** /devices/{id} | New - Delete Device details by Device id.
[**devices_delete_by_address_async**](DevicesApi.md#devices_delete_by_address_async) | **DELETE** /devices/macaddress/{macaddress} | Deletes the device identified by MAC address.
[**devices_delete_by_alternate_id_async**](DevicesApi.md#devices_delete_by_alternate_id_async) | **DELETE** /devices | New - Deletes Device details by alternate id for Device.
[**devices_device_extensive_search_async**](DevicesApi.md#devices_device_extensive_search_async) | **GET** /devices/extensivesearch | New - Extensive search of device details.
[**devices_device_extensive_search_lite_async**](DevicesApi.md#devices_device_extensive_search_lite_async) | **GET** /devices/litesearch | New - Searches devices and its custom attributes.
[**devices_edit_device_async**](DevicesApi.md#devices_edit_device_async) | **PUT** /devices/{id} | New - Edit the device details identified by Device id.
[**devices_edit_device_by_alternate_id_async**](DevicesApi.md#devices_edit_device_by_alternate_id_async) | **PUT** /devices | New - Edit the device details identified by alternate id for Device.
[**devices_filter_enrolled_devices_count_async**](DevicesApi.md#devices_filter_enrolled_devices_count_async) | **POST** /devices/enrolleddevicescount | Retrieves Count of all enrolled devices based on any or all of the following OG id, Tag Name,and devices registered after &#39;SeenSince&#39; datetime until the &#39;SeenTill&#39; datetime.
[**devices_get_app_status_async**](DevicesApi.md#devices_get_app_status_async) | **GET** /devices/appstatus | New - Gets App Status for a combination of input elements.
[**devices_get_bulk_settings**](DevicesApi.md#devices_get_bulk_settings) | **GET** /devices/bulksettings | Retrieve limits for bulk actions.
[**devices_get_by_alternate_id_async**](DevicesApi.md#devices_get_by_alternate_id_async) | **GET** /devices | New - Get Device details by Alternate id.
[**devices_get_by_id_async**](DevicesApi.md#devices_get_by_id_async) | **GET** /devices/{id} | New - Get Device details by Device id.
[**devices_get_by_udid_async**](DevicesApi.md#devices_get_by_udid_async) | **GET** /devices/udid/{udid} | New - Get device info based on UDID.
[**devices_get_device_count_details**](DevicesApi.md#devices_get_device_count_details) | **GET** /devices/devicecountinfo | Retrieves Device Count Information which are Categorized by Device Info like Platform, EnrollmentStatus, Ownership etc..
[**devices_get_device_enrollment_statusby_udid_async**](DevicesApi.md#devices_get_device_enrollment_statusby_udid_async) | **GET** /devices/udid/{udid}/deviceenrollmentstatus | Retrieves Device status based on the device identifier(UDID).
[**devices_get_device_tags_async**](DevicesApi.md#devices_get_device_tags_async) | **GET** /devices/{uuid}/tags | New - Retrieves associated tags for a device
[**devices_get_devices_by_id_async**](DevicesApi.md#devices_get_devices_by_id_async) | **POST** /devices/id | New - Retrieves information about multiple devices identified by device id.
[**devices_get_logged_in_users_async**](DevicesApi.md#devices_get_logged_in_users_async) | **GET** /devices/{deviceId}/loggedinusers | Gets all logged in users on the device.
[**devices_load_device_event_history**](DevicesApi.md#devices_load_device_event_history) | **GET** /ogs/{og_id}/devices/audit | Returns the device audit history for a device.
[**devices_managed_settings_for_device_by_alternate_id**](DevicesApi.md#devices_managed_settings_for_device_by_alternate_id) | **POST** /devices/managedsettings | Sets the managed settings for an iOS device based on alternate id.
[**devices_search_async**](DevicesApi.md#devices_search_async) | **GET** /devices/search | New - Find relevant devices using various criteria.
[**devices_send_message**](DevicesApi.md#devices_send_message) | **POST** /devices/{id}/sendmessage | Sends a push notification to the device identified by device ID. If not enrolled, sends an SMS message instead.
[**devices_send_message_by_mac**](DevicesApi.md#devices_send_message_by_mac) | **POST** /devices/macaddress/{macaddress}/sendmessage | Sends a push notification to the device identified by MAC address. If not enrolled, sends an SMS message instead.
[**devices_send_message_by_serial_number**](DevicesApi.md#devices_send_message_by_serial_number) | **POST** /devices/serialnumber/{serialnumber}/sendmessage | Sends a push notification to the device identified by serial number. If not enrolled, sends an SMS message instead.
[**devices_send_message_by_udid**](DevicesApi.md#devices_send_message_by_udid) | **POST** /devices/udid/{udid}/sendmessage | Sends a push notification to the device identified by UDID. If not enrolled, sends an SMS message instead.
[**devices_update_custom_attributes_by_asset_nr**](DevicesApi.md#devices_update_custom_attributes_by_asset_nr) | **POST** /devices/assetnumber/{assetnumber}/updatecustomattributes | Updates the device custom attribute value if already present for a device, else adds the same to the device.


# **devices_bulk_delete_devices_async**
> BulkResponse devices_bulk_delete_devices_async(bulk_input, searchby=searchby)

New - Deletes multiple devices identified by device id or alternate id.

 Deletes multiple multiple devices by an alternate id which can be any one of the following ids:  1. Macaddress, 2. Udid, 3. Serialnumber, 4. ImeiNumber, 5. EasId, 6. DeviceId.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
bulk_input = mdmv1.BulkInput() # BulkInput | Bulk input containing multiple device ids.(Required).
searchby = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber, EasId, DeviceId]. If not included, device id is used. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 1234, DeviceId: 1234). (optional) (default to )

try:
    # New - Deletes multiple devices identified by device id or alternate id.
    api_response = api_instance.devices_bulk_delete_devices_async(bulk_input, searchby=searchby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_bulk_delete_devices_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| Bulk input containing multiple device ids.(Required). | 
 **searchby** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber, EasId, DeviceId]. If not included, device id is used. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 1234, DeviceId: 1234). | [optional] [default to ]

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_bulk_get_devices_by_alternate_id_async**
> DeviceSearchResultExtended devices_bulk_get_devices_by_alternate_id_async(bulk_input, searchby)

New - Retrieves information about multiple devices identified by the specified id type.

 Retrieves the device details for multiple devices by an alternate id which can be any one of the following ids:  1. Macaddress, 2. Udid, 3. Serialnumber, 4. ImeiNumber, 5. EasId, 6. DeviceId.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
bulk_input = mdmv1.BulkInput() # BulkInput | Bulk input containing multiple device IDs.(Required).
searchby = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber, EasId, DeviceId]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 1234, DeviceId: 1234).(Required) (default to )

try:
    # New - Retrieves information about multiple devices identified by the specified id type.
    api_response = api_instance.devices_bulk_get_devices_by_alternate_id_async(bulk_input, searchby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_bulk_get_devices_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| Bulk input containing multiple device IDs.(Required). | 
 **searchby** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber, EasId, DeviceId]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 1234, DeviceId: 1234).(Required) | [default to ]

### Return type

[**DeviceSearchResultExtended**](DeviceSearchResultExtended.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_delete_async**
> Device devices_delete_async(id)

New - Delete Device details by Device id.

Delete Device details by Device id.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
id = 56 # int | Device id of the Device.(Required).

try:
    # New - Delete Device details by Device id.
    api_response = api_instance.devices_delete_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device id of the Device.(Required). | 

### Return type

[**Device**](Device.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_delete_by_address_async**
> devices_delete_by_address_async(macaddress)

Deletes the device identified by MAC address.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
macaddress = 'macaddress_example' # str | MAC address of the device.

try:
    # Deletes the device identified by MAC address.
    api_instance.devices_delete_by_address_async(macaddress)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_delete_by_address_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **macaddress** | **str**| MAC address of the device. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_delete_by_alternate_id_async**
> devices_delete_by_alternate_id_async(id, searchby)

New - Deletes Device details by alternate id for Device.

 Deletes the device details by an alternate id which can be any one of the following ids:  1. Macaddress, 2. Udid, 3. Serialnumber, 4. ImeiNumber, 5. EasId, 6. DeviceId.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
id = 56 # int | Device alternate ID.(Required)
searchby = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber, EasId, DeviceId]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 1234, DeviceId: 1234).(Required) (default to )

try:
    # New - Deletes Device details by alternate id for Device.
    api_instance.devices_delete_by_alternate_id_async(id, searchby)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_delete_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device alternate ID.(Required) | 
 **searchby** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber, EasId, DeviceId]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 1234, DeviceId: 1234).(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_device_extensive_search_async**
> DeviceExtensiveSearchResult devices_device_extensive_search_async(organizationgroupid=organizationgroupid, platform=platform, startdatetime=startdatetime, enddatetime=enddatetime, deviceid=deviceid, customattributes=customattributes, enrollmentstatus=enrollmentstatus, statuschangestarttime=statuschangestarttime, statuschangeendtime=statuschangeendtime, page=page, pagesize=pagesize, macaddress=macaddress)

New - Extensive search of device details.

This API returns device details, summarized product compliance details, smart groups, and custom attributes for enrolled devices. For unenrolled devices, only the device details are returned in the response.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | OrganizationGroup to be searched, admin's OG is considered if not sent. (optional)
platform = 56 # int | Device platform. (optional)
startdatetime = '' # datetime | Filters devices such that devices with last seen after this date will be returned. (optional) (default to )
enddatetime = '' # datetime | Filters devices such that devices with last seen till this date will be returned. (optional) (default to )
deviceid = 56 # int | Device Identifier. (optional)
customattributes = '' # str | Custom attribute names. (optional) (default to )
enrollmentstatus = '' # str | Filters devices based on their EnrollmentStatus [Enrolled, EnterpriseWipePending, DeviceWipePending, Unenrolled]. (optional) (default to )
statuschangestarttime = '' # str | Filters the devices for which EnrollmentStatus has changes from enrollmentstatuschangefrom datetime. This filter is only for Enrolled and Unenrolled enrollment status. (optional) (default to )
statuschangeendtime = '' # str | Filters the devices for which EnrollmentStatus has changes till enrollmentstatuschangeto datetime. This filter is only for Enrolled and Unenrolled enrollment status. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)
macaddress = '' # str | MAC address. (optional) (default to )

try:
    # New - Extensive search of device details.
    api_response = api_instance.devices_device_extensive_search_async(organizationgroupid=organizationgroupid, platform=platform, startdatetime=startdatetime, enddatetime=enddatetime, deviceid=deviceid, customattributes=customattributes, enrollmentstatus=enrollmentstatus, statuschangestarttime=statuschangestarttime, statuschangeendtime=statuschangeendtime, page=page, pagesize=pagesize, macaddress=macaddress)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_device_extensive_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| OrganizationGroup to be searched, admin&#39;s OG is considered if not sent. | [optional] 
 **platform** | **int**| Device platform. | [optional] 
 **startdatetime** | **datetime**| Filters devices such that devices with last seen after this date will be returned. | [optional] [default to ]
 **enddatetime** | **datetime**| Filters devices such that devices with last seen till this date will be returned. | [optional] [default to ]
 **deviceid** | **int**| Device Identifier. | [optional] 
 **customattributes** | **str**| Custom attribute names. | [optional] [default to ]
 **enrollmentstatus** | **str**| Filters devices based on their EnrollmentStatus [Enrolled, EnterpriseWipePending, DeviceWipePending, Unenrolled]. | [optional] [default to ]
 **statuschangestarttime** | **str**| Filters the devices for which EnrollmentStatus has changes from enrollmentstatuschangefrom datetime. This filter is only for Enrolled and Unenrolled enrollment status. | [optional] [default to ]
 **statuschangeendtime** | **str**| Filters the devices for which EnrollmentStatus has changes till enrollmentstatuschangeto datetime. This filter is only for Enrolled and Unenrolled enrollment status. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 
 **macaddress** | **str**| MAC address. | [optional] [default to ]

### Return type

[**DeviceExtensiveSearchResult**](DeviceExtensiveSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_device_extensive_search_lite_async**
> DeviceExtensiveLiteSearchResult devices_device_extensive_search_lite_async(organizationgroupid=organizationgroupid, platform=platform, seensince=seensince, seentill=seentill, deviceid=deviceid, customattributes=customattributes, page=page, pagesize=pagesize)

New - Searches devices and its custom attributes.

Searches devices and its custom attributes using the query information provided. A list of custom attributes to search can be given as a query parameter. The search results are limited to the requested custom attributes.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | OrganizationGroup to be searched. Admin's OG is considered if this is not sent. (optional)
platform = '' # str | Device Platform [Android, Apple, AppleOsX, AppleTv, Athena, AveryDennisonPrinter, ChromeBook, ChromeOS, Epson, Motorola, Qnx, Symbian, ToshibaPrinter, WindowsMobile, WindowsPc, WindowsPhone8, WinRT, ZebraPrinter]. (optional) (default to )
seensince = '' # datetime | Filters devices such that devices with last seen after this date will be returned. (optional) (default to )
seentill = '' # datetime | Filters devices such that devices with last seen till this date will be returned. (optional) (default to )
deviceid = 56 # int | Device Identifier. (optional)
customattributes = '' # str | Custom attribute names. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # New - Searches devices and its custom attributes.
    api_response = api_instance.devices_device_extensive_search_lite_async(organizationgroupid=organizationgroupid, platform=platform, seensince=seensince, seentill=seentill, deviceid=deviceid, customattributes=customattributes, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_device_extensive_search_lite_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| OrganizationGroup to be searched. Admin&#39;s OG is considered if this is not sent. | [optional] 
 **platform** | **str**| Device Platform [Android, Apple, AppleOsX, AppleTv, Athena, AveryDennisonPrinter, ChromeBook, ChromeOS, Epson, Motorola, Qnx, Symbian, ToshibaPrinter, WindowsMobile, WindowsPc, WindowsPhone8, WinRT, ZebraPrinter]. | [optional] [default to ]
 **seensince** | **datetime**| Filters devices such that devices with last seen after this date will be returned. | [optional] [default to ]
 **seentill** | **datetime**| Filters devices such that devices with last seen till this date will be returned. | [optional] [default to ]
 **deviceid** | **int**| Device Identifier. | [optional] 
 **customattributes** | **str**| Custom attribute names. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**DeviceExtensiveLiteSearchResult**](DeviceExtensiveLiteSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_edit_device_async**
> devices_edit_device_async(id, device)

New - Edit the device details identified by Device id.

Edit the device details identified by Device id.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
id = 56 # int | Device id of the Device.(Required).
device = mdmv1.DeviceRequestModel() # DeviceRequestModel | Device details which need to be updated.(Required).

try:
    # New - Edit the device details identified by Device id.
    api_instance.devices_edit_device_async(id, device)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_edit_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device id of the Device.(Required). | 
 **device** | [**DeviceRequestModel**](DeviceRequestModel.md)| Device details which need to be updated.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_edit_device_by_alternate_id_async**
> devices_edit_device_by_alternate_id_async(device, id, searchby)

New - Edit the device details identified by alternate id for Device.

 Updates the device details by an alternate id which can be any one of the following ids:  1. Macaddress, 2. Udid, 3. Serialnumber, 4. ImeiNumber, 5. EasId, 6. DeviceId.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
device = mdmv1.DeviceRequestModel() # DeviceRequestModel | Device details which need to be updated.(Required).
id = 56 # int | Device alternate id.(Required)
searchby = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber, EasId, DeviceId]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 1234, DeviceId: 1234).(Required) (default to )

try:
    # New - Edit the device details identified by alternate id for Device.
    api_instance.devices_edit_device_by_alternate_id_async(device, id, searchby)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_edit_device_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**DeviceRequestModel**](DeviceRequestModel.md)| Device details which need to be updated.(Required). | 
 **id** | **int**| Device alternate id.(Required) | 
 **searchby** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber, EasId, DeviceId]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 1234, DeviceId: 1234).(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_filter_enrolled_devices_count_async**
> devices_filter_enrolled_devices_count_async(request, filter_criteria=filter_criteria)

Retrieves Count of all enrolled devices based on any or all of the following OG id, Tag Name,and devices registered after 'SeenSince' datetime until the 'SeenTill' datetime.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
request = {'key': 'request_example'} # dict(str, str) | Http Request.
filter_criteria = mdmv1.DeviceCountFilterCriteriaRequestModel() # DeviceCountFilterCriteriaRequestModel | Filter Entity. (optional)

try:
    # Retrieves Count of all enrolled devices based on any or all of the following OG id, Tag Name,and devices registered after 'SeenSince' datetime until the 'SeenTill' datetime.
    api_instance.devices_filter_enrolled_devices_count_async(request, filter_criteria=filter_criteria)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_filter_enrolled_devices_count_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**dict(str, str)**](str.md)| Http Request. | 
 **filter_criteria** | [**DeviceCountFilterCriteriaRequestModel**](DeviceCountFilterCriteriaRequestModel.md)| Filter Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get_app_status_async**
> AppStatusV1ResponseModel devices_get_app_status_async(search_by, id, groupid, bundle_id, version, device_type)

New - Gets App Status for a combination of input elements.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber etc].(Required). (default to )
id = '' # str | The alternate id for the provided type.(Required). (default to )
groupid = '' # str | Organizations Groups's customer code.(Required). (default to )
bundle_id = '' # str | App Bundle Id.(Required). (default to )
version = '' # str | App version.(Required). (default to )
device_type = '' # str | Type of the device [Apple, Android, WindowsPhone8, WinRT].(Required). (default to )

try:
    # New - Gets App Status for a combination of input elements.
    api_response = api_instance.devices_get_app_status_async(search_by, id, groupid, bundle_id, version, device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get_app_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber etc].(Required). | [default to ]
 **id** | **str**| The alternate id for the provided type.(Required). | [default to ]
 **groupid** | **str**| Organizations Groups&#39;s customer code.(Required). | [default to ]
 **bundle_id** | **str**| App Bundle Id.(Required). | [default to ]
 **version** | **str**| App version.(Required). | [default to ]
 **device_type** | **str**| Type of the device [Apple, Android, WindowsPhone8, WinRT].(Required). | [default to ]

### Return type

[**AppStatusV1ResponseModel**](AppStatusV1ResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get_bulk_settings**
> BulkSettings devices_get_bulk_settings()

Retrieve limits for bulk actions.

Gets the limit for bulk action as below:  1. Max Devices allowed for bulk SendMessage  2. Max Devices allowed for bulk EnterpriseWipe  3. Max Devices allowed for bulk DeleteDevice  4. Max Devices allowed for bulk GPS  5. Max Devices allowed for bulk RemoveFSecure.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))

try:
    # Retrieve limits for bulk actions.
    api_response = api_instance.devices_get_bulk_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get_bulk_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BulkSettings**](BulkSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get_by_alternate_id_async**
> Device devices_get_by_alternate_id_async(searchby, id)

New - Get Device details by Alternate id.

 Get the device details by an alternate id which can be any one of the following ids:  1. Macaddress, 2. Udid, 3. Serialnumber, 4. ImeiNumber, 5. EasId, 6. DeviceId.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
searchby = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber, EasId, DeviceId]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 1234, DeviceId: 1234).(Required) (default to )
id = '' # str | Device alternate id.(Required) (default to )

try:
    # New - Get Device details by Alternate id.
    api_response = api_instance.devices_get_by_alternate_id_async(searchby, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchby** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber, EasId, DeviceId]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 1234, DeviceId: 1234).(Required) | [default to ]
 **id** | **str**| Device alternate id.(Required) | [default to ]

### Return type

[**Device**](Device.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get_by_id_async**
> Device devices_get_by_id_async(id)

New - Get Device details by Device id.

Get Device details by Device id.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
id = 56 # int | Device id of the Device.(Required).

try:
    # New - Get Device details by Device id.
    api_response = api_instance.devices_get_by_id_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device id of the Device.(Required). | 

### Return type

[**Device**](Device.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get_by_udid_async**
> DeviceResponseV1Model devices_get_by_udid_async(udid)

New - Get device info based on UDID.

Get device info based on UDID. The API returns a 404 - NotFound if the device is not available.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
udid = 'udid_example' # str | UDID of the device.(Required).

try:
    # New - Get device info based on UDID.
    api_response = api_instance.devices_get_by_udid_async(udid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get_by_udid_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **udid** | **str**| UDID of the device.(Required). | 

### Return type

[**DeviceResponseV1Model**](DeviceResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get_device_count_details**
> DeviceCountSummary devices_get_device_count_details(organizationgroupid=organizationgroupid)

Retrieves Device Count Information which are Categorized by Device Info like Platform, EnrollmentStatus, Ownership etc..

Retrieves the device count for the following information.  1. Total number of devices deployed in an OG.  2. Device count breakdown by Security Info.  3. Device count breakdown by Ownership Info.  4. Device count breakdown by Platform Info.  5. Device count breakdown by EnrollmentStatus Info.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | OrganizationGroup to be searched, user's OG is considered if not sent. (optional)

try:
    # Retrieves Device Count Information which are Categorized by Device Info like Platform, EnrollmentStatus, Ownership etc..
    api_response = api_instance.devices_get_device_count_details(organizationgroupid=organizationgroupid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get_device_count_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| OrganizationGroup to be searched, user&#39;s OG is considered if not sent. | [optional] 

### Return type

[**DeviceCountSummary**](DeviceCountSummary.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get_device_enrollment_statusby_udid_async**
> CurrentEnrollmentStatus devices_get_device_enrollment_statusby_udid_async(udid, organizationgroupid=organizationgroupid)

Retrieves Device status based on the device identifier(UDID).

Retrieves information about the device such as:  1. Device Enrollment Status 2. Device Managed By 3. User name 4. Domain.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
udid = 'udid_example' # str | Unique device identifier.
organizationgroupid = 56 # int | DeviceUDID. (optional)

try:
    # Retrieves Device status based on the device identifier(UDID).
    api_response = api_instance.devices_get_device_enrollment_statusby_udid_async(udid, organizationgroupid=organizationgroupid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get_device_enrollment_statusby_udid_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **udid** | **str**| Unique device identifier. | 
 **organizationgroupid** | **int**| DeviceUDID. | [optional] 

### Return type

[**CurrentEnrollmentStatus**](CurrentEnrollmentStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get_device_tags_async**
> DeviceTagResultV1Model devices_get_device_tags_async(uuid)

New - Retrieves associated tags for a device

Retrieves a list of all associated tags for the device specified by the device UUID.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier for a device. Ex. 153B4D9D-24DC-416B-91F9-94253D623611(Required).

try:
    # New - Retrieves associated tags for a device
    api_response = api_instance.devices_get_device_tags_async(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get_device_tags_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier for a device. Ex. 153B4D9D-24DC-416B-91F9-94253D623611(Required). | 

### Return type

[**DeviceTagResultV1Model**](DeviceTagResultV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get_devices_by_id_async**
> DeviceSearchResultExtended devices_get_devices_by_id_async(bulk_input)

New - Retrieves information about multiple devices identified by device id.

Gets the details about multiple devices based on a list of device ids supplied.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
bulk_input = mdmv1.BulkInput() # BulkInput | Bulk input containing multiple device ids.(Required).

try:
    # New - Retrieves information about multiple devices identified by device id.
    api_response = api_instance.devices_get_devices_by_id_async(bulk_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get_devices_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| Bulk input containing multiple device ids.(Required). | 

### Return type

[**DeviceSearchResultExtended**](DeviceSearchResultExtended.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get_logged_in_users_async**
> devices_get_logged_in_users_async(device_id)

Gets all logged in users on the device.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
device_id = 56 # int | The device id.

try:
    # Gets all logged in users on the device.
    api_instance.devices_get_logged_in_users_async(device_id)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get_logged_in_users_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The device id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_load_device_event_history**
> devices_load_device_event_history(og_id, serialnumber=serialnumber, status=status, startdate=startdate, enddate=enddate, page=page, pagesize=pagesize, sortorder=sortorder)

Returns the device audit history for a device.

The query parameters startdate and enddate accepts the below DateTime formats :  <br>yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff, yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff,</br>  yyyy/MM/ddTHH:mm:ss.fff, yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
og_id = 'og_id_example' # str | organization Group code.
serialnumber = '' # str | The device serial number (Example : SerialNumber123). (optional) (default to )
status = '' # str | The device status. Accepted values are 'UnEnrolled', 'Deleted', 'Replaced', 'Inserted', and 'Updated'. (optional) (default to )
startdate = '' # datetime | DateTime, Filters device events where event date falls on/after this startdate time. Start date should be within 30 days of the current date. (optional) (default to )
enddate = '' # datetime | DateTime, Filters device events where event date falls on/before this enddate time. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)
sortorder = '' # str | Sorting order. Values ASC or DESC. Defaults to ASC. (optional) (default to )

try:
    # Returns the device audit history for a device.
    api_instance.devices_load_device_event_history(og_id, serialnumber=serialnumber, status=status, startdate=startdate, enddate=enddate, page=page, pagesize=pagesize, sortorder=sortorder)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_load_device_event_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **og_id** | **str**| organization Group code. | 
 **serialnumber** | **str**| The device serial number (Example : SerialNumber123). | [optional] [default to ]
 **status** | **str**| The device status. Accepted values are &#39;UnEnrolled&#39;, &#39;Deleted&#39;, &#39;Replaced&#39;, &#39;Inserted&#39;, and &#39;Updated&#39;. | [optional] [default to ]
 **startdate** | **datetime**| DateTime, Filters device events where event date falls on/after this startdate time. Start date should be within 30 days of the current date. | [optional] [default to ]
 **enddate** | **datetime**| DateTime, Filters device events where event date falls on/before this enddate time. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 
 **sortorder** | **str**| Sorting order. Values ASC or DESC. Defaults to ASC. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_managed_settings_for_device_by_alternate_id**
> devices_managed_settings_for_device_by_alternate_id(settings=settings, search_by=search_by, id=id)

Sets the managed settings for an iOS device based on alternate id.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
settings = mdmv1.DeviceManagedSettings() # DeviceManagedSettings | Managed settings. (optional)
search_by = '' # str | The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber, EasId]. (optional) (default to )
id = '' # str | The alternate id of the device. (optional) (default to )

try:
    # Sets the managed settings for an iOS device based on alternate id.
    api_instance.devices_managed_settings_for_device_by_alternate_id(settings=settings, search_by=search_by, id=id)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_managed_settings_for_device_by_alternate_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**DeviceManagedSettings**](DeviceManagedSettings.md)| Managed settings. | [optional] 
 **search_by** | **str**| The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber, EasId]. | [optional] [default to ]
 **id** | **str**| The alternate id of the device. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_search_async**
> DeviceSearchResultExtended devices_search_async(user=user, model=model, platform=platform, lastseen=lastseen, ownership=ownership, lgid=lgid, compliantstatus=compliantstatus, seensince=seensince, page=page, pagesize=pagesize, orderby=orderby, sortorder=sortorder)

New - Find relevant devices using various criteria.

 Returns details of relevant devices belonging to an enrollment user matching specified criteria, where results are ranked/sorted using the specified orderby criteria with maximum pagesize limit of 500.  If page size is greater than the maximum limit, it will return the first 500 records.  seensince and lastseen fields accept the following Valid DateTime formats :  yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt,  yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
user = '' # str | Filters devices based on enrolled username. (optional) (default to )
model = '' # str | Filters devices based on model. For example iPhone. (optional) (default to )
platform = '' # str | Filters devices based on platform. For example Apple. (optional) (default to )
lastseen = '' # datetime | Filters devices based on the date when they were last seen. (optional) (default to )
ownership = '' # str | Filters devices based on ownership type. One of C, E, S or Undefined. (optional) (default to )
lgid = 56 # int | Limits the search to given OrganizationGroup. Defaults to admin's OrganizationGroup. (optional)
compliantstatus = '' # str | Filters devices based on specified compliant status. Possible values are true (for Compliant) and false (for NonCompliant). (optional) (default to )
seensince = '' # datetime | Filters devices based on date when they were seen after given date. (optional) (default to )
page = 56 # int | Filters search result to return results based on page number. Page numbering is 0 based and omitting this parameter will return the first page. (optional)
pagesize = 56 # int | Limits the number of search results per page. Defaults to 500. (optional)
orderby = '' # str | Sort results based on given field. One of model, lastseen, ownership, platform, deviceid etc. Defaults to deviceid. (optional) (default to )
sortorder = '' # str | Sort order of results. One of ASC or DESC. Defaults to ASC. (optional) (default to )

try:
    # New - Find relevant devices using various criteria.
    api_response = api_instance.devices_search_async(user=user, model=model, platform=platform, lastseen=lastseen, ownership=ownership, lgid=lgid, compliantstatus=compliantstatus, seensince=seensince, page=page, pagesize=pagesize, orderby=orderby, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Filters devices based on enrolled username. | [optional] [default to ]
 **model** | **str**| Filters devices based on model. For example iPhone. | [optional] [default to ]
 **platform** | **str**| Filters devices based on platform. For example Apple. | [optional] [default to ]
 **lastseen** | **datetime**| Filters devices based on the date when they were last seen. | [optional] [default to ]
 **ownership** | **str**| Filters devices based on ownership type. One of C, E, S or Undefined. | [optional] [default to ]
 **lgid** | **int**| Limits the search to given OrganizationGroup. Defaults to admin&#39;s OrganizationGroup. | [optional] 
 **compliantstatus** | **str**| Filters devices based on specified compliant status. Possible values are true (for Compliant) and false (for NonCompliant). | [optional] [default to ]
 **seensince** | **datetime**| Filters devices based on date when they were seen after given date. | [optional] [default to ]
 **page** | **int**| Filters search result to return results based on page number. Page numbering is 0 based and omitting this parameter will return the first page. | [optional] 
 **pagesize** | **int**| Limits the number of search results per page. Defaults to 500. | [optional] 
 **orderby** | **str**| Sort results based on given field. One of model, lastseen, ownership, platform, deviceid etc. Defaults to deviceid. | [optional] [default to ]
 **sortorder** | **str**| Sort order of results. One of ASC or DESC. Defaults to ASC. | [optional] [default to ]

### Return type

[**DeviceSearchResultExtended**](DeviceSearchResultExtended.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_send_message**
> devices_send_message(id, generic_message=generic_message)

Sends a push notification to the device identified by device ID. If not enrolled, sends an SMS message instead.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
id = 'id_example' # str | The device ID.
generic_message = mdmv1.GenericMessage() # GenericMessage | The message to send. (optional)

try:
    # Sends a push notification to the device identified by device ID. If not enrolled, sends an SMS message instead.
    api_instance.devices_send_message(id, generic_message=generic_message)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The device ID. | 
 **generic_message** | [**GenericMessage**](GenericMessage.md)| The message to send. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_send_message_by_mac**
> devices_send_message_by_mac(macaddress, generic_message=generic_message)

Sends a push notification to the device identified by MAC address. If not enrolled, sends an SMS message instead.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
macaddress = 'macaddress_example' # str | The MAC address of the device.
generic_message = mdmv1.GenericMessage() # GenericMessage | The message to send. (optional)

try:
    # Sends a push notification to the device identified by MAC address. If not enrolled, sends an SMS message instead.
    api_instance.devices_send_message_by_mac(macaddress, generic_message=generic_message)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_send_message_by_mac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **macaddress** | **str**| The MAC address of the device. | 
 **generic_message** | [**GenericMessage**](GenericMessage.md)| The message to send. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_send_message_by_serial_number**
> devices_send_message_by_serial_number(serialnumber, generic_message=generic_message)

Sends a push notification to the device identified by serial number. If not enrolled, sends an SMS message instead.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
serialnumber = 'serialnumber_example' # str | The serial number of the device.
generic_message = mdmv1.GenericMessage() # GenericMessage | The message to send. (optional)

try:
    # Sends a push notification to the device identified by serial number. If not enrolled, sends an SMS message instead.
    api_instance.devices_send_message_by_serial_number(serialnumber, generic_message=generic_message)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_send_message_by_serial_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialnumber** | **str**| The serial number of the device. | 
 **generic_message** | [**GenericMessage**](GenericMessage.md)| The message to send. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_send_message_by_udid**
> devices_send_message_by_udid(udid, generic_message=generic_message)

Sends a push notification to the device identified by UDID. If not enrolled, sends an SMS message instead.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
udid = 'udid_example' # str | The UDID of the device.
generic_message = mdmv1.GenericMessage() # GenericMessage | The message to send. (optional)

try:
    # Sends a push notification to the device identified by UDID. If not enrolled, sends an SMS message instead.
    api_instance.devices_send_message_by_udid(udid, generic_message=generic_message)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_send_message_by_udid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **udid** | **str**| The UDID of the device. | 
 **generic_message** | [**GenericMessage**](GenericMessage.md)| The message to send. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_update_custom_attributes_by_asset_nr**
> devices_update_custom_attributes_by_asset_nr(assetnumber, custom_attributes=custom_attributes)

Updates the device custom attribute value if already present for a device, else adds the same to the device.

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
api_instance = mdmv1.DevicesApi(mdmv1.ApiClient(configuration))
assetnumber = 'assetnumber_example' # str | Device Asset number.
custom_attributes = mdmv1.DeviceCustomAttributeListModel() # DeviceCustomAttributeListModel | Custom Attribute name and value pairs. (optional)

try:
    # Updates the device custom attribute value if already present for a device, else adds the same to the device.
    api_instance.devices_update_custom_attributes_by_asset_nr(assetnumber, custom_attributes=custom_attributes)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_update_custom_attributes_by_asset_nr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetnumber** | **str**| Device Asset number. | 
 **custom_attributes** | [**DeviceCustomAttributeListModel**](DeviceCustomAttributeListModel.md)| Custom Attribute name and value pairs. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

