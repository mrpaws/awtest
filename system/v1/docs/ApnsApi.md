# systemv1.ApnsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apns_apns_certificate**](ApnsApi.md#apns_apns_certificate) | **GET** /groups/{id}/apns | Method to Create APNs Certificate Request.
[**apns_save_apns_certificate**](ApnsApi.md#apns_save_apns_certificate) | **POST** /groups/{id}/apns | Method to Save the APNs Configuration for an Organization Group.
[**apns_update_apns_certificate**](ApnsApi.md#apns_update_apns_certificate) | **PATCH** /groups/{id}/apns | New - Update the APNs Configuration for an Organization Group.


# **apns_apns_certificate**
> ApnsSetupModel_ apns_apns_certificate(id, force=force)

Method to Create APNs Certificate Request.

Returns the status of the APNs Configuration for an Organization Group.  Upload certificate Blob Id is -1 when APNs is already Configured for the Organization Group.

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
api_instance = systemv1.ApnsApi(systemv1.ApiClient(configuration))
id = 56 # int | This is the Organization Group Identifier also known as GroupID. Typically used during enrollment (Required).
force =  # bool | Option to force generate APNs Cert Request. (optional) (default to )

try:
    # Method to Create APNs Certificate Request.
    api_response = api_instance.apns_apns_certificate(id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApnsApi->apns_apns_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| This is the Organization Group Identifier also known as GroupID. Typically used during enrollment (Required). | 
 **force** | **bool**| Option to force generate APNs Cert Request. | [optional] [default to ]

### Return type

[**ApnsSetupModel_**](ApnsSetupModel_.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apns_save_apns_certificate**
> apns_save_apns_certificate(apns_setup_model, id)

Method to Save the APNs Configuration for an Organization Group.

This endpoint is applicable after the APNs certificate Blob(.pem) is uploaded to the AirWatch server.

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
api_instance = systemv1.ApnsApi(systemv1.ApiClient(configuration))
apns_setup_model = systemv1.ApnsSetupModel_() # ApnsSetupModel_ | Parameter for APNs Setup Model (Required).
id = 56 # int | This is the Organization Group Identifier also known as GroupID. Typically used during enrollment (Required).

try:
    # Method to Save the APNs Configuration for an Organization Group.
    api_instance.apns_save_apns_certificate(apns_setup_model, id)
except ApiException as e:
    print("Exception when calling ApnsApi->apns_save_apns_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apns_setup_model** | [**ApnsSetupModel_**](ApnsSetupModel_.md)| Parameter for APNs Setup Model (Required). | 
 **id** | **int**| This is the Organization Group Identifier also known as GroupID. Typically used during enrollment (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apns_update_apns_certificate**
> apns_update_apns_certificate(id, apns_configuration_model=apns_configuration_model)

New - Update the APNs Configuration for an Organization Group.

This endpoint is applicable after APNs is configured on the AirWatch server.

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
api_instance = systemv1.ApnsApi(systemv1.ApiClient(configuration))
id = 56 # int | The OrganizationGroup Identifier (Required).
apns_configuration_model = systemv1.ApnsConfigurationModel() # ApnsConfigurationModel | Parameter for APNs Configuration Model. (optional)

try:
    # New - Update the APNs Configuration for an Organization Group.
    api_instance.apns_update_apns_certificate(id, apns_configuration_model=apns_configuration_model)
except ApiException as e:
    print("Exception when calling ApnsApi->apns_update_apns_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The OrganizationGroup Identifier (Required). | 
 **apns_configuration_model** | [**ApnsConfigurationModel**](ApnsConfigurationModel.md)| Parameter for APNs Configuration Model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

