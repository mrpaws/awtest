# mamv2.InternalAppsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**internal_apps_v2_get_application_branch_cache_statistics_async**](InternalAppsV2Api.md#internal_apps_v2_get_application_branch_cache_statistics_async) | **GET** /apps/internal/peerdistribution/branchcache/{bundleid} | New - Gets the BranchCache statistics for the application bundle identifier.
[**internal_apps_v2_get_internal_app_by_uuid**](InternalAppsV2Api.md#internal_apps_v2_get_internal_app_by_uuid) | **GET** /apps/internal/{uuid} | New - Details of an internal app identified by UUID.
[**internal_apps_v2_renew_provisioning_profile**](InternalAppsV2Api.md#internal_apps_v2_renew_provisioning_profile) | **PUT** /apps/internal/provisionings/{uuid} | New - Renew the provisioning profile of all the applications using the given provisioning profile.


# **internal_apps_v2_get_application_branch_cache_statistics_async**
> ApplicationBranchCacheStatisticsModel internal_apps_v2_get_application_branch_cache_statistics_async(bundleid, summary_only=summary_only, application_uuids=application_uuids, device_uuids=device_uuids, smart_group_uuids=smart_group_uuids, organization_group_uuid=organization_group_uuid)

New - Gets the BranchCache statistics for the application bundle identifier.

Gets the BranchCache statistics for application deployments for the application bundle.

### Example
```python
from __future__ import print_function
import time
import mamv2
from mamv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv2.InternalAppsV2Api(mamv2.ApiClient(configuration))
bundleid = 'bundleid_example' # str | The application bundle identifier to query BranchCache statistics.(Required)
summary_only =  # bool | Only the summary of the BranchCache statistics for the application deployments is returned. This is the default behavior if not specified. (optional) (default to )
application_uuids = '' # str | Comma separated list of application UUIDs for the BranchCache statistics of the applications deployed to devices. At least one application must be part of the application bundle. (optional) (default to )
device_uuids = '' # str | Comma separated list of device UUIDs for the BranchCache statistics of the applications deployed to those devices. Must not be specified with smart_group_uuids. (optional) (default to )
smart_group_uuids = '' # str | Comma separated list of smart group UUIDs for the BranchCache statistics of the applications deployed to those smart groups. Must not be specified with device_uuids. (optional) (default to )
organization_group_uuid =  # object | The organization group to limit the BranchCache statistics query to. (optional) (default to )

try:
    # New - Gets the BranchCache statistics for the application bundle identifier.
    api_response = api_instance.internal_apps_v2_get_application_branch_cache_statistics_async(bundleid, summary_only=summary_only, application_uuids=application_uuids, device_uuids=device_uuids, smart_group_uuids=smart_group_uuids, organization_group_uuid=organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV2Api->internal_apps_v2_get_application_branch_cache_statistics_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundleid** | **str**| The application bundle identifier to query BranchCache statistics.(Required) | 
 **summary_only** | **bool**| Only the summary of the BranchCache statistics for the application deployments is returned. This is the default behavior if not specified. | [optional] [default to ]
 **application_uuids** | **str**| Comma separated list of application UUIDs for the BranchCache statistics of the applications deployed to devices. At least one application must be part of the application bundle. | [optional] [default to ]
 **device_uuids** | **str**| Comma separated list of device UUIDs for the BranchCache statistics of the applications deployed to those devices. Must not be specified with smart_group_uuids. | [optional] [default to ]
 **smart_group_uuids** | **str**| Comma separated list of smart group UUIDs for the BranchCache statistics of the applications deployed to those smart groups. Must not be specified with device_uuids. | [optional] [default to ]
 **organization_group_uuid** | [**object**](.md)| The organization group to limit the BranchCache statistics query to. | [optional] [default to ]

### Return type

[**ApplicationBranchCacheStatisticsModel**](ApplicationBranchCacheStatisticsModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v2_get_internal_app_by_uuid**
> InternalAppModel internal_apps_v2_get_internal_app_by_uuid(uuid)

New - Details of an internal app identified by UUID.

Gets the details of an internal app identified by UUID.

### Example
```python
from __future__ import print_function
import time
import mamv2
from mamv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv2.InternalAppsV2Api(mamv2.ApiClient(configuration))
uuid = 'uuid_example' # str | Application UUID(Required)

try:
    # New - Details of an internal app identified by UUID.
    api_response = api_instance.internal_apps_v2_get_internal_app_by_uuid(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV2Api->internal_apps_v2_get_internal_app_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Application UUID(Required) | 

### Return type

[**InternalAppModel**](InternalAppModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v2_renew_provisioning_profile**
> ApplicationsProvisionProfileModel internal_apps_v2_renew_provisioning_profile(uuid)

New - Renew the provisioning profile of all the applications using the given provisioning profile.

Renews the provisioning profile all the applications using the given provisioning profile.

### Example
```python
from __future__ import print_function
import time
import mamv2
from mamv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv2.InternalAppsV2Api(mamv2.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the ptovisioning profile which has to be renewed.(Required)

try:
    # New - Renew the provisioning profile of all the applications using the given provisioning profile.
    api_response = api_instance.internal_apps_v2_renew_provisioning_profile(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV2Api->internal_apps_v2_renew_provisioning_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the ptovisioning profile which has to be renewed.(Required) | 

### Return type

[**ApplicationsProvisionProfileModel**](ApplicationsProvisionProfileModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

