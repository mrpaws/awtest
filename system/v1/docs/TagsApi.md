# systemv1.TagsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_create_tag_for_og**](TagsApi.md#tags_create_tag_for_og) | **POST** /groups/{id}/addTag | Retrieves a particular tag for the specified organization group.
[**tags_delete_tag**](TagsApi.md#tags_delete_tag) | **DELETE** /groups/{ogid}/tags/{tagid} | Deletes a tag for the specified organization group.  &lt;br /&gt;Tag is a custom identifier that can be associated to a device(Example: Refursbished, Repaired).
[**tags_get_tag**](TagsApi.md#tags_get_tag) | **GET** /groups/{ogid}/tags/{tagid} | Retrieves the tag details for a given tag in an organization group.
[**tags_get_tags_by_og**](TagsApi.md#tags_get_tags_by_og) | **GET** /groups/{id}/tags | Retrieves the tags for the specified organization group.
[**tags_update_tag_for_og**](TagsApi.md#tags_update_tag_for_og) | **POST** /groups/{ogid}/tags/{tagid}/update | Updates a tag for the specified organization group.


# **tags_create_tag_for_og**
> tags_create_tag_for_og(id, tag=tag)

Retrieves a particular tag for the specified organization group.

v1.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.TagsApi(systemv1.ApiClient(configuration))
id = 56 # int | The OrganizationGroup Id.
tag = systemv1.Tag() # Tag | The tag Id. (optional)

try:
    # Retrieves a particular tag for the specified organization group.
    api_instance.tags_create_tag_for_og(id, tag=tag)
except ApiException as e:
    print("Exception when calling TagsApi->tags_create_tag_for_og: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The OrganizationGroup Id. | 
 **tag** | [**Tag**](Tag.md)| The tag Id. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_delete_tag**
> tags_delete_tag(ogid, tagid)

Deletes a tag for the specified organization group.  <br />Tag is a custom identifier that can be associated to a device(Example: Refursbished, Repaired).

Delete a tag specified in the input that is present in the given organization group.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.TagsApi(systemv1.ApiClient(configuration))
ogid = 56 # int | The OrganizationGroup Id.
tagid = 56 # int | The tag Id to be deleted.

try:
    # Deletes a tag for the specified organization group.  <br />Tag is a custom identifier that can be associated to a device(Example: Refursbished, Repaired).
    api_instance.tags_delete_tag(ogid, tagid)
except ApiException as e:
    print("Exception when calling TagsApi->tags_delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ogid** | **int**| The OrganizationGroup Id. | 
 **tagid** | **int**| The tag Id to be deleted. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_get_tag**
> TagSearchResult tags_get_tag(ogid, tagid)

Retrieves the tag details for a given tag in an organization group.

Retrieves all the details about a tag in an organization group<br />Tag is a custom identifier that can be associated to a device(Example: Refursbished, Repaired).

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.TagsApi(systemv1.ApiClient(configuration))
ogid = 56 # int | The OrganizationGroup Id.
tagid = 56 # int | The tag Id.

try:
    # Retrieves the tag details for a given tag in an organization group.
    api_response = api_instance.tags_get_tag(ogid, tagid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ogid** | **int**| The OrganizationGroup Id. | 
 **tagid** | **int**| The tag Id. | 

### Return type

[**TagSearchResult**](TagSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_get_tags_by_og**
> TagSearchResult tags_get_tags_by_og(id)

Retrieves the tags for the specified organization group.

Gets the list of tags for the given organization group              <br />Tag is a custom identifier that can be associated to a device(Example: Refursbished, Repaired).

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.TagsApi(systemv1.ApiClient(configuration))
id = 56 # int | The OrganizationGroup Id.

try:
    # Retrieves the tags for the specified organization group.
    api_response = api_instance.tags_get_tags_by_og(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_get_tags_by_og: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The OrganizationGroup Id. | 

### Return type

[**TagSearchResult**](TagSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_update_tag_for_og**
> tags_update_tag_for_og(ogid, tagid, tag=tag)

Updates a tag for the specified organization group.

v1.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.TagsApi(systemv1.ApiClient(configuration))
ogid = 56 # int | The OrganizationGroup Id.
tagid = 56 # int | The tag Id to be updated.
tag = systemv1.Tag() # Tag | The Resource containing tag details. (optional)

try:
    # Updates a tag for the specified organization group.
    api_instance.tags_update_tag_for_og(ogid, tagid, tag=tag)
except ApiException as e:
    print("Exception when calling TagsApi->tags_update_tag_for_og: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ogid** | **int**| The OrganizationGroup Id. | 
 **tagid** | **int**| The tag Id to be updated. | 
 **tag** | [**Tag**](Tag.md)| The Resource containing tag details. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

