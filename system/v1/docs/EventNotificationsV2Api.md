# systemv1.EventNotificationsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_notifications_v2_create_event_notification_rule**](EventNotificationsV2Api.md#event_notifications_v2_create_event_notification_rule) | **POST** /eventnotifications/V2/eventnotifications | New - Creates a new Event Notification rule with events to subscribe to.
[**event_notifications_v2_delete_event_notification_rule**](EventNotificationsV2Api.md#event_notifications_v2_delete_event_notification_rule) | **DELETE** /eventnotifications/V2/eventnotifications/{uuid} | New - Deletes an Event Notification Rule identified by the Event Notification Id.
[**event_notifications_v2_get_event_notification_by_id**](EventNotificationsV2Api.md#event_notifications_v2_get_event_notification_by_id) | **GET** /eventnotifications/V2/eventnotifications/{uuid} | New - Retrieves details of an Event Notification Rule identified by EventNotification Id.
[**event_notifications_v2_get_event_notifications_and_subscriptions**](EventNotificationsV2Api.md#event_notifications_v2_get_event_notifications_and_subscriptions) | **GET** /eventnotifications/V2/eventnotifications/get | Get Event Notifications and Subscriptions based on optional OrganizationGroup Id or page size.
[**event_notifications_v2_search**](EventNotificationsV2Api.md#event_notifications_v2_search) | **GET** /eventnotifications/V2/eventnotifications/search | New - Searches Event Notifications based on the query information provided.
[**event_notifications_v2_update_event_notification_rule**](EventNotificationsV2Api.md#event_notifications_v2_update_event_notification_rule) | **PUT** /eventnotifications/V2/eventnotifications/{uuid} | New - Updates an Event Notification Rule identified by the Event Notification Id.


# **event_notifications_v2_create_event_notification_rule**
> event_notifications_v2_create_event_notification_rule(model=model)

New - Creates a new Event Notification rule with events to subscribe to.

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
api_instance = systemv1.EventNotificationsV2Api(systemv1.ApiClient(configuration))
model = systemv1.EventNotificationModel() # EventNotificationModel | The Event Notification Model. (optional)

try:
    # New - Creates a new Event Notification rule with events to subscribe to.
    api_instance.event_notifications_v2_create_event_notification_rule(model=model)
except ApiException as e:
    print("Exception when calling EventNotificationsV2Api->event_notifications_v2_create_event_notification_rule: %s\n" % e)
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

# **event_notifications_v2_delete_event_notification_rule**
> event_notifications_v2_delete_event_notification_rule(uuid)

New - Deletes an Event Notification Rule identified by the Event Notification Id.

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
api_instance = systemv1.EventNotificationsV2Api(systemv1.ApiClient(configuration))
uuid = 'uuid_example' # str | The Event Notification GUID.

try:
    # New - Deletes an Event Notification Rule identified by the Event Notification Id.
    api_instance.event_notifications_v2_delete_event_notification_rule(uuid)
except ApiException as e:
    print("Exception when calling EventNotificationsV2Api->event_notifications_v2_delete_event_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The Event Notification GUID. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_notifications_v2_get_event_notification_by_id**
> event_notifications_v2_get_event_notification_by_id(uuid)

New - Retrieves details of an Event Notification Rule identified by EventNotification Id.

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
api_instance = systemv1.EventNotificationsV2Api(systemv1.ApiClient(configuration))
uuid = 'uuid_example' # str | The Event Notification GUID.

try:
    # New - Retrieves details of an Event Notification Rule identified by EventNotification Id.
    api_instance.event_notifications_v2_get_event_notification_by_id(uuid)
except ApiException as e:
    print("Exception when calling EventNotificationsV2Api->event_notifications_v2_get_event_notification_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The Event Notification GUID. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_notifications_v2_get_event_notifications_and_subscriptions**
> event_notifications_v2_get_event_notifications_and_subscriptions(organizationgroupuuid=organizationgroupuuid, page=page, pagesize=pagesize)

Get Event Notifications and Subscriptions based on optional OrganizationGroup Id or page size.

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
api_instance = systemv1.EventNotificationsV2Api(systemv1.ApiClient(configuration))
organizationgroupuuid = '' # str | The OrganizationGroup Identifier. (optional) (default to )
page = 56 # int | Page number. (optional)
pagesize = 56 # int | Number of Records per page. (optional)

try:
    # Get Event Notifications and Subscriptions based on optional OrganizationGroup Id or page size.
    api_instance.event_notifications_v2_get_event_notifications_and_subscriptions(organizationgroupuuid=organizationgroupuuid, page=page, pagesize=pagesize)
except ApiException as e:
    print("Exception when calling EventNotificationsV2Api->event_notifications_v2_get_event_notifications_and_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupuuid** | **str**| The OrganizationGroup Identifier. | [optional] [default to ]
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

# **event_notifications_v2_search**
> event_notifications_v2_search(targetname=targetname, organizationgroupuuid=organizationgroupuuid, status=status, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)

New - Searches Event Notifications based on the query information provided.

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
api_instance = systemv1.EventNotificationsV2Api(systemv1.ApiClient(configuration))
targetname = '' # str | The Target Name. (optional) (default to )
organizationgroupuuid = '' # str | The OrganizationGroup Identifier. (optional) (default to )
status = '' # str | The Event Notification status [Active, Inactive]. (optional) (default to )
orderby = '' # str | Sorts the response based on this attribute [TargetName, TargetUrl, FormatType, UserName, Active]. (optional) (default to )
sortorder = '' # str | Sorting order. Values ASC or DESC. Defaults to ASC.. (optional) (default to )
page = 56 # int | Page number. (optional)
pagesize = 56 # int | Number of Records per page. (optional)

try:
    # New - Searches Event Notifications based on the query information provided.
    api_instance.event_notifications_v2_search(targetname=targetname, organizationgroupuuid=organizationgroupuuid, status=status, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)
except ApiException as e:
    print("Exception when calling EventNotificationsV2Api->event_notifications_v2_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targetname** | **str**| The Target Name. | [optional] [default to ]
 **organizationgroupuuid** | **str**| The OrganizationGroup Identifier. | [optional] [default to ]
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

# **event_notifications_v2_update_event_notification_rule**
> event_notifications_v2_update_event_notification_rule(uuid, model=model)

New - Updates an Event Notification Rule identified by the Event Notification Id.

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
api_instance = systemv1.EventNotificationsV2Api(systemv1.ApiClient(configuration))
uuid = 'uuid_example' # str | The Event Notification GUID.
model = systemv1.EventNotificationModel() # EventNotificationModel | The Event Notification Model. (optional)

try:
    # New - Updates an Event Notification Rule identified by the Event Notification Id.
    api_instance.event_notifications_v2_update_event_notification_rule(uuid, model=model)
except ApiException as e:
    print("Exception when calling EventNotificationsV2Api->event_notifications_v2_update_event_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The Event Notification GUID. | 
 **model** | [**EventNotificationModel**](EventNotificationModel.md)| The Event Notification Model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

