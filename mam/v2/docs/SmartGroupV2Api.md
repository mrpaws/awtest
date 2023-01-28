# mamv2.SmartGroupV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smart_group_v2_add_bsp_app_to_smart_group_async**](SmartGroupV2Api.md#smart_group_v2_add_bsp_app_to_smart_group_async) | **POST** /apps/public/{applicationId}/bspsmartgroups | New - Assigns Smart Groups to an BSP Application.


# **smart_group_v2_add_bsp_app_to_smart_group_async**
> smart_group_v2_add_bsp_app_to_smart_group_async(application_id, offlinesmartgroupid=offlinesmartgroupid, onlinesmartgroupid=onlinesmartgroupid, type=type)

New - Assigns Smart Groups to an BSP Application.

Assigns smartgroup identified by the smartgroup id to the BSP application.

### Example
```python
from __future__ import print_function
import time
import mamv2
from mamv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv2.SmartGroupV2Api(mamv2.ApiClient(configuration))
application_id = 56 # int | Application Id.
offlinesmartgroupid = '' # str | Offline smart group Identifier. (optional) (default to )
onlinesmartgroupid = '' # str | Online smart group Identifier. (optional) (default to )
type = '' # str | Type is {harmony/airwatch}. (optional) (default to )

try:
    # New - Assigns Smart Groups to an BSP Application.
    api_instance.smart_group_v2_add_bsp_app_to_smart_group_async(application_id, offlinesmartgroupid=offlinesmartgroupid, onlinesmartgroupid=onlinesmartgroupid, type=type)
except ApiException as e:
    print("Exception when calling SmartGroupV2Api->smart_group_v2_add_bsp_app_to_smart_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| Application Id. | 
 **offlinesmartgroupid** | **str**| Offline smart group Identifier. | [optional] [default to ]
 **onlinesmartgroupid** | **str**| Online smart group Identifier. | [optional] [default to ]
 **type** | **str**| Type is {harmony/airwatch}. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

