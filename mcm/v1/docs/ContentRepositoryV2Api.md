# mcmv1.ContentRepositoryV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mcm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_repository_v2_content_repository_bulk_delete_async**](ContentRepositoryV2Api.md#content_repository_v2_content_repository_bulk_delete_async) | **POST** /V2/contents/repositories/delete | New - Bulk delete content repositories.
[**content_repository_v2_content_repository_delete_async**](ContentRepositoryV2Api.md#content_repository_v2_content_repository_delete_async) | **DELETE** /V2/contents/repositories/{contentRepositoryUuid} | New - Deletes a content repository.
[**content_repository_v2_create_content_repository_async**](ContentRepositoryV2Api.md#content_repository_v2_create_content_repository_async) | **POST** /V2/contents/repositories | New - Creates an Admin Content Repository.
[**content_repository_v2_personal_content_repository_bulk_delete_async**](ContentRepositoryV2Api.md#content_repository_v2_personal_content_repository_bulk_delete_async) | **DELETE** /V2/contents/groups/{organizationGroupUuid}/personal-content | New - Deletes personal content related metadata.


# **content_repository_v2_content_repository_bulk_delete_async**
> content_repository_v2_content_repository_bulk_delete_async(content_repository_uuids)

New - Bulk delete content repositories.

Deletes the content repository for multiple content repository uuids.

### Example
```python
from __future__ import print_function
import time
import mcmv1
from mcmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mcmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
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
api_instance = mcmv1.ContentRepositoryV2Api(mcmv1.ApiClient(configuration))
content_repository_uuids = [mcmv1.list[str]()] # list[str] | Content repository uuids to be deleted.(Required)

try:
    # New - Bulk delete content repositories.
    api_instance.content_repository_v2_content_repository_bulk_delete_async(content_repository_uuids)
except ApiException as e:
    print("Exception when calling ContentRepositoryV2Api->content_repository_v2_content_repository_bulk_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_repository_uuids** | **list[str]**| Content repository uuids to be deleted.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_repository_v2_content_repository_delete_async**
> content_repository_v2_content_repository_delete_async(content_repository_uuid)

New - Deletes a content repository.

Deletes the content repository for a content repository uuid.

### Example
```python
from __future__ import print_function
import time
import mcmv1
from mcmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mcmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
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
api_instance = mcmv1.ContentRepositoryV2Api(mcmv1.ApiClient(configuration))
content_repository_uuid = 'content_repository_uuid_example' # str | Uuid of the content repository to be deleted(Required)

try:
    # New - Deletes a content repository.
    api_instance.content_repository_v2_content_repository_delete_async(content_repository_uuid)
except ApiException as e:
    print("Exception when calling ContentRepositoryV2Api->content_repository_v2_content_repository_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_repository_uuid** | [**str**](.md)| Uuid of the content repository to be deleted(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_repository_v2_create_content_repository_async**
> content_repository_v2_create_content_repository_async(content_repository_v2_model)

New - Creates an Admin Content Repository.

It creates an admin content repository and has options for adding assignment, deployment, and security.

### Example
```python
from __future__ import print_function
import time
import mcmv1
from mcmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mcmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
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
api_instance = mcmv1.ContentRepositoryV2Api(mcmv1.ApiClient(configuration))
content_repository_v2_model = mcmv1.ContentRepositoryV2Model() # ContentRepositoryV2Model | Content gateway configuration details to be created.(Required)

try:
    # New - Creates an Admin Content Repository.
    api_instance.content_repository_v2_create_content_repository_async(content_repository_v2_model)
except ApiException as e:
    print("Exception when calling ContentRepositoryV2Api->content_repository_v2_create_content_repository_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_repository_v2_model** | [**ContentRepositoryV2Model**](ContentRepositoryV2Model.md)| Content gateway configuration details to be created.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_repository_v2_personal_content_repository_bulk_delete_async**
> content_repository_v2_personal_content_repository_bulk_delete_async(organization_group_uuid)

New - Deletes personal content related metadata.

Deletes all personal content repository for the provided Organization Group and its children Organization Group.

### Example
```python
from __future__ import print_function
import time
import mcmv1
from mcmv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mcmv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
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
api_instance = mcmv1.ContentRepositoryV2Api(mcmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group Uuid.(Required)

try:
    # New - Deletes personal content related metadata.
    api_instance.content_repository_v2_personal_content_repository_bulk_delete_async(organization_group_uuid)
except ApiException as e:
    print("Exception when calling ContentRepositoryV2Api->content_repository_v2_personal_content_repository_bulk_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Organization Group Uuid.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

