# systemv1.SSLPinningApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s_sl_pinning_create_pinned_host_async**](SSLPinningApi.md#s_sl_pinning_create_pinned_host_async) | **POST** /sslpinning/pinnedhost | Create a pinned host.
[**s_sl_pinning_disable_pin_async**](SSLPinningApi.md#s_sl_pinning_disable_pin_async) | **POST** /sslpinning/disablepin/{hostGuid}/{organizationgroupid} | Disable a pinned relationship between host and cert.
[**s_sl_pinning_disable_pinning_async**](SSLPinningApi.md#s_sl_pinning_disable_pinning_async) | **POST** /sslpinning/disable/{organizationgroupid} | Disable SSL Pinning at an Organization Group.
[**s_sl_pinning_enable_pin_async**](SSLPinningApi.md#s_sl_pinning_enable_pin_async) | **POST** /sslpinning/enablepin/{hostGuid}/{organizationgroupid} | Enable a pinned relationship between host and cert.
[**s_sl_pinning_enable_pinning_async**](SSLPinningApi.md#s_sl_pinning_enable_pinning_async) | **POST** /sslpinning/enable/{organizationgroupid} | Enable SSL Pinning at an Organization Group.
[**s_sl_pinning_find_pinned_hosts_async**](SSLPinningApi.md#s_sl_pinning_find_pinned_hosts_async) | **GET** /sslpinning/pinnedhosts | Query for pinned hosts by host name.
[**s_sl_pinning_pin_certificate_to_host_async**](SSLPinningApi.md#s_sl_pinning_pin_certificate_to_host_async) | **POST** /sslpinning/pincertificate | Pin a given certificate to a pinned host.
[**s_sl_pinning_remove_pinned_host_async**](SSLPinningApi.md#s_sl_pinning_remove_pinned_host_async) | **DELETE** /sslpinning/pinnedhost/{hostGuid} | Query for pinned hosts by UDID.
[**s_sl_pinning_sync_with_auto_discovery_async**](SSLPinningApi.md#s_sl_pinning_sync_with_auto_discovery_async) | **POST** /sslpinning/syncwithautodiscovery/{organizationgroupid} | Synchronize Pins with Auto Discovery at an Organization Group.
[**s_sl_pinning_unpin_certificate_from_host_async**](SSLPinningApi.md#s_sl_pinning_unpin_certificate_from_host_async) | **POST** /sslpinning/unpincertificate | Unpin a given certificate from a pinned host.
[**s_sl_pinning_update_pinned_host_async**](SSLPinningApi.md#s_sl_pinning_update_pinned_host_async) | **PATCH** /sslpinning/pinnedhost/{hostGuid} | Update a specific pinned host.


# **s_sl_pinning_create_pinned_host_async**
> PinnedHostResponseModel s_sl_pinning_create_pinned_host_async(model)

Create a pinned host.

Accepts and parses a fully qualified domain name for the contextual, or specified, Organization Group and creates a container to attach acceptable public keys to.

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
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.SSLPinningApi(systemv1.ApiClient(configuration))
model = systemv1.PinnedHostModel() # PinnedHostModel | Specifies the Pinned Host to be created (Required).

try:
    # Create a pinned host.
    api_response = api_instance.s_sl_pinning_create_pinned_host_async(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSLPinningApi->s_sl_pinning_create_pinned_host_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**PinnedHostModel**](PinnedHostModel.md)| Specifies the Pinned Host to be created (Required). | 

### Return type

[**PinnedHostResponseModel**](PinnedHostResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_sl_pinning_disable_pin_async**
> s_sl_pinning_disable_pin_async(host_guid, organizationgroupid)

Disable a pinned relationship between host and cert.

Disables the enforcement of pinning for one particular Pinned Host-Pinned Certificate pair.

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
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.SSLPinningApi(systemv1.ApiClient(configuration))
host_guid = 'host_guid_example' # str | The ID of the pertinent host (Required).
organizationgroupid = 56 # int | The Organization Group to disable at (Required).

try:
    # Disable a pinned relationship between host and cert.
    api_instance.s_sl_pinning_disable_pin_async(host_guid, organizationgroupid)
except ApiException as e:
    print("Exception when calling SSLPinningApi->s_sl_pinning_disable_pin_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_guid** | [**str**](.md)| The ID of the pertinent host (Required). | 
 **organizationgroupid** | **int**| The Organization Group to disable at (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_sl_pinning_disable_pinning_async**
> s_sl_pinning_disable_pinning_async(organizationgroupid)

Disable SSL Pinning at an Organization Group.

Disables the enforcement of SSL Pinning at the specified Organization Group if it is allowed.

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
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.SSLPinningApi(systemv1.ApiClient(configuration))
organizationgroupid = 56 # int | The ID of the organization group to disable at (Required).

try:
    # Disable SSL Pinning at an Organization Group.
    api_instance.s_sl_pinning_disable_pinning_async(organizationgroupid)
except ApiException as e:
    print("Exception when calling SSLPinningApi->s_sl_pinning_disable_pinning_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| The ID of the organization group to disable at (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_sl_pinning_enable_pin_async**
> s_sl_pinning_enable_pin_async(host_guid, organizationgroupid)

Enable a pinned relationship between host and cert.

Enables the enforcement of pinning for one particular Pinned Host-Pinned Certificate pair.

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
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.SSLPinningApi(systemv1.ApiClient(configuration))
host_guid = 'host_guid_example' # str | The ID of the pertinent host (Required).
organizationgroupid = 56 # int | The ID of the organization group.

try:
    # Enable a pinned relationship between host and cert.
    api_instance.s_sl_pinning_enable_pin_async(host_guid, organizationgroupid)
except ApiException as e:
    print("Exception when calling SSLPinningApi->s_sl_pinning_enable_pin_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_guid** | [**str**](.md)| The ID of the pertinent host (Required). | 
 **organizationgroupid** | **int**| The ID of the organization group. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_sl_pinning_enable_pinning_async**
> s_sl_pinning_enable_pinning_async(organizationgroupid)

Enable SSL Pinning at an Organization Group.

Enables the enforcement of SSL Pinning at the specified Organization Group if it is allowed.

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
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.SSLPinningApi(systemv1.ApiClient(configuration))
organizationgroupid = 56 # int | The ID of the organization group to enable at (Required).

try:
    # Enable SSL Pinning at an Organization Group.
    api_instance.s_sl_pinning_enable_pinning_async(organizationgroupid)
except ApiException as e:
    print("Exception when calling SSLPinningApi->s_sl_pinning_enable_pinning_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| The ID of the organization group to enable at (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_sl_pinning_find_pinned_hosts_async**
> list[CertificatePinningHostEntity] s_sl_pinning_find_pinned_hosts_async(host_name=host_name, organizationgroupid=organizationgroupid)

Query for pinned hosts by host name.

Finds and returns all pinned hosts and their associated public keys that match the fully qualified domain name of the search criteria that are visible at the contextual, or specified, Organization Group.

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
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.SSLPinningApi(systemv1.ApiClient(configuration))
host_name = 'host_name_example' # str | The hostname to query for (Required). (optional)
organizationgroupid = 56 # int | The organization group to check at. (optional)

try:
    # Query for pinned hosts by host name.
    api_response = api_instance.s_sl_pinning_find_pinned_hosts_async(host_name=host_name, organizationgroupid=organizationgroupid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSLPinningApi->s_sl_pinning_find_pinned_hosts_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| The hostname to query for (Required). | [optional] 
 **organizationgroupid** | **int**| The organization group to check at. | [optional] 

### Return type

[**list[CertificatePinningHostEntity]**](CertificatePinningHostEntity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_sl_pinning_pin_certificate_to_host_async**
> OperationStatusModel s_sl_pinning_pin_certificate_to_host_async(model)

Pin a given certificate to a pinned host.

Processes a public key from a provided certificate and maps it to the pinned host with the specified UUID.

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
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.SSLPinningApi(systemv1.ApiClient(configuration))
model = systemv1.PinnedCertificateModel() # PinnedCertificateModel | The model of the pinned certificate containing Host ID and the Base64 Certificate (Required).

try:
    # Pin a given certificate to a pinned host.
    api_response = api_instance.s_sl_pinning_pin_certificate_to_host_async(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSLPinningApi->s_sl_pinning_pin_certificate_to_host_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**PinnedCertificateModel**](PinnedCertificateModel.md)| The model of the pinned certificate containing Host ID and the Base64 Certificate (Required). | 

### Return type

[**OperationStatusModel**](OperationStatusModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_sl_pinning_remove_pinned_host_async**
> s_sl_pinning_remove_pinned_host_async(host_guid)

Query for pinned hosts by UDID.

Returns the pinned host and its associated public keys with the specified UUID and that are visible at the contextual, or specified, Organization Group.

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
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.SSLPinningApi(systemv1.ApiClient(configuration))
host_guid = 'host_guid_example' # str | The ID (returned during creation or a query) of the host to delete (Required).

try:
    # Query for pinned hosts by UDID.
    api_instance.s_sl_pinning_remove_pinned_host_async(host_guid)
except ApiException as e:
    print("Exception when calling SSLPinningApi->s_sl_pinning_remove_pinned_host_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_guid** | [**str**](.md)| The ID (returned during creation or a query) of the host to delete (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_sl_pinning_sync_with_auto_discovery_async**
> OperationStatusModel s_sl_pinning_sync_with_auto_discovery_async(organizationgroupid)

Synchronize Pins with Auto Discovery at an Organization Group.

Initiates the synchronization routine with Auto Discovery to send it the pinned public keys for the Device Services host at the specified Organization Group.

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
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.SSLPinningApi(systemv1.ApiClient(configuration))
organizationgroupid = 56 # int | The ID of the organization group (Required).

try:
    # Synchronize Pins with Auto Discovery at an Organization Group.
    api_response = api_instance.s_sl_pinning_sync_with_auto_discovery_async(organizationgroupid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSLPinningApi->s_sl_pinning_sync_with_auto_discovery_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| The ID of the organization group (Required). | 

### Return type

[**OperationStatusModel**](OperationStatusModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_sl_pinning_unpin_certificate_from_host_async**
> s_sl_pinning_unpin_certificate_from_host_async(model)

Unpin a given certificate from a pinned host.

Un-maps the certificate with the specified thumbprint from the pinned host with the specified UUID.

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
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.SSLPinningApi(systemv1.ApiClient(configuration))
model = systemv1.PinnedCertificateQueryModel() # PinnedCertificateQueryModel | The model of the Pinned Certificate containing Host ID and Certificate Thumbprint (Required).

try:
    # Unpin a given certificate from a pinned host.
    api_instance.s_sl_pinning_unpin_certificate_from_host_async(model)
except ApiException as e:
    print("Exception when calling SSLPinningApi->s_sl_pinning_unpin_certificate_from_host_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**PinnedCertificateQueryModel**](PinnedCertificateQueryModel.md)| The model of the Pinned Certificate containing Host ID and Certificate Thumbprint (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_sl_pinning_update_pinned_host_async**
> s_sl_pinning_update_pinned_host_async(host_guid, model)

Update a specific pinned host.

Updates the pinned host with the given UUID with new details, including a parsed FQDN.

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
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.SSLPinningApi(systemv1.ApiClient(configuration))
host_guid = 'host_guid_example' # str | The ID of the host to delete (Required).
model = systemv1.PinnedHostModel() # PinnedHostModel | The model that describes the host update (Required).

try:
    # Update a specific pinned host.
    api_instance.s_sl_pinning_update_pinned_host_async(host_guid, model)
except ApiException as e:
    print("Exception when calling SSLPinningApi->s_sl_pinning_update_pinned_host_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_guid** | [**str**](.md)| The ID of the host to delete (Required). | 
 **model** | [**PinnedHostModel**](PinnedHostModel.md)| The model that describes the host update (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

