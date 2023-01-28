# systemv1.DeviceRegistrationV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_registration_v1_delete_registered_devices**](DeviceRegistrationV1Api.md#device_registration_v1_delete_registered_devices) | **POST** /users/registereddevices/delete | Delete the registered devices.
[**device_registration_v1_delete_registered_devices_by_asset_number**](DeviceRegistrationV1Api.md#device_registration_v1_delete_registered_devices_by_asset_number) | **POST** /users/registereddevices/deletebyassetnumber | Deletes the registered devices identified by Asset number.
[**device_registration_v1_delete_registered_devices_by_serial_number**](DeviceRegistrationV1Api.md#device_registration_v1_delete_registered_devices_by_serial_number) | **POST** /users/registereddevices/deletebyserialnumber | Deletes the registered devices identified by serial number.
[**device_registration_v1_delete_registered_devices_by_udid**](DeviceRegistrationV1Api.md#device_registration_v1_delete_registered_devices_by_udid) | **POST** /users/registereddevices/deletebyudid | Deletes the registered devices identified by UDID.
[**device_registration_v1_enrollment_token_search**](DeviceRegistrationV1Api.md#device_registration_v1_enrollment_token_search) | **GET** /users/enrollmenttoken/search | Search for Enrollment Token and Device details.
[**device_registration_v1_register_device_for_user_async**](DeviceRegistrationV1Api.md#device_registration_v1_register_device_for_user_async) | **POST** /users/{id}/registerdevice | Register a device to enrollment user.
[**device_registration_v1_retrieve_enrolled_devices**](DeviceRegistrationV1Api.md#device_registration_v1_retrieve_enrolled_devices) | **GET** /users/enrolleddevices/search | Retrieves enrolled device details.
[**device_registration_v1_retrieve_registered_devices**](DeviceRegistrationV1Api.md#device_registration_v1_retrieve_registered_devices) | **GET** /users/registereddevices/search | Retrieves registered device details.


# **device_registration_v1_delete_registered_devices**
> BulkResponse device_registration_v1_delete_registered_devices(http_request, searchby, bulk_input=bulk_input, username=username)

Delete the registered devices.

Delete the registered devices identified by [Asset number] or [Udid] or [Serialnumber]              (Formats: Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: RZ1G124JZ6W, AssetNumber: ea856771ba6277bfca16528a79c5ce1f).

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
api_instance = systemv1.DeviceRegistrationV1Api(systemv1.ApiClient(configuration))
http_request = {'key': 'http_request_example'} # dict(str, str) | Holds request entity coming through call pipeline.
searchby = '' # str | The identifier type must be one of the following [ Udid, Serialnumber, AssetNumber](Required). (default to )
bulk_input = systemv1.BulkInput() # BulkInput | List of devices identified by Asset number/Udid/SerialNumber. (optional)
username = '' # str | User name with which the device is enrolled. (optional) (default to )

try:
    # Delete the registered devices.
    api_response = api_instance.device_registration_v1_delete_registered_devices(http_request, searchby, bulk_input=bulk_input, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceRegistrationV1Api->device_registration_v1_delete_registered_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **http_request** | [**dict(str, str)**](str.md)| Holds request entity coming through call pipeline. | 
 **searchby** | **str**| The identifier type must be one of the following [ Udid, Serialnumber, AssetNumber](Required). | [default to ]
 **bulk_input** | [**BulkInput**](BulkInput.md)| List of devices identified by Asset number/Udid/SerialNumber. | [optional] 
 **username** | **str**| User name with which the device is enrolled. | [optional] [default to ]

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_registration_v1_delete_registered_devices_by_asset_number**
> device_registration_v1_delete_registered_devices_by_asset_number(bulk_input=bulk_input)

Deletes the registered devices identified by Asset number.

v1.

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
api_instance = systemv1.DeviceRegistrationV1Api(systemv1.ApiClient(configuration))
bulk_input = systemv1.BulkInput() # BulkInput | List of devices identified by Asset number. (optional)

try:
    # Deletes the registered devices identified by Asset number.
    api_instance.device_registration_v1_delete_registered_devices_by_asset_number(bulk_input=bulk_input)
except ApiException as e:
    print("Exception when calling DeviceRegistrationV1Api->device_registration_v1_delete_registered_devices_by_asset_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| List of devices identified by Asset number. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_registration_v1_delete_registered_devices_by_serial_number**
> device_registration_v1_delete_registered_devices_by_serial_number(bulk_input=bulk_input)

Deletes the registered devices identified by serial number.

v1.

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
api_instance = systemv1.DeviceRegistrationV1Api(systemv1.ApiClient(configuration))
bulk_input = systemv1.BulkInput() # BulkInput | List of devices identified by serial number. (optional)

try:
    # Deletes the registered devices identified by serial number.
    api_instance.device_registration_v1_delete_registered_devices_by_serial_number(bulk_input=bulk_input)
except ApiException as e:
    print("Exception when calling DeviceRegistrationV1Api->device_registration_v1_delete_registered_devices_by_serial_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| List of devices identified by serial number. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_registration_v1_delete_registered_devices_by_udid**
> device_registration_v1_delete_registered_devices_by_udid(bulk_input=bulk_input)

Deletes the registered devices identified by UDID.

v1.

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
api_instance = systemv1.DeviceRegistrationV1Api(systemv1.ApiClient(configuration))
bulk_input = systemv1.BulkInput() # BulkInput | List of devices identified by UDID. (optional)

try:
    # Deletes the registered devices identified by UDID.
    api_instance.device_registration_v1_delete_registered_devices_by_udid(bulk_input=bulk_input)
except ApiException as e:
    print("Exception when calling DeviceRegistrationV1Api->device_registration_v1_delete_registered_devices_by_udid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| List of devices identified by UDID. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_registration_v1_enrollment_token_search**
> EnrollmentTokensModel device_registration_v1_enrollment_token_search(username=username, userid=userid, organizationgroupid=organizationgroupid, organizationgroup=organizationgroup, serialnumber=serialnumber, assetnumber=assetnumber, enrollmentstatusid=enrollmentstatusid, compliancestatusid=compliancestatusid)

Search for Enrollment Token and Device details.

Search for Enrollment Token and Device details using the query information provided.

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
api_instance = systemv1.DeviceRegistrationV1Api(systemv1.ApiClient(configuration))
username = '' # str | UserName of the Enrollment User for whom Enrollment Tokens needs to be searched. (optional) (default to )
userid = 56 # int | Identifier of the Enrollment User for whom Enrollment Tokens needs to be searched. (optional)
organizationgroupid = 56 # int | Identifier of the Organization Group where Enrollment Tokens needs to be searched. (optional)
organizationgroup = '' # str | Organization Group Name where Enrollment Tokens needs to be searched. (optional) (default to )
serialnumber = '' # str | Serial number of device for which Enrollment Tokens to be retrieved. Eg:RZ1G124JZ6W. (optional) (default to )
assetnumber = '' # str | Asset Number of device for which Enrollment Tokens to be retrieved.  Eg:ea856771ba6277bfca16528a79c5ce1f. (optional) (default to )
enrollmentstatusid = 56 # int | EnrollmentStatusID of device for which Enrollment Tokens to be retrieved. (optional)
compliancestatusid = 56 # int | ComplianceStatus of device for which Enrollment Tokens to be retrieved. (optional)

try:
    # Search for Enrollment Token and Device details.
    api_response = api_instance.device_registration_v1_enrollment_token_search(username=username, userid=userid, organizationgroupid=organizationgroupid, organizationgroup=organizationgroup, serialnumber=serialnumber, assetnumber=assetnumber, enrollmentstatusid=enrollmentstatusid, compliancestatusid=compliancestatusid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceRegistrationV1Api->device_registration_v1_enrollment_token_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| UserName of the Enrollment User for whom Enrollment Tokens needs to be searched. | [optional] [default to ]
 **userid** | **int**| Identifier of the Enrollment User for whom Enrollment Tokens needs to be searched. | [optional] 
 **organizationgroupid** | **int**| Identifier of the Organization Group where Enrollment Tokens needs to be searched. | [optional] 
 **organizationgroup** | **str**| Organization Group Name where Enrollment Tokens needs to be searched. | [optional] [default to ]
 **serialnumber** | **str**| Serial number of device for which Enrollment Tokens to be retrieved. Eg:RZ1G124JZ6W. | [optional] [default to ]
 **assetnumber** | **str**| Asset Number of device for which Enrollment Tokens to be retrieved.  Eg:ea856771ba6277bfca16528a79c5ce1f. | [optional] [default to ]
 **enrollmentstatusid** | **int**| EnrollmentStatusID of device for which Enrollment Tokens to be retrieved. | [optional] 
 **compliancestatusid** | **int**| ComplianceStatus of device for which Enrollment Tokens to be retrieved. | [optional] 

### Return type

[**EnrollmentTokensModel**](EnrollmentTokensModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_registration_v1_register_device_for_user_async**
> device_registration_v1_register_device_for_user_async(id, register_device_details=register_device_details)

Register a device to enrollment user.

Register a device to the specified enrollment user.

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
api_instance = systemv1.DeviceRegistrationV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The enrollment user Id.
register_device_details = systemv1.RegisterDeviceDetailsModel() # RegisterDeviceDetailsModel | The device details to register. (optional)

try:
    # Register a device to enrollment user.
    api_instance.device_registration_v1_register_device_for_user_async(id, register_device_details=register_device_details)
except ApiException as e:
    print("Exception when calling DeviceRegistrationV1Api->device_registration_v1_register_device_for_user_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The enrollment user Id. | 
 **register_device_details** | [**RegisterDeviceDetailsModel**](RegisterDeviceDetailsModel.md)| The device details to register. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_registration_v1_retrieve_enrolled_devices**
> EnrolledDevices device_registration_v1_retrieve_enrolled_devices(organizationgroupid=organizationgroupid, organizationgroup=organizationgroup, platform=platform, customattributes=customattributes, serialnumber=serialnumber, seensince=seensince, seentill=seentill, enrolledsince=enrolledsince, enrolledtill=enrolledtill)

Retrieves enrolled device details.

Retrieves enrolled device details for the query information provided in the request              <br />              *seensince, seentill, enrolledsince and enrolledtill* fields accept the following              Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,              yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,              yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = systemv1.DeviceRegistrationV1Api(systemv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization Group Identifier in which device details will be retrieved. (optional)
organizationgroup = '' # str | Organization Group Name search parameter in which device details will be retrieved. (optional) (default to )
platform = '' # str | Platform filter for the device details to be retrieved. (optional) (default to )
customattributes = '' # str | List of custom attribute names [separated by comma (,)] for which values should be returned. (optional) (default to )
serialnumber = '' # str | Device serialnumber for which values should be returned. (optional) (default to )
seensince = '' # datetime | SeenSince DateTime, devices registered after the seensince datetime will be returned if present. (optional) (default to )
seentill = '' # datetime | SeenTill DateTime, devices registered till the seentill datetime will be returned if present. (optional) (default to )
enrolledsince = '' # datetime | EnrolledSince DateTime, devices enrolled after the enrolledsince datetime will be returned if present. (optional) (default to )
enrolledtill = '' # datetime | EnrolledTill DateTime, devices enrolled till the enrolledtill datetime will be returned if present. (optional) (default to )

try:
    # Retrieves enrolled device details.
    api_response = api_instance.device_registration_v1_retrieve_enrolled_devices(organizationgroupid=organizationgroupid, organizationgroup=organizationgroup, platform=platform, customattributes=customattributes, serialnumber=serialnumber, seensince=seensince, seentill=seentill, enrolledsince=enrolledsince, enrolledtill=enrolledtill)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceRegistrationV1Api->device_registration_v1_retrieve_enrolled_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization Group Identifier in which device details will be retrieved. | [optional] 
 **organizationgroup** | **str**| Organization Group Name search parameter in which device details will be retrieved. | [optional] [default to ]
 **platform** | **str**| Platform filter for the device details to be retrieved. | [optional] [default to ]
 **customattributes** | **str**| List of custom attribute names [separated by comma (,)] for which values should be returned. | [optional] [default to ]
 **serialnumber** | **str**| Device serialnumber for which values should be returned. | [optional] [default to ]
 **seensince** | **datetime**| SeenSince DateTime, devices registered after the seensince datetime will be returned if present. | [optional] [default to ]
 **seentill** | **datetime**| SeenTill DateTime, devices registered till the seentill datetime will be returned if present. | [optional] [default to ]
 **enrolledsince** | **datetime**| EnrolledSince DateTime, devices enrolled after the enrolledsince datetime will be returned if present. | [optional] [default to ]
 **enrolledtill** | **datetime**| EnrolledTill DateTime, devices enrolled till the enrolledtill datetime will be returned if present. | [optional] [default to ]

### Return type

[**EnrolledDevices**](EnrolledDevices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_registration_v1_retrieve_registered_devices**
> RegisteredDevices device_registration_v1_retrieve_registered_devices(organizationgroupid=organizationgroupid, organizationgroup=organizationgroup, platform=platform, customattributes=customattributes, assetnumber=assetnumber, seensince=seensince, seentill=seentill)

Retrieves registered device details.

Retrieves registered device details for the query information provided in the request              <br />              *seensince and seentill* fields accept the following              Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,              yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,              yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = systemv1.DeviceRegistrationV1Api(systemv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization Group Identifier in which device details will be retrieved. (optional)
organizationgroup = '' # str | Organization Group Name search parameter in which device details will be retrieved. (optional) (default to )
platform = '' # str | Platform filter for the device details to be retrieved. (optional) (default to )
customattributes = '' # str | List of custom attribute names [separated by comma (,)] for which values should be returned. (optional) (default to )
assetnumber = '' # str | Asset number filter for the device details to be retrieved. Eg: ea856771ba6277bfca16528a79c5ce1f. (optional) (default to )
seensince = '' # datetime | SeenSince DateTime, devices registered after the seensince datetime will be returned if present. (optional) (default to )
seentill = '' # datetime | SeenTill DateTime, devices registered till the seentill datetime will be returned if present. (optional) (default to )

try:
    # Retrieves registered device details.
    api_response = api_instance.device_registration_v1_retrieve_registered_devices(organizationgroupid=organizationgroupid, organizationgroup=organizationgroup, platform=platform, customattributes=customattributes, assetnumber=assetnumber, seensince=seensince, seentill=seentill)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceRegistrationV1Api->device_registration_v1_retrieve_registered_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization Group Identifier in which device details will be retrieved. | [optional] 
 **organizationgroup** | **str**| Organization Group Name search parameter in which device details will be retrieved. | [optional] [default to ]
 **platform** | **str**| Platform filter for the device details to be retrieved. | [optional] [default to ]
 **customattributes** | **str**| List of custom attribute names [separated by comma (,)] for which values should be returned. | [optional] [default to ]
 **assetnumber** | **str**| Asset number filter for the device details to be retrieved. Eg: ea856771ba6277bfca16528a79c5ce1f. | [optional] [default to ]
 **seensince** | **datetime**| SeenSince DateTime, devices registered after the seensince datetime will be returned if present. | [optional] [default to ]
 **seentill** | **datetime**| SeenTill DateTime, devices registered till the seentill datetime will be returned if present. | [optional] [default to ]

### Return type

[**RegisteredDevices**](RegisteredDevices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

