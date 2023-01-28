# mdmv1.ResourceActionV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_action_v1_resource_validate_action_async**](ResourceActionV1Api.md#resource_action_v1_resource_validate_action_async) | **POST** /resources/validation | New - Checks if the resource can be allowed to perform the action.


# **resource_action_v1_resource_validate_action_async**
> list[ResourceValidationResponseV1Model] resource_action_v1_resource_validate_action_async(resources)

New - Checks if the resource can be allowed to perform the action.



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
api_instance = mdmv1.ResourceActionV1Api(mdmv1.ApiClient(configuration))
resources = mdmv1.ResourceValidationRequestV1Model() # ResourceValidationRequestV1Model | Request to validate the resource.(Required)

try:
    # New - Checks if the resource can be allowed to perform the action.
    api_response = api_instance.resource_action_v1_resource_validate_action_async(resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceActionV1Api->resource_action_v1_resource_validate_action_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resources** | [**ResourceValidationRequestV1Model**](ResourceValidationRequestV1Model.md)| Request to validate the resource.(Required) | 

### Return type

[**list[ResourceValidationResponseV1Model]**](ResourceValidationResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

