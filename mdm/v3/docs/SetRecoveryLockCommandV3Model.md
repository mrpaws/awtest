# SetRecoveryLockCommandV3Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | The current recovery lock password set on the device. If provided, will be used for issuing the command to set a new password or clear the existing password. If not provided, the last Applied Password via Workspace ONE UEM will be used. | [optional] 
**clear_password** | **bool** | If true, ignores the password policy in the request and clears the password set on the device. | [optional] 
**password_policy** | [**DeviceRecoveryLockPasswordPolicyV3Model**](DeviceRecoveryLockPasswordPolicyV3Model.md) | Specifies the complexity of the Recovery Lock password generated and sent to the device as part of the SetRecoveryLock command. If all of include_numbers, include_letters and include_special_characters are false, then the password can contain all the characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


