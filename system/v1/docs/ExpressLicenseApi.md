# systemv1.ExpressLicenseApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**express_license_create_license_async**](ExpressLicenseApi.md#express_license_create_license_async) | **POST** /expresslicenses | New - Creates specific number of aw express licenses at given organization group.


# **express_license_create_license_async**
> express_license_create_license_async(license_model)

New - Creates specific number of aw express licenses at given organization group.

Creates specific number of airwatch express licenses at given organization group.

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
api_instance = systemv1.ExpressLicenseApi(systemv1.ApiClient(configuration))
license_model = systemv1.LicenseModel() # LicenseModel | License details to be added. (Required).

try:
    # New - Creates specific number of aw express licenses at given organization group.
    api_instance.express_license_create_license_async(license_model)
except ApiException as e:
    print("Exception when calling ExpressLicenseApi->express_license_create_license_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_model** | [**LicenseModel**](LicenseModel.md)| License details to be added. (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

