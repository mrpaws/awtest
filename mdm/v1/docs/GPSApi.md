# mdmv1.GPSApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_ps_bulk_gps_coordinates_search_by_device_identifiers**](GPSApi.md#g_ps_bulk_gps_coordinates_search_by_device_identifiers) | **POST** /devices/gps/search | Retrieves the GPS coordinates of multiple devices within the specified day range.
[**g_ps_execute_bulk_gps_coordinates_by_device_by_alternate_id**](GPSApi.md#g_ps_execute_bulk_gps_coordinates_by_device_by_alternate_id) | **POST** /devices/gps | Executes bulk gps coordinates by device and alternate id.
[**g_ps_get_gps_coordinates_by_alternate_id**](GPSApi.md#g_ps_get_gps_coordinates_by_alternate_id) | **GET** /devices/gps | Retrieves the GPS coordinates of the device identified by alternate id.
[**g_ps_get_gps_coordinates_by_device**](GPSApi.md#g_ps_get_gps_coordinates_by_device) | **GET** /devices/{id}/gps | Retrieves the GPS coordinates of the device identified by device ID.


# **g_ps_bulk_gps_coordinates_search_by_device_identifiers**
> list[GpsCoordinate] g_ps_bulk_gps_coordinates_search_by_device_identifiers(bulk_input, search_by=search_by, startdatetime=startdatetime, enddatetime=enddatetime, daterange=daterange)

Retrieves the GPS coordinates of multiple devices within the specified day range.

Retrieves gps co-ordinates in latitude and longitude decimal degree format(i.e. D.D) for specified date range for given searchby query param value type(i.e Macaddress/UDID/Serialnumber/deviceID).  <br />  startdatetime and enddatetime fields accept the following  Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.GPSApi(mdmv1.ApiClient(configuration))
bulk_input = mdmv1.BulkInput() # BulkInput | Bulk input of containing multiple Device Identifiers.(Required).
search_by = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837). (optional) (default to )
startdatetime = '' # datetime | Start Date time. (optional) (default to )
enddatetime = '' # datetime | End Date time. (optional) (default to )
daterange = 56 # int | Number of days in which range device location details needs to be returned. (optional)

try:
    # Retrieves the GPS coordinates of multiple devices within the specified day range.
    api_response = api_instance.g_ps_bulk_gps_coordinates_search_by_device_identifiers(bulk_input, search_by=search_by, startdatetime=startdatetime, enddatetime=enddatetime, daterange=daterange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GPSApi->g_ps_bulk_gps_coordinates_search_by_device_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| Bulk input of containing multiple Device Identifiers.(Required). | 
 **search_by** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837). | [optional] [default to ]
 **startdatetime** | **datetime**| Start Date time. | [optional] [default to ]
 **enddatetime** | **datetime**| End Date time. | [optional] [default to ]
 **daterange** | **int**| Number of days in which range device location details needs to be returned. | [optional] 

### Return type

[**list[GpsCoordinate]**](GpsCoordinate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_ps_execute_bulk_gps_coordinates_by_device_by_alternate_id**
> list[GpsCoordinate] g_ps_execute_bulk_gps_coordinates_by_device_by_alternate_id(bulk_input, search_by=search_by)

Executes bulk gps coordinates by device and alternate id.

Retrieves gps co-ordinates in latitude and longitude decimal degree format(i.e. D.D) for specified bulk input values.

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
api_instance = mdmv1.GPSApi(mdmv1.ApiClient(configuration))
bulk_input = mdmv1.BulkInput() # BulkInput | Bulk input of containing multiple alternate ids.(Required).
search_by = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837). (optional) (default to )

try:
    # Executes bulk gps coordinates by device and alternate id.
    api_response = api_instance.g_ps_execute_bulk_gps_coordinates_by_device_by_alternate_id(bulk_input, search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GPSApi->g_ps_execute_bulk_gps_coordinates_by_device_by_alternate_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| Bulk input of containing multiple alternate ids.(Required). | 
 **search_by** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837). | [optional] [default to ]

### Return type

[**list[GpsCoordinate]**](GpsCoordinate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_ps_get_gps_coordinates_by_alternate_id**
> list[GpsCoordinate] g_ps_get_gps_coordinates_by_alternate_id(search_by, id=id, day_range=day_range)

Retrieves the GPS coordinates of the device identified by alternate id.

Retrieves gps co-ordinates in latitude and longitude decimal degree format(i.e. D.D) for specified dayrange and searchBy type(i.e Macaddress/UDID/Serialnumber) but not deviceID.

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
api_instance = mdmv1.GPSApi(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837) (Required). (default to )
id = '' # str | Device alternate id. (optional) (default to )
day_range = 56 # int | The number of days for which to retrieve GPS coordinates. (optional)

try:
    # Retrieves the GPS coordinates of the device identified by alternate id.
    api_response = api_instance.g_ps_get_gps_coordinates_by_alternate_id(search_by, id=id, day_range=day_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GPSApi->g_ps_get_gps_coordinates_by_alternate_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837) (Required). | [default to ]
 **id** | **str**| Device alternate id. | [optional] [default to ]
 **day_range** | **int**| The number of days for which to retrieve GPS coordinates. | [optional] 

### Return type

[**list[GpsCoordinate]**](GpsCoordinate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_ps_get_gps_coordinates_by_device**
> list[GpsCoordinate] g_ps_get_gps_coordinates_by_device(id, day_range=day_range)

Retrieves the GPS coordinates of the device identified by device ID.

Retrieves gps co-ordinates in latitude and longitude decimal degree format(i.e. D.D) for specified dayrange and device ID.

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
api_instance = mdmv1.GPSApi(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID.(Required).
day_range = 56 # int | The number of days for which to retrieve GPS coordinates. (optional)

try:
    # Retrieves the GPS coordinates of the device identified by device ID.
    api_response = api_instance.g_ps_get_gps_coordinates_by_device(id, day_range=day_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GPSApi->g_ps_get_gps_coordinates_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID.(Required). | 
 **day_range** | **int**| The number of days for which to retrieve GPS coordinates. | [optional] 

### Return type

[**list[GpsCoordinate]**](GpsCoordinate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

