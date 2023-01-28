# mcmv1.ContentGatewayV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mcm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_gateway_v2_content_gateway_configuration_bulk_delete_async**](ContentGatewayV2Api.md#content_gateway_v2_content_gateway_configuration_bulk_delete_async) | **POST** /V2/groups/contentgateway/delete | New - Deletes Content Gateway configurations.
[**content_gateway_v2_content_gateway_configuration_delete_async**](ContentGatewayV2Api.md#content_gateway_v2_content_gateway_configuration_delete_async) | **DELETE** /V2/groups/contentgateway/{contentGatewayConfigurationUuid} | New - Deletes a Content Gateway configuration.
[**content_gateway_v2_create_content_gateway_configuration_async**](ContentGatewayV2Api.md#content_gateway_v2_create_content_gateway_configuration_async) | **POST** /V2/groups/contentgateway | New - Creates a Content Gateway Configuration
[**content_gateway_v2_get_content_gateway_configuration_custom_settings_by_id_async**](ContentGatewayV2Api.md#content_gateway_v2_get_content_gateway_configuration_custom_settings_by_id_async) | **POST** /V2/groups/customsettings/contentgateway/{contentGatewayConfigurationId} | New - Gets the content gateway configurations and the certificate details with custom settings.
[**content_gateway_v2_get_content_gateway_configurations_async**](ContentGatewayV2Api.md#content_gateway_v2_get_content_gateway_configurations_async) | **GET** /V2/groups/{groupId}/contentgateway | New - Gets the content gateway configurations
[**content_gateway_v2_get_content_gateway_configurations_by_id_async**](ContentGatewayV2Api.md#content_gateway_v2_get_content_gateway_configurations_by_id_async) | **POST** /V2/groups/contentgateway/{contentGatewayConfigurationUuid} | New - gets the content gateway configurations and the certificate details


# **content_gateway_v2_content_gateway_configuration_bulk_delete_async**
> content_gateway_v2_content_gateway_configuration_bulk_delete_async(content_gateway_configuration_uuids)

New - Deletes Content Gateway configurations.

Deletes content gateway configuration in bulk for the provided configuration uuids.

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
api_instance = mcmv1.ContentGatewayV2Api(mcmv1.ApiClient(configuration))
content_gateway_configuration_uuids = [mcmv1.list[str]()] # list[str] | Content gateway configuration uuids to be deleted.(Required)

try:
    # New - Deletes Content Gateway configurations.
    api_instance.content_gateway_v2_content_gateway_configuration_bulk_delete_async(content_gateway_configuration_uuids)
except ApiException as e:
    print("Exception when calling ContentGatewayV2Api->content_gateway_v2_content_gateway_configuration_bulk_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_gateway_configuration_uuids** | **list[str]**| Content gateway configuration uuids to be deleted.(Required) | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gateway_v2_content_gateway_configuration_delete_async**
> content_gateway_v2_content_gateway_configuration_delete_async(content_gateway_configuration_uuid)

New - Deletes a Content Gateway configuration.

It deletes a content gateway configuration for the provided content gateway configuration uuid.

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
api_instance = mcmv1.ContentGatewayV2Api(mcmv1.ApiClient(configuration))
content_gateway_configuration_uuid = 'content_gateway_configuration_uuid_example' # str | Content gateway configuration uuid to be deleted.(Required)

try:
    # New - Deletes a Content Gateway configuration.
    api_instance.content_gateway_v2_content_gateway_configuration_delete_async(content_gateway_configuration_uuid)
except ApiException as e:
    print("Exception when calling ContentGatewayV2Api->content_gateway_v2_content_gateway_configuration_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_gateway_configuration_uuid** | [**str**](.md)| Content gateway configuration uuid to be deleted.(Required) | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gateway_v2_create_content_gateway_configuration_async**
> content_gateway_v2_create_content_gateway_configuration_async(content_gateway_v2_model)

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
api_instance = mcmv1.ContentGatewayV2Api(mcmv1.ApiClient(configuration))
content_gateway_v2_model = mcmv1.ContentGatewayV2Model() # ContentGatewayV2Model | Content gateway configuration details to be created(Required)

try:
    # New - Creates a Content Gateway Configuration
    api_instance.content_gateway_v2_create_content_gateway_configuration_async(content_gateway_v2_model)
except ApiException as e:
    print("Exception when calling ContentGatewayV2Api->content_gateway_v2_create_content_gateway_configuration_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_gateway_v2_model** | [**ContentGatewayV2Model**](ContentGatewayV2Model.md)| Content gateway configuration details to be created(Required) | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gateway_v2_get_content_gateway_configuration_custom_settings_by_id_async**
> list[ContentGatewayCustomSettings] content_gateway_v2_get_content_gateway_configuration_custom_settings_by_id_async(content_gateway_configuration_id, password)

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
api_instance = mcmv1.ContentGatewayV2Api(mcmv1.ApiClient(configuration))
content_gateway_configuration_id = 'content_gateway_configuration_id_example' # str | Content gateway configuration id for which content gateway configurations are needed(Required)
password = mcmv1.EncryptionModel() # EncryptionModel | A JSON object containing certificate password.(Required)

try:
    # New - Gets the content gateway configurations and the certificate details with custom settings.
    api_response = api_instance.content_gateway_v2_get_content_gateway_configuration_custom_settings_by_id_async(content_gateway_configuration_id, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentGatewayV2Api->content_gateway_v2_get_content_gateway_configuration_custom_settings_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_gateway_configuration_id** | **str**| Content gateway configuration id for which content gateway configurations are needed(Required) | 
 **password** | [**EncryptionModel**](EncryptionModel.md)| A JSON object containing certificate password.(Required) | 

### Return type

[**list[ContentGatewayCustomSettings]**](ContentGatewayCustomSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gateway_v2_get_content_gateway_configurations_async**
> ContentGatewayV2Model content_gateway_v2_get_content_gateway_configurations_async(group_id)

New - Gets the content gateway configurations

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
api_instance = mcmv1.ContentGatewayV2Api(mcmv1.ApiClient(configuration))
group_id = 'group_id_example' # str | Location group id for which content gateway configurations are needed(Required)

try:
    # New - Gets the content gateway configurations
    api_response = api_instance.content_gateway_v2_get_content_gateway_configurations_async(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentGatewayV2Api->content_gateway_v2_get_content_gateway_configurations_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Location group id for which content gateway configurations are needed(Required) | 

### Return type

[**ContentGatewayV2Model**](ContentGatewayV2Model.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gateway_v2_get_content_gateway_configurations_by_id_async**
> content_gateway_v2_get_content_gateway_configurations_by_id_async(content_gateway_configuration_uuid, password)

New - gets the content gateway configurations and the certificate details

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
api_instance = mcmv1.ContentGatewayV2Api(mcmv1.ApiClient(configuration))
content_gateway_configuration_uuid = 'content_gateway_configuration_uuid_example' # str | Content gateway configuration uuid for which content gateway configurations are needed.(Required)
password = mcmv1.EncryptionModel() # EncryptionModel | A JSON object containing certificate password.(Required)

try:
    # New - gets the content gateway configurations and the certificate details
    api_instance.content_gateway_v2_get_content_gateway_configurations_by_id_async(content_gateway_configuration_uuid, password)
except ApiException as e:
    print("Exception when calling ContentGatewayV2Api->content_gateway_v2_get_content_gateway_configurations_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_gateway_configuration_uuid** | [**str**](.md)| Content gateway configuration uuid for which content gateway configurations are needed.(Required) | 
 **password** | [**EncryptionModel**](EncryptionModel.md)| A JSON object containing certificate password.(Required) | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml -application/x-www-form-urlencoded
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

