# mdmv1.ContentsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contents_get_contents_by_alternate_id**](ContentsApi.md#contents_get_contents_by_alternate_id) | **GET** /devices/content | Retrieves the content details of the device identified by alternate ID.
[**contents_get_contents_by_device**](ContentsApi.md#contents_get_contents_by_device) | **GET** /devices/{id}/content | Retrieves the content details of the device identified by device ID.


# **contents_get_contents_by_alternate_id**
> contents_get_contents_by_alternate_id(search_by=search_by, id=id, page=page, pagesize=pagesize)

Retrieves the content details of the device identified by alternate ID.

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
api_instance = mdmv1.ContentsApi(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber]. (optional) (default to )
id = '' # str | Device alternate id. (optional) (default to )
page = 56 # int | The specific page number to get. (optional)
pagesize = 56 # int | Max records per page. (optional)

try:
    # Retrieves the content details of the device identified by alternate ID.
    api_instance.contents_get_contents_by_alternate_id(search_by=search_by, id=id, page=page, pagesize=pagesize)
except ApiException as e:
    print("Exception when calling ContentsApi->contents_get_contents_by_alternate_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber]. | [optional] [default to ]
 **id** | **str**| Device alternate id. | [optional] [default to ]
 **page** | **int**| The specific page number to get. | [optional] 
 **pagesize** | **int**| Max records per page. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contents_get_contents_by_device**
> contents_get_contents_by_device(id, page=page, pagesize=pagesize)

Retrieves the content details of the device identified by device ID.

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
api_instance = mdmv1.ContentsApi(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID.
page = 56 # int | The specific page number to get. (optional)
pagesize = 56 # int | Max records per page. (optional)

try:
    # Retrieves the content details of the device identified by device ID.
    api_instance.contents_get_contents_by_device(id, page=page, pagesize=pagesize)
except ApiException as e:
    print("Exception when calling ContentsApi->contents_get_contents_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID. | 
 **page** | **int**| The specific page number to get. | [optional] 
 **pagesize** | **int**| Max records per page. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

