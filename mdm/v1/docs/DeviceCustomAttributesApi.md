# mdmv1.DeviceCustomAttributesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_custom_attributes_bulk_update_device_custom_attributes**](DeviceCustomAttributesApi.md#device_custom_attributes_bulk_update_device_custom_attributes) | **PUT** /devices/customattributes | New - Bulk update of device custom attributes.
[**device_custom_attributes_delete_custom_attributes_by_serial_nr**](DeviceCustomAttributesApi.md#device_custom_attributes_delete_custom_attributes_by_serial_nr) | **DELETE** /devices/serialnumber/{serialnumber}/customattributes | Deletes the device custom attributes by serial number.
[**device_custom_attributes_delete_custom_attributes_for_device_async**](DeviceCustomAttributesApi.md#device_custom_attributes_delete_custom_attributes_for_device_async) | **DELETE** /devices/{id}/customattributes | Deletes the device custom attributes by device id.
[**device_custom_attributes_device_custom_attribute_change_report**](DeviceCustomAttributesApi.md#device_custom_attributes_device_custom_attribute_change_report) | **GET** /devices/customattribute/changereport | Searches for changes made to device custom attributes.
[**device_custom_attributes_device_custom_attribute_search**](DeviceCustomAttributesApi.md#device_custom_attributes_device_custom_attribute_search) | **GET** /devices/customattribute/search | Searches for device custom attributes.
[**device_custom_attributes_update_custom_attributes_async**](DeviceCustomAttributesApi.md#device_custom_attributes_update_custom_attributes_async) | **PUT** /devices/{id}/customattributes | Updates the device custom attribute value by device id.
[**device_custom_attributes_update_custom_attributes_by_asset_nr**](DeviceCustomAttributesApi.md#device_custom_attributes_update_custom_attributes_by_asset_nr) | **PUT** /devices/assetnumber/{assetnumber}/customattributes | Updates the device custom attribute value by asset number.
[**device_custom_attributes_update_custom_attributes_by_serial_nr**](DeviceCustomAttributesApi.md#device_custom_attributes_update_custom_attributes_by_serial_nr) | **PUT** /devices/serialnumber/{serialnumber}/customattributes | Updates the device custom attribute value by serial number.


# **device_custom_attributes_bulk_update_device_custom_attributes**
> CustomAttributesBulkUpdateResponseV1Model device_custom_attributes_bulk_update_device_custom_attributes(devices)

New - Bulk update of device custom attributes.

Device custom attributes of multiple devices are updated in a single call. This API will not add new custom attributes to device, but update existing custom attributes by assigning new values to them. Custom attributes for 500 devices can be updated at a time with this API. Device custom attributes can be updated using device uuid or serial number. Optionally user name can be used with serial number to uniquely identify the device.

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
api_instance = mdmv1.DeviceCustomAttributesApi(mdmv1.ApiClient(configuration))
devices = [mdmv1.DeviceCustomAttributeRequestV1Model()] # list[DeviceCustomAttributeRequestV1Model] | The list of devices to update custom attributes.(Required)

try:
    # New - Bulk update of device custom attributes.
    api_response = api_instance.device_custom_attributes_bulk_update_device_custom_attributes(devices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceCustomAttributesApi->device_custom_attributes_bulk_update_device_custom_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices** | [**list[DeviceCustomAttributeRequestV1Model]**](DeviceCustomAttributeRequestV1Model.md)| The list of devices to update custom attributes.(Required) | 

### Return type

[**CustomAttributesBulkUpdateResponseV1Model**](CustomAttributesBulkUpdateResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_custom_attributes_delete_custom_attributes_by_serial_nr**
> BulkResponseEntity device_custom_attributes_delete_custom_attributes_by_serial_nr(serialnumber, custom_attributes=custom_attributes)

Deletes the device custom attributes by serial number.

Deletes the device custom attributes by serial number for the input Names and Application Groups.

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
api_instance = mdmv1.DeviceCustomAttributesApi(mdmv1.ApiClient(configuration))
serialnumber = 'serialnumber_example' # str | Device Serialnumber (Required).
custom_attributes = mdmv1.DeleteDeviceCustomAttributeListModel() # DeleteDeviceCustomAttributeListModel | Custom attribute list. (optional)

try:
    # Deletes the device custom attributes by serial number.
    api_response = api_instance.device_custom_attributes_delete_custom_attributes_by_serial_nr(serialnumber, custom_attributes=custom_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceCustomAttributesApi->device_custom_attributes_delete_custom_attributes_by_serial_nr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialnumber** | **str**| Device Serialnumber (Required). | 
 **custom_attributes** | [**DeleteDeviceCustomAttributeListModel**](DeleteDeviceCustomAttributeListModel.md)| Custom attribute list. | [optional] 

### Return type

[**BulkResponseEntity**](BulkResponseEntity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_custom_attributes_delete_custom_attributes_for_device_async**
> BulkResponseEntity device_custom_attributes_delete_custom_attributes_for_device_async(id, custom_attributes=custom_attributes)

Deletes the device custom attributes by device id.

Deletes the device custom attributes by device id for the input Names and Application Groups.

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
api_instance = mdmv1.DeviceCustomAttributesApi(mdmv1.ApiClient(configuration))
id = 56 # int | Device Identifier (Required).
custom_attributes = mdmv1.DeleteDeviceCustomAttributeListModel() # DeleteDeviceCustomAttributeListModel | Custom attribute list. (optional)

try:
    # Deletes the device custom attributes by device id.
    api_response = api_instance.device_custom_attributes_delete_custom_attributes_for_device_async(id, custom_attributes=custom_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceCustomAttributesApi->device_custom_attributes_delete_custom_attributes_for_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device Identifier (Required). | 
 **custom_attributes** | [**DeleteDeviceCustomAttributeListModel**](DeleteDeviceCustomAttributeListModel.md)| Custom attribute list. | [optional] 

### Return type

[**BulkResponseEntity**](BulkResponseEntity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_custom_attributes_device_custom_attribute_change_report**
> DeviceCustomAttributeChangeReportResult device_custom_attributes_device_custom_attribute_change_report(organizationgroupid=organizationgroupid, deviceid=deviceid, startdate=startdate, enddate=enddate, applicationgroup=applicationgroup, customattributename=customattributename, source=source, page=page, pagesize=pagesize)

Searches for changes made to device custom attributes.

Searches for changes made to device custom attributes based on the input device id, custom attribute name, source, application group and other filtering attributes.

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
api_instance = mdmv1.DeviceCustomAttributesApi(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group id to be searched, user's OG is considered if not sent. (optional)
deviceid = 56 # int | Device id to search. (optional)
startdate = '' # datetime | Filters the custom attributes which are modified after this datetime. (optional) (default to )
enddate = '' # datetime | Filters the custom attributes which are modified before this datetime. (optional) (default to )
applicationgroup = '' # str | Application group to search. (optional) (default to )
customattributename = '' # str | Custom attribute name to search. (optional) (default to )
source = '' # str | Custom attribute source to search. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Searches for changes made to device custom attributes.
    api_response = api_instance.device_custom_attributes_device_custom_attribute_change_report(organizationgroupid=organizationgroupid, deviceid=deviceid, startdate=startdate, enddate=enddate, applicationgroup=applicationgroup, customattributename=customattributename, source=source, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceCustomAttributesApi->device_custom_attributes_device_custom_attribute_change_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group id to be searched, user&#39;s OG is considered if not sent. | [optional] 
 **deviceid** | **int**| Device id to search. | [optional] 
 **startdate** | **datetime**| Filters the custom attributes which are modified after this datetime. | [optional] [default to ]
 **enddate** | **datetime**| Filters the custom attributes which are modified before this datetime. | [optional] [default to ]
 **applicationgroup** | **str**| Application group to search. | [optional] [default to ]
 **customattributename** | **str**| Custom attribute name to search. | [optional] [default to ]
 **source** | **str**| Custom attribute source to search. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**DeviceCustomAttributeChangeReportResult**](DeviceCustomAttributeChangeReportResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_custom_attributes_device_custom_attribute_search**
> DeviceCustomAttributeSearchResult device_custom_attributes_device_custom_attribute_search(organizationgroupid=organizationgroupid, deviceid=deviceid, serialnumber=serialnumber, modifiedfrom=modifiedfrom, modifiedtill=modifiedtill, applicationgroup=applicationgroup, customattributename=customattributename, source=source, page=page, pagesize=pagesize)

Searches for device custom attributes.

Searches for device custom attributes based on the input Device ID, Custom Attribute Name, Source, Application Group and other filtering attributes.

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
api_instance = mdmv1.DeviceCustomAttributesApi(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group id to be searched, user's OG is considered if not sent. (optional)
deviceid = 56 # int | Device id to search. (optional)
serialnumber = '' # str | Device serial number to search. (optional) (default to )
modifiedfrom = '' # datetime | Filters the custom attributes which are modified after this datetime. (optional) (default to )
modifiedtill = '' # datetime | Filters the custom attributes which are modified before this datetime. (optional) (default to )
applicationgroup = '' # str | Application group to search. (optional) (default to )
customattributename = '' # str | Custom attribute name to search. (optional) (default to )
source = '' # str | Custom attribute source to search. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Searches for device custom attributes.
    api_response = api_instance.device_custom_attributes_device_custom_attribute_search(organizationgroupid=organizationgroupid, deviceid=deviceid, serialnumber=serialnumber, modifiedfrom=modifiedfrom, modifiedtill=modifiedtill, applicationgroup=applicationgroup, customattributename=customattributename, source=source, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceCustomAttributesApi->device_custom_attributes_device_custom_attribute_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group id to be searched, user&#39;s OG is considered if not sent. | [optional] 
 **deviceid** | **int**| Device id to search. | [optional] 
 **serialnumber** | **str**| Device serial number to search. | [optional] [default to ]
 **modifiedfrom** | **datetime**| Filters the custom attributes which are modified after this datetime. | [optional] [default to ]
 **modifiedtill** | **datetime**| Filters the custom attributes which are modified before this datetime. | [optional] [default to ]
 **applicationgroup** | **str**| Application group to search. | [optional] [default to ]
 **customattributename** | **str**| Custom attribute name to search. | [optional] [default to ]
 **source** | **str**| Custom attribute source to search. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**DeviceCustomAttributeSearchResult**](DeviceCustomAttributeSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_custom_attributes_update_custom_attributes_async**
> BulkResponse device_custom_attributes_update_custom_attributes_async(id, custom_attributes)

Updates the device custom attribute value by device id.

Updates the device custom attribute value by device id if already present for a device, else adds the same to the device.

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
api_instance = mdmv1.DeviceCustomAttributesApi(mdmv1.ApiClient(configuration))
id = 56 # int | Device Identifier (Required).
custom_attributes = mdmv1.DeviceCustomAttributeListModel() # DeviceCustomAttributeListModel | Custom Attribute name and value pairs (Required).

try:
    # Updates the device custom attribute value by device id.
    api_response = api_instance.device_custom_attributes_update_custom_attributes_async(id, custom_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceCustomAttributesApi->device_custom_attributes_update_custom_attributes_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device Identifier (Required). | 
 **custom_attributes** | [**DeviceCustomAttributeListModel**](DeviceCustomAttributeListModel.md)| Custom Attribute name and value pairs (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_custom_attributes_update_custom_attributes_by_asset_nr**
> BulkResponse device_custom_attributes_update_custom_attributes_by_asset_nr(assetnumber, custom_attributes)

Updates the device custom attribute value by asset number.

Updates the device custom attribute value if already present for a device, else adds the same to the device.

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
api_instance = mdmv1.DeviceCustomAttributesApi(mdmv1.ApiClient(configuration))
assetnumber = 'assetnumber_example' # str | Device Assetnumber (Required).
custom_attributes = mdmv1.DeviceCustomAttributeListModel() # DeviceCustomAttributeListModel | Custom Attribute name and value pairs (Required).

try:
    # Updates the device custom attribute value by asset number.
    api_response = api_instance.device_custom_attributes_update_custom_attributes_by_asset_nr(assetnumber, custom_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceCustomAttributesApi->device_custom_attributes_update_custom_attributes_by_asset_nr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetnumber** | **str**| Device Assetnumber (Required). | 
 **custom_attributes** | [**DeviceCustomAttributeListModel**](DeviceCustomAttributeListModel.md)| Custom Attribute name and value pairs (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_custom_attributes_update_custom_attributes_by_serial_nr**
> BulkResponse device_custom_attributes_update_custom_attributes_by_serial_nr(serialnumber, custom_attributes)

Updates the device custom attribute value by serial number.

Updates the device custom attribute value if already present for a device, else adds the same to the device.

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
api_instance = mdmv1.DeviceCustomAttributesApi(mdmv1.ApiClient(configuration))
serialnumber = 'serialnumber_example' # str | Device Serialnumber (Required).
custom_attributes = mdmv1.DeviceCustomAttributeListModel() # DeviceCustomAttributeListModel | Custom Attribute name and value pairs (Required).

try:
    # Updates the device custom attribute value by serial number.
    api_response = api_instance.device_custom_attributes_update_custom_attributes_by_serial_nr(serialnumber, custom_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceCustomAttributesApi->device_custom_attributes_update_custom_attributes_by_serial_nr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialnumber** | **str**| Device Serialnumber (Required). | 
 **custom_attributes** | [**DeviceCustomAttributeListModel**](DeviceCustomAttributeListModel.md)| Custom Attribute name and value pairs (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

