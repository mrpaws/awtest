# mdmv2.DevicesV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_check_out_device_to_user_async**](DevicesV2Api.md#devices_v2_check_out_device_to_user_async) | **PATCH** /devices/{id}/enrollmentuser/{enrollmentuserid} | New - Check In and Check Out the device to the Multi-Staging enrollment User. The checkout action is supported only for MacOS and iOS devices.
[**devices_v2_get_by_uuid_async**](DevicesV2Api.md#devices_v2_get_by_uuid_async) | **GET** /devices/{uuid} | New - Get basic details about the device
[**devices_v2_get_device_installs_async**](DevicesV2Api.md#devices_v2_get_device_installs_async) | **GET** /devices/{uuid}/installs | New - Retrieve application install status for an AFW device
[**devices_v2_get_os_updates_by_uuid_async**](DevicesV2Api.md#devices_v2_get_os_updates_by_uuid_async) | **GET** /devices/{uuid}/osupdate | New - Retrieves available OS updates for a device
[**devices_v2_search_async**](DevicesV2Api.md#devices_v2_search_async) | **GET** /devices/search | New - Find relevant devices using various criteria.


# **devices_v2_check_out_device_to_user_async**
> devices_v2_check_out_device_to_user_async(id, enrollmentuserid)

New - Check In and Check Out the device to the Multi-Staging enrollment User. The checkout action is supported only for MacOS and iOS devices.

Check In and Check Out the device to the Multi-Staging enrollment User. This API returns a 400 - BadRequest if device is not enrolled to Multi-Staging enrollment User.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DevicesV2Api(mdmv2.ApiClient(configuration))
id = 56 # int | Device Identifier.(Required).
enrollmentuserid = 56 # int | Enrollment User Identifier.(Required).

try:
    # New - Check In and Check Out the device to the Multi-Staging enrollment User. The checkout action is supported only for MacOS and iOS devices.
    api_instance.devices_v2_check_out_device_to_user_async(id, enrollmentuserid)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_check_out_device_to_user_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device Identifier.(Required). | 
 **enrollmentuserid** | **int**| Enrollment User Identifier.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_get_by_uuid_async**
> GetDeviceResponseV2Model devices_v2_get_by_uuid_async(uuid)

New - Get basic details about the device

Get basic information about the device based on the unique identifier passed in the path. The response contains hypermedia links, which can be followed to get more information about the device. The API returns a 404 - NotFound if the device is not available.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DevicesV2Api(mdmv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Device identifier(Required).

try:
    # New - Get basic details about the device
    api_response = api_instance.devices_v2_get_by_uuid_async(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_get_by_uuid_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Device identifier(Required). | 

### Return type

[**GetDeviceResponseV2Model**](GetDeviceResponseV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_get_device_installs_async**
> AndroidWorkInstallResponseModel devices_v2_get_device_installs_async(uuid, install_id)

New - Retrieve application install status for an AFW device

Retrieve application install status for an AFW device. The API returns a 404 - NotFound if the device is not available.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DevicesV2Api(mdmv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier for a device. Ex. 827BE1C5AEC05C378C61C44103E9D3FCB2EC354D(Required).
install_id = '' # str | Bundle id(Required) (default to )

try:
    # New - Retrieve application install status for an AFW device
    api_response = api_instance.devices_v2_get_device_installs_async(uuid, install_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_get_device_installs_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier for a device. Ex. 827BE1C5AEC05C378C61C44103E9D3FCB2EC354D(Required). | 
 **install_id** | **str**| Bundle id(Required) | [default to ]

### Return type

[**AndroidWorkInstallResponseModel**](AndroidWorkInstallResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_get_os_updates_by_uuid_async**
> OSUpdateResultModel devices_v2_get_os_updates_by_uuid_async(uuid)

New - Retrieves available OS updates for a device

Retrieves a list of all available OS and software updates for the device specified by the device UDID.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DevicesV2Api(mdmv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier for a device. Ex. 153B4D9D-24DC-416B-91F9-94253D623611(Required).

try:
    # New - Retrieves available OS updates for a device
    api_response = api_instance.devices_v2_get_os_updates_by_uuid_async(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_get_os_updates_by_uuid_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier for a device. Ex. 153B4D9D-24DC-416B-91F9-94253D623611(Required). | 

### Return type

[**OSUpdateResultModel**](OSUpdateResultModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_search_async**
> DeviceSearchResultExtended devices_v2_search_async(user=user, model=model, platform=platform, lastseen=lastseen, ownership=ownership, lgid=lgid, compliance_status=compliance_status, seen_since=seen_since, page=page, pagesize=pagesize, orderby=orderby, sortorder=sortorder)

New - Find relevant devices using various criteria.

 Returns details of relevant devices belonging to an enrollment user matching specified criteria, where results are ranked/sorted using the specified orderby criteria with maximum pagesize limit of 500.   If page size is greater than the maximum limit, it will return the first 500 records.  seensince and lastseen fields accept the following Valid DateTime formats :  yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt,  yyyy-MM-ddTHH-mm-ss-tt.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DevicesV2Api(mdmv2.ApiClient(configuration))
user = '' # str | Filters devices based on enrolled username. (optional) (default to )
model = '' # str | Filters devices based on model. For example iPhone. (optional) (default to )
platform = '' # str | Filters devices based on platform. For example Apple. (optional) (default to )
lastseen = '' # datetime | Filters devices based on date when they were last seen. (optional) (default to )
ownership = '' # str | Filters devices based on ownership type. One of C, E, S or Undefined. (optional) (default to )
lgid = 56 # int | Limits the search to given OrganizationGroup, defaults to user's OrganizationGroup. (optional)
compliance_status = '' # str | Filters devices based on specified compliance status. Possible values are true (for Compliant) and false (for NonCompliant). (optional) (default to )
seen_since = '' # datetime | Filters devices based on the date when they were seen after the given date. (optional) (default to )
page = 56 # int | Filters search result to return results based on page number. Page numbering is 0 based and omitting this parameter will return first page. (optional)
pagesize = 56 # int | Limits the number of search results per page. Defaults to 500. (optional)
orderby = '' # str | Sort results based on given field. One of model, lastseen, ownership, platform, deviceid etc. Defaults to deviceid. (optional) (default to )
sortorder = '' # str | Sort order of results. One of ASC or DESC. Defaults to ASC. (optional) (default to )

try:
    # New - Find relevant devices using various criteria.
    api_response = api_instance.devices_v2_search_async(user=user, model=model, platform=platform, lastseen=lastseen, ownership=ownership, lgid=lgid, compliance_status=compliance_status, seen_since=seen_since, page=page, pagesize=pagesize, orderby=orderby, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Filters devices based on enrolled username. | [optional] [default to ]
 **model** | **str**| Filters devices based on model. For example iPhone. | [optional] [default to ]
 **platform** | **str**| Filters devices based on platform. For example Apple. | [optional] [default to ]
 **lastseen** | **datetime**| Filters devices based on date when they were last seen. | [optional] [default to ]
 **ownership** | **str**| Filters devices based on ownership type. One of C, E, S or Undefined. | [optional] [default to ]
 **lgid** | **int**| Limits the search to given OrganizationGroup, defaults to user&#39;s OrganizationGroup. | [optional] 
 **compliance_status** | **str**| Filters devices based on specified compliance status. Possible values are true (for Compliant) and false (for NonCompliant). | [optional] [default to ]
 **seen_since** | **datetime**| Filters devices based on the date when they were seen after the given date. | [optional] [default to ]
 **page** | **int**| Filters search result to return results based on page number. Page numbering is 0 based and omitting this parameter will return first page. | [optional] 
 **pagesize** | **int**| Limits the number of search results per page. Defaults to 500. | [optional] 
 **orderby** | **str**| Sort results based on given field. One of model, lastseen, ownership, platform, deviceid etc. Defaults to deviceid. | [optional] [default to ]
 **sortorder** | **str**| Sort order of results. One of ASC or DESC. Defaults to ASC. | [optional] [default to ]

### Return type

[**DeviceSearchResultExtended**](DeviceSearchResultExtended.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

