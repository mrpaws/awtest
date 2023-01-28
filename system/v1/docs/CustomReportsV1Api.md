# systemv1.CustomReportsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_reports_v1_get_refresh_token**](CustomReportsV1Api.md#custom_reports_v1_get_refresh_token) | **GET** /customreports/refreshtoken | New - Gets the Custom Reports refresh token for an organization group


# **custom_reports_v1_get_refresh_token**
> CustomReportTokenV1Model custom_reports_v1_get_refresh_token()

New - Gets the Custom Reports refresh token for an organization group

This api generates the Custom Report refresh token valid at the user's topmost Customer Organization Group. The token is valid for 5 minutes.

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
api_instance = systemv1.CustomReportsV1Api(systemv1.ApiClient(configuration))

try:
    # New - Gets the Custom Reports refresh token for an organization group
    api_response = api_instance.custom_reports_v1_get_refresh_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomReportsV1Api->custom_reports_v1_get_refresh_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomReportTokenV1Model**](CustomReportTokenV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

