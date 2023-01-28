# mcmv1.AwContentsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mcm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aw_contents_delete_file**](AwContentsApi.md#aw_contents_delete_file) | **DELETE** /awcontents/{id} | New - Delete a Managed content.
[**aw_contents_download_file**](AwContentsApi.md#aw_contents_download_file) | **GET** /awcontents/{id} | New - Download a Managed content.
[**aw_contents_get_file_metadata_async**](AwContentsApi.md#aw_contents_get_file_metadata_async) | **GET** /awcontents/{id}/info | New - Get metadata for a Managed content.
[**aw_contents_search_async**](AwContentsApi.md#aw_contents_search_async) | **GET** /awcontents | New - Search managed content.
[**aw_contents_update_file_metadata_async**](AwContentsApi.md#aw_contents_update_file_metadata_async) | **PUT** /awcontents/{id}/info | New - Update metadata for a Managed content.
[**aw_contents_upload_file_async**](AwContentsApi.md#aw_contents_upload_file_async) | **POST** /awcontents | New - Upload a Managed content.


# **aw_contents_delete_file**
> aw_contents_delete_file(id)

New - Delete a Managed content.

Delete a file.

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
api_instance = mcmv1.AwContentsApi(mcmv1.ApiClient(configuration))
id = 'id_example' # str | Unique identifier of the file.(Required).

try:
    # New - Delete a Managed content.
    api_instance.aw_contents_delete_file(id)
except ApiException as e:
    print("Exception when calling AwContentsApi->aw_contents_delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file.(Required). | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aw_contents_download_file**
> str aw_contents_download_file(id)

New - Download a Managed content.

Download a file.

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
api_instance = mcmv1.AwContentsApi(mcmv1.ApiClient(configuration))
id = 'id_example' # str | Unique identifier of the file.(Required).

try:
    # New - Download a Managed content.
    api_response = api_instance.aw_contents_download_file(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwContentsApi->aw_contents_download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file.(Required). | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/octet-stream;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aw_contents_get_file_metadata_async**
> AwContentModel aw_contents_get_file_metadata_async(id)

New - Get metadata for a Managed content.

Get metadata for the specified managed content.

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
api_instance = mcmv1.AwContentsApi(mcmv1.ApiClient(configuration))
id = 'id_example' # str | Unique identifier of the file.(Required).

try:
    # New - Get metadata for a Managed content.
    api_response = api_instance.aw_contents_get_file_metadata_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwContentsApi->aw_contents_get_file_metadata_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file.(Required). | 

### Return type

[**AwContentModel**](AwContentModel.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aw_contents_search_async**
> AwContentPagedResultModel aw_contents_search_async(locationgroupcode=locationgroupcode, locationgroupid=locationgroupid, query_string=query_string, category_id=category_id, mime_type=mime_type, expires_in=expires_in, sort_by=sort_by, sort_ascending=sort_ascending, sort_index=sort_index, page_size=page_size)

New - Search managed content.

Search managed content.

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
api_instance = mcmv1.AwContentsApi(mcmv1.ApiClient(configuration))
locationgroupcode = '' # str | Organization group code. (optional) (default to )
locationgroupid = 56 # int | Organization group id. (optional)
query_string = '' # str | Searches for the string value in the File Name. (optional) (default to )
category_id =  # object | The unique identifier for the Category. (optional) (default to )
mime_type = '' # str | Filter contents by Mime Type. (optional) (default to )
expires_in = 56 # int | Filter by Contents that are going to expire within days specified. (optional)
sort_by = '' # str | Sort the result based on a property. Accepts \"Name\", \"Size\", \"Author\", \"DownloadPriority\", \"IsRequired\", \"IsActive\", \"EffectiveDate\", \"ExpirationDate\", \"ModifiedOn\", or \"ModifiedBy\". By default it sorts by \"Name\".. (optional) (default to )
sort_ascending =  # bool | Sort direction. By default it sorts Ascending. (optional) (default to )
sort_index = 56 # int | Start index of page. (optional)
page_size = 56 # int | Specifies the number of results returned per Page. (optional)

try:
    # New - Search managed content.
    api_response = api_instance.aw_contents_search_async(locationgroupcode=locationgroupcode, locationgroupid=locationgroupid, query_string=query_string, category_id=category_id, mime_type=mime_type, expires_in=expires_in, sort_by=sort_by, sort_ascending=sort_ascending, sort_index=sort_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwContentsApi->aw_contents_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locationgroupcode** | **str**| Organization group code. | [optional] [default to ]
 **locationgroupid** | **int**| Organization group id. | [optional] 
 **query_string** | **str**| Searches for the string value in the File Name. | [optional] [default to ]
 **category_id** | [**object**](.md)| The unique identifier for the Category. | [optional] [default to ]
 **mime_type** | **str**| Filter contents by Mime Type. | [optional] [default to ]
 **expires_in** | **int**| Filter by Contents that are going to expire within days specified. | [optional] 
 **sort_by** | **str**| Sort the result based on a property. Accepts \&quot;Name\&quot;, \&quot;Size\&quot;, \&quot;Author\&quot;, \&quot;DownloadPriority\&quot;, \&quot;IsRequired\&quot;, \&quot;IsActive\&quot;, \&quot;EffectiveDate\&quot;, \&quot;ExpirationDate\&quot;, \&quot;ModifiedOn\&quot;, or \&quot;ModifiedBy\&quot;. By default it sorts by \&quot;Name\&quot;.. | [optional] [default to ]
 **sort_ascending** | **bool**| Sort direction. By default it sorts Ascending. | [optional] [default to ]
 **sort_index** | **int**| Start index of page. | [optional] 
 **page_size** | **int**| Specifies the number of results returned per Page. | [optional] 

### Return type

[**AwContentPagedResultModel**](AwContentPagedResultModel.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aw_contents_update_file_metadata_async**
> AwContentModel aw_contents_update_file_metadata_async(id, model)

New - Update metadata for a Managed content.

Update metadata for the specified managed content.

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
api_instance = mcmv1.AwContentsApi(mcmv1.ApiClient(configuration))
id = 'id_example' # str | Unique identifier of the file.(Required).
model = mcmv1.AwContentModel() # AwContentModel | The json for updating the content metadata.(Required).

try:
    # New - Update metadata for a Managed content.
    api_response = api_instance.aw_contents_update_file_metadata_async(id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwContentsApi->aw_contents_update_file_metadata_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file.(Required). | 
 **model** | [**AwContentModel**](AwContentModel.md)| The json for updating the content metadata.(Required). | 

### Return type

[**AwContentModel**](AwContentModel.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aw_contents_upload_file_async**
> AwContentModel aw_contents_upload_file_async(file_name, category_id, effective_date, location_group_id, location_group_code)

New - Upload a Managed content.

Uploads a file to specified OG.

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
api_instance = mcmv1.AwContentsApi(mcmv1.ApiClient(configuration))
file_name = '' # str | File name for the uploaded file.(Required) (default to )
category_id =  # object | The category for the file.(Required) (default to )
effective_date = '' # datetime | The effective date for the file.(Required) (default to )
location_group_id = 56 # int | The ID of the organization group.(Required)
location_group_code = '' # str | The group code of the organization group.(Required) (default to )

try:
    # New - Upload a Managed content.
    api_response = api_instance.aw_contents_upload_file_async(file_name, category_id, effective_date, location_group_id, location_group_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwContentsApi->aw_contents_upload_file_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name for the uploaded file.(Required) | [default to ]
 **category_id** | [**object**](.md)| The category for the file.(Required) | [default to ]
 **effective_date** | **datetime**| The effective date for the file.(Required) | [default to ]
 **location_group_id** | **int**| The ID of the organization group.(Required) | 
 **location_group_code** | **str**| The group code of the organization group.(Required) | [default to ]

### Return type

[**AwContentModel**](AwContentModel.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

