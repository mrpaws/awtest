# mamv2.PurchasedAppsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchased_apps_v2_get_purchased_application_and_assignments**](PurchasedAppsV2Api.md#purchased_apps_v2_get_purchased_application_and_assignments) | **GET** /apps/purchased/{uuid} | New - Get purchased application and assignment details


# **purchased_apps_v2_get_purchased_application_and_assignments**
> PurchasedApplicationV2Model purchased_apps_v2_get_purchased_application_and_assignments(uuid)

New - Get purchased application and assignment details

Retrieve the details of a license-based purchased application and its assignments.

### Example
```python
from __future__ import print_function
import time
import mamv2
from mamv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv2.PurchasedAppsV2Api(mamv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Purchased application's UUID(Required)

try:
    # New - Get purchased application and assignment details
    api_response = api_instance.purchased_apps_v2_get_purchased_application_and_assignments(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasedAppsV2Api->purchased_apps_v2_get_purchased_application_and_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Purchased application&#39;s UUID(Required) | 

### Return type

[**PurchasedApplicationV2Model**](PurchasedApplicationV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

