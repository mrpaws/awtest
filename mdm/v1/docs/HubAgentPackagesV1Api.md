# mdmv1.HubAgentPackagesV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/mdm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hub_agent_packages_v1_search**](HubAgentPackagesV1Api.md#hub_agent_packages_v1_search) | **GET** /product-components/hub-agent-packages/search | New - Search Airwatch Agent/Hub Packages based on the query information provided


# **hub_agent_packages_v1_search**
> AgentPackagesSearchResultV1Model hub_agent_packages_v1_search(organization_group_uuid=organization_group_uuid, device_type=device_type, search_text=search_text)

New - Search Airwatch Agent/Hub Packages based on the query information provided

Search Airwatch Agent/Hub Packages based on the query parameters like organization group uuid, device type and search text.

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
api_instance = mdmv1.HubAgentPackagesV1Api(mdmv1.ApiClient(configuration))
organization_group_uuid = '' # str | organization group to search Airwatch Agent/Hub Packages (optional) (default to )
device_type =  # object | device type such as Android or Windows Mobile (optional) (default to )
search_text = '' # str | text for searching the Agent/Hub Packages. (optional) (default to )

try:
    # New - Search Airwatch Agent/Hub Packages based on the query information provided
    api_response = api_instance.hub_agent_packages_v1_search(organization_group_uuid=organization_group_uuid, device_type=device_type, search_text=search_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubAgentPackagesV1Api->hub_agent_packages_v1_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_group_uuid** | **str**| organization group to search Airwatch Agent/Hub Packages | [optional] [default to ]
 **device_type** | [**object**](.md)| device type such as Android or Windows Mobile | [optional] [default to ]
 **search_text** | **str**| text for searching the Agent/Hub Packages. | [optional] [default to ]

### Return type

[**AgentPackagesSearchResultV1Model**](AgentPackagesSearchResultV1Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [CmsAuth](../README.md#CmsAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

