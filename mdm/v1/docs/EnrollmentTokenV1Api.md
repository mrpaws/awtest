# mdmv1.EnrollmentTokenV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrollment_token_v1_create_async**](EnrollmentTokenV1Api.md#enrollment_token_v1_create_async) | **POST** /groups/{ogUuid}/enrollment-tokens | New - Creates device enrollment token based on registration type
[**enrollment_token_v1_delete_by_id_async**](EnrollmentTokenV1Api.md#enrollment_token_v1_delete_by_id_async) | **DELETE** /groups/{ogUuid}/enrollment-tokens/{tokenUuid} | New - Delete device enrollment token
[**enrollment_token_v1_get_by_criteria_async**](EnrollmentTokenV1Api.md#enrollment_token_v1_get_by_criteria_async) | **GET** /groups/{ogUuid}/enrollment-tokens | New - Returns a list of enrollment tokens that match the search criteria
[**enrollment_token_v1_get_by_id_async**](EnrollmentTokenV1Api.md#enrollment_token_v1_get_by_id_async) | **GET** /groups/{ogUuid}/enrollment-tokens/{tokenUuid} | New - Get device enrollment token details


# **enrollment_token_v1_create_async**
> enrollment_token_v1_create_async(device_registration_record, og_uuid)

New - Creates device enrollment token based on registration type

Creates enrollment token for devices with specific registration type like Blacklist or Whitelist

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.EnrollmentTokenV1Api(mdmv1.ApiClient(configuration))
device_registration_record = mdmv1.EnrollmentTokenRequestV1Model() # EnrollmentTokenRequestV1Model | Device registration record to create token with registration type(Required)
og_uuid = 'og_uuid_example' # str | Organization group UUID(Required)

try:
    # New - Creates device enrollment token based on registration type
    api_instance.enrollment_token_v1_create_async(device_registration_record, og_uuid)
except ApiException as e:
    print("Exception when calling EnrollmentTokenV1Api->enrollment_token_v1_create_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_registration_record** | [**EnrollmentTokenRequestV1Model**](EnrollmentTokenRequestV1Model.md)| Device registration record to create token with registration type(Required) | 
 **og_uuid** | [**str**](.md)| Organization group UUID(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_token_v1_delete_by_id_async**
> enrollment_token_v1_delete_by_id_async(token_uuid, og_uuid)

New - Delete device enrollment token

Delete device enrollment token for provided enrollment token UUID

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.EnrollmentTokenV1Api(mdmv1.ApiClient(configuration))
token_uuid = 'token_uuid_example' # str | Enrollment token UUID(Required)
og_uuid = 'og_uuid_example' # str | Organization group UUID(Required)

try:
    # New - Delete device enrollment token
    api_instance.enrollment_token_v1_delete_by_id_async(token_uuid, og_uuid)
except ApiException as e:
    print("Exception when calling EnrollmentTokenV1Api->enrollment_token_v1_delete_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | [**str**](.md)| Enrollment token UUID(Required) | 
 **og_uuid** | [**str**](.md)| Organization group UUID(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_token_v1_get_by_criteria_async**
> EnrollmentTokenGetByCriteriaResponseModel enrollment_token_v1_get_by_criteria_async(og_uuid, serial_number=serial_number, imei=imei, compliance_status=compliance_status, enrollment_status=enrollment_status, device_type=device_type, page=page, page_size=page_size)

New - Returns a list of enrollment tokens that match the search criteria



### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.EnrollmentTokenV1Api(mdmv1.ApiClient(configuration))
og_uuid = 'og_uuid_example' # str | Organization group UUID.(Required)
serial_number =  # object | Serial number of the device. (optional) (default to )
imei = '' # str | IMEI number of the device (optional) (default to )
compliance_status = '' # str | Compliance status of registration. (optional) (default to )
enrollment_status = '' # str | Enrollment status. (optional) (default to )
device_type = '' # str | Device type (Platform) (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
page_size = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # New - Returns a list of enrollment tokens that match the search criteria
    api_response = api_instance.enrollment_token_v1_get_by_criteria_async(og_uuid, serial_number=serial_number, imei=imei, compliance_status=compliance_status, enrollment_status=enrollment_status, device_type=device_type, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentTokenV1Api->enrollment_token_v1_get_by_criteria_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **og_uuid** | [**str**](.md)| Organization group UUID.(Required) | 
 **serial_number** | [**object**](.md)| Serial number of the device. | [optional] [default to ]
 **imei** | **str**| IMEI number of the device | [optional] [default to ]
 **compliance_status** | **str**| Compliance status of registration. | [optional] [default to ]
 **enrollment_status** | **str**| Enrollment status. | [optional] [default to ]
 **device_type** | **str**| Device type (Platform) | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **page_size** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**EnrollmentTokenGetByCriteriaResponseModel**](EnrollmentTokenGetByCriteriaResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_token_v1_get_by_id_async**
> EnrollmentTokenResponseV1Model enrollment_token_v1_get_by_id_async(token_uuid, og_uuid)

New - Get device enrollment token details

Retrieves device enrollment token for provided enrollment token UUID

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv1.EnrollmentTokenV1Api(mdmv1.ApiClient(configuration))
token_uuid = 'token_uuid_example' # str | Enrollment token UUID(Required)
og_uuid = 'og_uuid_example' # str | Organization group UUID(Required)

try:
    # New - Get device enrollment token details
    api_response = api_instance.enrollment_token_v1_get_by_id_async(token_uuid, og_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentTokenV1Api->enrollment_token_v1_get_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | [**str**](.md)| Enrollment token UUID(Required) | 
 **og_uuid** | [**str**](.md)| Organization group UUID(Required) | 

### Return type

[**EnrollmentTokenResponseV1Model**](EnrollmentTokenResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

