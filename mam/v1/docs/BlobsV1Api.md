# mamv1.BlobsV1Api

All URIs are relative to *https://awapi.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blobs_v1_delete_blob_async**](BlobsV1Api.md#blobs_v1_delete_blob_async) | **DELETE** /blobs/blob/{blobId} | New - Deletes a blob by ID
[**blobs_v1_download_blob**](BlobsV1Api.md#blobs_v1_download_blob) | **GET** /blobs/downloadblob/{blobId} | New - Gets a blob by the ID
[**blobs_v1_upload_blob_async**](BlobsV1Api.md#blobs_v1_upload_blob_async) | **POST** /blobs/uploadblob | New - Create a new blob with attached file


# **blobs_v1_delete_blob_async**
> blobs_v1_delete_blob_async(blob_id)

New - Deletes a blob by ID

Deletes a blob by ID.

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
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.BlobsV1Api(mamv1.ApiClient(configuration))
blob_id = 56 # int | Blob ID to be deleted(Required)

try:
    # New - Deletes a blob by ID
    api_instance.blobs_v1_delete_blob_async(blob_id)
except ApiException as e:
    print("Exception when calling BlobsV1Api->blobs_v1_delete_blob_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blob_id** | **int**| Blob ID to be deleted(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobs_v1_download_blob**
> blobs_v1_download_blob(blob_id)

New - Gets a blob by the ID

Returns the contents of a blob as a byte array

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
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.BlobsV1Api(mamv1.ApiClient(configuration))
blob_id = 56 # int | Identifier of the blob to be retrieved(Required)

try:
    # New - Gets a blob by the ID
    api_instance.blobs_v1_download_blob(blob_id)
except ApiException as e:
    print("Exception when calling BlobsV1Api->blobs_v1_download_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blob_id** | **int**| Identifier of the blob to be retrieved(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/octet-stream;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobs_v1_upload_blob_async**
> EntityV1Model blobs_v1_upload_blob_async(file_name, organization_group_id, module_type=module_type, file_link=file_link, access_via=access_via, content_gateway_id=content_gateway_id, downloadfilefromlink=downloadfilefromlink, username=username, password=password)

New - Create a new blob with attached file

 - Create a new blob with attached file  - Supported file types are 'ipa',    'apk', 'xap', 'appx', 'msi', 'app', 'zip', 'xml', 'pem', 'exe', 'pkg',    'dmg', 'plist', 'mpkg', 'js', 'jse', 'ps1', 'ps1xml', 'psc1', 'psd1',    'psm1', 'pssc', 'cdxml', 'vbs', 'vbe', 'wsf', 'wsc', 'msp', 'mst',    'p12', 'pfx', 'p7b', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'p7m', 'ppkg', 'cat', 'apf'  - No size restrictions  - Organization Group will be set to Global irrespective of value passed if the file type is of 'apf'

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
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.BlobsV1Api(mamv1.ApiClient(configuration))
file_name = '' # str | Name of the file being uploaded(Required) (default to )
organization_group_id = 56 # int | Organization Group ID integer identifying the customer or container(Required)
module_type =  # object | Module type of the blob. For application blobs, module type is required and should be set as Application. (optional) (default to )
file_link = '' # str | Path of the file to upload. Required if blob file is not submitted (optional) (default to )
access_via =  # object | Access type. If EIS, content gateway ID is required and validated for the Organization Group Id (optional) (default to )
content_gateway_id = 56 # int | Content gateway ID of the repository to save to. Required if accessVia is EIS. (optional)
downloadfilefromlink =  # bool | Set to true if application needs to be downloaded from the link. (optional) (default to )
username = '' # str | required when accessVia is EIS and downloadfilefromlink is true (optional) (default to )
password = '' # str | required when accessVia is EIS and downloadfilefromlink is true (optional) (default to )

try:
    # New - Create a new blob with attached file
    api_response = api_instance.blobs_v1_upload_blob_async(file_name, organization_group_id, module_type=module_type, file_link=file_link, access_via=access_via, content_gateway_id=content_gateway_id, downloadfilefromlink=downloadfilefromlink, username=username, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobsV1Api->blobs_v1_upload_blob_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the file being uploaded(Required) | [default to ]
 **organization_group_id** | **int**| Organization Group ID integer identifying the customer or container(Required) | 
 **module_type** | [**object**](.md)| Module type of the blob. For application blobs, module type is required and should be set as Application. | [optional] [default to ]
 **file_link** | **str**| Path of the file to upload. Required if blob file is not submitted | [optional] [default to ]
 **access_via** | [**object**](.md)| Access type. If EIS, content gateway ID is required and validated for the Organization Group Id | [optional] [default to ]
 **content_gateway_id** | **int**| Content gateway ID of the repository to save to. Required if accessVia is EIS. | [optional] 
 **downloadfilefromlink** | **bool**| Set to true if application needs to be downloaded from the link. | [optional] [default to ]
 **username** | **str**| required when accessVia is EIS and downloadfilefromlink is true | [optional] [default to ]
 **password** | **str**| required when accessVia is EIS and downloadfilefromlink is true | [optional] [default to ]

### Return type

[**EntityV1Model**](EntityV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

