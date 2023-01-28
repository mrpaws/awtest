# mdmv1.AppsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_v1_get_app_info_for_device**](AppsV1Api.md#apps_v1_get_app_info_for_device) | **GET** /devices/{deviceUuid}/apps | New - Returns details for the specified app installed/assigned to the device.
[**apps_v1_search_apps_for_device**](AppsV1Api.md#apps_v1_search_apps_for_device) | **GET** /devices/{deviceUuid}/apps/search | New - Returns the apps which are applicable to the device.


# **apps_v1_get_app_info_for_device**
> AppV1Model apps_v1_get_app_info_for_device(device_uuid, bundleid)

New - Returns details for the specified app installed/assigned to the device.

This endpoint returns the details of specified app which is assigned or installed on the device.

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
api_instance = mdmv1.AppsV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | The uuid of the device.              Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required)
bundleid = '' # str | The bundle id of the application.              E.g. com.tencent.ig(Required) (default to )

try:
    # New - Returns details for the specified app installed/assigned to the device.
    api_response = api_instance.apps_v1_get_app_info_for_device(device_uuid, bundleid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsV1Api->apps_v1_get_app_info_for_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| The uuid of the device.              Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required) | 
 **bundleid** | **str**| The bundle id of the application.              E.g. com.tencent.ig(Required) | [default to ]

### Return type

[**AppV1Model**](AppV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_v1_search_apps_for_device**
> AppV1PagedSearchResultsModel apps_v1_search_apps_for_device(device_uuid, page=page, pagesize=pagesize, searchtext=searchtext, sortorder=sortorder)

New - Returns the apps which are applicable to the device.

This endpoint returns the details of apps which are assigned or installed on the device matching the search text.  Following special characters are not allowed in query params ('[', ']', '(', ')', '{', '}', '&lt;', '&gt;', '\\\"').

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
api_instance = mdmv1.AppsV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | The uuid of the device.              Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required)
page = 56 # int | Page number which will be fetched, 0 based index. Default 0. (optional)
pagesize = 56 # int | Maximum number of results to be returned in one page. Default 500. (optional)
searchtext = '' # str | If provided, the records matching this text will be returned. The search will be applied on the following properties [name, installed_version, assigned_version]. The default value will be empty string. (optional) (default to )
sortorder = '' # str | Whether the sort order is ascending or descending. The property used for sorting is name. Possible values [Asc, Desc]. Default value is Asc. (optional) (default to )

try:
    # New - Returns the apps which are applicable to the device.
    api_response = api_instance.apps_v1_search_apps_for_device(device_uuid, page=page, pagesize=pagesize, searchtext=searchtext, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsV1Api->apps_v1_search_apps_for_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| The uuid of the device.              Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required) | 
 **page** | **int**| Page number which will be fetched, 0 based index. Default 0. | [optional] 
 **pagesize** | **int**| Maximum number of results to be returned in one page. Default 500. | [optional] 
 **searchtext** | **str**| If provided, the records matching this text will be returned. The search will be applied on the following properties [name, installed_version, assigned_version]. The default value will be empty string. | [optional] [default to ]
 **sortorder** | **str**| Whether the sort order is ascending or descending. The property used for sorting is name. Possible values [Asc, Desc]. Default value is Asc. | [optional] [default to ]

### Return type

[**AppV1PagedSearchResultsModel**](AppV1PagedSearchResultsModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

