# systemv1.UsersBatchesV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_batches_v1_batch_import_async_async**](UsersBatchesV1Api.md#users_batches_v1_batch_import_async_async) | **POST** /users/batches | New - Imports users batch.
[**users_batches_v1_generate_report_async**](UsersBatchesV1Api.md#users_batches_v1_generate_report_async) | **POST** /users/batches/report | New - Generate report of users batch details.
[**users_batches_v1_generate_user_batch_details_report_async**](UsersBatchesV1Api.md#users_batches_v1_generate_user_batch_details_report_async) | **POST** /users/batches/{userBatchUuid}/details/report | New - Generate user batch details Report.
[**users_batches_v1_get_users_batch_details_async_async**](UsersBatchesV1Api.md#users_batches_v1_get_users_batch_details_async_async) | **GET** /users/batches/{userBatchUuid}/details | New - List of users batch details.
[**users_batches_v1_get_users_batches_async_async**](UsersBatchesV1Api.md#users_batches_v1_get_users_batches_async_async) | **GET** /users/batches | New - Returns a list of users batches.
[**users_batches_v1_patch_batch_async**](UsersBatchesV1Api.md#users_batches_v1_patch_batch_async) | **PATCH** /users/batches/{user-batch-id} | New - Update Users Batch.


# **users_batches_v1_batch_import_async_async**
> int users_batches_v1_batch_import_async_async(organization_group_uuid, batch_name, batch_description, batch_type=batch_type)

New - Imports users batch.

Imports user batch data.

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
api_instance = systemv1.UsersBatchesV1Api(systemv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group unique identifier.(Required).
batch_name = 'batch_name_example' # str | Name of the batch.(Required).
batch_description = 'batch_description_example' # str | Description of the batch.(Required).
batch_type =  # object | Type of the batch. (optional) (default to )

try:
    # New - Imports users batch.
    api_response = api_instance.users_batches_v1_batch_import_async_async(organization_group_uuid, batch_name, batch_description, batch_type=batch_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersBatchesV1Api->users_batches_v1_batch_import_async_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Organization Group unique identifier.(Required). | 
 **batch_name** | **str**| Name of the batch.(Required). | 
 **batch_description** | **str**| Description of the batch.(Required). | 
 **batch_type** | [**object**](.md)| Type of the batch. | [optional] [default to ]

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_batches_v1_generate_report_async**
> users_batches_v1_generate_report_async(report_parameters)

New - Generate report of users batch details.

Generate report of users batch details based on the parameters.

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
api_instance = systemv1.UsersBatchesV1Api(systemv1.ApiClient(configuration))
report_parameters = systemv1.UsersBatchesReportV1Model() # UsersBatchesReportV1Model | user batch details for report.(Required).

try:
    # New - Generate report of users batch details.
    api_instance.users_batches_v1_generate_report_async(report_parameters)
except ApiException as e:
    print("Exception when calling UsersBatchesV1Api->users_batches_v1_generate_report_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_parameters** | [**UsersBatchesReportV1Model**](UsersBatchesReportV1Model.md)| user batch details for report.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_batches_v1_generate_user_batch_details_report_async**
> users_batches_v1_generate_user_batch_details_report_async(user_batch_uuid, report_parameters)

New - Generate user batch details Report.

Generate report of user batch details based on the parameters.

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
api_instance = systemv1.UsersBatchesV1Api(systemv1.ApiClient(configuration))
user_batch_uuid = 'user_batch_uuid_example' # str | Unique identifier of user batch.(Required).
report_parameters = systemv1.UserBatchDetailsReportV1Model() # UserBatchDetailsReportV1Model | User batch error model.(Required).

try:
    # New - Generate user batch details Report.
    api_instance.users_batches_v1_generate_user_batch_details_report_async(user_batch_uuid, report_parameters)
except ApiException as e:
    print("Exception when calling UsersBatchesV1Api->users_batches_v1_generate_user_batch_details_report_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_batch_uuid** | [**str**](.md)| Unique identifier of user batch.(Required). | 
 **report_parameters** | [**UserBatchDetailsReportV1Model**](UserBatchDetailsReportV1Model.md)| User batch error model.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_batches_v1_get_users_batch_details_async_async**
> UsersBatchDetailsV1ResultModel users_batches_v1_get_users_batch_details_async_async(user_batch_uuid, row_number=row_number, description=description, page=page, page_size=page_size, sort_column=sort_column, sort_order=sort_order)

New - List of users batch details.

Returns a list of users batch details.

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
api_instance = systemv1.UsersBatchesV1Api(systemv1.ApiClient(configuration))
user_batch_uuid = 'user_batch_uuid_example' # str | id of user batch.(Required).
row_number = '' # str | Filter records based on row number. (optional) (default to )
description = '' # str | Filter records based on description. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
page_size = 56 # int | Maximum records per page. Default 500. (optional)
sort_column =  # object | Column based on which we can provide the sorting. (optional) (default to )
sort_order =  # object | The order based which on we can sort. Default value is ASC. (optional) (default to )

try:
    # New - List of users batch details.
    api_response = api_instance.users_batches_v1_get_users_batch_details_async_async(user_batch_uuid, row_number=row_number, description=description, page=page, page_size=page_size, sort_column=sort_column, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersBatchesV1Api->users_batches_v1_get_users_batch_details_async_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_batch_uuid** | [**str**](.md)| id of user batch.(Required). | 
 **row_number** | **str**| Filter records based on row number. | [optional] [default to ]
 **description** | **str**| Filter records based on description. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **page_size** | **int**| Maximum records per page. Default 500. | [optional] 
 **sort_column** | [**object**](.md)| Column based on which we can provide the sorting. | [optional] [default to ]
 **sort_order** | [**object**](.md)| The order based which on we can sort. Default value is ASC. | [optional] [default to ]

### Return type

[**UsersBatchDetailsV1ResultModel**](UsersBatchDetailsV1ResultModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_batches_v1_get_users_batches_async_async**
> UsersBatchesV1ResultModel users_batches_v1_get_users_batches_async_async(organization_group_uuid, batch_name=batch_name, batch_description=batch_description, page=page, page_size=page_size, sort_column=sort_column, sort_order=sort_order)

New - Returns a list of users batches.

Returns a list of users batches satisfying the search criteria.

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
api_instance = systemv1.UsersBatchesV1Api(systemv1.ApiClient(configuration))
organization_group_uuid =  # object | Uuid of the Organization group to fetch the user batches for.(Required) (default to )
batch_name = '' # str | Filter records based on batch name. (optional) (default to )
batch_description = '' # str | Filter records based on batch description. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
page_size = 56 # int | Maximum records per page. Default 500. (optional)
sort_column =  # object | Column based on which we can provide the sorting. (optional) (default to )
sort_order =  # object | The order based which on we can sort. Default value is ASC. (optional) (default to )

try:
    # New - Returns a list of users batches.
    api_response = api_instance.users_batches_v1_get_users_batches_async_async(organization_group_uuid, batch_name=batch_name, batch_description=batch_description, page=page, page_size=page_size, sort_column=sort_column, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersBatchesV1Api->users_batches_v1_get_users_batches_async_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**object**](.md)| Uuid of the Organization group to fetch the user batches for.(Required) | [default to ]
 **batch_name** | **str**| Filter records based on batch name. | [optional] [default to ]
 **batch_description** | **str**| Filter records based on batch description. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **page_size** | **int**| Maximum records per page. Default 500. | [optional] 
 **sort_column** | [**object**](.md)| Column based on which we can provide the sorting. | [optional] [default to ]
 **sort_order** | [**object**](.md)| The order based which on we can sort. Default value is ASC. | [optional] [default to ]

### Return type

[**UsersBatchesV1ResultModel**](UsersBatchesV1ResultModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_batches_v1_patch_batch_async**
> users_batches_v1_patch_batch_async(user_batch_id, users_model, user_batch_id2)

New - Update Users Batch.

Update Users Batch resource.

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
api_instance = systemv1.UsersBatchesV1Api(systemv1.ApiClient(configuration))
user_batch_id = 'user_batch_id_example' # str | User batch ID(Required).
users_model = systemv1.UsersBatchesV1Model() # UsersBatchesV1Model | Configuration request model(Required).
user_batch_id2 = 'user_batch_id_example' # str | 

try:
    # New - Update Users Batch.
    api_instance.users_batches_v1_patch_batch_async(user_batch_id, users_model, user_batch_id2)
except ApiException as e:
    print("Exception when calling UsersBatchesV1Api->users_batches_v1_patch_batch_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_batch_id** | **str**| User batch ID(Required). | 
 **users_model** | [**UsersBatchesV1Model**](UsersBatchesV1Model.md)| Configuration request model(Required). | 
 **user_batch_id2** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

