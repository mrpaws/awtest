# mdmv1.SecurityV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**security_v1_device_security_info_search**](SecurityV1Api.md#security_v1_device_security_info_search) | **GET** /devices/securityinfosearch | Searches for Device Security Information for the device.
[**security_v1_get_device_encryption_status_async**](SecurityV1Api.md#security_v1_get_device_encryption_status_async) | **GET** /devices/{uuid}/security/encryption-status | New - Get encryption status of an enrolled device.
[**security_v1_get_device_recovery_lock_password_async**](SecurityV1Api.md#security_v1_get_device_recovery_lock_password_async) | **GET** /devices/{uuid}/security/recovery-lock-password | New - Gets the Recovery Lock password for a macOS device.
[**security_v1_get_device_security_info_async**](SecurityV1Api.md#security_v1_get_device_security_info_async) | **GET** /devices/{id}/security | Retrieves the security information of the device identified by device ID.
[**security_v1_get_device_security_info_by_alternateid_async**](SecurityV1Api.md#security_v1_get_device_security_info_by_alternateid_async) | **GET** /devices/security | Retrieves the security information of the device identified by device ID.
[**security_v1_get_managed_admin_information**](SecurityV1Api.md#security_v1_get_managed_admin_information) | **GET** /devices/{uuid}/security/managed-admin-information | New - Get information of the administrator account configured on a macOS device via the device enrollment program (DEP).


# **security_v1_device_security_info_search**
> DeviceSecurityInfoSearchResult security_v1_device_security_info_search(organizationgroupid, user, model=model, platform=platform, lastseen=lastseen, ownership=ownership, compliantstatus=compliantstatus, seensince=seensince, page=page, pagesize=pagesize)

Searches for Device Security Information for the device.

Processes the information like organizationgroup ID, user name, model, platform, last seen, ownership, compliant status,              seen since parameters and fetches the security information for the same.

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
api_instance = mdmv1.SecurityV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | OrganizationGroup to be searched, user's OG is considered if not sent. e.g.[testOrganizationGroup] (Required).
user = '' # str | Enrolled username. e.g.[testUser] (Required). (default to )
model = '' # str | Device model. e.g.[iPhone].  (optional) (default to )
platform = 56 # int | Device platform. e.g.[Apple].  (optional)
lastseen = '' # datetime | Last seen date string. e.g. [2017-02-03 01:33:07.383]. (optional) (default to )
ownership = '' # str | Ownership. e.g. [C:Corporate Dedicated, E:Employee Owned, S:Corporate Shared]. (optional) (default to )
compliantstatus =  # bool | Complaint status [True or False]. (optional) (default to )
seensince = '' # datetime | Specifies the date filter for device search, which retrieves the devices that are seen after this date e.g. [2017-02-03 01:33:07.383]. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Searches for Device Security Information for the device.
    api_response = api_instance.security_v1_device_security_info_search(organizationgroupid, user, model=model, platform=platform, lastseen=lastseen, ownership=ownership, compliantstatus=compliantstatus, seensince=seensince, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityV1Api->security_v1_device_security_info_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| OrganizationGroup to be searched, user&#39;s OG is considered if not sent. e.g.[testOrganizationGroup] (Required). | 
 **user** | **str**| Enrolled username. e.g.[testUser] (Required). | [default to ]
 **model** | **str**| Device model. e.g.[iPhone].  | [optional] [default to ]
 **platform** | **int**| Device platform. e.g.[Apple].  | [optional] 
 **lastseen** | **datetime**| Last seen date string. e.g. [2017-02-03 01:33:07.383]. | [optional] [default to ]
 **ownership** | **str**| Ownership. e.g. [C:Corporate Dedicated, E:Employee Owned, S:Corporate Shared]. | [optional] [default to ]
 **compliantstatus** | **bool**| Complaint status [True or False]. | [optional] [default to ]
 **seensince** | **datetime**| Specifies the date filter for device search, which retrieves the devices that are seen after this date e.g. [2017-02-03 01:33:07.383]. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**DeviceSecurityInfoSearchResult**](DeviceSecurityInfoSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_v1_get_device_encryption_status_async**
> DeviceEncryptionStatus security_v1_get_device_encryption_status_async(uuid)

New - Get encryption status of an enrolled device.

Get encryption status of an enrolled device identified by device Uuid.

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
api_instance = mdmv1.SecurityV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Unique identifier (Uuid) of a device.(Required)

try:
    # New - Get encryption status of an enrolled device.
    api_response = api_instance.security_v1_get_device_encryption_status_async(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityV1Api->security_v1_get_device_encryption_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique identifier (Uuid) of a device.(Required) | 

### Return type

[**DeviceEncryptionStatus**](DeviceEncryptionStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_v1_get_device_recovery_lock_password_async**
> DeviceRecoveryLockPasswordResponseV1Model security_v1_get_device_recovery_lock_password_async(uuid)

New - Gets the Recovery Lock password for a macOS device.

Gets the Recovery Lock password for a macOS device identified by the device Uuid. Applicable for macOS 11.5+ and available with Apple Silicon.

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
api_instance = mdmv1.SecurityV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Unique identifier (Uuid) of a device.(Required).

try:
    # New - Gets the Recovery Lock password for a macOS device.
    api_response = api_instance.security_v1_get_device_recovery_lock_password_async(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityV1Api->security_v1_get_device_recovery_lock_password_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique identifier (Uuid) of a device.(Required). | 

### Return type

[**DeviceRecoveryLockPasswordResponseV1Model**](DeviceRecoveryLockPasswordResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_v1_get_device_security_info_async**
> DeviceSecurityInfo security_v1_get_device_security_info_async(id)

Retrieves the security information of the device identified by device ID.

Processes the device ID to retrieve the security information sample related info. Security Info Sample for that device              needs to be reported to the server prior to the call in order to get successful response. This API will fetch security info by              device ID.

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
api_instance = mdmv1.SecurityV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID. (Required).

try:
    # Retrieves the security information of the device identified by device ID.
    api_response = api_instance.security_v1_get_device_security_info_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityV1Api->security_v1_get_device_security_info_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID. (Required). | 

### Return type

[**DeviceSecurityInfo**](DeviceSecurityInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_v1_get_device_security_info_by_alternateid_async**
> DeviceSecurityInfo security_v1_get_device_security_info_by_alternateid_async(search_by, id)

Retrieves the security information of the device identified by device ID.

Processes the device id to retrieve the security information sample related info. Security Info Sample for that device              needs to be reported to the server prior to the call in order to get successful response. This API will fetch security info by alternate ID              of the device.

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
api_instance = mdmv1.SecurityV1Api(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Required). (default to )
id = '' # str | The alternate ID of the device. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837)(Required). (default to )

try:
    # Retrieves the security information of the device identified by device ID.
    api_response = api_instance.security_v1_get_device_security_info_by_alternateid_async(search_by, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityV1Api->security_v1_get_device_security_info_by_alternateid_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber]. (Required). | [default to ]
 **id** | **str**| The alternate ID of the device. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837)(Required). | [default to ]

### Return type

[**DeviceSecurityInfo**](DeviceSecurityInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_v1_get_managed_admin_information**
> ManagedAdminInformationResponseV1Model security_v1_get_managed_admin_information(uuid)

New - Get information of the administrator account configured on a macOS device via the device enrollment program (DEP).

Get information of the administrator account configured on a macOS device via the device enrollment program (DEP). It includes the name for the account, current and the old passwords for the account, and the date and time of the day on which the administrator password was last rotated. If a unique random password is generated for the account, for security reasons, a command will be queued automatically to rotate the administrator password in 8 hour(s) from when the information was accessed.

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
api_instance = mdmv1.SecurityV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Universally unique identifier (UUID) of a device.(Required)

try:
    # New - Get information of the administrator account configured on a macOS device via the device enrollment program (DEP).
    api_response = api_instance.security_v1_get_managed_admin_information(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityV1Api->security_v1_get_managed_admin_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Universally unique identifier (UUID) of a device.(Required) | 

### Return type

[**ManagedAdminInformationResponseV1Model**](ManagedAdminInformationResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

