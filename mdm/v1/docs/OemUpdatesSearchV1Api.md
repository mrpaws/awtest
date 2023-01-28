# mdmv1.OemUpdatesSearchV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oem_updates_search_v1_get_oem_updates_by_device_uuid_async**](OemUpdatesSearchV1Api.md#oem_updates_search_v1_get_oem_updates_by_device_uuid_async) | **GET** /oem-updates/v1/groups/{uuid}/device/{deviceUuid}/updates-list | New - Getting OEM updates for a device.
[**oem_updates_search_v1_get_summary_devices_async**](OemUpdatesSearchV1Api.md#oem_updates_search_v1_get_summary_devices_async) | **GET** /oem-updates/v1/groups/{uuid}/summary/devices | New - Gets the devices where OEM Update Summary is installed(status would be either failed or success).
[**oem_updates_search_v1_get_summary_status_async**](OemUpdatesSearchV1Api.md#oem_updates_search_v1_get_summary_status_async) | **GET** /oem-updates/v1/groups/{uuid}/summary/status | New - Gets the count of OemUpdate Summary installed in devices for a given release_id + version.
[**oem_updates_search_v1_search_async**](OemUpdatesSearchV1Api.md#oem_updates_search_v1_search_async) | **GET** /oem-updates/v1/groups/{uuid}/summary | New - Returns a collection of OemUpdateSummary details based on the search criteria.


# **oem_updates_search_v1_get_oem_updates_by_device_uuid_async**
> OemUpdateDeviceSearchResultInfoV1Model oem_updates_search_v1_get_oem_updates_by_device_uuid_async(uuid, device_uuid, search_text=search_text, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_column=sort_column, status=status)

New - Getting OEM updates for a device.

Getting OEM updates for a device of a given device Uuid.

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
api_instance = mdmv1.OemUpdatesSearchV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization group UUID to perform the operation on.(Required).
device_uuid = 'device_uuid_example' # str | Device UUID to perform the operation on.(Required).
search_text = '' # str | OemUpdate is searched on Name, Message, Criticality, Category and UpdateType (optional) (default to )
page_number = 56 # int | Specific page number to get. 0 based index. (optional)
page_size = 56 # int | Maximum number of records per page. Default value is 50. (optional)
sort_order = '' # str | The order based on which we can sort, supported values are ASC, DESC. Default value is ASC. (optional) (default to )
sort_column = '' # str | Column based on which we can provide the sorting. (optional) (default to )
status =  # bool | The installed status of the OEM update. Supported values true, and false. (optional) (default to )

try:
    # New - Getting OEM updates for a device.
    api_response = api_instance.oem_updates_search_v1_get_oem_updates_by_device_uuid_async(uuid, device_uuid, search_text=search_text, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_column=sort_column, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OemUpdatesSearchV1Api->oem_updates_search_v1_get_oem_updates_by_device_uuid_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required). | 
 **device_uuid** | [**str**](.md)| Device UUID to perform the operation on.(Required). | 
 **search_text** | **str**| OemUpdate is searched on Name, Message, Criticality, Category and UpdateType | [optional] [default to ]
 **page_number** | **int**| Specific page number to get. 0 based index. | [optional] 
 **page_size** | **int**| Maximum number of records per page. Default value is 50. | [optional] 
 **sort_order** | **str**| The order based on which we can sort, supported values are ASC, DESC. Default value is ASC. | [optional] [default to ]
 **sort_column** | **str**| Column based on which we can provide the sorting. | [optional] [default to ]
 **status** | **bool**| The installed status of the OEM update. Supported values true, and false. | [optional] [default to ]

### Return type

[**OemUpdateDeviceSearchResultInfoV1Model**](OemUpdateDeviceSearchResultInfoV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oem_updates_search_v1_get_summary_devices_async**
> list[OemUpdateSummaryInstalledDeviceInfoResponseV1Model] oem_updates_search_v1_get_summary_devices_async(uuid, release_id, version, status, search_text=search_text, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_column=sort_column)

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
api_instance = mdmv1.OemUpdatesSearchV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization group UUID to perform the operation on.(Required).
release_id = '' # str | Release identifier of the OEM update.(Required) (default to )
version = '' # str | Version of the OEM update.(Required) (default to )
status =  # bool | The installed status of the OEM update.(Required). Supported values true, and false. (default to )
search_text = '' # str | OemUpdate is searched on Name, Message, Criticality, Category and UpdateType (optional) (default to )
page_number = 56 # int | Specific page number to get. 0 based index. (optional)
page_size = 56 # int | Maximum number of records per page. Default value is 50. (optional)
sort_order = '' # str | The order based on which we can sort, supported values are ASC, DESC. Default value is ASC. (optional) (default to )
sort_column = '' # str | Column based on which we can provide the sorting. Default OemupdateName(Example:OemupdateName, OemupdateCategory) (optional) (default to )

try:
    # New - Gets the devices where OEM Update Summary is installed(status would be either failed or success).
    api_response = api_instance.oem_updates_search_v1_get_summary_devices_async(uuid, release_id, version, status, search_text=search_text, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_column=sort_column)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OemUpdatesSearchV1Api->oem_updates_search_v1_get_summary_devices_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required). | 
 **release_id** | **str**| Release identifier of the OEM update.(Required) | [default to ]
 **version** | **str**| Version of the OEM update.(Required) | [default to ]
 **status** | **bool**| The installed status of the OEM update.(Required). Supported values true, and false. | [default to ]
 **search_text** | **str**| OemUpdate is searched on Name, Message, Criticality, Category and UpdateType | [optional] [default to ]
 **page_number** | **int**| Specific page number to get. 0 based index. | [optional] 
 **page_size** | **int**| Maximum number of records per page. Default value is 50. | [optional] 
 **sort_order** | **str**| The order based on which we can sort, supported values are ASC, DESC. Default value is ASC. | [optional] [default to ]
 **sort_column** | **str**| Column based on which we can provide the sorting. Default OemupdateName(Example:OemupdateName, OemupdateCategory) | [optional] [default to ]

### Return type

[**list[OemUpdateSummaryInstalledDeviceInfoResponseV1Model]**](OemUpdateSummaryInstalledDeviceInfoResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oem_updates_search_v1_get_summary_status_async**
> list[OemUpdateSummaryInstalledStatusInfoResponseV1Model] oem_updates_search_v1_get_summary_status_async(uuid, release_id, version)

New - Gets the count of OemUpdate Summary installed in devices for a given release_id + version.

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
api_instance = mdmv1.OemUpdatesSearchV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization group UUID to perform the operation on.(Required).
release_id = '' # str | Release identifier of the OEM update.(Required) (default to )
version = '' # str | Version of the OEM update.(Required) (default to )

try:
    # New - Gets the count of OemUpdate Summary installed in devices for a given release_id + version.
    api_response = api_instance.oem_updates_search_v1_get_summary_status_async(uuid, release_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OemUpdatesSearchV1Api->oem_updates_search_v1_get_summary_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required). | 
 **release_id** | **str**| Release identifier of the OEM update.(Required) | [default to ]
 **version** | **str**| Version of the OEM update.(Required) | [default to ]

### Return type

[**list[OemUpdateSummaryInstalledStatusInfoResponseV1Model]**](OemUpdateSummaryInstalledStatusInfoResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oem_updates_search_v1_search_async**
> OemUpdateSummarySearchResultInfoV1Model oem_updates_search_v1_search_async(uuid, search_text=search_text, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_column=sort_column)

New - Returns a collection of OemUpdateSummary details based on the search criteria.

Returns a collection of OemUpdate summary details based on the search criteria specified.

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
api_instance = mdmv1.OemUpdatesSearchV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization group UUID to perform the operation on.(Required).
search_text = '' # str | OemUpdate is searched on Name, Message, Criticality, Category and UpdateType (optional) (default to )
page_number = 56 # int | Specific page number to get. 0 based index. (optional)
page_size = 56 # int | Maximum number of records per page. Default value is 50. (optional)
sort_order = '' # str | The order based on which we can sort, supported values are ASC, DESC. Default value is ASC. (optional) (default to )
sort_column = '' # str | Column based on which we can provide the sorting. Default OemupdateName(Example:OemupdateName, OemupdateCategory) (optional) (default to )

try:
    # New - Returns a collection of OemUpdateSummary details based on the search criteria.
    api_response = api_instance.oem_updates_search_v1_search_async(uuid, search_text=search_text, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_column=sort_column)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OemUpdatesSearchV1Api->oem_updates_search_v1_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required). | 
 **search_text** | **str**| OemUpdate is searched on Name, Message, Criticality, Category and UpdateType | [optional] [default to ]
 **page_number** | **int**| Specific page number to get. 0 based index. | [optional] 
 **page_size** | **int**| Maximum number of records per page. Default value is 50. | [optional] 
 **sort_order** | **str**| The order based on which we can sort, supported values are ASC, DESC. Default value is ASC. | [optional] [default to ]
 **sort_column** | **str**| Column based on which we can provide the sorting. Default OemupdateName(Example:OemupdateName, OemupdateCategory) | [optional] [default to ]

### Return type

[**OemUpdateSummarySearchResultInfoV1Model**](OemUpdateSummarySearchResultInfoV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

