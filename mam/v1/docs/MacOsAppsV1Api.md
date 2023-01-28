# mamv1.MacOsAppsV1Api

All URIs are relative to *https://awapi.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mac_os_apps_v1_create_mac_os_application**](MacOsAppsV1Api.md#mac_os_apps_v1_create_mac_os_application) | **POST** /groups/{id}/macos/apps | New - Creates a new macOS application with provided metadata for distribution on macOS Devices
[**mac_os_apps_v1_download_mac_os_application_metadata**](MacOsAppsV1Api.md#mac_os_apps_v1_download_mac_os_application_metadata) | **GET** /groups/{organizationGroupUuid}/macos/apps/{applicationUuid}/metadata | New - Download xml macOS application metadata
[**mac_os_apps_v1_update_mac_os_application**](MacOsAppsV1Api.md#mac_os_apps_v1_update_mac_os_application) | **PUT** /groups/{id}/macos/apps/{applicationId} | New - Updates a macOS application with provided metadata for distribution on macOS Devices


# **mac_os_apps_v1_create_mac_os_application**
> mac_os_apps_v1_create_mac_os_application(mac_os_application_model, id)

New - Creates a new macOS application with provided metadata for distribution on macOS Devices

Creates a new macOS application with provided metadata for distribution on macOS Devices

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.MacOsAppsV1Api(mamv1.ApiClient(configuration))
mac_os_application_model = mamv1.MacOsCreateApplicationRequestV1Model() # MacOsCreateApplicationRequestV1Model | macOS application metadata and icons(Required).
id = 56 # int | Unique identifier of the organization group to perform the operation.(Required).

try:
    # New - Creates a new macOS application with provided metadata for distribution on macOS Devices
    api_instance.mac_os_apps_v1_create_mac_os_application(mac_os_application_model, id)
except ApiException as e:
    print("Exception when calling MacOsAppsV1Api->mac_os_apps_v1_create_mac_os_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac_os_application_model** | [**MacOsCreateApplicationRequestV1Model**](MacOsCreateApplicationRequestV1Model.md)| macOS application metadata and icons(Required). | 
 **id** | **int**| Unique identifier of the organization group to perform the operation.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mac_os_apps_v1_download_mac_os_application_metadata**
> mac_os_apps_v1_download_mac_os_application_metadata(organization_group_uuid, application_uuid)

New - Download xml macOS application metadata

Download xml macOS application metadata

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.MacOsAppsV1Api(mamv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Uuid of the organization group to perform the operation.(Required).
application_uuid = 'application_uuid_example' # str | Application Uuid to perform the operation on.(Required).

try:
    # New - Download xml macOS application metadata
    api_instance.mac_os_apps_v1_download_mac_os_application_metadata(organization_group_uuid, application_uuid)
except ApiException as e:
    print("Exception when calling MacOsAppsV1Api->mac_os_apps_v1_download_mac_os_application_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Uuid of the organization group to perform the operation.(Required). | 
 **application_uuid** | [**str**](.md)| Application Uuid to perform the operation on.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mac_os_apps_v1_update_mac_os_application**
> mac_os_apps_v1_update_mac_os_application(mac_os_application_model, id, application_id)

New - Updates a macOS application with provided metadata for distribution on macOS Devices

Updates a macOS application with provided metadata for distribution on macOS Devices

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.MacOsAppsV1Api(mamv1.ApiClient(configuration))
mac_os_application_model = mamv1.MacOsEditApplicationRequestV1Model() # MacOsEditApplicationRequestV1Model | macOS application metadata and icons(Required).
id = 56 # int | Unique identifier of the organization group to perform the operation.(Required).
application_id = 'application_id_example' # str | Application ID to perform the operation on.(Required).

try:
    # New - Updates a macOS application with provided metadata for distribution on macOS Devices
    api_instance.mac_os_apps_v1_update_mac_os_application(mac_os_application_model, id, application_id)
except ApiException as e:
    print("Exception when calling MacOsAppsV1Api->mac_os_apps_v1_update_mac_os_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac_os_application_model** | [**MacOsEditApplicationRequestV1Model**](MacOsEditApplicationRequestV1Model.md)| macOS application metadata and icons(Required). | 
 **id** | **int**| Unique identifier of the organization group to perform the operation.(Required). | 
 **application_id** | **str**| Application ID to perform the operation on.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

