# mdmv1.DirectEnrollmentSettingsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**direct_enrollment_settings_v1_create_direct_enrollment_settings**](DirectEnrollmentSettingsV1Api.md#direct_enrollment_settings_v1_create_direct_enrollment_settings) | **POST** /groups/{uuid}/settings/directenrollment | New - Creates a new system override to save direct enrollment settings for Workspace ONE
[**direct_enrollment_settings_v1_get_direct_enrollment_settings**](DirectEnrollmentSettingsV1Api.md#direct_enrollment_settings_v1_get_direct_enrollment_settings) | **GET** /groups/{uuid}/settings/directenrollment | New - Get direct enrollment settings for Workspace ONE


# **direct_enrollment_settings_v1_create_direct_enrollment_settings**
> direct_enrollment_settings_v1_create_direct_enrollment_settings(uuid, direct_enrollment_settings)

New - Creates a new system override to save direct enrollment settings for Workspace ONE

Saves direct enrollment settings for Workspace ONE devices by enabling it for iOS, Legacy Android, and Android Enterprise devices and then assigns them to a specific user group.

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
api_instance = mdmv1.DirectEnrollmentSettingsV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization Group code at which the direct enrollment settings will be returned(Required).
direct_enrollment_settings = mdmv1.DirectEnrollmentSettingsRequestV1Model() # DirectEnrollmentSettingsRequestV1Model | Details of the direct enrollment settings to be created.(Required).

try:
    # New - Creates a new system override to save direct enrollment settings for Workspace ONE
    api_instance.direct_enrollment_settings_v1_create_direct_enrollment_settings(uuid, direct_enrollment_settings)
except ApiException as e:
    print("Exception when calling DirectEnrollmentSettingsV1Api->direct_enrollment_settings_v1_create_direct_enrollment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization Group code at which the direct enrollment settings will be returned(Required). | 
 **direct_enrollment_settings** | [**DirectEnrollmentSettingsRequestV1Model**](DirectEnrollmentSettingsRequestV1Model.md)| Details of the direct enrollment settings to be created.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **direct_enrollment_settings_v1_get_direct_enrollment_settings**
> DirectEnrollmentSettingsResponseV1Model direct_enrollment_settings_v1_get_direct_enrollment_settings(uuid)

New - Get direct enrollment settings for Workspace ONE

Get admin configured direct enrollment settings for Workspace ONE devices at a location group.

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
api_instance = mdmv1.DirectEnrollmentSettingsV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Organization Group code at which the direct enrollment settings will be returned(Required).

try:
    # New - Get direct enrollment settings for Workspace ONE
    api_response = api_instance.direct_enrollment_settings_v1_get_direct_enrollment_settings(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectEnrollmentSettingsV1Api->direct_enrollment_settings_v1_get_direct_enrollment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Organization Group code at which the direct enrollment settings will be returned(Required). | 

### Return type

[**DirectEnrollmentSettingsResponseV1Model**](DirectEnrollmentSettingsResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

