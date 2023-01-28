# systemv2.GroupSyncActionsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_sync_actions_v2_group_acknowledgement**](GroupSyncActionsV2Api.md#group_sync_actions_v2_group_acknowledgement) | **GET** /GroupSyncActions/{uuid} | New - Get Group Acknowledgement
[**group_sync_actions_v2_merge_pending_groups**](GroupSyncActionsV2Api.md#group_sync_actions_v2_merge_pending_groups) | **POST** /GroupSyncActions | New - Merges the group changes


# **group_sync_actions_v2_group_acknowledgement**
> GroupAcknowledgementV2Model group_sync_actions_v2_group_acknowledgement(uuid, membership_status=membership_status, page=page)

New - Get Group Acknowledgement

Gets the approval status for a group along with the access token and link to merge that group. This will also include the details of members added and removed from the group.

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
api_instance = systemv2.GroupSyncActionsV2Api(systemv2.ApiClient(configuration))
uuid = 'uuid_example' # str | UserGroup Uuid.(Required)
membership_status =  # object | Filter for Added and Removed Users - ('Add'/'Remove') (optional) (default to )
page = '' # str | Page number to be displayed (optional) (default to )

try:
    # New - Get Group Acknowledgement
    api_response = api_instance.group_sync_actions_v2_group_acknowledgement(uuid, membership_status=membership_status, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupSyncActionsV2Api->group_sync_actions_v2_group_acknowledgement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| UserGroup Uuid.(Required) | 
 **membership_status** | [**object**](.md)| Filter for Added and Removed Users - (&#39;Add&#39;/&#39;Remove&#39;) | [optional] [default to ]
 **page** | **str**| Page number to be displayed | [optional] [default to ]

### Return type

[**GroupAcknowledgementV2Model**](GroupAcknowledgementV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_sync_actions_v2_merge_pending_groups**
> group_sync_actions_v2_merge_pending_groups(merge_pending_groups_v2_model)

New - Merges the group changes

Merges the user or admin group which are in 'MergePendingApproval' or 'MergeFailed' state.

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
api_instance = systemv2.GroupSyncActionsV2Api(systemv2.ApiClient(configuration))
merge_pending_groups_v2_model = systemv2.MergePendingGroupsV2Model() # MergePendingGroupsV2Model | (Required)

try:
    # New - Merges the group changes
    api_instance.group_sync_actions_v2_merge_pending_groups(merge_pending_groups_v2_model)
except ApiException as e:
    print("Exception when calling GroupSyncActionsV2Api->group_sync_actions_v2_merge_pending_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_pending_groups_v2_model** | [**MergePendingGroupsV2Model**](MergePendingGroupsV2Model.md)| (Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

