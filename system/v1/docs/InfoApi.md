# systemv1.InfoApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_get_info_async**](InfoApi.md#info_get_info_async) | **GET** /info | Retrieves the information of the AirWatch Developer APIs.


# **info_get_info_async**
> ServiceDocument info_get_info_async()

Retrieves the information of the AirWatch Developer APIs.

Provides information about AirWatch version and API URLs. Replaces \"https://{host}/API/v1\" and \"https://{host}/API/v2\".

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

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
api_instance = systemv1.InfoApi(systemv1.ApiClient(configuration))

try:
    # Retrieves the information of the AirWatch Developer APIs.
    api_response = api_instance.info_get_info_async()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->info_get_info_async: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceDocument**](ServiceDocument.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

