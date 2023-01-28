# mdmv1.CatalogsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogs_v1_get_all_policies_async**](CatalogsV1Api.md#catalogs_v1_get_all_policies_async) | **GET** /baselines/catalogs/{osVersionUUID}/policies | New - Search policies in the Policy catalog of a specific version
[**catalogs_v1_get_policy_async**](CatalogsV1Api.md#catalogs_v1_get_policy_async) | **GET** /baselines/catalogs/policies/{policyUUID} | New - Fetch a policy with it&#39;s options
[**catalogs_v1_get_policy_catalog_async**](CatalogsV1Api.md#catalogs_v1_get_policy_catalog_async) | **GET** /baselines/catalogs/{osVersionUUID} | New - Fetch policy catalog for the given operating system version.


# **catalogs_v1_get_all_policies_async**
> GetAllPoliciesResponseV1Model catalogs_v1_get_all_policies_async(os_version_uuid, q=q, language=language, offset=offset, limit=limit)

New - Search policies in the Policy catalog of a specific version

Returns all or matching policies from the requested catalog version

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

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
api_instance = mdmv1.CatalogsV1Api(mdmv1.ApiClient(configuration))
os_version_uuid = 'os_version_uuid_example' # str | The operating system version identifier(Required)
q = '' # str | The search text (optional) (default to )
language = '' # str | The language code (Default en-US) (optional) (default to )
offset =  # object | The number of records to skip (Default 0). (optional) (default to )
limit =  # object | The maximum number of rows to return (Default 10) (optional) (default to )

try:
    # New - Search policies in the Policy catalog of a specific version
    api_response = api_instance.catalogs_v1_get_all_policies_async(os_version_uuid, q=q, language=language, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsV1Api->catalogs_v1_get_all_policies_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_version_uuid** | [**str**](.md)| The operating system version identifier(Required) | 
 **q** | **str**| The search text | [optional] [default to ]
 **language** | **str**| The language code (Default en-US) | [optional] [default to ]
 **offset** | [**object**](.md)| The number of records to skip (Default 0). | [optional] [default to ]
 **limit** | [**object**](.md)| The maximum number of rows to return (Default 10) | [optional] [default to ]

### Return type

[**GetAllPoliciesResponseV1Model**](GetAllPoliciesResponseV1Model.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_v1_get_policy_async**
> PolicyModel catalogs_v1_get_policy_async(policy_uuid, language=language)

New - Fetch a policy with it's options

Returns a policy with it's options localized for a selected language

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

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
api_instance = mdmv1.CatalogsV1Api(mdmv1.ApiClient(configuration))
policy_uuid = 'policy_uuid_example' # str | The policy identifier(Required)
language = '' # str | The language code (Default en-US) (optional) (default to )

try:
    # New - Fetch a policy with it's options
    api_response = api_instance.catalogs_v1_get_policy_async(policy_uuid, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsV1Api->catalogs_v1_get_policy_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | [**str**](.md)| The policy identifier(Required) | 
 **language** | **str**| The language code (Default en-US) | [optional] [default to ]

### Return type

[**PolicyModel**](PolicyModel.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_v1_get_policy_catalog_async**
> PolicyCatalogModel catalogs_v1_get_policy_catalog_async(os_version_uuid, language=language)

New - Fetch policy catalog for the given operating system version.

Returns the policy catalog for the given operating system version.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

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
api_instance = mdmv1.CatalogsV1Api(mdmv1.ApiClient(configuration))
os_version_uuid = 'os_version_uuid_example' # str | The operating system version identifier(Required)
language = '' # str | The language code (Default en-US) (optional) (default to )

try:
    # New - Fetch policy catalog for the given operating system version.
    api_response = api_instance.catalogs_v1_get_policy_catalog_async(os_version_uuid, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsV1Api->catalogs_v1_get_policy_catalog_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_version_uuid** | [**str**](.md)| The operating system version identifier(Required) | 
 **language** | **str**| The language code (Default en-US) | [optional] [default to ]

### Return type

[**PolicyCatalogModel**](PolicyCatalogModel.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

