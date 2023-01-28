# systemv2.OrganizationGroupsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_groups_v2_delete_organization_group**](OrganizationGroupsV2Api.md#organization_groups_v2_delete_organization_group) | **DELETE** /groups/{uuid} | New - Deletes the specified organization group.
[**organization_groups_v2_get_organization_group**](OrganizationGroupsV2Api.md#organization_groups_v2_get_organization_group) | **GET** /groups/{uuid} | New - Retrieves information about the specified organization group.
[**organization_groups_v2_update_organization_group**](OrganizationGroupsV2Api.md#organization_groups_v2_update_organization_group) | **PUT** /groups/{uuid} | New - Updates the metadata of the specified organization group.


# **organization_groups_v2_delete_organization_group**
> organization_groups_v2_delete_organization_group(uuid)

New - Deletes the specified organization group.

Delete organization group by given UUID. It return Forbidden if user want to delete current organization group. It returns bad request,if organization group cannot be deleted.

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
api_instance = systemv2.OrganizationGroupsV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier for an organization group on which operation is to be executed.(Required)

try:
    # New - Deletes the specified organization group.
    api_instance.organization_groups_v2_delete_organization_group(uuid)
except ApiException as e:
    print("Exception when calling OrganizationGroupsV2Api->organization_groups_v2_delete_organization_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier for an organization group on which operation is to be executed.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_groups_v2_get_organization_group**
> OrganizationGroup organization_groups_v2_get_organization_group(uuid)

New - Retrieves information about the specified organization group.

Retrieves organization group by UUID. If Organization goup is not found, it will throw 404 error.

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
api_instance = systemv2.OrganizationGroupsV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier for an organization group on which operation is to be executed.(Required)

try:
    # New - Retrieves information about the specified organization group.
    api_response = api_instance.organization_groups_v2_get_organization_group(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationGroupsV2Api->organization_groups_v2_get_organization_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier for an organization group on which operation is to be executed.(Required) | 

### Return type

[**OrganizationGroup**](OrganizationGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_groups_v2_update_organization_group**
> organization_groups_v2_update_organization_group(uuid, organization_group)

New - Updates the metadata of the specified organization group.

Update the metadata of organization group specified by UUID. It return bad request if organization group name too long or group id too long.

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
api_instance = systemv2.OrganizationGroupsV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Identifier for an organization group on which operation is to be executed.(Required)
organization_group = systemv2.OrganizationGroup() # OrganizationGroup | model containing OG details(Required)

try:
    # New - Updates the metadata of the specified organization group.
    api_instance.organization_groups_v2_update_organization_group(uuid, organization_group)
except ApiException as e:
    print("Exception when calling OrganizationGroupsV2Api->organization_groups_v2_update_organization_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifier for an organization group on which operation is to be executed.(Required) | 
 **organization_group** | [**OrganizationGroup**](OrganizationGroup.md)| model containing OG details(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

