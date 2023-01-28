# mdmv1.EventLogApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_log_get_event_logs_by_alternate_id**](EventLogApi.md#event_log_get_event_logs_by_alternate_id) | **GET** /devices/eventlog | Retrieves events corresponding to the device identified by alternate Id&#39;s.
[**event_log_get_event_logs_by_device**](EventLogApi.md#event_log_get_event_logs_by_device) | **GET** /devices/{id}/eventlog | Retrieves events corresponding to the device identified by device Id.


# **event_log_get_event_logs_by_alternate_id**
> DeviceEventLogSearchResult event_log_get_event_logs_by_alternate_id(search_by, id, page=page, pagesize=pagesize, severity=severity, dayrange=dayrange)

Retrieves events corresponding to the device identified by alternate Id's.

Event log contains information like the severity, timestamp, source, actual event details and the account corresponding to the event. This API allows searching a device using alternate Id's specified in the searchby parameter.

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
api_instance = mdmv1.EventLogApi(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber] (Required). (default to )
id = '' # str | Device alternate id (Example: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837) (Required). (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximumm records per page. Default 500. (optional)
severity = '' # str | Event severity; possible values: [emergency, alert, critical, error, warning, notice, information, debug]. (optional) (default to )
dayrange = 56 # int | Number of days in the past for which the logs will be fetched (Example: 2). (optional)

try:
    # Retrieves events corresponding to the device identified by alternate Id's.
    api_response = api_instance.event_log_get_event_logs_by_alternate_id(search_by, id, page=page, pagesize=pagesize, severity=severity, dayrange=dayrange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventLogApi->event_log_get_event_logs_by_alternate_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate id type; possible values: [Macaddress, Udid, Serialnumber, ImeiNumber] (Required). | [default to ]
 **id** | **str**| Device alternate id (Example: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837) (Required). | [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximumm records per page. Default 500. | [optional] 
 **severity** | **str**| Event severity; possible values: [emergency, alert, critical, error, warning, notice, information, debug]. | [optional] [default to ]
 **dayrange** | **int**| Number of days in the past for which the logs will be fetched (Example: 2). | [optional] 

### Return type

[**DeviceEventLogSearchResult**](DeviceEventLogSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_log_get_event_logs_by_device**
> DeviceEventLogSearchResult event_log_get_event_logs_by_device(id, page=page, pagesize=pagesize, severity=severity, dayrange=dayrange)

Retrieves events corresponding to the device identified by device Id.

Event log contains information like the severity, timestamp, source, actual event details and the account corresponding to the event.

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
api_instance = mdmv1.EventLogApi(mdmv1.ApiClient(configuration))
id = 56 # int | Device identifier (Example: 3010055).
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximumm records per page. Default 500. (optional)
severity = '' # str | Event severity; possible values: [emergency, alert, critical, error, warning, notice, information, debug]. (optional) (default to )
dayrange = 56 # int | Number of days in the past for which the logs will be fetched (Example: 2). (optional)

try:
    # Retrieves events corresponding to the device identified by device Id.
    api_response = api_instance.event_log_get_event_logs_by_device(id, page=page, pagesize=pagesize, severity=severity, dayrange=dayrange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventLogApi->event_log_get_event_logs_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device identifier (Example: 3010055). | 
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximumm records per page. Default 500. | [optional] 
 **severity** | **str**| Event severity; possible values: [emergency, alert, critical, error, warning, notice, information, debug]. | [optional] [default to ]
 **dayrange** | **int**| Number of days in the past for which the logs will be fetched (Example: 2). | [optional] 

### Return type

[**DeviceEventLogSearchResult**](DeviceEventLogSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

