# systemv2.ScimV2ServiceProviderConfigApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scim_v2_service_provider_config_get_service_provider_config**](ScimV2ServiceProviderConfigApi.md#scim_v2_service_provider_config_get_service_provider_config) | **GET** /scim/v2/ServiceProviderConfig | New - Get the service provider configuration


# **scim_v2_service_provider_config_get_service_provider_config**
> ServiceProviderConfig scim_v2_service_provider_config_get_service_provider_config()

New - Get the service provider configuration

Clients can invoke this endpoint to get the service provider configuration

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
api_instance = systemv2.ScimV2ServiceProviderConfigApi(systemv2.ApiClient(configuration))

try:
    # New - Get the service provider configuration
    api_response = api_instance.scim_v2_service_provider_config_get_service_provider_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScimV2ServiceProviderConfigApi->scim_v2_service_provider_config_get_service_provider_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceProviderConfig**](ServiceProviderConfig.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

