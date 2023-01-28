# mamv2.BlobsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blobs_v2_delete**](BlobsV2Api.md#blobs_v2_delete) | **DELETE** /blobs/{blobId} | New - Deletes a blob by Guid
[**blobs_v2_head**](BlobsV2Api.md#blobs_v2_head) | **HEAD** /blobs/{blobId} | New - Gets a blob contents information by the Guid


# **blobs_v2_delete**
> blobs_v2_delete(blob_id)

New - Deletes a blob by Guid

Deletes a blob by Guid.

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
api_instance = mamv2.BlobsV2Api(mamv2.ApiClient(configuration))
blob_id = 'blob_id_example' # str | Identifier of the blob to be deleted(Required)

try:
    # New - Deletes a blob by Guid
    api_instance.blobs_v2_delete(blob_id)
except ApiException as e:
    print("Exception when calling BlobsV2Api->blobs_v2_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blob_id** | [**str**](.md)| Identifier of the blob to be deleted(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobs_v2_head**
> blobs_v2_head(blob_id)

New - Gets a blob contents information by the Guid

Returns the information for blob contents

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
api_instance = mamv2.BlobsV2Api(mamv2.ApiClient(configuration))
blob_id = 'blob_id_example' # str | Identifier of the blob to be retrieved(Required)

try:
    # New - Gets a blob contents information by the Guid
    api_instance.blobs_v2_head(blob_id)
except ApiException as e:
    print("Exception when calling BlobsV2Api->blobs_v2_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blob_id** | [**str**](.md)| Identifier of the blob to be retrieved(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/octet-stream;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

