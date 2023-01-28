# mdmv1.WorkflowDeviceSideV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_device_side_v1_get_bulk_workflow_definitions_async**](WorkflowDeviceSideV1Api.md#workflow_device_side_v1_get_bulk_workflow_definitions_async) | **POST** /workflows/query | New - Gets the workflows for the device.
[**workflow_device_side_v1_get_workflow_metadata_async**](WorkflowDeviceSideV1Api.md#workflow_device_side_v1_get_workflow_metadata_async) | **GET** /workflows/metadata | New - Gets the metadata for the workflows assigned to the device.


# **workflow_device_side_v1_get_bulk_workflow_definitions_async**
> list[DeviceWorkflowDefinitionBulkResponseV1Model] workflow_device_side_v1_get_bulk_workflow_definitions_async(workflow_uuids)

New - Gets the workflows for the device.

Retrieves the workflows for a device.

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
api_instance = mdmv1.WorkflowDeviceSideV1Api(mdmv1.ApiClient(configuration))
workflow_uuids = [mdmv1.DeviceWorkflowBulkRequestV1Model()] # list[DeviceWorkflowBulkRequestV1Model] | Uuids of the workflows to retrieve.(Required)

try:
    # New - Gets the workflows for the device.
    api_response = api_instance.workflow_device_side_v1_get_bulk_workflow_definitions_async(workflow_uuids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDeviceSideV1Api->workflow_device_side_v1_get_bulk_workflow_definitions_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_uuids** | [**list[DeviceWorkflowBulkRequestV1Model]**](DeviceWorkflowBulkRequestV1Model.md)| Uuids of the workflows to retrieve.(Required) | 

### Return type

[**list[DeviceWorkflowDefinitionBulkResponseV1Model]**](DeviceWorkflowDefinitionBulkResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_device_side_v1_get_workflow_metadata_async**
> list[WorkflowMetadataV1Model] workflow_device_side_v1_get_workflow_metadata_async(device_uuid)

New - Gets the metadata for the workflows assigned to the device.



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
api_instance = mdmv1.WorkflowDeviceSideV1Api(mdmv1.ApiClient(configuration))
device_uuid =  # object | Uuid of the device.(Required) (default to )

try:
    # New - Gets the metadata for the workflows assigned to the device.
    api_response = api_instance.workflow_device_side_v1_get_workflow_metadata_async(device_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDeviceSideV1Api->workflow_device_side_v1_get_workflow_metadata_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**object**](.md)| Uuid of the device.(Required) | [default to ]

### Return type

[**list[WorkflowMetadataV1Model]**](WorkflowMetadataV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

