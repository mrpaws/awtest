# mdmv2.AssignmentGroupsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignment_groups_v2_get_assignment_groups_by_search_context_async**](AssignmentGroupsV2Api.md#assignment_groups_v2_get_assignment_groups_by_search_context_async) | **GET** /groups/{organizationGroupUuid}/assignmentgroups | New - Returns a list of Assignment Groups matching the search criteria


# **assignment_groups_v2_get_assignment_groups_by_search_context_async**
> list[AssignmentGroupsPagedResultsModelV1] assignment_groups_v2_get_assignment_groups_by_search_context_async(organization_group_uuid, assignment_type, name=name, order_by=order_by, sort_order=sort_order, page=page, page_size=page_size)

New - Returns a list of Assignment Groups matching the search criteria

Get List of Assignment Groups based on the Organization Group, Search Text, AssignmentType. Search text should not be more than 255 characters.

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
api_instance = mdmv2.AssignmentGroupsV2Api(mdmv2.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Unique Identifier for the Organization Group(Required).
assignment_type = 56 # int | Type of Assignment Group to search               All types of Assignment Groups (Smart Group, User Group, Organization Group)                SmartGroups                UserGroups                OrganizationGroups (Required)
name = '' # str | Name of the Assignment Group by which result will be filtered (Optional). When not passed, all Assignment Groups present in that organization will be returned. (optional) (default to )
order_by = '' # str | The column used for sorting. (optional) (default to )
sort_order =  # object | The sort order ascending/decending. Default value is ASC. (optional) (default to )
page = 56 # int | The page number for the paged result. (optional)
page_size = 56 # int | The number of records per page. (optional)

try:
    # New - Returns a list of Assignment Groups matching the search criteria
    api_response = api_instance.assignment_groups_v2_get_assignment_groups_by_search_context_async(organization_group_uuid, assignment_type, name=name, order_by=order_by, sort_order=sort_order, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentGroupsV2Api->assignment_groups_v2_get_assignment_groups_by_search_context_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Unique Identifier for the Organization Group(Required). | 
 **assignment_type** | **int**| Type of Assignment Group to search               All types of Assignment Groups (Smart Group, User Group, Organization Group)                SmartGroups                UserGroups                OrganizationGroups (Required) | 
 **name** | **str**| Name of the Assignment Group by which result will be filtered (Optional). When not passed, all Assignment Groups present in that organization will be returned. | [optional] [default to ]
 **order_by** | **str**| The column used for sorting. | [optional] [default to ]
 **sort_order** | [**object**](.md)| The sort order ascending/decending. Default value is ASC. | [optional] [default to ]
 **page** | **int**| The page number for the paged result. | [optional] 
 **page_size** | **int**| The number of records per page. | [optional] 

### Return type

[**list[AssignmentGroupsPagedResultsModelV1]**](AssignmentGroupsPagedResultsModelV1.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

