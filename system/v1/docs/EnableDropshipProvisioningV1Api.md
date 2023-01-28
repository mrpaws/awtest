# systemv1.EnableDropshipProvisioningV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enable_dropship_provisioning_v1_enable_dropship_provisioning_async**](EnableDropshipProvisioningV1Api.md#enable_dropship_provisioning_v1_enable_dropship_provisioning_async) | **POST** /groups/{uuid}/dropship-provisioning | New - Enable a dropship provisioning for given organization groups
[**enable_dropship_provisioning_v1_get_details_async**](EnableDropshipProvisioningV1Api.md#enable_dropship_provisioning_v1_get_details_async) | **GET** /groups/{uuid}/dropship-provisioning | New - Gets dropship provisioning details of a given organization group UUID.


# **enable_dropship_provisioning_v1_enable_dropship_provisioning_async**
> DropshipProvisioningSettingsDetailsResponseV1Model enable_dropship_provisioning_v1_enable_dropship_provisioning_async(uuid, enable_dropship_provisioning_details)

New - Enable a dropship provisioning for given organization groups

Saves and enable dropship provisioning for a given Organization Group UUID.

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
api_instance = systemv1.EnableDropshipProvisioningV1Api(systemv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization group UUID to perform the operation on.(Required).
enable_dropship_provisioning_details = systemv1.DropshipProvisioningSettingsDetailsRequestV1Model() # DropshipProvisioningSettingsDetailsRequestV1Model | Enable Dropship Provisioning to be saved.(Required).

try:
    # New - Enable a dropship provisioning for given organization groups
    api_response = api_instance.enable_dropship_provisioning_v1_enable_dropship_provisioning_async(uuid, enable_dropship_provisioning_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnableDropshipProvisioningV1Api->enable_dropship_provisioning_v1_enable_dropship_provisioning_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required). | 
 **enable_dropship_provisioning_details** | [**DropshipProvisioningSettingsDetailsRequestV1Model**](DropshipProvisioningSettingsDetailsRequestV1Model.md)| Enable Dropship Provisioning to be saved.(Required). | 

### Return type

[**DropshipProvisioningSettingsDetailsResponseV1Model**](DropshipProvisioningSettingsDetailsResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_dropship_provisioning_v1_get_details_async**
> DropshipProvisioningSettingsDetailsResponseV1Model enable_dropship_provisioning_v1_get_details_async(uuid)

New - Gets dropship provisioning details of a given organization group UUID.

Returns dropship provisioning details of given organization group id and its children.

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
api_instance = systemv1.EnableDropshipProvisioningV1Api(systemv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization group UUID to perform the operation on.(Required).

try:
    # New - Gets dropship provisioning details of a given organization group UUID.
    api_response = api_instance.enable_dropship_provisioning_v1_get_details_async(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnableDropshipProvisioningV1Api->enable_dropship_provisioning_v1_get_details_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required). | 

### Return type

[**DropshipProvisioningSettingsDetailsResponseV1Model**](DropshipProvisioningSettingsDetailsResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

