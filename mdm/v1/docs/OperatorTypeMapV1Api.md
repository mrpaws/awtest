# mdmv1.OperatorTypeMapV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operator_type_map_v1_get_all_type_maps_async**](OperatorTypeMapV1Api.md#operator_type_map_v1_get_all_type_maps_async) | **GET** /device-expression/operator-type-map/organization-group/{ogUuid} | New - Gets the mapping of all Rules Engine Operator values against types defined in the Schema Registry.
[**operator_type_map_v1_get_type_map_async**](OperatorTypeMapV1Api.md#operator_type_map_v1_get_type_map_async) | **GET** /device-expression/operator-type-map/organization-group/{ogUuid}/type/{type} | New - Gets the supported Operator values in Rules Engine for a particular type defined in the Schema Registry.


# **operator_type_map_v1_get_all_type_maps_async**
> OperatorTypeMapListModel operator_type_map_v1_get_all_type_maps_async(og_uuid)

New - Gets the mapping of all Rules Engine Operator values against types defined in the Schema Registry.



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
api_instance = mdmv1.OperatorTypeMapV1Api(mdmv1.ApiClient(configuration))
og_uuid = 'og_uuid_example' # str | Uuid of the Organization Group.(Required).

try:
    # New - Gets the mapping of all Rules Engine Operator values against types defined in the Schema Registry.
    api_response = api_instance.operator_type_map_v1_get_all_type_maps_async(og_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorTypeMapV1Api->operator_type_map_v1_get_all_type_maps_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **og_uuid** | [**str**](.md)| Uuid of the Organization Group.(Required). | 

### Return type

[**OperatorTypeMapListModel**](OperatorTypeMapListModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_type_map_v1_get_type_map_async**
> OperatorTypeMapModel operator_type_map_v1_get_type_map_async(og_uuid, type)

New - Gets the supported Operator values in Rules Engine for a particular type defined in the Schema Registry.



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
api_instance = mdmv1.OperatorTypeMapV1Api(mdmv1.ApiClient(configuration))
og_uuid = 'og_uuid_example' # str | Uuid of the Organization Group.(Required).
type = 'type_example' # str | Type for which operator map is needed.(Required).

try:
    # New - Gets the supported Operator values in Rules Engine for a particular type defined in the Schema Registry.
    api_response = api_instance.operator_type_map_v1_get_type_map_async(og_uuid, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorTypeMapV1Api->operator_type_map_v1_get_type_map_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **og_uuid** | [**str**](.md)| Uuid of the Organization Group.(Required). | 
 **type** | **str**| Type for which operator map is needed.(Required). | 

### Return type

[**OperatorTypeMapModel**](OperatorTypeMapModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

