# systemv1.ExportedReportsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exported_reports_v1_create_report_async**](ExportedReportsV1Api.md#exported_reports_v1_create_report_async) | **POST** /groups/{organizationGroupUuid}/exported-reports | New - Submit a bulk export job matching specified criteria.
[**exported_reports_v1_get_all_exported_reports_async**](ExportedReportsV1Api.md#exported_reports_v1_get_all_exported_reports_async) | **GET** /groups/{organizationGroupUuid}/exported-reports | New - Get List of all exported reports by admin.
[**exported_reports_v1_get_report_status_async**](ExportedReportsV1Api.md#exported_reports_v1_get_report_status_async) | **GET** /groups/{organizationGroupUuid}/exported-reports/{reportUuid} | New - Get report status.


# **exported_reports_v1_create_report_async**
> exported_reports_v1_create_report_async(organization_group_uuid, report_parameters)

New - Submit a bulk export job matching specified criteria.



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
api_instance = systemv1.ExportedReportsV1Api(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group UUID.(Required).
report_parameters = systemv1.ReportParametersV1() # ReportParametersV1 | Report Parameters(Required).

try:
    # New - Submit a bulk export job matching specified criteria.
    api_instance.exported_reports_v1_create_report_async(organization_group_uuid, report_parameters)
except ApiException as e:
    print("Exception when calling ExportedReportsV1Api->exported_reports_v1_create_report_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Organization Group UUID.(Required). | 
 **report_parameters** | [**ReportParametersV1**](ReportParametersV1.md)| Report Parameters(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exported_reports_v1_get_all_exported_reports_async**
> list[ReportsModel] exported_reports_v1_get_all_exported_reports_async(organization_group_uuid, export_type, search=search, created_start_date=created_start_date, created_end_date=created_end_date, sort_column=sort_column, page=page, page_size=page_size, sort_order=sort_order)

New - Get List of all exported reports by admin.

Get List of all exported reports by admin for each organization group .

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
api_instance = systemv1.ExportedReportsV1Api(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group UUID.(Required).
export_type =  # object | The export type which the results will be filtered by.(Required) (default to )
search = '' # str | The text to search for in the name and description for exports. (optional) (default to )
created_start_date = '' # datetime | The start of the created date range in UTC by which the results will be filtered. Format of the date is YYYY-MM-DD. (optional) (default to )
created_end_date = '' # datetime | The end of the created date range in UTC by which the results will be filtered. Format of the date is YYYY-MM-DD. (optional) (default to )
sort_column =  # object | Order the results by this attribute, default value can be Time Exported. (optional) (default to )
page = 56 # int | The specific page number to get. (optional)
page_size = 56 # int | Maximum records per page, default value is 20 (optional)
sort_order =  # object | The sort order by direction. (optional) (default to )

try:
    # New - Get List of all exported reports by admin.
    api_response = api_instance.exported_reports_v1_get_all_exported_reports_async(organization_group_uuid, export_type, search=search, created_start_date=created_start_date, created_end_date=created_end_date, sort_column=sort_column, page=page, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportedReportsV1Api->exported_reports_v1_get_all_exported_reports_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Organization Group UUID.(Required). | 
 **export_type** | [**object**](.md)| The export type which the results will be filtered by.(Required) | [default to ]
 **search** | **str**| The text to search for in the name and description for exports. | [optional] [default to ]
 **created_start_date** | **datetime**| The start of the created date range in UTC by which the results will be filtered. Format of the date is YYYY-MM-DD. | [optional] [default to ]
 **created_end_date** | **datetime**| The end of the created date range in UTC by which the results will be filtered. Format of the date is YYYY-MM-DD. | [optional] [default to ]
 **sort_column** | [**object**](.md)| Order the results by this attribute, default value can be Time Exported. | [optional] [default to ]
 **page** | **int**| The specific page number to get. | [optional] 
 **page_size** | **int**| Maximum records per page, default value is 20 | [optional] 
 **sort_order** | [**object**](.md)| The sort order by direction. | [optional] [default to ]

### Return type

[**list[ReportsModel]**](ReportsModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exported_reports_v1_get_report_status_async**
> ExportStatusModelV1 exported_reports_v1_get_report_status_async(organization_group_uuid, report_uuid)

New - Get report status.

Get status of exported report.

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
api_instance = systemv1.ExportedReportsV1Api(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group UUID.(Required).
report_uuid = 'report_uuid_example' # str | Report UUID.(Required).

try:
    # New - Get report status.
    api_response = api_instance.exported_reports_v1_get_report_status_async(organization_group_uuid, report_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportedReportsV1Api->exported_reports_v1_get_report_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Organization Group UUID.(Required). | 
 **report_uuid** | [**str**](.md)| Report UUID.(Required). | 

### Return type

[**ExportStatusModelV1**](ExportStatusModelV1.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

