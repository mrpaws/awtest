# systemv1.EventNotificationsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_notifications_v1_create_event_notification_rule**](EventNotificationsV1Api.md#event_notifications_v1_create_event_notification_rule) | **POST** /eventnotifications | Creates a new Event Notification rule with events to subscribe to.
[**event_notifications_v1_create_event_notification_rule_0**](EventNotificationsV1Api.md#event_notifications_v1_create_event_notification_rule_0) | **POST** /eventnotifications/V1/eventnotifications | Creates a new Event Notification rule with events to subscribe to.
[**event_notifications_v1_delete_event_notification_rule**](EventNotificationsV1Api.md#event_notifications_v1_delete_event_notification_rule) | **DELETE** /eventnotifications/{id} | Deletes an Event Notification Rule identified by the Event Notification Id.
[**event_notifications_v1_delete_event_notification_rule_0**](EventNotificationsV1Api.md#event_notifications_v1_delete_event_notification_rule_0) | **DELETE** /eventnotifications/V1/eventnotifications/{id} | Deletes an Event Notification Rule identified by the Event Notification Id.
[**event_notifications_v1_get_event_notification_by_id**](EventNotificationsV1Api.md#event_notifications_v1_get_event_notification_by_id) | **GET** /eventnotifications/{id} | Retrieves details of an Event Notification Rule identified by EventNotification Id.
[**event_notifications_v1_get_event_notification_by_id_0**](EventNotificationsV1Api.md#event_notifications_v1_get_event_notification_by_id_0) | **GET** /eventnotifications/V1/eventnotifications/{id} | Retrieves details of an Event Notification Rule identified by EventNotification Id.
[**event_notifications_v1_search**](EventNotificationsV1Api.md#event_notifications_v1_search) | **GET** /eventnotifications/search | Searches Event Notifications based on the query information provided.
[**event_notifications_v1_search_0**](EventNotificationsV1Api.md#event_notifications_v1_search_0) | **GET** /eventnotifications/V1/eventnotifications/search | Searches Event Notifications based on the query information provided.
[**event_notifications_v1_update_event_notification_rule**](EventNotificationsV1Api.md#event_notifications_v1_update_event_notification_rule) | **PUT** /eventnotifications/{id} | Updates an Event Notification Rule identified by the Event Notification Id.
[**event_notifications_v1_update_event_notification_rule_0**](EventNotificationsV1Api.md#event_notifications_v1_update_event_notification_rule_0) | **PUT** /eventnotifications/V1/eventnotifications/{id} | Updates an Event Notification Rule identified by the Event Notification Id.


# **event_notifications_v1_create_event_notification_rule**
> event_notifications_v1_create_event_notification_rule(model=model)

Creates a new Event Notification rule with events to subscribe to.

v1.

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
api_instance = systemv1.EventNotificationsV1Api(systemv1.ApiClient(configuration))
model = systemv1.EventNotificationModel() # EventNotificationModel | The Event Notification Model. (optional)

try:
    # Creates a new Event Notification rule with events to subscribe to.
    api_instance.event_notifications_v1_create_event_notification_rule(model=model)
except ApiException as e:
    print("Exception when calling EventNotificationsV1Api->event_notifications_v1_create_event_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**EventNotificationModel**](EventNotificationModel.md)| The Event Notification Model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_notifications_v1_create_event_notification_rule_0**
> event_notifications_v1_create_event_notification_rule_0(model=model)

Creates a new Event Notification rule with events to subscribe to.

v1.

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
api_instance = systemv1.EventNotificationsV1Api(systemv1.ApiClient(configuration))
model = systemv1.EventNotificationModel() # EventNotificationModel | The Event Notification Model. (optional)

try:
    # Creates a new Event Notification rule with events to subscribe to.
    api_instance.event_notifications_v1_create_event_notification_rule_0(model=model)
except ApiException as e:
    print("Exception when calling EventNotificationsV1Api->event_notifications_v1_create_event_notification_rule_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**EventNotificationModel**](EventNotificationModel.md)| The Event Notification Model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_notifications_v1_delete_event_notification_rule**
> event_notifications_v1_delete_event_notification_rule(id)

Deletes an Event Notification Rule identified by the Event Notification Id.

v1.

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
api_instance = systemv1.EventNotificationsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The Event Notification Id.

try:
    # Deletes an Event Notification Rule identified by the Event Notification Id.
    api_instance.event_notifications_v1_delete_event_notification_rule(id)
except ApiException as e:
    print("Exception when calling EventNotificationsV1Api->event_notifications_v1_delete_event_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Event Notification Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_notifications_v1_delete_event_notification_rule_0**
> event_notifications_v1_delete_event_notification_rule_0(id)

Deletes an Event Notification Rule identified by the Event Notification Id.

v1.

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
api_instance = systemv1.EventNotificationsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The Event Notification Id.

try:
    # Deletes an Event Notification Rule identified by the Event Notification Id.
    api_instance.event_notifications_v1_delete_event_notification_rule_0(id)
except ApiException as e:
    print("Exception when calling EventNotificationsV1Api->event_notifications_v1_delete_event_notification_rule_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Event Notification Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_notifications_v1_get_event_notification_by_id**
> event_notifications_v1_get_event_notification_by_id(id)

Retrieves details of an Event Notification Rule identified by EventNotification Id.

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
api_instance = systemv1.EventNotificationsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The Event Notification Id.

try:
    # Retrieves details of an Event Notification Rule identified by EventNotification Id.
    api_instance.event_notifications_v1_get_event_notification_by_id(id)
except ApiException as e:
    print("Exception when calling EventNotificationsV1Api->event_notifications_v1_get_event_notification_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Event Notification Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_notifications_v1_get_event_notification_by_id_0**
> event_notifications_v1_get_event_notification_by_id_0(id)

Retrieves details of an Event Notification Rule identified by EventNotification Id.

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
api_instance = systemv1.EventNotificationsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The Event Notification Id.

try:
    # Retrieves details of an Event Notification Rule identified by EventNotification Id.
    api_instance.event_notifications_v1_get_event_notification_by_id_0(id)
except ApiException as e:
    print("Exception when calling EventNotificationsV1Api->event_notifications_v1_get_event_notification_by_id_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Event Notification Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_notifications_v1_search**
> event_notifications_v1_search(targetname=targetname, organizationgroupid=organizationgroupid, status=status, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)

Searches Event Notifications based on the query information provided.

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
api_instance = systemv1.EventNotificationsV1Api(systemv1.ApiClient(configuration))
targetname = '' # str | The Target Name. (optional) (default to )
organizationgroupid = '' # str | The OrganizationGroup Identifier. (optional) (default to )
status = '' # str | The Event Notification status [Active, Inactive]. (optional) (default to )
orderby = '' # str | Sorts the response based on this attribute [TargetName, TargetUrl, FormatType, UserName, Active]. (optional) (default to )
sortorder = '' # str | Sorting order. Values ASC or DESC. Defaults to ASC.. (optional) (default to )
page = 56 # int | Page number. (optional)
pagesize = 56 # int | Number of Records per page. (optional)

try:
    # Searches Event Notifications based on the query information provided.
    api_instance.event_notifications_v1_search(targetname=targetname, organizationgroupid=organizationgroupid, status=status, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)
except ApiException as e:
    print("Exception when calling EventNotificationsV1Api->event_notifications_v1_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targetname** | **str**| The Target Name. | [optional] [default to ]
 **organizationgroupid** | **str**| The OrganizationGroup Identifier. | [optional] [default to ]
 **status** | **str**| The Event Notification status [Active, Inactive]. | [optional] [default to ]
 **orderby** | **str**| Sorts the response based on this attribute [TargetName, TargetUrl, FormatType, UserName, Active]. | [optional] [default to ]
 **sortorder** | **str**| Sorting order. Values ASC or DESC. Defaults to ASC.. | [optional] [default to ]
 **page** | **int**| Page number. | [optional] 
 **pagesize** | **int**| Number of Records per page. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_notifications_v1_search_0**
> event_notifications_v1_search_0(targetname=targetname, organizationgroupid=organizationgroupid, status=status, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)

Searches Event Notifications based on the query information provided.

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
api_instance = systemv1.EventNotificationsV1Api(systemv1.ApiClient(configuration))
targetname = '' # str | The Target Name. (optional) (default to )
organizationgroupid = '' # str | The OrganizationGroup Identifier. (optional) (default to )
status = '' # str | The Event Notification status [Active, Inactive]. (optional) (default to )
orderby = '' # str | Sorts the response based on this attribute [TargetName, TargetUrl, FormatType, UserName, Active]. (optional) (default to )
sortorder = '' # str | Sorting order. Values ASC or DESC. Defaults to ASC.. (optional) (default to )
page = 56 # int | Page number. (optional)
pagesize = 56 # int | Number of Records per page. (optional)

try:
    # Searches Event Notifications based on the query information provided.
    api_instance.event_notifications_v1_search_0(targetname=targetname, organizationgroupid=organizationgroupid, status=status, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)
except ApiException as e:
    print("Exception when calling EventNotificationsV1Api->event_notifications_v1_search_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targetname** | **str**| The Target Name. | [optional] [default to ]
 **organizationgroupid** | **str**| The OrganizationGroup Identifier. | [optional] [default to ]
 **status** | **str**| The Event Notification status [Active, Inactive]. | [optional] [default to ]
 **orderby** | **str**| Sorts the response based on this attribute [TargetName, TargetUrl, FormatType, UserName, Active]. | [optional] [default to ]
 **sortorder** | **str**| Sorting order. Values ASC or DESC. Defaults to ASC.. | [optional] [default to ]
 **page** | **int**| Page number. | [optional] 
 **pagesize** | **int**| Number of Records per page. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_notifications_v1_update_event_notification_rule**
> event_notifications_v1_update_event_notification_rule(id, model=model)

Updates an Event Notification Rule identified by the Event Notification Id.

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
api_instance = systemv1.EventNotificationsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The Event Notification Id.
model = systemv1.EventNotificationModel() # EventNotificationModel | The Event Notification Model. (optional)

try:
    # Updates an Event Notification Rule identified by the Event Notification Id.
    api_instance.event_notifications_v1_update_event_notification_rule(id, model=model)
except ApiException as e:
    print("Exception when calling EventNotificationsV1Api->event_notifications_v1_update_event_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Event Notification Id. | 
 **model** | [**EventNotificationModel**](EventNotificationModel.md)| The Event Notification Model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_notifications_v1_update_event_notification_rule_0**
> event_notifications_v1_update_event_notification_rule_0(id, model=model)

Updates an Event Notification Rule identified by the Event Notification Id.

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
api_instance = systemv1.EventNotificationsV1Api(systemv1.ApiClient(configuration))
id = 56 # int | The Event Notification Id.
model = systemv1.EventNotificationModel() # EventNotificationModel | The Event Notification Model. (optional)

try:
    # Updates an Event Notification Rule identified by the Event Notification Id.
    api_instance.event_notifications_v1_update_event_notification_rule_0(id, model=model)
except ApiException as e:
    print("Exception when calling EventNotificationsV1Api->event_notifications_v1_update_event_notification_rule_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Event Notification Id. | 
 **model** | [**EventNotificationModel**](EventNotificationModel.md)| The Event Notification Model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

