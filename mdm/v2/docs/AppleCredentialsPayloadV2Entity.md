# AppleCredentialsPayloadV2Entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_id** | **int** | Gets or sets unique numeric identifier obtained after upload a certificate using the upload cert API. | [optional] 
**credential_name** | **str** | Gets or sets a human-readable name for the profile payload. | [optional] 
**credential_source** | **str** | Gets or sets the source of the credentials. | [optional] 
**certificate_authority** | **int** | Gets or sets specifies the unique numeric identifier of the certificate authority. | [optional] 
**certificate_template** | **int** | Gets or sets specifies the numeric identifier of the certificate template. | [optional] 
**smime** | **str** | Gets or sets species if the S/MIME signing or encryption certificate of the user is used as a credential. | [optional] 
**name** | **str** | Gets or sets the name or description of the credential. | [optional] 
**key_usage** | **str** | Gets or sets the use of the key. | [optional] 
**certificate_metadata** | [**CertificateMetadataModel_**](CertificateMetadataModel_.md) | Gets or sets certificate metadata. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


