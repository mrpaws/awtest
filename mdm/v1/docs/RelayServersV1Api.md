# mdmv1.RelayServersV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**relay_servers_v1_add_relay_server**](RelayServersV1Api.md#relay_servers_v1_add_relay_server) | **POST** /relayservers | New - Creates a new relay server provided valid values are given.
[**relay_servers_v1_add_relay_servers_in_bulk**](RelayServersV1Api.md#relay_servers_v1_add_relay_servers_in_bulk) | **POST** /relayservers/bulk | New - Creates new relay servers in bulk provided valid values are given.
[**relay_servers_v1_delete_relay_server**](RelayServersV1Api.md#relay_servers_v1_delete_relay_server) | **DELETE** /relayservers/{serverId} | New - Delete the relay server.
[**relay_servers_v1_get_server_details**](RelayServersV1Api.md#relay_servers_v1_get_server_details) | **GET** /relayservers/{serverId} | New - Gets details of existing relay server.
[**relay_servers_v1_posts_contents_on_relay_server_async**](RelayServersV1Api.md#relay_servers_v1_posts_contents_on_relay_server_async) | **POST** /relayservers/contents | New - Posts contents for the eligible relay server for the product and og inputted.
[**relay_servers_v1_update_relay_server**](RelayServersV1Api.md#relay_servers_v1_update_relay_server) | **PUT** /relayservers | New - Update the details existing relay server.


# **relay_servers_v1_add_relay_server**
> relay_servers_v1_add_relay_server(relay_server_details=relay_server_details)

New - Creates a new relay server provided valid values are given.

Creates a new relay server based on the valid values given.<br>Relay server is a FTP server from where the devices can download the provisioning files.  This is done inorder to reduce the load of deviceservices.</br><br>These details include Name of relay server, Organization group under which it is managed, Username, Password, Connection details for the device and console to connect.</br>

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
api_instance = mdmv1.RelayServersV1Api(mdmv1.ApiClient(configuration))
relay_server_details = mdmv1.RelayServerDetailsModel_() # RelayServerDetailsModel_ | Details of the relay server to be created. (optional)

try:
    # New - Creates a new relay server provided valid values are given.
    api_instance.relay_servers_v1_add_relay_server(relay_server_details=relay_server_details)
except ApiException as e:
    print("Exception when calling RelayServersV1Api->relay_servers_v1_add_relay_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_server_details** | [**RelayServerDetailsModel_**](RelayServerDetailsModel_.md)| Details of the relay server to be created. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_servers_v1_add_relay_servers_in_bulk**
> RelayServerBulkResponseModel relay_servers_v1_add_relay_servers_in_bulk(relay_server_details_list)

New - Creates new relay servers in bulk provided valid values are given.

Creates new relay servers in bulk with valid values given.

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
api_instance = mdmv1.RelayServersV1Api(mdmv1.ApiClient(configuration))
relay_server_details_list = [mdmv1.RelayServerDetailsModel_()] # list[RelayServerDetailsModel_] | List of details of the relay server to be added.(Required)

try:
    # New - Creates new relay servers in bulk provided valid values are given.
    api_response = api_instance.relay_servers_v1_add_relay_servers_in_bulk(relay_server_details_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelayServersV1Api->relay_servers_v1_add_relay_servers_in_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_server_details_list** | [**list[RelayServerDetailsModel_]**](RelayServerDetailsModel_.md)| List of details of the relay server to be added.(Required) | 

### Return type

[**RelayServerBulkResponseModel**](RelayServerBulkResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_servers_v1_delete_relay_server**
> relay_servers_v1_delete_relay_server(server_id)

New - Delete the relay server.

Deletes the existing relay server.

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
api_instance = mdmv1.RelayServersV1Api(mdmv1.ApiClient(configuration))
server_id = 56 # int | Id of the relay server.

try:
    # New - Delete the relay server.
    api_instance.relay_servers_v1_delete_relay_server(server_id)
except ApiException as e:
    print("Exception when calling RelayServersV1Api->relay_servers_v1_delete_relay_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Id of the relay server. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_servers_v1_get_server_details**
> RelayServerDetailsModel_ relay_servers_v1_get_server_details(server_id)

New - Gets details of existing relay server.

Fetch the details of the existing relay server.<br>These details include Name of relay server, Organization group under which it is managed, Username, Password, Connection details for the device and console to connect.</br>

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
api_instance = mdmv1.RelayServersV1Api(mdmv1.ApiClient(configuration))
server_id = 56 # int | Relay server id.

try:
    # New - Gets details of existing relay server.
    api_response = api_instance.relay_servers_v1_get_server_details(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelayServersV1Api->relay_servers_v1_get_server_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Relay server id. | 

### Return type

[**RelayServerDetailsModel_**](RelayServerDetailsModel_.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_servers_v1_posts_contents_on_relay_server_async**
> relay_servers_v1_posts_contents_on_relay_server_async(relay_server_content_input_model)

New - Posts contents for the eligible relay server for the product and og inputted.

Posts contents for the eligible relay server for the product and og inputted when there are no devices enrolled in the organization group.

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
api_instance = mdmv1.RelayServersV1Api(mdmv1.ApiClient(configuration))
relay_server_content_input_model = mdmv1.RelayServerContentInputModel() # RelayServerContentInputModel | Input representing product uuid and organization group uuid(Required)

try:
    # New - Posts contents for the eligible relay server for the product and og inputted.
    api_instance.relay_servers_v1_posts_contents_on_relay_server_async(relay_server_content_input_model)
except ApiException as e:
    print("Exception when calling RelayServersV1Api->relay_servers_v1_posts_contents_on_relay_server_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_server_content_input_model** | [**RelayServerContentInputModel**](RelayServerContentInputModel.md)| Input representing product uuid and organization group uuid(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_servers_v1_update_relay_server**
> relay_servers_v1_update_relay_server(relay_server_details=relay_server_details)

New - Update the details existing relay server.

Update the details of existing relay server. <br>These details include Name of relay server, Organization group under which it is managed, Username, Password, Connection details for the device and console to connect. </br>

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
api_instance = mdmv1.RelayServersV1Api(mdmv1.ApiClient(configuration))
relay_server_details = mdmv1.RelayServerDetailsModel() # RelayServerDetailsModel | Details of the relay server to be updated. (optional)

try:
    # New - Update the details existing relay server.
    api_instance.relay_servers_v1_update_relay_server(relay_server_details=relay_server_details)
except ApiException as e:
    print("Exception when calling RelayServersV1Api->relay_servers_v1_update_relay_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_server_details** | [**RelayServerDetailsModel**](RelayServerDetailsModel.md)| Details of the relay server to be updated. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

