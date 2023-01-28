# mdmv1.ProductSetV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_set_v1_activate_product_in_product_set**](ProductSetV1Api.md#product_set_v1_activate_product_in_product_set) | **POST** /productsets/ActivateProductInProductSet | Activates a product in a Product Set.
[**product_set_v1_deactivate_product_in_product_set**](ProductSetV1Api.md#product_set_v1_deactivate_product_in_product_set) | **POST** /productsets/DeactivateProductInProduct | Deactivates a product in a Product Set.
[**product_set_v1_maintain_product_in_product_set_async**](ProductSetV1Api.md#product_set_v1_maintain_product_in_product_set_async) | **POST** /productsets/MaintainProductInProductSet | Adds a product to or modifies an existing product in a Product Set.
[**product_set_v1_maintain_product_set_async**](ProductSetV1Api.md#product_set_v1_maintain_product_set_async) | **POST** /productsets/maintainProductSet | Creates or updates a Product Set.
[**product_set_v1_product_set_inquiry**](ProductSetV1Api.md#product_set_v1_product_set_inquiry) | **GET** /productsets/ProductSetInquiry | Retrieves information about a Product Set and the included products.
[**product_set_v1_push_product_set_on_policy_engine**](ProductSetV1Api.md#product_set_v1_push_product_set_on_policy_engine) | **POST** /productsets/pushproductsetonpolicyengine | Pushes the Product Set onto the product policy engine.
[**product_set_v1_rank_all_products_in_product_set**](ProductSetV1Api.md#product_set_v1_rank_all_products_in_product_set) | **POST** /productsets/RankAllProductsInProductSet | Reranks all products in a Product Set.
[**product_set_v1_remove_product_from_product_set**](ProductSetV1Api.md#product_set_v1_remove_product_from_product_set) | **DELETE** /productsets/RemoveProductFromProductSet/{ogId}/{productSetIdOrName}/{productIdOrName} | Deletes a product from a Product Set.


# **product_set_v1_activate_product_in_product_set**
> MaintainResult product_set_v1_activate_product_in_product_set(product_set_id, product_id)

Activates a product in a Product Set.

Activates a product in a Product Set when Product Set and Product Id are passed .

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
api_instance = mdmv1.ProductSetV1Api(mdmv1.ApiClient(configuration))
product_set_id = 56 # int | Product Set ID. (Required).
product_id = 56 # int | Product ID. (Required).

try:
    # Activates a product in a Product Set.
    api_response = api_instance.product_set_v1_activate_product_in_product_set(product_set_id, product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSetV1Api->product_set_v1_activate_product_in_product_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_set_id** | **int**| Product Set ID. (Required). | 
 **product_id** | **int**| Product ID. (Required). | 

### Return type

[**MaintainResult**](MaintainResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_set_v1_deactivate_product_in_product_set**
> MaintainResult product_set_v1_deactivate_product_in_product_set(product_set_id, product_id)

Deactivates a product in a Product Set.

Deactivates a product in a Product Set when Product Set and Product Id are passed.

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
api_instance = mdmv1.ProductSetV1Api(mdmv1.ApiClient(configuration))
product_set_id = 56 # int | Product Set ID. (Required).
product_id = 56 # int | Product ID. (Required).

try:
    # Deactivates a product in a Product Set.
    api_response = api_instance.product_set_v1_deactivate_product_in_product_set(product_set_id, product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSetV1Api->product_set_v1_deactivate_product_in_product_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_set_id** | **int**| Product Set ID. (Required). | 
 **product_id** | **int**| Product ID. (Required). | 

### Return type

[**MaintainResult**](MaintainResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_set_v1_maintain_product_in_product_set_async**
> MaintainResult product_set_v1_maintain_product_in_product_set_async(maintain_product_in_product_set_model=maintain_product_in_product_set_model)

Adds a product to or modifies an existing product in a Product Set.

Adds a product to or modifies an existing product in a Product Set when product details are passed.

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
api_instance = mdmv1.ProductSetV1Api(mdmv1.ApiClient(configuration))
maintain_product_in_product_set_model = mdmv1.MaintainProductInProductSetModel() # MaintainProductInProductSetModel | Input representing product to be added or modified in a product set, Organization group. (optional)

try:
    # Adds a product to or modifies an existing product in a Product Set.
    api_response = api_instance.product_set_v1_maintain_product_in_product_set_async(maintain_product_in_product_set_model=maintain_product_in_product_set_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSetV1Api->product_set_v1_maintain_product_in_product_set_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintain_product_in_product_set_model** | [**MaintainProductInProductSetModel**](MaintainProductInProductSetModel.md)| Input representing product to be added or modified in a product set, Organization group. | [optional] 

### Return type

[**MaintainResult**](MaintainResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_set_v1_maintain_product_set_async**
> MaintainResult product_set_v1_maintain_product_set_async(maintain_product_set_input_entity=maintain_product_set_input_entity)

Creates or updates a Product Set.

Creates or updates a product set when Product Set details are provided.

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
api_instance = mdmv1.ProductSetV1Api(mdmv1.ApiClient(configuration))
maintain_product_set_input_entity = mdmv1.MaintainProductSetModel() # MaintainProductSetModel | Input representing product set, Organization group and insertOnly flag. (optional)

try:
    # Creates or updates a Product Set.
    api_response = api_instance.product_set_v1_maintain_product_set_async(maintain_product_set_input_entity=maintain_product_set_input_entity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSetV1Api->product_set_v1_maintain_product_set_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintain_product_set_input_entity** | [**MaintainProductSetModel**](MaintainProductSetModel.md)| Input representing product set, Organization group and insertOnly flag. | [optional] 

### Return type

[**MaintainResult**](MaintainResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_set_v1_product_set_inquiry**
> ProductSetInquiryResponseModel product_set_v1_product_set_inquiry(organization_group_id=organization_group_id, product_set_name=product_set_name, product_set_id=product_set_id)

Retrieves information about a Product Set and the included products.

Retrieves information about a Product Set and the list of products in the Product Set.

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
api_instance = mdmv1.ProductSetV1Api(mdmv1.ApiClient(configuration))
organization_group_id = 56 # int | Organization Group ID. (optional)
product_set_name = '' # str | ProductSet Name. (optional) (default to )
product_set_id = 56 # int | ProductSet ID. (optional)

try:
    # Retrieves information about a Product Set and the included products.
    api_response = api_instance.product_set_v1_product_set_inquiry(organization_group_id=organization_group_id, product_set_name=product_set_name, product_set_id=product_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSetV1Api->product_set_v1_product_set_inquiry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_id** | **int**| Organization Group ID. | [optional] 
 **product_set_name** | **str**| ProductSet Name. | [optional] [default to ]
 **product_set_id** | **int**| ProductSet ID. | [optional] 

### Return type

[**ProductSetInquiryResponseModel**](ProductSetInquiryResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_set_v1_push_product_set_on_policy_engine**
> product_set_v1_push_product_set_on_policy_engine(product_set_id, fasttrack)

Pushes the Product Set onto the product policy engine.

Pushes the Product Set onto the product policy engine when Product Set ID and fasttrack parameters are passed.

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
api_instance = mdmv1.ProductSetV1Api(mdmv1.ApiClient(configuration))
product_set_id = 56 # int | Product Set ID. (Required).
fasttrack = 56 # int | Should the device be fast tracked. (Required).

try:
    # Pushes the Product Set onto the product policy engine.
    api_instance.product_set_v1_push_product_set_on_policy_engine(product_set_id, fasttrack)
except ApiException as e:
    print("Exception when calling ProductSetV1Api->product_set_v1_push_product_set_on_policy_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_set_id** | **int**| Product Set ID. (Required). | 
 **fasttrack** | **int**| Should the device be fast tracked. (Required). | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_set_v1_rank_all_products_in_product_set**
> MaintainResult product_set_v1_rank_all_products_in_product_set(rank_all_products_in_product_set_input_entity=rank_all_products_in_product_set_input_entity)

Reranks all products in a Product Set.

Reranks all products in a Product Set with the specified parameters.

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
api_instance = mdmv1.ProductSetV1Api(mdmv1.ApiClient(configuration))
rank_all_products_in_product_set_input_entity = mdmv1.RankAllProductsInProductSetInputEntity() # RankAllProductsInProductSetInputEntity | Input representing product rankings in a product set, Organziation Group. (optional)

try:
    # Reranks all products in a Product Set.
    api_response = api_instance.product_set_v1_rank_all_products_in_product_set(rank_all_products_in_product_set_input_entity=rank_all_products_in_product_set_input_entity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSetV1Api->product_set_v1_rank_all_products_in_product_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rank_all_products_in_product_set_input_entity** | [**RankAllProductsInProductSetInputEntity**](RankAllProductsInProductSetInputEntity.md)| Input representing product rankings in a product set, Organziation Group. | [optional] 

### Return type

[**MaintainResult**](MaintainResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_set_v1_remove_product_from_product_set**
> MaintainResult product_set_v1_remove_product_from_product_set(og_id, product_set_id_or_name, product_id_or_name)

Deletes a product from a Product Set.

Deletes a product from a Product Set when Organization Group Id,Product Set and the product to be deleted in product set are provided.

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
api_instance = mdmv1.ProductSetV1Api(mdmv1.ApiClient(configuration))
og_id = 'og_id_example' # str | The Organization Group Id of the ProductSet. (Required).
product_set_id_or_name = 'product_set_id_or_name_example' # str | Product Set containing the product to be deleted. (Required).
product_id_or_name = 'product_id_or_name_example' # str | The product to be deleted. (Required).

try:
    # Deletes a product from a Product Set.
    api_response = api_instance.product_set_v1_remove_product_from_product_set(og_id, product_set_id_or_name, product_id_or_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSetV1Api->product_set_v1_remove_product_from_product_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **og_id** | **str**| The Organization Group Id of the ProductSet. (Required). | 
 **product_set_id_or_name** | **str**| Product Set containing the product to be deleted. (Required). | 
 **product_id_or_name** | **str**| The product to be deleted. (Required). | 

### Return type

[**MaintainResult**](MaintainResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

