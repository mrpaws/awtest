# AppleOsXCredentialPayloadEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_source** | **str** | Gets or sets the source of the credentials. | [optional] 
**credential_name** | **str** | Gets or sets a human-readable name for the profile payload. | [optional] 
**certificate_id** | **int** | Gets or sets unique numeric identifier obtained after upload a certificate using the upload cert API. | [optional] 
**certificate_authority** | **int** | Gets or sets specifies the unique numeric identifier of the certificate authority. | [optional] 
**certificate_template** | **int** | Gets or sets specifies the numeric identifier of the certificate template. | [optional] 
**allow_access_to_all_applications** | **bool** | Gets or sets a value indicating whether if true, apps have access to the private key. | [optional] 
**name** | **str** | Gets or sets the name or description of the credential. | [optional] 
**key_is_extractable** | **bool** | Gets or sets a value indicating whether value              Gets or sets a value indicating whether the private key can be exported from the keychain or not. | [optional] 
**certificate_metadata** | [**CertificateMetadataModel_**](CertificateMetadataModel_.md) | Gets or sets certificate metadata. | [optional] 
**identity_preference** | [**MacOsCredentialIdentityPreferencePayloadV2Model_**](MacOsCredentialIdentityPreferencePayloadV2Model_.md) | Gets or sets identity Preference payload using this credential payload. | [optional] 
**certificate_preference** | [**MacOsCredentialCertificatePreferencePayloadV2Model_**](MacOsCredentialCertificatePreferencePayloadV2Model_.md) | Gets or sets certificate Preference payload using this credential payload. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


