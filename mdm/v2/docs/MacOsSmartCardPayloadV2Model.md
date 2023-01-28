# MacOsSmartCardPayloadV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_smart_card** | **bool** | Gets or sets a value indicating whether indicates whether to allow SmartCard authentication. | [optional] 
**enforce_smart_card** | **bool** | Gets or sets a value indicating whether indicates whether to use SmartCard for all authentication. | [optional] 
**show_user_pairing_dialog** | **bool** | Gets or sets a value indicating whether indicates whether to show user pairing dialog. | [optional] 
**one_card_per_user** | **bool** | Gets or sets a value indicating whether indicates whether to restrict one card per user. | [optional] 
**certificate_trust_check** | **int** | Gets or sets certificate Trust Check. Valid values are 0-3.  0 - certificate trust check is turned off.  1 - certificate trust check is turned on with no additional revocation checks.  2 - certificate trust check is turned on, plus a soft revocation check is performed.  3 - certificate trust check is turned on, plus a hard revocation check is performed. | [optional] 
**token_removal_action** | **int** | Gets or sets if 1, when the SmartCard is removed, the screensaver will be enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


