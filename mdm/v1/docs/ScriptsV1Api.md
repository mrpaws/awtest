# mdmv1.ScriptsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scripts_v1_create_script_async**](ScriptsV1Api.md#scripts_v1_create_script_async) | **POST** /groups/{organizationGroupUuid}/scripts | New - CreateScriptAsync
[**scripts_v1_get_script_async**](ScriptsV1Api.md#scripts_v1_get_script_async) | **GET** /scripts/{scriptUuid} | New - GetScriptAsync
[**scripts_v1_get_script_configuration_async**](ScriptsV1Api.md#scripts_v1_get_script_configuration_async) | **GET** /{deviceUuid}/scripts/{scriptUuid}/config/{configBundleUuid} | New - GetScriptConfigurationAsync
[**scripts_v1_get_script_definition_async_async**](ScriptsV1Api.md#scripts_v1_get_script_definition_async_async) | **GET** /{deviceUuid}/scripts/{scriptUuid}/definition | New - GetScriptDefinitionAsync
[**scripts_v1_get_script_samples_async**](ScriptsV1Api.md#scripts_v1_get_script_samples_async) | **POST** /groups/{organizationGroupUuid}/scripts/samples | New - Get script samples.
[**scripts_v1_get_scripts_by_device_async**](ScriptsV1Api.md#scripts_v1_get_scripts_by_device_async) | **GET** /devices/{deviceUuid}/scripts | New - GetScriptsByDeviceAsync
[**scripts_v1_get_scripts_by_organization_group_async**](ScriptsV1Api.md#scripts_v1_get_scripts_by_organization_group_async) | **GET** /groups/{organizationGroupUuid}/scripts | New - GetScriptsByOrganizationGroupAsync
[**scripts_v1_replace_script_definition_async**](ScriptsV1Api.md#scripts_v1_replace_script_definition_async) | **PUT** /scripts/{scriptUuid} | New - ReplaceScriptDefinitionAsync
[**scripts_v1_script_bulk_delete_async**](ScriptsV1Api.md#scripts_v1_script_bulk_delete_async) | **POST** /groups/{organizationGroupUuid}/scripts/bulkdelete | New - ScriptBulkDelete


# **scripts_v1_create_script_async**
> scripts_v1_create_script_async(organization_group_uuid, body)

New - CreateScriptAsync

Create a script which includes script name, description, platform, script type, execution context, timeout, script data, script environment variables.

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
api_instance = mdmv1.ScriptsV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Unique identifier for the organization group(Required)
body = mdmv1.CreateScript() # CreateScript | Script request model. Includes script name, description, platform, script type, execution context, timeout, script data, script environment variables.(Required)

try:
    # New - CreateScriptAsync
    api_instance.scripts_v1_create_script_async(organization_group_uuid, body)
except ApiException as e:
    print("Exception when calling ScriptsV1Api->scripts_v1_create_script_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Unique identifier for the organization group(Required) | 
 **body** | [**CreateScript**](CreateScript.md)| Script request model. Includes script name, description, platform, script type, execution context, timeout, script data, script environment variables.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripts_v1_get_script_async**
> ScriptResource scripts_v1_get_script_async(script_uuid)

New - GetScriptAsync

Get a script which includes script name, description, display name, action type, category, organization group identifier, platform, script type, execution context, timeout, script data, script environment variables.

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
api_instance = mdmv1.ScriptsV1Api(mdmv1.ApiClient(configuration))
script_uuid = 'script_uuid_example' # str | Uuid of the script.(Required)

try:
    # New - GetScriptAsync
    api_response = api_instance.scripts_v1_get_script_async(script_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsV1Api->scripts_v1_get_script_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_uuid** | [**str**](.md)| Uuid of the script.(Required) | 

### Return type

[**ScriptResource**](ScriptResource.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripts_v1_get_script_configuration_async**
> scripts_v1_get_script_configuration_async(device_uuid, script_uuid, config_bundle_uuid)

New - GetScriptConfigurationAsync

An API to get configuration information for entitled script resource for the device. Configuration inludes the Trigger type, triggers events, trigger period along with looked up script variables)

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
api_instance = mdmv1.ScriptsV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | deviceUuid.
script_uuid = 'script_uuid_example' # str | uuid of the script.(Required)
config_bundle_uuid = 'config_bundle_uuid_example' # str | uuid of the configuration bundle.(Required)

try:
    # New - GetScriptConfigurationAsync
    api_instance.scripts_v1_get_script_configuration_async(device_uuid, script_uuid, config_bundle_uuid)
except ApiException as e:
    print("Exception when calling ScriptsV1Api->scripts_v1_get_script_configuration_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| deviceUuid. | 
 **script_uuid** | [**str**](.md)| uuid of the script.(Required) | 
 **config_bundle_uuid** | [**str**](.md)| uuid of the configuration bundle.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripts_v1_get_script_definition_async_async**
> ScriptDefinitionsResource scripts_v1_get_script_definition_async_async(device_uuid, script_uuid)

New - GetScriptDefinitionAsync

Device gateway API to get the Script definitions by device and script uuid

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
api_instance = mdmv1.ScriptsV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | deviceUuid.
script_uuid = 'script_uuid_example' # str | uuid of the script.(Required)

try:
    # New - GetScriptDefinitionAsync
    api_response = api_instance.scripts_v1_get_script_definition_async_async(device_uuid, script_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsV1Api->scripts_v1_get_script_definition_async_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| deviceUuid. | 
 **script_uuid** | [**str**](.md)| uuid of the script.(Required) | 

### Return type

[**ScriptDefinitionsResource**](ScriptDefinitionsResource.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripts_v1_get_script_samples_async**
> ScriptSampleSearchResponseModel scripts_v1_get_script_samples_async(organization_group_uuid, body)

New - Get script samples.

Get script samples which includes script execution details.

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
api_instance = mdmv1.ScriptsV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Unique identifier for the organization group(Required)
body = mdmv1.ScriptSampleSearchRequestModel() # ScriptSampleSearchRequestModel | Script request model. Includes script name, description, platform, script type, execution context, timeout, script data, script environment variables.(Required)

try:
    # New - Get script samples.
    api_response = api_instance.scripts_v1_get_script_samples_async(organization_group_uuid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsV1Api->scripts_v1_get_script_samples_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Unique identifier for the organization group(Required) | 
 **body** | [**ScriptSampleSearchRequestModel**](ScriptSampleSearchRequestModel.md)| Script request model. Includes script name, description, platform, script type, execution context, timeout, script data, script environment variables.(Required) | 

### Return type

[**ScriptSampleSearchResponseModel**](ScriptSampleSearchResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripts_v1_get_scripts_by_device_async**
> SearchResult11 scripts_v1_get_scripts_by_device_async(device_uuid, name=name, script_type=script_type, platform=platform, category=category, page=page, page_size=page_size, orderby=orderby, sort_order=sort_order)

New - GetScriptsByDeviceAsync

Get the list of scripts which is available on the device.

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
api_instance = mdmv1.ScriptsV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Unique identifier for the device.(Required)
name = '' # str | Filter records based on the script name. Partial names are accepted. (optional) (default to )
script_type =  # object | Filter records based on the script type. Accepted values are [POWERSHELL] when platform is [WIN_RT], [BASH] and [PYTHON] when platform is [APPLE_OSX]. (optional) (default to )
platform =  # object | Filter records based on the platform. Default is None. Accepted values are [WIN_RT] and [APPLE_OSX]. (optional) (default to )
category = '' # str | Filter records based on the script category.Default is None. Accept values like [IT-UTILITIES] and etc. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. Default is 0 (optional)
page_size = 56 # int | Maximum records per page. Default 500 (optional)
orderby =  # object | Name of the property used for sorting. Accepted values are [Name], [Platform], [ScriptType], [Category] and [ActionType] (optional) (default to )
sort_order =  # object | Whether the sort order is ascending or descending for specified orderby. The default property used for sorting is name. Accepted values are [Asc] and [Desc]. Default value is Asc. (optional) (default to )

try:
    # New - GetScriptsByDeviceAsync
    api_response = api_instance.scripts_v1_get_scripts_by_device_async(device_uuid, name=name, script_type=script_type, platform=platform, category=category, page=page, page_size=page_size, orderby=orderby, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsV1Api->scripts_v1_get_scripts_by_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Unique identifier for the device.(Required) | 
 **name** | **str**| Filter records based on the script name. Partial names are accepted. | [optional] [default to ]
 **script_type** | [**object**](.md)| Filter records based on the script type. Accepted values are [POWERSHELL] when platform is [WIN_RT], [BASH] and [PYTHON] when platform is [APPLE_OSX]. | [optional] [default to ]
 **platform** | [**object**](.md)| Filter records based on the platform. Default is None. Accepted values are [WIN_RT] and [APPLE_OSX]. | [optional] [default to ]
 **category** | **str**| Filter records based on the script category.Default is None. Accept values like [IT-UTILITIES] and etc. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. Default is 0 | [optional] 
 **page_size** | **int**| Maximum records per page. Default 500 | [optional] 
 **orderby** | [**object**](.md)| Name of the property used for sorting. Accepted values are [Name], [Platform], [ScriptType], [Category] and [ActionType] | [optional] [default to ]
 **sort_order** | [**object**](.md)| Whether the sort order is ascending or descending for specified orderby. The default property used for sorting is name. Accepted values are [Asc] and [Desc]. Default value is Asc. | [optional] [default to ]

### Return type

[**SearchResult11**](SearchResult11.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripts_v1_get_scripts_by_organization_group_async**
> SearchResult11 scripts_v1_get_scripts_by_organization_group_async(organization_group_uuid, expand, name=name, script_type=script_type, platform=platform, category=category, page=page, page_size=page_size, orderby=orderby, sort_order=sort_order)

New - GetScriptsByOrganizationGroupAsync

Returns a list of script(s) with scripts details for the organization group.

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
api_instance = mdmv1.ScriptsV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Unique identifier for the organization group(Required)
expand =  # bool | Flag to specify to get metadata or complete definition of a script(Required) (default to )
name = '' # str | Filter records based on the script name. Partial names are accepted. (optional) (default to )
script_type =  # object | Filter records based on the script type. Accepted values are [POWERSHELL] when platform is [WIN_RT], [BASH] and [PYTHON] when platform is [APPLE_OSX]. (optional) (default to )
platform =  # object | Filter records based on the platform. Default is None. Accepted values are [WIN_RT] and [APPLE_OSX]. (optional) (default to )
category = '' # str | Filter records based on the script category.Default is None. Accept values like [IT-UTILITIES] and etc. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. Default is 0 (optional)
page_size = 56 # int | Maximum records per page. Default 500 (optional)
orderby =  # object | Name of the property used for sorting. Accepted values are [Name], [Platform], [ScriptType], [Category] and [ActionType] (optional) (default to )
sort_order =  # object | Whether the sort order is ascending or descending for specified orderby. The default property used for sorting is name. Accepted values are [Asc] and [Desc]. Default value is Asc. (optional) (default to )

try:
    # New - GetScriptsByOrganizationGroupAsync
    api_response = api_instance.scripts_v1_get_scripts_by_organization_group_async(organization_group_uuid, expand, name=name, script_type=script_type, platform=platform, category=category, page=page, page_size=page_size, orderby=orderby, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsV1Api->scripts_v1_get_scripts_by_organization_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Unique identifier for the organization group(Required) | 
 **expand** | **bool**| Flag to specify to get metadata or complete definition of a script(Required) | [default to ]
 **name** | **str**| Filter records based on the script name. Partial names are accepted. | [optional] [default to ]
 **script_type** | [**object**](.md)| Filter records based on the script type. Accepted values are [POWERSHELL] when platform is [WIN_RT], [BASH] and [PYTHON] when platform is [APPLE_OSX]. | [optional] [default to ]
 **platform** | [**object**](.md)| Filter records based on the platform. Default is None. Accepted values are [WIN_RT] and [APPLE_OSX]. | [optional] [default to ]
 **category** | **str**| Filter records based on the script category.Default is None. Accept values like [IT-UTILITIES] and etc. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. Default is 0 | [optional] 
 **page_size** | **int**| Maximum records per page. Default 500 | [optional] 
 **orderby** | [**object**](.md)| Name of the property used for sorting. Accepted values are [Name], [Platform], [ScriptType], [Category] and [ActionType] | [optional] [default to ]
 **sort_order** | [**object**](.md)| Whether the sort order is ascending or descending for specified orderby. The default property used for sorting is name. Accepted values are [Asc] and [Desc]. Default value is Asc. | [optional] [default to ]

### Return type

[**SearchResult11**](SearchResult11.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripts_v1_replace_script_definition_async**
> scripts_v1_replace_script_definition_async(script_uuid, body)

New - ReplaceScriptDefinitionAsync

Replace the script definition which includes description, display name, action type, category, execution context, timeout, script data, script environment variables.

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
api_instance = mdmv1.ScriptsV1Api(mdmv1.ApiClient(configuration))
script_uuid = 'script_uuid_example' # str | Uuid of the script.(Required)
body = mdmv1.UpdateScript() # UpdateScript | Script update model. Includes script description, display name, action type, category, execution context, timeout, script data, script environment variables.(Required)

try:
    # New - ReplaceScriptDefinitionAsync
    api_instance.scripts_v1_replace_script_definition_async(script_uuid, body)
except ApiException as e:
    print("Exception when calling ScriptsV1Api->scripts_v1_replace_script_definition_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_uuid** | [**str**](.md)| Uuid of the script.(Required) | 
 **body** | [**UpdateScript**](UpdateScript.md)| Script update model. Includes script description, display name, action type, category, execution context, timeout, script data, script environment variables.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripts_v1_script_bulk_delete_async**
> scripts_v1_script_bulk_delete_async(organization_group_uuid, script_uuid_list)

New - ScriptBulkDelete

This API is used to delete the list of script attribute and attribute details along with the associated assignments.

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
api_instance = mdmv1.ScriptsV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Unique identifier for the organization group(Required)
script_uuid_list = [mdmv1.list[str]()] # list[str] | (Required)

try:
    # New - ScriptBulkDelete
    api_instance.scripts_v1_script_bulk_delete_async(organization_group_uuid, script_uuid_list)
except ApiException as e:
    print("Exception when calling ScriptsV1Api->scripts_v1_script_bulk_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Unique identifier for the organization group(Required) | 
 **script_uuid_list** | **list[str]**| (Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

