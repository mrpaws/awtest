# mdmv1.AssignmentGroupsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignment_groups_v1_get_assignment_groups_by_search_context**](AssignmentGroupsV1Api.md#assignment_groups_v1_get_assignment_groups_by_search_context) | **GET** /groups/{groupId}/assignmentgroups | New - Returns a list of Assignment Groups matching the search criteria


# **assignment_groups_v1_get_assignment_groups_by_search_context**
> list[AssignmentGroupsV1Model] assignment_groups_v1_get_assignment_groups_by_search_context(group_id, assignment_type, name=name)

New - Returns a list of Assignment Groups matching the search criteria

Get List of Assignment Groups based on the Organization Group, Search Text, AssignmentType.  Search text should not be more than 255 characters.

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
api_instance = mdmv1.AssignmentGroupsV1Api(mdmv1.ApiClient(configuration))
group_id = 56 # int | Unique Identifier for the Organization Group(Required)
assignment_type = 56 # int | Type of Assignment Group to search               0 - All types of Assignment Groups (Smart Group, User Group, Organization Group)                1 - Smart Group                2 - User Group                3 - Organization Group(Required)
name = '' # str | Name of the Assignment Group by which result will be filtered (Optional). When not passed, all Assignment Groups present in that organization will be returned. (optional) (default to )

try:
    # New - Returns a list of Assignment Groups matching the search criteria
    api_response = api_instance.assignment_groups_v1_get_assignment_groups_by_search_context(group_id, assignment_type, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentGroupsV1Api->assignment_groups_v1_get_assignment_groups_by_search_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Unique Identifier for the Organization Group(Required) | 
 **assignment_type** | **int**| Type of Assignment Group to search               0 - All types of Assignment Groups (Smart Group, User Group, Organization Group)                1 - Smart Group                2 - User Group                3 - Organization Group(Required) | 
 **name** | **str**| Name of the Assignment Group by which result will be filtered (Optional). When not passed, all Assignment Groups present in that organization will be returned. | [optional] [default to ]

### Return type

[**list[AssignmentGroupsV1Model]**](AssignmentGroupsV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

