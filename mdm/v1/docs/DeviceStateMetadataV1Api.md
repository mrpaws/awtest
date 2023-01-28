# mdmv1.DeviceStateMetadataV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_state_metadata_v1_get_device_state_metadata_async**](DeviceStateMetadataV1Api.md#device_state_metadata_v1_get_device_state_metadata_async) | **GET** /devicestatemetadata/{organizationgroupUuid} | New - Get device state attribute metadata for an Organization Group.


# **device_state_metadata_v1_get_device_state_metadata_async**
> DeviceStateMetadataModel device_state_metadata_v1_get_device_state_metadata_async(organizationgroup_uuid)

New - Get device state attribute metadata for an Organization Group.



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
api_instance = mdmv1.DeviceStateMetadataV1Api(mdmv1.ApiClient(configuration))
organizationgroup_uuid = 'organizationgroup_uuid_example' # str | Uuid of the Organization Group.(Required)

try:
    # New - Get device state attribute metadata for an Organization Group.
    api_response = api_instance.device_state_metadata_v1_get_device_state_metadata_async(organizationgroup_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceStateMetadataV1Api->device_state_metadata_v1_get_device_state_metadata_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroup_uuid** | [**str**](.md)| Uuid of the Organization Group.(Required) | 

### Return type

[**DeviceStateMetadataModel**](DeviceStateMetadataModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

