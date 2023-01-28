# mdmv1.MessagesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messages_send_bulk_email_by_alternate_id_async**](MessagesApi.md#messages_send_bulk_email_by_alternate_id_async) | **POST** /devices/messages/bulkemail | Sends an email to the users of multiple devices.
[**messages_send_bulk_message_sms_by_alternate_id_async**](MessagesApi.md#messages_send_bulk_message_sms_by_alternate_id_async) | **POST** /devices/messages/bulksms | Sends an SMS message to multiple devices.
[**messages_send_bulk_push_by_alternate_id_async**](MessagesApi.md#messages_send_bulk_push_by_alternate_id_async) | **POST** /devices/messages/bulkpush | Sends a push message to multiple devices.
[**messages_send_email_async**](MessagesApi.md#messages_send_email_async) | **POST** /devices/{id}/messages/email | Sends an email to the user of the device.
[**messages_send_email_by_alternate_id_async**](MessagesApi.md#messages_send_email_by_alternate_id_async) | **POST** /devices/messages/email | Sends an email to the user of the device.
[**messages_send_message_async**](MessagesApi.md#messages_send_message_async) | **POST** /devices/messages/{id}/message | Sends a message to the device.
[**messages_send_message_by_alternate_id_async**](MessagesApi.md#messages_send_message_by_alternate_id_async) | **POST** /devices/messages/message | Sends a message to the device.
[**messages_send_push_async**](MessagesApi.md#messages_send_push_async) | **POST** /devices/{id}/messages/push | Sends a push message to the device.
[**messages_send_push_by_alternate_id_async**](MessagesApi.md#messages_send_push_by_alternate_id_async) | **POST** /devices/messages/push | Sends a push message to the device.
[**messages_send_sms_async**](MessagesApi.md#messages_send_sms_async) | **POST** /devices/{id}/messages/sms | Sends an SMS message to the device.
[**messages_send_sms_by_alternate_id_async**](MessagesApi.md#messages_send_sms_by_alternate_id_async) | **POST** /devices/messages/sms | Sends an SMS message to the device.


# **messages_send_bulk_email_by_alternate_id_async**
> BulkResponse messages_send_bulk_email_by_alternate_id_async(email_message, searchby)

Sends an email to the users of multiple devices.

Sends an email to the users of multiple devices identified by their alternate ID.

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
api_instance = mdmv1.MessagesApi(mdmv1.ApiClient(configuration))
email_message = mdmv1.EmailMessage() # EmailMessage | Information about the email message to send and the recipient devices (Required).
searchby = '' # str | The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). (default to )

try:
    # Sends an email to the users of multiple devices.
    api_response = api_instance.messages_send_bulk_email_by_alternate_id_async(email_message, searchby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_bulk_email_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_message** | [**EmailMessage**](EmailMessage.md)| Information about the email message to send and the recipient devices (Required). | 
 **searchby** | **str**| The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). | [default to ]

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_send_bulk_message_sms_by_alternate_id_async**
> BulkResponse messages_send_bulk_message_sms_by_alternate_id_async(sms_message, searchby)

Sends an SMS message to multiple devices.

Sends an SMS message to multiple devices identified by their alternate ID.

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
api_instance = mdmv1.MessagesApi(mdmv1.ApiClient(configuration))
sms_message = mdmv1.SmsMessage() # SmsMessage | Information about the SMS message and recipient devices (Required).
searchby = '' # str | The alternate id type of the devices [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). (default to )

try:
    # Sends an SMS message to multiple devices.
    api_response = api_instance.messages_send_bulk_message_sms_by_alternate_id_async(sms_message, searchby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_bulk_message_sms_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_message** | [**SmsMessage**](SmsMessage.md)| Information about the SMS message and recipient devices (Required). | 
 **searchby** | **str**| The alternate id type of the devices [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). | [default to ]

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_send_bulk_push_by_alternate_id_async**
> BulkResponse messages_send_bulk_push_by_alternate_id_async(push_notification_message, search_by)

Sends a push message to multiple devices.

Sends a push message to multiple devices identified by their alternate ID.

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
api_instance = mdmv1.MessagesApi(mdmv1.ApiClient(configuration))
push_notification_message = mdmv1.PushNotificationMessage() # PushNotificationMessage | Information about the push message to send and the recipient devices (Required).
search_by = '' # str | The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). (default to )

try:
    # Sends a push message to multiple devices.
    api_response = api_instance.messages_send_bulk_push_by_alternate_id_async(push_notification_message, search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_bulk_push_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_notification_message** | [**PushNotificationMessage**](PushNotificationMessage.md)| Information about the push message to send and the recipient devices (Required). | 
 **search_by** | **str**| The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). | [default to ]

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_send_email_async**
> messages_send_email_async(id, email)

Sends an email to the user of the device.

Sends an email message to the user of the device specified by the device id.

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
api_instance = mdmv1.MessagesApi(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID of the recipient device (Required).
email = mdmv1.Email() # Email | Information about the email message (Required).

try:
    # Sends an email to the user of the device.
    api_instance.messages_send_email_async(id, email)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_email_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID of the recipient device (Required). | 
 **email** | [**Email**](Email.md)| Information about the email message (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_send_email_by_alternate_id_async**
> messages_send_email_by_alternate_id_async(searchby, id, email=email)

Sends an email to the user of the device.

Sends an email to the user of the device identified by alternate id.

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
api_instance = mdmv1.MessagesApi(mdmv1.ApiClient(configuration))
searchby = '' # str | The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). (default to )
id = '' # str | The alternate id of the device (Required). (default to )
email = mdmv1.Email() # Email | Information about the email message. (optional)

try:
    # Sends an email to the user of the device.
    api_instance.messages_send_email_by_alternate_id_async(searchby, id, email=email)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_email_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchby** | **str**| The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). | [default to ]
 **id** | **str**| The alternate id of the device (Required). | [default to ]
 **email** | [**Email**](Email.md)| Information about the email message. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_send_message_async**
> messages_send_message_async(id, generic_message=generic_message)

Sends a message to the device.

Sends a push notification to the device identified by device ID. If the device is not enrolled, an SMS message will be sent instead.

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
api_instance = mdmv1.MessagesApi(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID of the recipient device (Required).
generic_message = mdmv1.GenericMessage() # GenericMessage | Information about the message to send. (optional)

try:
    # Sends a message to the device.
    api_instance.messages_send_message_async(id, generic_message=generic_message)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_message_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID of the recipient device (Required). | 
 **generic_message** | [**GenericMessage**](GenericMessage.md)| Information about the message to send. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_send_message_by_alternate_id_async**
> messages_send_message_by_alternate_id_async(searchby, id, generic_message=generic_message)

Sends a message to the device.

Sends a push notification to the device identified by alternate ID. If the device is not enrolled, an SMS message will be sent instead.

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
api_instance = mdmv1.MessagesApi(mdmv1.ApiClient(configuration))
searchby = '' # str | The alternate id type to search by [DeviceId, Macaddress, Udid, Serialnumber] (Required). (default to )
id = '' # str | The alternate id of the device (Required). (default to )
generic_message = mdmv1.GenericMessage() # GenericMessage | Information about the message to send. (optional)

try:
    # Sends a message to the device.
    api_instance.messages_send_message_by_alternate_id_async(searchby, id, generic_message=generic_message)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_message_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchby** | **str**| The alternate id type to search by [DeviceId, Macaddress, Udid, Serialnumber] (Required). | [default to ]
 **id** | **str**| The alternate id of the device (Required). | [default to ]
 **generic_message** | [**GenericMessage**](GenericMessage.md)| Information about the message to send. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_send_push_async**
> messages_send_push_async(id, push_message)

Sends a push message to the device.

Sends a push message to the device specified by the device id.

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
api_instance = mdmv1.MessagesApi(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID of the recipient device (Required).
push_message = mdmv1.PushMessage() # PushMessage | Information about the push message (Required).

try:
    # Sends a push message to the device.
    api_instance.messages_send_push_async(id, push_message)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_push_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID of the recipient device (Required). | 
 **push_message** | [**PushMessage**](PushMessage.md)| Information about the push message (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_send_push_by_alternate_id_async**
> messages_send_push_by_alternate_id_async(searchby, id, push_message=push_message)

Sends a push message to the device.

Sends a push notification message to the device identified by alternate id.

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
api_instance = mdmv1.MessagesApi(mdmv1.ApiClient(configuration))
searchby = '' # str | The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). (default to )
id = '' # str | The alternate id of the device (Required). (default to )
push_message = mdmv1.PushMessage() # PushMessage | Information about the push message to send. (optional)

try:
    # Sends a push message to the device.
    api_instance.messages_send_push_by_alternate_id_async(searchby, id, push_message=push_message)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_push_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchby** | **str**| The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). | [default to ]
 **id** | **str**| The alternate id of the device (Required). | [default to ]
 **push_message** | [**PushMessage**](PushMessage.md)| Information about the push message to send. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_send_sms_async**
> messages_send_sms_async(id, sms)

Sends an SMS message to the device.

Sends an SMS message to the device identified by the device ID in the URL.

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
api_instance = mdmv1.MessagesApi(mdmv1.ApiClient(configuration))
id = 56 # int | The device ID of the recipient device (Required).
sms = mdmv1.Sms() # Sms | Information about the SMS message (Required).

try:
    # Sends an SMS message to the device.
    api_instance.messages_send_sms_async(id, sms)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_sms_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID of the recipient device (Required). | 
 **sms** | [**Sms**](Sms.md)| Information about the SMS message (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_send_sms_by_alternate_id_async**
> messages_send_sms_by_alternate_id_async(searchby, id, sms=sms)

Sends an SMS message to the device.

Sends an SMS message to the device identified by alternate id.

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
api_instance = mdmv1.MessagesApi(mdmv1.ApiClient(configuration))
searchby = '' # str | The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). (default to )
id = '' # str | The alternate id of the device (Required). (default to )
sms = mdmv1.Sms() # Sms | Information about the SMS message. (optional)

try:
    # Sends an SMS message to the device.
    api_instance.messages_send_sms_by_alternate_id_async(searchby, id, sms=sms)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_sms_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchby** | **str**| The alternate id type [DeviceId, Macaddress, Udid, Serialnumber, ImeiNumber] (Required). | [default to ]
 **id** | **str**| The alternate id of the device (Required). | [default to ]
 **sms** | [**Sms**](Sms.md)| Information about the SMS message. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

