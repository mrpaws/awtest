# mcmv1.RepositoryTemplatesV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mcm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repository_templates_v2_content_repository_template_bulk_delete_async**](RepositoryTemplatesV2Api.md#repository_templates_v2_content_repository_template_bulk_delete_async) | **POST** /V2/contents/repository-templates/delete | New - Bulk delete content repository templates.
[**repository_templates_v2_content_repository_template_delete_async**](RepositoryTemplatesV2Api.md#repository_templates_v2_content_repository_template_delete_async) | **DELETE** /V2/contents/repository-templates/{contentRepositoryTemplateUuid} | New - Deletes a content repository template.
[**repository_templates_v2_create_repository_template_async**](RepositoryTemplatesV2Api.md#repository_templates_v2_create_repository_template_async) | **POST** /V2/contents/repository-templates | New - Creates a Repository template.


# **repository_templates_v2_content_repository_template_bulk_delete_async**
> repository_templates_v2_content_repository_template_bulk_delete_async(content_repository_template_uuids)

New - Bulk delete content repository templates.

Deletes the content repository template for multiple content repository template ids.

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
api_instance = mcmv1.RepositoryTemplatesV2Api(mcmv1.ApiClient(configuration))
content_repository_template_uuids = [mcmv1.list[str]()] # list[str] | Content repository template uuids to be deleted.(Required)

try:
    # New - Bulk delete content repository templates.
    api_instance.repository_templates_v2_content_repository_template_bulk_delete_async(content_repository_template_uuids)
except ApiException as e:
    print("Exception when calling RepositoryTemplatesV2Api->repository_templates_v2_content_repository_template_bulk_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_repository_template_uuids** | **list[str]**| Content repository template uuids to be deleted.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_templates_v2_content_repository_template_delete_async**
> repository_templates_v2_content_repository_template_delete_async(content_repository_template_uuid)

New - Deletes a content repository template.

Deletes the content repository template for a content repository template id.

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
api_instance = mcmv1.RepositoryTemplatesV2Api(mcmv1.ApiClient(configuration))
content_repository_template_uuid = 'content_repository_template_uuid_example' # str | Uuid of the content repository template to be deleted(Required)

try:
    # New - Deletes a content repository template.
    api_instance.repository_templates_v2_content_repository_template_delete_async(content_repository_template_uuid)
except ApiException as e:
    print("Exception when calling RepositoryTemplatesV2Api->repository_templates_v2_content_repository_template_delete_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_repository_template_uuid** | [**str**](.md)| Uuid of the content repository template to be deleted(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_templates_v2_create_repository_template_async**
> repository_templates_v2_create_repository_template_async(repository_template_v2_model)

New - Creates a Repository template.

It creates a repository template and has option for adding assignment, deployment, and security.

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
api_instance = mcmv1.RepositoryTemplatesV2Api(mcmv1.ApiClient(configuration))
repository_template_v2_model = mcmv1.RepositoryTemplateV2Model() # RepositoryTemplateV2Model | Repository template details to be created.(Required)

try:
    # New - Creates a Repository template.
    api_instance.repository_templates_v2_create_repository_template_async(repository_template_v2_model)
except ApiException as e:
    print("Exception when calling RepositoryTemplatesV2Api->repository_templates_v2_create_repository_template_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_template_v2_model** | [**RepositoryTemplateV2Model**](RepositoryTemplateV2Model.md)| Repository template details to be created.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

