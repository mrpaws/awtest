# mamv1.InternalAppsV1Api

All URIs are relative to *https://awapi.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**internal_apps_v1_activate_internal_app_async**](InternalAppsV1Api.md#internal_apps_v1_activate_internal_app_async) | **POST** /apps/internal/{applicationid}/activate | Activates the specified internal application.
[**internal_apps_v1_add_assignments_with_flexible_deployment_parameters_async**](InternalAppsV1Api.md#internal_apps_v1_add_assignments_with_flexible_deployment_parameters_async) | **POST** /apps/internal/{applicationId}/assignments | Adds assignments along with the flexible deplyment parameters to an internal application.
[**internal_apps_v1_application_bulk_action_on_devices**](InternalAppsV1Api.md#internal_apps_v1_application_bulk_action_on_devices) | **POST** /apps/internal/devices | New - Applications actions (install, remove) for bulk devices
[**internal_apps_v1_create_internal_app_from_blob_async**](InternalAppsV1Api.md#internal_apps_v1_create_internal_app_from_blob_async) | **POST** /apps/internal/begininstall | Creates an internal application.
[**internal_apps_v1_create_internal_application_from_blob**](InternalAppsV1Api.md#internal_apps_v1_create_internal_application_from_blob) | **POST** /apps/internal/application | Creates an internal application.
[**internal_apps_v1_deactivate_internal_app_async**](InternalAppsV1Api.md#internal_apps_v1_deactivate_internal_app_async) | **POST** /apps/internal/{applicationid}/deactivate | Deactivates the specified internal application.
[**internal_apps_v1_delete_assignment_async**](InternalAppsV1Api.md#internal_apps_v1_delete_assignment_async) | **DELETE** /apps/internal/{applicationId}/assignments | Deletes Application Assignment to Smart Group(s).
[**internal_apps_v1_delete_internal_app_async**](InternalAppsV1Api.md#internal_apps_v1_delete_internal_app_async) | **DELETE** /apps/internal/{applicationid} | Deletes the specified internal application.
[**internal_apps_v1_delete_windows_app_dependency**](InternalAppsV1Api.md#internal_apps_v1_delete_windows_app_dependency) | **DELETE** /apps/internal/windowsappdependency/{windowsAppDependencyId} | New - Deletes the windows dependency application specified by id.
[**internal_apps_v1_edit_assignments_with_flexible_deployment_parameters_async**](InternalAppsV1Api.md#internal_apps_v1_edit_assignments_with_flexible_deployment_parameters_async) | **PUT** /apps/internal/{applicationId}/assignments | Edits assignments along with the flexible deployment parameters associated with an internal application.
[**internal_apps_v1_get_application_summary**](InternalAppsV1Api.md#internal_apps_v1_get_application_summary) | **GET** /apps/internal/summary | New - Gets the summary of the internal application uniquely identified by the bundle id, organization group uuid, and device type.
[**internal_apps_v1_get_devices_assigned_or_installed_for_app_at_app_level**](InternalAppsV1Api.md#internal_apps_v1_get_devices_assigned_or_installed_for_app_at_app_level) | **GET** /apps/internal/devices | New - Gets list of devices that have the specified internal application installed or assigned at the application level.
[**internal_apps_v1_get_internal_app_by_id_async**](InternalAppsV1Api.md#internal_apps_v1_get_internal_app_by_id_async) | **GET** /apps/internal/{applicationId} | New - Details of an internal app identified by id.
[**internal_apps_v1_get_internal_app_install_counts**](InternalAppsV1Api.md#internal_apps_v1_get_internal_app_install_counts) | **GET** /apps/internal/installcounts | New - Gets the installation counts for an internal app across versions
[**internal_apps_v1_get_internal_app_installed_or_assigned_devices**](InternalAppsV1Api.md#internal_apps_v1_get_internal_app_installed_or_assigned_devices) | **GET** /apps/internal/{applicationid}/devices | Gets list of devices that have the specified internal application installed or assigned.
[**internal_apps_v1_get_internal_app_reason_breakdown_counts**](InternalAppsV1Api.md#internal_apps_v1_get_internal_app_reason_breakdown_counts) | **GET** /apps/internal/reasonbreakdowncounts | New - Gets the device count for the application reasons
[**internal_apps_v1_get_internal_app_status_async**](InternalAppsV1Api.md#internal_apps_v1_get_internal_app_status_async) | **GET** /apps/internal/{applicationid}/status | Status of the specified internal application on a device.
[**internal_apps_v1_get_windows_app_dependancies_by_location_group_id**](InternalAppsV1Api.md#internal_apps_v1_get_windows_app_dependancies_by_location_group_id) | **GET** /apps/internal/windowsappdependencies/{organizationGroupId} | Gets the list of saved windows app dependency files for current OG and child OGs.
[**internal_apps_v1_get_windows_app_dependency_by_id**](InternalAppsV1Api.md#internal_apps_v1_get_windows_app_dependency_by_id) | **GET** /apps/internal/windowsappdependency/{windowsAppDependencyId} | Gets the details of an windows app dependency identified by id.
[**internal_apps_v1_insert_internal_application_chunk**](InternalAppsV1Api.md#internal_apps_v1_insert_internal_application_chunk) | **POST** /apps/internal/uploadchunk | Uploads the chunk data.
[**internal_apps_v1_install_internal_app_on_device_async**](InternalAppsV1Api.md#internal_apps_v1_install_internal_app_on_device_async) | **POST** /apps/internal/{applicationid}/install | Installs the specified internal application on a device.
[**internal_apps_v1_remove_internal_app_from_device_async**](InternalAppsV1Api.md#internal_apps_v1_remove_internal_app_from_device_async) | **POST** /apps/internal/{applicationid}/uninstall | Uninstalls the specified internal application from a device.
[**internal_apps_v1_retire_app_async**](InternalAppsV1Api.md#internal_apps_v1_retire_app_async) | **POST** /apps/internal/{applicationid}/retire | Retires the specified Internal application.
[**internal_apps_v1_retrieve_app_versions_async**](InternalAppsV1Api.md#internal_apps_v1_retrieve_app_versions_async) | **GET** /apps/internal/{bundleId}/{deviceType}/versions | New - Retrieves the versions of this app assigned at this Organization Group.
[**internal_apps_v1_un_retire_app_async**](InternalAppsV1Api.md#internal_apps_v1_un_retire_app_async) | **POST** /apps/internal/{applicationid}/unretire | Unretires the specified internal application.
[**internal_apps_v1_update_internal_app**](InternalAppsV1Api.md#internal_apps_v1_update_internal_app) | **PUT** /apps/internal/{applicationId} | Updates the internal application.


# **internal_apps_v1_activate_internal_app_async**
> internal_apps_v1_activate_internal_app_async(applicationid)

Activates the specified internal application.

Activates all versions of the internal application specified by ID.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | The Id integer of the application.(Required).

try:
    # Activates the specified internal application.
    api_instance.internal_apps_v1_activate_internal_app_async(applicationid)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_activate_internal_app_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The Id integer of the application.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_add_assignments_with_flexible_deployment_parameters_async**
> internal_apps_v1_add_assignments_with_flexible_deployment_parameters_async(application_id, application_assignments=application_assignments)

Adds assignments along with the flexible deplyment parameters to an internal application.

1. Adds assignments and returns a resource containing the transaction details  2. Excluded Assignment Groups are only available for viewing in the GET call.     Option to edit them is not currently available through POST/PUT APIs.  3. DELETE API however deletes any SG ID associated with an application, assigned or excluded.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
application_id = 56 # int | Internal Application Id.
application_assignments = mamv1.ApplicationAssignmentsModel_() # ApplicationAssignmentsModel_ | Application Assignments Model. (optional)

try:
    # Adds assignments along with the flexible deplyment parameters to an internal application.
    api_instance.internal_apps_v1_add_assignments_with_flexible_deployment_parameters_async(application_id, application_assignments=application_assignments)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_add_assignments_with_flexible_deployment_parameters_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| Internal Application Id. | 
 **application_assignments** | [**ApplicationAssignmentsModel_**](ApplicationAssignmentsModel_.md)| Application Assignments Model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_application_bulk_action_on_devices**
> internal_apps_v1_application_bulk_action_on_devices(filter_criteria, action)

New - Applications actions (install, remove) for bulk devices

This API performs applications actions (install, remove) for a set of devices. Set of devices will be passed as part of filter critera or it can be an individual device and app identifier combination. User needs to pass either filter criteria or individual device and app identifier combination. If user passes an individual device and app idenifier combination then filter criteria will be ignored.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
filter_criteria = mamv1.ApplicationDevicesSearchCriteriaModel() # ApplicationDevicesSearchCriteriaModel | Contains the filter criteria and a list of individual device and app identifier combinations. User can get the list of devices which is eligible to perfom the bulk actions(Install, remove).(Required)
action =  # object | The bulk action that we are going to perform(Required) (default to )

try:
    # New - Applications actions (install, remove) for bulk devices
    api_instance.internal_apps_v1_application_bulk_action_on_devices(filter_criteria, action)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_application_bulk_action_on_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_criteria** | [**ApplicationDevicesSearchCriteriaModel**](ApplicationDevicesSearchCriteriaModel.md)| Contains the filter criteria and a list of individual device and app identifier combinations. User can get the list of devices which is eligible to perfom the bulk actions(Install, remove).(Required) | 
 **action** | [**object**](.md)| The bulk action that we are going to perform(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_create_internal_app_from_blob_async**
> InternalApplicationEntity_ internal_apps_v1_create_internal_app_from_blob_async(app_chunk_transaction=app_chunk_transaction)

Creates an internal application.

1. Creates an internal application using the uploaded file chunks.  2. If application is added through link and downloadfilefromlink is set to true then UploadViaLink should be set to false.  3. ActualFileVersion in API is same as App version on the UI; AppVersion in API is UEM Version on the UI.  4. BundleId And ActualFileVersion Are required when the app is uploaded via link.  5. If UploadViaLink is false, TransactionId or BlobId is required.  6. Use '/internal/application' API endpoint for using 4th decimal in applications.  7. If AppVersion is not passed, it is parsed from the ActualFileVersion (0 for the decimal places it cannot parse).  8. For windows SFD apps of format exe and zip, admin can pass 'ActualFileVersion' even when UploadViaLink is False.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
app_chunk_transaction = mamv1.InternalAppChunkTransaction_() # InternalAppChunkTransaction_ | The chunk details of the application. (optional)

try:
    # Creates an internal application.
    api_response = api_instance.internal_apps_v1_create_internal_app_from_blob_async(app_chunk_transaction=app_chunk_transaction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_create_internal_app_from_blob_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_chunk_transaction** | [**InternalAppChunkTransaction_**](InternalAppChunkTransaction_.md)| The chunk details of the application. | [optional] 

### Return type

[**InternalApplicationEntity_**](InternalApplicationEntity_.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_create_internal_application_from_blob**
> InternalApplicationEntity_ internal_apps_v1_create_internal_application_from_blob(internal_app_chunk_transaction=internal_app_chunk_transaction)

Creates an internal application.

1. Creates an internal application using the uploaded file chunks. Will return the ApplicationEntity for newly created internal application.  2. If application is added through link and downloadfilefromlink is set to true then upload_via_link should be set to false.  3. actual_file_version is same as App version on the UI; app_uem_Version on the API is UEM Version on the UI.  4. bundle_id and actual_file_version are required when the app is uploaded via link.  5. If upload_via_link is false, transaction_id or blob_id is required.  6. If app_uem_version is not passed, it is parsed from the actual_file_version (0 for the decimal places it cannot parse).  7. For Windows SFD apps of format exe and zip, admin can pass 'actual_file_version' even when upload_via_link is False.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
internal_app_chunk_transaction = mamv1.InternalAppChunkTransactionV1Model() # InternalAppChunkTransactionV1Model | The chunk details of the application. (optional)

try:
    # Creates an internal application.
    api_response = api_instance.internal_apps_v1_create_internal_application_from_blob(internal_app_chunk_transaction=internal_app_chunk_transaction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_create_internal_application_from_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_app_chunk_transaction** | [**InternalAppChunkTransactionV1Model**](InternalAppChunkTransactionV1Model.md)| The chunk details of the application. | [optional] 

### Return type

[**InternalApplicationEntity_**](InternalApplicationEntity_.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_deactivate_internal_app_async**
> internal_apps_v1_deactivate_internal_app_async(applicationid)

Deactivates the specified internal application.

Deactivates all versions of the Internal Application identified by the passed Application ID.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | Application Id.

try:
    # Deactivates the specified internal application.
    api_instance.internal_apps_v1_deactivate_internal_app_async(applicationid)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_deactivate_internal_app_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| Application Id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_delete_assignment_async**
> internal_apps_v1_delete_assignment_async(application_id, application_delete_assignment_model=application_delete_assignment_model)

Deletes Application Assignment to Smart Group(s).

1. Deletes a given smart group assignment for an internal app specified by id.  2. Excluded Assignment Groups are only available for viewing in the GET call.     Option to edit them is not currently available through POST/PUT APIs.  3. DELETE API however deletes any SG ID associated with an application, assigned or excluded.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
application_id = 56 # int | The Id integer of the application.(Required).
application_delete_assignment_model = mamv1.ApplicationDeleteAssignmentModel() # ApplicationDeleteAssignmentModel | Application assignment to be deleted. (optional)

try:
    # Deletes Application Assignment to Smart Group(s).
    api_instance.internal_apps_v1_delete_assignment_async(application_id, application_delete_assignment_model=application_delete_assignment_model)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_delete_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The Id integer of the application.(Required). | 
 **application_delete_assignment_model** | [**ApplicationDeleteAssignmentModel**](ApplicationDeleteAssignmentModel.md)| Application assignment to be deleted. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_delete_internal_app_async**
> internal_apps_v1_delete_internal_app_async(applicationid)

Deletes the specified internal application.

Deletes the Selected internal application.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | The Id integer of the internal app to be deleted. (Required).

try:
    # Deletes the specified internal application.
    api_instance.internal_apps_v1_delete_internal_app_async(applicationid)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_delete_internal_app_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The Id integer of the internal app to be deleted. (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_delete_windows_app_dependency**
> internal_apps_v1_delete_windows_app_dependency(windows_app_dependency_id)

New - Deletes the windows dependency application specified by id.

Deletes windows dependency application specified by id.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
windows_app_dependency_id = 56 # int | The Id integer of the dependency to be deleted. (Required).

try:
    # New - Deletes the windows dependency application specified by id.
    api_instance.internal_apps_v1_delete_windows_app_dependency(windows_app_dependency_id)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_delete_windows_app_dependency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **windows_app_dependency_id** | **int**| The Id integer of the dependency to be deleted. (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_edit_assignments_with_flexible_deployment_parameters_async**
> internal_apps_v1_edit_assignments_with_flexible_deployment_parameters_async(application_id, application_assignments=application_assignments)

Edits assignments along with the flexible deployment parameters associated with an internal application.

1. Updates the assignments for internal application.  2. Excluded Assignment Groups are only available for viewing in the GET call.     Option to edit them is not currently available through POST/PUT APIs.  3. DELETE API however deletes any SG ID associated with an application, assigned or excluded.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
application_id = 56 # int | Internal Application Id.
application_assignments = mamv1.ApplicationAssignmentsModel_() # ApplicationAssignmentsModel_ | Application Assignments Model. (optional)

try:
    # Edits assignments along with the flexible deployment parameters associated with an internal application.
    api_instance.internal_apps_v1_edit_assignments_with_flexible_deployment_parameters_async(application_id, application_assignments=application_assignments)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_edit_assignments_with_flexible_deployment_parameters_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| Internal Application Id. | 
 **application_assignments** | [**ApplicationAssignmentsModel_**](ApplicationAssignmentsModel_.md)| Application Assignments Model. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_get_application_summary**
> ApplicationSummaryModel internal_apps_v1_get_application_summary(bundleid, apporganizationgroupuuid, devicetype, organizationgroupuuid=organizationgroupuuid)

New - Gets the summary of the internal application uniquely identified by the bundle id, organization group uuid, and device type.

This endpoint provides the basic details of an internal application at the application bundle identifier level.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
bundleid = '' # str | The bundle identifier of the application(Required) (default to )
apporganizationgroupuuid =  # object | Uuid of the Organization Group from where the app is uploaded(Required) (default to )
devicetype =  # object | The platform of the application, the possible values are [ AppleTv, Apple, Android, WindowsPhone8, AppleOsX, WinRT ](Required) (default to )
organizationgroupuuid =  # object | Uuid of the Organization Group from where the app is accessed (optional) (default to )

try:
    # New - Gets the summary of the internal application uniquely identified by the bundle id, organization group uuid, and device type.
    api_response = api_instance.internal_apps_v1_get_application_summary(bundleid, apporganizationgroupuuid, devicetype, organizationgroupuuid=organizationgroupuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_get_application_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundleid** | **str**| The bundle identifier of the application(Required) | [default to ]
 **apporganizationgroupuuid** | [**object**](.md)| Uuid of the Organization Group from where the app is uploaded(Required) | [default to ]
 **devicetype** | [**object**](.md)| The platform of the application, the possible values are [ AppleTv, Apple, Android, WindowsPhone8, AppleOsX, WinRT ](Required) | [default to ]
 **organizationgroupuuid** | [**object**](.md)| Uuid of the Organization Group from where the app is accessed | [optional] [default to ]

### Return type

[**ApplicationSummaryModel**](ApplicationSummaryModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_get_devices_assigned_or_installed_for_app_at_app_level**
> DevicesPagedSearchResultsModel internal_apps_v1_get_devices_assigned_or_installed_for_app_at_app_level(bundleid, devicetype, apporganizationgroupuuid, page=page, pagesize=pagesize, searchtext=searchtext, sortorder=sortorder, orderby=orderby, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids, isassigned=isassigned, isnotassigned=isnotassigned, isexcluded=isexcluded, isinstalledversionequaltoassigned=isinstalledversionequaltoassigned, isinstalledversionnotequaltoassigned=isinstalledversionnotequaltoassigned, isversionnotinstalled=isversionnotinstalled, installationstatus=installationstatus, lastactiontaken=lastactiontaken, peerdistributionstatus=peerdistributionstatus)

New - Gets list of devices that have the specified internal application installed or assigned at the application level.

This endpoint provides a list of devices that have the specified internal application installed or assigned at the application level. A list of all the assigned devices is returned by default.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
bundleid = '' # str | The bundle identifier of the application. E.g. com.airwatch.androidagent(Required) (default to )
devicetype =  # object | The platform of the application, the possible values are [ AppleTv, Apple, Android, WindowsPhone8, AppleOsX, WinRT ](Required) (default to )
apporganizationgroupuuid =  # object | The Organization Group id in which the app was created. E.g. EF331D65-C005-4388-8E52-B1390AA171D9(Required) (default to )
page = 56 # int | Page number which will be fetched, 0 based index. Default 0. (optional)
pagesize = 56 # int | Maximum number of results to be returned in one page. Default 500. (optional)
searchtext = '' # str | If provided, the records matching this text will be returned. The search will be applied on the following properties [name, installed_version, assigned_version]. The default value will be empty string. (optional) (default to )
sortorder = '' # str | Whether the sort order is ascending or descending. The property used for sorting is name. Possible values [Asc, Desc]. Default value is Asc. (optional) (default to )
orderby = '' # str | Name of the column used for sorting (optional) (default to )
organizationgroupuuid =  # object | The Organization Group identifier where the list of devices need to be fetched. If not set it will be defaulted to admin location group identifier. (optional) (default to )
smartgroupuuids =  # object | Comma separated list of smart group ids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. C961E60C-0283-4A43-AA1E-9A49369C0944, C961E60C-0283-4A43-AA1E-9A49369C0945 (optional) (default to )
isassigned =  # bool | If provided, the list of devices on which the app is assigned is included in the returned result set. Default false. (optional) (default to )
isnotassigned =  # bool | If provided, the list of devices on which the app is sideloaded or marked for removal but not assigned is included in the returned result set. Default false. (optional) (default to )
isexcluded =  # bool | If provided, the list of devices on which the app is excluded is included in the returned result set. Default false. (optional) (default to )
isinstalledversionequaltoassigned =  # bool | if provided, the list of devices where the installed version of the internal app is the same as the assigned version is returned. Default false. (optional) (default to )
isinstalledversionnotequaltoassigned =  # bool | if provided, the list of devices where the installed version of the internal app is not the same as the assigned version is returned. Default false. (optional) (default to )
isversionnotinstalled =  # bool | if provided, the list of devices on which the internal app is assigned but not installed is returned. Default false. (optional) (default to )
installationstatus =  # object | Comma separated list of managed application list reasons to which the devices assigned to the app belong. If no reason is passed, all the assigned devices will be returned based on the other filters. (optional) (default to )
lastactiontaken =  # object | Comma separated list of application deployment status to which the devices assigned to the app belong. If no deployment status is passed, all the assigned devices will be returned based on the other filters. (optional) (default to )
peerdistributionstatus =  # object | Comma separated list of peer distribution status to which the devices assigned to the app belong. If no peer distribution status is passed, all the assigned devices will be returned based on the other filters. (optional) (default to )

try:
    # New - Gets list of devices that have the specified internal application installed or assigned at the application level.
    api_response = api_instance.internal_apps_v1_get_devices_assigned_or_installed_for_app_at_app_level(bundleid, devicetype, apporganizationgroupuuid, page=page, pagesize=pagesize, searchtext=searchtext, sortorder=sortorder, orderby=orderby, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids, isassigned=isassigned, isnotassigned=isnotassigned, isexcluded=isexcluded, isinstalledversionequaltoassigned=isinstalledversionequaltoassigned, isinstalledversionnotequaltoassigned=isinstalledversionnotequaltoassigned, isversionnotinstalled=isversionnotinstalled, installationstatus=installationstatus, lastactiontaken=lastactiontaken, peerdistributionstatus=peerdistributionstatus)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_get_devices_assigned_or_installed_for_app_at_app_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundleid** | **str**| The bundle identifier of the application. E.g. com.airwatch.androidagent(Required) | [default to ]
 **devicetype** | [**object**](.md)| The platform of the application, the possible values are [ AppleTv, Apple, Android, WindowsPhone8, AppleOsX, WinRT ](Required) | [default to ]
 **apporganizationgroupuuid** | [**object**](.md)| The Organization Group id in which the app was created. E.g. EF331D65-C005-4388-8E52-B1390AA171D9(Required) | [default to ]
 **page** | **int**| Page number which will be fetched, 0 based index. Default 0. | [optional] 
 **pagesize** | **int**| Maximum number of results to be returned in one page. Default 500. | [optional] 
 **searchtext** | **str**| If provided, the records matching this text will be returned. The search will be applied on the following properties [name, installed_version, assigned_version]. The default value will be empty string. | [optional] [default to ]
 **sortorder** | **str**| Whether the sort order is ascending or descending. The property used for sorting is name. Possible values [Asc, Desc]. Default value is Asc. | [optional] [default to ]
 **orderby** | **str**| Name of the column used for sorting | [optional] [default to ]
 **organizationgroupuuid** | [**object**](.md)| The Organization Group identifier where the list of devices need to be fetched. If not set it will be defaulted to admin location group identifier. | [optional] [default to ]
 **smartgroupuuids** | [**object**](.md)| Comma separated list of smart group ids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. C961E60C-0283-4A43-AA1E-9A49369C0944, C961E60C-0283-4A43-AA1E-9A49369C0945 | [optional] [default to ]
 **isassigned** | **bool**| If provided, the list of devices on which the app is assigned is included in the returned result set. Default false. | [optional] [default to ]
 **isnotassigned** | **bool**| If provided, the list of devices on which the app is sideloaded or marked for removal but not assigned is included in the returned result set. Default false. | [optional] [default to ]
 **isexcluded** | **bool**| If provided, the list of devices on which the app is excluded is included in the returned result set. Default false. | [optional] [default to ]
 **isinstalledversionequaltoassigned** | **bool**| if provided, the list of devices where the installed version of the internal app is the same as the assigned version is returned. Default false. | [optional] [default to ]
 **isinstalledversionnotequaltoassigned** | **bool**| if provided, the list of devices where the installed version of the internal app is not the same as the assigned version is returned. Default false. | [optional] [default to ]
 **isversionnotinstalled** | **bool**| if provided, the list of devices on which the internal app is assigned but not installed is returned. Default false. | [optional] [default to ]
 **installationstatus** | [**object**](.md)| Comma separated list of managed application list reasons to which the devices assigned to the app belong. If no reason is passed, all the assigned devices will be returned based on the other filters. | [optional] [default to ]
 **lastactiontaken** | [**object**](.md)| Comma separated list of application deployment status to which the devices assigned to the app belong. If no deployment status is passed, all the assigned devices will be returned based on the other filters. | [optional] [default to ]
 **peerdistributionstatus** | [**object**](.md)| Comma separated list of peer distribution status to which the devices assigned to the app belong. If no peer distribution status is passed, all the assigned devices will be returned based on the other filters. | [optional] [default to ]

### Return type

[**DevicesPagedSearchResultsModel**](DevicesPagedSearchResultsModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_get_internal_app_by_id_async**
> InternalAppModel internal_apps_v1_get_internal_app_by_id_async(application_id)

New - Details of an internal app identified by id.

 1. Gets the details of an internal app identified by id.  2. Excluded assignment groups are only available for viewing in the GET call.     Option to edit them is not currently available through POST/PUT APIs.  3. DELETE API however deletes any smart group ID associated with an application, assigned or excluded.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
application_id = 56 # int | Internal application id(Required).

try:
    # New - Details of an internal app identified by id.
    api_response = api_instance.internal_apps_v1_get_internal_app_by_id_async(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_get_internal_app_by_id_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| Internal application id(Required). | 

### Return type

[**InternalAppModel**](InternalAppModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_get_internal_app_install_counts**
> InternalAppCountModel internal_apps_v1_get_internal_app_install_counts(bundleid, apporganizationgroupuuid, devicetype, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids)

New - Gets the installation counts for an internal app across versions

 Will return the following information for each version of the internal application in the provided organization group  1. Total assigned count  2. Total installed count  3. Total side loaded count

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
bundleid = '' # str | The bundle identifier of the application(Required) (default to )
apporganizationgroupuuid =  # object | The organization group identifer where application has been uploaded.(Required) (default to )
devicetype =  # object | The platform of the application, the possible values are [ AppleTv, Apple, Android, WindowsPhone8, AppleOsX, WinRT ](Required) (default to )
organizationgroupuuid =  # object | The organization group identifier where the counts need to be fetched. If not set it will be defaulted to admin location group identifier. (optional) (default to )
smartgroupuuids =  # object | Comma separated list of smart group ids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. C961E60C-0283-4A43-AA1E-9A49369C0944, C961E60C-0283-4A43-AA1E-9A49369C0945 (optional) (default to )

try:
    # New - Gets the installation counts for an internal app across versions
    api_response = api_instance.internal_apps_v1_get_internal_app_install_counts(bundleid, apporganizationgroupuuid, devicetype, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_get_internal_app_install_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundleid** | **str**| The bundle identifier of the application(Required) | [default to ]
 **apporganizationgroupuuid** | [**object**](.md)| The organization group identifer where application has been uploaded.(Required) | [default to ]
 **devicetype** | [**object**](.md)| The platform of the application, the possible values are [ AppleTv, Apple, Android, WindowsPhone8, AppleOsX, WinRT ](Required) | [default to ]
 **organizationgroupuuid** | [**object**](.md)| The organization group identifier where the counts need to be fetched. If not set it will be defaulted to admin location group identifier. | [optional] [default to ]
 **smartgroupuuids** | [**object**](.md)| Comma separated list of smart group ids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. C961E60C-0283-4A43-AA1E-9A49369C0944, C961E60C-0283-4A43-AA1E-9A49369C0945 | [optional] [default to ]

### Return type

[**InternalAppCountModel**](InternalAppCountModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_get_internal_app_installed_or_assigned_devices**
> DeviceList internal_apps_v1_get_internal_app_installed_or_assigned_devices(applicationid, status=status, locationgroupid=locationgroupid, page=page, pagesize=pagesize)

Gets list of devices that have the specified internal application installed or assigned.

Provides a list of devices that have the specified internal application installed or assigned. Provides a list of assigned devices by default when the status is not specified.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | The Id integer of the application.(Required).
status = '' # str | Status of the given application on the device - installed/assigned. (optional) (default to )
locationgroupid = '' # str | The Id integer of the LocationGroup, for example - 7. (optional) (default to )
page = '' # str | Specific page number to get. 0 based index. (optional) (default to )
pagesize = '' # str | Maximumm records per page. Default 500. (optional) (default to )

try:
    # Gets list of devices that have the specified internal application installed or assigned.
    api_response = api_instance.internal_apps_v1_get_internal_app_installed_or_assigned_devices(applicationid, status=status, locationgroupid=locationgroupid, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_get_internal_app_installed_or_assigned_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The Id integer of the application.(Required). | 
 **status** | **str**| Status of the given application on the device - installed/assigned. | [optional] [default to ]
 **locationgroupid** | **str**| The Id integer of the LocationGroup, for example - 7. | [optional] [default to ]
 **page** | **str**| Specific page number to get. 0 based index. | [optional] [default to ]
 **pagesize** | **str**| Maximumm records per page. Default 500. | [optional] [default to ]

### Return type

[**DeviceList**](DeviceList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_get_internal_app_reason_breakdown_counts**
> AppReasonBreakDownModel internal_apps_v1_get_internal_app_reason_breakdown_counts(bundleid, apporganizationgroupuuid, devicetype, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids)

New - Gets the device count for the application reasons

Will return the device count per application reason for all the versions of the app

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
bundleid = '' # str | The bundle identifier of the application(Required) (default to )
apporganizationgroupuuid =  # object | The Organization Group identifier where application has been uploaded.(Required) (default to )
devicetype =  # object | The platform of the application, the possible values are [ AppleTv, Apple, Android, WindowsPhone8, AppleOsX, WinRT ](Required) (default to )
organizationgroupuuid =  # object | The Organization Group identifier where the counts need to be fetched. If not set it will be defaulted to admin location group identifier. (optional) (default to )
smartgroupuuids =  # object | Comma separated list of smart group ids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. C961E60C-0283-4A43-AA1E-9A49369C0944, C961E60C-0283-4A43-AA1E-9A49369C0944 (optional) (default to )

try:
    # New - Gets the device count for the application reasons
    api_response = api_instance.internal_apps_v1_get_internal_app_reason_breakdown_counts(bundleid, apporganizationgroupuuid, devicetype, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_get_internal_app_reason_breakdown_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundleid** | **str**| The bundle identifier of the application(Required) | [default to ]
 **apporganizationgroupuuid** | [**object**](.md)| The Organization Group identifier where application has been uploaded.(Required) | [default to ]
 **devicetype** | [**object**](.md)| The platform of the application, the possible values are [ AppleTv, Apple, Android, WindowsPhone8, AppleOsX, WinRT ](Required) | [default to ]
 **organizationgroupuuid** | [**object**](.md)| The Organization Group identifier where the counts need to be fetched. If not set it will be defaulted to admin location group identifier. | [optional] [default to ]
 **smartgroupuuids** | [**object**](.md)| Comma separated list of smart group ids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. C961E60C-0283-4A43-AA1E-9A49369C0944, C961E60C-0283-4A43-AA1E-9A49369C0944 | [optional] [default to ]

### Return type

[**AppReasonBreakDownModel**](AppReasonBreakDownModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_get_internal_app_status_async**
> str internal_apps_v1_get_internal_app_status_async(applicationid, deviceid=deviceid, macaddress=macaddress, serialnumber=serialnumber, udid=udid)

Status of the specified internal application on a device.

Indicates the status of the specified internal application on a device.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | The integer id of the application.(Required).
deviceid = '' # str | Device Identifier, for example - 0dfe4a6f25647b8297c15b6a995fa985. (optional) (default to )
macaddress = '' # str | Device MAC address, for example - 0x848506B900BA. (optional) (default to )
serialnumber = '' # str | Device SerialNumber, for example - LGH871c18f631a. (optional) (default to )
udid = '' # str | Device UDID, for example - 6bf0f04c73681fbecfc3eb4f13cbf05b. (optional) (default to )

try:
    # Status of the specified internal application on a device.
    api_response = api_instance.internal_apps_v1_get_internal_app_status_async(applicationid, deviceid=deviceid, macaddress=macaddress, serialnumber=serialnumber, udid=udid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_get_internal_app_status_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The integer id of the application.(Required). | 
 **deviceid** | **str**| Device Identifier, for example - 0dfe4a6f25647b8297c15b6a995fa985. | [optional] [default to ]
 **macaddress** | **str**| Device MAC address, for example - 0x848506B900BA. | [optional] [default to ]
 **serialnumber** | **str**| Device SerialNumber, for example - LGH871c18f631a. | [optional] [default to ]
 **udid** | **str**| Device UDID, for example - 6bf0f04c73681fbecfc3eb4f13cbf05b. | [optional] [default to ]

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_get_windows_app_dependancies_by_location_group_id**
> list[WindowsAppDependencyModel] internal_apps_v1_get_windows_app_dependancies_by_location_group_id(organization_group_id)

Gets the list of saved windows app dependency files for current OG and child OGs.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
organization_group_id = 56 # int | Organization Group Id.

try:
    # Gets the list of saved windows app dependency files for current OG and child OGs.
    api_response = api_instance.internal_apps_v1_get_windows_app_dependancies_by_location_group_id(organization_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_get_windows_app_dependancies_by_location_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_id** | **int**| Organization Group Id. | 

### Return type

[**list[WindowsAppDependencyModel]**](WindowsAppDependencyModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_get_windows_app_dependency_by_id**
> WindowsAppDependencyModel internal_apps_v1_get_windows_app_dependency_by_id(windows_app_dependency_id)

Gets the details of an windows app dependency identified by id.

Loads Dependency Application Details and deployment options set in an application.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
windows_app_dependency_id = 56 # int | Windows app dependency id.

try:
    # Gets the details of an windows app dependency identified by id.
    api_response = api_instance.internal_apps_v1_get_windows_app_dependency_by_id(windows_app_dependency_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_get_windows_app_dependency_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **windows_app_dependency_id** | **int**| Windows app dependency id. | 

### Return type

[**WindowsAppDependencyModel**](WindowsAppDependencyModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_insert_internal_application_chunk**
> AppChunkTranscationResponse internal_apps_v1_insert_internal_application_chunk(internal_app_chunk=internal_app_chunk)

Uploads the chunk data.

Uploads the chunk data of an internal application into the server. A chunk of the application will contain the size of the chunk, sequence number, and the byte data.  The transaction ID should be null during the initial call to the API and the subsequent calls to the API should be made using the transaction ID from the response of the previous call  For uploading an application above 2 Gigabyte in size, File Storage needs to be configured.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
internal_app_chunk = mamv1.InternalAppChunk() # InternalAppChunk | The internal app chunk. (optional)

try:
    # Uploads the chunk data.
    api_response = api_instance.internal_apps_v1_insert_internal_application_chunk(internal_app_chunk=internal_app_chunk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_insert_internal_application_chunk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_app_chunk** | [**InternalAppChunk**](InternalAppChunk.md)| The internal app chunk. | [optional] 

### Return type

[**AppChunkTranscationResponse**](AppChunkTranscationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_install_internal_app_on_device_async**
> internal_apps_v1_install_internal_app_on_device_async(applicationid, device_info=device_info)

Installs the specified internal application on a device.

Installs the specified Internal application on a particular device.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 'applicationid_example' # str | The Id of the Application to be installed.
device_info = mamv1.DeviceInfo() # DeviceInfo | The details of the device to install the application on. (optional)

try:
    # Installs the specified internal application on a device.
    api_instance.internal_apps_v1_install_internal_app_on_device_async(applicationid, device_info=device_info)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_install_internal_app_on_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **str**| The Id of the Application to be installed. | 
 **device_info** | [**DeviceInfo**](DeviceInfo.md)| The details of the device to install the application on. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_remove_internal_app_from_device_async**
> internal_apps_v1_remove_internal_app_from_device_async(applicationid, device_info=device_info)

Uninstalls the specified internal application from a device.

Uninstalls the internal application specified by given id from a device.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | The application Id.(Required).
device_info = mamv1.DeviceInfo() # DeviceInfo | Device Information. (optional)

try:
    # Uninstalls the specified internal application from a device.
    api_instance.internal_apps_v1_remove_internal_app_from_device_async(applicationid, device_info=device_info)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_remove_internal_app_from_device_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The application Id.(Required). | 
 **device_info** | [**DeviceInfo**](DeviceInfo.md)| Device Information. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_retire_app_async**
> internal_apps_v1_retire_app_async(applicationid)

Retires the specified Internal application.

Retires the Internal application identified by the application ID. Only the current version of the app would be retired and be removed from devices. If a lower version is assigned, it will be deployed to the devices.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | The Id integer of the application.(Required).

try:
    # Retires the specified Internal application.
    api_instance.internal_apps_v1_retire_app_async(applicationid)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_retire_app_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The Id integer of the application.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_retrieve_app_versions_async**
> list[ApplicationVersionV1Model] internal_apps_v1_retrieve_app_versions_async(bundle_id, device_type, organizationgroupuuid=organizationgroupuuid)

New - Retrieves the versions of this app assigned at this Organization Group.



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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
bundle_id = 'bundle_id_example' # str | Bundle Identifier of application that corresponds with the App ID.(Required)
device_type = 56 # int | Device platform(Required)
organizationgroupuuid =  # object | The Organization Group identifier in which the counts need to be fetched. Will be defaulted to admin Organization Group identifier if not set. E.g. EF331D65-C005-4388-8E52-B1390AA171D9 (optional) (default to )

try:
    # New - Retrieves the versions of this app assigned at this Organization Group.
    api_response = api_instance.internal_apps_v1_retrieve_app_versions_async(bundle_id, device_type, organizationgroupuuid=organizationgroupuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_retrieve_app_versions_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| Bundle Identifier of application that corresponds with the App ID.(Required) | 
 **device_type** | **int**| Device platform(Required) | 
 **organizationgroupuuid** | [**object**](.md)| The Organization Group identifier in which the counts need to be fetched. Will be defaulted to admin Organization Group identifier if not set. E.g. EF331D65-C005-4388-8E52-B1390AA171D9 | [optional] [default to ]

### Return type

[**list[ApplicationVersionV1Model]**](ApplicationVersionV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_un_retire_app_async**
> internal_apps_v1_un_retire_app_async(applicationid, retirepreviousversion=retirepreviousversion)

Unretires the specified internal application.

Unretires the internal application.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
applicationid = 56 # int | The Id integer of the application.(Required).
retirepreviousversion = '' # str | Whether to retire previous versions of the application - Yes/No. (optional) (default to )

try:
    # Unretires the specified internal application.
    api_instance.internal_apps_v1_un_retire_app_async(applicationid, retirepreviousversion=retirepreviousversion)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_un_retire_app_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **int**| The Id integer of the application.(Required). | 
 **retirepreviousversion** | **str**| Whether to retire previous versions of the application - Yes/No. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_apps_v1_update_internal_app**
> internal_apps_v1_update_internal_app(application_id, application_entity=application_entity)

Updates the internal application.

Updates the internal application identified by applicationid.

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
api_instance = mamv1.InternalAppsV1Api(mamv1.ApiClient(configuration))
application_id = 56 # int | Application Id to be updated.
application_entity = mamv1.ApplicationEntity_() # ApplicationEntity_ | The application details. (optional)

try:
    # Updates the internal application.
    api_instance.internal_apps_v1_update_internal_app(application_id, application_entity=application_entity)
except ApiException as e:
    print("Exception when calling InternalAppsV1Api->internal_apps_v1_update_internal_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| Application Id to be updated. | 
 **application_entity** | [**ApplicationEntity_**](ApplicationEntity_.md)| The application details. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

