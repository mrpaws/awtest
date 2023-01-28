# memv1.MEMDevicesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mem*

Method | HTTP request | Description
------------- | ------------- | -------------
[**m_em_devices_search**](MEMDevicesApi.md#m_em_devices_search) | **GET** /memdevices/search | Searches for the MEM Devices.


# **m_em_devices_search**
> MEMDeviceSearchResult m_em_devices_search(organizationgroupid=organizationgroupid, page=page, pagesize=pagesize)

Searches for the MEM Devices.

Given a page index (row index) and page size, it gets the MEM Devices for a particular Organization Group.

### Example
```python
from __future__ import print_function
import time
import memv1
from memv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = memv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = memv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = memv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = memv1.MEMDevicesApi(memv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group id. (optional)
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximumm records per page. Default 500. (optional)

try:
    # Searches for the MEM Devices.
    api_response = api_instance.m_em_devices_search(organizationgroupid=organizationgroupid, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MEMDevicesApi->m_em_devices_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group id. | [optional] 
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximumm records per page. Default 500. | [optional] 

### Return type

[**MEMDeviceSearchResult**](MEMDeviceSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

