# mamv1.AppsApi

All URIs are relative to *https://awapi.delimitize.com/API/mam*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_get_app_action_breakdown_counts**](AppsApi.md#apps_get_app_action_breakdown_counts) | **GET** /apps/{uuid}/actioncounts | New - Gets the device count for the application actions
[**apps_get_app_config_template_async**](AppsApi.md#apps_get_app_config_template_async) | **GET** /apps/{applicationUuid}/app-config-template | New - Get app config template for an application.
[**apps_get_app_deployment_counts**](AppsApi.md#apps_get_app_deployment_counts) | **GET** /apps/{uuid}/deploymentcounts | New - Gets the deployment counts for an internal or public app
[**apps_get_app_management_status**](AppsApi.md#apps_get_app_management_status) | **GET** /apps/managementstatus | Retrieves the application management status, i.e. the application bundle id passed is managedby AirWatch or not.
[**apps_get_app_reason_breakdown_counts**](AppsApi.md#apps_get_app_reason_breakdown_counts) | **GET** /apps/{uuid}/reasoncounts | New - Gets the device count for the application reasons
[**apps_get_app_removal_protection_logs**](AppsApi.md#apps_get_app_removal_protection_logs) | **GET** /apps/removallogs | Returns removal log events for an internal application, filtered by the App bundle identifier of the application and organization group.
[**apps_get_assignment_rule_async**](AppsApi.md#apps_get_assignment_rule_async) | **GET** /apps/{applicationUuid}/assignment-rule | New - Get assignment rule for an application.
[**apps_get_devices_assigned_or_installed_for_app_at_version_level**](AppsApi.md#apps_get_devices_assigned_or_installed_for_app_at_version_level) | **GET** /apps/{uuid}/devices | New - Gets list of devices that have the specified internal or public application installed or assigned.
[**apps_get_sdk_ananlytics**](AppsApi.md#apps_get_sdk_ananlytics) | **POST** /apps/sdkanalytics | Gets SDK analytics based on the query information provided.
[**apps_search_apple_store_async**](AppsApi.md#apps_search_apple_store_async) | **GET** /apps/applestore/search | Searches in App stores for the applications with the specified search string and returns the details.
[**apps_search_async**](AppsApi.md#apps_search_async) | **GET** /apps/search | Search and retrieve details for both internal and external applications or books.
[**apps_update_admin_action_taken_on_app_removal_protection_logs**](AppsApi.md#apps_update_admin_action_taken_on_app_removal_protection_logs) | **PUT** /apps/removallogs | Sets the action (unlock or clear) executed after the threshold for the Removal Log events is reached.
[**apps_update_assignment_rule_async**](AppsApi.md#apps_update_assignment_rule_async) | **PUT** /apps/{applicationUuid}/assignment-rule | New - Updates assignment rule for an application and publishes the application to the devices associated with assignment rule.
[**apps_windows_store_search_async**](AppsApi.md#apps_windows_store_search_async) | **GET** /apps/windowsstore/search | Retrieves the details of the applications from the Windows App Store based on the search request.


# **apps_get_app_action_breakdown_counts**
> AppActionBreakDownModel apps_get_app_action_breakdown_counts(uuid, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids)

New - Gets the device count for the application actions

Will return the device count per application last action taken for the application

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
uuid = 'uuid_example' # str | The uuid of the application.               Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required)
organizationgroupuuid =  # object | The organization group identifier where the counts need to be fetched. Will be defaulted to admin organization group identifier if not set. E.g. EF331D65-C005-4388-8E52-B1390AA171D9 (optional) (default to )
smartgroupuuids = '' # str | Comma separated list of smart group uuids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. EF331D65-C005-4388-8E52-B1390AA171D9, EF331D65-C005-4388-8E52-B1390AA172D9 (optional) (default to )

try:
    # New - Gets the device count for the application actions
    api_response = api_instance.apps_get_app_action_breakdown_counts(uuid, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get_app_action_breakdown_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The uuid of the application.               Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required) | 
 **organizationgroupuuid** | [**object**](.md)| The organization group identifier where the counts need to be fetched. Will be defaulted to admin organization group identifier if not set. E.g. EF331D65-C005-4388-8E52-B1390AA171D9 | [optional] [default to ]
 **smartgroupuuids** | **str**| Comma separated list of smart group uuids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. EF331D65-C005-4388-8E52-B1390AA171D9, EF331D65-C005-4388-8E52-B1390AA172D9 | [optional] [default to ]

### Return type

[**AppActionBreakDownModel**](AppActionBreakDownModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_app_config_template_async**
> list[AppConfigTemplateV1Model] apps_get_app_config_template_async(application_uuid, organization_group_uuid=organization_group_uuid)

New - Get app config template for an application.

Get list of app configs supported for an application based on the application uuid provided.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
application_uuid = 'application_uuid_example' # str | Unique identifier for the application.               Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required)
organization_group_uuid =  # object | Current Organization Group identifier for which admin is trying to get the template and from where assigment of the given app will happen. Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073 (optional) (default to )

try:
    # New - Get app config template for an application.
    api_response = api_instance.apps_get_app_config_template_async(application_uuid, organization_group_uuid=organization_group_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get_app_config_template_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | [**str**](.md)| Unique identifier for the application.               Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required) | 
 **organization_group_uuid** | [**object**](.md)| Current Organization Group identifier for which admin is trying to get the template and from where assigment of the given app will happen. Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073 | [optional] [default to ]

### Return type

[**list[AppConfigTemplateV1Model]**](AppConfigTemplateV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/template;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_app_deployment_counts**
> AppVersionLevelCountModel apps_get_app_deployment_counts(uuid, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids)

New - Gets the deployment counts for an internal or public app

Will return the following information for internal/public application in the provided Organization Group. 1. Total assigned devices count 2. Total installed devices count 3. Total side loaded devices count

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
uuid = 'uuid_example' # str | The uuid of the application.               Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required)
organizationgroupuuid =  # object | The Organization Group identifier in which the counts need to be fetched. Will be defaulted to admin Organization Group identifier if not set. E.g. EF331D65-C005-4388-8E52-B1390AA171D9 (optional) (default to )
smartgroupuuids = '' # str | Comma separated list of smart group uuids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. EF331D65-C005-4388-8E52-B1390AA171D9, EF331D65-C005-4388-8E52-B1390AA172D9 (optional) (default to )

try:
    # New - Gets the deployment counts for an internal or public app
    api_response = api_instance.apps_get_app_deployment_counts(uuid, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get_app_deployment_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The uuid of the application.               Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required) | 
 **organizationgroupuuid** | [**object**](.md)| The Organization Group identifier in which the counts need to be fetched. Will be defaulted to admin Organization Group identifier if not set. E.g. EF331D65-C005-4388-8E52-B1390AA171D9 | [optional] [default to ]
 **smartgroupuuids** | **str**| Comma separated list of smart group uuids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. EF331D65-C005-4388-8E52-B1390AA171D9, EF331D65-C005-4388-8E52-B1390AA172D9 | [optional] [default to ]

### Return type

[**AppVersionLevelCountModel**](AppVersionLevelCountModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_app_management_status**
> apps_get_app_management_status(managementid=managementid, bundleid=bundleid)

Retrieves the application management status, i.e. the application bundle id passed is managedby AirWatch or not.

v1.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
managementid = '' # str | Management Id. (optional) (default to )
bundleid = '' # str | Bundle Id. (optional) (default to )

try:
    # Retrieves the application management status, i.e. the application bundle id passed is managedby AirWatch or not.
    api_instance.apps_get_app_management_status(managementid=managementid, bundleid=bundleid)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get_app_management_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managementid** | **str**| Management Id. | [optional] [default to ]
 **bundleid** | **str**| Bundle Id. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_app_reason_breakdown_counts**
> AppReasonBreakDownModel apps_get_app_reason_breakdown_counts(uuid, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids)

New - Gets the device count for the application reasons

Will return the device count per application reason for the application

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
uuid = 'uuid_example' # str | The uuid of the application.               Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required)
organizationgroupuuid =  # object | The Organization Group identifier where the counts need to be fetched. Will be defaulted to admin Organization Group identifier if not set. E.g. EF331D65-C005-4388-8E52-B1390AA171D9 (optional) (default to )
smartgroupuuids = '' # str | Comma separated list of smart group uuids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. EF331D65-C005-4388-8E52-B1390AA171D9, EF331D65-C005-4388-8E52-B1390AA172D9 (optional) (default to )

try:
    # New - Gets the device count for the application reasons
    api_response = api_instance.apps_get_app_reason_breakdown_counts(uuid, organizationgroupuuid=organizationgroupuuid, smartgroupuuids=smartgroupuuids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get_app_reason_breakdown_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The uuid of the application.               Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required) | 
 **organizationgroupuuid** | [**object**](.md)| The Organization Group identifier where the counts need to be fetched. Will be defaulted to admin Organization Group identifier if not set. E.g. EF331D65-C005-4388-8E52-B1390AA171D9 | [optional] [default to ]
 **smartgroupuuids** | **str**| Comma separated list of smart group uuids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. EF331D65-C005-4388-8E52-B1390AA171D9, EF331D65-C005-4388-8E52-B1390AA172D9 | [optional] [default to ]

### Return type

[**AppReasonBreakDownModel**](AppReasonBreakDownModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_app_removal_protection_logs**
> AppRemovalProtectionLogSearchResultModel apps_get_app_removal_protection_logs(bundleid=bundleid, organizationgroupid=organizationgroupid, status=status, page=page, pagesize=pagesize, orderby=orderby)

Returns removal log events for an internal application, filtered by the App bundle identifier of the application and organization group.

Search and retrieve removal logs for internal applications.              If the number of remove application commands queued in a set time interval is exceeded the commands are put in locked state              The API method returns the details of the commands that are put in locked state              The records returned take into consideration the filter criteria received in request query.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
bundleid = '' # str | BundleId/PackageId.Example = \"com.test.testapp\". (optional) (default to )
organizationgroupid = '' # str | OrganizationGroup Identifier. Example = \"890\". (optional) (default to )
status = '' # str | The AppRemoval Log Threshold Status.Example = \"3\". (optional) (default to )
page = '' # str | Page number.Example = \"2\". (optional) (default to )
pagesize = '' # str | Records per page.Example = \"10\". (optional) (default to )
orderby = '' # str | Orderby column name.Example = \"ThresholdId\". (optional) (default to )

try:
    # Returns removal log events for an internal application, filtered by the App bundle identifier of the application and organization group.
    api_response = api_instance.apps_get_app_removal_protection_logs(bundleid=bundleid, organizationgroupid=organizationgroupid, status=status, page=page, pagesize=pagesize, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get_app_removal_protection_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundleid** | **str**| BundleId/PackageId.Example &#x3D; \&quot;com.test.testapp\&quot;. | [optional] [default to ]
 **organizationgroupid** | **str**| OrganizationGroup Identifier. Example &#x3D; \&quot;890\&quot;. | [optional] [default to ]
 **status** | **str**| The AppRemoval Log Threshold Status.Example &#x3D; \&quot;3\&quot;. | [optional] [default to ]
 **page** | **str**| Page number.Example &#x3D; \&quot;2\&quot;. | [optional] [default to ]
 **pagesize** | **str**| Records per page.Example &#x3D; \&quot;10\&quot;. | [optional] [default to ]
 **orderby** | **str**| Orderby column name.Example &#x3D; \&quot;ThresholdId\&quot;. | [optional] [default to ]

### Return type

[**AppRemovalProtectionLogSearchResultModel**](AppRemovalProtectionLogSearchResultModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_assignment_rule_async**
> AppAssignmentRuleV1Model apps_get_assignment_rule_async(application_uuid)

New - Get assignment rule for an application.

Get assignment rule which contains deployment parameters for assignments and smart group exclusions for an application.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
application_uuid = 'application_uuid_example' # str | Unique identifier for the application.              Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required)

try:
    # New - Get assignment rule for an application.
    api_response = api_instance.apps_get_assignment_rule_async(application_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get_assignment_rule_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | [**str**](.md)| Unique identifier for the application.              Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required) | 

### Return type

[**AppAssignmentRuleV1Model**](AppAssignmentRuleV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_devices_assigned_or_installed_for_app_at_version_level**
> DevicesPagedSearchResultsModel apps_get_devices_assigned_or_installed_for_app_at_version_level(uuid, page=page, organizationgroupuuid=organizationgroupuuid, pagesize=pagesize, searchtext=searchtext, sortorder=sortorder, orderby=orderby, smartgroupids=smartgroupids, isassigned=isassigned, isnotassigned=isnotassigned, isexcluded=isexcluded, isinstalled=isinstalled, isnotinstalled=isnotinstalled, installationstatus=installationstatus, lastactiontaken=lastactiontaken)

New - Gets list of devices that have the specified internal or public application installed or assigned.

This endpoint provides a list of devices that have the specified internal or public application installed or assigned at the version level. A list of all the assigned devices is returned by default.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
uuid = 'uuid_example' # str | The uuid of the application.               Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required)
page = 56 # int | Page number which will be fetched, 0 based index. Default 0. (optional)
organizationgroupuuid =  # object | The Organization Group identifier in which the counts need to be fetched. Will be defaulted to admin organization group identifier if not set. E.g. EF331D65-C005-4388-8E52-B1390AA171D9 (optional) (default to )
pagesize = 56 # int | Maximum number of results to be returned in one page. Default 500. (optional)
searchtext = '' # str | If provided, the records matching this text will be returned. The search will be applied on the following properties [name, installed_version, assigned_version]. The default value will be empty string. (optional) (default to )
sortorder = '' # str | Whether the sort order is ascending or descending. The property used for sorting is name. Possible values [Asc, Desc]. Default value is Asc. (optional) (default to )
orderby = '' # str | Name of the property used for sorting (optional) (default to )
smartgroupids = '' # str | Comma separated list of smart group ids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. 10, 20 (optional) (default to )
isassigned =  # bool | If provided, the list of devices on which the app is assigned is included in the returned result set. Default false. (optional) (default to )
isnotassigned =  # bool | If provided, the list of devices on which the app is sideloaded or marked for removal but not assigned is included in the returned result set. Default false. (optional) (default to )
isexcluded =  # bool | If provided, the list of devices on which the app is excluded is included in the returned result set. Default false. (optional) (default to )
isinstalled =  # bool | if provided, the list of devices on which the app is installed is included in the returned result set. Default false. (optional) (default to )
isnotinstalled =  # bool | if provided, the list of devices on which the app is not installed but assigned is included in the returned result set. Default false. (optional) (default to )
installationstatus =  # object | Comma separated list of managed application list reasons to which the devices assigned to the app belong. If no reason is passed, all the assigned devices will be returned based on the other filters. (optional) (default to )
lastactiontaken =  # object | Comma separated list of application deployment status to which the devices assigned to the app belong. If no deployment status is passed, all the assigned devices will be returned based on the other filters. (optional) (default to )

try:
    # New - Gets list of devices that have the specified internal or public application installed or assigned.
    api_response = api_instance.apps_get_devices_assigned_or_installed_for_app_at_version_level(uuid, page=page, organizationgroupuuid=organizationgroupuuid, pagesize=pagesize, searchtext=searchtext, sortorder=sortorder, orderby=orderby, smartgroupids=smartgroupids, isassigned=isassigned, isnotassigned=isnotassigned, isexcluded=isexcluded, isinstalled=isinstalled, isnotinstalled=isnotinstalled, installationstatus=installationstatus, lastactiontaken=lastactiontaken)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get_devices_assigned_or_installed_for_app_at_version_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The uuid of the application.               Accepted formats **guid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required) | 
 **page** | **int**| Page number which will be fetched, 0 based index. Default 0. | [optional] 
 **organizationgroupuuid** | [**object**](.md)| The Organization Group identifier in which the counts need to be fetched. Will be defaulted to admin organization group identifier if not set. E.g. EF331D65-C005-4388-8E52-B1390AA171D9 | [optional] [default to ]
 **pagesize** | **int**| Maximum number of results to be returned in one page. Default 500. | [optional] 
 **searchtext** | **str**| If provided, the records matching this text will be returned. The search will be applied on the following properties [name, installed_version, assigned_version]. The default value will be empty string. | [optional] [default to ]
 **sortorder** | **str**| Whether the sort order is ascending or descending. The property used for sorting is name. Possible values [Asc, Desc]. Default value is Asc. | [optional] [default to ]
 **orderby** | **str**| Name of the property used for sorting | [optional] [default to ]
 **smartgroupids** | **str**| Comma separated list of smart group ids to which the devices belong. If no smart group id is passed, all the eligible devices will be returned based on the other filters. E.g. 10, 20 | [optional] [default to ]
 **isassigned** | **bool**| If provided, the list of devices on which the app is assigned is included in the returned result set. Default false. | [optional] [default to ]
 **isnotassigned** | **bool**| If provided, the list of devices on which the app is sideloaded or marked for removal but not assigned is included in the returned result set. Default false. | [optional] [default to ]
 **isexcluded** | **bool**| If provided, the list of devices on which the app is excluded is included in the returned result set. Default false. | [optional] [default to ]
 **isinstalled** | **bool**| if provided, the list of devices on which the app is installed is included in the returned result set. Default false. | [optional] [default to ]
 **isnotinstalled** | **bool**| if provided, the list of devices on which the app is not installed but assigned is included in the returned result set. Default false. | [optional] [default to ]
 **installationstatus** | [**object**](.md)| Comma separated list of managed application list reasons to which the devices assigned to the app belong. If no reason is passed, all the assigned devices will be returned based on the other filters. | [optional] [default to ]
 **lastactiontaken** | [**object**](.md)| Comma separated list of application deployment status to which the devices assigned to the app belong. If no deployment status is passed, all the assigned devices will be returned based on the other filters. | [optional] [default to ]

### Return type

[**DevicesPagedSearchResultsModel**](DevicesPagedSearchResultsModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_sdk_ananlytics**
> ApplicationEventSampleSearchResult apps_get_sdk_ananlytics(bulk_input=bulk_input, organizationgroupid=organizationgroupid, applicationid=applicationid, eventname=eventname, startdatetime=startdatetime, enddatetime=enddatetime, searchtype=searchtype, page=page, pagesize=pagesize)

Gets SDK analytics based on the query information provided.

Returns SDK Analytic Events within a time range and filtered by provided query parameters including Unique Device Identifiers and Application Identifiers.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
bulk_input = mamv1.BulkInput() # BulkInput | Bulk input containing multiple Device Attributes based on the search type. (optional)
organizationgroupid = 56 # int | OrganizationGroup Identifier. (optional)
applicationid = '' # str | Application Identifier. (optional) (default to )
eventname = '' # str | Event Name. (optional) (default to )
startdatetime = '' # datetime | Sample Starttime. (optional) (default to )
enddatetime = '' # datetime | Sample Endtime. (optional) (default to )
searchtype = '' # str | Search by Device Identifier types (DeviceId, MacAddress, Udid, SerialNumber, and ImeiNumber).. (optional) (default to )
page = 56 # int | Page number. (optional)
pagesize = 56 # int | Records per page. (optional)

try:
    # Gets SDK analytics based on the query information provided.
    api_response = api_instance.apps_get_sdk_ananlytics(bulk_input=bulk_input, organizationgroupid=organizationgroupid, applicationid=applicationid, eventname=eventname, startdatetime=startdatetime, enddatetime=enddatetime, searchtype=searchtype, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get_sdk_ananlytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_input** | [**BulkInput**](BulkInput.md)| Bulk input containing multiple Device Attributes based on the search type. | [optional] 
 **organizationgroupid** | **int**| OrganizationGroup Identifier. | [optional] 
 **applicationid** | **str**| Application Identifier. | [optional] [default to ]
 **eventname** | **str**| Event Name. | [optional] [default to ]
 **startdatetime** | **datetime**| Sample Starttime. | [optional] [default to ]
 **enddatetime** | **datetime**| Sample Endtime. | [optional] [default to ]
 **searchtype** | **str**| Search by Device Identifier types (DeviceId, MacAddress, Udid, SerialNumber, and ImeiNumber).. | [optional] [default to ]
 **page** | **int**| Page number. | [optional] 
 **pagesize** | **int**| Records per page. | [optional] 

### Return type

[**ApplicationEventSampleSearchResult**](ApplicationEventSampleSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_search_apple_store_async**
> apps_search_apple_store_async(appname)

Searches in App stores for the applications with the specified search string and returns the details.

Searches in the App store for applications that match a specified search string (Example: Boxer) and return the details.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
appname = '' # str | Application name to be searched. Example: Boxer. (Required). (default to )

try:
    # Searches in App stores for the applications with the specified search string and returns the details.
    api_instance.apps_search_apple_store_async(appname)
except ApiException as e:
    print("Exception when calling AppsApi->apps_search_apple_store_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appname** | **str**| Application name to be searched. Example: Boxer. (Required). | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_search_async**
> ApplicationSearchResult apps_search_async(type=type, applicationtype=applicationtype, applicationname=applicationname, product_component_apps_only=product_component_apps_only, category=category, bundleid=bundleid, locationgroupid=locationgroupid, model=model, status=status, platform=platform, winapptype=winapptype, include_apps_from_child_ogs=include_apps_from_child_ogs, include_apps_from_parent_ogs=include_apps_from_parent_ogs, app_command_target=app_command_target, distinct_applications_per_og=distinct_applications_per_og, exclude_assigned_or_installed_device_count=exclude_assigned_or_installed_device_count, page=page, pagesize=pagesize, orderby=orderby)

Search and retrieve details for both internal and external applications or books.

Searches for an application or book, given filters including type, name, category and organization group id. Returns a list of applications or books that match the criteria with details of each application/book.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
type = '' # str | The Product Type - App or Book. (optional) (default to )
applicationtype = '' # str | Type of the application. (Internal/Public). (optional) (default to )
applicationname = '' # str | Application Name. (optional) (default to )
product_component_apps_only = '' # str | Request query to include apps added under Products Staging and Provisioning. (optional) (default to )
category = '' # str | The Application Category. (optional) (default to )
bundleid = '' # str | BundleId/PackageId. (optional) (default to )
locationgroupid = '' # str | LocationGroup Identifier. (optional) (default to )
model = '' # str | Device Model. (optional) (default to )
status = '' # str | Application Status. (optional) (default to )
platform = '' # str | The Application Platform. (optional) (default to )
winapptype = '' # str | The application sub type for windows platforms. (optional) (default to )
include_apps_from_child_ogs =  # bool | Flag to indicate if apps from child og's should be included or not. (optional) (default to )
include_apps_from_parent_ogs =  # bool |  Flag to indicate if apps from parent og's should be included or not. (optional) (default to )
app_command_target = '' # str | Application command Targets for Windows Desktop/MacOs. (optional) (default to )
distinct_applications_per_og =  # bool | Flag to indicate if distinct applications at an OG should be returned by the API.              If two versions of an application have the same name, then the application with the greater version will be returned. (optional) (default to )
exclude_assigned_or_installed_device_count =  # bool | Flag to indicate if assigned or installed device counts for apps should be excluded or not. (optional) (default to )
page = '' # str | Page number. (optional) (default to )
pagesize = '' # str | Records per page. (optional) (default to )
orderby = '' # str | Orderby column name. (optional) (default to )

try:
    # Search and retrieve details for both internal and external applications or books.
    api_response = api_instance.apps_search_async(type=type, applicationtype=applicationtype, applicationname=applicationname, product_component_apps_only=product_component_apps_only, category=category, bundleid=bundleid, locationgroupid=locationgroupid, model=model, status=status, platform=platform, winapptype=winapptype, include_apps_from_child_ogs=include_apps_from_child_ogs, include_apps_from_parent_ogs=include_apps_from_parent_ogs, app_command_target=app_command_target, distinct_applications_per_og=distinct_applications_per_og, exclude_assigned_or_installed_device_count=exclude_assigned_or_installed_device_count, page=page, pagesize=pagesize, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The Product Type - App or Book. | [optional] [default to ]
 **applicationtype** | **str**| Type of the application. (Internal/Public). | [optional] [default to ]
 **applicationname** | **str**| Application Name. | [optional] [default to ]
 **product_component_apps_only** | **str**| Request query to include apps added under Products Staging and Provisioning. | [optional] [default to ]
 **category** | **str**| The Application Category. | [optional] [default to ]
 **bundleid** | **str**| BundleId/PackageId. | [optional] [default to ]
 **locationgroupid** | **str**| LocationGroup Identifier. | [optional] [default to ]
 **model** | **str**| Device Model. | [optional] [default to ]
 **status** | **str**| Application Status. | [optional] [default to ]
 **platform** | **str**| The Application Platform. | [optional] [default to ]
 **winapptype** | **str**| The application sub type for windows platforms. | [optional] [default to ]
 **include_apps_from_child_ogs** | **bool**| Flag to indicate if apps from child og&#39;s should be included or not. | [optional] [default to ]
 **include_apps_from_parent_ogs** | **bool**|  Flag to indicate if apps from parent og&#39;s should be included or not. | [optional] [default to ]
 **app_command_target** | **str**| Application command Targets for Windows Desktop/MacOs. | [optional] [default to ]
 **distinct_applications_per_og** | **bool**| Flag to indicate if distinct applications at an OG should be returned by the API.              If two versions of an application have the same name, then the application with the greater version will be returned. | [optional] [default to ]
 **exclude_assigned_or_installed_device_count** | **bool**| Flag to indicate if assigned or installed device counts for apps should be excluded or not. | [optional] [default to ]
 **page** | **str**| Page number. | [optional] [default to ]
 **pagesize** | **str**| Records per page. | [optional] [default to ]
 **orderby** | **str**| Orderby column name. | [optional] [default to ]

### Return type

[**ApplicationSearchResult**](ApplicationSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_update_admin_action_taken_on_app_removal_protection_logs**
> apps_update_admin_action_taken_on_app_removal_protection_logs(model=model, organizationgroupid=organizationgroupid)

Sets the action (unlock or clear) executed after the threshold for the Removal Log events is reached.

Updates the action taken on the threshold.              Either unlock/clear the threshold.              On unlock the commands are sent to the device              On clear the commands are purged from the queue.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
model = mamv1.UpdateAppRemovalProtectionModel() # UpdateAppRemovalProtectionModel | The body of the request. (optional)
organizationgroupid = '' # str | LocationGroup Identifier. (optional) (default to )

try:
    # Sets the action (unlock or clear) executed after the threshold for the Removal Log events is reached.
    api_instance.apps_update_admin_action_taken_on_app_removal_protection_logs(model=model, organizationgroupid=organizationgroupid)
except ApiException as e:
    print("Exception when calling AppsApi->apps_update_admin_action_taken_on_app_removal_protection_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**UpdateAppRemovalProtectionModel**](UpdateAppRemovalProtectionModel.md)| The body of the request. | [optional] 
 **organizationgroupid** | **str**| LocationGroup Identifier. | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_update_assignment_rule_async**
> apps_update_assignment_rule_async(application_uuid, assignment_rule)

New - Updates assignment rule for an application and publishes the application to the devices associated with assignment rule.

Updates assignments with assignment policies and exclusions for an application. Publishes the application to the devices associated with the assignment rule.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
application_uuid = 'application_uuid_example' # str | Unique identifier for the application.               Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required)
assignment_rule = mamv1.AppAssignmentRuleV1Model() # AppAssignmentRuleV1Model | Assignment rule which contains list of assignments and exclusions for an application.(Required)

try:
    # New - Updates assignment rule for an application and publishes the application to the devices associated with assignment rule.
    api_instance.apps_update_assignment_rule_async(application_uuid, assignment_rule)
except ApiException as e:
    print("Exception when calling AppsApi->apps_update_assignment_rule_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | [**str**](.md)| Unique identifier for the application.               Accepted formats **uuid**              E.g. 3d958f38-246e-4854-a306-189d941ab073(Required) | 
 **assignment_rule** | [**AppAssignmentRuleV1Model**](AppAssignmentRuleV1Model.md)| Assignment rule which contains list of assignments and exclusions for an application.(Required) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_windows_store_search_async**
> apps_windows_store_search_async(appname, platform)

Retrieves the details of the applications from the Windows App Store based on the search request.

Searches in the Windows store for applications that match a specified search string (Example: Boxer) and return the details.

### Example
```python
from __future__ import print_function
import time
import mamv1
from mamv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = mamv1.Configuration()
configuration.api_key['aw-tenant-code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aw-tenant-code'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = mamv1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: CmsAuth
configuration = mamv1.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = mamv1.AppsApi(mamv1.ApiClient(configuration))
appname = '' # str | Application name to be searched. Example: Boxer. (Required). (default to )
platform = '' # str | Device Platform to search the Applications for. Example: WindowsMobile. (Required). (default to )

try:
    # Retrieves the details of the applications from the Windows App Store based on the search request.
    api_instance.apps_windows_store_search_async(appname, platform)
except ApiException as e:
    print("Exception when calling AppsApi->apps_windows_store_search_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appname** | **str**| Application name to be searched. Example: Boxer. (Required). | [default to ]
 **platform** | **str**| Device Platform to search the Applications for. Example: WindowsMobile. (Required). | [default to ]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

