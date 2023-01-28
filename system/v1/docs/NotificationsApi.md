# systemv1.NotificationsApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_all_async**](NotificationsApi.md#notifications_all_async) | **GET** /notifications | Retrieves the list of notifications based on the core user.
[**notifications_dismiss_notification_async**](NotificationsApi.md#notifications_dismiss_notification_async) | **POST** /notifications/{id} | Dismiss a notification.
[**notifications_get_notification_counts**](NotificationsApi.md#notifications_get_notification_counts) | **GET** /notifications/count | Fetch notification counts.


# **notifications_all_async**
> list[ReadNotificationModel] notifications_all_async(start_index=start_index, page_size=page_size, active=active, culture_code=culture_code)

Retrieves the list of notifications based on the core user.

This API is used to get a list of all the notifications created for a particular admin.

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
api_instance = systemv1.NotificationsApi(systemv1.ApiClient(configuration))
start_index = 56 # int | Optional. Start index for the list of fetched notifications. Default value is 0. (optional)
page_size = 56 # int | Optional. Number of notifications fetched per page. Default value is 0. (optional)
active =  # bool | Optional. Option to fetch active/dismissed notifications. Value can be true or false. Default value is true. (optional) (default to )
culture_code = '' # str | Optional. Option to provide the locale setting for the fetched notifications. Default value is the default culture code for the core user. (optional) (default to )

try:
    # Retrieves the list of notifications based on the core user.
    api_response = api_instance.notifications_all_async(start_index=start_index, page_size=page_size, active=active, culture_code=culture_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_all_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| Optional. Start index for the list of fetched notifications. Default value is 0. | [optional] 
 **page_size** | **int**| Optional. Number of notifications fetched per page. Default value is 0. | [optional] 
 **active** | **bool**| Optional. Option to fetch active/dismissed notifications. Value can be true or false. Default value is true. | [optional] [default to ]
 **culture_code** | **str**| Optional. Option to provide the locale setting for the fetched notifications. Default value is the default culture code for the core user. | [optional] [default to ]

### Return type

[**list[ReadNotificationModel]**](ReadNotificationModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_dismiss_notification_async**
> EntityId notifications_dismiss_notification_async(id)

Dismiss a notification.

Dismiss a notification using notification id passed in by the user.

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
api_instance = systemv1.NotificationsApi(systemv1.ApiClient(configuration))
id = 56 # int | Notification id.

try:
    # Dismiss a notification.
    api_response = api_instance.notifications_dismiss_notification_async(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_dismiss_notification_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Notification id. | 

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_get_notification_counts**
> NotificationCountModel notifications_get_notification_counts()

Fetch notification counts.

Retrieves the total, active and dismissed count of notifications.

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
api_instance = systemv1.NotificationsApi(systemv1.ApiClient(configuration))

try:
    # Fetch notification counts.
    api_response = api_instance.notifications_get_notification_counts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_get_notification_counts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationCountModel**](NotificationCountModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

