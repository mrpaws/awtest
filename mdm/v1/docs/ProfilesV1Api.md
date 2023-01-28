# mdmv1.ProfilesV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profiles_v1_activate_profile_async**](ProfilesV1Api.md#profiles_v1_activate_profile_async) | **POST** /profiles/{profileid}/activate | Activates a Device Profile by Profile Id.
[**profiles_v1_create_iot_device_device_profile**](ProfilesV1Api.md#profiles_v1_create_iot_device_device_profile) | **POST** /profiles/platforms/iotdevice | New - Creates a new profile for IOT Device
[**profiles_v1_create_iot_gateway_device_profile**](ProfilesV1Api.md#profiles_v1_create_iot_gateway_device_profile) | **POST** /profiles/platforms/iotgateway | New - Creates a new profile for IOTGateway Device
[**profiles_v1_create_windows_mobile_device_profile**](ProfilesV1Api.md#profiles_v1_create_windows_mobile_device_profile) | **POST** /profiles/platforms/windowsmobile | New - Creates a Windows Mobile profile
[**profiles_v1_deactivate_profile_async**](ProfilesV1Api.md#profiles_v1_deactivate_profile_async) | **POST** /profiles/{profileid}/deactivate | De-Activates a Device Profile by Profile Id.
[**profiles_v1_delete_certificate_profile_mapping**](ProfilesV1Api.md#profiles_v1_delete_certificate_profile_mapping) | **DELETE** /profiles/certificatemap/{mappingID} | Deletes the mapping between a certificate and profile
[**profiles_v1_delete_device_profile_async**](ProfilesV1Api.md#profiles_v1_delete_device_profile_async) | **DELETE** /profiles/{profileid} | Deletes the Device Profile by Profile Id.
[**profiles_v1_generate_barcode**](ProfilesV1Api.md#profiles_v1_generate_barcode) | **POST** /profiles/Barcode | Generates a staging barcode sheet in the selected format.
[**profiles_v1_get_certificate_profile_mappings**](ProfilesV1Api.md#profiles_v1_get_certificate_profile_mappings) | **GET** /profiles/certificatemap | List the certificate mappings for a device profile
[**profiles_v1_get_devices_for_profile_status**](ProfilesV1Api.md#profiles_v1_get_devices_for_profile_status) | **GET** /profiles/{profileuuid}/devices | New - Returns a list of devices based on the installation status for the specified profile identified by profile uuid.
[**profiles_v1_get_profile_status_counts_async**](ProfilesV1Api.md#profiles_v1_get_profile_status_counts_async) | **GET** /profiles/{profileUuid}/summary | New - Returns device count by profile status for the given profile uuid.
[**profiles_v1_get_sso_profile_status**](ProfilesV1Api.md#profiles_v1_get_sso_profile_status) | **GET** /profiles/sso/status | New - Gets sso profiles configuration status for android, ios and windows.
[**profiles_v1_honeywell_barcode**](ProfilesV1Api.md#profiles_v1_honeywell_barcode) | **POST** /profiles/honeywell/barcode | New - Generates a barcode to be used with Honeywell EZ Config
[**profiles_v1_install_profile_async**](ProfilesV1Api.md#profiles_v1_install_profile_async) | **POST** /profiles/{profileid}/install | New - Installs the profile on device.
[**profiles_v1_maintain_custom_attribute_profile_async**](ProfilesV1Api.md#profiles_v1_maintain_custom_attribute_profile_async) | **POST** /profiles/MaintainCustomAttributeProfile | Creates a Custom Attribute Device Profile For QNX, Windows Mobile, IOTGateway and IOT Device.
[**profiles_v1_remove_profile_async**](ProfilesV1Api.md#profiles_v1_remove_profile_async) | **POST** /profiles/{profileid}/remove | Removes the profile from the device.
[**profiles_v1_save_certificate_profile_mapping**](ProfilesV1Api.md#profiles_v1_save_certificate_profile_mapping) | **POST** /profiles/certificatemap | New - Creates a mapping between a profile and certificate or certificate template
[**profiles_v1_search**](ProfilesV1Api.md#profiles_v1_search) | **GET** /profiles/search | Searches for all profiles applicable using the query information provided.
[**profiles_v1_stage_now_barcode**](ProfilesV1Api.md#profiles_v1_stage_now_barcode) | **POST** /profiles/stagenow/barcode | New - Generates a barcode to be used with Stage Now
[**profiles_v1_update_iot_device_profile**](ProfilesV1Api.md#profiles_v1_update_iot_device_profile) | **PUT** /profiles/platforms/iotdevice/{profileId} | New - Updates an existing profile for IOT device
[**profiles_v1_update_iot_gateway_device_profile**](ProfilesV1Api.md#profiles_v1_update_iot_gateway_device_profile) | **PUT** /profiles/platforms/iotgateway/{profileId} | New - Updates an existing profile for IOTGateway device
[**profiles_v1_update_windows_mobile_device_profile**](ProfilesV1Api.md#profiles_v1_update_windows_mobile_device_profile) | **PUT** /profiles/platforms/windowsmobile | New - Updates a Windows Mobile profile
[**profiles_v1_upload_certificate**](ProfilesV1Api.md#profiles_v1_upload_certificate) | **POST** /profiles/uploadcertificate | Uploads certificate into Airwatch.
[**profiles_v1_upload_profile_certificate**](ProfilesV1Api.md#profiles_v1_upload_profile_certificate) | **POST** /profiles/certificate/upload/{profileUuid} | New - Saves an uploaded certificate file and associates it with a profile and Organization Group


# **profiles_v1_activate_profile_async**
> profiles_v1_activate_profile_async(profileid)

Activates a Device Profile by Profile Id.

Activates a Device Profile identified by Profile Id.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
profileid = 56 # int | Profile Id (Required).

try:
    # Activates a Device Profile by Profile Id.
    api_instance.profiles_v1_activate_profile_async(profileid)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_activate_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profileid** | **int**| Profile Id (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_create_iot_device_device_profile**
> profiles_v1_create_iot_device_device_profile(device_profile)

New - Creates a new profile for IOT Device

Create a new profile for IOT device with configuration of payloads

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
device_profile = mdmv1.IOTDeviceDeviceProfileEntity() # IOTDeviceDeviceProfileEntity | IOTDevice Device profile to be created(required)

try:
    # New - Creates a new profile for IOT Device
    api_instance.profiles_v1_create_iot_device_device_profile(device_profile)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_create_iot_device_device_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**IOTDeviceDeviceProfileEntity**](IOTDeviceDeviceProfileEntity.md)| IOTDevice Device profile to be created(required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_create_iot_gateway_device_profile**
> profiles_v1_create_iot_gateway_device_profile(device_profile)

New - Creates a new profile for IOTGateway Device

Create a new profile for IOTGateway device with configuration of payloads

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
device_profile = mdmv1.IOTGatewayDeviceProfileEntity() # IOTGatewayDeviceProfileEntity | IOTGateway Device profile to be created(required)

try:
    # New - Creates a new profile for IOTGateway Device
    api_instance.profiles_v1_create_iot_gateway_device_profile(device_profile)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_create_iot_gateway_device_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**IOTGatewayDeviceProfileEntity**](IOTGatewayDeviceProfileEntity.md)| IOTGateway Device profile to be created(required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_create_windows_mobile_device_profile**
> int profiles_v1_create_windows_mobile_device_profile(model)

New - Creates a Windows Mobile profile

It creates an existing Windows Mobile profile payload.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
model = mdmv1.WindowsMobileDeviceProfileEntity() # WindowsMobileDeviceProfileEntity | Profile payload data(Required)

try:
    # New - Creates a Windows Mobile profile
    api_response = api_instance.profiles_v1_create_windows_mobile_device_profile(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_create_windows_mobile_device_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**WindowsMobileDeviceProfileEntity**](WindowsMobileDeviceProfileEntity.md)| Profile payload data(Required) | 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_deactivate_profile_async**
> profiles_v1_deactivate_profile_async(profileid)

De-Activates a Device Profile by Profile Id.

De-Activates a Device Profile identified by Profile Id.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
profileid = 56 # int | Profile Id (Required).

try:
    # De-Activates a Device Profile by Profile Id.
    api_instance.profiles_v1_deactivate_profile_async(profileid)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_deactivate_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profileid** | **int**| Profile Id (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_delete_certificate_profile_mapping**
> bool profiles_v1_delete_certificate_profile_mapping(mapping_id)

Deletes the mapping between a certificate and profile

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
mapping_id = 789 # int | certificate profile map id

try:
    # Deletes the mapping between a certificate and profile
    api_response = api_instance.profiles_v1_delete_certificate_profile_mapping(mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_delete_certificate_profile_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| certificate profile map id | 

### Return type

**bool**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_delete_device_profile_async**
> profiles_v1_delete_device_profile_async(profileid)

Deletes the Device Profile by Profile Id.

Deletes the Device Profile identified by the Profile Id.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
profileid = 56 # int | Profile Id (Required).

try:
    # Deletes the Device Profile by Profile Id.
    api_instance.profiles_v1_delete_device_profile_async(profileid)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_delete_device_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profileid** | **int**| Profile Id (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_generate_barcode**
> profiles_v1_generate_barcode(generate_barcode_entity=generate_barcode_entity)

Generates a staging barcode sheet in the selected format.

Used to generate barcode for the specific staging profile in selected format.<br> The generated barcode will be scanned for enrolling the device.</br>

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
generate_barcode_entity = mdmv1.GenerateBarcodeEntity() # GenerateBarcodeEntity | Details of the staging profile for which barcode has to be created. (optional)

try:
    # Generates a staging barcode sheet in the selected format.
    api_instance.profiles_v1_generate_barcode(generate_barcode_entity=generate_barcode_entity)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_generate_barcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_barcode_entity** | [**GenerateBarcodeEntity**](GenerateBarcodeEntity.md)| Details of the staging profile for which barcode has to be created. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/pdf;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_get_certificate_profile_mappings**
> list[CertificateProfileMapModel] profiles_v1_get_certificate_profile_mappings(device_profile_id)

List the certificate mappings for a device profile

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
device_profile_id = 56 # int | The device profile ID

try:
    # List the certificate mappings for a device profile
    api_response = api_instance.profiles_v1_get_certificate_profile_mappings(device_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_get_certificate_profile_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile_id** | **int**| The device profile ID | 

### Return type

[**list[CertificateProfileMapModel]**](CertificateProfileMapModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_get_devices_for_profile_status**
> ProfileAssignedDevicesPagedResultsV1Model_ profiles_v1_get_devices_for_profile_status(profileuuid, profilestatus=profilestatus, organizationgroupuuid=organizationgroupuuid, page=page, pagesize=pagesize)

New - Returns a list of devices based on the installation status for the specified profile identified by profile uuid.

Gets a paged list of devices along with a link to the respective GET Devices version 2 endpoint.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
profileuuid = 'profileuuid_example' # str | Unique Identifier of the Profile(Required)
profilestatus =  # object | Profile installation status:              * INSTALLED - Profile installed. This is the default value for profilestatus.              * NOT_INSTALLED - Profile assigned and not installed. (optional) (default to )
organizationgroupuuid =  # object | Unique Identifier of the Organization Group from which devices are to be returned based on the profile installation status (optional) (default to )
page = 56 # int | Page number to return, 0 based index. Default value is 0. (optional)
pagesize = 56 # int | Maximum number of records per page. Default value is 500. (optional)

try:
    # New - Returns a list of devices based on the installation status for the specified profile identified by profile uuid.
    api_response = api_instance.profiles_v1_get_devices_for_profile_status(profileuuid, profilestatus=profilestatus, organizationgroupuuid=organizationgroupuuid, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_get_devices_for_profile_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profileuuid** | [**str**](.md)| Unique Identifier of the Profile(Required) | 
 **profilestatus** | [**object**](.md)| Profile installation status:              * INSTALLED - Profile installed. This is the default value for profilestatus.              * NOT_INSTALLED - Profile assigned and not installed. | [optional] [default to ]
 **organizationgroupuuid** | [**object**](.md)| Unique Identifier of the Organization Group from which devices are to be returned based on the profile installation status | [optional] [default to ]
 **page** | **int**| Page number to return, 0 based index. Default value is 0. | [optional] 
 **pagesize** | **int**| Maximum number of records per page. Default value is 500. | [optional] 

### Return type

[**ProfileAssignedDevicesPagedResultsV1Model_**](ProfileAssignedDevicesPagedResultsV1Model_.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_get_profile_status_counts_async**
> ProfileSummaryModel profiles_v1_get_profile_status_counts_async(profile_uuid)

New - Returns device count by profile status for the given profile uuid.

Will return the following information for profile status count for the provided profile uuid.  1. Total assigned profile count 2. Total installed profile count 3. Total not installed profile count.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
profile_uuid = 'profile_uuid_example' # str | The uuid of the profile.              Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required).

try:
    # New - Returns device count by profile status for the given profile uuid.
    api_response = api_instance.profiles_v1_get_profile_status_counts_async(profile_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_get_profile_status_counts_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | [**str**](.md)| The uuid of the profile.              Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required). | 

### Return type

[**ProfileSummaryModel**](ProfileSummaryModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_get_sso_profile_status**
> SsoProfileStatusV1Model profiles_v1_get_sso_profile_status()

New - Gets sso profiles configuration status for android, ios and windows.

Checks whether sso profiles are existing in system for different platforms. Note that the profiles need to have a predefined name for api to fetch the proper status.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))

try:
    # New - Gets sso profiles configuration status for android, ios and windows.
    api_response = api_instance.profiles_v1_get_sso_profile_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_get_sso_profile_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SsoProfileStatusV1Model**](SsoProfileStatusV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_honeywell_barcode**
> profiles_v1_honeywell_barcode(honeywell_barcode_model)

New - Generates a barcode to be used with Honeywell EZ Config

It generates a barcode to be used with the EZ Config client on Honeywell Android devices.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
honeywell_barcode_model = mdmv1.HoneywellBarcodeV1Model() # HoneywellBarcodeV1Model | Honeywell barcode model(Required)

try:
    # New - Generates a barcode to be used with Honeywell EZ Config
    api_instance.profiles_v1_honeywell_barcode(honeywell_barcode_model)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_honeywell_barcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **honeywell_barcode_model** | [**HoneywellBarcodeV1Model**](HoneywellBarcodeV1Model.md)| Honeywell barcode model(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_install_profile_async**
> profiles_v1_install_profile_async(profileid, device_info)

New - Installs the profile on device.

Installs the profile on the device identified by the query information provided.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
profileid = 56 # int | The id of the profile to be installed.(Required).
device_info = mdmv1.DeviceInfo() # DeviceInfo | Device information for profile installation.(Required).

try:
    # New - Installs the profile on device.
    api_instance.profiles_v1_install_profile_async(profileid, device_info)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_install_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profileid** | **int**| The id of the profile to be installed.(Required). | 
 **device_info** | [**DeviceInfo**](DeviceInfo.md)| Device information for profile installation.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_maintain_custom_attribute_profile_async**
> profiles_v1_maintain_custom_attribute_profile_async(custom_attribute_device_profile=custom_attribute_device_profile)

Creates a Custom Attribute Device Profile For QNX, Windows Mobile, IOTGateway and IOT Device.

Creates a profile with custom attribute payload.<br>The payload details include custom attribute Name, Value and its application group</br>

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
custom_attribute_device_profile = mdmv1.CustomAttributeProfileEntity() # CustomAttributeProfileEntity | Details of custom attribute profile. (optional)

try:
    # Creates a Custom Attribute Device Profile For QNX, Windows Mobile, IOTGateway and IOT Device.
    api_instance.profiles_v1_maintain_custom_attribute_profile_async(custom_attribute_device_profile=custom_attribute_device_profile)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_maintain_custom_attribute_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_attribute_device_profile** | [**CustomAttributeProfileEntity**](CustomAttributeProfileEntity.md)| Details of custom attribute profile. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_remove_profile_async**
> profiles_v1_remove_profile_async(profileid, device_info=device_info)

Removes the profile from the device.

Removes the profile from the device identified by the query information provided.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
profileid = 56 # int | Profile Id Example=12.
device_info = mdmv1.DeviceInfo() # DeviceInfo | Device details. (optional)

try:
    # Removes the profile from the device.
    api_instance.profiles_v1_remove_profile_async(profileid, device_info=device_info)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_remove_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profileid** | **int**| Profile Id Example&#x3D;12. | 
 **device_info** | [**DeviceInfo**](DeviceInfo.md)| Device details. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_save_certificate_profile_mapping**
> CertificateProfileMapModel profiles_v1_save_certificate_profile_mapping(map_model=map_model)

New - Creates a mapping between a profile and certificate or certificate template

v1

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
map_model = mdmv1.CertificateProfileMapModel() # CertificateProfileMapModel | Certificate profile map model (optional)

try:
    # New - Creates a mapping between a profile and certificate or certificate template
    api_response = api_instance.profiles_v1_save_certificate_profile_mapping(map_model=map_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_save_certificate_profile_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_model** | [**CertificateProfileMapModel**](CertificateProfileMapModel.md)| Certificate profile map model | [optional] 

### Return type

[**CertificateProfileMapModel**](CertificateProfileMapModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_search**
> profiles_v1_search(type=type, profilename=profilename, organizationgroupid=organizationgroupid, platform=platform, status=status, ownership=ownership, modifiedfrom=modifiedfrom, modifiedtill=modifiedtill, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)

Searches for all profiles applicable using the query information provided.

v1.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
type = '' # str | Assignment Type. (optional) (default to )
profilename = '' # str | Profile Name. (optional) (default to )
organizationgroupid = 56 # int | Organization Group ID. (optional)
platform = '' # str | Platform name. (optional) (default to )
status = '' # str | Smart Group Identifier. (optional) (default to )
ownership = '' # str | Ownership Type. (optional) (default to )
modifiedfrom = '' # datetime | DateTime, Filters the result where Profile modified date is greater than or equal to modifiedfrom value. (optional) (default to )
modifiedtill = '' # datetime | DateTime, Filters the result where Profile modified date is less than or equal to modifiedtill value. (optional) (default to )
orderby = '' # str | Orderby parameter name. (optional) (default to )
sortorder = '' # str | Sorting order. Values ASC or DESC. Defaults to ASC. (optional) (default to )
page = 56 # int | Page number. (optional)
pagesize = 56 # int | Maximum results which should be returned in each page. (optional)

try:
    # Searches for all profiles applicable using the query information provided.
    api_instance.profiles_v1_search(type=type, profilename=profilename, organizationgroupid=organizationgroupid, platform=platform, status=status, ownership=ownership, modifiedfrom=modifiedfrom, modifiedtill=modifiedtill, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Assignment Type. | [optional] [default to ]
 **profilename** | **str**| Profile Name. | [optional] [default to ]
 **organizationgroupid** | **int**| Organization Group ID. | [optional] 
 **platform** | **str**| Platform name. | [optional] [default to ]
 **status** | **str**| Smart Group Identifier. | [optional] [default to ]
 **ownership** | **str**| Ownership Type. | [optional] [default to ]
 **modifiedfrom** | **datetime**| DateTime, Filters the result where Profile modified date is greater than or equal to modifiedfrom value. | [optional] [default to ]
 **modifiedtill** | **datetime**| DateTime, Filters the result where Profile modified date is less than or equal to modifiedtill value. | [optional] [default to ]
 **orderby** | **str**| Orderby parameter name. | [optional] [default to ]
 **sortorder** | **str**| Sorting order. Values ASC or DESC. Defaults to ASC. | [optional] [default to ]
 **page** | **int**| Page number. | [optional] 
 **pagesize** | **int**| Maximum results which should be returned in each page. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_stage_now_barcode**
> profiles_v1_stage_now_barcode(stage_now_barcode_model)

New - Generates a barcode to be used with Stage Now

It generates a barcode to be used with the Stage Now client on Zebra Android devices.  Stage Now replaces the RD staging client in newer Zebra Android devices.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
stage_now_barcode_model = mdmv1.StageNowBarcodeV1Model() # StageNowBarcodeV1Model | Stage now barcode model(Required)

try:
    # New - Generates a barcode to be used with Stage Now
    api_instance.profiles_v1_stage_now_barcode(stage_now_barcode_model)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_stage_now_barcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_now_barcode_model** | [**StageNowBarcodeV1Model**](StageNowBarcodeV1Model.md)| Stage now barcode model(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_update_iot_device_profile**
> profiles_v1_update_iot_device_profile(device_profile, profile_id)

New - Updates an existing profile for IOT device

Update an existing profile for IOT device with new configuration of payloads

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
device_profile = mdmv1.IOTDeviceDeviceProfileEntity() # IOTDeviceDeviceProfileEntity | IOT device profile to be updated(Required)
profile_id = 56 # int | Profile id

try:
    # New - Updates an existing profile for IOT device
    api_instance.profiles_v1_update_iot_device_profile(device_profile, profile_id)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_update_iot_device_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**IOTDeviceDeviceProfileEntity**](IOTDeviceDeviceProfileEntity.md)| IOT device profile to be updated(Required) | 
 **profile_id** | **int**| Profile id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_update_iot_gateway_device_profile**
> profiles_v1_update_iot_gateway_device_profile(device_profile, profile_id)

New - Updates an existing profile for IOTGateway device

Update an existing profile for IOTgateway device with new configuration of payloads

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
device_profile = mdmv1.IOTGatewayDeviceProfileEntity() # IOTGatewayDeviceProfileEntity | IOTGateway device profile to be updated(Required)
profile_id = 56 # int | Profile id

try:
    # New - Updates an existing profile for IOTGateway device
    api_instance.profiles_v1_update_iot_gateway_device_profile(device_profile, profile_id)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_update_iot_gateway_device_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**IOTGatewayDeviceProfileEntity**](IOTGatewayDeviceProfileEntity.md)| IOTGateway device profile to be updated(Required) | 
 **profile_id** | **int**| Profile id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_update_windows_mobile_device_profile**
> profiles_v1_update_windows_mobile_device_profile(model)

New - Updates a Windows Mobile profile

It updates an existing Windows Mobile profile payload.

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
model = mdmv1.WindowsMobileDeviceProfileEntity() # WindowsMobileDeviceProfileEntity | Profile payload data(Required)

try:
    # New - Updates a Windows Mobile profile
    api_instance.profiles_v1_update_windows_mobile_device_profile(model)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_update_windows_mobile_device_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**WindowsMobileDeviceProfileEntity**](WindowsMobileDeviceProfileEntity.md)| Profile payload data(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_upload_certificate**
> profiles_v1_upload_certificate(certificate=certificate)

Uploads certificate into Airwatch.

Uploads certificate into AirWatch [Both .pfx and .cer formats].

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
certificate = mdmv1.Certificate() # Certificate | Certificate resource. (optional)

try:
    # Uploads certificate into Airwatch.
    api_instance.profiles_v1_upload_certificate(certificate=certificate)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_upload_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | [**Certificate**](Certificate.md)| Certificate resource. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v1_upload_profile_certificate**
> CertificateModel profiles_v1_upload_profile_certificate(profile_uuid)

New - Saves an uploaded certificate file and associates it with a profile and Organization Group

Creates a new certificate associated with Organization Group and returns certificateID

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
api_instance = mdmv1.ProfilesV1Api(mdmv1.ApiClient(configuration))
profile_uuid = 'profile_uuid_example' # str | profile unique identifier

try:
    # New - Saves an uploaded certificate file and associates it with a profile and Organization Group
    api_response = api_instance.profiles_v1_upload_profile_certificate(profile_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV1Api->profiles_v1_upload_profile_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| profile unique identifier | 

### Return type

[**CertificateModel**](CertificateModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

