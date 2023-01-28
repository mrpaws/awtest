# mcmv1.ContentGatewayV4Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mcm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async**](ContentGatewayV4Api.md#content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async) | **POST** /V4/groups/content-gateway/custom-settings/{contentGatewayConfigurationUuid} | New - Gets the content gateway configurations and the certificate details with custom settings.


# **content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async**
> list[ContentGatewayCustomSettingsV3] content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async(content_gateway_configuration_uuid, password)

New - Gets the content gateway configurations and the certificate details with custom settings.

It returns content gateway configurations along with the custom settings.

### Example
```python
from __future__ import print_function
import time
import mcmv1
from mcmv1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = mcmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mcmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mcmv1.ContentGatewayV4Api(mcmv1.ApiClient(configuration))
content_gateway_configuration_uuid = 'content_gateway_configuration_uuid_example' # str | Content gateway configuration id for which content gateway configurations are needed.(Required).
password = mcmv1.EncryptionModel() # EncryptionModel | A JSON object containing certificate password.(Required).

try:
    # New - Gets the content gateway configurations and the certificate details with custom settings.
    api_response = api_instance.content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async(content_gateway_configuration_uuid, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentGatewayV4Api->content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_gateway_configuration_uuid** | [**str**](.md)| Content gateway configuration id for which content gateway configurations are needed.(Required). | 
 **password** | [**EncryptionModel**](EncryptionModel.md)| A JSON object containing certificate password.(Required). | 

### Return type

[**list[ContentGatewayCustomSettingsV3]**](ContentGatewayCustomSettingsV3.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

