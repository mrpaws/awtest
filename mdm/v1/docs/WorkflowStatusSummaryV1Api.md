# mdmv1.WorkflowStatusSummaryV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_status_summary_v1_get_workflow_status_summary_async**](WorkflowStatusSummaryV1Api.md#workflow_status_summary_v1_get_workflow_status_summary_async) | **GET** /workflows/{workflowUuid}/statuses/summary | New - Fetch workflow status summary across all assigned devices.
[**workflow_status_summary_v1_get_workflow_step_status_summary_async**](WorkflowStatusSummaryV1Api.md#workflow_status_summary_v1_get_workflow_step_status_summary_async) | **GET** /workflows/{workflowUuid}/steps/statuses/summary | New - Fetch workflow step status summary.


# **workflow_status_summary_v1_get_workflow_status_summary_async**
> WorkflowSummaryResponseModel workflow_status_summary_v1_get_workflow_status_summary_async(workflow_uuid, organization_group_uuid)

New - Fetch workflow status summary across all assigned devices.



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
api_instance = mdmv1.WorkflowStatusSummaryV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required).
organization_group_uuid =  # object | Operating organization group UUID for which the summary is required.(Required) (default to )

try:
    # New - Fetch workflow status summary across all assigned devices.
    api_response = api_instance.workflow_status_summary_v1_get_workflow_status_summary_async(workflow_uuid, organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowStatusSummaryV1Api->workflow_status_summary_v1_get_workflow_status_summary_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required). | 
 **organization_group_uuid** | [**object**](.md)| Operating organization group UUID for which the summary is required.(Required) | [default to ]

### Return type

[**WorkflowSummaryResponseModel**](WorkflowSummaryResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_status_summary_v1_get_workflow_step_status_summary_async**
> WorkflowStepSummaryResponseModel workflow_status_summary_v1_get_workflow_step_status_summary_async(workflow_uuid, organization_group_uuid)

New - Fetch workflow step status summary.



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
api_instance = mdmv1.WorkflowStatusSummaryV1Api(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Uuid of the workflow.(Required).
organization_group_uuid =  # object | Operating organization group UUID for which the summary is required.(Required) (default to )

try:
    # New - Fetch workflow step status summary.
    api_response = api_instance.workflow_status_summary_v1_get_workflow_step_status_summary_async(workflow_uuid, organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowStatusSummaryV1Api->workflow_status_summary_v1_get_workflow_step_status_summary_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Uuid of the workflow.(Required). | 
 **organization_group_uuid** | [**object**](.md)| Operating organization group UUID for which the summary is required.(Required) | [default to ]

### Return type

[**WorkflowStepSummaryResponseModel**](WorkflowStepSummaryResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

