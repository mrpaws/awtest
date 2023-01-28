# mdmv2.ProfilesV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profiles_v2_create_android_device_profile_async**](ProfilesV2Api.md#profiles_v2_create_android_device_profile_async) | **POST** /profiles/platforms/android/create | Creates an ANDROID Device Profile.
[**profiles_v2_create_apple_device_profile_async**](ProfilesV2Api.md#profiles_v2_create_apple_device_profile_async) | **POST** /profiles/platforms/apple/create | Creates an Apple iOS device profile.
[**profiles_v2_create_apple_os_x_device_profile_async**](ProfilesV2Api.md#profiles_v2_create_apple_os_x_device_profile_async) | **POST** /profiles/platforms/appleosx/create | Creates an Apple macOS device Profile.
[**profiles_v2_create_apple_tv_profiles**](ProfilesV2Api.md#profiles_v2_create_apple_tv_profiles) | **POST** /profiles/platforms/appletv | New - Create a new profile for apple tv.
[**profiles_v2_create_epson_printer_profiles**](ProfilesV2Api.md#profiles_v2_create_epson_printer_profiles) | **POST** /profiles/platforms/epson | New - Create a new profile for Epson printer.
[**profiles_v2_create_profile_resource_async**](ProfilesV2Api.md#profiles_v2_create_profile_resource_async) | **POST** /profiles/resources/{resourceType} | Creates a Resource for the requested type.
[**profiles_v2_create_qnx_device_profile_async**](ProfilesV2Api.md#profiles_v2_create_qnx_device_profile_async) | **POST** /profiles/platforms/qnx/create | Creates a Provisioning Enabled QNX Device Profile.
[**profiles_v2_delete_profile_resource_async**](ProfilesV2Api.md#profiles_v2_delete_profile_resource_async) | **DELETE** /profiles/resources/{id} | Deletes the Resource identified by the Resource ID.
[**profiles_v2_edit_assignment_async**](ProfilesV2Api.md#profiles_v2_edit_assignment_async) | **PUT** /profiles/resources/editassignment/{id} | Edit the Smart Group assignments for a given Resource.
[**profiles_v2_get_device_profile_details_async**](ProfilesV2Api.md#profiles_v2_get_device_profile_details_async) | **GET** /profiles/{profileId} | Gets Device Profile.
[**profiles_v2_get_payload_keys**](ProfilesV2Api.md#profiles_v2_get_payload_keys) | **GET** /profiles/platforms/{platform}/payloads/{payload}/getpayloadkeys | Gets PayloadKeys.
[**profiles_v2_get_profile_resource_details**](ProfilesV2Api.md#profiles_v2_get_profile_resource_details) | **GET** /profiles/resources/{id} | Gets a Resource for a given Resource ID.
[**profiles_v2_get_profile_resource_keys**](ProfilesV2Api.md#profiles_v2_get_profile_resource_keys) | **GET** /profiles/resources/{resourceType}/resourcekeys | Gets Resource keys and advanced settings for the specified Resource type.
[**profiles_v2_search_profiles**](ProfilesV2Api.md#profiles_v2_search_profiles) | **GET** /profiles/search | Gets List of profiles based on the search criteria.
[**profiles_v2_update_android_device_profile_async**](ProfilesV2Api.md#profiles_v2_update_android_device_profile_async) | **POST** /profiles/platforms/android/update | Updates an ANDROID Device Profile.  If the CreateNewVersion key is empty or false, a new Profile version will not be created but AssignedSmartGroups, RootLocationGroup, AssignedGeofenceArea and AssignedSchedule will be saved and published.  Else if it&#39;s true, new version of the profile will be created and published.
[**profiles_v2_update_apple_device_profile_async**](ProfilesV2Api.md#profiles_v2_update_apple_device_profile_async) | **POST** /profiles/platforms/apple/update | Updates an Apple iOS device profile.
[**profiles_v2_update_apple_os_x_device_profile_async**](ProfilesV2Api.md#profiles_v2_update_apple_os_x_device_profile_async) | **POST** /profiles/platforms/appleosx/update | Updates an Apple macOS device Profile.
[**profiles_v2_update_apple_tv_profiles**](ProfilesV2Api.md#profiles_v2_update_apple_tv_profiles) | **PUT** /profiles/platforms/appletv/{profileId} | New - Update an existing profile for apple tv
[**profiles_v2_update_epson_printer_profiles**](ProfilesV2Api.md#profiles_v2_update_epson_printer_profiles) | **PUT** /profiles/platforms/epson/{profileId} | New - Update the existing printer profile for Epson.
[**profiles_v2_update_profile_resource_async**](ProfilesV2Api.md#profiles_v2_update_profile_resource_async) | **PUT** /profiles/resources/{resourceType} | Updates the given Resource entity.
[**profiles_v2_update_qnx_device_profile_async**](ProfilesV2Api.md#profiles_v2_update_qnx_device_profile_async) | **POST** /profiles/platforms/qnx/update | Updates the custom attributes details of existing QNX Device Profile.


# **profiles_v2_create_android_device_profile_async**
> int profiles_v2_create_android_device_profile_async(device_profile=device_profile)

Creates an ANDROID Device Profile.

1. v2  2. For Compliance Assignment Type Allow Removal should always be Never.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
device_profile = mdmv2.AndroidDeviceProfileV2Entity() # AndroidDeviceProfileV2Entity | AndroidDeviceProfileEntity. (optional)

try:
    # Creates an ANDROID Device Profile.
    api_response = api_instance.profiles_v2_create_android_device_profile_async(device_profile=device_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_create_android_device_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**AndroidDeviceProfileV2Entity**](AndroidDeviceProfileV2Entity.md)| AndroidDeviceProfileEntity. | [optional] 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_create_apple_device_profile_async**
> int profiles_v2_create_apple_device_profile_async(device_profile=device_profile)

Creates an Apple iOS device profile.

1. Creates an Apple device profile containing a number of settings that you can specify, including : Passcode, Restrictions, VPN, Wi-Fi, Email, EAS, SCEP, Credentials, Custom Settings, etc.  2. For Compliance Assignment Type Allow Removal should always be Never.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
device_profile = mdmv2.AppleDeviceProfileV2Entity() # AppleDeviceProfileV2Entity | Apple Device Profile V2 Entity. (optional)

try:
    # Creates an Apple iOS device profile.
    api_response = api_instance.profiles_v2_create_apple_device_profile_async(device_profile=device_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_create_apple_device_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**AppleDeviceProfileV2Entity**](AppleDeviceProfileV2Entity.md)| Apple Device Profile V2 Entity. | [optional] 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_create_apple_os_x_device_profile_async**
> int profiles_v2_create_apple_os_x_device_profile_async(device_profile=device_profile)

Creates an Apple macOS device Profile.

1. Creates an Apple macOS device profile containing a number of settings that you can specify, including : Passcode, Restrictions, Network, Email, Dock, SCEP, Credentials, Custom Settings, etc.  2. For Compliance Assignment Type Allow Removal should always be Never.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
device_profile = mdmv2.AppleOsXDeviceProfileEntity_() # AppleOsXDeviceProfileEntity_ | Apple macOS Device Profile Entity. (optional)

try:
    # Creates an Apple macOS device Profile.
    api_response = api_instance.profiles_v2_create_apple_os_x_device_profile_async(device_profile=device_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_create_apple_os_x_device_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**AppleOsXDeviceProfileEntity_**](AppleOsXDeviceProfileEntity_.md)| Apple macOS Device Profile Entity. | [optional] 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_create_apple_tv_profiles**
> profiles_v2_create_apple_tv_profiles(apple_tv_device_profile_v2_entity)

New - Create a new profile for apple tv.

Create a new profile for apple tv with configuration of SingleAppMode or ConferenceRoomDisplay payload.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
apple_tv_device_profile_v2_entity = mdmv2.AppleTvDeviceProfileV2Entity_() # AppleTvDeviceProfileV2Entity_ | Apple tv device profile to be created.(Required)

try:
    # New - Create a new profile for apple tv.
    api_instance.profiles_v2_create_apple_tv_profiles(apple_tv_device_profile_v2_entity)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_create_apple_tv_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_tv_device_profile_v2_entity** | [**AppleTvDeviceProfileV2Entity_**](AppleTvDeviceProfileV2Entity_.md)| Apple tv device profile to be created.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_create_epson_printer_profiles**
> profiles_v2_create_epson_printer_profiles(epson_printer_profile_model)

New - Create a new profile for Epson printer.

Create a new profile for epson printer with configuration SCEP

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
epson_printer_profile_model = mdmv2.EpsonPrinterProfileV2Model_() # EpsonPrinterProfileV2Model_ | Epson printer device profile to be created.(Required)

try:
    # New - Create a new profile for Epson printer.
    api_instance.profiles_v2_create_epson_printer_profiles(epson_printer_profile_model)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_create_epson_printer_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epson_printer_profile_model** | [**EpsonPrinterProfileV2Model_**](EpsonPrinterProfileV2Model_.md)| Epson printer device profile to be created.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_create_profile_resource_async**
> ProfileResourceModel profiles_v2_create_profile_resource_async(resource_type, resource_name=resource_name, resource_description=resource_description, resource_id=resource_id, resource_assignment_assignment_type=resource_assignment_assignment_type, resource_assignment_managed_location_group_id=resource_assignment_managed_location_group_id, resource_assignment_assigned_smart_groups=resource_assignment_assigned_smart_groups, resource_assignment_excluded_smart_groups=resource_assignment_excluded_smart_groups)

Creates a Resource for the requested type.

Creates a Resource for the passed in Resource Type(VPN/Wifi/EAS).

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | Gets or sets resource name. (optional)
resource_description = 'resource_description_example' # str | Gets or sets resource description. (optional)
resource_id = 56 # int | Gets or sets resource id. (optional)
resource_assignment_assignment_type = 'resource_assignment_assignment_type_example' # str | Gets or sets assignment Type for Resource. (optional)
resource_assignment_managed_location_group_id = 56 # int | Gets or sets root Organization Group Id. (optional)
resource_assignment_assigned_smart_groups = [56] # list[int] | Gets or sets the SmartGroups need to be assigned. (optional)
resource_assignment_excluded_smart_groups = [56] # list[int] | Gets or sets the SmartGroups need to be excluded. (optional)

try:
    # Creates a Resource for the requested type.
    api_response = api_instance.profiles_v2_create_profile_resource_async(resource_type, resource_name=resource_name, resource_description=resource_description, resource_id=resource_id, resource_assignment_assignment_type=resource_assignment_assignment_type, resource_assignment_managed_location_group_id=resource_assignment_managed_location_group_id, resource_assignment_assigned_smart_groups=resource_assignment_assigned_smart_groups, resource_assignment_excluded_smart_groups=resource_assignment_excluded_smart_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_create_profile_resource_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**|  | 
 **resource_name** | **str**| Gets or sets resource name. | [optional] 
 **resource_description** | **str**| Gets or sets resource description. | [optional] 
 **resource_id** | **int**| Gets or sets resource id. | [optional] 
 **resource_assignment_assignment_type** | **str**| Gets or sets assignment Type for Resource. | [optional] 
 **resource_assignment_managed_location_group_id** | **int**| Gets or sets root Organization Group Id. | [optional] 
 **resource_assignment_assigned_smart_groups** | [**list[int]**](int.md)| Gets or sets the SmartGroups need to be assigned. | [optional] 
 **resource_assignment_excluded_smart_groups** | [**list[int]**](int.md)| Gets or sets the SmartGroups need to be excluded. | [optional] 

### Return type

[**ProfileResourceModel**](ProfileResourceModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_create_qnx_device_profile_async**
> profiles_v2_create_qnx_device_profile_async(device_profile=device_profile)

Creates a Provisioning Enabled QNX Device Profile.

1. Creates a new QNX profile with provisioning enabled.<br>With provisioning enabled, the profiles will be linked to products and will be assigned to devices using policy engine.</br>  2. For Compliance Assignment Type Allow Removal should always be Never.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
device_profile = mdmv2.QnxDeviceProfileEntity() # QnxDeviceProfileEntity | The profile details like Name, scope, custom attribute name, value and Id. (optional)

try:
    # Creates a Provisioning Enabled QNX Device Profile.
    api_instance.profiles_v2_create_qnx_device_profile_async(device_profile=device_profile)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_create_qnx_device_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**QnxDeviceProfileEntity**](QnxDeviceProfileEntity.md)| The profile details like Name, scope, custom attribute name, value and Id. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_delete_profile_resource_async**
> profiles_v2_delete_profile_resource_async(id)

Deletes the Resource identified by the Resource ID.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
id = 56 # int | Resource ID (Required).

try:
    # Deletes the Resource identified by the Resource ID.
    api_instance.profiles_v2_delete_profile_resource_async(id)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_delete_profile_resource_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Resource ID (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_edit_assignment_async**
> profiles_v2_edit_assignment_async(resource_assignment_model, id)

Edit the Smart Group assignments for a given Resource.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
resource_assignment_model = mdmv2.ResourceAssignmentModel() # ResourceAssignmentModel | Resource Assignment model (Required).
id = 56 # int | Resource ID (Required).

try:
    # Edit the Smart Group assignments for a given Resource.
    api_instance.profiles_v2_edit_assignment_async(resource_assignment_model, id)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_edit_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment_model** | [**ResourceAssignmentModel**](ResourceAssignmentModel.md)| Resource Assignment model (Required). | 
 **id** | **int**| Resource ID (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_get_device_profile_details_async**
> DeviceProfileV2Entity profiles_v2_get_device_profile_details_async(profile_id)

Gets Device Profile.

Gets Device Profile Details identified by the Profile Id.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
profile_id = 56 # int | Profile Id (Required).

try:
    # Gets Device Profile.
    api_response = api_instance.profiles_v2_get_device_profile_details_async(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_get_device_profile_details_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**| Profile Id (Required). | 

### Return type

[**DeviceProfileV2Entity**](DeviceProfileV2Entity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_get_payload_keys**
> DeviceProfileV2Entity profiles_v2_get_payload_keys(platform, payload, context_type=context_type)

Gets PayloadKeys.

Gets PayloadKeys for the specified Platform and Payload.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
platform = 'platform_example' # str | Platform Name (Required).
payload = 'payload_example' # str | Payload Name (Required).
context_type = '' # str | Context Type. (optional) (default to )

try:
    # Gets PayloadKeys.
    api_response = api_instance.profiles_v2_get_payload_keys(platform, payload, context_type=context_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_get_payload_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Platform Name (Required). | 
 **payload** | **str**| Payload Name (Required). | 
 **context_type** | **str**| Context Type. | [optional] [default to ]

### Return type

[**DeviceProfileV2Entity**](DeviceProfileV2Entity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_get_profile_resource_details**
> ProfileResourceModel profiles_v2_get_profile_resource_details(id)

Gets a Resource for a given Resource ID.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
id = 56 # int | Resource ID (Required).

try:
    # Gets a Resource for a given Resource ID.
    api_response = api_instance.profiles_v2_get_profile_resource_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_get_profile_resource_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Resource ID (Required). | 

### Return type

[**ProfileResourceModel**](ProfileResourceModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_get_profile_resource_keys**
> profiles_v2_get_profile_resource_keys(resource_type)

Gets Resource keys and advanced settings for the specified Resource type.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
resource_type = 'resource_type_example' # str | ResourceType (Required).

try:
    # Gets Resource keys and advanced settings for the specified Resource type.
    api_instance.profiles_v2_get_profile_resource_keys(resource_type)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_get_profile_resource_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| ResourceType (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_search_profiles**
> ProfileSearchResultV2Entity profiles_v2_search_profiles(organizationgroupid=organizationgroupid, organizationgroupuuid=organizationgroupuuid, platform=platform, profiletype=profiletype, status=status, searchtext=searchtext, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize, includeandroidforwork=includeandroidforwork, payload_name=payload_name)

Gets List of profiles based on the search criteria.

The search result will contain profile's basic informations.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
organizationgroupid = 56 # int | Organization Group ID. (optional)
organizationgroupuuid =  # object | Organization group uuid, based on we search the profiles, organizationgroupid will be ignored if valid organizationgroupuuid is Passed.  (optional) (default to )
platform = '' # str | Platform name. (optional) (default to )
profiletype = '' # str | Profile Type. (optional) (default to )
status = '' # str | Profile status (Active or Inactive). (optional) (default to )
searchtext = '' # str | search text. (optional) (default to )
orderby = '' # str | Orderby parameter name. (optional) (default to )
sortorder = '' # str | Sorting order. Values ASC or DESC. Defaults to ASC. (optional) (default to )
page = 56 # int | Page number. (optional)
pagesize = 56 # int | Maximum results which should be returned in each page. (optional)
includeandroidforwork =  # bool | It will include androidforwork profiles. (optional) (default to )
payload_name = '' # str | search with anyone of the payload name :Passcode, Email, Wi-Fi, Restriction, Vpn, CustomSetting, CustomAttribute, ExchangeActiveSync, ExchangeWebServices, Device,              SharedDevice, Notifications, HomeScreenLayout, GoogleAccount, ManagedDomains, WebClips, BookmarkSettings, SingleAppMode, SingleSignOn, Permissions, PublicAppAutoUpdate, CustomMessages, ApplicationControl,              NetworkSharePoint, DiskEncryption, KernelExtension, PrivacyPreferences, SmartCard, ConferenceRoomDisplay, WindowsLicensing, OemUpdates, WindowsAutomaticUpdates, Encryption, BIOS, UserData, Customization, PassportForWork,              Scep, Firewall, Proxy, Windows10Kiosk, Antivirus, P2PBranchCacheSettings, UnifiedWriteFilter, AssignedAccess, ShortcutSettings, Certificate. (optional) (default to )

try:
    # Gets List of profiles based on the search criteria.
    api_response = api_instance.profiles_v2_search_profiles(organizationgroupid=organizationgroupid, organizationgroupuuid=organizationgroupuuid, platform=platform, profiletype=profiletype, status=status, searchtext=searchtext, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize, includeandroidforwork=includeandroidforwork, payload_name=payload_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_search_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization Group ID. | [optional] 
 **organizationgroupuuid** | [**object**](.md)| Organization group uuid, based on we search the profiles, organizationgroupid will be ignored if valid organizationgroupuuid is Passed.  | [optional] [default to ]
 **platform** | **str**| Platform name. | [optional] [default to ]
 **profiletype** | **str**| Profile Type. | [optional] [default to ]
 **status** | **str**| Profile status (Active or Inactive). | [optional] [default to ]
 **searchtext** | **str**| search text. | [optional] [default to ]
 **orderby** | **str**| Orderby parameter name. | [optional] [default to ]
 **sortorder** | **str**| Sorting order. Values ASC or DESC. Defaults to ASC. | [optional] [default to ]
 **page** | **int**| Page number. | [optional] 
 **pagesize** | **int**| Maximum results which should be returned in each page. | [optional] 
 **includeandroidforwork** | **bool**| It will include androidforwork profiles. | [optional] [default to ]
 **payload_name** | **str**| search with anyone of the payload name :Passcode, Email, Wi-Fi, Restriction, Vpn, CustomSetting, CustomAttribute, ExchangeActiveSync, ExchangeWebServices, Device,              SharedDevice, Notifications, HomeScreenLayout, GoogleAccount, ManagedDomains, WebClips, BookmarkSettings, SingleAppMode, SingleSignOn, Permissions, PublicAppAutoUpdate, CustomMessages, ApplicationControl,              NetworkSharePoint, DiskEncryption, KernelExtension, PrivacyPreferences, SmartCard, ConferenceRoomDisplay, WindowsLicensing, OemUpdates, WindowsAutomaticUpdates, Encryption, BIOS, UserData, Customization, PassportForWork,              Scep, Firewall, Proxy, Windows10Kiosk, Antivirus, P2PBranchCacheSettings, UnifiedWriteFilter, AssignedAccess, ShortcutSettings, Certificate. | [optional] [default to ]

### Return type

[**ProfileSearchResultV2Entity**](ProfileSearchResultV2Entity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_update_android_device_profile_async**
> profiles_v2_update_android_device_profile_async(device_profile=device_profile)

Updates an ANDROID Device Profile.  If the CreateNewVersion key is empty or false, a new Profile version will not be created but AssignedSmartGroups, RootLocationGroup, AssignedGeofenceArea and AssignedSchedule will be saved and published.  Else if it's true, new version of the profile will be created and published.

1. v2  2. For Compliance Assignment Type Allow Removal should always be Never.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
device_profile = mdmv2.AndroidDeviceProfileV2Entity() # AndroidDeviceProfileV2Entity | AndroidDeviceProfileEntity. (optional)

try:
    # Updates an ANDROID Device Profile.  If the CreateNewVersion key is empty or false, a new Profile version will not be created but AssignedSmartGroups, RootLocationGroup, AssignedGeofenceArea and AssignedSchedule will be saved and published.  Else if it's true, new version of the profile will be created and published.
    api_instance.profiles_v2_update_android_device_profile_async(device_profile=device_profile)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_update_android_device_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**AndroidDeviceProfileV2Entity**](AndroidDeviceProfileV2Entity.md)| AndroidDeviceProfileEntity. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_update_apple_device_profile_async**
> profiles_v2_update_apple_device_profile_async(device_profile=device_profile)

Updates an Apple iOS device profile.

1. Updates an Apple device profile identified by its numeric ID.  2. For Compliance Assignment Type Allow Removal should always be Never.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
device_profile = mdmv2.AppleDeviceProfileV2Entity() # AppleDeviceProfileV2Entity | Apple Device Profile V2 Entity. (optional)

try:
    # Updates an Apple iOS device profile.
    api_instance.profiles_v2_update_apple_device_profile_async(device_profile=device_profile)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_update_apple_device_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**AppleDeviceProfileV2Entity**](AppleDeviceProfileV2Entity.md)| Apple Device Profile V2 Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_update_apple_os_x_device_profile_async**
> profiles_v2_update_apple_os_x_device_profile_async(device_profile=device_profile)

Updates an Apple macOS device Profile.

1. Updates an Apple macOS device profile identified by its numeric ID.  2. For Compliance Assignment Type Allow Removal should always be Never.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
device_profile = mdmv2.AppleOsXDeviceProfileEntity() # AppleOsXDeviceProfileEntity | Apple macOS Device Profile Entity. (optional)

try:
    # Updates an Apple macOS device Profile.
    api_instance.profiles_v2_update_apple_os_x_device_profile_async(device_profile=device_profile)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_update_apple_os_x_device_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**AppleOsXDeviceProfileEntity**](AppleOsXDeviceProfileEntity.md)| Apple macOS Device Profile Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_update_apple_tv_profiles**
> profiles_v2_update_apple_tv_profiles(apple_tv_device_profile_v2_entity, profile_id)

New - Update an existing profile for apple tv

Update an existing profile for apple tv with new configuration of payloads

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
apple_tv_device_profile_v2_entity = mdmv2.AppleTvDeviceProfileV2Entity() # AppleTvDeviceProfileV2Entity | Apple tv device profile to be updated(Required)
profile_id = 56 # int | Profile id

try:
    # New - Update an existing profile for apple tv
    api_instance.profiles_v2_update_apple_tv_profiles(apple_tv_device_profile_v2_entity, profile_id)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_update_apple_tv_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_tv_device_profile_v2_entity** | [**AppleTvDeviceProfileV2Entity**](AppleTvDeviceProfileV2Entity.md)| Apple tv device profile to be updated(Required) | 
 **profile_id** | **int**| Profile id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_update_epson_printer_profiles**
> profiles_v2_update_epson_printer_profiles(epson_printer_profile_model, profile_id)

New - Update the existing printer profile for Epson.

Update the existing Epson printer profile

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
epson_printer_profile_model = mdmv2.EpsonPrinterProfileV2Model() # EpsonPrinterProfileV2Model | Epson device profile to be updated.(Required)
profile_id = 56 # int | Profile id

try:
    # New - Update the existing printer profile for Epson.
    api_instance.profiles_v2_update_epson_printer_profiles(epson_printer_profile_model, profile_id)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_update_epson_printer_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epson_printer_profile_model** | [**EpsonPrinterProfileV2Model**](EpsonPrinterProfileV2Model.md)| Epson device profile to be updated.(Required) | 
 **profile_id** | **int**| Profile id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_update_profile_resource_async**
> profiles_v2_update_profile_resource_async(resource_type, resource_name=resource_name, resource_description=resource_description, resource_id=resource_id, resource_assignment_assignment_type=resource_assignment_assignment_type, resource_assignment_managed_location_group_id=resource_assignment_managed_location_group_id, resource_assignment_assigned_smart_groups=resource_assignment_assigned_smart_groups, resource_assignment_excluded_smart_groups=resource_assignment_excluded_smart_groups)

Updates the given Resource entity.

Updates the passed in Resource Entity(VPN/Wifi/EAS entity).

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | Gets or sets resource name. (optional)
resource_description = 'resource_description_example' # str | Gets or sets resource description. (optional)
resource_id = 56 # int | Gets or sets resource id. (optional)
resource_assignment_assignment_type = 'resource_assignment_assignment_type_example' # str | Gets or sets assignment Type for Resource. (optional)
resource_assignment_managed_location_group_id = 56 # int | Gets or sets root Organization Group Id. (optional)
resource_assignment_assigned_smart_groups = [56] # list[int] | Gets or sets the SmartGroups need to be assigned. (optional)
resource_assignment_excluded_smart_groups = [56] # list[int] | Gets or sets the SmartGroups need to be excluded. (optional)

try:
    # Updates the given Resource entity.
    api_instance.profiles_v2_update_profile_resource_async(resource_type, resource_name=resource_name, resource_description=resource_description, resource_id=resource_id, resource_assignment_assignment_type=resource_assignment_assignment_type, resource_assignment_managed_location_group_id=resource_assignment_managed_location_group_id, resource_assignment_assigned_smart_groups=resource_assignment_assigned_smart_groups, resource_assignment_excluded_smart_groups=resource_assignment_excluded_smart_groups)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_update_profile_resource_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**|  | 
 **resource_name** | **str**| Gets or sets resource name. | [optional] 
 **resource_description** | **str**| Gets or sets resource description. | [optional] 
 **resource_id** | **int**| Gets or sets resource id. | [optional] 
 **resource_assignment_assignment_type** | **str**| Gets or sets assignment Type for Resource. | [optional] 
 **resource_assignment_managed_location_group_id** | **int**| Gets or sets root Organization Group Id. | [optional] 
 **resource_assignment_assigned_smart_groups** | [**list[int]**](int.md)| Gets or sets the SmartGroups need to be assigned. | [optional] 
 **resource_assignment_excluded_smart_groups** | [**list[int]**](int.md)| Gets or sets the SmartGroups need to be excluded. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v2_update_qnx_device_profile_async**
> profiles_v2_update_qnx_device_profile_async(device_profile=device_profile)

Updates the custom attributes details of existing QNX Device Profile.

1. Updates the details of existing QNX profiles. <br> The details majorly include the custom attribute name, value and application group.</br>  2. For Compliance Assignment Type Allow Removal should always be Never.

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
api_instance = mdmv2.ProfilesV2Api(mdmv2.ApiClient(configuration))
device_profile = mdmv2.QnxDeviceProfileEntity() # QnxDeviceProfileEntity | Payload containing the details of the profile to be updated. (optional)

try:
    # Updates the custom attributes details of existing QNX Device Profile.
    api_instance.profiles_v2_update_qnx_device_profile_async(device_profile=device_profile)
except ApiException as e:
    print("Exception when calling ProfilesV2Api->profiles_v2_update_qnx_device_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile** | [**QnxDeviceProfileEntity**](QnxDeviceProfileEntity.md)| Payload containing the details of the profile to be updated. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

