# mdmv1.DsmV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dsm_v1_override_resources**](DsmV1Api.md#dsm_v1_override_resources) | **POST** /dsm/users/{userUuid}/devices/{deviceUuid}/overrides | Overrides the resource behaviour on the specified device.


# **dsm_v1_override_resources**
> dsm_v1_override_resources(user_uuid, device_uuid, resource_overrides_v1_request=resource_overrides_v1_request)

Overrides the resource behaviour on the specified device.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

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
api_instance = mdmv1.DsmV1Api(mdmv1.ApiClient(configuration))
user_uuid = 'user_uuid_example' # str | user id.
device_uuid = 'device_uuid_example' # str | device id.
resource_overrides_v1_request = mdmv1.ResourceOverridesV1Request() # ResourceOverridesV1Request | override request. (optional)

try:
    # Overrides the resource behaviour on the specified device.
    api_instance.dsm_v1_override_resources(user_uuid, device_uuid, resource_overrides_v1_request=resource_overrides_v1_request)
except ApiException as e:
    print("Exception when calling DsmV1Api->dsm_v1_override_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | [**str**](.md)| user id. | 
 **device_uuid** | [**str**](.md)| device id. | 
 **resource_overrides_v1_request** | [**ResourceOverridesV1Request**](ResourceOverridesV1Request.md)| override request. | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

