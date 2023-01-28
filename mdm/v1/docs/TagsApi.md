# mdmv1.TagsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_add_devices_to_tag_async**](TagsApi.md#tags_add_devices_to_tag_async) | **POST** /tags/{tagid}/adddevices | Add devices to the tag.
[**tags_add_tag**](TagsApi.md#tags_add_tag) | **POST** /tags/addtag | Add a new tag.
[**tags_delete_tag_async**](TagsApi.md#tags_delete_tag_async) | **DELETE** /tags/{tagId} | Delete a tag.
[**tags_devices_for_tag_async**](TagsApi.md#tags_devices_for_tag_async) | **GET** /tags/{tagId}/devices | Retrieves all the devices with the specified tag.
[**tags_remove_devices_from_tag_async**](TagsApi.md#tags_remove_devices_from_tag_async) | **POST** /tags/{tagid}/removedevices | Remove devices from the tag.
[**tags_update_tag**](TagsApi.md#tags_update_tag) | **POST** /tags/{tagId}/update | Updates a tag name, tag type or tag avatar.


# **tags_add_devices_to_tag_async**
> BulkResponse tags_add_devices_to_tag_async(tagid, add_devices=add_devices)

Add devices to the tag.

Associates the given tag to the set of devices.

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
api_instance = mdmv1.TagsApi(mdmv1.ApiClient(configuration))
tagid = 56 # int | Tag id.
add_devices = mdmv1.BulkInput() # BulkInput | Deviceids to be added to the tag. (optional)

try:
    # Add devices to the tag.
    api_response = api_instance.tags_add_devices_to_tag_async(tagid, add_devices=add_devices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_add_devices_to_tag_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagid** | **int**| Tag id. | 
 **add_devices** | [**BulkInput**](BulkInput.md)| Deviceids to be added to the tag. | [optional] 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_add_tag**
> EntityId tags_add_tag(tag=tag)

Add a new tag.

Add a tag based on the details provided.

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
api_instance = mdmv1.TagsApi(mdmv1.ApiClient(configuration))
tag = mdmv1.TagModel() # TagModel | Tag information. (optional)

try:
    # Add a new tag.
    api_response = api_instance.tags_add_tag(tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_add_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**TagModel**](TagModel.md)| Tag information. | [optional] 

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_delete_tag_async**
> tags_delete_tag_async(tag_id)

Delete a tag.

Delete a tag based on tag identifier.

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
api_instance = mdmv1.TagsApi(mdmv1.ApiClient(configuration))
tag_id = 56 # int | The tag ID.

try:
    # Delete a tag.
    api_instance.tags_delete_tag_async(tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->tags_delete_tag_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**| The tag ID. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_devices_for_tag_async**
> tags_devices_for_tag_async(tag_id, last_seen=last_seen)

Retrieves all the devices with the specified tag.

Retrieves the list of devices that have the specified input tag assinged.

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
api_instance = mdmv1.TagsApi(mdmv1.ApiClient(configuration))
tag_id = 56 # int | Tag identifier.
last_seen = '' # datetime | Date Last Seen. (optional) (default to )

try:
    # Retrieves all the devices with the specified tag.
    api_instance.tags_devices_for_tag_async(tag_id, last_seen=last_seen)
except ApiException as e:
    print("Exception when calling TagsApi->tags_devices_for_tag_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**| Tag identifier. | 
 **last_seen** | **datetime**| Date Last Seen. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_remove_devices_from_tag_async**
> BulkResponse tags_remove_devices_from_tag_async(tagid, remove_devices=remove_devices)

Remove devices from the tag.

Remove devices from tag based on the tag identifier and devices to be removed.

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
api_instance = mdmv1.TagsApi(mdmv1.ApiClient(configuration))
tagid = 56 # int | Tag id.
remove_devices = mdmv1.BulkInput() # BulkInput | Deviceids to be removed from tag. (optional)

try:
    # Remove devices from the tag.
    api_response = api_instance.tags_remove_devices_from_tag_async(tagid, remove_devices=remove_devices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_remove_devices_from_tag_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagid** | **int**| Tag id. | 
 **remove_devices** | [**BulkInput**](BulkInput.md)| Deviceids to be removed from tag. | [optional] 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_update_tag**
> tags_update_tag(tag_id, tag=tag)

Updates a tag name, tag type or tag avatar.

Updates a tag based on the tag identifier and tag details. This API can be used to update the tag name, tag type and tag avatar.

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
api_instance = mdmv1.TagsApi(mdmv1.ApiClient(configuration))
tag_id = 56 # int | Unique identifier for the tag.
tag = mdmv1.TagModel() # TagModel | Tag details that needs to be updated. (optional)

try:
    # Updates a tag name, tag type or tag avatar.
    api_instance.tags_update_tag(tag_id, tag=tag)
except ApiException as e:
    print("Exception when calling TagsApi->tags_update_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**| Unique identifier for the tag. | 
 **tag** | [**TagModel**](TagModel.md)| Tag details that needs to be updated. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

