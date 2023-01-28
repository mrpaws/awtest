# ApnsSetupModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apple_id** | **str** | Gets or sets apple id of account from which APNS certificate is created. | [optional] 
**certificate_signing_request_blob_id** | **int** | Gets or sets blob Url from which user can download .plist file required for APNS certificate generation. | [optional] 
**uploaded_certificate_blob_id** | **int** | Gets or sets id of APNS certificate blob uploaded by user,  Used in view to mark blob which points to Apple signed certificate uploaded by user from view  Remark this property is issued at the time of saving apple signed certificate, with the help of this Id, actual file is fetched from BlobStore. | [optional] 
**issued_certificate_id** | **int** | Gets or sets apns certificate Id issued for given environment, Id is 0 if no certificate exists for current OG. | [optional] 
**renew** | **bool** | Gets or sets apns certificate Child permission for given environment. | [optional] 
**certificate_password** | **str** | Gets or sets apns certificate Password for given environment. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


