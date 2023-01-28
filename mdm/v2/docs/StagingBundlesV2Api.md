# mdmv2.StagingBundlesV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**staging_bundles_v2_staging_bundles**](StagingBundlesV2Api.md#staging_bundles_v2_staging_bundles) | **GET** /product-components/staging-bundles/{stagingUuid} | New - Finds Staging Bundle by Staging Bundle UUID
[**staging_bundles_v2_staging_bundles_add**](StagingBundlesV2Api.md#staging_bundles_v2_staging_bundles_add) | **POST** /product-components/staging-bundles | New - Adds a new Staging Bundle
[**staging_bundles_v2_staging_bundles_delete**](StagingBundlesV2Api.md#staging_bundles_v2_staging_bundles_delete) | **DELETE** /product-components/staging-bundles/{stagingUuid} | New - Deletes a Staging Bundle identified by Staging Bundle UUID
[**staging_bundles_v2_staging_bundles_update**](StagingBundlesV2Api.md#staging_bundles_v2_staging_bundles_update) | **PUT** /product-components/staging-bundles | New - Updates a Staging Bundle identified by Staging Bundle UUID


# **staging_bundles_v2_staging_bundles**
> StagingBundleV2Model staging_bundles_v2_staging_bundles(staging_uuid)

New - Finds Staging Bundle by Staging Bundle UUID

Returns a single Staging Bundle identified by Staging Bundle UUID

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.StagingBundlesV2Api(mdmv2.ApiClient(configuration))
staging_uuid = 'staging_uuid_example' # str | UUID of Staging Bundle to return(Required)

try:
    # New - Finds Staging Bundle by Staging Bundle UUID
    api_response = api_instance.staging_bundles_v2_staging_bundles(staging_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StagingBundlesV2Api->staging_bundles_v2_staging_bundles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staging_uuid** | [**str**](.md)| UUID of Staging Bundle to return(Required) | 

### Return type

[**StagingBundleV2Model**](StagingBundleV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staging_bundles_v2_staging_bundles_add**
> staging_bundles_v2_staging_bundles_add(body)

New - Adds a new Staging Bundle

Adds a new Staging Bundle

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.StagingBundlesV2Api(mdmv2.ApiClient(configuration))
body = mdmv2.StagingBundleRequestV2Model() # StagingBundleRequestV2Model | Staging Bundle that needs to be added(Required)

try:
    # New - Adds a new Staging Bundle
    api_instance.staging_bundles_v2_staging_bundles_add(body)
except ApiException as e:
    print("Exception when calling StagingBundlesV2Api->staging_bundles_v2_staging_bundles_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StagingBundleRequestV2Model**](StagingBundleRequestV2Model.md)| Staging Bundle that needs to be added(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staging_bundles_v2_staging_bundles_delete**
> staging_bundles_v2_staging_bundles_delete(staging_uuid)

New - Deletes a Staging Bundle identified by Staging Bundle UUID

Deletes a Staging Bundle package identified by the Staging Bundle UUID

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.StagingBundlesV2Api(mdmv2.ApiClient(configuration))
staging_uuid = 'staging_uuid_example' # str | UUID of Staging Bundle to return(Required)

try:
    # New - Deletes a Staging Bundle identified by Staging Bundle UUID
    api_instance.staging_bundles_v2_staging_bundles_delete(staging_uuid)
except ApiException as e:
    print("Exception when calling StagingBundlesV2Api->staging_bundles_v2_staging_bundles_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staging_uuid** | [**str**](.md)| UUID of Staging Bundle to return(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staging_bundles_v2_staging_bundles_update**
> staging_bundles_v2_staging_bundles_update(body)

New - Updates a Staging Bundle identified by Staging Bundle UUID

Updates a Staging Bundle with Staging Bundle UUID as the required field

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.StagingBundlesV2Api(mdmv2.ApiClient(configuration))
body = mdmv2.StagingBundleRequestV2Model() # StagingBundleRequestV2Model | Staging Bundle that needs to be updated(Required)

try:
    # New - Updates a Staging Bundle identified by Staging Bundle UUID
    api_instance.staging_bundles_v2_staging_bundles_update(body)
except ApiException as e:
    print("Exception when calling StagingBundlesV2Api->staging_bundles_v2_staging_bundles_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StagingBundleRequestV2Model**](StagingBundleRequestV2Model.md)| Staging Bundle that needs to be updated(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

