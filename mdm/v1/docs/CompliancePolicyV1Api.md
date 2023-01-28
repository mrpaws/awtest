# mdmv1.CompliancePolicyV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compliance_policy_v1_get_compliance_policies**](CompliancePolicyV1Api.md#compliance_policy_v1_get_compliance_policies) | **GET** /compliancepolicies | New - Returns a collection of Compliance Policies based on the search criteria.
[**compliance_policy_v1_search**](CompliancePolicyV1Api.md#compliance_policy_v1_search) | **GET** /compliancepolicy/search | Searches for the CompliancePolicies with the search parameters passed.


# **compliance_policy_v1_get_compliance_policies**
> CompliancePolicySearchResultV1Model compliance_policy_v1_get_compliance_policies(organizationgroupuuid=organizationgroupuuid, page=page, pagesize=pagesize, searchtext=searchtext, status=status)

New - Returns a collection of Compliance Policies based on the search criteria.

Returns a collection of Compliance Policies based on the search criteria specified. The search parameters can be organization group id, page, and the pagesize. this end point supports json only.

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
api_instance = mdmv1.CompliancePolicyV1Api(mdmv1.ApiClient(configuration))
organizationgroupuuid = '' # str | Organization Group UUID. (optional) (default to )
page = 56 # int | Page number (optional)
pagesize = 56 # int | Maximum number of results to be returned in each page (optional)
searchtext = '' # str | Search text can be a part of the policy name or policy description (optional) (default to )
status = '' # str | Status can be used to filter the search results based on the compliance policy status. Expected values of status can be All(Both Active and Inactive policies), Active(Active complaince policies) or Inactive(Inactive compliance policies) (optional) (default to )

try:
    # New - Returns a collection of Compliance Policies based on the search criteria.
    api_response = api_instance.compliance_policy_v1_get_compliance_policies(organizationgroupuuid=organizationgroupuuid, page=page, pagesize=pagesize, searchtext=searchtext, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompliancePolicyV1Api->compliance_policy_v1_get_compliance_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupuuid** | **str**| Organization Group UUID. | [optional] [default to ]
 **page** | **int**| Page number | [optional] 
 **pagesize** | **int**| Maximum number of results to be returned in each page | [optional] 
 **searchtext** | **str**| Search text can be a part of the policy name or policy description | [optional] [default to ]
 **status** | **str**| Status can be used to filter the search results based on the compliance policy status. Expected values of status can be All(Both Active and Inactive policies), Active(Active complaince policies) or Inactive(Inactive compliance policies) | [optional] [default to ]

### Return type

[**CompliancePolicySearchResultV1Model**](CompliancePolicySearchResultV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_policy_v1_search**
> CompliancePolicySearchResult compliance_policy_v1_search(organizationgroupid=organizationgroupid, page=page, pagesize=pagesize)

Searches for the CompliancePolicies with the search parameters passed.

Searches for a compliance policy in airwatch based on the search parameters passed.  The search parameters can be organization group id, page, and the pagesize.

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
api_instance = mdmv1.CompliancePolicyV1Api(mdmv1.ApiClient(configuration))
organizationgroupid = 56 # int | Organization group id which is similar to selected organization group selected in console. (optional)
page = 56 # int | page number. (optional)
pagesize = 56 # int | Maximum results which should be returned in each page. (optional)

try:
    # Searches for the CompliancePolicies with the search parameters passed.
    api_response = api_instance.compliance_policy_v1_search(organizationgroupid=organizationgroupid, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompliancePolicyV1Api->compliance_policy_v1_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationgroupid** | **int**| Organization group id which is similar to selected organization group selected in console. | [optional] 
 **page** | **int**| page number. | [optional] 
 **pagesize** | **int**| Maximum results which should be returned in each page. | [optional] 

### Return type

[**CompliancePolicySearchResult**](CompliancePolicySearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json;version=1, application/xml;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

