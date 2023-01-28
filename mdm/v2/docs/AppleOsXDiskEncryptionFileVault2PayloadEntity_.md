# AppleOsXDiskEncryptionFileVault2PayloadEntity_

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Gets or sets a value indicating whether indicates whether disk encryption should be enforced. | [optional] 
**show_recovery_key** | **bool** | Gets or sets indicates whether the personal recovery key should be shown. | [optional] 
**recovery_type** | **int** | Gets or sets indicates whether the recovery key type is personal (1), institutional (2) or personal and corporate (3). | [optional] 
**file_vault_enterprise_certificate** | **str** | Gets or sets name of the certificate configured in the credential payload, ex. Certificate #1. | [optional] 
**file_vault_user** | **int** | Gets or sets user type that will be added to FileVault, Current or Next Login User (1), or Specific User(2). | [optional] 
**username** | **str** | Gets or sets user name of the Open Directory user that will be added to FileVault. | [optional] 
**prompt_to_enable_file_vault_at** | **int** | Gets or sets when to prompt to enable FileVault, Both Login and Logout (1), Logout Only (2)  or Login Only (3). | [optional] 
**number_of_times_user_can_bypass** | **int** | Gets or sets number of times user can bypass enabling FileVault, this will be used to set the value of DeferForceAtUserLoginMaxBypassAttempts and DeferDontAskAtUserLogout. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


