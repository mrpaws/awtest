# systemv2.EnrollmentRestrictionPolicyV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrollment_restriction_policy_v2_get_enrollment_restriction_policies**](EnrollmentRestrictionPolicyV2Api.md#enrollment_restriction_policy_v2_get_enrollment_restriction_policies) | **GET** /enrollment/restriction-policies | New - Gets Enrollment Restriction Policies accessible to admin
[**enrollment_restriction_policy_v2_get_enrollment_restriction_policy_details_by_uuid**](EnrollmentRestrictionPolicyV2Api.md#enrollment_restriction_policy_v2_get_enrollment_restriction_policy_details_by_uuid) | **GET** /enrollment/restriction-policies/{uuid} | New - Gets Enrollment Restriction Policy details based on uuid.
[**enrollment_restriction_policy_v2_update**](EnrollmentRestrictionPolicyV2Api.md#enrollment_restriction_policy_v2_update) | **PATCH** /enrollment/restriction-policies/{enrollmentRestrictionPolicyUuid}/organization-group/{organizationGroupUuid} | New - Assigns a list of usergroups to Enrollment Restriction policy


# **enrollment_restriction_policy_v2_get_enrollment_restriction_policies**
> EnrollmentRestrictionsPoliciesResponseModel enrollment_restriction_policy_v2_get_enrollment_restriction_policies()

New - Gets Enrollment Restriction Policies accessible to admin

Fetch Enrollment Restriction Policies accessible to admin. We only return the following properties- name, uuid, organization group uuid

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
api_instance = systemv2.EnrollmentRestrictionPolicyV2Api(systemv2.ApiClient(configuration))

try:
    # New - Gets Enrollment Restriction Policies accessible to admin
    api_response = api_instance.enrollment_restriction_policy_v2_get_enrollment_restriction_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentRestrictionPolicyV2Api->enrollment_restriction_policy_v2_get_enrollment_restriction_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnrollmentRestrictionsPoliciesResponseModel**](EnrollmentRestrictionsPoliciesResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_restriction_policy_v2_get_enrollment_restriction_policy_details_by_uuid**
> EnrollmentRestrictionsPolicyResponseModel enrollment_restriction_policy_v2_get_enrollment_restriction_policy_details_by_uuid(uuid)

New - Gets Enrollment Restriction Policy details based on uuid.

Fetch details for an Enrollment Restriction policy which includes name, uuid, ogname and User group assignments

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
api_instance = systemv2.EnrollmentRestrictionPolicyV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier of an enrollment restriction policy

try:
    # New - Gets Enrollment Restriction Policy details based on uuid.
    api_response = api_instance.enrollment_restriction_policy_v2_get_enrollment_restriction_policy_details_by_uuid(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentRestrictionPolicyV2Api->enrollment_restriction_policy_v2_get_enrollment_restriction_policy_details_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier of an enrollment restriction policy | 

### Return type

[**EnrollmentRestrictionsPolicyResponseModel**](EnrollmentRestrictionsPolicyResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_restriction_policy_v2_update**
> AssignUserGroupsResponse enrollment_restriction_policy_v2_update(enrollment_restriction_policy_uuid, organization_group_uuid, usergroups)

New - Assigns a list of usergroups to Enrollment Restriction policy

Assigns a list of usergroups to Enrollment Restriction policy

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
api_instance = systemv2.EnrollmentRestrictionPolicyV2Api(systemv2.ApiClient(configuration))
enrollment_restriction_policy_uuid = 'enrollment_restriction_policy_uuid_example' # str | Identifier of an enrollment restriction policy(Required)
organization_group_uuid = 'organization_group_uuid_example' # str | Identifier of an enrollment organization group(Required)
usergroups = systemv2.UserGroupsListModel() # UserGroupsListModel | List of User Groups(Required)

try:
    # New - Assigns a list of usergroups to Enrollment Restriction policy
    api_response = api_instance.enrollment_restriction_policy_v2_update(enrollment_restriction_policy_uuid, organization_group_uuid, usergroups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentRestrictionPolicyV2Api->enrollment_restriction_policy_v2_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_restriction_policy_uuid** | [**str**](.md)| Identifier of an enrollment restriction policy(Required) | 
 **organization_group_uuid** | [**str**](.md)| Identifier of an enrollment organization group(Required) | 
 **usergroups** | [**UserGroupsListModel**](UserGroupsListModel.md)| List of User Groups(Required) | 

### Return type

[**AssignUserGroupsResponse**](AssignUserGroupsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

