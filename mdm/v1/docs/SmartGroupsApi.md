# mdmv1.SmartGroupsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smart_groups_create_smart_group_async**](SmartGroupsApi.md#smart_groups_create_smart_group_async) | **POST** /smartgroups | Creates a smart group in Airwatch.
[**smart_groups_delete_async**](SmartGroupsApi.md#smart_groups_delete_async) | **DELETE** /smartgroups/{id} | Deletes the Smart Group identified by the Smart Group Identifier.
[**smart_groups_get_apps_by_smart_group_async**](SmartGroupsApi.md#smart_groups_get_apps_by_smart_group_async) | **GET** /smartgroups/{id}/apps | Gets List of Apps assigned to Smart Group.
[**smart_groups_get_devices**](SmartGroupsApi.md#smart_groups_get_devices) | **GET** /smartgroups/{smartgroupid}/devices | Retrieves the device details in the smart group.
[**smart_groups_load_smart_group_async**](SmartGroupsApi.md#smart_groups_load_smart_group_async) | **GET** /smartgroups/{id} | Retrieves the Smart Group Details.
[**smart_groups_search**](SmartGroupsApi.md#smart_groups_search) | **GET** /smartgroups/search | Searches for smart groups using the query information provided.
[**smart_groups_update_smart_group_async**](SmartGroupsApi.md#smart_groups_update_smart_group_async) | **PUT** /smartgroups/{id} | Updates the details of the specified Smart Group.


# **smart_groups_create_smart_group_async**
> EntityId smart_groups_create_smart_group_async(smart_group_edit_model=smart_group_edit_model)

Creates a smart group in Airwatch.

Create a smart group in Airwatch based on the given details.

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
api_instance = mdmv1.SmartGroupsApi(mdmv1.ApiClient(configuration))
smart_group_edit_model = mdmv1.SmartGroupEditV1Model_() # SmartGroupEditV1Model_ | SmartGroup details. (optional)

try:
    # Creates a smart group in Airwatch.
    api_response = api_instance.smart_groups_create_smart_group_async(smart_group_edit_model=smart_group_edit_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartGroupsApi->smart_groups_create_smart_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_group_edit_model** | [**SmartGroupEditV1Model_**](SmartGroupEditV1Model_.md)| SmartGroup details. | [optional] 

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_groups_delete_async**
> smart_groups_delete_async(id)

Deletes the Smart Group identified by the Smart Group Identifier.

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
api_instance = mdmv1.SmartGroupsApi(mdmv1.ApiClient(configuration))
id = 56 # int | The SmartGroup Identifier (Required).

try:
    # Deletes the Smart Group identified by the Smart Group Identifier.
    api_instance.smart_groups_delete_async(id)
except ApiException as e:
    print("Exception when calling SmartGroupsApi->smart_groups_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SmartGroup Identifier (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_groups_get_apps_by_smart_group_async**
> list[ApplicationModel] smart_groups_get_apps_by_smart_group_async(id)

Gets List of Apps assigned to Smart Group.

Get List of Apps assigned to the Smart Group based on Smart Group Identifier.

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
api_instance = mdmv1.SmartGroupsApi(mdmv1.ApiClient(configuration))
id = 56 # int | Smart Group Id (Required).

try:
    # Gets List of Apps assigned to Smart Group.
    api_response = api_instance.smart_groups_get_apps_by_smart_group_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartGroupsApi->smart_groups_get_apps_by_smart_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Smart Group Id (Required). | 

### Return type

[**list[ApplicationModel]**](ApplicationModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_groups_get_devices**
> SmartGroupDevices smart_groups_get_devices(smartgroupid, seensince=seensince, seentill=seentill)

Retrieves the device details in the smart group.

Retrieves the list of all devices with their respective details (such as DeviceId, Model, OS Version, Platform and Ownership) which belongs to a specific SmartGroup based on Smart Group Identifier.              <br />              **seensince and seentill** fields accept the following              Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,              yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,              yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.SmartGroupsApi(mdmv1.ApiClient(configuration))
smartgroupid = 56 # int | The SmartGroup Identifier.
seensince = '' # str | Filters the devices in the smart group seen after the seensince datetime. (optional) (default to )
seentill = '' # str | Filters the devices in the smart group seen before the seentill datetime. (optional) (default to )

try:
    # Retrieves the device details in the smart group.
    api_response = api_instance.smart_groups_get_devices(smartgroupid, seensince=seensince, seentill=seentill)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartGroupsApi->smart_groups_get_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smartgroupid** | **int**| The SmartGroup Identifier. | 
 **seensince** | **str**| Filters the devices in the smart group seen after the seensince datetime. | [optional] [default to ]
 **seentill** | **str**| Filters the devices in the smart group seen before the seentill datetime. | [optional] [default to ]

### Return type

[**SmartGroupDevices**](SmartGroupDevices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_groups_load_smart_group_async**
> SmartGroup_ smart_groups_load_smart_group_async(id)

Retrieves the Smart Group Details.

Retrieves all the Smart Group details like ( Name, Id, RootLocationGroup, Devices Assigned,list of Users/User Groups etc.) from the Smart Group Identifier.

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
api_instance = mdmv1.SmartGroupsApi(mdmv1.ApiClient(configuration))
id = 56 # int | The SmartGroup Identifier (Required).

try:
    # Retrieves the Smart Group Details.
    api_response = api_instance.smart_groups_load_smart_group_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartGroupsApi->smart_groups_load_smart_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SmartGroup Identifier (Required). | 

### Return type

[**SmartGroup_**](SmartGroup_.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_groups_search**
> SmartGroupSearchResult smart_groups_search(name=name, organizationgroupid=organizationgroupid, managedbyorganizationgroupid=managedbyorganizationgroupid, modifiedfrom=modifiedfrom, modifiedtill=modifiedtill, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)

Searches for smart groups using the query information provided.

Searches for smart groups using the query information (smartgroup name, organizationgroup Id, mdodifedfrom/modifiedtill date, page , pagesize) provided in the request query.              <br />              **modifiedfrom and modifiedtill** fields accept the following              Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,              yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,              yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.SmartGroupsApi(mdmv1.ApiClient(configuration))
name = '' # str | SmartGroup name. (optional) (default to )
organizationgroupid = 56 # int | Organization Group identifier. (optional)
managedbyorganizationgroupid = 56 # int | Smart group managing organization group identifier. (optional)
modifiedfrom = '' # datetime | DateTime, Filters the result where SmartGroup modified date is greater or equal to modifiedfrom value. (optional) (default to )
modifiedtill = '' # datetime | DateTime, Filters the result where SmartGroup modified date is less or equal to modifiedtill value. (optional) (default to )
orderby = '' # str | Order by column name. (optional) (default to )
sortorder = '' # str | Sorting order. Values ASC or DESC. Defaults to ASC. (optional) (default to )
page = 56 # int | Page number. (optional)
pagesize = 56 # int | Records per page. (optional)

try:
    # Searches for smart groups using the query information provided.
    api_response = api_instance.smart_groups_search(name=name, organizationgroupid=organizationgroupid, managedbyorganizationgroupid=managedbyorganizationgroupid, modifiedfrom=modifiedfrom, modifiedtill=modifiedtill, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartGroupsApi->smart_groups_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| SmartGroup name. | [optional] [default to ]
 **organizationgroupid** | **int**| Organization Group identifier. | [optional] 
 **managedbyorganizationgroupid** | **int**| Smart group managing organization group identifier. | [optional] 
 **modifiedfrom** | **datetime**| DateTime, Filters the result where SmartGroup modified date is greater or equal to modifiedfrom value. | [optional] [default to ]
 **modifiedtill** | **datetime**| DateTime, Filters the result where SmartGroup modified date is less or equal to modifiedtill value. | [optional] [default to ]
 **orderby** | **str**| Order by column name. | [optional] [default to ]
 **sortorder** | **str**| Sorting order. Values ASC or DESC. Defaults to ASC. | [optional] [default to ]
 **page** | **int**| Page number. | [optional] 
 **pagesize** | **int**| Records per page. | [optional] 

### Return type

[**SmartGroupSearchResult**](SmartGroupSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_groups_update_smart_group_async**
> smart_groups_update_smart_group_async(id, smart_group_edit_model=smart_group_edit_model)

Updates the details of the specified Smart Group.

Updates the details of the specified Smart Group based on Smart Group Identifier and Smart Group details.

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
api_instance = mdmv1.SmartGroupsApi(mdmv1.ApiClient(configuration))
id = 56 # int | The SmartGroup Identifier.
smart_group_edit_model = mdmv1.SmartGroupEditV1Model_() # SmartGroupEditV1Model_ | The SmartGroup details to be updated. (optional)

try:
    # Updates the details of the specified Smart Group.
    api_instance.smart_groups_update_smart_group_async(id, smart_group_edit_model=smart_group_edit_model)
except ApiException as e:
    print("Exception when calling SmartGroupsApi->smart_groups_update_smart_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SmartGroup Identifier. | 
 **smart_group_edit_model** | [**SmartGroupEditV1Model_**](SmartGroupEditV1Model_.md)| The SmartGroup details to be updated. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

