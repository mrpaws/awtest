# mdmv1.WorkflowEntityV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_entity_v1_get_workflows_for_entity_async**](WorkflowEntityV1Api.md#workflow_entity_v1_get_workflows_for_entity_async) | **GET** /workflows/{entitytype}/search/{entityUuid} | New - Retrieves a paginated result of the workflows assigned to this entity.


# **workflow_entity_v1_get_workflows_for_entity_async**
> list[WorkflowEntitySearchListResponseV1Model] workflow_entity_v1_get_workflows_for_entity_async(entitytype, entity_uuid, orderby=orderby, page=page, page_size=page_size, sortorder=sortorder, via_freestyle=via_freestyle)

New - Retrieves a paginated result of the workflows assigned to this entity.



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
api_instance = mdmv1.WorkflowEntityV1Api(mdmv1.ApiClient(configuration))
entitytype = 56 # int | The type of the entity.(Required)
entity_uuid = 'entity_uuid_example' # str | The identifier of the entity for which we are searching for the workflows assigned.(Required)
orderby = '' # str | Order the results by this attribute (optional) (default to )
page = 56 # int | The specific page number to get (optional)
page_size = 56 # int | Maximum records per page (optional)
sortorder = '' # str | Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified (optional) (default to )
via_freestyle =  # bool | The optional query parameter via_freestyle will fetch the workflows created via Freestyle. Setting this optional parameter to true, will fetch only the workflows created via Freestyle only. Setting the optional parameter to false, will fetch implicitly created workflows from other sources such as Scripts. Not passing this optional parameter will fetch all available workflows. (optional) (default to )

try:
    # New - Retrieves a paginated result of the workflows assigned to this entity.
    api_response = api_instance.workflow_entity_v1_get_workflows_for_entity_async(entitytype, entity_uuid, orderby=orderby, page=page, page_size=page_size, sortorder=sortorder, via_freestyle=via_freestyle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowEntityV1Api->workflow_entity_v1_get_workflows_for_entity_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitytype** | **int**| The type of the entity.(Required) | 
 **entity_uuid** | [**str**](.md)| The identifier of the entity for which we are searching for the workflows assigned.(Required) | 
 **orderby** | **str**| Order the results by this attribute | [optional] [default to ]
 **page** | **int**| The specific page number to get | [optional] 
 **page_size** | **int**| Maximum records per page | [optional] 
 **sortorder** | **str**| Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified | [optional] [default to ]
 **via_freestyle** | **bool**| The optional query parameter via_freestyle will fetch the workflows created via Freestyle. Setting this optional parameter to true, will fetch only the workflows created via Freestyle only. Setting the optional parameter to false, will fetch implicitly created workflows from other sources such as Scripts. Not passing this optional parameter will fetch all available workflows. | [optional] [default to ]

### Return type

[**list[WorkflowEntitySearchListResponseV1Model]**](WorkflowEntitySearchListResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

