# mdmv1.StagingBundlesV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**staging_bundles_v2_retrieve_sideload_staging_file**](StagingBundlesV2Api.md#staging_bundles_v2_retrieve_sideload_staging_file) | **GET** /product-components/staging-bundles/{stagingUuid}/sideload | New - Retrieves a side-load staging zip or tar.gz file


# **staging_bundles_v2_retrieve_sideload_staging_file**
> Stream staging_bundles_v2_retrieve_sideload_staging_file(staging_uuid, organizationgroupid=organizationgroupid, key=key, universal=universal)

New - Retrieves a side-load staging zip or tar.gz file

Retrieves a side-load zip or tar.gz file used for staging a device, installing the agent, installing staging content, and enrolling, used mostly on Rugged devices.

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
api_instance = mdmv1.StagingBundlesV2Api(mdmv1.ApiClient(configuration))
staging_uuid = 'staging_uuid_example' # str | staging bundle uuid(Required)
organizationgroupid = 56 # int | organization group id (optional)
key = '' # str | key used to encrypt some of the files in archive (optional) (default to )
universal =  # bool | when staging the device, set to true if you want the end-user to choose the organization group the device will be apart of. (optional) (default to )

try:
    # New - Retrieves a side-load staging zip or tar.gz file
    api_response = api_instance.staging_bundles_v2_retrieve_sideload_staging_file(staging_uuid, organizationgroupid=organizationgroupid, key=key, universal=universal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StagingBundlesV2Api->staging_bundles_v2_retrieve_sideload_staging_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staging_uuid** | [**str**](.md)| staging bundle uuid(Required) | 
 **organizationgroupid** | **int**| organization group id | [optional] 
 **key** | **str**| key used to encrypt some of the files in archive | [optional] [default to ]
 **universal** | **bool**| when staging the device, set to true if you want the end-user to choose the organization group the device will be apart of. | [optional] [default to ]

### Return type

[**Stream**](Stream.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

