# mdmv1.ComplianceV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compliance_v1_get_compliance_by_alternate_id_async**](ComplianceV1Api.md#compliance_v1_get_compliance_by_alternate_id_async) | **GET** /devices/compliance | Retrieves compliance details of the device identified by the alternate id.
[**compliance_v1_get_compliance_by_device_async**](ComplianceV1Api.md#compliance_v1_get_compliance_by_device_async) | **GET** /devices/{deviceId}/compliance | Retrieves compliance details of the device identified by device ID.


# **compliance_v1_get_compliance_by_alternate_id_async**
> DeviceComplianceSearchResult compliance_v1_get_compliance_by_alternate_id_async(search_by, id, page=page, pagesize=pagesize)

Retrieves compliance details of the device identified by the alternate id.

Processes the alternate ID for the device to get compliance details of this specific device. It also facilitates to search by different types of alternate IDs.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

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
api_instance = mdmv1.ComplianceV1Api(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber] (Required). (default to )
id = '' # str | Device alternate id (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837) (Required). (default to )
page = 56 # int | The specific page number to get. (optional)
pagesize = 56 # int | Max records per page. (optional)

try:
    # Retrieves compliance details of the device identified by the alternate id.
    api_response = api_instance.compliance_v1_get_compliance_by_alternate_id_async(search_by, id, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceV1Api->compliance_v1_get_compliance_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber] (Required). | [default to ]
 **id** | **str**| Device alternate id (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837) (Required). | [default to ]
 **page** | **int**| The specific page number to get. | [optional] 
 **pagesize** | **int**| Max records per page. | [optional] 

### Return type

[**DeviceComplianceSearchResult**](DeviceComplianceSearchResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_v1_get_compliance_by_device_async**
> DeviceComplianceSearchResultModel compliance_v1_get_compliance_by_device_async(device_id, page=page, pagesize=pagesize)

Retrieves compliance details of the device identified by device ID.

Processes the device ID to get compliance policy details for specified device. It also checks if device is compromised or not.

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
api_instance = mdmv1.ComplianceV1Api(mdmv1.ApiClient(configuration))
device_id = 56 # int | Identifier of the device(Required).
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Retrieves compliance details of the device identified by device ID.
    api_response = api_instance.compliance_v1_get_compliance_by_device_async(device_id, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceV1Api->compliance_v1_get_compliance_by_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Identifier of the device(Required). | 
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**DeviceComplianceSearchResultModel**](DeviceComplianceSearchResultModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

