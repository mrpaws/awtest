# mcmv1.ContentGatewayV3Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mcm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_gateway_v3_content_gateway_configuration_bulk_delete_async**](ContentGatewayV3Api.md#content_gateway_v3_content_gateway_configuration_bulk_delete_async) | **PUT** /V3/groups/content-gateway/configuration | New - Bulk deletes Content Gateway configurations.
[**content_gateway_v3_content_gateway_configuration_delete_async**](ContentGatewayV3Api.md#content_gateway_v3_content_gateway_configuration_delete_async) | **DELETE** /V3/groups/content-gateway/configuration | New - Deletes a Content Gateway configuration.
[**content_gateway_v3_create_content_gateway_configuration_async**](ContentGatewayV3Api.md#content_gateway_v3_create_content_gateway_configuration_async) | **POST** /V3/groups/content-gateway/configuration | New - Creates a Content Gateway Configuration.
[**content_gateway_v3_get_content_gateway_configuration_custom_settings_by_id_async**](ContentGatewayV3Api.md#content_gateway_v3_get_content_gateway_configuration_custom_settings_by_id_async) | **POST** /V3/groups/content-gateway/custom-settings/{contentGatewayConfigurationUuid} | New - gets the content gateway configurations and the certificate details with custom settings.
[**content_gateway_v3_get_content_gateway_configurations_async**](ContentGatewayV3Api.md#content_gateway_v3_get_content_gateway_configurations_async) | **GET** /V3/groups/content-gateway/organization-group/{organizationGroupUuid} | New - Gets all content gateway configurations of provider Organization Group.
[**content_gateway_v3_get_content_gateway_configurations_by_id_async**](ContentGatewayV3Api.md#content_gateway_v3_get_content_gateway_configurations_by_id_async) | **POST** /V3/groups/content-gateway/configuration/export-password | New - Gets the content gateway configurations and the certificate details by provided export password.


# **content_gateway_v3_content_gateway_configuration_bulk_delete_async**
> content_gateway_v3_content_gateway_configuration_bulk_delete_async(content_gateway_configuration_uuids)

New - Bulk deletes Content Gateway configurations.

Deletes content gateway configurations in bulk for the provided configuration uuids.

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
api_instance = mcmv1.ContentGatewayV3Api(mcmv1.ApiClient(configuration))
content_gateway_configuration_uuids = [mcmv1.list[str]()] # list[str] | Content gateway configuration uuids to be deleted.(Required)

try:
    # New - Bulk deletes Content Gateway configurations.
    api_instance.content_gateway_v3_content_gateway_configuration_bulk_delete_async(content_gateway_configuration_uuids)
except ApiException as e:
    print("Exception when calling ContentGatewayV3Api->content_gateway_v3_content_gateway_configuration_bulk_delete_async: %s\n" % e)
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

# **content_gateway_v3_content_gateway_configuration_delete_async**
> content_gateway_v3_content_gateway_configuration_delete_async(content_gateway_configuration_uuid)

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
api_instance = mcmv1.ContentGatewayV3Api(mcmv1.ApiClient(configuration))
content_gateway_configuration_uuid =  # object | Content gateway configuration uuid to be deleted.(Required) (default to )

try:
    # New - Deletes a Content Gateway configuration.
    api_instance.content_gateway_v3_content_gateway_configuration_delete_async(content_gateway_configuration_uuid)
except ApiException as e:
    print("Exception when calling ContentGatewayV3Api->content_gateway_v3_content_gateway_configuration_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_gateway_configuration_uuid** | [**object**](.md)| Content gateway configuration uuid to be deleted.(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gateway_v3_create_content_gateway_configuration_async**
> content_gateway_v3_create_content_gateway_configuration_async(content_gateway_v3_model)

New - Creates a Content Gateway Configuration.

It creates a content gateway configuration for the specific platform for which content gateway needs to be configured.

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
api_instance = mcmv1.ContentGatewayV3Api(mcmv1.ApiClient(configuration))
content_gateway_v3_model = mcmv1.ContentGatewayV3Model() # ContentGatewayV3Model | Content gateway configuration details to be created.(Required)

try:
    # New - Creates a Content Gateway Configuration.
    api_instance.content_gateway_v3_create_content_gateway_configuration_async(content_gateway_v3_model)
except ApiException as e:
    print("Exception when calling ContentGatewayV3Api->content_gateway_v3_create_content_gateway_configuration_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_gateway_v3_model** | [**ContentGatewayV3Model**](ContentGatewayV3Model.md)| Content gateway configuration details to be created.(Required) | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gateway_v3_get_content_gateway_configuration_custom_settings_by_id_async**
> list[ContentGatewayCustomSettingsV3] content_gateway_v3_get_content_gateway_configuration_custom_settings_by_id_async(content_gateway_configuration_uuid, password)

New - gets the content gateway configurations and the certificate details with custom settings.

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
api_instance = mcmv1.ContentGatewayV3Api(mcmv1.ApiClient(configuration))
content_gateway_configuration_uuid = 'content_gateway_configuration_uuid_example' # str | Content gateway configuration id for which content gateway configurations are needed.(Required)
password = mcmv1.EncryptionModel() # EncryptionModel | A JSON object containing certificate password.(Required)

try:
    # New - gets the content gateway configurations and the certificate details with custom settings.
    api_response = api_instance.content_gateway_v3_get_content_gateway_configuration_custom_settings_by_id_async(content_gateway_configuration_uuid, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentGatewayV3Api->content_gateway_v3_get_content_gateway_configuration_custom_settings_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_gateway_configuration_uuid** | [**str**](.md)| Content gateway configuration id for which content gateway configurations are needed.(Required) | 
 **password** | [**EncryptionModel**](EncryptionModel.md)| A JSON object containing certificate password.(Required) | 

### Return type

[**list[ContentGatewayCustomSettingsV3]**](ContentGatewayCustomSettingsV3.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gateway_v3_get_content_gateway_configurations_async**
> ContentGatewayV3Model content_gateway_v3_get_content_gateway_configurations_async(organization_group_uuid)

New - Gets all content gateway configurations of provider Organization Group.

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
api_instance = mcmv1.ContentGatewayV3Api(mcmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group id for which content gateway configurations are needed.(Required)

try:
    # New - Gets all content gateway configurations of provider Organization Group.
    api_response = api_instance.content_gateway_v3_get_content_gateway_configurations_async(organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentGatewayV3Api->content_gateway_v3_get_content_gateway_configurations_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Organization Group id for which content gateway configurations are needed.(Required) | 

### Return type

[**ContentGatewayV3Model**](ContentGatewayV3Model.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_gateway_v3_get_content_gateway_configurations_by_id_async**
> content_gateway_v3_get_content_gateway_configurations_by_id_async(password, content_gateway_configuration_uuid)

New - Gets the content gateway configurations and the certificate details by provided export password.

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
api_instance = mcmv1.ContentGatewayV3Api(mcmv1.ApiClient(configuration))
password = mcmv1.EncryptionModel() # EncryptionModel | A JSON object containing certificate password.(Required)
content_gateway_configuration_uuid =  # object | Content gateway configuration uuid for which content gateway configurations are needed.(Required) (default to )

try:
    # New - Gets the content gateway configurations and the certificate details by provided export password.
    api_instance.content_gateway_v3_get_content_gateway_configurations_by_id_async(password, content_gateway_configuration_uuid)
except ApiException as e:
    print("Exception when calling ContentGatewayV3Api->content_gateway_v3_get_content_gateway_configurations_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | [**EncryptionModel**](EncryptionModel.md)| A JSON object containing certificate password.(Required) | 
 **content_gateway_configuration_uuid** | [**object**](.md)| Content gateway configuration uuid for which content gateway configurations are needed.(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

