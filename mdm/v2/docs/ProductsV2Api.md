# mdmv2.ProductsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_v2_assigned_product_devices_async**](ProductsV2Api.md#products_v2_assigned_product_devices_async) | **GET** /products/{id}/assigned | Returns the details of the Device for which Provisioning is Assigned.
[**products_v2_failed_product_devices_async**](ProductsV2Api.md#products_v2_failed_product_devices_async) | **GET** /products/{id}/failed | Returns the details of the Device for which Provisioning is Failed.
[**products_v2_inprogress_product_devices_async**](ProductsV2Api.md#products_v2_inprogress_product_devices_async) | **GET** /products/{id}/inprogress | Returns the details of the Device for which Provisioning is In-Progress.
[**products_v2_product_compliant_devices_async**](ProductsV2Api.md#products_v2_product_compliant_devices_async) | **GET** /products/{id}/compliant | Returns the details of the Devices which are Product Compliant .


# **products_v2_assigned_product_devices_async**
> ProductDeviceDetailsSearchResult products_v2_assigned_product_devices_async(id, seensince=seensince, lastjobupdatefrom=lastjobupdatefrom, page=page, pagesize=pagesize)

Returns the details of the Device for which Provisioning is Assigned.

Returns the details of the Device for which Provisioning is Assigned.<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />

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
api_instance = mdmv2.ProductsV2Api(mdmv2.ApiClient(configuration))
id = 56 # int | Identfier of the Product(Required).
seensince = '' # datetime | Filters devices such that devices with last seen after this date will be returned.              Valid DateTime formats includes as below:              yyyy/MM/dd,yyyy-MM-dd,MM/dd/yyyy,MM-dd-yyyy,              yyyy/MM/dd HH:mm:ss.fff,yyyy-MM-dd HH:mm:ss.fff,              MM/dd/yyyy HH:mm:ss.fff,MM-dd-yyyy HH:mm:ss.fff,              yyyy/MM/ddTHH:mm:ss.fff,yyyy-MM-ddTHH:mm:ss.fff,              MM/dd/yyyyTHH:mm:ss.fff,MM-dd-yyyyTHH:mm:ss.fff,              yyyy-MM-dd HH-mm-ss-tt,yyyy-MM-ddTHH-mm-ss-tt. (optional) (default to )
lastjobupdatefrom = '' # datetime | Filters devices on lastjobstatus DateTime.              Valid DateTime formats includes as below:              yyyy/MM/dd,yyyy-MM-dd,MM/dd/yyyy,MM-dd-yyyy,              yyyy/MM/dd HH:mm:ss.fff,yyyy-MM-dd HH:mm:ss.fff,              MM/dd/yyyy HH:mm:ss.fff,MM-dd-yyyy HH:mm:ss.fff,              yyyy/MM/ddTHH:mm:ss.fff,yyyy-MM-ddTHH:mm:ss.fff,              MM/dd/yyyyTHH:mm:ss.fff,MM-dd-yyyyTHH:mm:ss.fff,              yyyy-MM-dd HH-mm-ss-tt,yyyy-MM-ddTHH-mm-ss-tt. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Returns the details of the Device for which Provisioning is Assigned.
    api_response = api_instance.products_v2_assigned_product_devices_async(id, seensince=seensince, lastjobupdatefrom=lastjobupdatefrom, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV2Api->products_v2_assigned_product_devices_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identfier of the Product(Required). | 
 **seensince** | **datetime**| Filters devices such that devices with last seen after this date will be returned.              Valid DateTime formats includes as below:              yyyy/MM/dd,yyyy-MM-dd,MM/dd/yyyy,MM-dd-yyyy,              yyyy/MM/dd HH:mm:ss.fff,yyyy-MM-dd HH:mm:ss.fff,              MM/dd/yyyy HH:mm:ss.fff,MM-dd-yyyy HH:mm:ss.fff,              yyyy/MM/ddTHH:mm:ss.fff,yyyy-MM-ddTHH:mm:ss.fff,              MM/dd/yyyyTHH:mm:ss.fff,MM-dd-yyyyTHH:mm:ss.fff,              yyyy-MM-dd HH-mm-ss-tt,yyyy-MM-ddTHH-mm-ss-tt. | [optional] [default to ]
 **lastjobupdatefrom** | **datetime**| Filters devices on lastjobstatus DateTime.              Valid DateTime formats includes as below:              yyyy/MM/dd,yyyy-MM-dd,MM/dd/yyyy,MM-dd-yyyy,              yyyy/MM/dd HH:mm:ss.fff,yyyy-MM-dd HH:mm:ss.fff,              MM/dd/yyyy HH:mm:ss.fff,MM-dd-yyyy HH:mm:ss.fff,              yyyy/MM/ddTHH:mm:ss.fff,yyyy-MM-ddTHH:mm:ss.fff,              MM/dd/yyyyTHH:mm:ss.fff,MM-dd-yyyyTHH:mm:ss.fff,              yyyy-MM-dd HH-mm-ss-tt,yyyy-MM-ddTHH-mm-ss-tt. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**ProductDeviceDetailsSearchResult**](ProductDeviceDetailsSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v2_failed_product_devices_async**
> ProductDeviceDetailsSearchResult products_v2_failed_product_devices_async(id, page=page, pagesize=pagesize)

Returns the details of the Device for which Provisioning is Failed.

Returns the details of the Devices for which Provisioning is Failed<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />

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
api_instance = mdmv2.ProductsV2Api(mdmv2.ApiClient(configuration))
id = 56 # int | Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required).
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Returns the details of the Device for which Provisioning is Failed.
    api_response = api_instance.products_v2_failed_product_devices_async(id, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV2Api->products_v2_failed_product_devices_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required). | 
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**ProductDeviceDetailsSearchResult**](ProductDeviceDetailsSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v2_inprogress_product_devices_async**
> ProductDeviceDetailsSearchResult products_v2_inprogress_product_devices_async(id, page=page, pagesize=pagesize)

Returns the details of the Device for which Provisioning is In-Progress.

Returns the details of the Devices which provisioning is in-progress.<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />

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
api_instance = mdmv2.ProductsV2Api(mdmv2.ApiClient(configuration))
id = 56 # int | Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required).
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum results which should be returned in each page. (optional)

try:
    # Returns the details of the Device for which Provisioning is In-Progress.
    api_response = api_instance.products_v2_inprogress_product_devices_async(id, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV2Api->products_v2_inprogress_product_devices_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required). | 
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum results which should be returned in each page. | [optional] 

### Return type

[**ProductDeviceDetailsSearchResult**](ProductDeviceDetailsSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v2_product_compliant_devices_async**
> ProductDeviceDetailsSearchResult products_v2_product_compliant_devices_async(id, page=page, pagesize=pagesize)

Returns the details of the Devices which are Product Compliant .

Returns the details of the Devices which are Product Compliant<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />

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
api_instance = mdmv2.ProductsV2Api(mdmv2.ApiClient(configuration))
id = 56 # int | Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required).
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximum records per page. Default 500. (optional)

try:
    # Returns the details of the Devices which are Product Compliant .
    api_response = api_instance.products_v2_product_compliant_devices_async(id, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV2Api->products_v2_product_compliant_devices_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required). | 
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximum records per page. Default 500. | [optional] 

### Return type

[**ProductDeviceDetailsSearchResult**](ProductDeviceDetailsSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

