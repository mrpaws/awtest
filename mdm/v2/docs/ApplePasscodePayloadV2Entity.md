# ApplePasscodePayloadV2Entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_passcode_on_device** | **bool** | Gets or sets a value indicating whether determines whether the user is forced to set a PIN. | [optional] 
**allow_simple_value** | **bool** | Gets or sets a value indicating whether determines whether a simple passcode is allowed. | [optional] 
**require_alphanumeric_value** | **bool** | Gets or sets a value indicating whether specifies whether the user must enter alphabetic characters (\&quot;abcd\&quot;), or if numbers are sufficient. | [optional] 
**minimum_passcode_length** | **int** | Gets or sets specifies the minimum overall length of the passcode. | [optional] 
**minimum_number_of_complex_characters** | **int** | Gets or sets specifies the minimum number of complex characters that a passcode must contain. | [optional] 
**maximum_passcode_age** | **str** | Gets or sets specifies the number of days for which the passcode can remain unchanged. | [optional] 
**auto_lock** | **str** | Gets or sets specifies the number of minutes for which the device can be idle (without being unlocked by the user) before it gets locked by the system. | [optional] 
**passcode_history** | **str** | Gets or sets when the user changes the passcode, it has to be unique within the last N entries in the history. Minimum value is 1, maximum value is 50. | [optional] 
**grace_period_for_device_lock** | **int** | Gets or sets the maximum grace period, in minutes, to unlock the phone without entering a passcode. | [optional] 
**maximum_number_of_failed_attempts** | **str** | Gets or sets specifies the number of allowed failed attempts to enter the passcode at the device&#39;s lock screen. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


