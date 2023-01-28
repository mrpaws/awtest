# MacOsSystemExtensionsPayloadV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_user_overrides** | **bool** | Gets or sets a value indicating whether if false, restricts users from approving additional system extensions. | [optional] 
**allowed_system_extension_types** | [**list[MacOsAllowedSystemExtensionTypesV2Model_]**](MacOsAllowedSystemExtensionTypesV2Model_.md) | Gets or sets includes a list of team identifiers with types of system extensions allowed or not allowed.  Team identifier Value \&quot;*\&quot; indicates the global team identifier. | [optional] 
**allowed_system_extensions** | [**list[MacOsAllowedSystemExtensionV2Model_]**](MacOsAllowedSystemExtensionV2Model_.md) | Gets or sets includes a list of team identifier and bundle identifier pairs defining the system extension to be installed.  Either Identifier is optional, but both can be included. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


