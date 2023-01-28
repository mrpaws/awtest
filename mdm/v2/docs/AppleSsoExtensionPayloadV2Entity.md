# AppleSsoExtensionPayloadV2Entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_type** | **int** | Gets or sets extension type: Generic, Kerberos. | [optional] 
**extension_identifier** | **str** | Gets or sets application extension that performs single sign-on. | [optional] 
**type** | **str** | Gets or sets single sign-on extension type. | [optional] 
**realm** | **str** | Gets or sets realm name for SSO extension. | [optional] 
**hosts** | **list[str]** | Gets or sets list of hosts for which the app extension performs single sign-on. | [optional] 
**urls** | **list[str]** | Gets or sets list of URLs for which the app extension performs single sign-on. | [optional] 
**custom_xml** | **str** | Gets or sets custom XML for SSO extension data. | [optional] 
**certificate_uuid** | **str** | Gets or sets certificate UUID for SSO extension data. | [optional] 
**certificate_name** | **str** | Gets or sets certificate name for SSO extension data. | [optional] 
**use_site_auto_discovery** | **bool** | Gets or sets a value indicating whether use site auto discovery flag for kerberos single sign-on. | [optional] 
**allow_automatic_login** | **bool** | Gets or sets a value indicating whether allow automatic login flag for kerberos single sign-on. | [optional] 
**require_user_touch_id_or_password** | **bool** | Gets or sets a value indicating whether require user presence flag for kerberos single sign-on. | [optional] 
**credential_bundle_ids** | **list[str]** | Gets or sets list of allowed bundle ids for kerberos single sign-on. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


