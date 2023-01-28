# mdmv3.ProfilesV3Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profiles_v3_create_device_profile_async**](ProfilesV3Api.md#profiles_v3_create_device_profile_async) | **POST** /profiles | New - Create a new profile
[**profiles_v3_delete_device_profile_async**](ProfilesV3Api.md#profiles_v3_delete_device_profile_async) | **DELETE** /profiles/{profileUuid} | New - Delete a Profile
[**profiles_v3_get_device_profile_details_async**](ProfilesV3Api.md#profiles_v3_get_device_profile_details_async) | **GET** /profiles/{profileUuid} | New - Retrieve details of a specific profile
[**profiles_v3_get_device_profiles**](ProfilesV3Api.md#profiles_v3_get_device_profiles) | **GET** /groups/{organizationGroupUuid}/profiles | Get all device profiles as per search filter
[**profiles_v3_search_async**](ProfilesV3Api.md#profiles_v3_search_async) | **POST** /profiles/search | New - Search API to Retrieve a list of profiles.
[**profiles_v3_update_device_profile**](ProfilesV3Api.md#profiles_v3_update_device_profile) | **PUT** /profiles/{profileUuid} | New - Updates Device Profile.
[**profiles_v3_upload_profile_payload**](ProfilesV3Api.md#profiles_v3_upload_profile_payload) | **POST** /devices/{deviceUuid}/profiles/{profileUuid} | Uploads a completed (already built for device) profile


# **profiles_v3_create_device_profile_async**
> ProfileV3Entity profiles_v3_create_device_profile_async(profile_entity=profile_entity)

New - Create a new profile

1. Create a new profile for the provided platform with the specified payloads.  2. For Version 2004, only Windows Defender Payload is supported.

### Example
```python
from __future__ import print_function
import time
import mdmv3
from mdmv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv3.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv3.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv3.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv3.ProfilesV3Api(mdmv3.ApiClient(configuration))
profile_entity = mdmv3.ProfileV3Entity() # ProfileV3Entity | An entity containing the attributes for creating a profile for the windows desktop platform. (optional)

try:
    # New - Create a new profile
    api_response = api_instance.profiles_v3_create_device_profile_async(profile_entity=profile_entity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV3Api->profiles_v3_create_device_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_entity** | [**ProfileV3Entity**](ProfileV3Entity.md)| An entity containing the attributes for creating a profile for the windows desktop platform. | [optional] 

### Return type

[**ProfileV3Entity**](ProfileV3Entity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v3_delete_device_profile_async**
> profiles_v3_delete_device_profile_async(profile_uuid)

New - Delete a Profile

Deletes the specified profile.

### Example
```python
from __future__ import print_function
import time
import mdmv3
from mdmv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv3.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv3.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv3.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv3.ProfilesV3Api(mdmv3.ApiClient(configuration))
profile_uuid = 'profile_uuid_example' # str | Unique identifier of the device profile

try:
    # New - Delete a Profile
    api_instance.profiles_v3_delete_device_profile_async(profile_uuid)
except ApiException as e:
    print("Exception when calling ProfilesV3Api->profiles_v3_delete_device_profile_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | [**str**](.md)| Unique identifier of the device profile | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=3, application/xml;version=3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v3_get_device_profile_details_async**
> ProfileV3Entity profiles_v3_get_device_profile_details_async(profile_uuid)

New - Retrieve details of a specific profile

1. Returns the full profile details, including all payloads associated with the profile.  2. For Version 2004, only Windows Defender Payload is supported.

### Example
```python
from __future__ import print_function
import time
import mdmv3
from mdmv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv3.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv3.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv3.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv3.ProfilesV3Api(mdmv3.ApiClient(configuration))
profile_uuid = 'profile_uuid_example' # str | Unique identifier of the profile

try:
    # New - Retrieve details of a specific profile
    api_response = api_instance.profiles_v3_get_device_profile_details_async(profile_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV3Api->profiles_v3_get_device_profile_details_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | [**str**](.md)| Unique identifier of the profile | 

### Return type

[**ProfileV3Entity**](ProfileV3Entity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v3_get_device_profiles**
> profiles_v3_get_device_profiles(organization_group_uuid, platform=platform, status=status, searchtext=searchtext, orderby=orderby, sortorder=sortorder, offset=offset, limit=limit)

Get all device profiles as per search filter

### Example
```python
from __future__ import print_function
import time
import mdmv3
from mdmv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv3.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv3.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv3.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv3.ProfilesV3Api(mdmv3.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Unique identifier for organization group
platform = '' # str | Platform name (optional) (default to )
status = '' # str | Profile status (Active or Inactive) (optional) (default to )
searchtext = '' # str | search text (optional) (default to )
orderby = '' # str | Orderby parameter name (optional) (default to )
sortorder = '' # str | Sorting order, Values ASC or DESC, Defaults to ASC (optional) (default to )
offset = 56 # int | to skip number of records (optional)
limit = 56 # int | Maximum results which should be returned in each request (optional)

try:
    # Get all device profiles as per search filter
    api_instance.profiles_v3_get_device_profiles(organization_group_uuid, platform=platform, status=status, searchtext=searchtext, orderby=orderby, sortorder=sortorder, offset=offset, limit=limit)
except ApiException as e:
    print("Exception when calling ProfilesV3Api->profiles_v3_get_device_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Unique identifier for organization group | 
 **platform** | **str**| Platform name | [optional] [default to ]
 **status** | **str**| Profile status (Active or Inactive) | [optional] [default to ]
 **searchtext** | **str**| search text | [optional] [default to ]
 **orderby** | **str**| Orderby parameter name | [optional] [default to ]
 **sortorder** | **str**| Sorting order, Values ASC or DESC, Defaults to ASC | [optional] [default to ]
 **offset** | **int**| to skip number of records | [optional] 
 **limit** | **int**| Maximum results which should be returned in each request | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=3, application/xml;version=3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v3_search_async**
> ProfilesSearchResultV3Model profiles_v3_search_async(profile_search_request_v3_model)

New - Search API to Retrieve a list of profiles.

Returns a list of profiles based on the search criteria.

### Example
```python
from __future__ import print_function
import time
import mdmv3
from mdmv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv3.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv3.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv3.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv3.ProfilesV3Api(mdmv3.ApiClient(configuration))
profile_search_request_v3_model = mdmv3.ProfileSearchRequestV3Model() # ProfileSearchRequestV3Model | Model for profile search request.(Required)

try:
    # New - Search API to Retrieve a list of profiles.
    api_response = api_instance.profiles_v3_search_async(profile_search_request_v3_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV3Api->profiles_v3_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_search_request_v3_model** | [**ProfileSearchRequestV3Model**](ProfileSearchRequestV3Model.md)| Model for profile search request.(Required) | 

### Return type

[**ProfilesSearchResultV3Model**](ProfilesSearchResultV3Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v3_update_device_profile**
> ProfileV3Entity profiles_v3_update_device_profile(profile_uuid, profile_entity=profile_entity)

New - Updates Device Profile.

1. If the add_version attribute is empty or false a new Profile version will not be created but AssignedSmartGroups RootLocationGroup AssignedGeofenceArea and AssignedSchedule will be saved and published.   2. If it is true new version of the profile will be created and published.  3. For Version 2004, only Windows Defender Payload is supported.

### Example
```python
from __future__ import print_function
import time
import mdmv3
from mdmv3.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = mdmv3.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv3.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv3.ProfilesV3Api(mdmv3.ApiClient(configuration))
profile_uuid = 'profile_uuid_example' # str | Unique identifier of the device profile.
profile_entity = mdmv3.ProfileV3Entity() # ProfileV3Entity | An entity containing the attributes for creating a profile for the windows desktop platform. (optional)

try:
    # New - Updates Device Profile.
    api_response = api_instance.profiles_v3_update_device_profile(profile_uuid, profile_entity=profile_entity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesV3Api->profiles_v3_update_device_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | [**str**](.md)| Unique identifier of the device profile. | 
 **profile_entity** | [**ProfileV3Entity**](ProfileV3Entity.md)| An entity containing the attributes for creating a profile for the windows desktop platform. | [optional] 

### Return type

[**ProfileV3Entity**](ProfileV3Entity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_v3_upload_profile_payload**
> profiles_v3_upload_profile_payload(device_uuid, profile_uuid, format)

Uploads a completed (already built for device) profile

For an existing profile in pending state, upload the completed profile for a given device

### Example
```python
from __future__ import print_function
import time
import mdmv3
from mdmv3.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = mdmv3.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv3.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv3.ProfilesV3Api(mdmv3.ApiClient(configuration))
device_uuid = 'device_uuid_example' # str | Unique identifier for the device
profile_uuid = 'profile_uuid_example' # str | Unique identifier for the profile
format = 56 # int | Specifies the type of payload wrapped in the CMS body

try:
    # Uploads a completed (already built for device) profile
    api_instance.profiles_v3_upload_profile_payload(device_uuid, profile_uuid, format)
except ApiException as e:
    print("Exception when calling ProfilesV3Api->profiles_v3_upload_profile_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | [**str**](.md)| Unique identifier for the device | 
 **profile_uuid** | [**str**](.md)| Unique identifier for the profile | 
 **format** | **int**| Specifies the type of payload wrapped in the CMS body | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/pkcs7-mime
 - **Accept**: application/json;version=3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

