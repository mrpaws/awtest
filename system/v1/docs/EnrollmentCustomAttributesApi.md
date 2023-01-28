# systemv1.EnrollmentCustomAttributesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrollment_custom_attributes_create_custom_attributes_for_reg_devices**](EnrollmentCustomAttributesApi.md#enrollment_custom_attributes_create_custom_attributes_for_reg_devices) | **POST** /users/registereddevices/serialnumber/{serialnumber}/createcustomattributes | Creates multiple new device custom attributes for a registered device.
[**enrollment_custom_attributes_create_custom_attributes_for_reg_devices_by_asset_nr**](EnrollmentCustomAttributesApi.md#enrollment_custom_attributes_create_custom_attributes_for_reg_devices_by_asset_nr) | **POST** /users/registereddevices/assetnumber/{assetnumber}/createcustomattributes | Creates multiple new device custom attributes for a registered device.
[**enrollment_custom_attributes_delete_custom_attributes_for_reg_devices**](EnrollmentCustomAttributesApi.md#enrollment_custom_attributes_delete_custom_attributes_for_reg_devices) | **POST** /users/registereddevices/serialnumber/{serialnumber}/deletecustomattributes | Deletes multiple device custom attribute values for a registered device.
[**enrollment_custom_attributes_delete_custom_attributes_for_reg_devices_by_asset_nr**](EnrollmentCustomAttributesApi.md#enrollment_custom_attributes_delete_custom_attributes_for_reg_devices_by_asset_nr) | **POST** /users/registereddevices/assetnumber/{assetnumber}/deletecustomattributes | Deletes multiple device custom attribute values for a registered device.
[**enrollment_custom_attributes_update_custom_attributes_for_reg_devices**](EnrollmentCustomAttributesApi.md#enrollment_custom_attributes_update_custom_attributes_for_reg_devices) | **POST** /users/registereddevices/serialnumber/{serialnumber}/updatecustomattributes | Updates multiple device custom attribute values for a registered device.
[**enrollment_custom_attributes_update_custom_attributes_for_reg_devices_by_asset_nr**](EnrollmentCustomAttributesApi.md#enrollment_custom_attributes_update_custom_attributes_for_reg_devices_by_asset_nr) | **POST** /users/registereddevices/assetnumber/{assetnumber}/updatecustomattributes | Updates multiple device custom attribute values for a registered device.


# **enrollment_custom_attributes_create_custom_attributes_for_reg_devices**
> BulkResponse enrollment_custom_attributes_create_custom_attributes_for_reg_devices(serialnumber, custom_attributes)

Creates multiple new device custom attributes for a registered device.

Creates new device custom attributes for regisered devices. Device Serial number is used as the key to find the device.

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
api_instance = systemv1.EnrollmentCustomAttributesApi(systemv1.ApiClient(configuration))
serialnumber = 'serialnumber_example' # str | Device Serial number  (Required).
custom_attributes = systemv1.CustomAttributeListModel() # CustomAttributeListModel | An Entity for the custom attributes  (Required).

try:
    # Creates multiple new device custom attributes for a registered device.
    api_response = api_instance.enrollment_custom_attributes_create_custom_attributes_for_reg_devices(serialnumber, custom_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentCustomAttributesApi->enrollment_custom_attributes_create_custom_attributes_for_reg_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialnumber** | **str**| Device Serial number  (Required). | 
 **custom_attributes** | [**CustomAttributeListModel**](CustomAttributeListModel.md)| An Entity for the custom attributes  (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_custom_attributes_create_custom_attributes_for_reg_devices_by_asset_nr**
> BulkResponse enrollment_custom_attributes_create_custom_attributes_for_reg_devices_by_asset_nr(assetnumber, custom_attributes)

Creates multiple new device custom attributes for a registered device.

Creates new device custom attributes for regisered devices. Device Asset number is used as the key to find the device.

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
api_instance = systemv1.EnrollmentCustomAttributesApi(systemv1.ApiClient(configuration))
assetnumber = 'assetnumber_example' # str | Device Asset number (Required).
custom_attributes = systemv1.CustomAttributeListModel() # CustomAttributeListModel | An Entity for the custom attributes (Required).

try:
    # Creates multiple new device custom attributes for a registered device.
    api_response = api_instance.enrollment_custom_attributes_create_custom_attributes_for_reg_devices_by_asset_nr(assetnumber, custom_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentCustomAttributesApi->enrollment_custom_attributes_create_custom_attributes_for_reg_devices_by_asset_nr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetnumber** | **str**| Device Asset number (Required). | 
 **custom_attributes** | [**CustomAttributeListModel**](CustomAttributeListModel.md)| An Entity for the custom attributes (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_custom_attributes_delete_custom_attributes_for_reg_devices**
> BulkResponse enrollment_custom_attributes_delete_custom_attributes_for_reg_devices(serialnumber, custom_attributes)

Deletes multiple device custom attribute values for a registered device.

Deletes device custom attributes for a regisered device. Device Serial number is used as the key to find the device.

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
api_instance = systemv1.EnrollmentCustomAttributesApi(systemv1.ApiClient(configuration))
serialnumber = 'serialnumber_example' # str | Device Serial number (Required).
custom_attributes = systemv1.CustomAttributeListModel() # CustomAttributeListModel | An Entity for the custom attributes (Required).

try:
    # Deletes multiple device custom attribute values for a registered device.
    api_response = api_instance.enrollment_custom_attributes_delete_custom_attributes_for_reg_devices(serialnumber, custom_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentCustomAttributesApi->enrollment_custom_attributes_delete_custom_attributes_for_reg_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialnumber** | **str**| Device Serial number (Required). | 
 **custom_attributes** | [**CustomAttributeListModel**](CustomAttributeListModel.md)| An Entity for the custom attributes (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_custom_attributes_delete_custom_attributes_for_reg_devices_by_asset_nr**
> BulkResponse enrollment_custom_attributes_delete_custom_attributes_for_reg_devices_by_asset_nr(assetnumber, custom_attributes)

Deletes multiple device custom attribute values for a registered device.

Deletes device custom attributes for a regisered device. Device asset number is used as the key to find the device.

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
api_instance = systemv1.EnrollmentCustomAttributesApi(systemv1.ApiClient(configuration))
assetnumber = 'assetnumber_example' # str | Device asset number (Required).
custom_attributes = systemv1.CustomAttributeListModel() # CustomAttributeListModel | An Entity for the custom attributes (Required).

try:
    # Deletes multiple device custom attribute values for a registered device.
    api_response = api_instance.enrollment_custom_attributes_delete_custom_attributes_for_reg_devices_by_asset_nr(assetnumber, custom_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentCustomAttributesApi->enrollment_custom_attributes_delete_custom_attributes_for_reg_devices_by_asset_nr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetnumber** | **str**| Device asset number (Required). | 
 **custom_attributes** | [**CustomAttributeListModel**](CustomAttributeListModel.md)| An Entity for the custom attributes (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_custom_attributes_update_custom_attributes_for_reg_devices**
> BulkResponse enrollment_custom_attributes_update_custom_attributes_for_reg_devices(serialnumber, custom_attributes)

Updates multiple device custom attribute values for a registered device.

Updates device custom attributes for a regisered device. Device Serial number is used as the key to find the device.

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
api_instance = systemv1.EnrollmentCustomAttributesApi(systemv1.ApiClient(configuration))
serialnumber = 'serialnumber_example' # str | Device Serial number  (Required).
custom_attributes = systemv1.CustomAttributeListModel() # CustomAttributeListModel | An Entity for the custom attributes  (Required).

try:
    # Updates multiple device custom attribute values for a registered device.
    api_response = api_instance.enrollment_custom_attributes_update_custom_attributes_for_reg_devices(serialnumber, custom_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentCustomAttributesApi->enrollment_custom_attributes_update_custom_attributes_for_reg_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialnumber** | **str**| Device Serial number  (Required). | 
 **custom_attributes** | [**CustomAttributeListModel**](CustomAttributeListModel.md)| An Entity for the custom attributes  (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_custom_attributes_update_custom_attributes_for_reg_devices_by_asset_nr**
> BulkResponse enrollment_custom_attributes_update_custom_attributes_for_reg_devices_by_asset_nr(assetnumber, custom_attributes)

Updates multiple device custom attribute values for a registered device.

Updates device custom attributes for a regisered device. Device asset number is used as the key to find the device.

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
api_instance = systemv1.EnrollmentCustomAttributesApi(systemv1.ApiClient(configuration))
assetnumber = 'assetnumber_example' # str | Device asset number (Required).
custom_attributes = systemv1.CustomAttributeListModel() # CustomAttributeListModel | An Entity for the custom attributes (Required).

try:
    # Updates multiple device custom attribute values for a registered device.
    api_response = api_instance.enrollment_custom_attributes_update_custom_attributes_for_reg_devices_by_asset_nr(assetnumber, custom_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentCustomAttributesApi->enrollment_custom_attributes_update_custom_attributes_for_reg_devices_by_asset_nr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetnumber** | **str**| Device asset number (Required). | 
 **custom_attributes** | [**CustomAttributeListModel**](CustomAttributeListModel.md)| An Entity for the custom attributes (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

