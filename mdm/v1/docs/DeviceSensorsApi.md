# mdmv1.DeviceSensorsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_sensors_get_device_sensors_by_device_uuid_async**](DeviceSensorsApi.md#device_sensors_get_device_sensors_by_device_uuid_async) | **GET** /devices/{deviceUuid}/sensors | New - Returns the list of sensors reported by the specified device.


# **device_sensors_get_device_sensors_by_device_uuid_async**
> DeviceSensorSearchResponseModel device_sensors_get_device_sensors_by_device_uuid_async(device_uuid, search_text=search_text, limit=limit, offset=offset, orderby=orderby, sort_order=sort_order)

New - Returns the list of sensors reported by the specified device.

Gets the list of sensors reported by the specified device.

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
api_instance = mdmv1.DeviceSensorsApi(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | The unique identifier of the device.              Accepted formats **guid**.              E.g. 3d958f38-246e-4854-a306-189d941ab073.(Required)
search_text = '' # str | Filter records based on the sensor name and value. Pattern search will be performed. (optional) (default to )
limit = 56 # int | An integer that indicates the maximum number of results to return. Valid input range for this property is 1 to 2000. (Default value - 50). (optional)
offset = 56 # int | An integer describing the starting position in the result set. Valid input range for this property is 0 to 2000. (Default value - 0). (optional)
orderby = '' # str | Name of the property used for sorting. Default is Name. Accepted values are [name] and [last_executed_at]. (optional) (default to )
sort_order = '' # str | Whether the sort order is ascending or descending. Default value is Asc. Accepted values are [Asc] and [Desc]. (optional) (default to )

try:
    # New - Returns the list of sensors reported by the specified device.
    api_response = api_instance.device_sensors_get_device_sensors_by_device_uuid_async(device_uuid, search_text=search_text, limit=limit, offset=offset, orderby=orderby, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSensorsApi->device_sensors_get_device_sensors_by_device_uuid_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| The unique identifier of the device.              Accepted formats **guid**.              E.g. 3d958f38-246e-4854-a306-189d941ab073.(Required) | 
 **search_text** | **str**| Filter records based on the sensor name and value. Pattern search will be performed. | [optional] [default to ]
 **limit** | **int**| An integer that indicates the maximum number of results to return. Valid input range for this property is 1 to 2000. (Default value - 50). | [optional] 
 **offset** | **int**| An integer describing the starting position in the result set. Valid input range for this property is 0 to 2000. (Default value - 0). | [optional] 
 **orderby** | **str**| Name of the property used for sorting. Default is Name. Accepted values are [name] and [last_executed_at]. | [optional] [default to ]
 **sort_order** | **str**| Whether the sort order is ascending or descending. Default value is Asc. Accepted values are [Asc] and [Desc]. | [optional] [default to ]

### Return type

[**DeviceSensorSearchResponseModel**](DeviceSensorSearchResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

