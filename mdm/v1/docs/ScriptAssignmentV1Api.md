# mdmv1.ScriptAssignmentV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**script_assignment_v1_add_script_assignment_async**](ScriptAssignmentV1Api.md#script_assignment_v1_add_script_assignment_async) | **POST** /scripts/{scriptUuid}/assignments | New - AddScriptAssignmentAsync
[**script_assignment_v1_bulk_update_script_assignments_async**](ScriptAssignmentV1Api.md#script_assignment_v1_bulk_update_script_assignments_async) | **POST** /scripts/{scriptUuid}/updateassignments | New - BulkUpdateScriptAssignmentsAsync
[**script_assignment_v1_delete_script_assignment_async**](ScriptAssignmentV1Api.md#script_assignment_v1_delete_script_assignment_async) | **DELETE** /scripts/{scriptUuid}/assignments/{assignmentUuid} | New - DeleteScriptAssignmentAsync
[**script_assignment_v1_get_script_assignment_async**](ScriptAssignmentV1Api.md#script_assignment_v1_get_script_assignment_async) | **GET** /scriptassignments/{assignmentUuid} | New - GetScriptAssignmentAsync
[**script_assignment_v1_get_script_assignments_async**](ScriptAssignmentV1Api.md#script_assignment_v1_get_script_assignments_async) | **GET** /scripts/{scriptUuid}/assignments | New - GetScriptAssignmentsAsync
[**script_assignment_v1_replace_script_assignment_async**](ScriptAssignmentV1Api.md#script_assignment_v1_replace_script_assignment_async) | **PUT** /scripts/{scriptUuid}/assignments/{assignmentUuid} | New - ReplaceScriptAssignmentAsync
[**script_assignment_v1_update_assignment_rankings_async**](ScriptAssignmentV1Api.md#script_assignment_v1_update_assignment_rankings_async) | **PATCH** /scripts/{scriptUuid}/assignments/updateranking | New - UpdateScriptAssignmentsAsync


# **script_assignment_v1_add_script_assignment_async**
> script_assignment_v1_add_script_assignment_async(script_uuid, create_script_assignment)

New - AddScriptAssignmentAsync

Adds an assignment to script. Assignment information includes assigned smart groups and triggers.

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
api_instance = mdmv1.ScriptAssignmentV1Api(mdmv1.ApiClient(configuration))
script_uuid = 'script_uuid_example' # str | Uuid of the script.(Required)
create_script_assignment = mdmv1.CreateScriptAssignment() # CreateScriptAssignment | Script assignment request model. Includes smart group uuids, triggers and assignment group name.(Required)

try:
    # New - AddScriptAssignmentAsync
    api_instance.script_assignment_v1_add_script_assignment_async(script_uuid, create_script_assignment)
except ApiException as e:
    print("Exception when calling ScriptAssignmentV1Api->script_assignment_v1_add_script_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_uuid** | [**str**](.md)| Uuid of the script.(Required) | 
 **create_script_assignment** | [**CreateScriptAssignment**](CreateScriptAssignment.md)| Script assignment request model. Includes smart group uuids, triggers and assignment group name.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_assignment_v1_bulk_update_script_assignments_async**
> script_assignment_v1_bulk_update_script_assignments_async(script_uuid, bulk_update_script_assignment)

New - BulkUpdateScriptAssignmentsAsync

Updates the list of assignment for the script.

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
api_instance = mdmv1.ScriptAssignmentV1Api(mdmv1.ApiClient(configuration))
script_uuid = 'script_uuid_example' # str | Uuid of the script.(Required)
bulk_update_script_assignment = mdmv1.BulkUpdateScriptAssignment() # BulkUpdateScriptAssignment | Bulk Script assignments request model. List of assignments which include smart group uuids, triggers and assignment group name.(Required)

try:
    # New - BulkUpdateScriptAssignmentsAsync
    api_instance.script_assignment_v1_bulk_update_script_assignments_async(script_uuid, bulk_update_script_assignment)
except ApiException as e:
    print("Exception when calling ScriptAssignmentV1Api->script_assignment_v1_bulk_update_script_assignments_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_uuid** | [**str**](.md)| Uuid of the script.(Required) | 
 **bulk_update_script_assignment** | [**BulkUpdateScriptAssignment**](BulkUpdateScriptAssignment.md)| Bulk Script assignments request model. List of assignments which include smart group uuids, triggers and assignment group name.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_assignment_v1_delete_script_assignment_async**
> script_assignment_v1_delete_script_assignment_async(script_uuid, assignment_uuid)

New - DeleteScriptAssignmentAsync

Deletes a single script assignment.

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
api_instance = mdmv1.ScriptAssignmentV1Api(mdmv1.ApiClient(configuration))
script_uuid = 'script_uuid_example' # str | Uuid of the script.(Required)
assignment_uuid = 'assignment_uuid_example' # str | Uuid of the script assignment.(Required)

try:
    # New - DeleteScriptAssignmentAsync
    api_instance.script_assignment_v1_delete_script_assignment_async(script_uuid, assignment_uuid)
except ApiException as e:
    print("Exception when calling ScriptAssignmentV1Api->script_assignment_v1_delete_script_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_uuid** | [**str**](.md)| Uuid of the script.(Required) | 
 **assignment_uuid** | [**str**](.md)| Uuid of the script assignment.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_assignment_v1_get_script_assignment_async**
> ScriptAssignmentResource script_assignment_v1_get_script_assignment_async(assignment_uuid)

New - GetScriptAssignmentAsync

Get script assignment information which includes assigned smart groups and triggers.

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
api_instance = mdmv1.ScriptAssignmentV1Api(mdmv1.ApiClient(configuration))
assignment_uuid = 'assignment_uuid_example' # str | Uuid of the device assignment.(Required)

try:
    # New - GetScriptAssignmentAsync
    api_response = api_instance.script_assignment_v1_get_script_assignment_async(assignment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptAssignmentV1Api->script_assignment_v1_get_script_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_uuid** | [**str**](.md)| Uuid of the device assignment.(Required) | 

### Return type

[**ScriptAssignmentResource**](ScriptAssignmentResource.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_assignment_v1_get_script_assignments_async**
> SearchResult1 script_assignment_v1_get_script_assignments_async(script_uuid)

New - GetScriptAssignmentsAsync

Get a list of script assignments information which includes assigned smart groups and triggers for each assignment.

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
api_instance = mdmv1.ScriptAssignmentV1Api(mdmv1.ApiClient(configuration))
script_uuid = 'script_uuid_example' # str | Uuid of the script.(Required)

try:
    # New - GetScriptAssignmentsAsync
    api_response = api_instance.script_assignment_v1_get_script_assignments_async(script_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptAssignmentV1Api->script_assignment_v1_get_script_assignments_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_uuid** | [**str**](.md)| Uuid of the script.(Required) | 

### Return type

[**SearchResult1**](SearchResult1.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_assignment_v1_replace_script_assignment_async**
> BaseExceptionModel script_assignment_v1_replace_script_assignment_async(script_uuid, assignment_uuid, update_script_assignment)

New - ReplaceScriptAssignmentAsync

Replace the script assignment information which includes smartgroup ids and triggers.

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
api_instance = mdmv1.ScriptAssignmentV1Api(mdmv1.ApiClient(configuration))
script_uuid = 'script_uuid_example' # str | Uuid of the script.(Required)
assignment_uuid = 'assignment_uuid_example' # str | Uuid of the script assignment.(Required)
update_script_assignment = mdmv1.UpdateScriptAssignment() # UpdateScriptAssignment | Script assignment request model. Includes smart group uuids, triggers and assignment group name.(Required)

try:
    # New - ReplaceScriptAssignmentAsync
    api_response = api_instance.script_assignment_v1_replace_script_assignment_async(script_uuid, assignment_uuid, update_script_assignment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptAssignmentV1Api->script_assignment_v1_replace_script_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_uuid** | [**str**](.md)| Uuid of the script.(Required) | 
 **assignment_uuid** | [**str**](.md)| Uuid of the script assignment.(Required) | 
 **update_script_assignment** | [**UpdateScriptAssignment**](UpdateScriptAssignment.md)| Script assignment request model. Includes smart group uuids, triggers and assignment group name.(Required) | 

### Return type

[**BaseExceptionModel**](BaseExceptionModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_assignment_v1_update_assignment_rankings_async**
> script_assignment_v1_update_assignment_rankings_async(script_uuid, update_rankings)

New - UpdateScriptAssignmentsAsync

Bulk update script assignments priority so that no two scripts assignment have same priority.

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
api_instance = mdmv1.ScriptAssignmentV1Api(mdmv1.ApiClient(configuration))
script_uuid = 'script_uuid_example' # str | Uuid of the script.(Required)
update_rankings = [mdmv1.AssignmentRankingMap()] # list[AssignmentRankingMap] | Contains a list of script assignment rankings.(Required)

try:
    # New - UpdateScriptAssignmentsAsync
    api_instance.script_assignment_v1_update_assignment_rankings_async(script_uuid, update_rankings)
except ApiException as e:
    print("Exception when calling ScriptAssignmentV1Api->script_assignment_v1_update_assignment_rankings_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_uuid** | [**str**](.md)| Uuid of the script.(Required) | 
 **update_rankings** | [**list[AssignmentRankingMap]**](AssignmentRankingMap.md)| Contains a list of script assignment rankings.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

