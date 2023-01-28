# mdmv1.OemEnrollmentTokenV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oem_enrollment_token_v1_get_enrollment_token_async**](OemEnrollmentTokenV1Api.md#oem_enrollment_token_v1_get_enrollment_token_async) | **GET** /android-oem-integration/enrollment-token/organization-groups/{organizationGroupUuid}/zebra | New - Retrieves the enrollment token for the tenant.


# **oem_enrollment_token_v1_get_enrollment_token_async**
> ZebraEnrollmentTokenResponseV1Model oem_enrollment_token_v1_get_enrollment_token_async(organization_group_uuid)

New - Retrieves the enrollment token for the tenant.

Gets the enrollment token and its expiration time for the given tenant.

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
api_instance = mdmv1.OemEnrollmentTokenV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Unique identifier of organization group.(Required).

try:
    # New - Retrieves the enrollment token for the tenant.
    api_response = api_instance.oem_enrollment_token_v1_get_enrollment_token_async(organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OemEnrollmentTokenV1Api->oem_enrollment_token_v1_get_enrollment_token_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Unique identifier of organization group.(Required). | 

### Return type

[**ZebraEnrollmentTokenResponseV1Model**](ZebraEnrollmentTokenResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

