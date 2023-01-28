# systemv1.LookupFieldsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup_fields_v1_retrieve_lookup_keys_async**](LookupFieldsV1Api.md#lookup_fields_v1_retrieve_lookup_keys_async) | **GET** /lookup-value/keys/{organizationGroupUuid} | New - Retrieves lookup keys for a given organization group
[**lookup_fields_v1_retrieve_lookup_keys_by_type_async**](LookupFieldsV1Api.md#lookup_fields_v1_retrieve_lookup_keys_by_type_async) | **GET** /lookup-value/keys/{organizationGroupUuid}/{lookupValueType} | New - Retrieves lookup keys for a specified lookup field type.


# **lookup_fields_v1_retrieve_lookup_keys_async**
> LookupFieldsV1Entity lookup_fields_v1_retrieve_lookup_keys_async(organization_group_uuid, language=language)

New - Retrieves lookup keys for a given organization group

Retrieve all lookup value keys for the given organization group.

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
api_instance = systemv1.LookupFieldsV1Api(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Represents the organization group to retrieve lookup value keys from(Required)
language = '' # str | The language code (Default en-US). (optional) (default to )

try:
    # New - Retrieves lookup keys for a given organization group
    api_response = api_instance.lookup_fields_v1_retrieve_lookup_keys_async(organization_group_uuid, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookupFieldsV1Api->lookup_fields_v1_retrieve_lookup_keys_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Represents the organization group to retrieve lookup value keys from(Required) | 
 **language** | **str**| The language code (Default en-US). | [optional] [default to ]

### Return type

[**LookupFieldsV1Entity**](LookupFieldsV1Entity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_fields_v1_retrieve_lookup_keys_by_type_async**
> LookupFieldsV1Entity lookup_fields_v1_retrieve_lookup_keys_by_type_async(organization_group_uuid, lookup_value_type)

New - Retrieves lookup keys for a specified lookup field type.

Retrieve all lookup keys for the specified lookup field type.

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
api_instance = systemv1.LookupFieldsV1Api(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Represents the organization group to retrieve lookup value keys from(Required)
lookup_value_type = 'lookup_value_type_example' # str | Represents the category of lookup value keys to retrieve.(Required)

try:
    # New - Retrieves lookup keys for a specified lookup field type.
    api_response = api_instance.lookup_fields_v1_retrieve_lookup_keys_by_type_async(organization_group_uuid, lookup_value_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookupFieldsV1Api->lookup_fields_v1_retrieve_lookup_keys_by_type_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Represents the organization group to retrieve lookup value keys from(Required) | 
 **lookup_value_type** | **str**| Represents the category of lookup value keys to retrieve.(Required) | 

### Return type

[**LookupFieldsV1Entity**](LookupFieldsV1Entity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

