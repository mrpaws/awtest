# mcmv1.CategoryApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mcm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**category_add_category**](CategoryApi.md#category_add_category) | **POST** /categories | Create new category under OG specified.
[**category_delete_category**](CategoryApi.md#category_delete_category) | **DELETE** /categories/{id} | Endpoint to delete a category specified by the Id.
[**category_get_categories**](CategoryApi.md#category_get_categories) | **GET** /categories | Get all cateogries available for this OG.
[**category_update_category**](CategoryApi.md#category_update_category) | **PUT** /categories/{id} | Update the category metadata.


# **category_add_category**
> category_add_category(model=model)

Create new category under OG specified.

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
api_instance = mcmv1.CategoryApi(mcmv1.ApiClient(configuration))
model = mcmv1.CategoryModel() # CategoryModel | Category model. (optional)

try:
    # Create new category under OG specified.
    api_instance.category_add_category(model=model)
except ApiException as e:
    print("Exception when calling CategoryApi->category_add_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**CategoryModel**](CategoryModel.md)| Category model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_delete_category**
> category_delete_category(id)

Endpoint to delete a category specified by the Id.

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
api_instance = mcmv1.CategoryApi(mcmv1.ApiClient(configuration))
id = 'id_example' # str | CategoryId.

try:
    # Endpoint to delete a category specified by the Id.
    api_instance.category_delete_category(id)
except ApiException as e:
    print("Exception when calling CategoryApi->category_delete_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CategoryId. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_get_categories**
> category_get_categories(locationgroupcode=locationgroupcode, locationgroupid=locationgroupid)

Get all cateogries available for this OG.

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
api_instance = mcmv1.CategoryApi(mcmv1.ApiClient(configuration))
locationgroupcode = '' # str | Location group code. (optional) (default to )
locationgroupid = 56 # int | Location group id. (optional)

try:
    # Get all cateogries available for this OG.
    api_instance.category_get_categories(locationgroupcode=locationgroupcode, locationgroupid=locationgroupid)
except ApiException as e:
    print("Exception when calling CategoryApi->category_get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locationgroupcode** | **str**| Location group code. | [optional] [default to ]
 **locationgroupid** | **int**| Location group id. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_update_category**
> category_update_category(id, model=model)

Update the category metadata.

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
api_instance = mcmv1.CategoryApi(mcmv1.ApiClient(configuration))
id = 'id_example' # str | Category Id.
model = mcmv1.CategoryModel() # CategoryModel | Category model. (optional)

try:
    # Update the category metadata.
    api_instance.category_update_category(id, model=model)
except ApiException as e:
    print("Exception when calling CategoryApi->category_update_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Category Id. | 
 **model** | [**CategoryModel**](CategoryModel.md)| Category model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

