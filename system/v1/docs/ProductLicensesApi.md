# systemv1.ProductLicensesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_licenses_get_product_licenses_async**](ProductLicensesApi.md#product_licenses_get_product_licenses_async) | **GET** /groups/{organizationGroupUuid}/licenses | New - Returns the list of product licenses associated with the given organization group.


# **product_licenses_get_product_licenses_async**
> ProductLicenseResponseV1Model product_licenses_get_product_licenses_async(organization_group_uuid)

New - Returns the list of product licenses associated with the given organization group.



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

# create an instance of the API class
api_instance = systemv1.ProductLicensesApi(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | The unique identifier of the organization group.(Required).

try:
    # New - Returns the list of product licenses associated with the given organization group.
    api_response = api_instance.product_licenses_get_product_licenses_async(organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLicensesApi->product_licenses_get_product_licenses_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| The unique identifier of the organization group.(Required). | 

### Return type

[**ProductLicenseResponseV1Model**](ProductLicenseResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

