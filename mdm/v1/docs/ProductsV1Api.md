# mdmv1.ProductsV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_v1_activate**](ProductsV1Api.md#products_v1_activate) | **POST** /products/{id}/activate | Activates the Product.
[**products_v1_add_conditions_to_product_async**](ProductsV1Api.md#products_v1_add_conditions_to_product_async) | **POST** /products/{productid}/addconditions | Adds Conditions to Product.
[**products_v1_add_smart_group**](ProductsV1Api.md#products_v1_add_smart_group) | **POST** /products/{id}/addsmartgroup/{smartgroupid} | Adds SmartGroup to Product.
[**products_v1_copy_product**](ProductsV1Api.md#products_v1_copy_product) | **POST** /products/{id}/copy | Copies the existing product to create a new product.
[**products_v1_create_product**](ProductsV1Api.md#products_v1_create_product) | **POST** /products/create | Creates a new Product.
[**products_v1_deactivate**](ProductsV1Api.md#products_v1_deactivate) | **POST** /products/{id}/deactivate | Deactivates the Product.
[**products_v1_delete_product_async**](ProductsV1Api.md#products_v1_delete_product_async) | **DELETE** /products/{id} | New - Deletes the product by the product Id
[**products_v1_device_health_check_search**](ProductsV1Api.md#products_v1_device_health_check_search) | **GET** /products/devicehealthcheck | Gets the details of the device health.
[**products_v1_get_product_by_product_id**](ProductsV1Api.md#products_v1_get_product_by_product_id) | **GET** /products/{id} | Gets the Product.
[**products_v1_get_products**](ProductsV1Api.md#products_v1_get_products) | **GET** /products/{appid}/assignments | Get the products based on Application ID.
[**products_v1_job_status_change_timestamp**](ProductsV1Api.md#products_v1_job_status_change_timestamp) | **GET** /products/jobstatuschangetimestamp | Get the details of job status changes.
[**products_v1_maintain_product_async**](ProductsV1Api.md#products_v1_maintain_product_async) | **POST** /products/maintainProduct | Creates or updates a product.
[**products_v1_product_compliance_issue_summary**](ProductsV1Api.md#products_v1_product_compliance_issue_summary) | **GET** /products/compliance/issues/summary | New - Returns summary of non-compliant devices for products in a OG by product compliance status
[**products_v1_product_compliance_issues**](ProductsV1Api.md#products_v1_product_compliance_issues) | **GET** /products/compliance/issues | New - Returns list of non-compliant devices for products in a OG
[**products_v1_product_extensive_search_async**](ProductsV1Api.md#products_v1_product_extensive_search_async) | **GET** /products/extensivesearch | Returns the Products.
[**products_v1_provisioning_jobs**](ProductsV1Api.md#products_v1_provisioning_jobs) | **GET** /products/provisioningjobs | Returns jobs and associated products.
[**products_v1_push_device_and_policy_on_policy_engine**](ProductsV1Api.md#products_v1_push_device_and_policy_on_policy_engine) | **POST** /products/pushdeviceandpolicyonqueue | Pushes the device and policy onto the policy engine.
[**products_v1_push_device_on_policy_engine**](ProductsV1Api.md#products_v1_push_device_on_policy_engine) | **POST** /products/{id}/pushdeviceonqueue | Pushes the device onto the product policy engine.
[**products_v1_remove_smart_group**](ProductsV1Api.md#products_v1_remove_smart_group) | **POST** /products/{id}/removesmartgroup/{smartgroupid} | Removes SmartGroup from the specified Product.
[**products_v1_reprocess_product_async**](ProductsV1Api.md#products_v1_reprocess_product_async) | **POST** /products/reprocessProduct | Initiates a reprocessing of a product.
[**products_v1_search**](ProductsV1Api.md#products_v1_search) | **GET** /products/search | Searches for the products with the search parameters passed.
[**products_v1_set_product_install_time**](ProductsV1Api.md#products_v1_set_product_install_time) | **POST** /products/{id}/setinstalltime | Sets the product install time.
[**products_v1_update_product**](ProductsV1Api.md#products_v1_update_product) | **POST** /products/{id}/update | Updates the product details.


# **products_v1_activate**
> products_v1_activate(id)

Activates the Product.

Activates the product which matches the input Product Identifier.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Identifier of Product which needs to be activated (Required).

try:
    # Activates the Product.
    api_instance.products_v1_activate(id)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of Product which needs to be activated (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_add_conditions_to_product_async**
> BulkResponse products_v1_add_conditions_to_product_async(productid, conditions)

Adds Conditions to Product.

Adds passed Download and Install Conditions to specified Product.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
productid = 56 # int | Identifier of the Product to which conditions to be added (Required).
conditions = mdmv1.Conditions() # Conditions | Conditions to be added to Product (Required).

try:
    # Adds Conditions to Product.
    api_response = api_instance.products_v1_add_conditions_to_product_async(productid, conditions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_add_conditions_to_product_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **productid** | **int**| Identifier of the Product to which conditions to be added (Required). | 
 **conditions** | [**Conditions**](Conditions.md)| Conditions to be added to Product (Required). | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_add_smart_group**
> products_v1_add_smart_group(id, smartgroupid)

Adds SmartGroup to Product.

Adds the smart group with specified {smartgroupid} to the product with specified {id}.  Note: POST /reprocessProduct API must be called explicitly to reprocess products to policy engine queue.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Identfier of the Product to which SmartGroup needs to be assigned (Required).
smartgroupid = 56 # int | Identfier of the Smart Group which needs to be assigned to the Product (Required).

try:
    # Adds SmartGroup to Product.
    api_instance.products_v1_add_smart_group(id, smartgroupid)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_add_smart_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identfier of the Product to which SmartGroup needs to be assigned (Required). | 
 **smartgroupid** | **int**| Identfier of the Smart Group which needs to be assigned to the Product (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_copy_product**
> EntityId products_v1_copy_product(id, product=product)

Copies the existing product to create a new product.

Copies the existing product to create a new product with the details passed in input, i.e. name and organizationgroupid.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Identfier of the Product from which copy has to be made (Required).
product = mdmv1.ProductModel() # ProductModel | Product details for the new product to be created, i.e. name and managedbyorganizationgroupid. (optional)

try:
    # Copies the existing product to create a new product.
    api_response = api_instance.products_v1_copy_product(id, product=product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_copy_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identfier of the Product from which copy has to be made (Required). | 
 **product** | [**ProductModel**](ProductModel.md)| Product details for the new product to be created, i.e. name and managedbyorganizationgroupid. | [optional] 

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_create_product**
> EntityId products_v1_create_product(product)

Creates a new Product.

Creates a new Product based on the input details like Name, Organization Group, Platform, etc.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
product = mdmv1.ProductModel_() # ProductModel_ | Product resource to create (Required).

try:
    # Creates a new Product.
    api_response = api_instance.products_v1_create_product(product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_create_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | [**ProductModel_**](ProductModel_.md)| Product resource to create (Required). | 

### Return type

[**EntityId**](EntityId.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_deactivate**
> products_v1_deactivate(id)

Deactivates the Product.

Deactivates the product based on input Product Identifier.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Identfier of the product which needs to be deactivated (Required).

try:
    # Deactivates the Product.
    api_instance.products_v1_deactivate(id)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_deactivate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identfier of the product which needs to be deactivated (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_delete_product_async**
> products_v1_delete_product_async(id)

New - Deletes the product by the product Id

Deletes the provisioning product by the product Id specified

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Product Id.(Required).

try:
    # New - Deletes the product by the product Id
    api_instance.products_v1_delete_product_async(id)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_delete_product_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Product Id.(Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_device_health_check_search**
> HealthCheckResult products_v1_device_health_check_search(organizationgroupid=organizationgroupid, organizationgroupname=organizationgroupname, platform=platform, customattributes=customattributes, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)

Gets the details of the device health.

Gets the details of the device health which satisfies the search parameters specified in the request.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | OrganizationGroupId to search for. (optional)
organizationgroupname = '' # str | OrganizationGroup name to search for. Example: US. (optional) (default to )
platform = '' # str | Platform name. Example: Android. (optional) (default to )
customattributes = '' # str | Custom Attribute name. Example: Location. (optional) (default to )
orderby = '' # str | Order results by. Example: DeviceId. (optional) (default to )
sortorder = '' # str | Sorts the result based on this attribute, i.e. ASC for Ascending order 'DESC' for descending order. Example: ASC. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximumm records per page. Default 500. (optional)

try:
    # Gets the details of the device health.
    api_response = api_instance.products_v1_device_health_check_search(organizationgroupid=organizationgroupid, organizationgroupname=organizationgroupname, platform=platform, customattributes=customattributes, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_device_health_check_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| OrganizationGroupId to search for. | [optional] 
 **organizationgroupname** | **str**| OrganizationGroup name to search for. Example: US. | [optional] [default to ]
 **platform** | **str**| Platform name. Example: Android. | [optional] [default to ]
 **customattributes** | **str**| Custom Attribute name. Example: Location. | [optional] [default to ]
 **orderby** | **str**| Order results by. Example: DeviceId. | [optional] [default to ]
 **sortorder** | **str**| Sorts the result based on this attribute, i.e. ASC for Ascending order &#39;DESC&#39; for descending order. Example: ASC. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximumm records per page. Default 500. | [optional] 

### Return type

[**HealthCheckResult**](HealthCheckResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_get_product_by_product_id**
> ProductModel products_v1_get_product_by_product_id(id)

Gets the Product.

Gets the Product based on input product identifier.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Identifier of the Product whose details to be fetched (Required).

try:
    # Gets the Product.
    api_response = api_instance.products_v1_get_product_by_product_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_get_product_by_product_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of the Product whose details to be fetched (Required). | 

### Return type

[**ProductModel**](ProductModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_get_products**
> list[Assignment] products_v1_get_products(appid)

Get the products based on Application ID.

Get the products details based on Application Identifier.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
appid = 56 # int | Product identifier (Required).

try:
    # Get the products based on Application ID.
    api_response = api_instance.products_v1_get_products(appid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appid** | **int**| Product identifier (Required). | 

### Return type

[**list[Assignment]**](Assignment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_job_status_change_timestamp**
> ProvisioningJobsStatusSearchResult products_v1_job_status_change_timestamp(organizationgroupid=organizationgroupid, deviceid=deviceid, productid=productid, jobid=jobid, modifieddatefrom=modifieddatefrom, modifieddateto=modifieddateto, page=page, pagesize=pagesize)

Get the details of job status changes.

Get the details of job status changes along with timestamps for those changes, for a device, a product, or a job  <br />  *modifieddatefrom, modifieddateto* fields accept the following  Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | ID of the Organization Group where Device/Product/Job under question is present.. (optional)
deviceid = '' # str | evice ID of the device for which the job status change timestamp is desired. Example: 1. (optional) (default to )
productid = '' # str | Product ID of the product for which the job status change timestamp is desired. Example: 1. (optional) (default to )
jobid = '' # str | Job ID of the job for which the job status change timestamp is desired. Example: 1. (optional) (default to )
modifieddatefrom = '' # datetime | The start date of the duration for which the job status change timestamp is desired. If none is provided, all the results since enrollment will be shown. (optional) (default to )
modifieddateto = '' # datetime | The end date of the duration for which the job status change timestamp is desired. If none is provided, all the results since enrollment will be shown. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximumm records per page. Default 500. (optional)

try:
    # Get the details of job status changes.
    api_response = api_instance.products_v1_job_status_change_timestamp(organizationgroupid=organizationgroupid, deviceid=deviceid, productid=productid, jobid=jobid, modifieddatefrom=modifieddatefrom, modifieddateto=modifieddateto, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_job_status_change_timestamp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| ID of the Organization Group where Device/Product/Job under question is present.. | [optional] 
 **deviceid** | **str**| evice ID of the device for which the job status change timestamp is desired. Example: 1. | [optional] [default to ]
 **productid** | **str**| Product ID of the product for which the job status change timestamp is desired. Example: 1. | [optional] [default to ]
 **jobid** | **str**| Job ID of the job for which the job status change timestamp is desired. Example: 1. | [optional] [default to ]
 **modifieddatefrom** | **datetime**| The start date of the duration for which the job status change timestamp is desired. If none is provided, all the results since enrollment will be shown. | [optional] [default to ]
 **modifieddateto** | **datetime**| The end date of the duration for which the job status change timestamp is desired. If none is provided, all the results since enrollment will be shown. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximumm records per page. Default 500. | [optional] 

### Return type

[**ProvisioningJobsStatusSearchResult**](ProvisioningJobsStatusSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_maintain_product_async**
> MaintainResult products_v1_maintain_product_async(maintain_product_input_model)

Creates or updates a product.

Creates or updates a product based on input product details like Product Name, Organization Group, Platform, etc.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
maintain_product_input_model = mdmv1.MaintainProductInputModel() # MaintainProductInputModel | Object representing product (Required).

try:
    # Creates or updates a product.
    api_response = api_instance.products_v1_maintain_product_async(maintain_product_input_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_maintain_product_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintain_product_input_model** | [**MaintainProductInputModel**](MaintainProductInputModel.md)| Object representing product (Required). | 

### Return type

[**MaintainResult**](MaintainResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application /json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_product_compliance_issue_summary**
> products_v1_product_compliance_issue_summary(organizationgroupid=organizationgroupid, resourceids=resourceids, parentresourceids=parentresourceids, devicetypes=devicetypes, compliancestatus=compliancestatus, customattributes=customattributes, customattributevalues=customattributevalues)

New - Returns summary of non-compliant devices for products in a OG by product compliance status

v1

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group id which is similar to selected organization group selected in console. (optional)
resourceids = '' # str | list of resources, meaning device uuids, this isnt mandatory (optional) (default to )
parentresourceids = '' # str | list of proxy parent resources, meaning device uuids, this isnt mandatory (optional) (default to )
devicetypes = '' # str | list of device types to filter. (optional) (default to )
compliancestatus = 56 # int | product compliance status id (optional)
customattributes = '' # str | custom attribute names (optional) (default to )
customattributevalues = '' # str | custom attribute values (optional) (default to )

try:
    # New - Returns summary of non-compliant devices for products in a OG by product compliance status
    api_instance.products_v1_product_compliance_issue_summary(organizationgroupid=organizationgroupid, resourceids=resourceids, parentresourceids=parentresourceids, devicetypes=devicetypes, compliancestatus=compliancestatus, customattributes=customattributes, customattributevalues=customattributevalues)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_product_compliance_issue_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group id which is similar to selected organization group selected in console. | [optional] 
 **resourceids** | **str**| list of resources, meaning device uuids, this isnt mandatory | [optional] [default to ]
 **parentresourceids** | **str**| list of proxy parent resources, meaning device uuids, this isnt mandatory | [optional] [default to ]
 **devicetypes** | **str**| list of device types to filter. | [optional] [default to ]
 **compliancestatus** | **int**| product compliance status id | [optional] 
 **customattributes** | **str**| custom attribute names | [optional] [default to ]
 **customattributevalues** | **str**| custom attribute values | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_product_compliance_issues**
> products_v1_product_compliance_issues(organizationgroupid=organizationgroupid, resourceids=resourceids, parentresourceids=parentresourceids, devicetypes=devicetypes, compliancestatus=compliancestatus, customattributse=customattributse, customattributevalues=customattributevalues, page=page, pagesize=pagesize)

New - Returns list of non-compliant devices for products in a OG

v1

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group id which is similar to selected organization group selected in console. (optional)
resourceids = '' # str | list of resources, meaning device uuids, this isnt mandatory (optional) (default to )
parentresourceids = '' # str | list of proxy parent resources, meaning device uuids, this isnt mandatory (optional) (default to )
devicetypes = '' # str | list of device types to filter. (optional) (default to )
compliancestatus = 56 # int | product compliance status id (optional)
customattributse = '' # str | custom attribute names (optional) (default to )
customattributevalues = '' # str | custom attribute values (optional) (default to )
page = 56 # int | Page number (optional)
pagesize = 56 # int | Maximum results which should be returned in each page. (optional)

try:
    # New - Returns list of non-compliant devices for products in a OG
    api_instance.products_v1_product_compliance_issues(organizationgroupid=organizationgroupid, resourceids=resourceids, parentresourceids=parentresourceids, devicetypes=devicetypes, compliancestatus=compliancestatus, customattributse=customattributse, customattributevalues=customattributevalues, page=page, pagesize=pagesize)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_product_compliance_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group id which is similar to selected organization group selected in console. | [optional] 
 **resourceids** | **str**| list of resources, meaning device uuids, this isnt mandatory | [optional] [default to ]
 **parentresourceids** | **str**| list of proxy parent resources, meaning device uuids, this isnt mandatory | [optional] [default to ]
 **devicetypes** | **str**| list of device types to filter. | [optional] [default to ]
 **compliancestatus** | **int**| product compliance status id | [optional] 
 **customattributse** | **str**| custom attribute names | [optional] [default to ]
 **customattributevalues** | **str**| custom attribute values | [optional] [default to ]
 **page** | **int**| Page number | [optional] 
 **pagesize** | **int**| Maximum results which should be returned in each page. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_product_extensive_search_async**
> ProductExtensiveSearchResult products_v1_product_extensive_search_async(productid=productid, organizationgroupid=organizationgroupid, modifiedfrom=modifiedfrom, modifiedtill=modifiedtill, managedbyorganizationgroupid=managedbyorganizationgroupid, name=name, platform=platform, customattributes=customattributes, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)

Returns the Products.

Returns the details of Products which satisfies the search parameter  <br />  *modifiedfrom, modifiedtill* fields accept the following  Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
productid = 56 # int | The Product Identifier. (optional)
organizationgroupid = 56 # int | The Organization Group Identifier. (optional)
modifiedfrom = '' # datetime | Modified from date time. (optional) (default to )
modifiedtill = '' # datetime | Modified till date time. (optional) (default to )
managedbyorganizationgroupid = 56 # int | The managed by Organization Group Identifier. (optional)
name = '' # str | Product name. Example: OS Upgrade 10. (optional) (default to )
platform = '' # str | Platform name. Example: Android. (optional) (default to )
customattributes = '' # str | Custom Attribute name. Example: Location. (optional) (default to )
orderby = '' # str | Order results by. Example: ProductId. (optional) (default to )
sortorder = '' # str | Sorts the result based on this attribute, i.e. ASC for Ascending order 'DESC' for descending order. Example: ASC. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximumm records per page. Default 500. (optional)

try:
    # Returns the Products.
    api_response = api_instance.products_v1_product_extensive_search_async(productid=productid, organizationgroupid=organizationgroupid, modifiedfrom=modifiedfrom, modifiedtill=modifiedtill, managedbyorganizationgroupid=managedbyorganizationgroupid, name=name, platform=platform, customattributes=customattributes, orderby=orderby, sortorder=sortorder, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_product_extensive_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **productid** | **int**| The Product Identifier. | [optional] 
 **organizationgroupid** | **int**| The Organization Group Identifier. | [optional] 
 **modifiedfrom** | **datetime**| Modified from date time. | [optional] [default to ]
 **modifiedtill** | **datetime**| Modified till date time. | [optional] [default to ]
 **managedbyorganizationgroupid** | **int**| The managed by Organization Group Identifier. | [optional] 
 **name** | **str**| Product name. Example: OS Upgrade 10. | [optional] [default to ]
 **platform** | **str**| Platform name. Example: Android. | [optional] [default to ]
 **customattributes** | **str**| Custom Attribute name. Example: Location. | [optional] [default to ]
 **orderby** | **str**| Order results by. Example: ProductId. | [optional] [default to ]
 **sortorder** | **str**| Sorts the result based on this attribute, i.e. ASC for Ascending order &#39;DESC&#39; for descending order. Example: ASC. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximumm records per page. Default 500. | [optional] 

### Return type

[**ProductExtensiveSearchResult**](ProductExtensiveSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_provisioning_jobs**
> ProvisioningJobsSearchResult products_v1_provisioning_jobs(organizationgroupid=organizationgroupid, deviceid=deviceid, modifieddatefrom=modifieddatefrom, modifieddateto=modifieddateto, page=page, pagesize=pagesize)

Returns jobs and associated products.

Returns jobs and associated products based on input parameters like Device Identifier, Organization Group Identifier, etc  <br />  *modifieddatefrom, modifieddateto* fields accept the following  Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group id which is similar to organization group selected in console. (optional)
deviceid = 56 # int | Device Id. (optional)
modifieddatefrom = '' # datetime | Modified date from. (optional) (default to )
modifieddateto = '' # datetime | Modified date to. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximumm records per page. Default 500. (optional)

try:
    # Returns jobs and associated products.
    api_response = api_instance.products_v1_provisioning_jobs(organizationgroupid=organizationgroupid, deviceid=deviceid, modifieddatefrom=modifieddatefrom, modifieddateto=modifieddateto, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_provisioning_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group id which is similar to organization group selected in console. | [optional] 
 **deviceid** | **int**| Device Id. | [optional] 
 **modifieddatefrom** | **datetime**| Modified date from. | [optional] [default to ]
 **modifieddateto** | **datetime**| Modified date to. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximumm records per page. Default 500. | [optional] 

### Return type

[**ProvisioningJobsSearchResult**](ProvisioningJobsSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_push_device_and_policy_on_policy_engine**
> products_v1_push_device_and_policy_on_policy_engine(deviceid, devicepolicyid, fasttrack=fasttrack)

Pushes the device and policy onto the policy engine.

Pushes the device and policy onto the policy engine based on the input Device Identifier and Device Policy Identifier.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
deviceid = 56 # int | DeviceId to insert. (Required).
devicepolicyid = 56 # int | PolicyId to insert. (Required).
fasttrack = 56 # int | Should the device be fast tracked (0 or 1). (optional)

try:
    # Pushes the device and policy onto the policy engine.
    api_instance.products_v1_push_device_and_policy_on_policy_engine(deviceid, devicepolicyid, fasttrack=fasttrack)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_push_device_and_policy_on_policy_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceid** | **int**| DeviceId to insert. (Required). | 
 **devicepolicyid** | **int**| PolicyId to insert. (Required). | 
 **fasttrack** | **int**| Should the device be fast tracked (0 or 1). | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_push_device_on_policy_engine**
> products_v1_push_device_on_policy_engine(id, fasttrack=fasttrack)

Pushes the device onto the product policy engine.

Pushes the device onto the product policy engine for processing.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Device Identifier to push (Required).
fasttrack = 56 # int | Should the device be fast tracked (0 or 1). (optional)

try:
    # Pushes the device onto the product policy engine.
    api_instance.products_v1_push_device_on_policy_engine(id, fasttrack=fasttrack)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_push_device_on_policy_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device Identifier to push (Required). | 
 **fasttrack** | **int**| Should the device be fast tracked (0 or 1). | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_remove_smart_group**
> products_v1_remove_smart_group(id, smartgroupid)

Removes SmartGroup from the specified Product.

Removes SmartGroup from the specified Product based on Product Identifier and Smart Group Identifier.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Identifier of the Product from which SmartGroup needs to be removed (Required).
smartgroupid = 56 # int | Identifier of the Smart Group which needs to be removed from the Product (Required).

try:
    # Removes SmartGroup from the specified Product.
    api_instance.products_v1_remove_smart_group(id, smartgroupid)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_remove_smart_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of the Product from which SmartGroup needs to be removed (Required). | 
 **smartgroupid** | **int**| Identifier of the Smart Group which needs to be removed from the Product (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_reprocess_product_async**
> MaintainResult products_v1_reprocess_product_async(reprocess_product_input_entity=reprocess_product_input_entity)

Initiates a reprocessing of a product.

Initiates a reprocessing of a product or product and device(s) by the policy engine. Supports a reprocess and a forced reprocess.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
reprocess_product_input_entity = mdmv1.ReprocessProductInputEntity() # ReprocessProductInputEntity | Object representing reprocessing details. (optional)

try:
    # Initiates a reprocessing of a product.
    api_response = api_instance.products_v1_reprocess_product_async(reprocess_product_input_entity=reprocess_product_input_entity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_reprocess_product_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reprocess_product_input_entity** | [**ReprocessProductInputEntity**](ReprocessProductInputEntity.md)| Object representing reprocessing details. | [optional] 

### Return type

[**MaintainResult**](MaintainResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_search**
> ProductSearchResult products_v1_search(name=name, organizationgroupid=organizationgroupid, managedbyorganizationgroupid=managedbyorganizationgroupid, platform=platform, smartgroupid=smartgroupid, orderby=orderby, sortorder=sortorder, modifiedfrom=modifiedfrom, modifiedtill=modifiedtill, page=page, pagesize=pagesize)

Searches for the products with the search parameters passed.

Searches for the products with the search parameters passed like Product Name, Organization Group Identifier, etc  <br />  *modifiedfrom, modifiedtill* fields accept the following  Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
name = '' # str | Product name. Example: OS Upgrade 10. (optional) (default to )
organizationgroupid = 56 # int | Organization group id which is similar to selected organization group selected in console. (optional)
managedbyorganizationgroupid = 56 # int | Managed by organization group id of the product. (optional)
platform = '' # str | Platform name. Example: Android. (optional) (default to )
smartgroupid = 56 # int | Smart Group Identifier. (optional)
orderby = '' # str | Orders the results by this attribute. Example: Name. (optional) (default to )
sortorder = '' # str | Sorts the result based on this attribute, i.e. ASC for Ascending order 'DESC' for descending order. Example: ASC. (optional) (default to )
modifiedfrom = '' # datetime | DateTime, Filters the result where product modified date is greater or equal to modifiedfrom value. (optional) (default to )
modifiedtill = '' # datetime | DateTime, Filters the result where product modified date is less or equal to modifiedtill value. (optional) (default to )
page = 56 # int | Specific page number to get. 0 based index. (optional)
pagesize = 56 # int | Maximumm records per page. Default 500. (optional)

try:
    # Searches for the products with the search parameters passed.
    api_response = api_instance.products_v1_search(name=name, organizationgroupid=organizationgroupid, managedbyorganizationgroupid=managedbyorganizationgroupid, platform=platform, smartgroupid=smartgroupid, orderby=orderby, sortorder=sortorder, modifiedfrom=modifiedfrom, modifiedtill=modifiedtill, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Product name. Example: OS Upgrade 10. | [optional] [default to ]
 **organizationgroupid** | **int**| Organization group id which is similar to selected organization group selected in console. | [optional] 
 **managedbyorganizationgroupid** | **int**| Managed by organization group id of the product. | [optional] 
 **platform** | **str**| Platform name. Example: Android. | [optional] [default to ]
 **smartgroupid** | **int**| Smart Group Identifier. | [optional] 
 **orderby** | **str**| Orders the results by this attribute. Example: Name. | [optional] [default to ]
 **sortorder** | **str**| Sorts the result based on this attribute, i.e. ASC for Ascending order &#39;DESC&#39; for descending order. Example: ASC. | [optional] [default to ]
 **modifiedfrom** | **datetime**| DateTime, Filters the result where product modified date is greater or equal to modifiedfrom value. | [optional] [default to ]
 **modifiedtill** | **datetime**| DateTime, Filters the result where product modified date is less or equal to modifiedtill value. | [optional] [default to ]
 **page** | **int**| Specific page number to get. 0 based index. | [optional] 
 **pagesize** | **int**| Maximumm records per page. Default 500. | [optional] 

### Return type

[**ProductSearchResult**](ProductSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_set_product_install_time**
> products_v1_set_product_install_time(id, install_time)

Sets the product install time.

Sets the product install time based on input Product Identifier and Install Time.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Product identifer for which the Install time has to be specified (Required).
install_time = mdmv1.InstallTime() # InstallTime | DateTime in UTC and 24 hour format. The required format is YYYYMMDD HH:MM (Required).

try:
    # Sets the product install time.
    api_instance.products_v1_set_product_install_time(id, install_time)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_set_product_install_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Product identifer for which the Install time has to be specified (Required). | 
 **install_time** | [**InstallTime**](InstallTime.md)| DateTime in UTC and 24 hour format. The required format is YYYYMMDD HH:MM (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_v1_update_product**
> products_v1_update_product(id, product)

Updates the product details.

Updates the product details based on Product Identifier and Product properties like Name, Organization Group Identifier, etc.

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
api_instance = mdmv1.ProductsV1Api(mdmv1.ApiClient(configuration))
id = 56 # int | Product identifier (Required).
product = mdmv1.ProductModel_() # ProductModel_ | Details of product to be edited (Required).

try:
    # Updates the product details.
    api_instance.products_v1_update_product(id, product)
except ApiException as e:
    print("Exception when calling ProductsV1Api->products_v1_update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Product identifier (Required). | 
 **product** | [**ProductModel_**](ProductModel_.md)| Details of product to be edited (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

