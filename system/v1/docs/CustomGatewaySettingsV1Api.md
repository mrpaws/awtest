# systemv1.CustomGatewaySettingsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_gateway_settings_v1_edit_custom_gateway_settings**](CustomGatewaySettingsV1Api.md#custom_gateway_settings_v1_edit_custom_gateway_settings) | **POST** /custom-gateway-settings/{moduleName}/configuration/{configurationUuid} | New - Bulk Add or update or Delete  Custom Gateway Settings
[**custom_gateway_settings_v1_get_custom_gateway_setting_key_details**](CustomGatewaySettingsV1Api.md#custom_gateway_settings_v1_get_custom_gateway_setting_key_details) | **GET** /custom-gateway-settings/keys/{keyUuid} | New - Gets Details of a Key
[**custom_gateway_settings_v1_get_custom_gateway_setting_keys**](CustomGatewaySettingsV1Api.md#custom_gateway_settings_v1_get_custom_gateway_setting_keys) | **GET** /custom-gateway-settings/{moduleName}/keys | New - Gets All the predefined keys for the module with its validation details
[**custom_gateway_settings_v1_get_custom_gateway_settings**](CustomGatewaySettingsV1Api.md#custom_gateway_settings_v1_get_custom_gateway_settings) | **GET** /custom-gateway-settings/{moduleName}/configuration/{configurationUuid} | New - Gets the Custom Gateway Settings for ContentGateway,Tunnel and MEM


# **custom_gateway_settings_v1_edit_custom_gateway_settings**
> custom_gateway_settings_v1_edit_custom_gateway_settings(configuration_uuid, module_name, custom_gateway_setting)

New - Bulk Add or update or Delete  Custom Gateway Settings

Bulk Add or update or Delete a set of Custom Gateway Settings linked to configuration

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
api_instance = systemv1.CustomGatewaySettingsV1Api(systemv1.ApiClient(configuration))
configuration_uuid = 'configuration_uuid_example' # str | configuration id(Required)
module_name = 'module_name_example' # str | module name ContentGateWay,Tunnel or MEM(Required)
custom_gateway_setting = [systemv1.CustomGatewaySettingV1()] # list[CustomGatewaySettingV1] | Custom Gateway Setting to be added(Required)

try:
    # New - Bulk Add or update or Delete  Custom Gateway Settings
    api_instance.custom_gateway_settings_v1_edit_custom_gateway_settings(configuration_uuid, module_name, custom_gateway_setting)
except ApiException as e:
    print("Exception when calling CustomGatewaySettingsV1Api->custom_gateway_settings_v1_edit_custom_gateway_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_uuid** | [**str**](.md)| configuration id(Required) | 
 **module_name** | **str**| module name ContentGateWay,Tunnel or MEM(Required) | 
 **custom_gateway_setting** | [**list[CustomGatewaySettingV1]**](CustomGatewaySettingV1.md)| Custom Gateway Setting to be added(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_gateway_settings_v1_get_custom_gateway_setting_key_details**
> CustomGatewaySettingKeyV1 custom_gateway_settings_v1_get_custom_gateway_setting_key_details(key_uuid)

New - Gets Details of a Key

Custom Gateway Setting keys

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
api_instance = systemv1.CustomGatewaySettingsV1Api(systemv1.ApiClient(configuration))
key_uuid = 'key_uuid_example' # str | Custom Gateway Settings Key Guid(Required)

try:
    # New - Gets Details of a Key
    api_response = api_instance.custom_gateway_settings_v1_get_custom_gateway_setting_key_details(key_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomGatewaySettingsV1Api->custom_gateway_settings_v1_get_custom_gateway_setting_key_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_uuid** | [**str**](.md)| Custom Gateway Settings Key Guid(Required) | 

### Return type

[**CustomGatewaySettingKeyV1**](CustomGatewaySettingKeyV1.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_gateway_settings_v1_get_custom_gateway_setting_keys**
> list[CustomGatewaySettingKeyV1] custom_gateway_settings_v1_get_custom_gateway_setting_keys(module_name)

New - Gets All the predefined keys for the module with its validation details

Custom Gateway Setting keys and its validation details

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
api_instance = systemv1.CustomGatewaySettingsV1Api(systemv1.ApiClient(configuration))
module_name = 'module_name_example' # str | module name ContentGateWay,Tunnel or MEM(Required)

try:
    # New - Gets All the predefined keys for the module with its validation details
    api_response = api_instance.custom_gateway_settings_v1_get_custom_gateway_setting_keys(module_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomGatewaySettingsV1Api->custom_gateway_settings_v1_get_custom_gateway_setting_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_name** | **str**| module name ContentGateWay,Tunnel or MEM(Required) | 

### Return type

[**list[CustomGatewaySettingKeyV1]**](CustomGatewaySettingKeyV1.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_gateway_settings_v1_get_custom_gateway_settings**
> list[CustomGatewaySettingV1] custom_gateway_settings_v1_get_custom_gateway_settings(configuration_uuid, module_name)

New - Gets the Custom Gateway Settings for ContentGateway,Tunnel and MEM

Custom Gateway Settings needed for interacting with ContentGateway,Tunnel and MEM

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
api_instance = systemv1.CustomGatewaySettingsV1Api(systemv1.ApiClient(configuration))
configuration_uuid = 'configuration_uuid_example' # str | configuration id of ContentGateway, Tunnel and MEM(Required)
module_name = 'module_name_example' # str | module name ContentGateway, Tunnel and MEM(Required)

try:
    # New - Gets the Custom Gateway Settings for ContentGateway,Tunnel and MEM
    api_response = api_instance.custom_gateway_settings_v1_get_custom_gateway_settings(configuration_uuid, module_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomGatewaySettingsV1Api->custom_gateway_settings_v1_get_custom_gateway_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_uuid** | [**str**](.md)| configuration id of ContentGateway, Tunnel and MEM(Required) | 
 **module_name** | **str**| module name ContentGateway, Tunnel and MEM(Required) | 

### Return type

[**list[CustomGatewaySettingV1]**](CustomGatewaySettingV1.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

