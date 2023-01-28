# systemv1.EnrollmentCustomizationSettingsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrollment_customization_settings_v1_get_enrollment_customizations_settings_for_og_async**](EnrollmentCustomizationSettingsV1Api.md#enrollment_customization_settings_v1_get_enrollment_customizations_settings_for_og_async) | **GET** /groups/{organizationGroupUuid}/settings/enrollment/customization | New - Get Enrollment Customizations settings for the given Organization Group


# **enrollment_customization_settings_v1_get_enrollment_customizations_settings_for_og_async**
> EnrollmentCustomizationSettingsResponseV1Model enrollment_customization_settings_v1_get_enrollment_customizations_settings_for_og_async(organization_group_uuid)

New - Get Enrollment Customizations settings for the given Organization Group

Get the Enrollment Customization settings for the given Organization Group

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
api_instance = systemv1.EnrollmentCustomizationSettingsV1Api(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Identifier of an Organization Group(Required)

try:
    # New - Get Enrollment Customizations settings for the given Organization Group
    api_response = api_instance.enrollment_customization_settings_v1_get_enrollment_customizations_settings_for_og_async(organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentCustomizationSettingsV1Api->enrollment_customization_settings_v1_get_enrollment_customizations_settings_for_og_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Identifier of an Organization Group(Required) | 

### Return type

[**EnrollmentCustomizationSettingsResponseV1Model**](EnrollmentCustomizationSettingsResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

