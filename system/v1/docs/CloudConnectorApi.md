# systemv1.CloudConnectorApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloud_connector_get_connection_status_async**](CloudConnectorApi.md#cloud_connector_get_connection_status_async) | **GET** /groups/{organizationGroupUuid}/cloud-connector/connection-status | New - Returns the connection status for the AirWatch Cloud Connector configured for the given organization group.


# **cloud_connector_get_connection_status_async**
> ConnectionStatusV1Model cloud_connector_get_connection_status_async(organization_group_uuid)

New - Returns the connection status for the AirWatch Cloud Connector configured for the given organization group.

Gets the AirWatch Cloud Connector connection status for the organization group.

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

# create an instance of the API class
api_instance = systemv1.CloudConnectorApi(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | The unique identifier of the organization group.(Required).

try:
    # New - Returns the connection status for the AirWatch Cloud Connector configured for the given organization group.
    api_response = api_instance.cloud_connector_get_connection_status_async(organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudConnectorApi->cloud_connector_get_connection_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| The unique identifier of the organization group.(Required). | 

### Return type

[**ConnectionStatusV1Model**](ConnectionStatusV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

