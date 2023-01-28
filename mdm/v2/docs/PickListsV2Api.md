# mdmv2.PickListsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pick_lists_v2_get_device_certificate_authorities_async**](PickListsV2Api.md#pick_lists_v2_get_device_certificate_authorities_async) | **GET** /groups/{organizationGroupUuid}/picklists/certificate-authorities | New - Gets the list of Certificate Authorities (CA) for an organization group.


# **pick_lists_v2_get_device_certificate_authorities_async**
> CertificateAuthorityV1Model pick_lists_v2_get_device_certificate_authorities_async(organization_group_uuid)

New - Gets the list of Certificate Authorities (CA) for an organization group.

Retrieves the list of Certificate Authority (CA) for an organization group. In cryptography, a certificate authority is an entity that issues digital certificates. A digital certificate certifies the ownership of a public key by the named subject of the certificate.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.PickListsV2Api(mdmv2.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | The unique identifier of the organization group.(Required).

try:
    # New - Gets the list of Certificate Authorities (CA) for an organization group.
    api_response = api_instance.pick_lists_v2_get_device_certificate_authorities_async(organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickListsV2Api->pick_lists_v2_get_device_certificate_authorities_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| The unique identifier of the organization group.(Required). | 

### Return type

[**CertificateAuthorityV1Model**](CertificateAuthorityV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

