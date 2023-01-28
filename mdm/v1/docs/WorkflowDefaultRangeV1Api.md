# mdmv1.WorkflowDefaultRangeV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_default_range_v1_get_workflow_default_values_and_range_async**](WorkflowDefaultRangeV1Api.md#workflow_default_range_v1_get_workflow_default_values_and_range_async) | **GET** /workflowdefaultrange | New - Get workflows default for this organization group.
[**workflow_default_range_v1_save_workflow_default_values_async**](WorkflowDefaultRangeV1Api.md#workflow_default_range_v1_save_workflow_default_values_async) | **POST** /workflowdefaultrange | New - Save Workflow Defaults for this Organization Group.


# **workflow_default_range_v1_get_workflow_default_values_and_range_async**
> WorkflowDefaultAndRangeResponseV1Model workflow_default_range_v1_get_workflow_default_values_and_range_async(organization_group_uuid)

New - Get workflows default for this organization group.

Get workflow deafults and their ranges for this  organization group.

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
api_instance = mdmv1.WorkflowDefaultRangeV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid =  # object | Uuid of the Organization group.(Required) (default to )

try:
    # New - Get workflows default for this organization group.
    api_response = api_instance.workflow_default_range_v1_get_workflow_default_values_and_range_async(organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefaultRangeV1Api->workflow_default_range_v1_get_workflow_default_values_and_range_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**object**](.md)| Uuid of the Organization group.(Required) | [default to ]

### Return type

[**WorkflowDefaultAndRangeResponseV1Model**](WorkflowDefaultAndRangeResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_default_range_v1_save_workflow_default_values_async**
> workflow_default_range_v1_save_workflow_default_values_async(data, organization_group_uuid)

New - Save Workflow Defaults for this Organization Group.



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
api_instance = mdmv1.WorkflowDefaultRangeV1Api(mdmv1.ApiClient(configuration))
data = mdmv1.WorkflowDefaultValueV1Model() # WorkflowDefaultValueV1Model | The post data(Required)
organization_group_uuid =  # object | Uuid of the Organization group.(Required) (default to )

try:
    # New - Save Workflow Defaults for this Organization Group.
    api_instance.workflow_default_range_v1_save_workflow_default_values_async(data, organization_group_uuid)
except ApiException as e:
    print("Exception when calling WorkflowDefaultRangeV1Api->workflow_default_range_v1_save_workflow_default_values_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WorkflowDefaultValueV1Model**](WorkflowDefaultValueV1Model.md)| The post data(Required) | 
 **organization_group_uuid** | [**object**](.md)| Uuid of the Organization group.(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

