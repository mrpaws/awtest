# mdmv1.AppsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_admin_app_details_async**](AppsApi.md#apps_admin_app_details_async) | **GET** /devices/{id}/adminapps | Retrieves Admin applications details for passed DeviceID.
[**apps_device_apps_by_alternate_id**](AppsApi.md#apps_device_apps_by_alternate_id) | **GET** /devices/apps | Retrieves application details of the device identified by alternate id.
[**apps_device_apps_by_id**](AppsApi.md#apps_device_apps_by_id) | **GET** /devices/{id}/apps | Retrieves application details of the device identified by device ID.


# **apps_admin_app_details_async**
> apps_admin_app_details_async(id)

Retrieves Admin applications details for passed DeviceID.

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
api_instance = mdmv1.AppsApi(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID.

try:
    # Retrieves Admin applications details for passed DeviceID.
    api_instance.apps_admin_app_details_async(id)
except ApiException as e:
    print("Exception when calling AppsApi->apps_admin_app_details_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_device_apps_by_alternate_id**
> DeviceAppsResult apps_device_apps_by_alternate_id(search_by=search_by, id=id, page=page, pagesize=pagesize)

Retrieves application details of the device identified by alternate id.

Fetches all application details for the device identified by alternate ID other than device ID.  Alternate device identifiers can be MAC address, IMEI, Serial number or UDID.  Example : IMEI-BCG84753GH, Serial Number-573489754.

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
api_instance = mdmv1.AppsApi(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber]. (optional) (default to )
id = '' # str | Device alternate id. (optional) (default to )
page = 56 # int | The specific page number to get. (optional)
pagesize = 56 # int | Max records per page. (optional)

try:
    # Retrieves application details of the device identified by alternate id.
    api_response = api_instance.apps_device_apps_by_alternate_id(search_by=search_by, id=id, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_device_apps_by_alternate_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber]. | [optional] [default to ]
 **id** | **str**| Device alternate id. | [optional] [default to ]
 **page** | **int**| The specific page number to get. | [optional] 
 **pagesize** | **int**| Max records per page. | [optional] 

### Return type

[**DeviceAppsResult**](DeviceAppsResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_device_apps_by_id**
> DeviceAppsResult apps_device_apps_by_id(id, page=page, pagesize=pagesize)

Retrieves application details of the device identified by device ID.

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
api_instance = mdmv1.AppsApi(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID (Required).
page = 56 # int | The specific page number to get. (optional)
pagesize = 56 # int | Max records per page. (optional)

try:
    # Retrieves application details of the device identified by device ID.
    api_response = api_instance.apps_device_apps_by_id(id, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_device_apps_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID (Required). | 
 **page** | **int**| The specific page number to get. | [optional] 
 **pagesize** | **int**| Max records per page. | [optional] 

### Return type

[**DeviceAppsResult**](DeviceAppsResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

