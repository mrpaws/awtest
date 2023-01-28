# mdmv1.PoliciesV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policies_v1_post_async**](PoliciesV1Api.md#policies_v1_post_async) | **POST** /android-oem-integration/policies/organization-groups/{organizationGroupUuid} | New - Create an Android Update Policy.


# **policies_v1_post_async**
> CreatePolicyResponseV1Model policies_v1_post_async(organization_group_uuid, policy_request)

New - Create an Android Update Policy.

Create an Android Update Policy.

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
api_instance = mdmv1.PoliciesV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Unique identifier for organization group.(Required)
policy_request = mdmv1.PolicyV1Model() # PolicyV1Model | The policy request model.(Required).

try:
    # New - Create an Android Update Policy.
    api_response = api_instance.policies_v1_post_async(organization_group_uuid, policy_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesV1Api->policies_v1_post_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Unique identifier for organization group.(Required) | 
 **policy_request** | [**PolicyV1Model**](PolicyV1Model.md)| The policy request model.(Required). | 

### Return type

[**CreatePolicyResponseV1Model**](CreatePolicyResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

