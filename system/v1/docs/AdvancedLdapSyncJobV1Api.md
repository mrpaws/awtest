# systemv1.AdvancedLdapSyncJobV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advanced_ldap_sync_job_v1_advanced_ldap_sync_job_details_async**](AdvancedLdapSyncJobV1Api.md#advanced_ldap_sync_job_v1_advanced_ldap_sync_job_details_async) | **GET** /advanced-ldap-sync-jobs | New - Gets Advanced Ldap Sync job details for a particular Organization group. Allows admins to preview the all the job details for a specific OG.
[**advanced_ldap_sync_job_v1_approve_or_decline_advanced_ldap_sync_job_async**](AdvancedLdapSyncJobV1Api.md#advanced_ldap_sync_job_v1_approve_or_decline_advanced_ldap_sync_job_async) | **POST** /advanced-ldap-sync-jobs/{uuid} | New - Approves or declines the created LDAP sync job.
[**advanced_ldap_sync_job_v1_create_advanced_ldap_sync_job_async**](AdvancedLdapSyncJobV1Api.md#advanced_ldap_sync_job_v1_create_advanced_ldap_sync_job_async) | **POST** /advanced-ldap-sync-jobs | New - Creates a new LDAP sync job.
[**advanced_ldap_sync_job_v1_get_job_status_async**](AdvancedLdapSyncJobV1Api.md#advanced_ldap_sync_job_v1_get_job_status_async) | **GET** /advanced-ldap-sync-jobs/status/{uuid} | New - Gets LDAP sync job details.
[**advanced_ldap_sync_job_v1_preview_advanced_ldap_sync_job_async**](AdvancedLdapSyncJobV1Api.md#advanced_ldap_sync_job_v1_preview_advanced_ldap_sync_job_async) | **GET** /advanced-ldap-sync-jobs/{uuid} | New - Gets LDAP sync job details. Allows admins to preview the changes to enrollment user attributes.


# **advanced_ldap_sync_job_v1_advanced_ldap_sync_job_details_async**
> AdvancedLdapSyncJobDetailsResponseModel advanced_ldap_sync_job_v1_advanced_ldap_sync_job_details_async(organization_group_uuid, page_number=page_number, page_size=page_size, status_filter=status_filter, search_text=search_text, sort_column=sort_column, sort_order=sort_order)

New - Gets Advanced Ldap Sync job details for a particular Organization group. Allows admins to preview the all the job details for a specific OG.

Preview details of all the advanced LDAP sync job including the job status, enrollment user attributes etc. for a particular OG.

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
api_instance = systemv1.AdvancedLdapSyncJobV1Api(systemv1.ApiClient(configuration))
organization_group_uuid =  # object | The unique id of the organization group.(Required) (default to )
page_number = 56 # int | Page number. (optional)
page_size = 56 # int | Page size. Default/Maximum is 500. (optional)
status_filter = 56 # int | Filters records based on the Job Status. Valid Status 1-10. (optional)
search_text = '' # str | Filters records based on the search text. (optional) (default to )
sort_column =  # object | Column based on which we can provide the sorting. Default JOB_ID. (optional) (default to )
sort_order =  # object | The order based which on we can sort. Default value is ASC. (optional) (default to )

try:
    # New - Gets Advanced Ldap Sync job details for a particular Organization group. Allows admins to preview the all the job details for a specific OG.
    api_response = api_instance.advanced_ldap_sync_job_v1_advanced_ldap_sync_job_details_async(organization_group_uuid, page_number=page_number, page_size=page_size, status_filter=status_filter, search_text=search_text, sort_column=sort_column, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedLdapSyncJobV1Api->advanced_ldap_sync_job_v1_advanced_ldap_sync_job_details_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**object**](.md)| The unique id of the organization group.(Required) | [default to ]
 **page_number** | **int**| Page number. | [optional] 
 **page_size** | **int**| Page size. Default/Maximum is 500. | [optional] 
 **status_filter** | **int**| Filters records based on the Job Status. Valid Status 1-10. | [optional] 
 **search_text** | **str**| Filters records based on the search text. | [optional] [default to ]
 **sort_column** | [**object**](.md)| Column based on which we can provide the sorting. Default JOB_ID. | [optional] [default to ]
 **sort_order** | [**object**](.md)| The order based which on we can sort. Default value is ASC. | [optional] [default to ]

### Return type

[**AdvancedLdapSyncJobDetailsResponseModel**](AdvancedLdapSyncJobDetailsResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **advanced_ldap_sync_job_v1_approve_or_decline_advanced_ldap_sync_job_async**
> advanced_ldap_sync_job_v1_approve_or_decline_advanced_ldap_sync_job_async(uuid, advanced_ldap_sync_job_approval_request, action)

New - Approves or declines the created LDAP sync job.

Functionality to approve or decline the created advanced LDAP sysnc job.

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
api_instance = systemv1.AdvancedLdapSyncJobV1Api(systemv1.ApiClient(configuration))
uuid = 'uuid_example' # str | The unique id of the advanced ldap sync job created.(Required).
advanced_ldap_sync_job_approval_request = systemv1.AdvancedLadpSyncJobApprovalRequestModel() # AdvancedLadpSyncJobApprovalRequestModel | Advanced ladp sync job approval request model.(Required).
action =  # object | The approval action.(Required) (default to )

try:
    # New - Approves or declines the created LDAP sync job.
    api_instance.advanced_ldap_sync_job_v1_approve_or_decline_advanced_ldap_sync_job_async(uuid, advanced_ldap_sync_job_approval_request, action)
except ApiException as e:
    print("Exception when calling AdvancedLdapSyncJobV1Api->advanced_ldap_sync_job_v1_approve_or_decline_advanced_ldap_sync_job_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The unique id of the advanced ldap sync job created.(Required). | 
 **advanced_ldap_sync_job_approval_request** | [**AdvancedLadpSyncJobApprovalRequestModel**](AdvancedLadpSyncJobApprovalRequestModel.md)| Advanced ladp sync job approval request model.(Required). | 
 **action** | [**object**](.md)| The approval action.(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **advanced_ldap_sync_job_v1_create_advanced_ldap_sync_job_async**
> AdvancedLdapSyncJobResponseModel advanced_ldap_sync_job_v1_create_advanced_ldap_sync_job_async(advanced_ldap_sync_job_request)

New - Creates a new LDAP sync job.

Creates the advanced ldap sync job. Queues a message in MSMQ for the Directory Sync Services to pick up and process.

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
api_instance = systemv1.AdvancedLdapSyncJobV1Api(systemv1.ApiClient(configuration))
advanced_ldap_sync_job_request = systemv1.AdvancedLadpSyncJobRequestModel() # AdvancedLadpSyncJobRequestModel | Request model to create new ldap sync job.(Required).

try:
    # New - Creates a new LDAP sync job.
    api_response = api_instance.advanced_ldap_sync_job_v1_create_advanced_ldap_sync_job_async(advanced_ldap_sync_job_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedLdapSyncJobV1Api->advanced_ldap_sync_job_v1_create_advanced_ldap_sync_job_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advanced_ldap_sync_job_request** | [**AdvancedLadpSyncJobRequestModel**](AdvancedLadpSyncJobRequestModel.md)| Request model to create new ldap sync job.(Required). | 

### Return type

[**AdvancedLdapSyncJobResponseModel**](AdvancedLdapSyncJobResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **advanced_ldap_sync_job_v1_get_job_status_async**
> AdvancedLdapSyncJobProgressResponseModel advanced_ldap_sync_job_v1_get_job_status_async(uuid)

New - Gets LDAP sync job details.

Get details of the advanced LDAP job including the job ID, job progress attributes etc.

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
api_instance = systemv1.AdvancedLdapSyncJobV1Api(systemv1.ApiClient(configuration))
uuid = 'uuid_example' # str | The unique id of the advanced ldap sync job.(Required).

try:
    # New - Gets LDAP sync job details.
    api_response = api_instance.advanced_ldap_sync_job_v1_get_job_status_async(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedLdapSyncJobV1Api->advanced_ldap_sync_job_v1_get_job_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The unique id of the advanced ldap sync job.(Required). | 

### Return type

[**AdvancedLdapSyncJobProgressResponseModel**](AdvancedLdapSyncJobProgressResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **advanced_ldap_sync_job_v1_preview_advanced_ldap_sync_job_async**
> PreviewAdvancedLdapSyncJobResponseModel advanced_ldap_sync_job_v1_preview_advanced_ldap_sync_job_async(uuid, page_number=page_number, page_size=page_size, search_text=search_text, sort_column=sort_column, sort_order=sort_order)

New - Gets LDAP sync job details. Allows admins to preview the changes to enrollment user attributes.

Preview details of the advanced LDAP sync job including the job status, enrollment user attributes etc.

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
api_instance = systemv1.AdvancedLdapSyncJobV1Api(systemv1.ApiClient(configuration))
uuid = 'uuid_example' # str | The unique id of the created advanced ldap sync job.(Required).
page_number = 56 # int | Page number. (optional)
page_size = 56 # int | Page size. Default/Maximum is 500. (optional)
search_text = '' # str | Filters records based on the search text. (optional) (default to )
sort_column =  # object | Column based on which we can provide the sorting. Default JOB_ID. (optional) (default to )
sort_order =  # object | The order based which on we can sort. Default value is ASC. (optional) (default to )

try:
    # New - Gets LDAP sync job details. Allows admins to preview the changes to enrollment user attributes.
    api_response = api_instance.advanced_ldap_sync_job_v1_preview_advanced_ldap_sync_job_async(uuid, page_number=page_number, page_size=page_size, search_text=search_text, sort_column=sort_column, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedLdapSyncJobV1Api->advanced_ldap_sync_job_v1_preview_advanced_ldap_sync_job_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The unique id of the created advanced ldap sync job.(Required). | 
 **page_number** | **int**| Page number. | [optional] 
 **page_size** | **int**| Page size. Default/Maximum is 500. | [optional] 
 **search_text** | **str**| Filters records based on the search text. | [optional] [default to ]
 **sort_column** | [**object**](.md)| Column based on which we can provide the sorting. Default JOB_ID. | [optional] [default to ]
 **sort_order** | [**object**](.md)| The order based which on we can sort. Default value is ASC. | [optional] [default to ]

### Return type

[**PreviewAdvancedLdapSyncJobResponseModel**](PreviewAdvancedLdapSyncJobResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

