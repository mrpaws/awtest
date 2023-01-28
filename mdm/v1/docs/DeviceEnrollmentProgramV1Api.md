# mdmv1.DeviceEnrollmentProgramV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_enrollment_program_v1_add_dep_profile_async**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_add_dep_profile_async) | **POST** /dep/profiles | New - Adds a new Device Enrollment Program profile.
[**device_enrollment_program_v1_delete_dep_authentication_entity_async**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_delete_dep_authentication_entity_async) | **DELETE** /dep/accounts/{organizationGroupId} | New - Deletes DEP and associated DEP profiles for the given organization group.
[**device_enrollment_program_v1_delete_mdm_enrollment_program_data_async**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_delete_mdm_enrollment_program_data_async) | **DELETE** /dep/profiles/{profileUuid} | New - Delete Device Enrollment Program profile based on the profile unique identifier.
[**device_enrollment_program_v1_dep_profile_action**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_dep_profile_action) | **PUT** /dep/profiles/{profileUuid}/devices/{serialNumber} | New - Assign or unassign a Device Enrollment Program profile from device.
[**device_enrollment_program_v1_edit_dep_profile**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_edit_dep_profile) | **PUT** /dep/profiles/{profileUuid} | New - Edit an existing Device Enrollment Program profile.
[**device_enrollment_program_v1_get_dep_certificate_async**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_get_dep_certificate_async) | **GET** /dep/certificates/{certId} | New - Get Device Enrollment Program certificate to upload in the Device Enrollment Program portal.
[**device_enrollment_program_v1_get_dep_devices**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_get_dep_devices) | **GET** /dep/groups/{groupUuid}/devices | New - Gets all Apple Device Enrollment Program devices at organization group.
[**device_enrollment_program_v1_get_dep_devices_for_profile**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_get_dep_devices_for_profile) | **GET** /dep/profiles/{profileUuid}/devices | New - Gets all Apple Device Enrollment Program devices assigned to the profile.
[**device_enrollment_program_v1_reconcile_dep_devices**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_reconcile_dep_devices) | **PUT** /dep/groups/{groupUuid}/devices | New - Fetches or syncs Apple Device Enrollment Program devices belonging to the organization group.
[**device_enrollment_program_v1_save_dep_authentication_entity_async**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_save_dep_authentication_entity_async) | **POST** /dep/accounts/{organizationGroupId} | New - Create a new DEP account for the organization group.
[**device_enrollment_program_v1_save_dep_certificate_async**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_save_dep_certificate_async) | **POST** /dep/certificates/{organizationGroupId} | New - Generate a new Device Enrollment Program certificate.
[**device_enrollment_program_v1_search**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_search) | **GET** /dep/profiles/search | Returns a collection of Device enrollment program profiles based on the search criteria.
[**device_enrollment_program_v1_view_shared_mdm_profile_data_async**](DeviceEnrollmentProgramV1Api.md#device_enrollment_program_v1_view_shared_mdm_profile_data_async) | **GET** /dep/profiles/{profileUuid} | New - Get Device Enrollment Program profile based on the profile unique identifier.


# **device_enrollment_program_v1_add_dep_profile_async**
> int device_enrollment_program_v1_add_dep_profile_async(dep_profile_model)

New - Adds a new Device Enrollment Program profile.

Saves the given Device Enrollment Program profile and also registers the created profile with the Apple server.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
dep_profile_model = mdmv1.MdmEnrollmentProgramApiModel_() # MdmEnrollmentProgramApiModel_ | The Device Enrollment program profile model containing the required profile properties. (Required).

try:
    # New - Adds a new Device Enrollment Program profile.
    api_response = api_instance.device_enrollment_program_v1_add_dep_profile_async(dep_profile_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_add_dep_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dep_profile_model** | [**MdmEnrollmentProgramApiModel_**](MdmEnrollmentProgramApiModel_.md)| The Device Enrollment program profile model containing the required profile properties. (Required). | 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_delete_dep_authentication_entity_async**
> device_enrollment_program_v1_delete_dep_authentication_entity_async(organization_group_id)

New - Deletes DEP and associated DEP profiles for the given organization group.

Deletes the device enrollment program account present at the given organization group. This will delete all associated profiles from AirWatch and it will also delete all the registered profiles from the Device Enrollment Program Apple server.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
organization_group_id = 56 # int | This is the organization group identifier also known as GroupID. Typically used during enrollment.(Required).

try:
    # New - Deletes DEP and associated DEP profiles for the given organization group.
    api_instance.device_enrollment_program_v1_delete_dep_authentication_entity_async(organization_group_id)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_delete_dep_authentication_entity_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_id** | **int**| This is the organization group identifier also known as GroupID. Typically used during enrollment.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_delete_mdm_enrollment_program_data_async**
> device_enrollment_program_v1_delete_mdm_enrollment_program_data_async(profile_uuid)

New - Delete Device Enrollment Program profile based on the profile unique identifier.

Deletes the given Device Enrollment Program Profile based on the profile unique identifier. This profile will also be deleted from the Apple server.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
profile_uuid = 'profile_uuid_example' # str | The unique identifier for the device enrollment program profile. (Required).

try:
    # New - Delete Device Enrollment Program profile based on the profile unique identifier.
    api_instance.device_enrollment_program_v1_delete_mdm_enrollment_program_data_async(profile_uuid)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_delete_mdm_enrollment_program_data_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| The unique identifier for the device enrollment program profile. (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_dep_profile_action**
> device_enrollment_program_v1_dep_profile_action(profile_uuid, serial_number, action)

New - Assign or unassign a Device Enrollment Program profile from device.

Assigns or unassigns the Device Enrollment Program profile to the device identified by the provided serial number based on the action flag.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
profile_uuid = 'profile_uuid_example' # str | The unique identifier of the Device Enrollment Program profile.(Required)
serial_number = 'serial_number_example' # str | The serial number of the device.(Required)
action = '' # str | Action flag is used to determine if the assign or unassign profile action must be performed for the device. Valid values are Assign and Unassign.(Required) (default to )

try:
    # New - Assign or unassign a Device Enrollment Program profile from device.
    api_instance.device_enrollment_program_v1_dep_profile_action(profile_uuid, serial_number, action)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_dep_profile_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| The unique identifier of the Device Enrollment Program profile.(Required) | 
 **serial_number** | **str**| The serial number of the device.(Required) | 
 **action** | **str**| Action flag is used to determine if the assign or unassign profile action must be performed for the device. Valid values are Assign and Unassign.(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_edit_dep_profile**
> device_enrollment_program_v1_edit_dep_profile(dep_profile_model, profile_uuid)

New - Edit an existing Device Enrollment Program profile.

Edits the Device Enrollment Program profile if the profile ID is correct. The edited profile is also registered with the Apple server.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
dep_profile_model = mdmv1.MdmEnrollmentProgramApiModel_() # MdmEnrollmentProgramApiModel_ | The Device Enrollment program profile model containing the required profile properties. (Required).
profile_uuid = 'profile_uuid_example' # str | The unique identifier for the device enrollment program profile. (Required).

try:
    # New - Edit an existing Device Enrollment Program profile.
    api_instance.device_enrollment_program_v1_edit_dep_profile(dep_profile_model, profile_uuid)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_edit_dep_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dep_profile_model** | [**MdmEnrollmentProgramApiModel_**](MdmEnrollmentProgramApiModel_.md)| The Device Enrollment program profile model containing the required profile properties. (Required). | 
 **profile_uuid** | **str**| The unique identifier for the device enrollment program profile. (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_get_dep_certificate_async**
> str device_enrollment_program_v1_get_dep_certificate_async(cert_id)

New - Get Device Enrollment Program certificate to upload in the Device Enrollment Program portal.

Gets the generated .pem certificate for the provided certificate ID. This certificate needs to be uploaded in the Device Enrollment Program Apple portal to continue setting up Device Enrollment Program in the organization group.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
cert_id = 789 # int | The certificate id of the certificate being requested. (Required).

try:
    # New - Get Device Enrollment Program certificate to upload in the Device Enrollment Program portal.
    api_response = api_instance.device_enrollment_program_v1_get_dep_certificate_async(cert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_get_dep_certificate_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **int**| The certificate id of the certificate being requested. (Required). | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-pem-file;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_get_dep_devices**
> list[DeviceEnrollmentProgramDevicesResponseV1Model] device_enrollment_program_v1_get_dep_devices(group_uuid)

New - Gets all Apple Device Enrollment Program devices at organization group.

Returns all the Apple Device Enrollment Program devices that have been synced into AirWatch for the given organization group.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
group_uuid = 'group_uuid_example' # str | Organization group UUID to perform the operation on.(Required)

try:
    # New - Gets all Apple Device Enrollment Program devices at organization group.
    api_response = api_instance.device_enrollment_program_v1_get_dep_devices(group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_get_dep_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | **str**| Organization group UUID to perform the operation on.(Required) | 

### Return type

[**list[DeviceEnrollmentProgramDevicesResponseV1Model]**](DeviceEnrollmentProgramDevicesResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_get_dep_devices_for_profile**
> list[DeviceEnrollmentProgramDevicesResponseV1Model] device_enrollment_program_v1_get_dep_devices_for_profile(profile_uuid, page=page, page_size=page_size)

New - Gets all Apple Device Enrollment Program devices assigned to the profile.

Returns all the Apple Device Enrollment Program devices that have been synced into AirWatch and assigned to the given profile unique key.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
profile_uuid = 'profile_uuid_example' # str | Device Enrollment Program profile unique key to get the device list for.(Required)
page = 56 # int | Specific page number to get. 0 based index (optional)
page_size = 56 # int | Maximum records per page. Default 500 (optional)

try:
    # New - Gets all Apple Device Enrollment Program devices assigned to the profile.
    api_response = api_instance.device_enrollment_program_v1_get_dep_devices_for_profile(profile_uuid, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_get_dep_devices_for_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Device Enrollment Program profile unique key to get the device list for.(Required) | 
 **page** | **int**| Specific page number to get. 0 based index | [optional] 
 **page_size** | **int**| Maximum records per page. Default 500 | [optional] 

### Return type

[**list[DeviceEnrollmentProgramDevicesResponseV1Model]**](DeviceEnrollmentProgramDevicesResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_reconcile_dep_devices**
> device_enrollment_program_v1_reconcile_dep_devices(group_uuid, action)

New - Fetches or syncs Apple Device Enrollment Program devices belonging to the organization group.

Fetches or syncs devices from the Apple server associated with the token uploaded in the given organization group based on the action flag.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
group_uuid = 'group_uuid_example' # str | Organization group UUID to perform the operation on.(Required)
action = '' # str | Action flag is used to determine if the fetch or sync action must be performed for the devices. Valid values are Sync and Fetch. Sync will only get the changed devices from the Apple server while fetch will get all devices associated with the token from the Apple server.(Required) (default to )

try:
    # New - Fetches or syncs Apple Device Enrollment Program devices belonging to the organization group.
    api_instance.device_enrollment_program_v1_reconcile_dep_devices(group_uuid, action)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_reconcile_dep_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | **str**| Organization group UUID to perform the operation on.(Required) | 
 **action** | **str**| Action flag is used to determine if the fetch or sync action must be performed for the devices. Valid values are Sync and Fetch. Sync will only get the changed devices from the Apple server while fetch will get all devices associated with the token from the Apple server.(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_save_dep_authentication_entity_async**
> int device_enrollment_program_v1_save_dep_authentication_entity_async(organization_group_id, dep_account_creation_model)

New - Create a new DEP account for the organization group.

Creates a new Device Enrollment Program account for the given organization group ID based on the provided token and certificate. This account will be used to make all subsequent requests to the Apple server.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
organization_group_id = 56 # int | This is the organization group identifier also known as GroupID. Typically used during enrollment.(Required).
dep_account_creation_model = mdmv1.DepAccountCreationApiModel() # DepAccountCreationApiModel | The dep Account Creation Model containing the token ID and the certificate ID that will be used to generate the device enrollment program account for the organization group. (Required).

try:
    # New - Create a new DEP account for the organization group.
    api_response = api_instance.device_enrollment_program_v1_save_dep_authentication_entity_async(organization_group_id, dep_account_creation_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_save_dep_authentication_entity_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_id** | **int**| This is the organization group identifier also known as GroupID. Typically used during enrollment.(Required). | 
 **dep_account_creation_model** | [**DepAccountCreationApiModel**](DepAccountCreationApiModel.md)| The dep Account Creation Model containing the token ID and the certificate ID that will be used to generate the device enrollment program account for the organization group. (Required). | 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_save_dep_certificate_async**
> int device_enrollment_program_v1_save_dep_certificate_async(organization_group_id)

New - Generate a new Device Enrollment Program certificate.

Generates a new .pem certificate for the provided organization group ID. This certificate needs to be uploaded in the Device Enrollment Program Apple portal to continue setting up Device Enrollment Program in the organization group.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
organization_group_id = 56 # int | This is the organization group identifier also known as GroupID. Typically used during enrollment.(Required).

try:
    # New - Generate a new Device Enrollment Program certificate.
    api_response = api_instance.device_enrollment_program_v1_save_dep_certificate_async(organization_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_save_dep_certificate_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_id** | **int**| This is the organization group identifier also known as GroupID. Typically used during enrollment.(Required). | 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_search**
> MdmEnrollmentProgramSearchResultV1Model device_enrollment_program_v1_search(organization_group_uuid=organization_group_uuid, search_text=search_text, page=page, page_size=page_size, order_by=order_by, sort_order=sort_order)

Returns a collection of Device enrollment program profiles based on the search criteria.

Returns a collection of device enrollment program profiles based on the search criteria specified. The search parameters can be organization group ID, page, and the pagesize.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid =  # object | Organization Group UUID. (Example:FFD1521E-70D7-4673-A0EF-62938079C0E8, FFD1521E-70D7-4673-A0EF-62938079C0E8) (optional) (default to )
search_text = '' # str | Profile name. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index (optional)
page_size = 56 # int | Maximum records per page. Default 50 (optional)
order_by = '' # str | Order By. Default Asc (Example:Asc,Dsc) (optional) (default to )
sort_order = '' # str | Sort Order. Default DeviceProfileName (Example:DeviceProfileName,RootLocationGroupName) (optional) (default to )

try:
    # Returns a collection of Device enrollment program profiles based on the search criteria.
    api_response = api_instance.device_enrollment_program_v1_search(organization_group_uuid=organization_group_uuid, search_text=search_text, page=page, page_size=page_size, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**object**](.md)| Organization Group UUID. (Example:FFD1521E-70D7-4673-A0EF-62938079C0E8, FFD1521E-70D7-4673-A0EF-62938079C0E8) | [optional] [default to ]
 **search_text** | **str**| Profile name. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index | [optional] 
 **page_size** | **int**| Maximum records per page. Default 50 | [optional] 
 **order_by** | **str**| Order By. Default Asc (Example:Asc,Dsc) | [optional] [default to ]
 **sort_order** | **str**| Sort Order. Default DeviceProfileName (Example:DeviceProfileName,RootLocationGroupName) | [optional] [default to ]

### Return type

[**MdmEnrollmentProgramSearchResultV1Model**](MdmEnrollmentProgramSearchResultV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_enrollment_program_v1_view_shared_mdm_profile_data_async**
> MdmEnrollmentProgramApiModel device_enrollment_program_v1_view_shared_mdm_profile_data_async(profile_uuid)

New - Get Device Enrollment Program profile based on the profile unique identifier.

Gets the details of the saved Device Enrollment Program profile created based on the provided profile unique identifier.

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
api_instance = mdmv1.DeviceEnrollmentProgramV1Api(mdmv1.ApiClient(configuration))
profile_uuid = 'profile_uuid_example' # str | The unique identifier for the device enrollment program profile. (Required).

try:
    # New - Get Device Enrollment Program profile based on the profile unique identifier.
    api_response = api_instance.device_enrollment_program_v1_view_shared_mdm_profile_data_async(profile_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceEnrollmentProgramV1Api->device_enrollment_program_v1_view_shared_mdm_profile_data_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| The unique identifier for the device enrollment program profile. (Required). | 

### Return type

[**MdmEnrollmentProgramApiModel**](MdmEnrollmentProgramApiModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

