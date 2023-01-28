# systemv1.TimeZoneV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**time_zone_v1_get_time_zone**](TimeZoneV1Api.md#time_zone_v1_get_time_zone) | **GET** /admin/timezones | New - Gets the list of TimeZones.


# **time_zone_v1_get_time_zone**
> TimeZoneResponseV1Model time_zone_v1_get_time_zone()

New - Gets the list of TimeZones.

Gets the list of supported TimeZones.

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
api_instance = systemv1.TimeZoneV1Api(systemv1.ApiClient(configuration))

try:
    # New - Gets the list of TimeZones.
    api_response = api_instance.time_zone_v1_get_time_zone()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeZoneV1Api->time_zone_v1_get_time_zone: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TimeZoneResponseV1Model**](TimeZoneResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

