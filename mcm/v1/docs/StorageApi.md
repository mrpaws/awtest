# mcmv1.StorageApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mcm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_get_admin_storage**](StorageApi.md#storage_get_admin_storage) | **GET** /storage | Returns Admin storage information of that OG.


# **storage_get_admin_storage**
> AdminStorageModel storage_get_admin_storage()

Returns Admin storage information of that OG.

Returns the admin storage information like content capacity.

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
api_instance = mcmv1.StorageApi(mcmv1.ApiClient(configuration))

try:
    # Returns Admin storage information of that OG.
    api_response = api_instance.storage_get_admin_storage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->storage_get_admin_storage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminStorageModel**](AdminStorageModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

