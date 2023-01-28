# mdmv2.DeviceSensorsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_sensors_v2_add_device_sensor_assignment_async**](DeviceSensorsV2Api.md#device_sensors_v2_add_device_sensor_assignment_async) | **POST** /devicesensors/{sensorUuid}/assignment | New - Adds an assignment to device sensor.
[**device_sensors_v2_bulk_update_device_sensor_assignment_rankings_async**](DeviceSensorsV2Api.md#device_sensors_v2_bulk_update_device_sensor_assignment_rankings_async) | **POST** /devicesensors/{sensorUuid}/assignments | New - Bulk update device sensor assignments based on custom action
[**device_sensors_v2_create_device_sensor_async**](DeviceSensorsV2Api.md#device_sensors_v2_create_device_sensor_async) | **POST** /devicesensors | New - Create a device sensor.
[**device_sensors_v2_delete_device_sensor_assignment_async**](DeviceSensorsV2Api.md#device_sensors_v2_delete_device_sensor_assignment_async) | **DELETE** /devicesensors/assignments/{assignmentUuid} | New - Deletes the device sensor assignment.
[**device_sensors_v2_get_device_sensor_assignment_async**](DeviceSensorsV2Api.md#device_sensors_v2_get_device_sensor_assignment_async) | **GET** /devicesensors/assignments/{assignmentUuid} | New - Gets the device sensor assignment information.
[**device_sensors_v2_get_device_sensor_assignments_async**](DeviceSensorsV2Api.md#device_sensors_v2_get_device_sensor_assignments_async) | **GET** /devicesensors/{sensorUuid}/assignments | New - Gets the list of device sensor assignments.
[**device_sensors_v2_get_device_sensor_async**](DeviceSensorsV2Api.md#device_sensors_v2_get_device_sensor_async) | **GET** /devicesensors/{sensorUuid} | New - Gets the device sensor information.
[**device_sensors_v2_get_device_sensors_async**](DeviceSensorsV2Api.md#device_sensors_v2_get_device_sensors_async) | **GET** /devicesensors/list/{organizationGroupUuid} | New - Gets the list of all the device sensors for the Organization Group.
[**device_sensors_v2_update_device_sensor_assignment_async**](DeviceSensorsV2Api.md#device_sensors_v2_update_device_sensor_assignment_async) | **PUT** /devicesensors/assignments/{assignmentUuid} | New - Update the device sensor assignment information.
[**device_sensors_v2_update_device_sensor_async**](DeviceSensorsV2Api.md#device_sensors_v2_update_device_sensor_async) | **PUT** /devicesensors/{sensorUuid} | New - Update the device sensor.


# **device_sensors_v2_add_device_sensor_assignment_async**
> BaseModel device_sensors_v2_add_device_sensor_assignment_async(sensor_uuid, device_sensor_assignment_request)

New - Adds an assignment to device sensor.

Adds an assignment to device sensor. Assignment information includes assigned smart groups and triggers.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DeviceSensorsV2Api(mdmv2.ApiClient(configuration))
sensor_uuid = 'sensor_uuid_example' # str | Uuid of the device sensor.(Required)
device_sensor_assignment_request = mdmv2.DeviceSensorAssignmentRequestV1Model() # DeviceSensorAssignmentRequestV1Model | Device sensor assignment request model. Includes smart group uuids, triggers, and assignment group name.(Required)

try:
    # New - Adds an assignment to device sensor.
    api_response = api_instance.device_sensors_v2_add_device_sensor_assignment_async(sensor_uuid, device_sensor_assignment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSensorsV2Api->device_sensors_v2_add_device_sensor_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_uuid** | [**str**](.md)| Uuid of the device sensor.(Required) | 
 **device_sensor_assignment_request** | [**DeviceSensorAssignmentRequestV1Model**](DeviceSensorAssignmentRequestV1Model.md)| Device sensor assignment request model. Includes smart group uuids, triggers, and assignment group name.(Required) | 

### Return type

[**BaseModel**](BaseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v2_bulk_update_device_sensor_assignment_rankings_async**
> device_sensors_v2_bulk_update_device_sensor_assignment_rankings_async(sensor_uuid, update_assignment_ranking, action)

New - Bulk update device sensor assignments based on custom action

Bulk update device sensor assignments for a specific device sensor

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DeviceSensorsV2Api(mdmv2.ApiClient(configuration))
sensor_uuid = 'sensor_uuid_example' # str | Uuid of the device sensor.(Required)
update_assignment_ranking = [mdmv2.DeviceSensorAssignmentRankingV1Model()] # list[DeviceSensorAssignmentRankingV1Model] | Contains a list of device sensor assignment rankings.(Required)
action = '' # str | Custom action on device sensor assignments. Possible values [update-ranking] update-ranking will update all the rankings provided for device assignments belonging to a specific device sensor.(Required) (default to )

try:
    # New - Bulk update device sensor assignments based on custom action
    api_instance.device_sensors_v2_bulk_update_device_sensor_assignment_rankings_async(sensor_uuid, update_assignment_ranking, action)
except ApiException as e:
    print("Exception when calling DeviceSensorsV2Api->device_sensors_v2_bulk_update_device_sensor_assignment_rankings_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_uuid** | [**str**](.md)| Uuid of the device sensor.(Required) | 
 **update_assignment_ranking** | [**list[DeviceSensorAssignmentRankingV1Model]**](DeviceSensorAssignmentRankingV1Model.md)| Contains a list of device sensor assignment rankings.(Required) | 
 **action** | **str**| Custom action on device sensor assignments. Possible values [update-ranking] update-ranking will update all the rankings provided for device assignments belonging to a specific device sensor.(Required) | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v2_create_device_sensor_async**
> BaseModel device_sensors_v2_create_device_sensor_async(device_sensor_request)

New - Create a device sensor.

Create a device sensor which includes sensor name, description, organization group identifier, platform, query type, execution context, timeout, script data, script blob identifier, and script environment variables.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DeviceSensorsV2Api(mdmv2.ApiClient(configuration))
device_sensor_request = mdmv2.DeviceSensorRequestV2Model() # DeviceSensorRequestV2Model | Device sensor request model. Includes sensor name, description, organization group identifier, platform, query type, execution context, timeout, script data, script blob identifier, and script environment variables.(Required)

try:
    # New - Create a device sensor.
    api_response = api_instance.device_sensors_v2_create_device_sensor_async(device_sensor_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSensorsV2Api->device_sensors_v2_create_device_sensor_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_sensor_request** | [**DeviceSensorRequestV2Model**](DeviceSensorRequestV2Model.md)| Device sensor request model. Includes sensor name, description, organization group identifier, platform, query type, execution context, timeout, script data, script blob identifier, and script environment variables.(Required) | 

### Return type

[**BaseModel**](BaseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v2_delete_device_sensor_assignment_async**
> device_sensors_v2_delete_device_sensor_assignment_async(assignment_uuid)

New - Deletes the device sensor assignment.

Deletes a single device sensor assignment.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DeviceSensorsV2Api(mdmv2.ApiClient(configuration))
assignment_uuid = 'assignment_uuid_example' # str | Uuid of the device sensor assignment.(Required)

try:
    # New - Deletes the device sensor assignment.
    api_instance.device_sensors_v2_delete_device_sensor_assignment_async(assignment_uuid)
except ApiException as e:
    print("Exception when calling DeviceSensorsV2Api->device_sensors_v2_delete_device_sensor_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_uuid** | [**str**](.md)| Uuid of the device sensor assignment.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v2_get_device_sensor_assignment_async**
> DeviceSensorAssignmentResponseV1Model device_sensors_v2_get_device_sensor_assignment_async(assignment_uuid)

New - Gets the device sensor assignment information.

Gets device sensor assignment information which includes assigned smart groups and triggers.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DeviceSensorsV2Api(mdmv2.ApiClient(configuration))
assignment_uuid = 'assignment_uuid_example' # str | Uuid of the device sensor assignment.(Required)

try:
    # New - Gets the device sensor assignment information.
    api_response = api_instance.device_sensors_v2_get_device_sensor_assignment_async(assignment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSensorsV2Api->device_sensors_v2_get_device_sensor_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_uuid** | [**str**](.md)| Uuid of the device sensor assignment.(Required) | 

### Return type

[**DeviceSensorAssignmentResponseV1Model**](DeviceSensorAssignmentResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v2_get_device_sensor_assignments_async**
> list[DeviceSensorAssignmentResponseV1Model] device_sensors_v2_get_device_sensor_assignments_async(sensor_uuid)

New - Gets the list of device sensor assignments.

Get a list of device sensor assignments information which includes assigned smart groups and triggers for each assignment.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DeviceSensorsV2Api(mdmv2.ApiClient(configuration))
sensor_uuid = 'sensor_uuid_example' # str | Uuid of the device sensor.(Required)

try:
    # New - Gets the list of device sensor assignments.
    api_response = api_instance.device_sensors_v2_get_device_sensor_assignments_async(sensor_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSensorsV2Api->device_sensors_v2_get_device_sensor_assignments_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_uuid** | [**str**](.md)| Uuid of the device sensor.(Required) | 

### Return type

[**list[DeviceSensorAssignmentResponseV1Model]**](DeviceSensorAssignmentResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v2_get_device_sensor_async**
> DeviceSensorResponseV2Model device_sensors_v2_get_device_sensor_async(sensor_uuid)

New - Gets the device sensor information.

Get a device sensor which includes sensor name, description, organization group identifier, platform, query type, execution context, timeout, script data, script blob identifier, and script environment variables.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DeviceSensorsV2Api(mdmv2.ApiClient(configuration))
sensor_uuid = 'sensor_uuid_example' # str | Uuid of the device sensor.(Required)

try:
    # New - Gets the device sensor information.
    api_response = api_instance.device_sensors_v2_get_device_sensor_async(sensor_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSensorsV2Api->device_sensors_v2_get_device_sensor_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_uuid** | [**str**](.md)| Uuid of the device sensor.(Required) | 

### Return type

[**DeviceSensorResponseV2Model**](DeviceSensorResponseV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v2_get_device_sensors_async**
> DeviceSensorListResponseV2Model device_sensors_v2_get_device_sensors_async(organization_group_uuid, name=name, query_type=query_type, platform=platform, page=page, page_size=page_size, orderby=orderby, sort_order=sort_order)

New - Gets the list of all the device sensors for the Organization Group.

Returns a list of device sensor(s) with sensor details for the Organization Group.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DeviceSensorsV2Api(mdmv2.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Identifier of the Organization Group(Required)
name = '' # str | Filter records based on the sensor name. Partial names are accepted. (optional) (default to )
query_type = '' # str | Filter records based on the query type. Default is None. Accepted values are [POWERSHELL],[BASH] and [PYTHON]. (optional) (default to )
platform = '' # str | Filter records based on the platform. Default is None. Accepted values are [WIN_RT] and [APPLE_OSX]. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. Default is 0 (optional)
page_size = 56 # int | Maximum records per page. Default 500 (optional)
orderby = '' # str | Name of the property used for sorting. Default is None. Accepted values are [Name], [Platform] and [QueryType] (optional) (default to )
sort_order = '' # str | Indicates whether the sort order is ascending or descending. The property used for sorting is name. Accepted values are [Asc] and [Desc]. Default value is Asc. (optional) (default to )

try:
    # New - Gets the list of all the device sensors for the Organization Group.
    api_response = api_instance.device_sensors_v2_get_device_sensors_async(organization_group_uuid, name=name, query_type=query_type, platform=platform, page=page, page_size=page_size, orderby=orderby, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSensorsV2Api->device_sensors_v2_get_device_sensors_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Identifier of the Organization Group(Required) | 
 **name** | **str**| Filter records based on the sensor name. Partial names are accepted. | [optional] [default to ]
 **query_type** | **str**| Filter records based on the query type. Default is None. Accepted values are [POWERSHELL],[BASH] and [PYTHON]. | [optional] [default to ]
 **platform** | **str**| Filter records based on the platform. Default is None. Accepted values are [WIN_RT] and [APPLE_OSX]. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. Default is 0 | [optional] 
 **page_size** | **int**| Maximum records per page. Default 500 | [optional] 
 **orderby** | **str**| Name of the property used for sorting. Default is None. Accepted values are [Name], [Platform] and [QueryType] | [optional] [default to ]
 **sort_order** | **str**| Indicates whether the sort order is ascending or descending. The property used for sorting is name. Accepted values are [Asc] and [Desc]. Default value is Asc. | [optional] [default to ]

### Return type

[**DeviceSensorListResponseV2Model**](DeviceSensorListResponseV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v2_update_device_sensor_assignment_async**
> BaseExceptionModel device_sensors_v2_update_device_sensor_assignment_async(assignment_uuid, device_sensor_assignment_request)

New - Update the device sensor assignment information.

Update the device sensor assignment information which includes smartgroup ids and triggers.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DeviceSensorsV2Api(mdmv2.ApiClient(configuration))
assignment_uuid = 'assignment_uuid_example' # str | Uuid of the device sensor assignment.(Required)
device_sensor_assignment_request = mdmv2.DeviceSensorAssignmentRequestV1Model() # DeviceSensorAssignmentRequestV1Model | Device sensor assignment request model. Includes smart group uuids, triggers, and assignment group name.(Required)

try:
    # New - Update the device sensor assignment information.
    api_response = api_instance.device_sensors_v2_update_device_sensor_assignment_async(assignment_uuid, device_sensor_assignment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSensorsV2Api->device_sensors_v2_update_device_sensor_assignment_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_uuid** | [**str**](.md)| Uuid of the device sensor assignment.(Required) | 
 **device_sensor_assignment_request** | [**DeviceSensorAssignmentRequestV1Model**](DeviceSensorAssignmentRequestV1Model.md)| Device sensor assignment request model. Includes smart group uuids, triggers, and assignment group name.(Required) | 

### Return type

[**BaseExceptionModel**](BaseExceptionModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v2_update_device_sensor_async**
> device_sensors_v2_update_device_sensor_async(sensor_uuid, device_sensor_request)

New - Update the device sensor.

Update the device sensor which includes description, platform, query type, execution context, timeout, script data, script blob identifier, and script environment variables.

### Example
```python
from __future__ import print_function
import time
import mdmv2
from mdmv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mdmv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mdmv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mdmv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mdmv2.DeviceSensorsV2Api(mdmv2.ApiClient(configuration))
sensor_uuid = 'sensor_uuid_example' # str | Uuid of the device sensor.(Required)
device_sensor_request = mdmv2.DeviceSensorUpdateV2Model() # DeviceSensorUpdateV2Model | Device sensor update model. Includes sensor description, platform, query type, execution context, timeout, script data, script blob identifier, and script environment variables.(Required)

try:
    # New - Update the device sensor.
    api_instance.device_sensors_v2_update_device_sensor_async(sensor_uuid, device_sensor_request)
except ApiException as e:
    print("Exception when calling DeviceSensorsV2Api->device_sensors_v2_update_device_sensor_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_uuid** | [**str**](.md)| Uuid of the device sensor.(Required) | 
 **device_sensor_request** | [**DeviceSensorUpdateV2Model**](DeviceSensorUpdateV2Model.md)| Device sensor update model. Includes sensor description, platform, query type, execution context, timeout, script data, script blob identifier, and script environment variables.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

