# mdmv1.BitLockerV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bit_locker_v1_get_device_bit_locker_drive_info_async**](BitLockerV1Api.md#bit_locker_v1_get_device_bit_locker_drive_info_async) | **GET** /devices/{deviceUuid}/bitlocker/drives | Returns the Bit Locker drive level information for the device.
[**bit_locker_v1_get_device_bit_locker_protector_info_async**](BitLockerV1Api.md#bit_locker_v1_get_device_bit_locker_protector_info_async) | **GET** /devices/{deviceUuid}/bitlocker/drives/{volumeIdentifier}/protectors | Returns the Bit Locker protector information for the device.


# **bit_locker_v1_get_device_bit_locker_drive_info_async**
> DeviceBitLockerDriveV1Model bit_locker_v1_get_device_bit_locker_drive_info_async(device_uuid)

Returns the Bit Locker drive level information for the device.

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
api_instance = mdmv1.BitLockerV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Unique identifier for the device(Required).

try:
    # Returns the Bit Locker drive level information for the device.
    api_response = api_instance.bit_locker_v1_get_device_bit_locker_drive_info_async(device_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitLockerV1Api->bit_locker_v1_get_device_bit_locker_drive_info_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Unique identifier for the device(Required). | 

### Return type

[**DeviceBitLockerDriveV1Model**](DeviceBitLockerDriveV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bit_locker_v1_get_device_bit_locker_protector_info_async**
> DeviceBitLockerProtectorV1Model bit_locker_v1_get_device_bit_locker_protector_info_async(device_uuid, volume_identifier)

Returns the Bit Locker protector information for the device.

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
api_instance = mdmv1.BitLockerV1Api(mdmv1.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Unique identifier for the device(Required).
volume_identifier = 'volume_identifier_example' # str | Drive volume identifier(Required).

try:
    # Returns the Bit Locker protector information for the device.
    api_response = api_instance.bit_locker_v1_get_device_bit_locker_protector_info_async(device_uuid, volume_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitLockerV1Api->bit_locker_v1_get_device_bit_locker_protector_info_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Unique identifier for the device(Required). | 
 **volume_identifier** | **str**| Drive volume identifier(Required). | 

### Return type

[**DeviceBitLockerProtectorV1Model**](DeviceBitLockerProtectorV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

