# mamv1.ChunkApi

All URIs are relative to *https://awapi.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chunk_chunk_async**](ChunkApi.md#chunk_chunk_async) | **POST** /blobs/chunk | New - upload the chunks.


# **chunk_chunk_async**
> chunk_chunk_async(chunk_sequence_number, total_application_size, chunk_size, transaction_id=transaction_id)

New - upload the chunks.

- Create a chunk at the specified path  - Supported file types are 'ipa',   'apk', 'xap', 'appx', 'msi', 'app', 'zip', 'xml', 'pem', 'exe', 'pkg',   'dmg', 'plist', 'mpkg', 'js', 'jse', 'ps1', 'ps1xml', 'psc1', 'psd1',   'psm1', 'pssc', 'cdxml', 'vbs', 'vbe', 'wsf', 'wsc', 'msp', 'mst',   'p12', 'pfx', 'p7b', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'p7m', 'ppkg', 'cat', 'apf'

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mamv1.ChunkApi(mamv1.ApiClient(configuration))
chunk_sequence_number = 56 # int | chunk sequence number being uploaded.(Required)
total_application_size =  # object | total application size to be uploaded.(Required) (default to )
chunk_size =  # object | total chunk size to be uploaded.(Required) (default to )
transaction_id = '' # str | UUID of the chunk file being uploaded. (optional) (default to )

try:
    # New - upload the chunks.
    api_instance.chunk_chunk_async(chunk_sequence_number, total_application_size, chunk_size, transaction_id=transaction_id)
except ApiException as e:
    print("Exception when calling ChunkApi->chunk_chunk_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chunk_sequence_number** | **int**| chunk sequence number being uploaded.(Required) | 
 **total_application_size** | [**object**](.md)| total application size to be uploaded.(Required) | [default to ]
 **chunk_size** | [**object**](.md)| total chunk size to be uploaded.(Required) | [default to ]
 **transaction_id** | **str**| UUID of the chunk file being uploaded. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

