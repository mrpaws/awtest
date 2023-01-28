# mdmv1.WorkflowStatusReportingApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_status_reporting_get_device_count_for_workflow_status_async**](WorkflowStatusReportingApi.md#workflow_status_reporting_get_device_count_for_workflow_status_async) | **GET** /devices/workflows/{workflowUuid}/status/device-count | New - Get the count of devices for each workflow status.
[**workflow_status_reporting_get_workflow_status_async**](WorkflowStatusReportingApi.md#workflow_status_reporting_get_workflow_status_async) | **GET** /devices/{deviceUuid}/workflows/{workflowUuid}/status | New - Gets the status of the workflow and corresponding steps for the device.
[**workflow_status_reporting_get_workflow_status_by_device_async**](WorkflowStatusReportingApi.md#workflow_status_reporting_get_workflow_status_by_device_async) | **GET** /devices/{deviceUuid}/workflows/status | New - Get the workflow status for device.


# **workflow_status_reporting_get_device_count_for_workflow_status_async**
> list[WorkflowStatusCount] workflow_status_reporting_get_device_count_for_workflow_status_async(workflow_uuid)

New - Get the count of devices for each workflow status.

Get the count of devices that belong to each workflow status for specified WorkflowUuid.

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
api_instance = mdmv1.WorkflowStatusReportingApi(mdmv1.ApiClient(configuration))
workflow_uuid = 'workflow_uuid_example' # str | Unique Identifier for the workflow.(Required)

try:
    # New - Get the count of devices for each workflow status.
    api_response = api_instance.workflow_status_reporting_get_device_count_for_workflow_status_async(workflow_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowStatusReportingApi->workflow_status_reporting_get_device_count_for_workflow_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuid** | [**str**](.md)| Unique Identifier for the workflow.(Required) | 

### Return type

[**list[WorkflowStatusCount]**](WorkflowStatusCount.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_status_reporting_get_workflow_status_async**
> WorkflowStatusV1Model workflow_status_reporting_get_workflow_status_async(device_uuid, workflow_uuid, page=page, pagesize=pagesize)

New - Gets the status of the workflow and corresponding steps for the device.

Gets the status of the workflow and corresponding steps for the device.

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
api_instance = mdmv1.WorkflowStatusReportingApi(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Unique Identifier for the device.(Required)
workflow_uuid = 'workflow_uuid_example' # str | Unique Identifier for the workflow.(Required)
page = 56 # int | The specific page number to get. (optional)
pagesize = 56 # int | Maximum records per page. (optional)

try:
    # New - Gets the status of the workflow and corresponding steps for the device.
    api_response = api_instance.workflow_status_reporting_get_workflow_status_async(device_uuid, workflow_uuid, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowStatusReportingApi->workflow_status_reporting_get_workflow_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Unique Identifier for the device.(Required) | 
 **workflow_uuid** | [**str**](.md)| Unique Identifier for the workflow.(Required) | 
 **page** | **int**| The specific page number to get. | [optional] 
 **pagesize** | **int**| Maximum records per page. | [optional] 

### Return type

[**WorkflowStatusV1Model**](WorkflowStatusV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_status_reporting_get_workflow_status_by_device_async**
> list[WorkflowStatusV1Model] workflow_status_reporting_get_workflow_status_by_device_async(device_uuid, search=search, orderby=orderby, page=page, pagesize=pagesize, sortorder=sortorder)

New - Get the workflow status for device.

Get the status of device workflow.

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
api_instance = mdmv1.WorkflowStatusReportingApi(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Uuid of the device.(Required)
search = '' # str | The text to search for in the name of the workflow. (optional) (default to )
orderby = '' # str | Order the results by this attribute. (optional) (default to )
page = 56 # int | The specific page number to get. (optional)
pagesize = 56 # int | Maximum records per page. (optional)
sortorder = '' # str | Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. (optional) (default to )

try:
    # New - Get the workflow status for device.
    api_response = api_instance.workflow_status_reporting_get_workflow_status_by_device_async(device_uuid, search=search, orderby=orderby, page=page, pagesize=pagesize, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowStatusReportingApi->workflow_status_reporting_get_workflow_status_by_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Uuid of the device.(Required) | 
 **search** | **str**| The text to search for in the name of the workflow. | [optional] [default to ]
 **orderby** | **str**| Order the results by this attribute. | [optional] [default to ]
 **page** | **int**| The specific page number to get. | [optional] 
 **pagesize** | **int**| Maximum records per page. | [optional] 
 **sortorder** | **str**| Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified. | [optional] [default to ]

### Return type

[**list[WorkflowStatusV1Model]**](WorkflowStatusV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

