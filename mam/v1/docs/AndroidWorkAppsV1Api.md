# mamv1.AndroidWorkAppsV1Api

All URIs are relative to *https://awapi.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**android_work_apps_v1_import**](AndroidWorkAppsV1Api.md#android_work_apps_v1_import) | **POST** /groups/{uuid}/androidwork/apps/import | New - Import approved Android Enterprise apps to AirWatch
[**android_work_apps_v1_patch**](AndroidWorkAppsV1Api.md#android_work_apps_v1_patch) | **PATCH** /groups/{uuid}/androidwork/apps | New - Approve an app on admin Google account for the organization


# **android_work_apps_v1_import**
> list[AndroidWorkImportedAppV1Model] android_work_apps_v1_import(uuid)

New - Import approved Android Enterprise apps to AirWatch

* Imports all the approved apps in admin Google account of the organization to AirWatch. This makes them available to be managed by AirWatch. Imported apps can be assigned to the smart groups to be made available to the users in the organization.

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
api_instance = mamv1.AndroidWorkAppsV1Api(mamv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Unique Identifier for the organization group(Required)

try:
    # New - Import approved Android Enterprise apps to AirWatch
    api_response = api_instance.android_work_apps_v1_import(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AndroidWorkAppsV1Api->android_work_apps_v1_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique Identifier for the organization group(Required) | 

### Return type

[**list[AndroidWorkImportedAppV1Model]**](AndroidWorkImportedAppV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **android_work_apps_v1_patch**
> android_work_apps_v1_patch(uuid, android_work_app_setting_v1_model, bundle_id)

New - Approve an app on admin Google account for the organization

* Approves the input application on admin Google account for given organization group. This has the same effect of logging into Google Work PlayStore and approving a selected application for the organization. This does not add that application automatically to AirWatch. Call to 'import' API is needed for the same.

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
api_instance = mamv1.AndroidWorkAppsV1Api(mamv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Unique Identifier for the organization group(Required)
android_work_app_setting_v1_model = mamv1.AndroidWorkAppSettingV1ModelPatch() # AndroidWorkAppSettingV1ModelPatch | JsonPatch containing operation type and the model. Only 'replace' operation is supported.(Required)
bundle_id = '' # str | Unique Identifier for the Android application on Google PlayStore(Required) (default to )

try:
    # New - Approve an app on admin Google account for the organization
    api_instance.android_work_apps_v1_patch(uuid, android_work_app_setting_v1_model, bundle_id)
except ApiException as e:
    print("Exception when calling AndroidWorkAppsV1Api->android_work_apps_v1_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique Identifier for the organization group(Required) | 
 **android_work_app_setting_v1_model** | [**AndroidWorkAppSettingV1ModelPatch**](AndroidWorkAppSettingV1ModelPatch.md)| JsonPatch containing operation type and the model. Only &#39;replace&#39; operation is supported.(Required) | 
 **bundle_id** | **str**| Unique Identifier for the Android application on Google PlayStore(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

