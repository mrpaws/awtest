# mdmv1.TunnelHealthV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tunnel_health_v1_health_async**](TunnelHealthV1Api.md#tunnel_health_v1_health_async) | **GET** /tunnel/health | New - Return health information for tunnel connectivity.
[**tunnel_health_v1_health_downstream_async**](TunnelHealthV1Api.md#tunnel_health_v1_health_downstream_async) | **GET** /tunnel/health/downstream | New - Return health information for tunnel downstream connectivity from microservice.


# **tunnel_health_v1_health_async**
> HealthV1Model tunnel_health_v1_health_async()

New - Return health information for tunnel connectivity.

It is used to get health information for tunnel endpoint.

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
api_instance = mdmv1.TunnelHealthV1Api(mdmv1.ApiClient(configuration))

try:
    # New - Return health information for tunnel connectivity.
    api_response = api_instance.tunnel_health_v1_health_async()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TunnelHealthV1Api->tunnel_health_v1_health_async: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthV1Model**](HealthV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnel_health_v1_health_downstream_async**
> tunnel_health_v1_health_downstream_async()

New - Return health information for tunnel downstream connectivity from microservice.

It is used to get health information for tunnel downstream connectivity.

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
api_instance = mdmv1.TunnelHealthV1Api(mdmv1.ApiClient(configuration))

try:
    # New - Return health information for tunnel downstream connectivity from microservice.
    api_instance.tunnel_health_v1_health_downstream_async()
except ApiException as e:
    print("Exception when calling TunnelHealthV1Api->tunnel_health_v1_health_downstream_async: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

