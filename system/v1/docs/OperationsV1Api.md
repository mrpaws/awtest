# systemv1.OperationsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operations_v1_get_operation_status**](OperationsV1Api.md#operations_v1_get_operation_status) | **GET** /operations/{operation-uuid} | New - Retrieves status for an operation


# **operations_v1_get_operation_status**
> operations_v1_get_operation_status(operation_uuid)

New - Retrieves status for an operation

Given an operation identifier this API retrieves and returns its latest recorded status

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
api_instance = systemv1.OperationsV1Api(systemv1.ApiClient(configuration))
operation_uuid = 'operation_uuid_example' # str | Identifier of the operation whose status to be obtained

try:
    # New - Retrieves status for an operation
    api_instance.operations_v1_get_operation_status(operation_uuid)
except ApiException as e:
    print("Exception when calling OperationsV1Api->operations_v1_get_operation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_uuid** | [**str**](.md)| Identifier of the operation whose status to be obtained | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

