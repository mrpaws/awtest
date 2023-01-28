# systemv2.ApnsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apns_v2_get_apns_configuration**](ApnsV2Api.md#apns_v2_get_apns_configuration) | **GET** /groups/{uuid}/apns | New - Gets the APNs configuration for an Organization Group


# **apns_v2_get_apns_configuration**
> ApnsCertificateV2Model apns_v2_get_apns_configuration(uuid)

New - Gets the APNs configuration for an Organization Group

It fetches the configuration for APNs certificate Blob(.pem) uploaded to Workspace ONE UEM

### Example
```python
from __future__ import print_function
import time
import systemv2
from systemv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv2.ApnsV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Unique identifier for the organization group(Required)

try:
    # New - Gets the APNs configuration for an Organization Group
    api_response = api_instance.apns_v2_get_apns_configuration(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApnsV2Api->apns_v2_get_apns_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique identifier for the organization group(Required) | 

### Return type

[**ApnsCertificateV2Model**](ApnsCertificateV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

