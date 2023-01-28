# systemv1.AdminIdentityV1Api

All URIs are relative to *https://awapi-cert.delimitize.com/API/system*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_identity_v1_get_admin_identity**](AdminIdentityV1Api.md#admin_identity_v1_get_admin_identity) | **POST** /idp/admin | New - Provides identity required to create token for basic and directory admin user.


# **admin_identity_v1_get_admin_identity**
> AdminUserIdentityModelV1 admin_identity_v1_get_admin_identity(token_service_idp_request_model_v1)

New - Provides identity required to create token for basic and directory admin user.

This API identifies the admin user and returns the uuid for the same.

### Example
```python
from __future__ import print_function
import time
import systemv1
from systemv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = systemv1.AdminIdentityV1Api()
token_service_idp_request_model_v1 = systemv1.TokenServiceIdpRequestModelV1() # TokenServiceIdpRequestModelV1 | Request body containing username password and tenant uuid.(Required)

try:
    # New - Provides identity required to create token for basic and directory admin user.
    api_response = api_instance.admin_identity_v1_get_admin_identity(token_service_idp_request_model_v1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminIdentityV1Api->admin_identity_v1_get_admin_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_service_idp_request_model_v1** | [**TokenServiceIdpRequestModelV1**](TokenServiceIdpRequestModelV1.md)| Request body containing username password and tenant uuid.(Required) | 

### Return type

[**AdminUserIdentityModelV1**](AdminUserIdentityModelV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;version=1

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

