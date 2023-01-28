# mdmv1.ChromeOsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chrome_os_v1_add_cloud_profile_async**](ChromeOsV1Api.md#chrome_os_v1_add_cloud_profile_async) | **POST** /chromeos/{groupId}/devicePolicy | New - Create a new Device Policy profile for the given organization Group
[**chrome_os_v1_createor_update_user_profile_async**](ChromeOsV1Api.md#chrome_os_v1_createor_update_user_profile_async) | **POST** /chromeos/{groupId}/userPolicy | New - Creates or Updates user policy for all the users in usergroups
[**chrome_os_v1_delete_chrome_book_configuration**](ChromeOsV1Api.md#chrome_os_v1_delete_chrome_book_configuration) | **DELETE** /chromeos/configuration/{groupId} | New - Deletes the ChromeBook Configuration Settings for a Organization Group
[**chrome_os_v1_delete_chrome_os_profile_async**](ChromeOsV1Api.md#chrome_os_v1_delete_chrome_os_profile_async) | **DELETE** /chromeos/cloudprofile/{profileId} | New - Deletes the Chrome OS Profile
[**chrome_os_v1_edit_cloud_profile**](ChromeOsV1Api.md#chrome_os_v1_edit_cloud_profile) | **PUT** /chromeos/{groupId}/policy/{policyId} | New - Edit the existing Device Policy profile by creating a version of the settings
[**chrome_os_v1_get_chrome_book_configuration**](ChromeOsV1Api.md#chrome_os_v1_get_chrome_book_configuration) | **GET** /chromeos/configuration/{groupId} | New - loads the ChromeBook Configuration Settings for an Organization Group
[**chrome_os_v1_get_cloud_profile_async**](ChromeOsV1Api.md#chrome_os_v1_get_cloud_profile_async) | **GET** /chromeos/{groupId}/policy/{policyId} | New - Retrieve the existing Policy profile
[**chrome_os_v1_get_cloud_profile_metadata_async**](ChromeOsV1Api.md#chrome_os_v1_get_cloud_profile_metadata_async) | **GET** /chromeos/{groupId}/cloudprofile/{profileId}/profileType/{profileType} | New - Get Metadata for loading device Policy cloud profile UI
[**chrome_os_v1_get_policy_async**](ChromeOsV1Api.md#chrome_os_v1_get_policy_async) | **GET** /chromeos/devices/{deviceId}/policy | New - Get the status of the update by returning the policy on the device
[**chrome_os_v1_insert_chrome_book_configuration**](ChromeOsV1Api.md#chrome_os_v1_insert_chrome_book_configuration) | **POST** /chromeos/configuration/{groupId} | New - Saves the ChromeBook Configuration Settings for an Organization Group
[**chrome_os_v1_set_lost_mode_async**](ChromeOsV1Api.md#chrome_os_v1_set_lost_mode_async) | **PUT** /chromeos/{deviceId}/lostmode/{isEnabled} | New - Enable or disable the device lost mode.
[**chrome_os_v1_sync_devices_async**](ChromeOsV1Api.md#chrome_os_v1_sync_devices_async) | **POST** /chromeos/{groupId}/devices/sync | New - Executes device sync command for the given organization group.


# **chrome_os_v1_add_cloud_profile_async**
> chrome_os_v1_add_cloud_profile_async(form_data, group_id)

New - Create a new Device Policy profile for the given organization Group

Device Policy profile will have customized settings that can be applied on a Chrome device. These settings include auto-Launched Kiosk App,device Heartbeat monitor rate,application Settings for specifying list of apps that can be force-installed on a device,Email/SMS deviceStatus Alert Delivery settings etc.

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
form_data = mdmv1.DdFormPayloadV1Model() # DdFormPayloadV1Model | Kiosk Device policy to manage a chrome device(Required)
group_id = 'group_id_example' # str | Organization group Identifier where the devicePolicy profile needs to be created.(Required)

try:
    # New - Create a new Device Policy profile for the given organization Group
    api_instance.chrome_os_v1_add_cloud_profile_async(form_data, group_id)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_add_cloud_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_data** | [**DdFormPayloadV1Model**](DdFormPayloadV1Model.md)| Kiosk Device policy to manage a chrome device(Required) | 
 **group_id** | **str**| Organization group Identifier where the devicePolicy profile needs to be created.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chrome_os_v1_createor_update_user_profile_async**
> chrome_os_v1_createor_update_user_profile_async(form_data, group_id)

New - Creates or Updates user policy for all the users in usergroups

User Policy profile will have customized settings that can be pushed to users on a Chrome device. These settings include incognito mode restrictions,application blacklisting,network settings,vpn etc.

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
form_data = mdmv1.DdFormPayloadV1Model() # DdFormPayloadV1Model | User Policy Settings to push to a user(Required)
group_id = 'group_id_example' # str | Organization group Identifier where the User Policy profile needs to be created.(Required)

try:
    # New - Creates or Updates user policy for all the users in usergroups
    api_instance.chrome_os_v1_createor_update_user_profile_async(form_data, group_id)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_createor_update_user_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_data** | [**DdFormPayloadV1Model**](DdFormPayloadV1Model.md)| User Policy Settings to push to a user(Required) | 
 **group_id** | **str**| Organization group Identifier where the User Policy profile needs to be created.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chrome_os_v1_delete_chrome_book_configuration**
> chrome_os_v1_delete_chrome_book_configuration(group_id)

New - Deletes the ChromeBook Configuration Settings for a Organization Group

Deletes the ChromeBook Configuration settings of an Organization Group

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
group_id = 'group_id_example' # str | The customer code of the organization group whose configuration will be deleted.(Required)

try:
    # New - Deletes the ChromeBook Configuration Settings for a Organization Group
    api_instance.chrome_os_v1_delete_chrome_book_configuration(group_id)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_delete_chrome_book_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The customer code of the organization group whose configuration will be deleted.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chrome_os_v1_delete_chrome_os_profile_async**
> chrome_os_v1_delete_chrome_os_profile_async(profile_id)

New - Deletes the Chrome OS Profile

Deletes the Specified Chrome OS Profile by passing Device profile Id.

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
profile_id = 56 # int | Defines the profile that needs to be deleted(Required)

try:
    # New - Deletes the Chrome OS Profile
    api_instance.chrome_os_v1_delete_chrome_os_profile_async(profile_id)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_delete_chrome_os_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**| Defines the profile that needs to be deleted(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chrome_os_v1_edit_cloud_profile**
> chrome_os_v1_edit_cloud_profile(group_id, policy_id, device_policy_data)

New - Edit the existing Device Policy profile by creating a version of the settings

Device Policy profile will have customized settings (key/value pairs with pre-defined airwatch specific keys) that can be applied on a Chrome device.These settings include auto-Launched Kiosk App,device Heartbeat monitor rate,applicationSettings for specifying list of apps that can be force-installed on a device,Email/SMS deviceStatus Alert Delivery settings etc. *On editing a cloud policy, new version of the settings will be created.*

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
group_id = 'group_id_example' # str | Organization group Identifier where the devicePolicy profile needs to be updated.(Required)
policy_id = 'policy_id_example' # str | AW internal devicePolicy profile identifier(Required)
device_policy_data = 'device_policy_data_example' # str | Kiosk Device policy to manage a chrome device(Required)

try:
    # New - Edit the existing Device Policy profile by creating a version of the settings
    api_instance.chrome_os_v1_edit_cloud_profile(group_id, policy_id, device_policy_data)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_edit_cloud_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Organization group Identifier where the devicePolicy profile needs to be updated.(Required) | 
 **policy_id** | **str**| AW internal devicePolicy profile identifier(Required) | 
 **device_policy_data** | **str**| Kiosk Device policy to manage a chrome device(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chrome_os_v1_get_chrome_book_configuration**
> ChromeOSConfigurationV1Model chrome_os_v1_get_chrome_book_configuration(group_id)

New - loads the ChromeBook Configuration Settings for an Organization Group

Loads the ChromeBook Configuration of a Domain for an Organization Group

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
group_id = 'group_id_example' # str | The customer code of the organization group whose configuration will be returned.(Required)

try:
    # New - loads the ChromeBook Configuration Settings for an Organization Group
    api_response = api_instance.chrome_os_v1_get_chrome_book_configuration(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_get_chrome_book_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The customer code of the organization group whose configuration will be returned.(Required) | 

### Return type

[**ChromeOSConfigurationV1Model**](ChromeOSConfigurationV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chrome_os_v1_get_cloud_profile_async**
> ChromeOsPolicySettingsV1Model chrome_os_v1_get_cloud_profile_async(group_id, policy_id)

New - Retrieve the existing Policy profile

Device/User Policy profile will have customized settings (key/value pairs with pre-defined airwatch specific keys) that can be applied on a Chrome device.These settings include auto-Launched Kiosk App,device Heartbeat monitor rate,application Settings for specifying list of apps that can be force-installed on a device,Email/SMS deviceStatus Alert Delivery settings etc. *On editing a cloud policy, new version of the settings will be created.*

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
group_id = 'group_id_example' # str | The identifier for the organization group where the policy is being requested.(Required)
policy_id = 'policy_id_example' # str | AW internal devicePolicy profile identifier(Required)

try:
    # New - Retrieve the existing Policy profile
    api_response = api_instance.chrome_os_v1_get_cloud_profile_async(group_id, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_get_cloud_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The identifier for the organization group where the policy is being requested.(Required) | 
 **policy_id** | **str**| AW internal devicePolicy profile identifier(Required) | 

### Return type

[**ChromeOsPolicySettingsV1Model**](ChromeOsPolicySettingsV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chrome_os_v1_get_cloud_profile_metadata_async**
> ChromeOsPolicySettingsV1Model chrome_os_v1_get_cloud_profile_metadata_async(group_id, profile_id, profile_type, read_only=read_only)

New - Get Metadata for loading device Policy cloud profile UI

Device or User Policy profile will have customized settings (key/value pairs with pre-defined airwatch specific keys) that can be applied on a Chrome device.These settings include network, VPN, URL Access control, Sign In, auto-Launched Kiosk App,device Heartbeat monitor rate,application Settings for specifying list of apps that can be force-installed on a device,Email/SMS deviceStatus Alert Delivery settings etc. *On editing a cloud profile, new version of the settings will be created.*

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
group_id = 'group_id_example' # str | The identifier for the organization group where the metadata is being requested.(Required)
profile_id = 'profile_id_example' # str | AW internal devicePolicy profile identifier(Required)
profile_type = 56 # int | Type of profile 1 is Device Profile 2 is User Profile(Required)
read_only =  # bool | Boolean flag to determine if the metadata returned should render the form in read only mode. (optional) (default to )

try:
    # New - Get Metadata for loading device Policy cloud profile UI
    api_response = api_instance.chrome_os_v1_get_cloud_profile_metadata_async(group_id, profile_id, profile_type, read_only=read_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_get_cloud_profile_metadata_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The identifier for the organization group where the metadata is being requested.(Required) | 
 **profile_id** | **str**| AW internal devicePolicy profile identifier(Required) | 
 **profile_type** | **int**| Type of profile 1 is Device Profile 2 is User Profile(Required) | 
 **read_only** | **bool**| Boolean flag to determine if the metadata returned should render the form in read only mode. | [optional] [default to ]

### Return type

[**ChromeOsPolicySettingsV1Model**](ChromeOsPolicySettingsV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chrome_os_v1_get_policy_async**
> ChromeOsV1Model chrome_os_v1_get_policy_async(device_id)

New - Get the status of the update by returning the policy on the device

Get the list of policies applied to a device

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
device_id = 'device_id_example' # str | Google-assigned device identifier whose policy is updated(Required)

try:
    # New - Get the status of the update by returning the policy on the device
    api_response = api_instance.chrome_os_v1_get_policy_async(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_get_policy_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Google-assigned device identifier whose policy is updated(Required) | 

### Return type

[**ChromeOsV1Model**](ChromeOsV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chrome_os_v1_insert_chrome_book_configuration**
> chrome_os_v1_insert_chrome_book_configuration(chromebook_configuration_model, group_id)

New - Saves the ChromeBook Configuration Settings for an Organization Group

Saves the ChromeBook Configuration of a Domain for an Organization Group

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
chromebook_configuration_model = mdmv1.ChromeOSConfigurationV1Model() # ChromeOSConfigurationV1Model | Chromebook Configuration Settings(Required)
group_id = 'group_id_example' # str | The customer code of the organization group where configuration needs to be added.(Required)

try:
    # New - Saves the ChromeBook Configuration Settings for an Organization Group
    api_instance.chrome_os_v1_insert_chrome_book_configuration(chromebook_configuration_model, group_id)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_insert_chrome_book_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chromebook_configuration_model** | [**ChromeOSConfigurationV1Model**](ChromeOSConfigurationV1Model.md)| Chromebook Configuration Settings(Required) | 
 **group_id** | **str**| The customer code of the organization group where configuration needs to be added.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chrome_os_v1_set_lost_mode_async**
> chrome_os_v1_set_lost_mode_async(device_id, is_enabled)

New - Enable or disable the device lost mode.

Enable or disable the device lost mode, device will be locked when it is in the lost mode.

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
device_id = 'device_id_example' # str | Defines the device id.(Required)
is_enabled = true # bool | Flag to indicate enable or disable lost mode.(Required)

try:
    # New - Enable or disable the device lost mode.
    api_instance.chrome_os_v1_set_lost_mode_async(device_id, is_enabled)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_set_lost_mode_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Defines the device id.(Required) | 
 **is_enabled** | **bool**| Flag to indicate enable or disable lost mode.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chrome_os_v1_sync_devices_async**
> chrome_os_v1_sync_devices_async(group_id, enrollment_date=enrollment_date)

New - Executes device sync command for the given organization group.

Saves all devices enrolled on or after the specified date from Google Cloud into AirWatch.

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
api_instance = mdmv1.ChromeOsV1Api(mdmv1.ApiClient(configuration))
group_id = 'group_id_example' # str | The customer code of the organization group that the devices belong to.(Required)
enrollment_date = '' # datetime | Retrieve all devices enrolled on or after this date in YYYY-MM-DDTHH:MM:SSZ format(Example - \"2013-03-23T14:23:05\"). (optional) (default to )

try:
    # New - Executes device sync command for the given organization group.
    api_instance.chrome_os_v1_sync_devices_async(group_id, enrollment_date=enrollment_date)
except ApiException as e:
    print("Exception when calling ChromeOsV1Api->chrome_os_v1_sync_devices_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The customer code of the organization group that the devices belong to.(Required) | 
 **enrollment_date** | **datetime**| Retrieve all devices enrolled on or after this date in YYYY-MM-DDTHH:MM:SSZ format(Example - \&quot;2013-03-23T14:23:05\&quot;). | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

