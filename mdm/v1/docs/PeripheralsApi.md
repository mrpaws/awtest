# mdmv1.PeripheralsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peripherals_get_printer_by_id_async**](PeripheralsApi.md#peripherals_get_printer_by_id_async) | **GET** /peripherals/printer/{deviceID} | Gets the printer by identifier.
[**peripherals_get_printer_by_location_group_id_async**](PeripheralsApi.md#peripherals_get_printer_by_location_group_id_async) | **GET** /peripherals/printers/{organizationGroupID} | Gets the printer by organization group identifier.


# **peripherals_get_printer_by_id_async**
> Printer peripherals_get_printer_by_id_async(device_id)

Gets the printer by identifier.

Gets the printer properties by printer identifier.

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
api_instance = mdmv1.PeripheralsApi(mdmv1.ApiClient(configuration))
device_id = 56 # int | The device identifier. (Required).

try:
    # Gets the printer by identifier.
    api_response = api_instance.peripherals_get_printer_by_id_async(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeripheralsApi->peripherals_get_printer_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The device identifier. (Required). | 

### Return type

[**Printer**](Printer.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peripherals_get_printer_by_location_group_id_async**
> list[Printer] peripherals_get_printer_by_location_group_id_async(organization_group_id)

Gets the printer by organization group identifier.

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
api_instance = mdmv1.PeripheralsApi(mdmv1.ApiClient(configuration))
organization_group_id = 56 # int | The organization group identifier. (Required).

try:
    # Gets the printer by organization group identifier.
    api_response = api_instance.peripherals_get_printer_by_location_group_id_async(organization_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeripheralsApi->peripherals_get_printer_by_location_group_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_id** | **int**| The organization group identifier. (Required). | 

### Return type

[**list[Printer]**](Printer.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

