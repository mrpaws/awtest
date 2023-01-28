# mamv1.SmartGroupApi

All URIs are relative to *https://awapi.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smart_group_add_internal_app_to_smart_group_async**](SmartGroupApi.md#smart_group_add_internal_app_to_smart_group_async) | **POST** /apps/internal/{applicationid}/smartgroups/{smartgroupid} | Assigns a Smart Group to an Internal Application.
[**smart_group_add_public_app_to_smart_group_async**](SmartGroupApi.md#smart_group_add_public_app_to_smart_group_async) | **POST** /apps/public/{applicationId}/smartgroups/{smartGroupId} | Assigns a Smart Group to an Public Application.
[**smart_group_delete_assignment_async**](SmartGroupApi.md#smart_group_delete_assignment_async) | **DELETE** /apps/purchased/{applicationid}/smartgroups/{smartgroupid} | Deletes smartgroup Assignment from a purchased application.
[**smart_group_remove_internal_app_from_smart_group_async**](SmartGroupApi.md#smart_group_remove_internal_app_from_smart_group_async) | **DELETE** /apps/internal/{applicationid}/smartgroups/{smartgroupid} | Removes the Smart Group Assignment from an Internal Application.
[**smart_group_remove_public_app_from_smart_group_async**](SmartGroupApi.md#smart_group_remove_public_app_from_smart_group_async) | **DELETE** /apps/public/{applicationid}/smartgroups/{smartgroupid} | Removes the Smart Group Assignment from a Public Application.


# **smart_group_add_internal_app_to_smart_group_async**
> smart_group_add_internal_app_to_smart_group_async(applicationid, smartgroupid)

Assigns a Smart Group to an Internal Application.

Assigns the smart group identified by the smartgroup id to the internal application.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.SmartGroupApi(mamv1.ApiClient(configuration))
applicationid = 56 # int | Application Id.
smartgroupid = 56 # int | SmartGroup Id.

try:
    # Assigns a Smart Group to an Internal Application.
    api_instance.smart_group_add_internal_app_to_smart_group_async(applicationid, smartgroupid)
except ApiException as e:
    print("Exception when calling SmartGroupApi->smart_group_add_internal_app_to_smart_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Application Id. | 
 **smartgroupid** | **int**| SmartGroup Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_group_add_public_app_to_smart_group_async**
> smart_group_add_public_app_to_smart_group_async(application_id, smart_group_id)

Assigns a Smart Group to an Public Application.

Assigns the smart group identified by the smartgroup id to the public application.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.SmartGroupApi(mamv1.ApiClient(configuration))
application_id = 56 # int | Application Id.
smart_group_id = 56 # int | SmartGroup Id.

try:
    # Assigns a Smart Group to an Public Application.
    api_instance.smart_group_add_public_app_to_smart_group_async(application_id, smart_group_id)
except ApiException as e:
    print("Exception when calling SmartGroupApi->smart_group_add_public_app_to_smart_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| Application Id. | 
 **smart_group_id** | **int**| SmartGroup Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_group_delete_assignment_async**
> smart_group_delete_assignment_async(applicationid, smartgroupid)

Deletes smartgroup Assignment from a purchased application.

Deletes the smart group assignment identified by the smartgroup id of the VPP application.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.SmartGroupApi(mamv1.ApiClient(configuration))
applicationid = 56 # int | Application Identifier.
smartgroupid = 56 # int | SmartGroup Identifier.

try:
    # Deletes smartgroup Assignment from a purchased application.
    api_instance.smart_group_delete_assignment_async(applicationid, smartgroupid)
except ApiException as e:
    print("Exception when calling SmartGroupApi->smart_group_delete_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Application Identifier. | 
 **smartgroupid** | **int**| SmartGroup Identifier. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_group_remove_internal_app_from_smart_group_async**
> smart_group_remove_internal_app_from_smart_group_async(applicationid, smartgroupid)

Removes the Smart Group Assignment from an Internal Application.

Removes the assignment identified by the smartgroup id for the internal application.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.SmartGroupApi(mamv1.ApiClient(configuration))
applicationid = 56 # int | Application Id.
smartgroupid = 56 # int | SmartGroup Id.

try:
    # Removes the Smart Group Assignment from an Internal Application.
    api_instance.smart_group_remove_internal_app_from_smart_group_async(applicationid, smartgroupid)
except ApiException as e:
    print("Exception when calling SmartGroupApi->smart_group_remove_internal_app_from_smart_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Application Id. | 
 **smartgroupid** | **int**| SmartGroup Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_group_remove_public_app_from_smart_group_async**
> smart_group_remove_public_app_from_smart_group_async(applicationid, smartgroupid)

Removes the Smart Group Assignment from a Public Application.

1. Removes the assignment identified by the smartgroup id for the public application  2. Excluded Assignment Groups are only available for viewing in the GET call.     Option to edit them is not currently available through POST/PUT APIs.  3. DELETE API however deletes any SG ID associated with an application, assigned or excluded.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.SmartGroupApi(mamv1.ApiClient(configuration))
applicationid = 56 # int | Application Id.
smartgroupid = 56 # int | SmartGroup Id.

try:
    # Removes the Smart Group Assignment from a Public Application.
    api_instance.smart_group_remove_public_app_from_smart_group_async(applicationid, smartgroupid)
except ApiException as e:
    print("Exception when calling SmartGroupApi->smart_group_remove_public_app_from_smart_group_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Application Id. | 
 **smartgroupid** | **int**| SmartGroup Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

