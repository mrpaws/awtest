# mdmv2.EnrollmentTokenV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrollment_token_v2_create_enrollment_token**](EnrollmentTokenV2Api.md#enrollment_token_v2_create_enrollment_token) | **POST** /groups/{ogUuid}/enrollment-tokens | New - Creates device enrollment token based on registration type


# **enrollment_token_v2_create_enrollment_token**
> RegisteredDeviceResponseV2Model enrollment_token_v2_create_enrollment_token(device_registration_record, og_uuid)

New - Creates device enrollment token based on registration type

Creates enrollment token for devices with specific registration type like Blacklist or Whitelist or RegisterDevice. Only for message type as QRCODE in register device record it returns the QR Code Data URI as response

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
api_instance = mdmv2.EnrollmentTokenV2Api(mdmv2.ApiClient(configuration))
device_registration_record = mdmv2.EnrollmentTokenRequestV2Model() # EnrollmentTokenRequestV2Model | Device registration record to create token with registration type(Required)
og_uuid = 'og_uuid_example' # str | Organization group UUID(Required)

try:
    # New - Creates device enrollment token based on registration type
    api_response = api_instance.enrollment_token_v2_create_enrollment_token(device_registration_record, og_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentTokenV2Api->enrollment_token_v2_create_enrollment_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_registration_record** | [**EnrollmentTokenRequestV2Model**](EnrollmentTokenRequestV2Model.md)| Device registration record to create token with registration type(Required) | 
 **og_uuid** | [**str**](.md)| Organization group UUID(Required) | 

### Return type

[**RegisteredDeviceResponseV2Model**](RegisteredDeviceResponseV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

