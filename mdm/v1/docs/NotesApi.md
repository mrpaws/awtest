# mdmv1.NotesApi

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notes_create_notes**](NotesApi.md#notes_create_notes) | **POST** /devices/{deviceId}/notes | Creates a new note for the device identified by device ID.
[**notes_create_notes_by_alternate_id_async**](NotesApi.md#notes_create_notes_by_alternate_id_async) | **POST** /devices/notes | Creates a note for the device identified by alternate ID.
[**notes_delete_note**](NotesApi.md#notes_delete_note) | **DELETE** /devices/{deviceId}/notes/{noteId} | Deletes a note identified by note ID for the device identified by device ID.
[**notes_delete_note_by_alternate_id_async**](NotesApi.md#notes_delete_note_by_alternate_id_async) | **DELETE** /devices/notes/{noteId} | Deletes a note for the device identified by alternate ID.
[**notes_get_device_note**](NotesApi.md#notes_get_device_note) | **GET** /devices/{deviceId}/notes/{noteId} | Retrieves a particular note identified by note ID for the device identified by device ID.
[**notes_get_device_note_by_alternate_id_async**](NotesApi.md#notes_get_device_note_by_alternate_id_async) | **GET** /devices/notes/{noteId} | Retrieves a particular note for the device identified by alternate ID.
[**notes_get_device_notes_by_alternate_id_async**](NotesApi.md#notes_get_device_notes_by_alternate_id_async) | **GET** /devices/notes | Retrieves the notes for the device identified by alternate ID.
[**notes_get_notes_by_device**](NotesApi.md#notes_get_notes_by_device) | **GET** /devices/{id}/notes | Retrieves the notes for the device identified by device ID.
[**notes_update_notes**](NotesApi.md#notes_update_notes) | **PUT** /devices/{deviceId}/notes/{noteId} | Updates a note identified by note ID for the device identified by device ID.
[**notes_update_notes_by_alternate_id_async**](NotesApi.md#notes_update_notes_by_alternate_id_async) | **PUT** /devices/notes/{noteId} | Updates a note for the device identified by alternate ID.


# **notes_create_notes**
> EntityId notes_create_notes(device_id, device_notes)

Creates a new note for the device identified by device ID.

Creates a new note for the specified device identified by device ID.  <br />   Notes can help better device management within deployment by specifying these against devices.

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
api_instance = mdmv1.NotesApi(mdmv1.ApiClient(configuration))
device_id = 56 # int | Unique identifier used to identify device. (Required).
device_notes = mdmv1.DeviceNotes() # DeviceNotes | New device note to be added against specified device. (required).

try:
    # Creates a new note for the device identified by device ID.
    api_response = api_instance.notes_create_notes(device_id, device_notes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_create_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Unique identifier used to identify device. (Required). | 
 **device_notes** | [**DeviceNotes**](DeviceNotes.md)| New device note to be added against specified device. (required). | 

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_create_notes_by_alternate_id_async**
> EntityId notes_create_notes_by_alternate_id_async(device_notes, search_by, id)

Creates a note for the device identified by alternate ID.

Perform all the necessary checks and  creates a note for the device corresponding to alternate ID [Macaddress, Udid, Serialnumber, ImeiNumber].  <br />  Notes can help better device management within deployment by specifying these against devices.

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
api_instance = mdmv1.NotesApi(mdmv1.ApiClient(configuration))
device_notes = mdmv1.DeviceNotes_() # DeviceNotes_ | The DeviceNotes resource to create.(Required).
search_by = '' # str | The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837).(Required). (default to )
id = '' # str | Device alternate ID.(Required). (default to )

try:
    # Creates a note for the device identified by alternate ID.
    api_response = api_instance.notes_create_notes_by_alternate_id_async(device_notes, search_by, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_create_notes_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_notes** | [**DeviceNotes_**](DeviceNotes_.md)| The DeviceNotes resource to create.(Required). | 
 **search_by** | **str**| The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837).(Required). | [default to ]
 **id** | **str**| Device alternate ID.(Required). | [default to ]

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_delete_note**
> EntityId notes_delete_note(device_id, note_id)

Deletes a note identified by note ID for the device identified by device ID.

Deletes the existing note identified by note ID for the specified device identified by device ID.  <br />  Notes can help better device management within deployment by specifying these against devices.

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
api_instance = mdmv1.NotesApi(mdmv1.ApiClient(configuration))
device_id = 56 # int | Unique identifier used to identify device. (Required).
note_id = 56 # int | Unique identifier used to identify device note. (Required).

try:
    # Deletes a note identified by note ID for the device identified by device ID.
    api_response = api_instance.notes_delete_note(device_id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_delete_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Unique identifier used to identify device. (Required). | 
 **note_id** | **int**| Unique identifier used to identify device note. (Required). | 

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_delete_note_by_alternate_id_async**
> notes_delete_note_by_alternate_id_async(note_id, search_by, id)

Deletes a note for the device identified by alternate ID.

Perform all the necessary checks and  deletes the note corresponding to alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber].  <br />  Notes can help better device management within deployment by specifying these against devices.

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
api_instance = mdmv1.NotesApi(mdmv1.ApiClient(configuration))
note_id = 56 # int | The note ID.(Required).
search_by = '' # str | The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837).(Required). (default to )
id = '' # str | Device alternate ID.(Required). (default to )

try:
    # Deletes a note for the device identified by alternate ID.
    api_instance.notes_delete_note_by_alternate_id_async(note_id, search_by, id)
except ApiException as e:
    print("Exception when calling NotesApi->notes_delete_note_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| The note ID.(Required). | 
 **search_by** | **str**| The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837).(Required). | [default to ]
 **id** | **str**| Device alternate ID.(Required). | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_get_device_note**
> DeviceNotes notes_get_device_note(device_id, note_id)

Retrieves a particular note identified by note ID for the device identified by device ID.

Retrieves the particular note identified by note ID added for specified device identified by device ID.  <br />  Notes can help better device management within deployment by specifying these against devices.

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
api_instance = mdmv1.NotesApi(mdmv1.ApiClient(configuration))
device_id = 56 # int | Unique identifier used to identify device. (Required).
note_id = 56 # int | Unique identifier used to identify device note. (Required).

try:
    # Retrieves a particular note identified by note ID for the device identified by device ID.
    api_response = api_instance.notes_get_device_note(device_id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_get_device_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Unique identifier used to identify device. (Required). | 
 **note_id** | **int**| Unique identifier used to identify device note. (Required). | 

### Return type

[**DeviceNotes**](DeviceNotes.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_get_device_note_by_alternate_id_async**
> DeviceNotes notes_get_device_note_by_alternate_id_async(note_id, search_by, id)

Retrieves a particular note for the device identified by alternate ID.

Perform all the necessary checks and  returns the particular note for the device corresponding to alternate ID.  <br />  Notes can help better device management within deployment by specifying these against devices.

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
api_instance = mdmv1.NotesApi(mdmv1.ApiClient(configuration))
note_id = 56 # int | The note ID.(Required).
search_by = '' # str | The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837).(Required). (default to )
id = '' # str | Device alternate ID.(Required). (default to )

try:
    # Retrieves a particular note for the device identified by alternate ID.
    api_response = api_instance.notes_get_device_note_by_alternate_id_async(note_id, search_by, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_get_device_note_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| The note ID.(Required). | 
 **search_by** | **str**| The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837).(Required). | [default to ]
 **id** | **str**| Device alternate ID.(Required). | [default to ]

### Return type

[**DeviceNotes**](DeviceNotes.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_get_device_notes_by_alternate_id_async**
> DeviceNotesSearchResult notes_get_device_notes_by_alternate_id_async(search_by, id)

Retrieves the notes for the device identified by alternate ID.

Perform all the necessary checks and  returns all the notes for the device corresponding to alternate search type and device ID.  <br />  Notes can help better device management within deployment by specifying these against devices.

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
api_instance = mdmv1.NotesApi(mdmv1.ApiClient(configuration))
search_by = '' # str | The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837).(Required). (default to )
id = '' # str | Device alternate ID.(Required). (default to )

try:
    # Retrieves the notes for the device identified by alternate ID.
    api_response = api_instance.notes_get_device_notes_by_alternate_id_async(search_by, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_get_device_notes_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837).(Required). | [default to ]
 **id** | **str**| Device alternate ID.(Required). | [default to ]

### Return type

[**DeviceNotesSearchResult**](DeviceNotesSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_get_notes_by_device**
> DeviceNotesSearchResult notes_get_notes_by_device(id)

Retrieves the notes for the device identified by device ID.

Retrieves the notes which are added for the specified device identified by device ID.  <br />  Notes can help better device management within deployment by specifying these against devices.

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
api_instance = mdmv1.NotesApi(mdmv1.ApiClient(configuration))
id = 56 # int | Unique identifier used to identify device. (Required).

try:
    # Retrieves the notes for the device identified by device ID.
    api_response = api_instance.notes_get_notes_by_device(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_get_notes_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique identifier used to identify device. (Required). | 

### Return type

[**DeviceNotesSearchResult**](DeviceNotesSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_update_notes**
> EntityId notes_update_notes(device_id, note_id, device_notes)

Updates a note identified by note ID for the device identified by device ID.

Updates the existing note identified by note ID for the specified device identified by device ID.  <br />  Notes can help better device management within deployment by specifying these against devices.

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
api_instance = mdmv1.NotesApi(mdmv1.ApiClient(configuration))
device_id = 56 # int | Unique identifier used to identify device. (Required).
note_id = 56 # int | Unique identifier used to identify device note. (Required).
device_notes = mdmv1.DeviceNotes() # DeviceNotes | Device note to be updated against specified device. (Required).

try:
    # Updates a note identified by note ID for the device identified by device ID.
    api_response = api_instance.notes_update_notes(device_id, note_id, device_notes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_update_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Unique identifier used to identify device. (Required). | 
 **note_id** | **int**| Unique identifier used to identify device note. (Required). | 
 **device_notes** | [**DeviceNotes**](DeviceNotes.md)| Device note to be updated against specified device. (Required). | 

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_update_notes_by_alternate_id_async**
> notes_update_notes_by_alternate_id_async(note_id, device_notes, search_by, id)

Updates a note for the device identified by alternate ID.

Perform all the necessary checks and  updates the note corresponding to alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber].  <br />  Notes can help better device management within deployment by specifying these against devices.

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
api_instance = mdmv1.NotesApi(mdmv1.ApiClient(configuration))
note_id = 56 # int | The note ID.(Required).
device_notes = mdmv1.DeviceNotes() # DeviceNotes | Resource containing the note details.(Required).
search_by = '' # str | The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837).(Required). (default to )
id = '' # str | Device alternate ID.(Required). (default to )

try:
    # Updates a note for the device identified by alternate ID.
    api_instance.notes_update_notes_by_alternate_id_async(note_id, device_notes, search_by, id)
except ApiException as e:
    print("Exception when calling NotesApi->notes_update_notes_by_alternate_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| The note ID.(Required). | 
 **device_notes** | [**DeviceNotes**](DeviceNotes.md)| Resource containing the note details.(Required). | 
 **search_by** | **str**| The alternate ID type [Macaddress, Udid, Serialnumber, ImeiNumber]. (Formats: Macaddress: 848506B900BA, Udid: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837).(Required). | [default to ]
 **id** | **str**| Device alternate ID.(Required). | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

