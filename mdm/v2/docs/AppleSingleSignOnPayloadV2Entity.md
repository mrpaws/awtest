# AppleSingleSignOnPayloadV2Entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_name** | **str** | Gets or sets kerberos principal name. | [optional] 
**realm** | **str** | Gets or sets kerberos realm name. This value should be properly capitalized. | [optional] 
**renewal_certificate_name** | **str** | Gets or sets renewal certificate name. | [optional] 
**url_prefix_matches** | **str** | Gets or sets comma separated URLs prefixes that must be matched to use this account for Kerberos authentication over HTTP. | [optional] 
**app_identifier_matches** | **str** | Gets or sets comma separated app identifiers that are allowed to use this SSO login. If this field is missing then SSO login works for all appidentifiers. | [optional] 
**name** | **str** | Gets or sets single sign on account name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


