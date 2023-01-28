# AppleEASNativeMailClientPayloadV2Entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | Gets or sets name of the account. | [optional] 
**exchange_active_sync_host** | **str** | Gets or sets specifies the Exchange server host name(or IP address). | [optional] 
**use_ssl** | **bool** | Gets or sets a value indicating whether specifies if all communication occurs through the secure socket layer. | [optional] 
**use_smime** | **bool** | Gets or sets a value indicating whether specifies whether the user&#39;s S/MIME certificates would be stored to be used with S/MIME enabled profiles on iOS 5.0 through iOS 9.3.3. | [optional] 
**smime_certificate_name** | **str** | Gets or sets s/MIME Certificate used to sign messages sent from this account. | [optional] 
**smime_encryption_certificate_name** | **str** | Gets or sets s/MIME Certificate used to decrypt messages sent to this account. | [optional] 
**smime_encryption_enabled** | **bool** | Gets or sets a value indicating whether if set to true, S/MIME encryption is on by default for this account on iOS 10.3+. | [optional] 
**smime_signing_enabled** | **bool** | Gets or sets a value indicating whether if set to true, S/MIME signing is enabled for this account on iOS 10.3+. | [optional] 
**domain** | **str** | Gets or sets user&#39;s email domain. | [optional] 
**user_name** | **str** | Gets or sets username for the account. | [optional] 
**email_address** | **str** | Gets or sets user&#39;s email address. | [optional] 
**password** | **str** | Gets or sets email account&#39;s password. | [optional] 
**payload_certificate_name** | **str** | Gets or sets name of the Payload certificate. | [optional] 
**past_days_of_mail_to_sync** | **int** | Gets or sets the number of days since synchronization. | [optional] 
**prevent_moving_messages** | **bool** | Gets or sets a value indicating whether if true, messages may not be moved out of this email account into another account. Also prevents forwarding or replying from a different account than the message was originated from on iOS 5+. | [optional] 
**prevent_use_in_third_party_apps** | **bool** | Gets or sets a value indicating whether if true, this account is not available for sending mail in any app other than the Apple Mail app. | [optional] 
**disable_recent_contact_sync** | **bool** | Gets or sets a value indicating whether if true, this account is excluded from address Recents syncing on iOS 6+. | [optional] 
**default_calling_app** | **str** | Gets or sets the audio call app that your Native EAS account will use to make calls when you select a phone number in an email message on iOS 10+. | [optional] 
**smime_signing_user_overrideable** | **bool** | Gets or sets a value indicating whether if set to true, this setting will allow users to toggle S/MIME signing in device email settings. | [optional] 
**smime_signing_certificate_uuid_user_overrideable** | **bool** | Gets or sets a value indicating whether if set to true, this setting will allow user to choose S/MIME signing certificate on iOS 12. | [optional] 
**smime_encrypt_by_default** | **bool** | Gets or sets a value indicating whether if set to true, this setting will encrypt by default when S/MIME encryption is enabled for iOS 12. | [optional] 
**smime_encrypt_by_default_user_overrideable** | **bool** | Gets or sets a value indicating whether if set to true, this setting will allow user to toggle S/MIME encryption on iOS 12. | [optional] 
**smime_encryption_certificate_uuid_user_overrideable** | **bool** | Gets or sets a value indicating whether if set to true, this setting will allow user to choose S/MIME encryption certificate on iOS 12. | [optional] 
**smime_enable_encryption_per_message_switch** | **bool** | Gets or sets a value indicating whether if set to true, this setting will enable S/MIME encryption on per-message switch on iOS 12. | [optional] 
**enable_mail** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether the Mail service for this account is enabled. | [optional] 
**enable_mail_user_overridable** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether to prevent the user from changing the state of the Mail service for this account in Settings. | [optional] 
**enable_contacts** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether the Contacts service for this account is enabled. | [optional] 
**enable_contacts_user_overridable** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether to prevent the user from changing the state of the Contacts service for this account in Settings. | [optional] 
**enable_calendars** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether the Calendars service for this account is enabled. | [optional] 
**enable_calendars_user_overridable** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether to prevent the user from changing the state of the Calendars service for this account in Settings. | [optional] 
**enable_notes** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether the Notes service for this account is enabled. | [optional] 
**enable_notes_user_overridable** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether to prevent the user from changing the state of the Notes service for this account in Settings. | [optional] 
**enable_reminders** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether the Reminders service for this account is enabled. | [optional] 
**enable_reminders_user_overridable** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether to prevent the user from changing the state of the Reminders service for this account in Settings. | [optional] 
**o_auth** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether to use OAuth for exchange or not. | [optional] 
**o_auth_sign_in_url** | **str** | Gets or sets a value for the URL that this account should use for signing in via OAuth. When this URL is specified, auto-discovery is not used for this account so you must also specify a host. | [optional] 
**o_auth_token_request_url** | **str** | Gets or sets a value for the URL that this account should use for token requests via OAuth. | [optional] 
**override_previous_password** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether overrides the previous user/EAS password with the new EAS password in the payload. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


