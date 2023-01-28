# mdmv1.ProductComponentsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_components_v1_condition_search**](ProductComponentsV1Api.md#product_components_v1_condition_search) | **GET** /products/conditionsearch | New - Returns available conditions for the Organization Group
[**product_components_v1_devices_processed_pe_async**](ProductComponentsV1Api.md#product_components_v1_devices_processed_pe_async) | **GET** /products/DevicesProcessedPE | Report back device counts pertaining to the policy engine.
[**product_components_v1_file_condition_search**](ProductComponentsV1Api.md#product_components_v1_file_condition_search) | **GET** /products/fileconditionsearch | New - Search for file conditions with the specified parameters.
[**product_components_v1_get_events_actions_list**](ProductComponentsV1Api.md#product_components_v1_get_events_actions_list) | **GET** /products/eventactionslist | Retrieves paginated lists of events actions for the specified organization group and page size.
[**product_components_v1_get_file_actions_by_product_id**](ProductComponentsV1Api.md#product_components_v1_get_file_actions_by_product_id) | **GET** /products/{id}/fileactions | Get specified Product file actions by Product Id.
[**product_components_v1_get_profile_by_product_id_async**](ProductComponentsV1Api.md#product_components_v1_get_profile_by_product_id_async) | **GET** /products/{id}/profiles | Returns the list of Profiles which are assigned to the passed Product ID.
[**product_components_v1_get_time_condition_by_product_id**](ProductComponentsV1Api.md#product_components_v1_get_time_condition_by_product_id) | **GET** /products/{id}/timesconditions | Get specified Product time conditions by Product Id.
[**product_components_v1_maintain_condition**](ProductComponentsV1Api.md#product_components_v1_maintain_condition) | **POST** /products/maintainCondition | Creates  or updates a condition.
[**product_components_v1_maintain_event_action**](ProductComponentsV1Api.md#product_components_v1_maintain_event_action) | **POST** /products/maintainEventAction | Create or update an Event/Action.
[**product_components_v1_maintain_file_action**](ProductComponentsV1Api.md#product_components_v1_maintain_file_action) | **POST** /products/maintainFileAction | Creates or updates a file action.
[**product_components_v1_provisioning_queue_counts_async**](ProductComponentsV1Api.md#product_components_v1_provisioning_queue_counts_async) | **GET** /products/{id}/provisioningqueuecounts | Report back queue counts pertaining to the policy engine.
[**product_components_v1_retrieve_product_download_and_install_statistics**](ProductComponentsV1Api.md#product_components_v1_retrieve_product_download_and_install_statistics) | **GET** /products/productdownloadandinstallstatistics | Retrieves the product installation and download statistics.
[**product_components_v1_search_files_actions**](ProductComponentsV1Api.md#product_components_v1_search_files_actions) | **GET** /products/filesactionssearch | Searches for the Files/Actions with the search parameters passed.
[**product_components_v1_time_condition_search**](ProductComponentsV1Api.md#product_components_v1_time_condition_search) | **GET** /products/timeconditionsearch | New - Search for Time Conditions with the specified parameters.


# **product_components_v1_condition_search**
> list[ProductCondition] product_components_v1_condition_search(organizationgroupid=organizationgroupid, page=page, pagesize=pagesize)

New - Returns available conditions for the Organization Group

Retrieves conditions available for the specified Organization Group

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group identifier (optional)
page = 56 # int | Specific page number to get. 0 based index (optional)
pagesize = 56 # int | Maximum records per page. Default 500 (optional)

try:
    # New - Returns available conditions for the Organization Group
    api_response = api_instance.product_components_v1_condition_search(organizationgroupid=organizationgroupid, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_condition_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group identifier | [optional] 
 **page** | **int**| Specific page number to get. 0 based index | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500 | [optional] 

### Return type

[**list[ProductCondition]**](ProductCondition.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_devices_processed_pe_async**
> DevicesProcessedPE product_components_v1_devices_processed_pe_async(organizationgroupid=organizationgroupid, starttime=starttime, endtime=endtime)

Report back device counts pertaining to the policy engine.

Report back device counts pertaining to the policy engine when Organization group ID, Start and End time are passed.  The parameters starttime and endtime accepts the below DateTime formats :  <br>yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff, yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff,</br>  yyyy/MM/ddTHH:mm:ss.fff, yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group ID. (optional)
starttime = '' # datetime | DateTime, Filters the result where modified date is greater than or equal to starttime value. (optional) (default to )
endtime = '' # datetime | DateTime, Filters the result where  modified date is lesser than or equal to endtime value. (optional) (default to )

try:
    # Report back device counts pertaining to the policy engine.
    api_response = api_instance.product_components_v1_devices_processed_pe_async(organizationgroupid=organizationgroupid, starttime=starttime, endtime=endtime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_devices_processed_pe_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group ID. | [optional] 
 **starttime** | **datetime**| DateTime, Filters the result where modified date is greater than or equal to starttime value. | [optional] [default to ]
 **endtime** | **datetime**| DateTime, Filters the result where  modified date is lesser than or equal to endtime value. | [optional] [default to ]

### Return type

[**DevicesProcessedPE**](DevicesProcessedPE.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_file_condition_search**
> list[FileCondtion] product_components_v1_file_condition_search(organizationgroupid=organizationgroupid, starttime=starttime, endtime=endtime)

New - Search for file conditions with the specified parameters.

Search for file conditions with the specified parameters such as organization group id, start time and end time value.  The parameters starttime and endtime accepts the below DateTime formats :  yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,   yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff,  yyyy/MM/ddTHH:mm:ss.fff, yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff,   MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group identifier (optional)
starttime = '' # str | DateTime, Filters the result where FileCondition modified date is greater than or equal to starttime value (optional) (default to )
endtime = '' # str | DateTime, Filters the result where FileCondition modified date is lesser than or equal to endtime value (optional) (default to )

try:
    # New - Search for file conditions with the specified parameters.
    api_response = api_instance.product_components_v1_file_condition_search(organizationgroupid=organizationgroupid, starttime=starttime, endtime=endtime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_file_condition_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group identifier | [optional] 
 **starttime** | **str**| DateTime, Filters the result where FileCondition modified date is greater than or equal to starttime value | [optional] [default to ]
 **endtime** | **str**| DateTime, Filters the result where FileCondition modified date is lesser than or equal to endtime value | [optional] [default to ]

### Return type

[**list[FileCondtion]**](FileCondtion.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_get_events_actions_list**
> EventActionsListResult product_components_v1_get_events_actions_list(organizationgroupid=organizationgroupid, page=page, pagesize=pagesize)

Retrieves paginated lists of events actions for the specified organization group and page size.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group identifier. (optional)
page = 56 # int | Specific page number to get in the resulting list. (optional)
pagesize = 56 # int | Maximum records per page. The default value is 500. (optional)

try:
    # Retrieves paginated lists of events actions for the specified organization group and page size.
    api_response = api_instance.product_components_v1_get_events_actions_list(organizationgroupid=organizationgroupid, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_get_events_actions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group identifier. | [optional] 
 **page** | **int**| Specific page number to get in the resulting list. | [optional] 
 **pagesize** | **int**| Maximum records per page. The default value is 500. | [optional] 

### Return type

[**EventActionsListResult**](EventActionsListResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_get_file_actions_by_product_id**
> ProductFileActions product_components_v1_get_file_actions_by_product_id(id)

Get specified Product file actions by Product Id.

Retrieves specified product file actions when Product ID is specified.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Identifier of the Product. (Required).

try:
    # Get specified Product file actions by Product Id.
    api_response = api_instance.product_components_v1_get_file_actions_by_product_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_get_file_actions_by_product_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of the Product. (Required). | 

### Return type

[**ProductFileActions**](ProductFileActions.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_get_profile_by_product_id_async**
> DevicePolicyProfiles product_components_v1_get_profile_by_product_id_async(id)

Returns the list of Profiles which are assigned to the passed Product ID.

Returns the list of Profiles when Product ID is passed.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Identifier of the Product. (Required).

try:
    # Returns the list of Profiles which are assigned to the passed Product ID.
    api_response = api_instance.product_components_v1_get_profile_by_product_id_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_get_profile_by_product_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of the Product. (Required). | 

### Return type

[**DevicePolicyProfiles**](DevicePolicyProfiles.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_get_time_condition_by_product_id**
> ProductTimeCondition product_components_v1_get_time_condition_by_product_id(id)

Get specified Product time conditions by Product Id.

Retrieves specified Product time conditions.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Identifier of the Product. (Required).

try:
    # Get specified Product time conditions by Product Id.
    api_response = api_instance.product_components_v1_get_time_condition_by_product_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_get_time_condition_by_product_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of the Product. (Required). | 

### Return type

[**ProductTimeCondition**](ProductTimeCondition.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_maintain_condition**
> MaintainResult product_components_v1_maintain_condition(maintain_condition_v1_model=maintain_condition_v1_model)

Creates  or updates a condition.

Creates or updates a condition with specified parameters.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
maintain_condition_v1_model = mdmv1.MaintainConditionV1Model() # MaintainConditionV1Model | Object representing ConditionModel. (optional)

try:
    # Creates  or updates a condition.
    api_response = api_instance.product_components_v1_maintain_condition(maintain_condition_v1_model=maintain_condition_v1_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_maintain_condition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintain_condition_v1_model** | [**MaintainConditionV1Model**](MaintainConditionV1Model.md)| Object representing ConditionModel. | [optional] 

### Return type

[**MaintainResult**](MaintainResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_maintain_event_action**
> MaintainResult product_components_v1_maintain_event_action(maintain_event_action_input=maintain_event_action_input)

Create or update an Event/Action.

This method creates new event action and updates existing event actions.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
maintain_event_action_input = mdmv1.MaintainEventActionInputEntity() # MaintainEventActionInputEntity | Input representing event/action and location group. (optional)

try:
    # Create or update an Event/Action.
    api_response = api_instance.product_components_v1_maintain_event_action(maintain_event_action_input=maintain_event_action_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_maintain_event_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintain_event_action_input** | [**MaintainEventActionInputEntity**](MaintainEventActionInputEntity.md)| Input representing event/action and location group. | [optional] 

### Return type

[**MaintainResult**](MaintainResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_maintain_file_action**
> product_components_v1_maintain_file_action(maintain_file_action_input=maintain_file_action_input)

Creates or updates a file action.

Creates or updates a file action when required data is passed.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
maintain_file_action_input = mdmv1.MaintainFileActionModel() # MaintainFileActionModel | Input representing file action and Organization group. (optional)

try:
    # Creates or updates a file action.
    api_instance.product_components_v1_maintain_file_action(maintain_file_action_input=maintain_file_action_input)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_maintain_file_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintain_file_action_input** | [**MaintainFileActionModel**](MaintainFileActionModel.md)| Input representing file action and Organization group. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_provisioning_queue_counts_async**
> ProvisioningQueueCounts product_components_v1_provisioning_queue_counts_async(id)

Report back queue counts pertaining to the policy engine.

Report back queue counts pertaining to the policy engine when Organization group ID is passed.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Organization group ID. (Required).

try:
    # Report back queue counts pertaining to the policy engine.
    api_response = api_instance.product_components_v1_provisioning_queue_counts_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_provisioning_queue_counts_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Organization group ID. (Required). | 

### Return type

[**ProvisioningQueueCounts**](ProvisioningQueueCounts.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_retrieve_product_download_and_install_statistics**
> DownloadAndInstallStatistics product_components_v1_retrieve_product_download_and_install_statistics(organizationgroupid=organizationgroupid, starttime=starttime, endtime=endtime, page=page, pagesize=pagesize)

Retrieves the product installation and download statistics.

Retrieves Product Download And Install Statistics based on the parameters passed.  The parameters starttime and endtime accepts the below DateTime formats :  <br>yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff, yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff,</br>  yyyy/MM/ddTHH:mm:ss.fff, yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group identifier. (optional)
starttime = '' # datetime | DateTime, Filters the result where Product's Last modified date on device is greater than or equal to starttime value.  (optional) (default to )
endtime = '' # datetime | DateTime, Filters the result where Product's Last modified date on device is lesser than or equal to endtime value. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Retrieves the product installation and download statistics.
    api_response = api_instance.product_components_v1_retrieve_product_download_and_install_statistics(organizationgroupid=organizationgroupid, starttime=starttime, endtime=endtime, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_retrieve_product_download_and_install_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group identifier. | [optional] 
 **starttime** | **datetime**| DateTime, Filters the result where Product&#39;s Last modified date on device is greater than or equal to starttime value.  | [optional] [default to ]
 **endtime** | **datetime**| DateTime, Filters the result where Product&#39;s Last modified date on device is lesser than or equal to endtime value. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**DownloadAndInstallStatistics**](DownloadAndInstallStatistics.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_search_files_actions**
> FilesActionsSearchResult product_components_v1_search_files_actions(organizationgroupid=organizationgroupid, platform=platform, lastmodifiedon=lastmodifiedon, lastmodifiedtill=lastmodifiedtill, page=page, pagesize=pagesize)

Searches for the Files/Actions with the search parameters passed.

Retrieves Files Actions Search Result when search parameters are passed.  The parameters lastmodifiedon and lastmodifiedtill accepts the below DateTime formats :  <br>yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff, yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff,</br>  yyyy/MM/ddTHH:mm:ss.fff, yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group ID. (optional)
platform = '' # str | Name of the Platform in which the Files/Actions is created. (Example:Android). (optional) (default to )
lastmodifiedon = '' # datetime | DateTime, Filters the result where Files/Actions modified date is greater than or equal to lastmodifiedon value. (optional) (default to )
lastmodifiedtill = '' # datetime | DateTime, Filters the result where Files/Actions modified date is lesser than or equal to lastmodifiedtill value. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Searches for the Files/Actions with the search parameters passed.
    api_response = api_instance.product_components_v1_search_files_actions(organizationgroupid=organizationgroupid, platform=platform, lastmodifiedon=lastmodifiedon, lastmodifiedtill=lastmodifiedtill, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_search_files_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group ID. | [optional] 
 **platform** | **str**| Name of the Platform in which the Files/Actions is created. (Example:Android). | [optional] [default to ]
 **lastmodifiedon** | **datetime**| DateTime, Filters the result where Files/Actions modified date is greater than or equal to lastmodifiedon value. | [optional] [default to ]
 **lastmodifiedtill** | **datetime**| DateTime, Filters the result where Files/Actions modified date is lesser than or equal to lastmodifiedtill value. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**FilesActionsSearchResult**](FilesActionsSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_components_v1_time_condition_search**
> list[TimeCondition] product_components_v1_time_condition_search(organizationgroupid=organizationgroupid, starttime=starttime, endtime=endtime)

New - Search for Time Conditions with the specified parameters.

Search for Time Conditions with the specified parameters such as organization group ID, start and end time values.  The parameters starttime and endtime accepts the below DateTime formats :  yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,   yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff,  yyyy/MM/ddTHH:mm:ss.fff, yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff,   MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.ProductComponentsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group identifier (optional)
starttime = '' # str | DateTime, Filters the result where TimeCondition modified date is greater than or equal to starttime value (optional) (default to )
endtime = '' # str | DateTime, Filters the result where TimeCondition modified date is lesser than or equal to endtime value (optional) (default to )

try:
    # New - Search for Time Conditions with the specified parameters.
    api_response = api_instance.product_components_v1_time_condition_search(organizationgroupid=organizationgroupid, starttime=starttime, endtime=endtime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductComponentsV1Api->product_components_v1_time_condition_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group identifier | [optional] 
 **starttime** | **str**| DateTime, Filters the result where TimeCondition modified date is greater than or equal to starttime value | [optional] [default to ]
 **endtime** | **str**| DateTime, Filters the result where TimeCondition modified date is lesser than or equal to endtime value | [optional] [default to ]

### Return type

[**list[TimeCondition]**](TimeCondition.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

