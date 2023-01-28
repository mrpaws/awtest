# ApplicationVersionV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_uuid** | **str** | Identifier of the application. | [optional] 
**unique_identifier** | **str** | Application Unique Identifier. | [optional] 
**version** | **str** | This only shows the numerical version. If PackageVersion is alphanumeric instead of numeric, these will not match. | [optional] 
**package_version** | **str** | The alphanumeric version from the application file. | [optional] 
**build_package_version** | **str** | Especially for IPA. The alphanumeric version of the application build. | [optional] 
**version_hash** | **str** | Hash of Package Version and Build Package Version. | [optional] 
**is_active** | **bool** | Indicates whether or not the application is active. | [optional] 
**is_retired** | **bool** | Indicates whether or not the application is retired. | [optional] 
**version_code** | **int** | The version code of the application. | [optional] 
**device_type** | **int** | The device type. | [optional] 
**is_provisioning_enabled** | **bool** | True if Product Provisioning is enabled for the application. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


