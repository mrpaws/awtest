# systemv1.OrganizationGroupsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_groups_create_og_async**](OrganizationGroupsApi.md#organization_groups_create_og_async) | **POST** /groups/{id} | New - Creates a new organization group.
[**organization_groups_delete_async**](OrganizationGroupsApi.md#organization_groups_delete_async) | **DELETE** /groups/{id} | Deletes the specified organization group.
[**organization_groups_get_async**](OrganizationGroupsApi.md#organization_groups_get_async) | **GET** /groups/{id} | Retrieves information about the specified organization group.
[**organization_groups_get_child_location_groups**](OrganizationGroupsApi.md#organization_groups_get_child_location_groups) | **GET** /groups/{id}/children | Provides a list of child organization groups of the specified organization group.
[**organization_groups_get_device_count_for_each_location_group_async**](OrganizationGroupsApi.md#organization_groups_get_device_count_for_each_location_group_async) | **GET** /groups/devicecounts | Returns the Device Count for all the Organization Groups that are available under the specified Organization Group.
[**organization_groups_get_sample_rates_async**](OrganizationGroupsApi.md#organization_groups_get_sample_rates_async) | **GET** /groups/{id}/sampleratesbyplatform | Provides the device sample rates for an organization group by platform.
[**organization_groups_get_sample_rates_by_platform_async**](OrganizationGroupsApi.md#organization_groups_get_sample_rates_by_platform_async) | **GET** /groups/{id}/samplerates | New - Provides the device sample rates.
[**organization_groups_location_group_search**](OrganizationGroupsApi.md#organization_groups_location_group_search) | **GET** /groups/search | Searches for organization groups using the query information provided.
[**organization_groups_update_location_group**](OrganizationGroupsApi.md#organization_groups_update_location_group) | **PUT** /groups/{id} | Updates the metadata of the specified organization group.


# **organization_groups_create_og_async**
> EntityIdModel organization_groups_create_og_async(id, location_group=location_group)

New - Creates a new organization group.

Create a new organization group.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.OrganizationGroupsApi(systemv1.ApiClient(configuration))
id = 56 # int | The parent OrganizationGroup Identifier.
location_group = systemv1.LocationGroup_() # LocationGroup_ | The OrganizationGroup resource to be created. (optional)

try:
    # New - Creates a new organization group.
    api_response = api_instance.organization_groups_create_og_async(id, location_group=location_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationGroupsApi->organization_groups_create_og_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The parent OrganizationGroup Identifier. | 
 **location_group** | [**LocationGroup_**](LocationGroup_.md)| The OrganizationGroup resource to be created. | [optional] 

### Return type

[**EntityIdModel**](EntityIdModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_groups_delete_async**
> organization_groups_delete_async(id)

Deletes the specified organization group.

Delete organization group by given ID. It return Forbidden if user want to delete current organization group. It returns bad request,if organization group cannot be deleted.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.OrganizationGroupsApi(systemv1.ApiClient(configuration))
id = 56 # int | The OrganizationGroup Identifier.

try:
    # Deletes the specified organization group.
    api_instance.organization_groups_delete_async(id)
except ApiException as e:
    print("Exception when calling OrganizationGroupsApi->organization_groups_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The OrganizationGroup Identifier. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_groups_get_async**
> LocationGroup_ organization_groups_get_async(id)

Retrieves information about the specified organization group.

Retrieves organization group by ID. If Organization goup is not found, it will throw 404 error.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.OrganizationGroupsApi(systemv1.ApiClient(configuration))
id = 56 # int | The OrganizationGroup Identifier.

try:
    # Retrieves information about the specified organization group.
    api_response = api_instance.organization_groups_get_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationGroupsApi->organization_groups_get_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The OrganizationGroup Identifier. | 

### Return type

[**LocationGroup_**](LocationGroup_.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_groups_get_child_location_groups**
> list[LocationGroup_] organization_groups_get_child_location_groups(id)

Provides a list of child organization groups of the specified organization group.

Lists the Organization Group specified by the ID and all of its child Organization Groups. Users, administrators, and devices in the OG specified by the ID are broken down and listed underneath the Organization Group they are enrolled or created at.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.OrganizationGroupsApi(systemv1.ApiClient(configuration))
id = 56 # int | The parent organization group ID.

try:
    # Provides a list of child organization groups of the specified organization group.
    api_response = api_instance.organization_groups_get_child_location_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationGroupsApi->organization_groups_get_child_location_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The parent organization group ID. | 

### Return type

[**list[LocationGroup_]**](LocationGroup_.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_groups_get_device_count_for_each_location_group_async**
> DeviceCountPerLocationGroupSearchResultModel organization_groups_get_device_count_for_each_location_group_async(organizationgroupid=organizationgroupid, seensince=seensince, seentill=seentill, page=page, pagesize=pagesize)

Returns the Device Count for all the Organization Groups that are available under the specified Organization Group.

Returns the device count for all the organization groups under specified organization group. It return bad request if start date is greater than end date or user has no access to the organization group.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.OrganizationGroupsApi(systemv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization Group to be searched, user's OG is considered if not sent. (optional)
seensince = '' # datetime | Filter devices such that devices with last seen after this date will be returned. Supported format:              \"yyyy/MM/dd\", \"yyyy-MM-dd\", \"MM/dd/yyyy\", \"MM-dd-yyyy\", \"yyyy/MM/dd HH:mm:ss.fff\", \"yyyy-MM-dd HH:mm:ss.fff\", \"MM/dd/yyyy HH:mm:ss.fff\", \"MM-dd-yyyy HH:mm:ss.fff\", \"yyyy/MM/ddTHH:mm:ss.fff\", \"yyyy-MM-ddTHH:mm:ss.fff\", \"MM/dd/yyyyTHH:mm:ss.fff\", \"MM-dd-yyyyTHH:mm:ss.fff\", \"yyyy-MM-dd HH-mm-ss-tt\", \"yyyy-MM-ddTHH-mm-ss-tt\".               (optional) (default to )
seentill = '' # datetime | Filter devices such that devices with last seen till this date will be returned              Supported format:\"yyyy/MM/dd\", \"yyyy-MM-dd\", \"MM/dd/yyyy\", \"MM-dd-yyyy\", \"yyyy/MM/dd HH:mm:ss.fff\", \"yyyy-MM-dd HH:mm:ss.fff\", \"MM/dd/yyyy HH:mm:ss.fff\", \"MM-dd-yyyy HH:mm:ss.fff\", \"yyyy/MM/ddTHH:mm:ss.fff\", \"yyyy-MM-ddTHH:mm:ss.fff\", \"MM/dd/yyyyTHH:mm:ss.fff\", \"MM-dd-yyyyTHH:mm:ss.fff\", \"yyyy-MM-dd HH-mm-ss-tt\", \"yyyy-MM-ddTHH-mm-ss-tt\".               (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Returns the Device Count for all the Organization Groups that are available under the specified Organization Group.
    api_response = api_instance.organization_groups_get_device_count_for_each_location_group_async(organizationgroupid=organizationgroupid, seensince=seensince, seentill=seentill, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationGroupsApi->organization_groups_get_device_count_for_each_location_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization Group to be searched, user&#39;s OG is considered if not sent. | [optional] 
 **seensince** | **datetime**| Filter devices such that devices with last seen after this date will be returned. Supported format:              \&quot;yyyy/MM/dd\&quot;, \&quot;yyyy-MM-dd\&quot;, \&quot;MM/dd/yyyy\&quot;, \&quot;MM-dd-yyyy\&quot;, \&quot;yyyy/MM/dd HH:mm:ss.fff\&quot;, \&quot;yyyy-MM-dd HH:mm:ss.fff\&quot;, \&quot;MM/dd/yyyy HH:mm:ss.fff\&quot;, \&quot;MM-dd-yyyy HH:mm:ss.fff\&quot;, \&quot;yyyy/MM/ddTHH:mm:ss.fff\&quot;, \&quot;yyyy-MM-ddTHH:mm:ss.fff\&quot;, \&quot;MM/dd/yyyyTHH:mm:ss.fff\&quot;, \&quot;MM-dd-yyyyTHH:mm:ss.fff\&quot;, \&quot;yyyy-MM-dd HH-mm-ss-tt\&quot;, \&quot;yyyy-MM-ddTHH-mm-ss-tt\&quot;.               | [optional] [default to ]
 **seentill** | **datetime**| Filter devices such that devices with last seen till this date will be returned              Supported format:\&quot;yyyy/MM/dd\&quot;, \&quot;yyyy-MM-dd\&quot;, \&quot;MM/dd/yyyy\&quot;, \&quot;MM-dd-yyyy\&quot;, \&quot;yyyy/MM/dd HH:mm:ss.fff\&quot;, \&quot;yyyy-MM-dd HH:mm:ss.fff\&quot;, \&quot;MM/dd/yyyy HH:mm:ss.fff\&quot;, \&quot;MM-dd-yyyy HH:mm:ss.fff\&quot;, \&quot;yyyy/MM/ddTHH:mm:ss.fff\&quot;, \&quot;yyyy-MM-ddTHH:mm:ss.fff\&quot;, \&quot;MM/dd/yyyyTHH:mm:ss.fff\&quot;, \&quot;MM-dd-yyyyTHH:mm:ss.fff\&quot;, \&quot;yyyy-MM-dd HH-mm-ss-tt\&quot;, \&quot;yyyy-MM-ddTHH-mm-ss-tt\&quot;.               | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**DeviceCountPerLocationGroupSearchResultModel**](DeviceCountPerLocationGroupSearchResultModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_groups_get_sample_rates_async**
> DeviceSampleRates organization_groups_get_sample_rates_async(id, platform=platform)

Provides the device sample rates for an organization group by platform.

Return the device sample rates for organization group by Platform such as iOS, Android etc.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.OrganizationGroupsApi(systemv1.ApiClient(configuration))
id = 56 # int | The Organization group ID.
platform = '' # str | Platform name. (optional) (default to )

try:
    # Provides the device sample rates for an organization group by platform.
    api_response = api_instance.organization_groups_get_sample_rates_async(id, platform=platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationGroupsApi->organization_groups_get_sample_rates_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Organization group ID. | 
 **platform** | **str**| Platform name. | [optional] [default to ]

### Return type

[**DeviceSampleRates**](DeviceSampleRates.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_groups_get_sample_rates_by_platform_async**
> DeviceSampleRates organization_groups_get_sample_rates_by_platform_async(id, platform)

New - Provides the device sample rates.

Provides the device sample rates for an organization group by platform.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.OrganizationGroupsApi(systemv1.ApiClient(configuration))
id = 56 # int | Organization Group Id.(Required).
platform =  # object | The platform of device for which sample rates are requested.(Required) (default to )

try:
    # New - Provides the device sample rates.
    api_response = api_instance.organization_groups_get_sample_rates_by_platform_async(id, platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationGroupsApi->organization_groups_get_sample_rates_by_platform_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Organization Group Id.(Required). | 
 **platform** | [**object**](.md)| The platform of device for which sample rates are requested.(Required) | [default to ]

### Return type

[**DeviceSampleRates**](DeviceSampleRates.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_groups_location_group_search**
> LocationGroupSearchResult organization_groups_location_group_search(name=name, type=type, groupid=groupid, orderby=orderby, page=page, pagesize=pagesize, sortorder=sortorder)

Searches for organization groups using the query information provided.

Search organization group by given parameter.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.OrganizationGroupsApi(systemv1.ApiClient(configuration))
name = '' # str | The OrganizationGroup name, such as \"Global\". (optional) (default to )
type = '' # str | The OrganizationGroup type. (eg. \"Container\",\"Customer\",\"Partner\"). (optional) (default to )
groupid = '' # str | The organization group identifier[Activation code] to search for.[Exact match is performed for this attribute]. (optional) (default to )
orderby = '' # str | Orders the results based on this attribute-value[Valid values are: Id/Name/GroupId/LocationGroupType]. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)
sortorder = '' # str | Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. (optional) (default to )

try:
    # Searches for organization groups using the query information provided.
    api_response = api_instance.organization_groups_location_group_search(name=name, type=type, groupid=groupid, orderby=orderby, page=page, pagesize=pagesize, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationGroupsApi->organization_groups_location_group_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The OrganizationGroup name, such as \&quot;Global\&quot;. | [optional] [default to ]
 **type** | **str**| The OrganizationGroup type. (eg. \&quot;Container\&quot;,\&quot;Customer\&quot;,\&quot;Partner\&quot;). | [optional] [default to ]
 **groupid** | **str**| The organization group identifier[Activation code] to search for.[Exact match is performed for this attribute]. | [optional] [default to ]
 **orderby** | **str**| Orders the results based on this attribute-value[Valid values are: Id/Name/GroupId/LocationGroupType]. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 
 **sortorder** | **str**| Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. | [optional] [default to ]

### Return type

[**LocationGroupSearchResult**](LocationGroupSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_groups_update_location_group**
> organization_groups_update_location_group(id, location_group=location_group)

Updates the metadata of the specified organization group.

update the metadata of organization group specified by ID. It return bad request if organization group name too long or group id too long.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.OrganizationGroupsApi(systemv1.ApiClient(configuration))
id = 56 # int | The Organization Group Identifier.
location_group = systemv1.LocationGroup_() # LocationGroup_ | An organization group resource containing the updated values. (optional)

try:
    # Updates the metadata of the specified organization group.
    api_instance.organization_groups_update_location_group(id, location_group=location_group)
except ApiException as e:
    print("Exception when calling OrganizationGroupsApi->organization_groups_update_location_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Organization Group Identifier. | 
 **location_group** | [**LocationGroup_**](LocationGroup_.md)| An organization group resource containing the updated values. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

