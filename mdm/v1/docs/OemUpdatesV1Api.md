# mdmv1.OemUpdatesV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oem_updates_v1_get_oem_updates_by_device_uuid_async**](OemUpdatesV1Api.md#oem_updates_v1_get_oem_updates_by_device_uuid_async) | **GET** /groups/{uuid}/device/{deviceUuid}/oemupdates | New - Gets all OEM Update Summary details of a given organization group UUID.
[**oem_updates_v1_get_summary_details_async**](OemUpdatesV1Api.md#oem_updates_v1_get_summary_details_async) | **GET** /groups/{uuid}/oemupdates/summary | New - Gets all OEM Update Summary details of a given organization group UUID.
[**oem_updates_v1_get_summary_devices_async**](OemUpdatesV1Api.md#oem_updates_v1_get_summary_devices_async) | **GET** /groups/{uuid}/oemupdates/summary/{summaryUuid}/devices | New - Gets the devices where OEM Update Summary is installed(status would be either failed or success).
[**oem_updates_v1_get_summary_status_async**](OemUpdatesV1Api.md#oem_updates_v1_get_summary_status_async) | **GET** /groups/{uuid}/oemupdates/summary/{summaryUuid}/status | New - Gets the count of OemUpdate Summary installed in devices for a given summaryID.
[**oem_updates_v1_search_async**](OemUpdatesV1Api.md#oem_updates_v1_search_async) | **GET** /groups/{uuid}/oemupdates/summary/search | New - Returns a collection of OemUpdateSummary details based on the search criteria.


# **oem_updates_v1_get_oem_updates_by_device_uuid_async**
> OemUpdateSummarySearchResultV1Model oem_updates_v1_get_oem_updates_by_device_uuid_async(uuid, device_uuid)

New - Gets all OEM Update Summary details of a given organization group UUID.

Returns all OEM Update Summary details of a given organization group id and its children.

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
api_instance = mdmv1.OemUpdatesV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization group UUID to perform the operation on.(Required)
device_uuid = 'device_uuid_example' # str | Device UUID to perform the operation on.(Required)

try:
    # New - Gets all OEM Update Summary details of a given organization group UUID.
    api_response = api_instance.oem_updates_v1_get_oem_updates_by_device_uuid_async(uuid, device_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OemUpdatesV1Api->oem_updates_v1_get_oem_updates_by_device_uuid_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required) | 
 **device_uuid** | [**str**](.md)| Device UUID to perform the operation on.(Required) | 

### Return type

[**OemUpdateSummarySearchResultV1Model**](OemUpdateSummarySearchResultV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oem_updates_v1_get_summary_details_async**
> OemUpdateSummaryResponseV1Model oem_updates_v1_get_summary_details_async(uuid, page=page, page_size=page_size)

New - Gets all OEM Update Summary details of a given organization group UUID.

Returns all OEM Update Summary details of a given organization group id and its children.

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
api_instance = mdmv1.OemUpdatesV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization group UUID to perform the operation on.(Required)
page = 56 # int | Specific page number to get. 0 based index (optional)
page_size = 56 # int | Maximum records per page. Default 50 (optional)

try:
    # New - Gets all OEM Update Summary details of a given organization group UUID.
    api_response = api_instance.oem_updates_v1_get_summary_details_async(uuid, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OemUpdatesV1Api->oem_updates_v1_get_summary_details_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required) | 
 **page** | **int**| Specific page number to get. 0 based index | [optional] 
 **page_size** | **int**| Maximum records per page. Default 50 | [optional] 

### Return type

[**OemUpdateSummaryResponseV1Model**](OemUpdateSummaryResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oem_updates_v1_get_summary_devices_async**
> list[OemUpdateSummaryInstalledDeviceResponseV1Model] oem_updates_v1_get_summary_devices_async(uuid, summary_uuid, page=page, page_size=page_size)

New - Gets the devices where OEM Update Summary is installed(status would be either failed or success).

Returns the devices where the OEM Update is installed(status would be either failed or success).

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
api_instance = mdmv1.OemUpdatesV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization group UUID to perform the operation on.(Required)
summary_uuid = 'summary_uuid_example' # str | Unique value of the OEM Update Summary detail to perform the operation on.(Required)
page = 56 # int | Specific page number to get. 0 based index (optional)
page_size = 56 # int | Maximum records per page. Default 50 (optional)

try:
    # New - Gets the devices where OEM Update Summary is installed(status would be either failed or success).
    api_response = api_instance.oem_updates_v1_get_summary_devices_async(uuid, summary_uuid, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OemUpdatesV1Api->oem_updates_v1_get_summary_devices_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required) | 
 **summary_uuid** | [**str**](.md)| Unique value of the OEM Update Summary detail to perform the operation on.(Required) | 
 **page** | **int**| Specific page number to get. 0 based index | [optional] 
 **page_size** | **int**| Maximum records per page. Default 50 | [optional] 

### Return type

[**list[OemUpdateSummaryInstalledDeviceResponseV1Model]**](OemUpdateSummaryInstalledDeviceResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oem_updates_v1_get_summary_status_async**
> list[OemUpdateSummaryInstalledStatusResponseV1Model] oem_updates_v1_get_summary_status_async(uuid, summary_uuid)

New - Gets the count of OemUpdate Summary installed in devices for a given summaryID.

It will return the summary with installed success and failed count.

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
api_instance = mdmv1.OemUpdatesV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization group UUID to perform the operation on.(Required)
summary_uuid = 'summary_uuid_example' # str | Unique value of the OEM Update Summary detail to perform the operation on.(Required)

try:
    # New - Gets the count of OemUpdate Summary installed in devices for a given summaryID.
    api_response = api_instance.oem_updates_v1_get_summary_status_async(uuid, summary_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OemUpdatesV1Api->oem_updates_v1_get_summary_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required) | 
 **summary_uuid** | [**str**](.md)| Unique value of the OEM Update Summary detail to perform the operation on.(Required) | 

### Return type

[**list[OemUpdateSummaryInstalledStatusResponseV1Model]**](OemUpdateSummaryInstalledStatusResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oem_updates_v1_search_async**
> OemUpdateSummarySearchResultV1Model oem_updates_v1_search_async(uuid, search_text, page=page, page_size=page_size, order_by=order_by, sort_order=sort_order)

New - Returns a collection of OemUpdateSummary details based on the search criteria.

Returns a collection of OemUpdate summary details based on the search criteria specified. The search parameters can be Name, Criticality, UpdateType, Category and the pagesize.   searchcriteria =&gt; /{ce3f9d78-c411-4f02-af77-2a85bad7c262}/summary/search?searchText={intel}&amp;page={1}&amp;pageSize={20}&amp;orderBy={Asc}&amp;sortOrder={name}\")]

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
api_instance = mdmv1.OemUpdatesV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization group UUID to perform the operation on.(Required)
search_text = '' # str | OemUpdate is searched on Name, Message, Criticality, Category and UpdateType(Required) (default to )
page = 56 # int | Specific page number to get. 0 based index (optional)
page_size = 56 # int | Maximum records per page. Default 50 (optional)
order_by = '' # str | Order By.  Default Asc (Example:Asc,Dsc) (optional) (default to )
sort_order = '' # str | Sort Order. Default OemupdateName(Example:OemupdateName, OemupdateCategory) (optional) (default to )

try:
    # New - Returns a collection of OemUpdateSummary details based on the search criteria.
    api_response = api_instance.oem_updates_v1_search_async(uuid, search_text, page=page, page_size=page_size, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OemUpdatesV1Api->oem_updates_v1_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required) | 
 **search_text** | **str**| OemUpdate is searched on Name, Message, Criticality, Category and UpdateType(Required) | [default to ]
 **page** | **int**| Specific page number to get. 0 based index | [optional] 
 **page_size** | **int**| Maximum records per page. Default 50 | [optional] 
 **order_by** | **str**| Order By.  Default Asc (Example:Asc,Dsc) | [optional] [default to ]
 **sort_order** | **str**| Sort Order. Default OemupdateName(Example:OemupdateName, OemupdateCategory) | [optional] [default to ]

### Return type

[**OemUpdateSummarySearchResultV1Model**](OemUpdateSummarySearchResultV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

