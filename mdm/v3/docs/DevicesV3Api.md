# mdmv3.DevicesV3Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v3_get_by_uuid_async**](DevicesV3Api.md#devices_v3_get_by_uuid_async) | **GET** /devices/{uuid} | New - Get basic details about the device.
[**devices_v3_search_async**](DevicesV3Api.md#devices_v3_search_async) | **GET** /devices/search | New - Searches the device using the query information provided.


# **devices_v3_get_by_uuid_async**
> DeviceResponseV3Model devices_v3_get_by_uuid_async(uuid)

New - Get basic details about the device.

Get basic information about the device based on the unique identifier passed in the path. The response contains hypermedia links, which can be followed to get more information about the device.

### Example
```python
from __future__ import print_function
import time
import mdmv3
from mdmv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv3.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv3.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv3.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv3.DevicesV3Api(mdmv3.ApiClient(configuration))
uuid = 'uuid_example' # str | Device unique identifier.(Required).

try:
    # New - Get basic details about the device.
    api_response = api_instance.devices_v3_get_by_uuid_async(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV3Api->devices_v3_get_by_uuid_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Device unique identifier.(Required). | 

### Return type

[**DeviceResponseV3Model**](DeviceResponseV3Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v3_search_async**
> DeviceSearchResultExtendedV2 devices_v3_search_async(user=user, model_identifier=model_identifier, device_type=device_type, last_seen=last_seen, ownership=ownership, organization_group_uuid=organization_group_uuid, compliance_status=compliance_status, seen_since=seen_since, page=page, page_size=page_size, order_by=order_by, sort_order=sort_order)

New - Searches the device using the query information provided.

Get basic information about the device with maximum pagesize limit of 500. If page size is greater than the maximum limit, it will return the first 500 records.

### Example
```python
from __future__ import print_function
import time
import mdmv3
from mdmv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv3.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv3.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv3.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv3.DevicesV3Api(mdmv3.ApiClient(configuration))
user = '' # str | Username the device enrolled under. (optional) (default to )
model_identifier = '' # str | Partial search by device model. Search by MD20 would return device with model MD200LL. (optional) (default to )
device_type = '' # str | Device platform type, i.e. Apple, Android, WindowsPC, etc. (optional) (default to )
last_seen = '' # datetime | Last seen date string. (optional) (default to )
ownership = '' # str | Device ownership. (optional) (default to )
organization_group_uuid = '' # str | Organization Group to be searched. User's OG is considered if not specified. (optional) (default to )
compliance_status = '' # str | Compliance status. (optional) (default to )
seen_since = '' # datetime | Specifies the date filter for device search, which retrieves the devices that are seen after this date. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
page_size = 56 # int | Maximum records per page. Default 500. (optional)
order_by = '' # str | Order by column name. (optional) (default to )
sort_order = '' # str | Sorting order. Values ASC or DESC. Defaults to ASC. (optional) (default to )

try:
    # New - Searches the device using the query information provided.
    api_response = api_instance.devices_v3_search_async(user=user, model_identifier=model_identifier, device_type=device_type, last_seen=last_seen, ownership=ownership, organization_group_uuid=organization_group_uuid, compliance_status=compliance_status, seen_since=seen_since, page=page, page_size=page_size, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV3Api->devices_v3_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username the device enrolled under. | [optional] [default to ]
 **model_identifier** | **str**| Partial search by device model. Search by MD20 would return device with model MD200LL. | [optional] [default to ]
 **device_type** | **str**| Device platform type, i.e. Apple, Android, WindowsPC, etc. | [optional] [default to ]
 **last_seen** | **datetime**| Last seen date string. | [optional] [default to ]
 **ownership** | **str**| Device ownership. | [optional] [default to ]
 **organization_group_uuid** | **str**| Organization Group to be searched. User&#39;s OG is considered if not specified. | [optional] [default to ]
 **compliance_status** | **str**| Compliance status. | [optional] [default to ]
 **seen_since** | **datetime**| Specifies the date filter for device search, which retrieves the devices that are seen after this date. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **page_size** | **int**| Maximum records per page. Default 500. | [optional] 
 **order_by** | **str**| Order by column name. | [optional] [default to ]
 **sort_order** | **str**| Sorting order. Values ASC or DESC. Defaults to ASC. | [optional] [default to ]

### Return type

[**DeviceSearchResultExtendedV2**](DeviceSearchResultExtendedV2.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

