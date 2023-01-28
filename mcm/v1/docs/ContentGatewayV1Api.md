# mcmv1.ContentGatewayV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mcm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_gateway_v1_create_content_gateway_configuration**](ContentGatewayV1Api.md#content_gateway_v1_create_content_gateway_configuration) | **POST** /groups/contentgateway | New - Creates a Content Gateway Configuration
[**content_gateway_v1_get_content_gateway_configurations**](ContentGatewayV1Api.md#content_gateway_v1_get_content_gateway_configurations) | **GET** /groups/{groupId}/contentgateway | New - gets the content gateway configurations
[**content_gateway_v1_get_content_gateway_configurations_by_id**](ContentGatewayV1Api.md#content_gateway_v1_get_content_gateway_configurations_by_id) | **POST** /groups/contentgateway/{contentGatewayConfigurationId} | New - Gets the content gateway configurations and the certificate details


# **content_gateway_v1_create_content_gateway_configuration**
> content_gateway_v1_create_content_gateway_configuration(content_gateway_v1_model)

New - Creates a Content Gateway Configuration

It creates a content gateway configuration for the specific platform for which content gateway needs to be configured

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
api_instance = mcmv1.ContentGatewayV1Api(mcmv1.ApiClient(configuration))
content_gateway_v1_model = mcmv1.ContentGatewayV1Model() # ContentGatewayV1Model | Content gateway configuration details to be created(Required)

try:
    # New - Creates a Content Gateway Configuration
    api_instance.content_gateway_v1_create_content_gateway_configuration(content_gateway_v1_model)
except ApiException as e:
    print("Exception when calling ContentGatewayV1Api->content_gateway_v1_create_content_gateway_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_gateway_v1_model** | [**ContentGatewayV1Model**](ContentGatewayV1Model.md)| Content gateway configuration details to be created(Required) | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gateway_v1_get_content_gateway_configurations**
> ContentGatewayV1Model content_gateway_v1_get_content_gateway_configurations(group_id)

New - gets the content gateway configurations

It returns all the content gateway configurations such as the platform in which the content gateway is configured and the ports to which requests are to be forwarded.

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
api_instance = mcmv1.ContentGatewayV1Api(mcmv1.ApiClient(configuration))
group_id = 'group_id_example' # str | location group id for which content gateway configurations are needed(Required)

try:
    # New - gets the content gateway configurations
    api_response = api_instance.content_gateway_v1_get_content_gateway_configurations(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentGatewayV1Api->content_gateway_v1_get_content_gateway_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| location group id for which content gateway configurations are needed(Required) | 

### Return type

[**ContentGatewayV1Model**](ContentGatewayV1Model.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gateway_v1_get_content_gateway_configurations_by_id**
> content_gateway_v1_get_content_gateway_configurations_by_id(content_gateway_configuration_id, password)

New - Gets the content gateway configurations and the certificate details

It returns a content gateway configuration such as the platform in which the content gateway is configured and the port to which requests are to be forwarded.

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
api_instance = mcmv1.ContentGatewayV1Api(mcmv1.ApiClient(configuration))
content_gateway_configuration_id = 'content_gateway_configuration_id_example' # str | Content gateway configuration id for which contentgateway configurations are needed(Required)
password = mcmv1.EncryptionModel() # EncryptionModel | Password with which the certificate details are retrieved(Required)

try:
    # New - Gets the content gateway configurations and the certificate details
    api_instance.content_gateway_v1_get_content_gateway_configurations_by_id(content_gateway_configuration_id, password)
except ApiException as e:
    print("Exception when calling ContentGatewayV1Api->content_gateway_v1_get_content_gateway_configurations_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_gateway_configuration_id** | **str**| Content gateway configuration id for which contentgateway configurations are needed(Required) | 
 **password** | [**EncryptionModel**](EncryptionModel.md)| Password with which the certificate details are retrieved(Required) | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

