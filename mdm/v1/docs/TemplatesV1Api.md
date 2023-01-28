# mdmv1.TemplatesV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**templates_v1_get_all_async**](TemplatesV1Api.md#templates_v1_get_all_async) | **GET** /baselines/templates | New - Fetch GPO templates
[**templates_v1_get_policy_async**](TemplatesV1Api.md#templates_v1_get_policy_async) | **GET** /baselines/templates/{baselineTemplateUUID}/policies/{policyUUID} | New - Fetch a policy with it&#39;s recommended values
[**templates_v1_search_template_async**](TemplatesV1Api.md#templates_v1_search_template_async) | **GET** /baselines/templates/search/{vendorTemplateUUID} | New - Find a vendor template


# **templates_v1_get_all_async**
> list[BaselineVendorTemplateV1Model] templates_v1_get_all_async()

New - Fetch GPO templates

Returns a list of GPO security baseline templates provided by various vendors.

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
api_instance = mdmv1.TemplatesV1Api(mdmv1.ApiClient(configuration))

try:
    # New - Fetch GPO templates
    api_response = api_instance.templates_v1_get_all_async()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesV1Api->templates_v1_get_all_async: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BaselineVendorTemplateV1Model]**](BaselineVendorTemplateV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_v1_get_policy_async**
> PolicyModel templates_v1_get_policy_async(baseline_template_uuid, policy_uuid, language=language)

New - Fetch a policy with it's recommended values

Returns a policy with it's options localized for a selected language and recommended values

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

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
api_instance = mdmv1.TemplatesV1Api(mdmv1.ApiClient(configuration))
baseline_template_uuid = 'baseline_template_uuid_example' # str | The baseline template unique identifier(Required)
policy_uuid = 'policy_uuid_example' # str | The policy identifier(Required)
language = '' # str | The language code (Default en-US) (optional) (default to )

try:
    # New - Fetch a policy with it's recommended values
    api_response = api_instance.templates_v1_get_policy_async(baseline_template_uuid, policy_uuid, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesV1Api->templates_v1_get_policy_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baseline_template_uuid** | [**str**](.md)| The baseline template unique identifier(Required) | 
 **policy_uuid** | [**str**](.md)| The policy identifier(Required) | 
 **language** | **str**| The language code (Default en-US) | [optional] [default to ]

### Return type

[**PolicyModel**](PolicyModel.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_v1_search_template_async**
> BaselineTemplate templates_v1_search_template_async(vendor_template_uuid, os_version_uuid, security_level_uuid=security_level_uuid, policy_tree=policy_tree, language=language)

New - Find a vendor template

Returns a GPO security baseline template provided by a vendor.

### Example
```python
from __future__ import print_function
import time
import mdmv1
from mdmv1.rest import ApiException
from pprint import pprint

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
api_instance = mdmv1.TemplatesV1Api(mdmv1.ApiClient(configuration))
vendor_template_uuid = 'vendor_template_uuid_example' # str | The vendor template identifier(Required)
os_version_uuid =  # object | The operating system version identifier(Required) (default to )
security_level_uuid =  # object | The security level identifier (optional) (default to )
policy_tree =  # bool | load the policy tree (optional) (default to )
language = '' # str | The language code (Default en-US) (optional) (default to )

try:
    # New - Find a vendor template
    api_response = api_instance.templates_v1_search_template_async(vendor_template_uuid, os_version_uuid, security_level_uuid=security_level_uuid, policy_tree=policy_tree, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesV1Api->templates_v1_search_template_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_template_uuid** | [**str**](.md)| The vendor template identifier(Required) | 
 **os_version_uuid** | [**object**](.md)| The operating system version identifier(Required) | [default to ]
 **security_level_uuid** | [**object**](.md)| The security level identifier | [optional] [default to ]
 **policy_tree** | **bool**| load the policy tree | [optional] [default to ]
 **language** | **str**| The language code (Default en-US) | [optional] [default to ]

### Return type

[**BaselineTemplate**](BaselineTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

