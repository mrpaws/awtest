# mdmv1.OSVersionsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_s_versions_v1_get_active_os_versions**](OSVersionsV1Api.md#o_s_versions_v1_get_active_os_versions) | **GET** /baselines/osversions | New - Retrieves a list of active os versions


# **o_s_versions_v1_get_active_os_versions**
> list[OSVersionV1Model] o_s_versions_v1_get_active_os_versions()

New - Retrieves a list of active os versions

Fetch a list of active os versions

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
api_instance = mdmv1.OSVersionsV1Api(mdmv1.ApiClient(configuration))

try:
    # New - Retrieves a list of active os versions
    api_response = api_instance.o_s_versions_v1_get_active_os_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OSVersionsV1Api->o_s_versions_v1_get_active_os_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OSVersionV1Model]**](OSVersionV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

