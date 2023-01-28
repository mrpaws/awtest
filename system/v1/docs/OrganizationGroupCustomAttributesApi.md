# systemv1.OrganizationGroupCustomAttributesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_group_custom_attributes_get_custom_attributes_by_og_id**](OrganizationGroupCustomAttributesApi.md#organization_group_custom_attributes_get_custom_attributes_by_og_id) | **GET** /groups/{ogid}/customattributes | Gets Custom Attribute Details.


# **organization_group_custom_attributes_get_custom_attributes_by_og_id**
> GetCustomAttributeResult organization_group_custom_attributes_get_custom_attributes_by_og_id(ogid)

Gets Custom Attribute Details.

Gets Custom Attribute Details for the specified Organization Group.

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
api_instance = systemv1.OrganizationGroupCustomAttributesApi(systemv1.ApiClient(configuration))
ogid = 56 # int | The OrganizationGroup Identifier (Required).

try:
    # Gets Custom Attribute Details.
    api_response = api_instance.organization_group_custom_attributes_get_custom_attributes_by_og_id(ogid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationGroupCustomAttributesApi->organization_group_custom_attributes_get_custom_attributes_by_og_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ogid** | **int**| The OrganizationGroup Identifier (Required). | 

### Return type

[**GetCustomAttributeResult**](GetCustomAttributeResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

