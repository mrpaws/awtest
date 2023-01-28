# mdmv4.ProfilesV4Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profiles_v4_get_device_profile_details_async**](ProfilesV4Api.md#profiles_v4_get_device_profile_details_async) | **GET** /profiles/{profileId} | New - Retrive profile details from Profile Id.


# **profiles_v4_get_device_profile_details_async**
> DeviceProfileV4Entity profiles_v4_get_device_profile_details_async(profile_id)

New - Retrive profile details from Profile Id.

Returns the full profile details, including all payloads associated with the profile.

### Example
```python
from __future__ import print_function
import time
import mdmv4
from mdmv4.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv4.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv4.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv4.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv4.ProfilesV4Api(mdmv4.ApiClient(configuration))
profile_id = 56 # int | Profile Id(Required)

try:
    # New - Retrive profile details from Profile Id.
    api_response = api_instance.profiles_v4_get_device_profile_details_async(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV4Api->profiles_v4_get_device_profile_details_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**| Profile Id(Required) | 

### Return type

[**DeviceProfileV4Entity**](DeviceProfileV4Entity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=4, application/xml;version=4

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

