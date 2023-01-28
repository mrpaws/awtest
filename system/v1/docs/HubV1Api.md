# systemv1.HubV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hub_v1_configure_hub_services_url**](HubV1Api.md#hub_v1_configure_hub_services_url) | **POST** /hubconfig/hubservicesurl | New - Updates Hub Services configuration URL at given organization group.


# **hub_v1_configure_hub_services_url**
> hub_v1_configure_hub_services_url(hub_configuration_model)

New - Updates Hub Services configuration URL at given organization group.

Updates Hub Services configuration URL at the given organization group.

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
api_instance = systemv1.HubV1Api(systemv1.ApiClient(configuration))
hub_configuration_model = systemv1.HubConfigurationV1Model() # HubConfigurationV1Model | Model containing Hub Services configurations.(Required)

try:
    # New - Updates Hub Services configuration URL at given organization group.
    api_instance.hub_v1_configure_hub_services_url(hub_configuration_model)
except ApiException as e:
    print("Exception when calling HubV1Api->hub_v1_configure_hub_services_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_configuration_model** | [**HubConfigurationV1Model**](HubConfigurationV1Model.md)| Model containing Hub Services configurations.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

