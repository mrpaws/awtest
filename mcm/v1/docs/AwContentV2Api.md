# mcmv1.AwContentV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mcm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aw_content_v2_bulk_delete**](AwContentV2Api.md#aw_content_v2_bulk_delete) | **POST** /V2/awcontents/BulkDelete | New - Queues the deletion of multiple files
[**aw_content_v2_get_content_status_counts_async**](AwContentV2Api.md#aw_content_v2_get_content_status_counts_async) | **GET** /V2/awcontents/status/{contentUuid} | New - Get content status counts.


# **aw_content_v2_bulk_delete**
> aw_content_v2_bulk_delete(aw_content_ids)

New - Queues the deletion of multiple files

Queues the Deletion of multiple managed content files selected.

### Example
```python
from __future__ import print_function
import time
import mcmv1
from mcmv1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = mcmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mcmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mcmv1.AwContentV2Api(mcmv1.ApiClient(configuration))
aw_content_ids = [mcmv1.list[str]()] # list[str] | List of GUIDs of the managed content to be dleted(Required)

try:
    # New - Queues the deletion of multiple files
    api_instance.aw_content_v2_bulk_delete(aw_content_ids)
except ApiException as e:
    print("Exception when calling AwContentV2Api->aw_content_v2_bulk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aw_content_ids** | **list[str]**| List of GUIDs of the managed content to be dleted(Required) | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml -application/x-www-form-urlencoded
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aw_content_v2_get_content_status_counts_async**
> ContentStatusModel aw_content_v2_get_content_status_counts_async(content_uuid)

New - Get content status counts.

It returns the count of content status like installed, uninstalled, assigned, viewed, and acknowledged.

### Example
```python
from __future__ import print_function
import time
import mcmv1
from mcmv1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = mcmv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mcmv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mcmv1.AwContentV2Api(mcmv1.ApiClient(configuration))
content_uuid = 'content_uuid_example' # str | Content Uuid.(Required)

try:
    # New - Get content status counts.
    api_response = api_instance.aw_content_v2_get_content_status_counts_async(content_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwContentV2Api->aw_content_v2_get_content_status_counts_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_uuid** | [**str**](.md)| Content Uuid.(Required) | 

### Return type

[**ContentStatusModel**](ContentStatusModel.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

