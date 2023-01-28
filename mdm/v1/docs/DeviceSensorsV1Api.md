# mdmv1.DeviceSensorsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_sensors_v1_assign_device_sensor**](DeviceSensorsV1Api.md#device_sensors_v1_assign_device_sensor) | **POST** /devicesensors/assign | New - Assign device sensors to smart groups.
[**device_sensors_v1_bulk_delete_device_sensors**](DeviceSensorsV1Api.md#device_sensors_v1_bulk_delete_device_sensors) | **POST** /devicesensors/bulkdelete | New - Deletes the list of device sensors based on the identifiers provided.
[**device_sensors_v1_create_device_sensor**](DeviceSensorsV1Api.md#device_sensors_v1_create_device_sensor) | **POST** /devicesensors | New - Create a device sensor.
[**device_sensors_v1_get_device_sensor**](DeviceSensorsV1Api.md#device_sensors_v1_get_device_sensor) | **GET** /devicesensors/{sensorUuid} | New - Gets the device sensor information.
[**device_sensors_v1_get_device_sensors**](DeviceSensorsV1Api.md#device_sensors_v1_get_device_sensors) | **GET** /devicesensors/list/{organizationGroupUuid} | New - Gets the list of all the device sensors for the Organization Group.
[**device_sensors_v1_update_device_sensor**](DeviceSensorsV1Api.md#device_sensors_v1_update_device_sensor) | **PUT** /devicesensors/{sensorUuid} | New - Update the device sensor.


# **device_sensors_v1_assign_device_sensor**
> DeviceSensorSmartGroupAssignmentResponseV1Model device_sensors_v1_assign_device_sensor(assignment_model)

New - Assign device sensors to smart groups.

Device sensor to smart group assignment map.

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
api_instance = mdmv1.DeviceSensorsV1Api(mdmv1.ApiClient(configuration))
assignment_model = mdmv1.DeviceSensorSmartGroupAssignmentV1Model() # DeviceSensorSmartGroupAssignmentV1Model | Model to map the assignment for device sensors and smart groups.(Required)

try:
    # New - Assign device sensors to smart groups.
    api_response = api_instance.device_sensors_v1_assign_device_sensor(assignment_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSensorsV1Api->device_sensors_v1_assign_device_sensor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_model** | [**DeviceSensorSmartGroupAssignmentV1Model**](DeviceSensorSmartGroupAssignmentV1Model.md)| Model to map the assignment for device sensors and smart groups.(Required) | 

### Return type

[**DeviceSensorSmartGroupAssignmentResponseV1Model**](DeviceSensorSmartGroupAssignmentResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v1_bulk_delete_device_sensors**
> device_sensors_v1_bulk_delete_device_sensors(bulk_delete_request_v1_model)

New - Deletes the list of device sensors based on the identifiers provided.

This API is used to delete the list of device sensors attribute and attribute details along with the associated assignments.

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
api_instance = mdmv1.DeviceSensorsV1Api(mdmv1.ApiClient(configuration))
bulk_delete_request_v1_model = mdmv1.DeviceSensorsBulkDeleteRequestV1Model() # DeviceSensorsBulkDeleteRequestV1Model | (Required)

try:
    # New - Deletes the list of device sensors based on the identifiers provided.
    api_instance.device_sensors_v1_bulk_delete_device_sensors(bulk_delete_request_v1_model)
except ApiException as e:
    print("Exception when calling DeviceSensorsV1Api->device_sensors_v1_bulk_delete_device_sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_delete_request_v1_model** | [**DeviceSensorsBulkDeleteRequestV1Model**](DeviceSensorsBulkDeleteRequestV1Model.md)| (Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v1_create_device_sensor**
> device_sensors_v1_create_device_sensor(device_sensor_request)

New - Create a device sensor.

Create a device sensor which includes sensor name, description, organization group identifier, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.

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
api_instance = mdmv1.DeviceSensorsV1Api(mdmv1.ApiClient(configuration))
device_sensor_request = mdmv1.DeviceSensorRequestV1Model() # DeviceSensorRequestV1Model | Device sensor request model. Includes sensor name, description, organization group identifier, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.(Required)

try:
    # New - Create a device sensor.
    api_instance.device_sensors_v1_create_device_sensor(device_sensor_request)
except ApiException as e:
    print("Exception when calling DeviceSensorsV1Api->device_sensors_v1_create_device_sensor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_sensor_request** | [**DeviceSensorRequestV1Model**](DeviceSensorRequestV1Model.md)| Device sensor request model. Includes sensor name, description, organization group identifier, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v1_get_device_sensor**
> DeviceSensorResponseV1Model device_sensors_v1_get_device_sensor(sensor_uuid)

New - Gets the device sensor information.

Get a device sensor which includes sensor name, description, organization group identifier, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.

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
api_instance = mdmv1.DeviceSensorsV1Api(mdmv1.ApiClient(configuration))
sensor_uuid = 'sensor_uuid_example' # str | Uuid of the device sensor.(Required)

try:
    # New - Gets the device sensor information.
    api_response = api_instance.device_sensors_v1_get_device_sensor(sensor_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSensorsV1Api->device_sensors_v1_get_device_sensor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_uuid** | [**str**](.md)| Uuid of the device sensor.(Required) | 

### Return type

[**DeviceSensorResponseV1Model**](DeviceSensorResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v1_get_device_sensors**
> DeviceSensorListResponseV1Model device_sensors_v1_get_device_sensors(organization_group_uuid, page=page, page_size=page_size)

New - Gets the list of all the device sensors for the Organization Group.

Returns a list of device sensor(s) with sensor details for the Organization Group.

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
api_instance = mdmv1.DeviceSensorsV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid = 'organization_group_uuid_example' # str | Identifier of the Organization Group(Required)
page = 56 # int | Specific page number to get. 0 based index (optional)
page_size = 56 # int | Maximum records per page. Default 500 (optional)

try:
    # New - Gets the list of all the device sensors for the Organization Group.
    api_response = api_instance.device_sensors_v1_get_device_sensors(organization_group_uuid, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceSensorsV1Api->device_sensors_v1_get_device_sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | [**str**](.md)| Identifier of the Organization Group(Required) | 
 **page** | **int**| Specific page number to get. 0 based index | [optional] 
 **page_size** | **int**| Maximum records per page. Default 500 | [optional] 

### Return type

[**DeviceSensorListResponseV1Model**](DeviceSensorListResponseV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sensors_v1_update_device_sensor**
> device_sensors_v1_update_device_sensor(sensor_uuid, device_sensor_request)

New - Update the device sensor.

Update the device sensor which includes description, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.

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
api_instance = mdmv1.DeviceSensorsV1Api(mdmv1.ApiClient(configuration))
sensor_uuid = 'sensor_uuid_example' # str | Uuid of the device sensor.(Required)
device_sensor_request = mdmv1.DeviceSensorUpdateV1Model() # DeviceSensorUpdateV1Model | Device sensor update model. Includes sensor description, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.(Required)

try:
    # New - Update the device sensor.
    api_instance.device_sensors_v1_update_device_sensor(sensor_uuid, device_sensor_request)
except ApiException as e:
    print("Exception when calling DeviceSensorsV1Api->device_sensors_v1_update_device_sensor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_uuid** | [**str**](.md)| Uuid of the device sensor.(Required) | 
 **device_sensor_request** | [**DeviceSensorUpdateV1Model**](DeviceSensorUpdateV1Model.md)| Device sensor update model. Includes sensor description, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

