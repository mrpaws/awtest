# mdmv1.WorkflowV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_v1_create_assignment_async**](WorkflowV1Api.md#workflow_v1_create_assignment_async) | **POST** /workflows/{workflowUuid}/assignments | New - Create a new assignment corresponding to the workflow.
[**workflow_v1_create_workflow_async**](WorkflowV1Api.md#workflow_v1_create_workflow_async) | **POST** /workflows | New - Create a new workflow.
[**workflow_v1_delete_assignment_async**](WorkflowV1Api.md#workflow_v1_delete_assignment_async) | **DELETE** /workflows/{workflowUuid}/assignments/{assignmentUuid} | New - Deletes an existing workflow assignment at this Organization Group.
[**workflow_v1_delete_workflow_async**](WorkflowV1Api.md#workflow_v1_delete_workflow_async) | **DELETE** /workflows/{workflowUuid} | New - Delete a workflow.
[**workflow_v1_get_all_assignments_async**](WorkflowV1Api.md#workflow_v1_get_all_assignments_async) | **GET** /workflows/{workflowUuid}/assignments | New - Get all assignments corresponding to the workflow identifier.
[**workflow_v1_get_all_devices_for_workflow_async**](WorkflowV1Api.md#workflow_v1_get_all_devices_for_workflow_async) | **GET** /workflows/{workflowUuid}/devices | New - Get all devices for a given workflow.
[**workflow_v1_get_all_workflows_async**](WorkflowV1Api.md#workflow_v1_get_all_workflows_async) | **GET** /workflows | New - Get all workflows at this Organization Group.
[**workflow_v1_get_assignment_by_id_async**](WorkflowV1Api.md#workflow_v1_get_assignment_by_id_async) | **GET** /workflows/{workflowUuid}/assignments/{assignmentUuid} | New - Get the assignment at this Organization Group corresponding to the workflow uuid and assignment uuid.
[**workflow_v1_get_workflow_by_id_async**](WorkflowV1Api.md#workflow_v1_get_workflow_by_id_async) | **GET** /workflows/{workflowUuid} | New - Get the workflow corresponding to the workflow uuid.
[**workflow_v1_preview_publish_device_count_async**](WorkflowV1Api.md#workflow_v1_preview_publish_device_count_async) | **POST** /workflows/previewpublishdevicecount | New - Obtain the expected count of affected devices for a workflow publish.
[**workflow_v1_update_assignment_async**](WorkflowV1Api.md#workflow_v1_update_assignment_async) | **PUT** /workflows/{workflowUuid}/assignments/{assignmentUuid} | New - Updates an existing assignment for this workflow at this Organization Group.
[**workflow_v1_update_assignment_priorities_async**](WorkflowV1Api.md#workflow_v1_update_assignment_priorities_async) | **POST** /workflows/{workflowUuid}/assignments/arrange | New - Arrange assignments in the order or priorities.
[**workflow_v1_update_workflow_async**](WorkflowV1Api.md#workflow_v1_update_workflow_async) | **PUT** /workflows/{workflowUuid} | New - Update a workflow.


# **workflow_v1_create_assignment_async**
> str workflow_v1_create_assignment_async(workflow_uuid, data)

New - Create a new assignment corresponding to the workflow.



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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the Workflow.(Required)
data = mdmv1.AssignmentV1Model() # AssignmentV1Model | The post data(Required)

try:
    # New - Create a new assignment corresponding to the workflow.
    api_response = api_instance.workflow_v1_create_assignment_async(workflow_uuid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_create_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the Workflow.(Required) | 
 **data** | [**AssignmentV1Model**](AssignmentV1Model.md)| The post data(Required) | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_create_workflow_async**
> str workflow_v1_create_workflow_async(data)

New - Create a new workflow.



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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
data = mdmv1.WorkflowV1Model() # WorkflowV1Model | The post data(Required)

try:
    # New - Create a new workflow.
    api_response = api_instance.workflow_v1_create_workflow_async(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_create_workflow_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WorkflowV1Model**](WorkflowV1Model.md)| The post data(Required) | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_delete_assignment_async**
> workflow_v1_delete_assignment_async(workflow_uuid, assignment_uuid)

New - Deletes an existing workflow assignment at this Organization Group.



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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required)
assignment_uuid = 'assignment_uuid_example' # str | Uuid of the assignment.(Required)

try:
    # New - Deletes an existing workflow assignment at this Organization Group.
    api_instance.workflow_v1_delete_assignment_async(workflow_uuid, assignment_uuid)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_delete_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required) | 
 **assignment_uuid** | [**str**](.md)| Uuid of the assignment.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_delete_workflow_async**
> workflow_v1_delete_workflow_async(workflow_uuid)

New - Delete a workflow.



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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required)

try:
    # New - Delete a workflow.
    api_instance.workflow_v1_delete_workflow_async(workflow_uuid)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_delete_workflow_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_get_all_assignments_async**
> AssignmentListResponseV1Model workflow_v1_get_all_assignments_async(workflow_uuid, organization_group_uuid, search=search, orderby=orderby, page=page, page_size=page_size, sortorder=sortorder)

New - Get all assignments corresponding to the workflow identifier.

Used for searching and filtering. Returns a paginated result.

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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the Workflow.(Required)
organization_group_uuid =  # object | Uuid of the Organization Group.(Required) (default to )
search = '' # str | The text to search for in the name of the assignments. (optional) (default to )
orderby = '' # str | Order the results by this attribute (optional) (default to )
page = 56 # int | The specific page number to get (optional)
page_size = 56 # int | Maximum records per page (optional)
sortorder = '' # str | Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified (optional) (default to )

try:
    # New - Get all assignments corresponding to the workflow identifier.
    api_response = api_instance.workflow_v1_get_all_assignments_async(workflow_uuid, organization_group_uuid, search=search, orderby=orderby, page=page, page_size=page_size, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_get_all_assignments_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the Workflow.(Required) | 
 **organization_group_uuid** | [**object**](.md)| Uuid of the Organization Group.(Required) | [default to ]
 **search** | **str**| The text to search for in the name of the assignments. | [optional] [default to ]
 **orderby** | **str**| Order the results by this attribute | [optional] [default to ]
 **page** | **int**| The specific page number to get | [optional] 
 **page_size** | **int**| Maximum records per page | [optional] 
 **sortorder** | **str**| Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified | [optional] [default to ]

### Return type

[**AssignmentListResponseV1Model**](AssignmentListResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_get_all_devices_for_workflow_async**
> DeviceListResponseV1Model workflow_v1_get_all_devices_for_workflow_async(workflow_uuid, organization_group_uuid, search=search, orderby=orderby, page=page, page_size=page_size, sortorder=sortorder)

New - Get all devices for a given workflow.

Used for searching and filtering. Returns a paginated result.

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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required)
organization_group_uuid =  # object | Uuid of the Organization Group.(Required) (default to )
search = '' # str | The text to search for in the name and description for workflows. (optional) (default to )
orderby = '' # str | Order the results by this attribute (optional) (default to )
page = 56 # int | The specific page number to get (optional)
page_size = 56 # int | Maximum records per page (optional)
sortorder = '' # str | Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified (optional) (default to )

try:
    # New - Get all devices for a given workflow.
    api_response = api_instance.workflow_v1_get_all_devices_for_workflow_async(workflow_uuid, organization_group_uuid, search=search, orderby=orderby, page=page, page_size=page_size, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_get_all_devices_for_workflow_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required) | 
 **organization_group_uuid** | [**object**](.md)| Uuid of the Organization Group.(Required) | [default to ]
 **search** | **str**| The text to search for in the name and description for workflows. | [optional] [default to ]
 **orderby** | **str**| Order the results by this attribute | [optional] [default to ]
 **page** | **int**| The specific page number to get | [optional] 
 **page_size** | **int**| Maximum records per page | [optional] 
 **sortorder** | **str**| Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified | [optional] [default to ]

### Return type

[**DeviceListResponseV1Model**](DeviceListResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_get_all_workflows_async**
> WorkflowListResponseV1Model workflow_v1_get_all_workflows_async(organization_group_uuid, search=search, orderby=orderby, page=page, page_size=page_size, sortorder=sortorder)

New - Get all workflows at this Organization Group.

Used for searching and filtering. Returns a paginated result.

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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid =  # object | UUID of the Organization Group.(Required) (default to )
search = '' # str | The text to search for in the name and description for workflows. (optional) (default to )
orderby = '' # str | Order the results by this attribute (optional) (default to )
page = 56 # int | The specific page number to get (optional)
page_size = 56 # int | Maximum records per page (optional)
sortorder = '' # str | Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified (optional) (default to )

try:
    # New - Get all workflows at this Organization Group.
    api_response = api_instance.workflow_v1_get_all_workflows_async(organization_group_uuid, search=search, orderby=orderby, page=page, page_size=page_size, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_get_all_workflows_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**object**](.md)| UUID of the Organization Group.(Required) | [default to ]
 **search** | **str**| The text to search for in the name and description for workflows. | [optional] [default to ]
 **orderby** | **str**| Order the results by this attribute | [optional] [default to ]
 **page** | **int**| The specific page number to get | [optional] 
 **page_size** | **int**| Maximum records per page | [optional] 
 **sortorder** | **str**| Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified | [optional] [default to ]

### Return type

[**WorkflowListResponseV1Model**](WorkflowListResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_get_assignment_by_id_async**
> AssignmentResponseV1Model workflow_v1_get_assignment_by_id_async(workflow_uuid, assignment_uuid)

New - Get the assignment at this Organization Group corresponding to the workflow uuid and assignment uuid.



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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required)
assignment_uuid = 'assignment_uuid_example' # str | Uuid of the Assignment.(Required)

try:
    # New - Get the assignment at this Organization Group corresponding to the workflow uuid and assignment uuid.
    api_response = api_instance.workflow_v1_get_assignment_by_id_async(workflow_uuid, assignment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_get_assignment_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required) | 
 **assignment_uuid** | [**str**](.md)| Uuid of the Assignment.(Required) | 

### Return type

[**AssignmentResponseV1Model**](AssignmentResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_get_workflow_by_id_async**
> WorkflowResponseV1Model workflow_v1_get_workflow_by_id_async(workflow_uuid)

New - Get the workflow corresponding to the workflow uuid.



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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required)

try:
    # New - Get the workflow corresponding to the workflow uuid.
    api_response = api_instance.workflow_v1_get_workflow_by_id_async(workflow_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_get_workflow_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required) | 

### Return type

[**WorkflowResponseV1Model**](WorkflowResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_preview_publish_device_count_async**
> PreviewPublishDeviceCountResponseV1Model workflow_v1_preview_publish_device_count_async(data)

New - Obtain the expected count of affected devices for a workflow publish.

The device count is used to check the applicability of faster DSM delivery for workflows.

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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
data = mdmv1.PreviewPublishDeviceCountV1Model() # PreviewPublishDeviceCountV1Model | The data used to obtain the expected count of affected devices for a workflow publish.(Required)

try:
    # New - Obtain the expected count of affected devices for a workflow publish.
    api_response = api_instance.workflow_v1_preview_publish_device_count_async(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_preview_publish_device_count_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PreviewPublishDeviceCountV1Model**](PreviewPublishDeviceCountV1Model.md)| The data used to obtain the expected count of affected devices for a workflow publish.(Required) | 

### Return type

[**PreviewPublishDeviceCountResponseV1Model**](PreviewPublishDeviceCountResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_update_assignment_async**
> workflow_v1_update_assignment_async(workflow_uuid, assignment_uuid, data)

New - Updates an existing assignment for this workflow at this Organization Group.



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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required)
assignment_uuid = 'assignment_uuid_example' # str | Uuid of the assignment.(Required)
data = mdmv1.AssignmentV1Model() # AssignmentV1Model | The form data(Required)

try:
    # New - Updates an existing assignment for this workflow at this Organization Group.
    api_instance.workflow_v1_update_assignment_async(workflow_uuid, assignment_uuid, data)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_update_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required) | 
 **assignment_uuid** | [**str**](.md)| Uuid of the assignment.(Required) | 
 **data** | [**AssignmentV1Model**](AssignmentV1Model.md)| The form data(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_update_assignment_priorities_async**
> workflow_v1_update_assignment_priorities_async(workflow_uuid, assignment_priorities)

New - Arrange assignments in the order or priorities.

Priority of the assignment should be updated in bulk. No two assignments should have the same priority.

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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required)
assignment_priorities = [mdmv1.WorkflowAssignmentPrioritiesV1Model()] # list[WorkflowAssignmentPrioritiesV1Model] | The list of assignments and their priorities(Required)

try:
    # New - Arrange assignments in the order or priorities.
    api_instance.workflow_v1_update_assignment_priorities_async(workflow_uuid, assignment_priorities)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_update_assignment_priorities_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required) | 
 **assignment_priorities** | [**list[WorkflowAssignmentPrioritiesV1Model]**](WorkflowAssignmentPrioritiesV1Model.md)| The list of assignments and their priorities(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v1_update_workflow_async**
> workflow_v1_update_workflow_async(workflow_uuid, data)

New - Update a workflow.



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
api_instance = mdmv1.WorkflowV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required)
data = mdmv1.WorkflowV1Model() # WorkflowV1Model | The form data(Required)

try:
    # New - Update a workflow.
    api_instance.workflow_v1_update_workflow_async(workflow_uuid, data)
except ApiException as e:
    print("Exception when calling WorkflowV1Api->workflow_v1_update_workflow_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required) | 
 **data** | [**WorkflowV1Model**](WorkflowV1Model.md)| The form data(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

