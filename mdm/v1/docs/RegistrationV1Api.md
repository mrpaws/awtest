# mdmv1.RegistrationV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registration_v1_complete_registration_async**](RegistrationV1Api.md#registration_v1_complete_registration_async) | **PATCH** /android-oem-integration/registration/organization-groups/{organizationGroupUuid}/zebra | New - Complete authorization, retrieve and store access and refresh tokens for the tenant.
[**registration_v1_delete_registration_async**](RegistrationV1Api.md#registration_v1_delete_registration_async) | **DELETE** /android-oem-integration/registration/organization-groups/{organizationGroupUuid}/zebra | New - Delete registration for specified tenant.
[**registration_v1_initiate_registration_async**](RegistrationV1Api.md#registration_v1_initiate_registration_async) | **POST** /android-oem-integration/registration/organization-groups/{organizationGroupUuid}/zebra | New - Registration with zebra data services.


# **registration_v1_complete_registration_async**
> registration_v1_complete_registration_async(organization_group_uuid)

New - Complete authorization, retrieve and store access and refresh tokens for the tenant.

Complete authorization, retrieve and store access and refresh tokens for the tenant.

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
api_instance = mdmv1.RegistrationV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Unique identifier for organization group.(Required).

try:
    # New - Complete authorization, retrieve and store access and refresh tokens for the tenant.
    api_instance.registration_v1_complete_registration_async(organization_group_uuid)
except ApiException as e:
    print("Exception when calling RegistrationV1Api->registration_v1_complete_registration_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Unique identifier for organization group.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_v1_delete_registration_async**
> registration_v1_delete_registration_async(organization_group_uuid)

New - Delete registration for specified tenant.

Deletes the registration records for the tenant if registration exists.

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
api_instance = mdmv1.RegistrationV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Unique identifier for organization group.(Required).

try:
    # New - Delete registration for specified tenant.
    api_instance.registration_v1_delete_registration_async(organization_group_uuid)
except ApiException as e:
    print("Exception when calling RegistrationV1Api->registration_v1_delete_registration_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Unique identifier for organization group.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_v1_initiate_registration_async**
> ZebraRegistrationResponseV1Model registration_v1_initiate_registration_async(organization_group_uuid, registration_request)

New - Registration with zebra data services.

Initiate the registration with zebra data services.

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
api_instance = mdmv1.RegistrationV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Unique identifier for organization group.(Required).
registration_request = mdmv1.ZebraRegistrationRequestV1Model() # ZebraRegistrationRequestV1Model | The registration request model.(Required).

try:
    # New - Registration with zebra data services.
    api_response = api_instance.registration_v1_initiate_registration_async(organization_group_uuid, registration_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationV1Api->registration_v1_initiate_registration_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Unique identifier for organization group.(Required). | 
 **registration_request** | [**ZebraRegistrationRequestV1Model**](ZebraRegistrationRequestV1Model.md)| The registration request model.(Required). | 

### Return type

[**ZebraRegistrationResponseV1Model**](ZebraRegistrationResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

