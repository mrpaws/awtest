# systemv2.TenantStorageSettingsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenant_storage_settings_v2_get_tenant_storage_configuration_async**](TenantStorageSettingsV2Api.md#tenant_storage_settings_v2_get_tenant_storage_configuration_async) | **GET** /groups/{ogUuid}/settings/agent/storage | New - Retrieves the tenant storage configuration details.


# **tenant_storage_settings_v2_get_tenant_storage_configuration_async**
> TenantStorageSettingsV2ResponseModel tenant_storage_settings_v2_get_tenant_storage_configuration_async(og_uuid)

New - Retrieves the tenant storage configuration details.

Retrieves the configuration settings for the Workspace ONE UEM to tenant storage configuration.

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
api_instance = systemv2.TenantStorageSettingsV2Api(systemv2.ApiClient(configuration))
og_uuid = 'og_uuid_example' # str | Organization uuid.(Required).

try:
    # New - Retrieves the tenant storage configuration details.
    api_response = api_instance.tenant_storage_settings_v2_get_tenant_storage_configuration_async(og_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantStorageSettingsV2Api->tenant_storage_settings_v2_get_tenant_storage_configuration_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **og_uuid** | [**str**](.md)| Organization uuid.(Required). | 

### Return type

[**TenantStorageSettingsV2ResponseModel**](TenantStorageSettingsV2ResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

