# mdmv2.SmartGroupsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smart_groups_v2_partial_update_smart_group_async**](SmartGroupsV2Api.md#smart_groups_v2_partial_update_smart_group_async) | **PATCH** /smartgroups/{uuid} | New - Partially updates Smart Group criteria.


# **smart_groups_v2_partial_update_smart_group_async**
> SmartGroupPatchResponseV2Model smart_groups_v2_partial_update_smart_group_async(uuid, smart_groups_operations)

New - Partially updates Smart Group criteria.

 Partially updates Smart Group criteria by adding/removing rules and/or values to rules like Organization groups, user groups, etc.                           ------------Example--------------    [    {op: \"add\", path: \"/smartGroupsOperationsV2/organizationGroups\", value: \"069DC0E2-D4E2-E611-8114-005056AF67FF, 069DC0E2-D4E2-E611-8114-005056AF67FF\"},    {op: \"remove\", path: \"/smartGroupsOperationsV2/users\", value: \"069DC0E2-D4E2-E611-8114-005056AF67FF, 069DC0E2-D4E2-E611-8114-005056AF67FF\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/devices\", value: \"069DC0E2-D4E2-E611-8114-005056AF67FF\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/tags\", value: \"123, 345\"},    {op: \"remove\", path: \"/smartGroupsOperationsV2/platforms\", value: \"WindowsMobile, Apple, BlackBerry, Android, Athena, Motorola, WindowsPhone, WindowsPc, AppleOsX, WindowsPhone8, WinRT, BlackBerry10, AppleTv, Qnx, ChromeBook, ChromeOS\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/managementTypes\", value: \"MdmEnrolled\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/enrollmentCategories\", value: \"DepEnrolled, AndroidEnterprise\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/cpuArchitectures\", value: \"049892B1-BCFE-447A-B34C-52D2BE897715, 1D88CEFE-8959-4E26-BD0C-355889B14378\"}  ]       -----------Platforms--------------    \"WindowsMobile, Apple, BlackBerry, Android, Athena, Motorola, WindowsPhone, WindowsPc, AppleOsX, WindowsPhone8, WinRT, BlackBerry10, AppleTv, Qnx, ChromeBook, ChromeOS\"  -----------Ownerships-------------         \"CorporateDedicated, CorporateShared, EmployeeOwned, AllOwnerships\"      ----------ManagementTypes-------      \"MdmEnrolled, ApplicationManaged, All\"      ----------EnrollmentCategories---      \"DepEnrolled, Supervised, UserApprovedMdmEnrolled, SharedIpad, EduShared, AndroidLegacy, AndroidEnterprise, AadEnrolled, All\"     --- Get all CPU Architectures API /processor-architectures

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
api_instance = mdmv2.SmartGroupsV2Api(mdmv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Smart Group unique identifier(Required).
smart_groups_operations = mdmv2.SmartGroupsOperationsV2ModelPatch() # SmartGroupsOperationsV2ModelPatch | Model containing operation type, resource path and value. Supports add and remove operations.(Required).

try:
    # New - Partially updates Smart Group criteria.
    api_response = api_instance.smart_groups_v2_partial_update_smart_group_async(uuid, smart_groups_operations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartGroupsV2Api->smart_groups_v2_partial_update_smart_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Smart Group unique identifier(Required). | 
 **smart_groups_operations** | [**SmartGroupsOperationsV2ModelPatch**](SmartGroupsOperationsV2ModelPatch.md)| Model containing operation type, resource path and value. Supports add and remove operations.(Required). | 

### Return type

[**SmartGroupPatchResponseV2Model**](SmartGroupPatchResponseV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

