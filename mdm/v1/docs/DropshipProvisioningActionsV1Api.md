# mdmv1.DropshipProvisioningActionsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dropship_provisioning_actions_v1_dropship_provisioning_actions_async**](DropshipProvisioningActionsV1Api.md#dropship_provisioning_actions_v1_dropship_provisioning_actions_async) | **POST** /dropship-action/organization-group/{ogUuid}/sync-devices | New - Sync devices for given organization group.


# **dropship_provisioning_actions_v1_dropship_provisioning_actions_async**
> dropship_provisioning_actions_v1_dropship_provisioning_actions_async(og_uuid)

New - Sync devices for given organization group.

Sync devices from OEM Provisioning Service for given organization group UUID.

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
api_instance = mdmv1.DropshipProvisioningActionsV1Api(mdmv1.ApiClient(configuration))
og_uuid = 'og_uuid_example' # str | Organization group UUID to perform the operation on.(Required).

try:
    # New - Sync devices for given organization group.
    api_instance.dropship_provisioning_actions_v1_dropship_provisioning_actions_async(og_uuid)
except ApiException as e:
    print("Exception when calling DropshipProvisioningActionsV1Api->dropship_provisioning_actions_v1_dropship_provisioning_actions_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **og_uuid** | [**str**](.md)| Organization group UUID to perform the operation on.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

