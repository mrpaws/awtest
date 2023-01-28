# mdmv1.ResourcesV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources_v1_query_resources_async**](ResourcesV1Api.md#resources_v1_query_resources_async) | **POST** /resources/query | New - Retrieves the details about the resources


# **resources_v1_query_resources_async**
> list[ResourceResponseV1Model] resources_v1_query_resources_async(resources)

New - Retrieves the details about the resources



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
api_instance = mdmv1.ResourcesV1Api(mdmv1.ApiClient(configuration))
resources = [mdmv1.ResourceRequestV1Model()] # list[ResourceRequestV1Model] | The resources to retrieve details about.(Required)

try:
    # New - Retrieves the details about the resources
    api_response = api_instance.resources_v1_query_resources_async(resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesV1Api->resources_v1_query_resources_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resources** | [**list[ResourceRequestV1Model]**](ResourceRequestV1Model.md)| The resources to retrieve details about.(Required) | 

### Return type

[**list[ResourceResponseV1Model]**](ResourceResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

