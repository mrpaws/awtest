# mdmv1.TunnelStandaloneClientV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tunnel_standalone_client_v1_create_one_time_token_async**](TunnelStandaloneClientV1Api.md#tunnel_standalone_client_v1_create_one_time_token_async) | **POST** /devices/{uuid}/tunnel/{tunnelConfigUuid}/applications/{bundleId}/profile/{profileUuid}/scep-token/{issuer} | New - Generates one time token to allow device to obtain authentication certificate
[**tunnel_standalone_client_v1_get_tunnel_configuration_async**](TunnelStandaloneClientV1Api.md#tunnel_standalone_client_v1_get_tunnel_configuration_async) | **GET** /devices/{deviceUuid}/tunnel/profile | New - Retrieves the tunnel configuration for the device.


# **tunnel_standalone_client_v1_create_one_time_token_async**
> tunnel_standalone_client_v1_create_one_time_token_async(uuid, tunnel_config_uuid, bundle_id, profile_uuid, issuer)

New - Generates one time token to allow device to obtain authentication certificate

Generates one time token that is required for the device to make seperate request to the certificate delivery endpoint to obtain authentication certificate using SCEP

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
api_instance = mdmv1.TunnelStandaloneClientV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Unique identifier (GUID) of the device(Required).
tunnel_config_uuid = 'tunnel_config_uuid_example' # str | Unique identifier (GUID) of the device(Required).
bundle_id = 'bundle_id_example' # str | Application Identifier (i.e com.apple.mobilesafari)(Required).
profile_uuid = 'profile_uuid_example' # str | Unique identifier (GUID) of the profile.(Required).
issuer = 'issuer_example' # str | Certificate issuer - uniquely identifies authority and template for the certificate(Required).

try:
    # New - Generates one time token to allow device to obtain authentication certificate
    api_instance.tunnel_standalone_client_v1_create_one_time_token_async(uuid, tunnel_config_uuid, bundle_id, profile_uuid, issuer)
except ApiException as e:
    print("Exception when calling TunnelStandaloneClientV1Api->tunnel_standalone_client_v1_create_one_time_token_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique identifier (GUID) of the device(Required). | 
 **tunnel_config_uuid** | [**str**](.md)| Unique identifier (GUID) of the device(Required). | 
 **bundle_id** | **str**| Application Identifier (i.e com.apple.mobilesafari)(Required). | 
 **profile_uuid** | [**str**](.md)| Unique identifier (GUID) of the profile.(Required). | 
 **issuer** | **str**| Certificate issuer - uniquely identifies authority and template for the certificate(Required). | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnel_standalone_client_v1_get_tunnel_configuration_async**
> TunnelStandAloneClientConfigurationV1Model tunnel_standalone_client_v1_get_tunnel_configuration_async(device_uuid)

New - Retrieves the tunnel configuration for the device.

Retrieves the tunnel configuration for the specified device based on the provided tunnel configuration uuid and other query params.

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
api_instance = mdmv1.TunnelStandaloneClientV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | The device uuid(Required).

try:
    # New - Retrieves the tunnel configuration for the device.
    api_response = api_instance.tunnel_standalone_client_v1_get_tunnel_configuration_async(device_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TunnelStandaloneClientV1Api->tunnel_standalone_client_v1_get_tunnel_configuration_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| The device uuid(Required). | 

### Return type

[**TunnelStandAloneClientConfigurationV1Model**](TunnelStandAloneClientConfigurationV1Model.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

