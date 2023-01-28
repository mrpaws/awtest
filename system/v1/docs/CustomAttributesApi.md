# systemv1.CustomAttributesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_attributes_save_custom_attribute**](CustomAttributesApi.md#custom_attributes_save_custom_attribute) | **POST** /customattributes/create | Creates a custom attribute definition in AirWatch.
[**custom_attributes_search**](CustomAttributesApi.md#custom_attributes_search) | **GET** /customattributes/search | Search custom attributes.


# **custom_attributes_save_custom_attribute**
> EntityId custom_attributes_save_custom_attribute(custom_attribute)

Creates a custom attribute definition in AirWatch.

Creates a custom attibute for the organization group. Multiple values can be added to a custom attribute with this API.

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
api_instance = systemv1.CustomAttributesApi(systemv1.ApiClient(configuration))
custom_attribute = systemv1.CustomAttributeModel_() # CustomAttributeModel_ | Entity defining a custom attribute to be added (Required).

try:
    # Creates a custom attribute definition in AirWatch.
    api_response = api_instance.custom_attributes_save_custom_attribute(custom_attribute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomAttributesApi->custom_attributes_save_custom_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_attribute** | [**CustomAttributeModel_**](CustomAttributeModel_.md)| Entity defining a custom attribute to be added (Required). | 

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_attributes_search**
> CustomAttributeSearchResult custom_attributes_search(organizationgroupid=organizationgroupid, name=name, page=page, pagesize=pagesize)

Search custom attributes.

Searches Custom Attributes based on name, page and pagesize.

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
api_instance = systemv1.CustomAttributesApi(systemv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization Group Identifer. (optional)
name = '' # str | Custom Attribute Name. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximumm records per page. Default 500. (optional)

try:
    # Search custom attributes.
    api_response = api_instance.custom_attributes_search(organizationgroupid=organizationgroupid, name=name, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomAttributesApi->custom_attributes_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization Group Identifer. | [optional] 
 **name** | **str**| Custom Attribute Name. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximumm records per page. Default 500. | [optional] 

### Return type

[**CustomAttributeSearchResult**](CustomAttributeSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

