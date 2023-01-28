# mdmv1.AppleV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apple_v1_create_remote_view_destination_by_location_group_id**](AppleV1Api.md#apple_v1_create_remote_view_destination_by_location_group_id) | **POST** /apple/remoteviewdestination | New - Add a destination for Remote View
[**apple_v1_delete_remote_view_destination_by_id**](AppleV1Api.md#apple_v1_delete_remote_view_destination_by_id) | **DELETE** /apple/remoteviewdestination/{id} | New - Delete a Remote View destination for the device
[**apple_v1_get_remote_view_destination_by_id**](AppleV1Api.md#apple_v1_get_remote_view_destination_by_id) | **GET** /apple/remoteviewdestination/{id} | New - Gets Remote View destination details for the device
[**apple_v1_get_remote_view_destination_by_location_group_id**](AppleV1Api.md#apple_v1_get_remote_view_destination_by_location_group_id) | **GET** /apple/remoteviewdestination | New - Gets the list of Remote View destinations configured in the organization group
[**apple_v1_update_remote_view_destination_by_id**](AppleV1Api.md#apple_v1_update_remote_view_destination_by_id) | **PUT** /apple/remoteviewdestination | New - Update the destination details of a previously configured Remote View destination.


# **apple_v1_create_remote_view_destination_by_location_group_id**
> apple_v1_create_remote_view_destination_by_location_group_id(model)

New - Add a destination for Remote View

iOS device can be remotely viewed by using software like AirServer or Reflector. It is required to save the details of the destination device like mac address, ip address, pk, pi. This endpoint is used to save the destination details for the organization group.

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
api_instance = mdmv1.AppleV1Api(mdmv1.ApiClient(configuration))
model = mdmv1.RemoteViewDestinationV1Model() # RemoteViewDestinationV1Model | RemoteViewDestination data(Required)

try:
    # New - Add a destination for Remote View
    api_instance.apple_v1_create_remote_view_destination_by_location_group_id(model)
except ApiException as e:
    print("Exception when calling AppleV1Api->apple_v1_create_remote_view_destination_by_location_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**RemoteViewDestinationV1Model**](RemoteViewDestinationV1Model.md)| RemoteViewDestination data(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apple_v1_delete_remote_view_destination_by_id**
> apple_v1_delete_remote_view_destination_by_id(id)

New - Delete a Remote View destination for the device

This api is used to delete the destination details for the organization group, destination details like mac address, ip address, pk, pi  are required for remote viewing the iOS device

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
api_instance = mdmv1.AppleV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Id of Remote View destination device to be deleted(Required)

try:
    # New - Delete a Remote View destination for the device
    api_instance.apple_v1_delete_remote_view_destination_by_id(id)
except ApiException as e:
    print("Exception when calling AppleV1Api->apple_v1_delete_remote_view_destination_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of Remote View destination device to be deleted(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apple_v1_get_remote_view_destination_by_id**
> RemoteViewDestinationV1Model apple_v1_get_remote_view_destination_by_id(id)

New - Gets Remote View destination details for the device

This api is used to get the details of the specified destination. Destination details like mac address, ip address, pk, pi  are required for remote viewing the iOS device

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
api_instance = mdmv1.AppleV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Id of the Remote View destination device(Required)

try:
    # New - Gets Remote View destination details for the device
    api_response = api_instance.apple_v1_get_remote_view_destination_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleV1Api->apple_v1_get_remote_view_destination_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the Remote View destination device(Required) | 

### Return type

[**RemoteViewDestinationV1Model**](RemoteViewDestinationV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apple_v1_get_remote_view_destination_by_location_group_id**
> RemoteViewDestinationV1Model apple_v1_get_remote_view_destination_by_location_group_id(group_id, group_id2)

New - Gets the list of Remote View destinations configured in the organization group

This api is used to get list of destinations for the organization group. Destination details like mac address, ip address, pk, pi  are required for remote viewing the iOS device

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
api_instance = mdmv1.AppleV1Api(mdmv1.ApiClient(configuration))
group_id = 56 # int | Id of organization group(Required)
group_id2 = 56 # int | Id of organization group(Required)

try:
    # New - Gets the list of Remote View destinations configured in the organization group
    api_response = api_instance.apple_v1_get_remote_view_destination_by_location_group_id(group_id, group_id2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleV1Api->apple_v1_get_remote_view_destination_by_location_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of organization group(Required) | 
 **group_id2** | **int**| Id of organization group(Required) | 

### Return type

[**RemoteViewDestinationV1Model**](RemoteViewDestinationV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apple_v1_update_remote_view_destination_by_id**
> apple_v1_update_remote_view_destination_by_id(model)

New - Update the destination details of a previously configured Remote View destination.

iOS device can be remotely viewed by using software like AirServer or Reflector, it is required to save the details of the destination device like mac address, ip address, pk, pi. This endpoint is used to edit the details of a previously configured destination for the organization group.

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
api_instance = mdmv1.AppleV1Api(mdmv1.ApiClient(configuration))
model = mdmv1.RemoteViewDestinationV1Model() # RemoteViewDestinationV1Model | RemoteViewDestination data(Required)

try:
    # New - Update the destination details of a previously configured Remote View destination.
    api_instance.apple_v1_update_remote_view_destination_by_id(model)
except ApiException as e:
    print("Exception when calling AppleV1Api->apple_v1_update_remote_view_destination_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**RemoteViewDestinationV1Model**](RemoteViewDestinationV1Model.md)| RemoteViewDestination data(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

