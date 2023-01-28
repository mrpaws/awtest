# mdmv2.WorkflowV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_v2_create_workflow_async**](WorkflowV2Api.md#workflow_v2_create_workflow_async) | **POST** /workflows | New - Create a new workflow.
[**workflow_v2_get_all_workflows_async**](WorkflowV2Api.md#workflow_v2_get_all_workflows_async) | **GET** /workflows | New - Get all workflows at this Organization Group.
[**workflow_v2_get_workflow_by_id_async**](WorkflowV2Api.md#workflow_v2_get_workflow_by_id_async) | **GET** /workflows/{workflowUuid} | New - Get the workflow corresponding to the workflow uuid.
[**workflow_v2_update_workflow_async**](WorkflowV2Api.md#workflow_v2_update_workflow_async) | **PUT** /workflows/{workflowUuid} | New - Update a workflow.


# **workflow_v2_create_workflow_async**
> str workflow_v2_create_workflow_async(data)

New - Create a new workflow.



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
api_instance = mdmv2.WorkflowV2Api(mdmv2.ApiClient(configuration))
data = mdmv2.WorkflowV2Model() # WorkflowV2Model | The post data(Required)

try:
    # New - Create a new workflow.
    api_response = api_instance.workflow_v2_create_workflow_async(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowV2Api->workflow_v2_create_workflow_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WorkflowV2Model**](WorkflowV2Model.md)| The post data(Required) | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v2_get_all_workflows_async**
> WorkflowListResponseV2Model workflow_v2_get_all_workflows_async(organization_group_uuid, search=search, orderby=orderby, page=page, page_size=page_size, sortorder=sortorder, implicitworkflow=implicitworkflow, device_type=device_type, assignment_state=assignment_state, type=type)

New - Get all workflows at this Organization Group.

Used for searching and filtering. Returns a paginated result.

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
api_instance = mdmv2.WorkflowV2Api(mdmv2.ApiClient(configuration))
organization_group_uuid =  # object | Uuid of the Organization group or csv of uuids of organization groups.(Required) (default to )
search = '' # str | The text to search for in the name and description for workflows. (optional) (default to )
orderby = '' # str | Order the results by this attribute (optional) (default to )
page = 56 # int | The specific page number to get (optional)
page_size = 56 # int | Maximum records per page (optional)
sortorder = '' # str | Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified (optional) (default to )
implicitworkflow =  # object | A flag to indicate whether or not to return implicit workflows. (optional) (default to )
device_type = '' # str | Comma separated list of device types. (optional) (default to )
assignment_state = '' # str | Comma separated list of workflow assignment states. (optional) (default to )
type = '' # str | The workflow type to query. (optional) (default to )

try:
    # New - Get all workflows at this Organization Group.
    api_response = api_instance.workflow_v2_get_all_workflows_async(organization_group_uuid, search=search, orderby=orderby, page=page, page_size=page_size, sortorder=sortorder, implicitworkflow=implicitworkflow, device_type=device_type, assignment_state=assignment_state, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowV2Api->workflow_v2_get_all_workflows_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**object**](.md)| Uuid of the Organization group or csv of uuids of organization groups.(Required) | [default to ]
 **search** | **str**| The text to search for in the name and description for workflows. | [optional] [default to ]
 **orderby** | **str**| Order the results by this attribute | [optional] [default to ]
 **page** | **int**| The specific page number to get | [optional] 
 **page_size** | **int**| Maximum records per page | [optional] 
 **sortorder** | **str**| Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified | [optional] [default to ]
 **implicitworkflow** | [**object**](.md)| A flag to indicate whether or not to return implicit workflows. | [optional] [default to ]
 **device_type** | **str**| Comma separated list of device types. | [optional] [default to ]
 **assignment_state** | **str**| Comma separated list of workflow assignment states. | [optional] [default to ]
 **type** | **str**| The workflow type to query. | [optional] [default to ]

### Return type

[**WorkflowListResponseV2Model**](WorkflowListResponseV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v2_get_workflow_by_id_async**
> WorkflowResponseV2Model workflow_v2_get_workflow_by_id_async(workflow_uuid, step_summary=step_summary)

New - Get the workflow corresponding to the workflow uuid.



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
api_instance = mdmv2.WorkflowV2Api(mdmv2.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required)
step_summary =  # object | Determines whether to fetch the workflow step status summary. (optional) (default to )

try:
    # New - Get the workflow corresponding to the workflow uuid.
    api_response = api_instance.workflow_v2_get_workflow_by_id_async(workflow_uuid, step_summary=step_summary)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowV2Api->workflow_v2_get_workflow_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required) | 
 **step_summary** | [**object**](.md)| Determines whether to fetch the workflow step status summary. | [optional] [default to ]

### Return type

[**WorkflowResponseV2Model**](WorkflowResponseV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_v2_update_workflow_async**
> workflow_v2_update_workflow_async(workflow_uuid, data)

New - Update a workflow.



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
api_instance = mdmv2.WorkflowV2Api(mdmv2.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required)
data = mdmv2.WorkflowV2Model() # WorkflowV2Model | The form data(Required)

try:
    # New - Update a workflow.
    api_instance.workflow_v2_update_workflow_async(workflow_uuid, data)
except ApiException as e:
    print("Exception when calling WorkflowV2Api->workflow_v2_update_workflow_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required) | 
 **data** | [**WorkflowV2Model**](WorkflowV2Model.md)| The form data(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

