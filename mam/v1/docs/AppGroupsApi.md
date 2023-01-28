# mamv1.AppGroupsApi

All URIs are relative to *https://awapi.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_groups_add_applications_to_application_group**](AppGroupsApi.md#app_groups_add_applications_to_application_group) | **POST** /apps/appgroups/{appgroupid}/applications | Adds applications to the specified Application Group.
[**app_groups_application_group_search**](AppGroupsApi.md#app_groups_application_group_search) | **GET** /apps/appgroups/search | Searches for the Application Groups based on the query information provided.
[**app_groups_bulk_delete_application_group**](AppGroupsApi.md#app_groups_bulk_delete_application_group) | **DELETE** /apps/appgroups | Deletes Application Groups identified by Application Group Identifiers.
[**app_groups_create_application_group**](AppGroupsApi.md#app_groups_create_application_group) | **POST** /apps/appgroups | Creates an Application Group.
[**app_groups_delete_applications_from_application_group**](AppGroupsApi.md#app_groups_delete_applications_from_application_group) | **DELETE** /apps/appgroups/{appgroupid}/applications | Deletes applications from the specified Application Group.
[**app_groups_get_app_group_details**](AppGroupsApi.md#app_groups_get_app_group_details) | **GET** /apps/appgroups/{appgroupid} | Retrieves the Application group details based on the Application Group id.
[**app_groups_update_application_group**](AppGroupsApi.md#app_groups_update_application_group) | **PUT** /apps/appgroups/{appgroupid} | Updates the specified Application Group.


# **app_groups_add_applications_to_application_group**
> app_groups_add_applications_to_application_group(appgroupid, bulk_input=bulk_input)

Adds applications to the specified Application Group.

Performs the mandatory params check and adds the List of applications supplied to the specified Application Group.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppGroupsApi(mamv1.ApiClient(configuration))
appgroupid = 56 # int | Application Group Identifier. (Minimum value = 1) Example = 2.
bulk_input = mamv1.BulkAppInput() # BulkAppInput | List of Applications to be added to the specified application group. (optional)

try:
    # Adds applications to the specified Application Group.
    api_instance.app_groups_add_applications_to_application_group(appgroupid, bulk_input=bulk_input)
except ApiException as e:
    print("Exception when calling AppGroupsApi->app_groups_add_applications_to_application_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appgroupid** | **int**| Application Group Identifier. (Minimum value &#x3D; 1) Example &#x3D; 2. | 
 **bulk_input** | [**BulkAppInput**](BulkAppInput.md)| List of Applications to be added to the specified application group. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_groups_application_group_search**
> ApplicationGroupSearchResult app_groups_application_group_search(appgroupname=appgroupname, organizationgroupid=organizationgroupid, platform=platform, appgrouptype=appgrouptype, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)

Searches for the Application Groups based on the query information provided.

Takes in query parameters to perform a search on the available Application Groups.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppGroupsApi(mamv1.ApiClient(configuration))
appgroupname = '' # str | App Group name. Example = \"Apple MDM Applications\". (optional) (default to )
organizationgroupid = '' # str | OrganizationGroup Id. Example = \"7\". (optional) (default to )
platform = '' # str | The Application Platform. Example = \"Android\". (optional) (default to )
appgrouptype = '' # str | Application group type [Whitelist, Blacklist, Required, MDMApplication]. (optional) (default to )
orderby = '' # str | Orderby column name. Example = \"ApplicationCount\". (optional) (default to )
sortorder = '' # str | Sorting order. Values ASC or DESC. Defaults to ASC. (optional) (default to )
page = '' # str | Page number.Example = \"2\". (optional) (default to )
pagesize = '' # str | Records per page.Example = \"10\". (optional) (default to )

try:
    # Searches for the Application Groups based on the query information provided.
    api_response = api_instance.app_groups_application_group_search(appgroupname=appgroupname, organizationgroupid=organizationgroupid, platform=platform, appgrouptype=appgrouptype, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppGroupsApi->app_groups_application_group_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appgroupname** | **str**| App Group name. Example &#x3D; \&quot;Apple MDM Applications\&quot;. | [optional] [default to ]
 **organizationgroupid** | **str**| OrganizationGroup Id. Example &#x3D; \&quot;7\&quot;. | [optional] [default to ]
 **platform** | **str**| The Application Platform. Example &#x3D; \&quot;Android\&quot;. | [optional] [default to ]
 **appgrouptype** | **str**| Application group type [Whitelist, Blacklist, Required, MDMApplication]. | [optional] [default to ]
 **orderby** | **str**| Orderby column name. Example &#x3D; \&quot;ApplicationCount\&quot;. | [optional] [default to ]
 **sortorder** | **str**| Sorting order. Values ASC or DESC. Defaults to ASC. | [optional] [default to ]
 **page** | **str**| Page number.Example &#x3D; \&quot;2\&quot;. | [optional] [default to ]
 **pagesize** | **str**| Records per page.Example &#x3D; \&quot;10\&quot;. | [optional] [default to ]

### Return type

[**ApplicationGroupSearchResult**](ApplicationGroupSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_groups_bulk_delete_application_group**
> BulkResponse app_groups_bulk_delete_application_group(bulk_input=bulk_input)

Deletes Application Groups identified by Application Group Identifiers.

Takes in atleast one App Group Id to perform deletion of the corresponding record.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppGroupsApi(mamv1.ApiClient(configuration))
bulk_input = mamv1.BulkInput() # BulkInput | List of Application Group IDs. (optional)

try:
    # Deletes Application Groups identified by Application Group Identifiers.
    api_response = api_instance.app_groups_bulk_delete_application_group(bulk_input=bulk_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppGroupsApi->app_groups_bulk_delete_application_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| List of Application Group IDs. | [optional] 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_groups_create_application_group**
> ApplicationGroup app_groups_create_application_group(application_group=application_group)

Creates an Application Group.

Checks for the mandatory params in the input request body and creates an Application Group.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppGroupsApi(mamv1.ApiClient(configuration))
application_group = mamv1.ApplicationGroup() # ApplicationGroup | The Application Group details. (optional)

try:
    # Creates an Application Group.
    api_response = api_instance.app_groups_create_application_group(application_group=application_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppGroupsApi->app_groups_create_application_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_group** | [**ApplicationGroup**](ApplicationGroup.md)| The Application Group details. | [optional] 

### Return type

[**ApplicationGroup**](ApplicationGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_groups_delete_applications_from_application_group**
> app_groups_delete_applications_from_application_group(appgroupid, bulk_input=bulk_input)

Deletes applications from the specified Application Group.

Takes in a list of application groups, checks for the Application Group Type and performs deletion.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppGroupsApi(mamv1.ApiClient(configuration))
appgroupid = 56 # int | Application Group Identifier. (Minimum value = 1) Example = 2.
bulk_input = mamv1.BulkAppInput() # BulkAppInput | List of Applications to be deleted from the specified application group. (optional)

try:
    # Deletes applications from the specified Application Group.
    api_instance.app_groups_delete_applications_from_application_group(appgroupid, bulk_input=bulk_input)
except ApiException as e:
    print("Exception when calling AppGroupsApi->app_groups_delete_applications_from_application_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appgroupid** | **int**| Application Group Identifier. (Minimum value &#x3D; 1) Example &#x3D; 2. | 
 **bulk_input** | [**BulkAppInput**](BulkAppInput.md)| List of Applications to be deleted from the specified application group. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_groups_get_app_group_details**
> ApplicationGroup app_groups_get_app_group_details(appgroupid)

Retrieves the Application group details based on the Application Group id.

Checks if application group with passed in id exists and if its accessible and returns the application group record.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppGroupsApi(mamv1.ApiClient(configuration))
appgroupid = 56 # int | Application Group Identifier. (Minimum value = 1) Example=2.

try:
    # Retrieves the Application group details based on the Application Group id.
    api_response = api_instance.app_groups_get_app_group_details(appgroupid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppGroupsApi->app_groups_get_app_group_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appgroupid** | **int**| Application Group Identifier. (Minimum value &#x3D; 1) Example&#x3D;2. | 

### Return type

[**ApplicationGroup**](ApplicationGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_groups_update_application_group**
> app_groups_update_application_group(appgroupid, application_group=application_group)

Updates the specified Application Group.

Performs a check for the mandatory params present in the request body and updates the specified Application Group.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppGroupsApi(mamv1.ApiClient(configuration))
appgroupid = 56 # int | The Application Group Id. (Minimum value = 1) Example=2.
application_group = mamv1.ApplicationGroup() # ApplicationGroup | Updated Application Group details. (optional)

try:
    # Updates the specified Application Group.
    api_instance.app_groups_update_application_group(appgroupid, application_group=application_group)
except ApiException as e:
    print("Exception when calling AppGroupsApi->app_groups_update_application_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appgroupid** | **int**| The Application Group Id. (Minimum value &#x3D; 1) Example&#x3D;2. | 
 **application_group** | [**ApplicationGroup**](ApplicationGroup.md)| Updated Application Group details. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

