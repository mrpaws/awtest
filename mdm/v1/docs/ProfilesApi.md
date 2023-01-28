# mdmv1.ProfilesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profiles_execute_install_profile_commands**](ProfilesApi.md#profiles_execute_install_profile_commands) | **POST** /devices/{id}/commands/installprofile | Installs the profile on device.
[**profiles_get_profiles_by_alternate_id**](ProfilesApi.md#profiles_get_profiles_by_alternate_id) | **GET** /devices/profiles | Retrieves the profile details of the device identified by alternate ID.
[**profiles_get_profiles_by_device**](ProfilesApi.md#profiles_get_profiles_by_device) | **GET** /devices/{id}/profiles | Retrieves the profile details of the device by Device ID.


# **profiles_execute_install_profile_commands**
> profiles_execute_install_profile_commands(id, payloads, profileid=profileid)

Installs the profile on device.

Queues up installation commands for interactive profiles for a device by overriding payload settings.

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
api_instance = mdmv1.ProfilesApi(mdmv1.ApiClient(configuration))
id = 'id_example' # str | The device ID (Required).
payloads = [mdmv1.PayloadModel()] # list[PayloadModel] | Array of payload bodies (Required).
profileid = 56 # int | Profile id. (optional)

try:
    # Installs the profile on device.
    api_instance.profiles_execute_install_profile_commands(id, payloads, profileid=profileid)
except ApiException as e:
    print("Exception when calling ProfilesApi->profiles_execute_install_profile_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The device ID (Required). | 
 **payloads** | [**list[PayloadModel]**](PayloadModel.md)| Array of payload bodies (Required). | 
 **profileid** | **int**| Profile id. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_get_profiles_by_alternate_id**
> DeviceProfileSearchResult profiles_get_profiles_by_alternate_id(search_by=search_by, id=id, page=page, pagesize=pagesize)

Retrieves the profile details of the device identified by alternate ID.

Fetches all the profiles and details for the device identified by alternate ID other than device ID.  Alternate device identifiers can be MAC address, IMEI, Serial number or UDID.  Example : IMEI-BCG84753GH, Serial Number-573489754.

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
api_instance = mdmv1.ProfilesApi(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber]. (optional) (default to )
id = '' # str | Device alternate id. (optional) (default to )
page = 56 # int | The specific page number to get. (optional)
pagesize = 56 # int | Max records per page. (optional)

try:
    # Retrieves the profile details of the device identified by alternate ID.
    api_response = api_instance.profiles_get_profiles_by_alternate_id(search_by=search_by, id=id, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesApi->profiles_get_profiles_by_alternate_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber]. | [optional] [default to ]
 **id** | **str**| Device alternate id. | [optional] [default to ]
 **page** | **int**| The specific page number to get. | [optional] 
 **pagesize** | **int**| Max records per page. | [optional] 

### Return type

[**DeviceProfileSearchResult**](DeviceProfileSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_get_profiles_by_device**
> DeviceProfileSearchResult profiles_get_profiles_by_device(id, page=page, pagesize=pagesize)

Retrieves the profile details of the device by Device ID.

Fetches all the profiles and details for the device identified by device ID.

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
api_instance = mdmv1.ProfilesApi(mdmv1.ApiClient(configuration))
id = 56 # int | DeviceID is the unique identifier for devices in AirWatch (Required).
page = 56 # int | The specific page number to get. (optional)
pagesize = 56 # int | Max records per page. (optional)

try:
    # Retrieves the profile details of the device by Device ID.
    api_response = api_instance.profiles_get_profiles_by_device(id, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesApi->profiles_get_profiles_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| DeviceID is the unique identifier for devices in AirWatch (Required). | 
 **page** | **int**| The specific page number to get. | [optional] 
 **pagesize** | **int**| Max records per page. | [optional] 

### Return type

[**DeviceProfileSearchResult**](DeviceProfileSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

