# GenerateBarcodeEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staging_profile_id** | **int** | Gets or sets the identifier of the staging profile for which barcode has to be generated. | [optional] 
**organization_group_id** | **int** | Gets or sets organizationGroup under which the staging profile is being managed. | [optional] 
**universal_barcode** | **bool** | Gets or sets a value indicating whether whether the barcode can be used to enroll the device to any OG (Universal). | [optional] 
**staging_relay_server_id** | **int** | Gets or sets identifier of Relay Server where the files will be pushed. | [optional] 
**wifi_profile_id** | **int** | Gets or sets identifier of wifi profile for connection. | [optional] 
**encryption_passphrase_method** | **int** | Gets or sets the type of encryption passphrase to be used for barcode generation. 1 - built-in, 2 - user defined. | [optional] 
**passphrase** | **str** | Gets or sets passcode validation on the device immediately after scanning the barcode (only for EncryptionPassphraseMethod - user-defined). | [optional] 
**barcode_format_pdf417** | **bool** | Gets or sets a value indicating whether whether the required format is PDF417. | [optional] 
**barcode_format_narrow_pdf417** | **bool** | Gets or sets a value indicating whether whether the required format is NarrowPDF417. | [optional] 
**barcode_format_linear** | **bool** | Gets or sets a value indicating whether whether the required format is Linear. | [optional] 
**barcode_format_narrow_linear** | **bool** | Gets or sets a value indicating whether whether the required format is NarrowLinear. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


