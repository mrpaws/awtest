# AppleEmailPayloadV2Entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_description** | **str** | Gets or sets a user-visible description of the email account, shown in the Mail and Settings applications. | [optional] 
**account_type** | **str** | Gets or sets defines the protocol to be used for that account. | [optional] 
**path_prefix** | **str** | Gets or sets path prefix for IMAP mail server. | [optional] 
**user_display_name** | **str** | Gets or sets the full user name for the account. | [optional] 
**email_address** | **str** | Gets or sets designates the full email address for the account. | [optional] 
**prevent_moving_messages** | **bool** | Gets or sets a value indicating whether if true, messages may not be moved out of this email account into another account on iOS 5+. | [optional] 
**disable_recent_contact_sync** | **bool** | Gets or sets a value indicating whether if true, this account is excluded from address Recents syncing on iOS 6+. | [optional] 
**incoming_mail_server_host_name** | **str** | Gets or sets designates the incoming mail server host name (or IP address). | [optional] 
**incoming_mail_server_port_number** | **str** | Gets or sets designates the incoming mail server port number. | [optional] 
**incoming_mail_server_use_ssl** | **bool** | Gets or sets a value indicating whether designates whether the incoming mail server uses SSL for authentication. | [optional] 
**incoming_mail_server_username** | **str** | Gets or sets designates the user name for the email account, usually the same as the email address up to the @ character. | [optional] 
**incoming_mail_server_authentication** | **str** | Gets or sets designates the authentication scheme for incoming mail. | [optional] 
**incoming_password** | **str** | Gets or sets password for the Incoming Mail Server. | [optional] 
**outgoing_mail_server_host_name** | **str** | Gets or sets designates the outgoing mail server host name (or IP address). | [optional] 
**outgoing_mail_server_port_number** | **str** | Gets or sets designates the outgoing mail server port number. | [optional] 
**outgoing_mail_server_authentication** | **str** | Gets or sets designates the authentication scheme for outgoing mail. | [optional] 
**outgoing_mail_server_use_ssl** | **bool** | Gets or sets a value indicating whether designates whether the outgoing mail server uses SSL for authentication. | [optional] 
**outgoing_mail_server_username** | **str** | Gets or sets designates the user name for the email account, usually the same as the email address up to the @ character. | [optional] 
**outgoing_password_same_as_incoming** | **bool** | Gets or sets a value indicating whether if set, the user will be prompted for the password only once and it will be used for both outgoing and incoming mail. | [optional] 
**outgoing_password** | **str** | Gets or sets password for the Outgoing Mail Server. | [optional] 
**prevent_use_in_third_party_apps** | **bool** | Gets or sets a value indicating whether if true, this account is not available for sending mail in any app other than the Apple Mail app on iOS 5+. | [optional] 
**use_smime** | **bool** | Gets or sets a value indicating whether if true, this account supports S/MIME on iOS 5.0 through iOS 9.3.3. | [optional] 
**smime_certificate** | **str** | Gets or sets s/MIME Certificate used to sign messages sent from this account on iOS 5+. | [optional] 
**smime_encryption_certificate** | **str** | Gets or sets s/MIME Certificate used to decrypt messages sent to this account on iOS 5+. | [optional] 
**smime_encryption_enabled** | **bool** | Gets or sets a value indicating whether if set to true, S/MIME encryption is on by default for this account on iOS 10.3+. | [optional] 
**smime_signing_enabled** | **bool** | Gets or sets a value indicating whether if set to true, S/MIME signing is enabled for this account on iOS 10.3+. | [optional] 
**smime_signing_user_overrideable** | **bool** | Gets or sets a value indicating whether if set to true, this setting will allow users to toggle S/MIME signing in device email settings. | [optional] 
**smime_signing_certificate_uuid_user_overrideable** | **bool** | Gets or sets a value indicating whether if set to true, this setting will allow user to choose S/MIME signing certificate on iOS 12. | [optional] 
**smime_encrypt_by_default** | **bool** | Gets or sets a value indicating whether if set to true, this setting will encrypt by default when S/MIME encryption is enabled for iOS 12. | [optional] 
**smime_encrypt_by_default_user_overrideable** | **bool** | Gets or sets a value indicating whether if set to true, this setting will allow user to toggle S/MIME encryption on iOS 12. | [optional] 
**smime_encryption_certificate_uuid_user_overrideable** | **bool** | Gets or sets a value indicating whether if set to true, this setting will allow user to choose S/MIME encryption certificate on iOS 12. | [optional] 
**smime_enable_encryption_per_message_switch** | **bool** | Gets or sets a value indicating whether if set to true, this setting will enable S/MIME encryption on per-message switch on iOS 12. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


