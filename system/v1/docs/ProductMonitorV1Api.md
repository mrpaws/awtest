# systemv1.ProductMonitorV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_monitor_v1_get_applications**](ProductMonitorV1Api.md#product_monitor_v1_get_applications) | **GET** /productmonitor/apps/search | New - Gets the list of apps based on the search parameters
[**product_monitor_v1_get_product_deployment_status**](ProductMonitorV1Api.md#product_monitor_v1_get_product_deployment_status) | **GET** /productmonitor/products/{uuid}/deploymentstatus | New - Gets the deployment status of the specified app or profile on various devices
[**product_monitor_v1_get_profiles**](ProductMonitorV1Api.md#product_monitor_v1_get_profiles) | **GET** /productmonitor/profiles/search | New - Gets the list of profiles based on the search parameters


# **product_monitor_v1_get_applications**
> list[ProductDetailV1Model] product_monitor_v1_get_applications(searchtext=searchtext, pagenumber=pagenumber, pagesize=pagesize)

New - Gets the list of apps based on the search parameters

Returns the list of all matching apps on the search criteria provided

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.ProductMonitorV1Api(systemv1.ApiClient(configuration))
searchtext = '' # str | App name or part of app name used as Search text for searching applications (optional) (default to )
pagenumber = 56 # int | Specific page number to get. Default value is 0 (optional)
pagesize = 56 # int | Maximumm records per page. Default value is 20 (optional)

try:
    # New - Gets the list of apps based on the search parameters
    api_response = api_instance.product_monitor_v1_get_applications(searchtext=searchtext, pagenumber=pagenumber, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductMonitorV1Api->product_monitor_v1_get_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchtext** | **str**| App name or part of app name used as Search text for searching applications | [optional] [default to ]
 **pagenumber** | **int**| Specific page number to get. Default value is 0 | [optional] 
 **pagesize** | **int**| Maximumm records per page. Default value is 20 | [optional] 

### Return type

[**list[ProductDetailV1Model]**](ProductDetailV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_monitor_v1_get_product_deployment_status**
> ProductDeploymentDetailsV1Model product_monitor_v1_get_product_deployment_status(uuid, producttype)

New - Gets the deployment status of the specified app or profile on various devices

Returns the deployment status of the specified app or profile on various devices

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.ProductMonitorV1Api(systemv1.ApiClient(configuration))
uuid = 'uuid_example' # str | Unique Identifier for App or profile(Required)
producttype = '' # str | Type of the product i.e., InternalApp, PublicApp, PurchasedApp or Profile(Required) (default to )

try:
    # New - Gets the deployment status of the specified app or profile on various devices
    api_response = api_instance.product_monitor_v1_get_product_deployment_status(uuid, producttype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductMonitorV1Api->product_monitor_v1_get_product_deployment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique Identifier for App or profile(Required) | 
 **producttype** | **str**| Type of the product i.e., InternalApp, PublicApp, PurchasedApp or Profile(Required) | [default to ]

### Return type

[**ProductDeploymentDetailsV1Model**](ProductDeploymentDetailsV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_monitor_v1_get_profiles**
> list[ProductDetailV1Model] product_monitor_v1_get_profiles(searchtext=searchtext, pagenumber=pagenumber, pagesize=pagesize)

New - Gets the list of profiles based on the search parameters

Returns the list of all matching profiles on the search criteria provided

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = systemv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = systemv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = systemv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = systemv1.ProductMonitorV1Api(systemv1.ApiClient(configuration))
searchtext = '' # str | Profile name or part of profile name used as Search text for searching profiles (optional) (default to )
pagenumber = 56 # int | Specific page number to get. Default value is 0 (optional)
pagesize = 56 # int | Maximumm records per page. Default value is 20 (optional)

try:
    # New - Gets the list of profiles based on the search parameters
    api_response = api_instance.product_monitor_v1_get_profiles(searchtext=searchtext, pagenumber=pagenumber, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductMonitorV1Api->product_monitor_v1_get_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchtext** | **str**| Profile name or part of profile name used as Search text for searching profiles | [optional] [default to ]
 **pagenumber** | **int**| Specific page number to get. Default value is 0 | [optional] 
 **pagesize** | **int**| Maximumm records per page. Default value is 20 | [optional] 

### Return type

[**list[ProductDetailV1Model]**](ProductDetailV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

