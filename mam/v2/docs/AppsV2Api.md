# mamv2.AppsV2Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_v2_get_app_config_template_async**](AppsV2Api.md#apps_v2_get_app_config_template_async) | **GET** /apps/{applicationUuid}/app-config-template | New - Get app config template for an application.
[**apps_v2_get_assignment_rule_async**](AppsV2Api.md#apps_v2_get_assignment_rule_async) | **GET** /apps/{applicationUuid}/assignment-rules | New - Get assignment rule for an application.
[**apps_v2_update_assignment_rule_async**](AppsV2Api.md#apps_v2_update_assignment_rule_async) | **PUT** /apps/{applicationUuid}/assignment-rules | New - Updates assignment rule for an application and publishes the application to the devices associated with assignment rule.


# **apps_v2_get_app_config_template_async**
> list[AppConfigTemplateV2Model] apps_v2_get_app_config_template_async(application_uuid, organization_group_uuid=organization_group_uuid)

New - Get app config template for an application.

Get list of app configs supported for an application based on the application uuid provided.

### Example
```python
from __future__ import print_function
import time
import mamv2
from mamv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv2.AppsV2Api(mamv2.ApiClient(configuration))
application_uuid = 'application_uuid_example' # str | Unique identifier for the application.              Accepted formats **uuid**              example: 3d958f38-246e-4854-a306-189d941ab073(Required).
organization_group_uuid =  # object | Current Organization Group identifier for which admin is trying to get the template and from where assigment of the given app will happen. Accepted formats **uuid**              example: 3d958f38-246e-4854-a306-189d941ab073 (optional) (default to )

try:
    # New - Get app config template for an application.
    api_response = api_instance.apps_v2_get_app_config_template_async(application_uuid, organization_group_uuid=organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsV2Api->apps_v2_get_app_config_template_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | [**str**](.md)| Unique identifier for the application.              Accepted formats **uuid**              example: 3d958f38-246e-4854-a306-189d941ab073(Required). | 
 **organization_group_uuid** | [**object**](.md)| Current Organization Group identifier for which admin is trying to get the template and from where assigment of the given app will happen. Accepted formats **uuid**              example: 3d958f38-246e-4854-a306-189d941ab073 | [optional] [default to ]

### Return type

[**list[AppConfigTemplateV2Model]**](AppConfigTemplateV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=2, application/xml;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_v2_get_assignment_rule_async**
> AppAssignmentRuleV2Model apps_v2_get_assignment_rule_async(application_uuid)

New - Get assignment rule for an application.

Get assignment rule which contains deployment parameters for assignments and smart group exclusions for an application.

### Example
```python
from __future__ import print_function
import time
import mamv2
from mamv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv2.AppsV2Api(mamv2.ApiClient(configuration))
application_uuid = 'application_uuid_example' # str | Unique identifier for the application.              Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required)

try:
    # New - Get assignment rule for an application.
    api_response = api_instance.apps_v2_get_assignment_rule_async(application_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsV2Api->apps_v2_get_assignment_rule_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | [**str**](.md)| Unique identifier for the application.              Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required) | 

### Return type

[**AppAssignmentRuleV2Model**](AppAssignmentRuleV2Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_v2_update_assignment_rule_async**
> apps_v2_update_assignment_rule_async(application_uuid, assignment_rule)

New - Updates assignment rule for an application and publishes the application to the devices associated with assignment rule.

Updates assignments with assignment policies and exclusions for an application. Publishes the application to the devices associated with the assignment rule.

### Example
```python
from __future__ import print_function
import time
import mamv2
from mamv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv2.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv2.AppsV2Api(mamv2.ApiClient(configuration))
application_uuid = 'application_uuid_example' # str | Unique identifier for the application.              Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required)
assignment_rule = mamv2.AppAssignmentRuleV2Model() # AppAssignmentRuleV2Model | Assignment rule which contains list of assignments and exclusions for an application.(Required)

try:
    # New - Updates assignment rule for an application and publishes the application to the devices associated with assignment rule.
    api_instance.apps_v2_update_assignment_rule_async(application_uuid, assignment_rule)
except ApiException as e:
    print("Exception when calling AppsV2Api->apps_v2_update_assignment_rule_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | [**str**](.md)| Unique identifier for the application.              Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required) | 
 **assignment_rule** | [**AppAssignmentRuleV2Model**](AppAssignmentRuleV2Model.md)| Assignment rule which contains list of assignments and exclusions for an application.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json;version=2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

