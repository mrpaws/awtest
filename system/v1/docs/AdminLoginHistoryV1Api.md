# systemv1.AdminLoginHistoryV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_login_history_v1_generate_login_history_report_async**](AdminLoginHistoryV1Api.md#admin_login_history_v1_generate_login_history_report_async) | **POST** /admins/login-history/report | New - Generate Login History Report.
[**admin_login_history_v1_get_admin_login_history_async**](AdminLoginHistoryV1Api.md#admin_login_history_v1_get_admin_login_history_async) | **POST** /admins/login-history/search | New - Returns a list of admin login history records.


# **admin_login_history_v1_generate_login_history_report_async**
> admin_login_history_v1_generate_login_history_report_async(search_criteria)

New - Generate Login History Report.

Generate report of Login history based on the parameters.

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
api_instance = systemv1.AdminLoginHistoryV1Api(systemv1.ApiClient(configuration))
search_criteria = systemv1.AdminLoginHistoryReportV1Model() # AdminLoginHistoryReportV1Model | Admin login history search criteria(Required).

try:
    # New - Generate Login History Report.
    api_instance.admin_login_history_v1_generate_login_history_report_async(search_criteria)
except ApiException as e:
    print("Exception when calling AdminLoginHistoryV1Api->admin_login_history_v1_generate_login_history_report_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_criteria** | [**AdminLoginHistoryReportV1Model**](AdminLoginHistoryReportV1Model.md)| Admin login history search criteria(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_login_history_v1_get_admin_login_history_async**
> AdminLoginHistoryResponse admin_login_history_v1_get_admin_login_history_async(search_criteria)

New - Returns a list of admin login history records.

Returns a list of admin login history records satisfying the search criteria.

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
api_instance = systemv1.AdminLoginHistoryV1Api(systemv1.ApiClient(configuration))
search_criteria = systemv1.AdminLoginHistorySearchCriteria() # AdminLoginHistorySearchCriteria | Admin login history search criteria(Required).

try:
    # New - Returns a list of admin login history records.
    api_response = api_instance.admin_login_history_v1_get_admin_login_history_async(search_criteria)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminLoginHistoryV1Api->admin_login_history_v1_get_admin_login_history_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_criteria** | [**AdminLoginHistorySearchCriteria**](AdminLoginHistorySearchCriteria.md)| Admin login history search criteria(Required). | 

### Return type

[**AdminLoginHistoryResponse**](AdminLoginHistoryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

