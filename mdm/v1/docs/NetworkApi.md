# mdmv1.NetworkApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_get_network_info_by_alternate_id**](NetworkApi.md#network_get_network_info_by_alternate_id) | **GET** /devices/network | Returns network information of single device from alternate device identifier.
[**network_get_network_info_by_device**](NetworkApi.md#network_get_network_info_by_device) | **GET** /devices/{id}/network | Returns network information of single device specified by id parameter.
[**network_network_info_search**](NetworkApi.md#network_network_info_search) | **GET** /devices/networkinfosearch | Finds device network information matching specified criteria.


# **network_get_network_info_by_alternate_id**
> DeviceNetworkInfoEntityModel network_get_network_info_by_alternate_id(search_by, id)

Returns network information of single device from alternate device identifier.

Returns network information including voice and data roamingstatus, IP address, WiFi details for a device based on alternate ID like MAC address, UUID, Serial number, IMEI number.

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
api_instance = mdmv1.NetworkApi(mdmv1.ApiClient(configuration))
search_by = '' # str | Alternate device identifier type. One of Macaddress, Udid, Serialnumber or ImeiNumber (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837) (Required). (default to )
id = '' # str | Device alternate ID (Required). (default to )

try:
    # Returns network information of single device from alternate device identifier.
    api_response = api_instance.network_get_network_info_by_alternate_id(search_by, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->network_get_network_info_by_alternate_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| Alternate device identifier type. One of Macaddress, Udid, Serialnumber or ImeiNumber (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837) (Required). | [default to ]
 **id** | **str**| Device alternate ID (Required). | [default to ]

### Return type

[**DeviceNetworkInfoEntityModel**](DeviceNetworkInfoEntityModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_get_network_info_by_device**
> DeviceNetworkInfoEntityModel network_get_network_info_by_device(id)

Returns network information of single device specified by id parameter.

Returns network information including voice and data roamingstatus, IP address and WiFi details for a device identified by the ID provided.

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
api_instance = mdmv1.NetworkApi(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID for which network info is to be retrieved.(Required).

try:
    # Returns network information of single device specified by id parameter.
    api_response = api_instance.network_get_network_info_by_device(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->network_get_network_info_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID for which network info is to be retrieved.(Required). | 

### Return type

[**DeviceNetworkInfoEntityModel**](DeviceNetworkInfoEntityModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_network_info_search**
> NetworkInfoSearchResult network_network_info_search(user=user, model=model, platform=platform, lastseen=lastseen, ownership=ownership, lgid=lgid, compliantstatus=compliantstatus, seensince=seensince, page=page, pagesize=pagesize, sortorder=sortorder)

Finds device network information matching specified criteria.

Returns network information like device IP address along with corresponding device id which satisfies given criteria.  <br />  seensince and lastseen fields accept the following Valid DateTime formats :  yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt,  yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.NetworkApi(mdmv1.ApiClient(configuration))
user = '' # str | Filters results based on Enrolled username. (optional) (default to )
model = '' # str | Filters results based on Device model. For example iPhone. (optional) (default to )
platform = '' # str | Filters results based on Device platform. For example Apple. (optional) (default to )
lastseen = '' # str | Filters result based on Device Last seen date. (optional) (default to )
ownership = '' # str | Filters result based on Device Ownership. One of C, E, S or Undefined. (optional) (default to )
lgid = 56 # int | Limits search results to given OrganizationGroup. Defaults to user's OrganizationGroup. (optional)
compliantstatus = '' # str | Filters results based on Device Complaint status. One of Compliant, NonCompliant or NotAvailable. (optional) (default to )
seensince = '' # str | Filters results based on the devices that are seen after given date. (optional) (default to )
page = 56 # int | Filters results to show records present in only given page number. Page numbering is 0 based and omitting this parameter will return first page. (optional)
pagesize = 56 # int | Limits the number of search results per page. Defaults to 500. (optional)
sortorder = '' # str | Sort order of results.One of ASC or DESC. Defaults to ASC. (optional) (default to )

try:
    # Finds device network information matching specified criteria.
    api_response = api_instance.network_network_info_search(user=user, model=model, platform=platform, lastseen=lastseen, ownership=ownership, lgid=lgid, compliantstatus=compliantstatus, seensince=seensince, page=page, pagesize=pagesize, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->network_network_info_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Filters results based on Enrolled username. | [optional] [default to ]
 **model** | **str**| Filters results based on Device model. For example iPhone. | [optional] [default to ]
 **platform** | **str**| Filters results based on Device platform. For example Apple. | [optional] [default to ]
 **lastseen** | **str**| Filters result based on Device Last seen date. | [optional] [default to ]
 **ownership** | **str**| Filters result based on Device Ownership. One of C, E, S or Undefined. | [optional] [default to ]
 **lgid** | **int**| Limits search results to given OrganizationGroup. Defaults to user&#39;s OrganizationGroup. | [optional] 
 **compliantstatus** | **str**| Filters results based on Device Complaint status. One of Compliant, NonCompliant or NotAvailable. | [optional] [default to ]
 **seensince** | **str**| Filters results based on the devices that are seen after given date. | [optional] [default to ]
 **page** | **int**| Filters results to show records present in only given page number. Page numbering is 0 based and omitting this parameter will return first page. | [optional] 
 **pagesize** | **int**| Limits the number of search results per page. Defaults to 500. | [optional] 
 **sortorder** | **str**| Sort order of results.One of ASC or DESC. Defaults to ASC. | [optional] [default to ]

### Return type

[**NetworkInfoSearchResult**](NetworkInfoSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

