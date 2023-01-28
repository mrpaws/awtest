# mdmv1.UpdatesV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updates_v1_bulk_update_device_update_deployment**](UpdatesV1Api.md#updates_v1_bulk_update_device_update_deployment) | **POST** /updates/{updateUuid}/groups/{organizationGroupUuid}/deployments | New - Bulk update device update deployments based on custom action.
[**updates_v1_create_update_deployment**](UpdatesV1Api.md#updates_v1_create_update_deployment) | **POST** /updates/{updateUuid}/groups/{organizationGroupUuid}/deployment | New - Creates a deployment for a specific device update.
[**updates_v1_delete_device_update_deployment**](UpdatesV1Api.md#updates_v1_delete_device_update_deployment) | **DELETE** /updates/deployments/{uuid} | New - Deletes the device update deployment.
[**updates_v1_devices_update_action**](UpdatesV1Api.md#updates_v1_devices_update_action) | **POST** /updates/{updateUuid}/groups/{organizationGroupUuid} | New - Starts or stops the roll out of the device update for the specific Organization Group.
[**updates_v1_get_count_of_device_status**](UpdatesV1Api.md#updates_v1_get_count_of_device_status) | **GET** /updates/{updateUuid}/groups/{organizationGroupUuid}/device-status | New - Gets the breakdown of device statuses for a given device update at the specified Organization Group
[**updates_v1_get_deployments_by_device_update**](UpdatesV1Api.md#updates_v1_get_deployments_by_device_update) | **GET** /updates/{uuid}/deployments | New - Get deployments for a device update at a specific Organization Group.
[**updates_v1_get_device_readiness**](UpdatesV1Api.md#updates_v1_get_device_readiness) | **GET** /updates/{updateUuid}/groups/{organizationGroupUuid}/device-readiness | New - Gets device readiness for a given device update at the specified Organization Group.
[**updates_v1_get_device_update_deployment_details**](UpdatesV1Api.md#updates_v1_get_device_update_deployment_details) | **GET** /updates/deployments/{uuid} | New - Gets the device update deployment details.
[**updates_v1_get_device_update_status_by_search_parameters**](UpdatesV1Api.md#updates_v1_get_device_update_status_by_search_parameters) | **GET** /updates/{updateUuid}/groups/{organizationGroupUuid}/update-status | New - Gets the device update status for all the assigned devices by search parameters
[**updates_v1_get_device_updates_by_search_parameters**](UpdatesV1Api.md#updates_v1_get_device_updates_by_search_parameters) | **GET** /updates | New - Get device updates by search parameters
[**updates_v1_get_specific_update_details**](UpdatesV1Api.md#updates_v1_get_specific_update_details) | **GET** /updates/{uuid} | New - Get Specific device update details.
[**updates_v1_update_device_update_deployment**](UpdatesV1Api.md#updates_v1_update_device_update_deployment) | **PUT** /updates/deployments/{uuid} | New - Updates the device update deployment.


# **updates_v1_bulk_update_device_update_deployment**
> updates_v1_bulk_update_device_update_deployment(update_uuid, organization_group_uuid, update_deployment_rankings, action)

New - Bulk update device update deployments based on custom action.

Bulk updates device update deployments based on custom action for a specific device update at the deployment Organization Group.

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
update_uuid = 'update_uuid_example' # str | Device update UUID(Required)
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group UUID(Required)
update_deployment_rankings = [mdmv1.DeviceUpdateDeploymentRankingV1Model()] # list[DeviceUpdateDeploymentRankingV1Model] | Contains a list of device update deployment rankings.(Required)
action = '' # str | Custom action on deployments. Possible values [update-ranking] update-ranking will update all the rankings provided for device update deployments belonging to a specific device update and Organization Group.(Required) (default to )

try:
    # New - Bulk update device update deployments based on custom action.
    api_instance.updates_v1_bulk_update_device_update_deployment(update_uuid, organization_group_uuid, update_deployment_rankings, action)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_bulk_update_device_update_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_uuid** | [**str**](.md)| Device update UUID(Required) | 
 **organization_group_uuid** | [**str**](.md)| Organization Group UUID(Required) | 
 **update_deployment_rankings** | [**list[DeviceUpdateDeploymentRankingV1Model]**](DeviceUpdateDeploymentRankingV1Model.md)| Contains a list of device update deployment rankings.(Required) | 
 **action** | **str**| Custom action on deployments. Possible values [update-ranking] update-ranking will update all the rankings provided for device update deployments belonging to a specific device update and Organization Group.(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_v1_create_update_deployment**
> BaseModel updates_v1_create_update_deployment(update_uuid, organization_group_uuid, update_deployment)

New - Creates a deployment for a specific device update.

Creates a deployment for a specific device update by specifying the deployment parameters and notification preferences for the deployment.

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
update_uuid = 'update_uuid_example' # str | Update UUID(Required)
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group UUID(Required)
update_deployment = mdmv1.DeviceUpdateDeploymentBaseV1Model() # DeviceUpdateDeploymentBaseV1Model | Contains the deployment parameters and notification preferences for the deployment.(Required)

try:
    # New - Creates a deployment for a specific device update.
    api_response = api_instance.updates_v1_create_update_deployment(update_uuid, organization_group_uuid, update_deployment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_create_update_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_uuid** | [**str**](.md)| Update UUID(Required) | 
 **organization_group_uuid** | [**str**](.md)| Organization Group UUID(Required) | 
 **update_deployment** | [**DeviceUpdateDeploymentBaseV1Model**](DeviceUpdateDeploymentBaseV1Model.md)| Contains the deployment parameters and notification preferences for the deployment.(Required) | 

### Return type

[**BaseModel**](BaseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_v1_delete_device_update_deployment**
> updates_v1_delete_device_update_deployment(uuid)

New - Deletes the device update deployment.

Deletes the device update deployment along with deployment parameters and notifications.

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Deployment UUID(Required)

try:
    # New - Deletes the device update deployment.
    api_instance.updates_v1_delete_device_update_deployment(uuid)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_delete_device_update_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Deployment UUID(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_v1_devices_update_action**
> updates_v1_devices_update_action(update_uuid, organization_group_uuid, action)

New - Starts or stops the roll out of the device update for the specific Organization Group.

START will serve the purpose of resuming the roll out of updates if it has been stopped previously.  STOP will pause any further commands being delivered for a specific update in specific Organization Group.

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
update_uuid = 'update_uuid_example' # str | Device update UUID (Required)
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group UUID (Required)
action =  # object | Action for device update. [START, STOP] are accepted values. (Required) (default to )

try:
    # New - Starts or stops the roll out of the device update for the specific Organization Group.
    api_instance.updates_v1_devices_update_action(update_uuid, organization_group_uuid, action)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_devices_update_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_uuid** | [**str**](.md)| Device update UUID (Required) | 
 **organization_group_uuid** | [**str**](.md)| Organization Group UUID (Required) | 
 **action** | [**object**](.md)| Action for device update. [START, STOP] are accepted values. (Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_v1_get_count_of_device_status**
> DeviceUpdateCountDeviceStatusV1Model updates_v1_get_count_of_device_status(update_uuid, organization_group_uuid)

New - Gets the breakdown of device statuses for a given device update at the specified Organization Group

Gets the breakdown of the different device statuses (Idle, Downloading, Installing, DownloadRequiresComputer etc.) for the device update at the specified Organization Group

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
update_uuid = 'update_uuid_example' # str | Device update UUID(Required)
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group UUID(Required)

try:
    # New - Gets the breakdown of device statuses for a given device update at the specified Organization Group
    api_response = api_instance.updates_v1_get_count_of_device_status(update_uuid, organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_get_count_of_device_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_uuid** | [**str**](.md)| Device update UUID(Required) | 
 **organization_group_uuid** | [**str**](.md)| Organization Group UUID(Required) | 

### Return type

[**DeviceUpdateCountDeviceStatusV1Model**](DeviceUpdateCountDeviceStatusV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_v1_get_deployments_by_device_update**
> list[DeploymentV1Model] updates_v1_get_deployments_by_device_update(uuid, organization_group_uuid)

New - Get deployments for a device update at a specific Organization Group.

Retrieves a list of deployments for a specific device update at a specific Organization Group.

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Update UUID(Required)
organization_group_uuid =  # object | Organization Group UUID(Required) (default to )

try:
    # New - Get deployments for a device update at a specific Organization Group.
    api_response = api_instance.updates_v1_get_deployments_by_device_update(uuid, organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_get_deployments_by_device_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Update UUID(Required) | 
 **organization_group_uuid** | [**object**](.md)| Organization Group UUID(Required) | [default to ]

### Return type

[**list[DeploymentV1Model]**](DeploymentV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_v1_get_device_readiness**
> DeviceUpdateDeviceReadinessV1Model updates_v1_get_device_readiness(update_uuid, organization_group_uuid)

New - Gets device readiness for a given device update at the specified Organization Group.

Gets the count of eligible devices, non-eligible devices, devices already on this version, and devices on a higher version for the device update at the specified Organization Group.

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
update_uuid = 'update_uuid_example' # str | Device update UUID(Required)
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group UUID(Required)

try:
    # New - Gets device readiness for a given device update at the specified Organization Group.
    api_response = api_instance.updates_v1_get_device_readiness(update_uuid, organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_get_device_readiness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_uuid** | [**str**](.md)| Device update UUID(Required) | 
 **organization_group_uuid** | [**str**](.md)| Organization Group UUID(Required) | 

### Return type

[**DeviceUpdateDeviceReadinessV1Model**](DeviceUpdateDeviceReadinessV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_v1_get_device_update_deployment_details**
> DeviceUpdateDeploymentCreateV1Model updates_v1_get_device_update_deployment_details(uuid)

New - Gets the device update deployment details.

Gets the device update deployment details along with deployment parameters and notifications.

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Deployment UUID(Required)

try:
    # New - Gets the device update deployment details.
    api_response = api_instance.updates_v1_get_device_update_deployment_details(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_get_device_update_deployment_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Deployment UUID(Required) | 

### Return type

[**DeviceUpdateDeploymentCreateV1Model**](DeviceUpdateDeploymentCreateV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_v1_get_device_update_status_by_search_parameters**
> DeviceUpdateStatusPagedSearchResultsV1Model updates_v1_get_device_update_status_by_search_parameters(update_uuid, organization_group_uuid, device_name=device_name, user=user, status=status, reason=reason, page=page, page_size=page_size)

New - Gets the device update status for all the assigned devices by search parameters

Retrieves the list of all devices assigned to an update with the update status and failure reason (if any) in the specified Organization Group.

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
update_uuid = 'update_uuid_example' # str | Device update UUID(Required)
organization_group_uuid = 'organization_group_uuid_example' # str | Organization Group UUID(Required)
device_name = '' # str | Filter records based on the device name. (optional) (default to )
user = '' # str | Filter records based on the device user. Accepted values are user's first name or last name. (optional) (default to )
status =  # object | Filter records based on update status. Accepted values are DOWNLOADING, DOWNLOAD_FAILED, INSTALLING, INSTALL_FAILED, DOWNLOAD_COMPLETE, INSTALL_COMPLETE, NOT_STARTED, IDLE (optional) (default to )
reason =  # object | Filter records based on the reason for update status. Accepted values are IDLE, DOWNLOADING, DOWNLOAD_FAILED, DOWNLOAD_REQUIRES_COMPUTER, DOWNLOAD_INSUFFICIENT_SPACE, DOWNLOAD_INSUFFICIENT_POWER, DOWNLOAD_INSUFFICIENT_NETWORK, INSTALLING, INSTALL_INSUFFICIENT_SPACE, INSTALL_INSUFFICIENT_POWER, INSTALL_PHONE_CALL_INPROGRESS, INSTALL_FAILED, DOWNLOAD_COMPLETE, INSTALL_COMPLETE, NOT_STARTED (optional) (default to )
page = 56 # int | Page number which will be fetched. 1 based index. Default 1. (optional)
page_size = 56 # int | Maximum number of results to be returned in one page. Default 50. (optional)

try:
    # New - Gets the device update status for all the assigned devices by search parameters
    api_response = api_instance.updates_v1_get_device_update_status_by_search_parameters(update_uuid, organization_group_uuid, device_name=device_name, user=user, status=status, reason=reason, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_get_device_update_status_by_search_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_uuid** | [**str**](.md)| Device update UUID(Required) | 
 **organization_group_uuid** | [**str**](.md)| Organization Group UUID(Required) | 
 **device_name** | **str**| Filter records based on the device name. | [optional] [default to ]
 **user** | **str**| Filter records based on the device user. Accepted values are user&#39;s first name or last name. | [optional] [default to ]
 **status** | [**object**](.md)| Filter records based on update status. Accepted values are DOWNLOADING, DOWNLOAD_FAILED, INSTALLING, INSTALL_FAILED, DOWNLOAD_COMPLETE, INSTALL_COMPLETE, NOT_STARTED, IDLE | [optional] [default to ]
 **reason** | [**object**](.md)| Filter records based on the reason for update status. Accepted values are IDLE, DOWNLOADING, DOWNLOAD_FAILED, DOWNLOAD_REQUIRES_COMPUTER, DOWNLOAD_INSUFFICIENT_SPACE, DOWNLOAD_INSUFFICIENT_POWER, DOWNLOAD_INSUFFICIENT_NETWORK, INSTALLING, INSTALL_INSUFFICIENT_SPACE, INSTALL_INSUFFICIENT_POWER, INSTALL_PHONE_CALL_INPROGRESS, INSTALL_FAILED, DOWNLOAD_COMPLETE, INSTALL_COMPLETE, NOT_STARTED | [optional] [default to ]
 **page** | **int**| Page number which will be fetched. 1 based index. Default 1. | [optional] 
 **page_size** | **int**| Maximum number of results to be returned in one page. Default 50. | [optional] 

### Return type

[**DeviceUpdateStatusPagedSearchResultsV1Model**](DeviceUpdateStatusPagedSearchResultsV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_v1_get_device_updates_by_search_parameters**
> DeviceUpdatePagedSearchResultsV1Model updates_v1_get_device_updates_by_search_parameters(organization_group_uuid, platform=platform, page=page, page_size=page_size, update_name=update_name, version=version, release_date=release_date, expiration_date=expiration_date, custom_release_start_date=custom_release_start_date, custom_release_end_date=custom_release_end_date, custom_expiry_start_date=custom_expiry_start_date, custom_expiry_end_date=custom_expiry_end_date, update_available=update_available)

New - Get device updates by search parameters

Retrieve a list of all available device updates based on specified search parameters.

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid =  # object | Organization Group UUID(Required) (default to )
platform =  # object | Platform name Ex. Apple, AppleOSX, AppleTV. (optional) (default to )
page = 56 # int | Page number which will be fetched. 1 based index. Default 1. (optional)
page_size = 56 # int | Maximum number of results to be returned in one page. Default 50. (optional)
update_name = '' # str | Filter records based on the update name. (optional) (default to )
version = '' # str | Filter records based on the update version. (optional) (default to )
release_date =  # object | Filter records based on the update release date. Accepted values are LastSevenDays, LastThirtyDays, LastThreeMonths, LastSixMonths, Custom (optional) (default to )
expiration_date =  # object | Filter records based on the update expiration date. Accepted values are NextSevenDays, NextThirtyDays, NextThreeMonths, NextSixMonths, Custom (optional) (default to )
custom_release_start_date = '' # datetime | Filter records starting from custom release start date. Example formats are \"yyyy/MM/dd\", \"yyyy-MM-dd\", \"MM/dd/yyyy\", \"MM-dd-yyyy\" (optional) (default to )
custom_release_end_date = '' # datetime | Filter records starting from custom release end date. Example formats are \"yyyy/MM/dd\", \"yyyy-MM-dd\", \"MM/dd/yyyy\", \"MM-dd-yyyy\" (optional) (default to )
custom_expiry_start_date = '' # datetime | Filter records starting from custom expiry start date. Example formats are \"yyyy/MM/dd\", \"yyyy-MM-dd\", \"MM/dd/yyyy\", \"MM-dd-yyyy\" (optional) (default to )
custom_expiry_end_date = '' # datetime | Filter records starting from custom expiry end date. Example formats are \"yyyy/MM/dd\", \"yyyy-MM-dd\", \"MM/dd/yyyy\", \"MM-dd-yyyy\" (optional) (default to )
update_available =  # bool | Filter records based on the update status. (optional) (default to )

try:
    # New - Get device updates by search parameters
    api_response = api_instance.updates_v1_get_device_updates_by_search_parameters(organization_group_uuid, platform=platform, page=page, page_size=page_size, update_name=update_name, version=version, release_date=release_date, expiration_date=expiration_date, custom_release_start_date=custom_release_start_date, custom_release_end_date=custom_release_end_date, custom_expiry_start_date=custom_expiry_start_date, custom_expiry_end_date=custom_expiry_end_date, update_available=update_available)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_get_device_updates_by_search_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**object**](.md)| Organization Group UUID(Required) | [default to ]
 **platform** | [**object**](.md)| Platform name Ex. Apple, AppleOSX, AppleTV. | [optional] [default to ]
 **page** | **int**| Page number which will be fetched. 1 based index. Default 1. | [optional] 
 **page_size** | **int**| Maximum number of results to be returned in one page. Default 50. | [optional] 
 **update_name** | **str**| Filter records based on the update name. | [optional] [default to ]
 **version** | **str**| Filter records based on the update version. | [optional] [default to ]
 **release_date** | [**object**](.md)| Filter records based on the update release date. Accepted values are LastSevenDays, LastThirtyDays, LastThreeMonths, LastSixMonths, Custom | [optional] [default to ]
 **expiration_date** | [**object**](.md)| Filter records based on the update expiration date. Accepted values are NextSevenDays, NextThirtyDays, NextThreeMonths, NextSixMonths, Custom | [optional] [default to ]
 **custom_release_start_date** | **datetime**| Filter records starting from custom release start date. Example formats are \&quot;yyyy/MM/dd\&quot;, \&quot;yyyy-MM-dd\&quot;, \&quot;MM/dd/yyyy\&quot;, \&quot;MM-dd-yyyy\&quot; | [optional] [default to ]
 **custom_release_end_date** | **datetime**| Filter records starting from custom release end date. Example formats are \&quot;yyyy/MM/dd\&quot;, \&quot;yyyy-MM-dd\&quot;, \&quot;MM/dd/yyyy\&quot;, \&quot;MM-dd-yyyy\&quot; | [optional] [default to ]
 **custom_expiry_start_date** | **datetime**| Filter records starting from custom expiry start date. Example formats are \&quot;yyyy/MM/dd\&quot;, \&quot;yyyy-MM-dd\&quot;, \&quot;MM/dd/yyyy\&quot;, \&quot;MM-dd-yyyy\&quot; | [optional] [default to ]
 **custom_expiry_end_date** | **datetime**| Filter records starting from custom expiry end date. Example formats are \&quot;yyyy/MM/dd\&quot;, \&quot;yyyy-MM-dd\&quot;, \&quot;MM/dd/yyyy\&quot;, \&quot;MM-dd-yyyy\&quot; | [optional] [default to ]
 **update_available** | **bool**| Filter records based on the update status. | [optional] [default to ]

### Return type

[**DeviceUpdatePagedSearchResultsV1Model**](DeviceUpdatePagedSearchResultsV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_v1_get_specific_update_details**
> DeviceUpdateDetailsSupportedDevicesV1Model updates_v1_get_specific_update_details(uuid)

New - Get Specific device update details.

Retrieve details about a specific device update.

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Update UUID(Required)

try:
    # New - Get Specific device update details.
    api_response = api_instance.updates_v1_get_specific_update_details(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_get_specific_update_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Update UUID(Required) | 

### Return type

[**DeviceUpdateDetailsSupportedDevicesV1Model**](DeviceUpdateDetailsSupportedDevicesV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_v1_update_device_update_deployment**
> updates_v1_update_device_update_deployment(uuid, deployment_update)

New - Updates the device update deployment.

Updates the device update deployment along with deployment parameters and notifications.

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
api_instance = mdmv1.UpdatesV1Api(mdmv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Deployment UUID(Required)
deployment_update = mdmv1.DeviceUpdateDeploymentUpdateV1Model() # DeviceUpdateDeploymentUpdateV1Model | Deployment update information(Required)

try:
    # New - Updates the device update deployment.
    api_instance.updates_v1_update_device_update_deployment(uuid, deployment_update)
except ApiException as e:
    print("Exception when calling UpdatesV1Api->updates_v1_update_device_update_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Deployment UUID(Required) | 
 **deployment_update** | [**DeviceUpdateDeploymentUpdateV1Model**](DeviceUpdateDeploymentUpdateV1Model.md)| Deployment update information(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

