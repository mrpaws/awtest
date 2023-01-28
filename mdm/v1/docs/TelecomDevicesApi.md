# mdmv1.TelecomDevicesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**telecom_devices_search_cell_card_daily_usage_history_by_device_async**](TelecomDevicesApi.md#telecom_devices_search_cell_card_daily_usage_history_by_device_async) | **GET** /telecom/devices/usagehistory | Searches for telecom device usage history by device using the query information provided.
[**telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async**](TelecomDevicesApi.md#telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async) | **GET** /telecom/devices/bulkusagehistory | Searches for telecom device usage history in bulk by Organization Group using the query information provided.


# **telecom_devices_search_cell_card_daily_usage_history_by_device_async**
> CellCardDailyUsagePagedSearchResultModel telecom_devices_search_cell_card_daily_usage_history_by_device_async(organizationgroupid=organizationgroupid, search_by=search_by, id=id, phonenumber=phonenumber, startdate=startdate, enddate=enddate, page=page, pagesize=pagesize, orderby=orderby, sortorder=sortorder)

Searches for telecom device usage history by device using the query information provided.

Searches for telecom device usage history based on the Organization Group ID, Alternate Id, Phone Number, Start Date, End Date.  <br />  *startdate and enddate* fields accept the following  Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.TelecomDevicesApi(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization Group ID. (optional)
search_by = '' # str | The Alternate ID type; possible values: [Macaddress, UdId, Serialnumber, ImeiNumber, EasId, DeviceId].(Formats: Macaddress: 848506B900BA, UdId: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 499NCV2JH55N5CUTR2D27GG42, DeviceId: 12345). (optional) (default to )
id = 56 # int | Device Alternate ID. (optional)
phonenumber = '' # str | Search by device phone number. (optional) (default to )
startdate = '' # datetime | Search by start date. (optional) (default to )
enddate = '' # datetime | Search by end date. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)
orderby = '' # str | Orderby column name. (optional) (default to )
sortorder = '' # str | Sorting order. Values ASC or DESC. Defaults to ASC. (optional) (default to )

try:
    # Searches for telecom device usage history by device using the query information provided.
    api_response = api_instance.telecom_devices_search_cell_card_daily_usage_history_by_device_async(organizationgroupid=organizationgroupid, search_by=search_by, id=id, phonenumber=phonenumber, startdate=startdate, enddate=enddate, page=page, pagesize=pagesize, orderby=orderby, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelecomDevicesApi->telecom_devices_search_cell_card_daily_usage_history_by_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization Group ID. | [optional] 
 **search_by** | **str**| The Alternate ID type; possible values: [Macaddress, UdId, Serialnumber, ImeiNumber, EasId, DeviceId].(Formats: Macaddress: 848506B900BA, UdId: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 499NCV2JH55N5CUTR2D27GG42, DeviceId: 12345). | [optional] [default to ]
 **id** | **int**| Device Alternate ID. | [optional] 
 **phonenumber** | **str**| Search by device phone number. | [optional] [default to ]
 **startdate** | **datetime**| Search by start date. | [optional] [default to ]
 **enddate** | **datetime**| Search by end date. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 
 **orderby** | **str**| Orderby column name. | [optional] [default to ]
 **sortorder** | **str**| Sorting order. Values ASC or DESC. Defaults to ASC. | [optional] [default to ]

### Return type

[**CellCardDailyUsagePagedSearchResultModel**](CellCardDailyUsagePagedSearchResultModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async**
> CellCardDailyUsagePagedSearchResultModel telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async(organizationgroupid=organizationgroupid, _date=_date, page=page, pagesize=pagesize, orderby=orderby, sortorder=sortorder)

Searches for telecom device usage history in bulk by Organization Group using the query information provided.

Searches for telecom device usage history in bulk based on the Organization Group ID and Date.  <br />  date* field accepts the following  Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.TelecomDevicesApi(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Search by Organization Group ID. (optional)
_date =  # object | Search by date, if not provided current UTC date will be considered. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)
orderby = '' # str | Orderby column name. (optional) (default to )
sortorder = '' # str | Sorting order. Values ASC or DESC. Defaults to ASC. (optional) (default to )

try:
    # Searches for telecom device usage history in bulk by Organization Group using the query information provided.
    api_response = api_instance.telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async(organizationgroupid=organizationgroupid, _date=_date, page=page, pagesize=pagesize, orderby=orderby, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelecomDevicesApi->telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Search by Organization Group ID. | [optional] 
 **_date** | [**object**](.md)| Search by date, if not provided current UTC date will be considered. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 
 **orderby** | **str**| Orderby column name. | [optional] [default to ]
 **sortorder** | **str**| Sorting order. Values ASC or DESC. Defaults to ASC. | [optional] [default to ]

### Return type

[**CellCardDailyUsagePagedSearchResultModel**](CellCardDailyUsagePagedSearchResultModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

