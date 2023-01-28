# systemv2.UsersV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_v2_create**](UsersV2Api.md#users_v2_create) | **POST** /users | New - Create an enrollment user
[**users_v2_delete_async**](UsersV2Api.md#users_v2_delete_async) | **DELETE** /users/{uuid} | New - Delete an enrollment user by UUID
[**users_v2_read**](UsersV2Api.md#users_v2_read) | **GET** /users/{uuid} | New - Read an enrollment user by UUID
[**users_v2_update_async**](UsersV2Api.md#users_v2_update_async) | **PUT** /users/{uuid} | New - Update an enrollment user by UUID


# **users_v2_create**
> users_v2_create(user)

New - Create an enrollment user

Create an enrollment user with attributes including externalId, userName, password, firstName, lastName, displayName, userPrincipalName, emailAddress, phoneNumber, mobileNumber, messageType, messageTemplateUuid, enrollmentRoleUuid, status, securityType, deviceStagingEnabled, deviceStagingType, organizationGroupUuid, enrollmentOrganizationGroupUuid, aadMappingAttribute, department, employeeIdentifier, costCenter, customAttribute1, customAttribute2, customAttribute3, customAttribute4 and customAttribute5. &lt;br/&gt;&lt;br/&gt;UsersV2 API support syncing of users into the Workspace ONE Access from Workspace ONE UEM.

### Example
```python
from __future__ import print_function
import time
import systemv2
from systemv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv2.UsersV2Api(systemv2.ApiClient(configuration))
user = systemv2.CreateEnrollmentUserV2Model() # CreateEnrollmentUserV2Model | Enrollment user attributes(Required)

try:
    # New - Create an enrollment user
    api_instance.users_v2_create(user)
except ApiException as e:
    print("Exception when calling UsersV2Api->users_v2_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**CreateEnrollmentUserV2Model**](CreateEnrollmentUserV2Model.md)| Enrollment user attributes(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v2_delete_async**
> users_v2_delete_async(uuid)

New - Delete an enrollment user by UUID

Delete an enrollment user by UUID. &lt;br/&gt;&lt;br/&gt;UsersV2 API support syncing of users into the Workspace ONE Access from Workspace ONE UEM.

### Example
```python
from __future__ import print_function
import time
import systemv2
from systemv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv2.UsersV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier of an enrollment user(Required)

try:
    # New - Delete an enrollment user by UUID
    api_instance.users_v2_delete_async(uuid)
except ApiException as e:
    print("Exception when calling UsersV2Api->users_v2_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier of an enrollment user(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v2_read**
> ReadEnrollmentUserV2Model users_v2_read(uuid)

New - Read an enrollment user by UUID

Read an enrollment user attributes including uuid, externalId, domain, userName, firstName, lastName, displayName, fullName, userPrincipalName, emailAddress, phoneNumber, mobileNumber, emailUserName, messageType, messageTemplateUuid, enrollmentRoleUuid, status, securityType, deviceStagingType, enrolledDeviceCount, organizationGroupUuid, enrollmentOrganizationGroupUuid, aadMappingAttribute, department, employeeIdentifier, costCenter, customAttribute1, customAttribute2, customAttribute3, customAttribute4 and customAttribute5

### Example
```python
from __future__ import print_function
import time
import systemv2
from systemv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv2.UsersV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier of an enrollment user(Required)

try:
    # New - Read an enrollment user by UUID
    api_response = api_instance.users_v2_read(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersV2Api->users_v2_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier of an enrollment user(Required) | 

### Return type

[**ReadEnrollmentUserV2Model**](ReadEnrollmentUserV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v2_update_async**
> users_v2_update_async(uuid, user)

New - Update an enrollment user by UUID

Update the enrollment user with attributes including password, firstName, lastName, displayName, emailAddress, phoneNumber, mobileNumber, messageType, messageTemplateUuid, deviceStagingEnabled, deviceStagingType,  enrollmentRoleUuid, enrollmentOrganizationGroupUuid, aadMappingAttribute, department, employeeIdentifier, costCenter, customAttribute1, customAttribute2, customAttribute3, customAttribute4 and customAttribute5. &lt;br/&gt;&lt;br/&gt;UsersV2 API support syncing of users into the Workspace ONE Access from Workspace ONE UEM.

### Example
```python
from __future__ import print_function
import time
import systemv2
from systemv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv2.UsersV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier of an enrollment user(Required)
user = systemv2.UpdateEnrollmentUserV2Model() # UpdateEnrollmentUserV2Model | Enrollment user attributes(Required)

try:
    # New - Update an enrollment user by UUID
    api_instance.users_v2_update_async(uuid, user)
except ApiException as e:
    print("Exception when calling UsersV2Api->users_v2_update_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier of an enrollment user(Required) | 
 **user** | [**UpdateEnrollmentUserV2Model**](UpdateEnrollmentUserV2Model.md)| Enrollment user attributes(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

