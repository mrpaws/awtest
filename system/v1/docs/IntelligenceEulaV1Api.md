# systemv1.IntelligenceEulaV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**intelligence_eula_v1_accept_eula_async**](IntelligenceEulaV1Api.md#intelligence_eula_v1_accept_eula_async) | **POST** /groups/{organizationGroupUuid}/intelligence/accept-eula | New - Accept intelligence EULA details.
[**intelligence_eula_v1_get_eula_async**](IntelligenceEulaV1Api.md#intelligence_eula_v1_get_eula_async) | **GET** /groups/{organizationGroupUuid}/intelligence/eula | New - Gets EULA for Intelligence of given organization group.


# **intelligence_eula_v1_accept_eula_async**
> intelligence_eula_v1_accept_eula_async(organization_group_uuid, intelligence_eula)

New - Accept intelligence EULA details.



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
api_instance = systemv1.IntelligenceEulaV1Api(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Identifier of an Organization Group(Required).
intelligence_eula = systemv1.IntelligenceEulaModelV1() # IntelligenceEulaModelV1 | Intelligence eula acceptance model(Required).

try:
    # New - Accept intelligence EULA details.
    api_instance.intelligence_eula_v1_accept_eula_async(organization_group_uuid, intelligence_eula)
except ApiException as e:
    print("Exception when calling IntelligenceEulaV1Api->intelligence_eula_v1_accept_eula_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Identifier of an Organization Group(Required). | 
 **intelligence_eula** | [**IntelligenceEulaModelV1**](IntelligenceEulaModelV1.md)| Intelligence eula acceptance model(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intelligence_eula_v1_get_eula_async**
> IntelligenceEulaModelV1 intelligence_eula_v1_get_eula_async(organization_group_uuid)

New - Gets EULA for Intelligence of given organization group.

Gets EULA for Intelligence of given organization group.

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
api_instance = systemv1.IntelligenceEulaV1Api(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | The unique identifier of the organization group.(Required).

try:
    # New - Gets EULA for Intelligence of given organization group.
    api_response = api_instance.intelligence_eula_v1_get_eula_async(organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceEulaV1Api->intelligence_eula_v1_get_eula_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| The unique identifier of the organization group.(Required). | 

### Return type

[**IntelligenceEulaModelV1**](IntelligenceEulaModelV1.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

