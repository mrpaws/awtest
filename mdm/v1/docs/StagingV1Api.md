# mdmv1.StagingV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**staging_v1_add_staging_bundle_async**](StagingV1Api.md#staging_v1_add_staging_bundle_async) | **POST** /staging | New - Creates a new staging bundle provided valid values are given.
[**staging_v1_delete_staging_bundle**](StagingV1Api.md#staging_v1_delete_staging_bundle) | **DELETE** /staging/{stagingId} | New - Delete the staging package identified by the staging package id provided it is valid.
[**staging_v1_generate_qr_code_pdf_file**](StagingV1Api.md#staging_v1_generate_qr_code_pdf_file) | **POST** /staging/androidwork/qrcodeenrollment | New - Retrieves a QRCode pdf file for Enrollment
[**staging_v1_get_staging_details**](StagingV1Api.md#staging_v1_get_staging_details) | **GET** /staging/{stagingId} | New - Gets the staging bundle identified by the staging package id provided it is valid.
[**staging_v1_retrieve_sideload_staging_file**](StagingV1Api.md#staging_v1_retrieve_sideload_staging_file) | **GET** /staging/{stagingId}/sideload | New - Retrieves a side-load staging zip or tar.gz file
[**staging_v1_update_staging_bundle_async**](StagingV1Api.md#staging_v1_update_staging_bundle_async) | **PUT** /staging | New - Update the already existing staging package.


# **staging_v1_add_staging_bundle_async**
> staging_v1_add_staging_bundle_async(staging_details=staging_details)

New - Creates a new staging bundle provided valid values are given.

Creates a new staging package with the valid values provided.<br>Staging package is used for enrolling a device through barcode scanning or side loading. </br>

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
api_instance = mdmv1.StagingV1Api(mdmv1.ApiClient(configuration))
staging_details = mdmv1.StagingDetailsModel() # StagingDetailsModel | Details of the staging bunlde to be added. (optional)

try:
    # New - Creates a new staging bundle provided valid values are given.
    api_instance.staging_v1_add_staging_bundle_async(staging_details=staging_details)
except ApiException as e:
    print("Exception when calling StagingV1Api->staging_v1_add_staging_bundle_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staging_details** | [**StagingDetailsModel**](StagingDetailsModel.md)| Details of the staging bunlde to be added. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staging_v1_delete_staging_bundle**
> staging_v1_delete_staging_bundle(staging_id)

New - Delete the staging package identified by the staging package id provided it is valid.

The staging will be deleted if identifier of existing staging package is passed.

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
api_instance = mdmv1.StagingV1Api(mdmv1.ApiClient(configuration))
staging_id = 56 # int | Valid staging bundle id.

try:
    # New - Delete the staging package identified by the staging package id provided it is valid.
    api_instance.staging_v1_delete_staging_bundle(staging_id)
except ApiException as e:
    print("Exception when calling StagingV1Api->staging_v1_delete_staging_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staging_id** | **int**| Valid staging bundle id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staging_v1_generate_qr_code_pdf_file**
> Stream staging_v1_generate_qr_code_pdf_file(configure_qr_code_enrollment_model)

New - Retrieves a QRCode pdf file for Enrollment

Retrieves a QRCode pdf file for Enrollment used in Enrollment for Corporate Owned AFW Devices.

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
api_instance = mdmv1.StagingV1Api(mdmv1.ApiClient(configuration))
configure_qr_code_enrollment_model = mdmv1.ConfigureQRCodeEnrollmentModel() # ConfigureQRCodeEnrollmentModel | Configure QRCode Enrollment Model(Required)

try:
    # New - Retrieves a QRCode pdf file for Enrollment
    api_response = api_instance.staging_v1_generate_qr_code_pdf_file(configure_qr_code_enrollment_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StagingV1Api->staging_v1_generate_qr_code_pdf_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configure_qr_code_enrollment_model** | [**ConfigureQRCodeEnrollmentModel**](ConfigureQRCodeEnrollmentModel.md)| Configure QRCode Enrollment Model(Required) | 

### Return type

[**Stream**](Stream.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staging_v1_get_staging_details**
> StagingDetailsModel staging_v1_get_staging_details(staging_id)

New - Gets the staging bundle identified by the staging package id provided it is valid.

Fetch the details of the existing staging package. <br>Staging package is used for enrolling a device through barcode scanning or side loading </br><br>The fetched details include name of package, organization group under which it is managed, Agent package id and manifest actions like Install profile, Uninstall application.</br>

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
api_instance = mdmv1.StagingV1Api(mdmv1.ApiClient(configuration))
staging_id = 56 # int | Valid staging bundle id.

try:
    # New - Gets the staging bundle identified by the staging package id provided it is valid.
    api_response = api_instance.staging_v1_get_staging_details(staging_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StagingV1Api->staging_v1_get_staging_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staging_id** | **int**| Valid staging bundle id. | 

### Return type

[**StagingDetailsModel**](StagingDetailsModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staging_v1_retrieve_sideload_staging_file**
> Stream staging_v1_retrieve_sideload_staging_file(staging_id, organizationgroupid=organizationgroupid, key=key, universal=universal)

New - Retrieves a side-load staging zip or tar.gz file

Retrieves a side-load zip or tar.gz file used for staging a device, installing the agent, installing staging content, and enrolling, used mostly on Rugged devices.

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
api_instance = mdmv1.StagingV1Api(mdmv1.ApiClient(configuration))
staging_id = 56 # int | staging bundle id(Required)
organizationgroupid = 56 # int | organization group id (optional)
key = '' # str | key used to encrypt some of the files in archive (optional) (default to )
universal =  # bool | when staging the device, set to true if you want the end-user to choose the organization group the device will be apart of. (optional) (default to )

try:
    # New - Retrieves a side-load staging zip or tar.gz file
    api_response = api_instance.staging_v1_retrieve_sideload_staging_file(staging_id, organizationgroupid=organizationgroupid, key=key, universal=universal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StagingV1Api->staging_v1_retrieve_sideload_staging_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staging_id** | **int**| staging bundle id(Required) | 
 **organizationgroupid** | **int**| organization group id | [optional] 
 **key** | **str**| key used to encrypt some of the files in archive | [optional] [default to ]
 **universal** | **bool**| when staging the device, set to true if you want the end-user to choose the organization group the device will be apart of. | [optional] [default to ]

### Return type

[**Stream**](Stream.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staging_v1_update_staging_bundle_async**
> staging_v1_update_staging_bundle_async(staging_details=staging_details)

New - Update the already existing staging package.

Updates the details of existing staging package. <br>Staging package is used for enrolling a device through barcode scanning or side loading </br><br>The details include name of package, organization group under which it is managed, Agent package id and manifest actions like Install profile, Uninstall application</br>

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
api_instance = mdmv1.StagingV1Api(mdmv1.ApiClient(configuration))
staging_details = mdmv1.StagingDetailsModel() # StagingDetailsModel | Details of the staging package to be updated. (optional)

try:
    # New - Update the already existing staging package.
    api_instance.staging_v1_update_staging_bundle_async(staging_details=staging_details)
except ApiException as e:
    print("Exception when calling StagingV1Api->staging_v1_update_staging_bundle_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staging_details** | [**StagingDetailsModel**](StagingDetailsModel.md)| Details of the staging package to be updated. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

