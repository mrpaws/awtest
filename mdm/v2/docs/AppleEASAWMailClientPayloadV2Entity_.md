# AppleEASAWMailClientPayloadV2Entity_

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_active_sync_host** | **str** | Gets or sets public host name for the Emailserver. | [optional] 
**ignore_ssl_errors** | **bool** | Gets or sets a value indicating whether specifies if the device is allowed to ignore SSL errors for Agent Process. | [optional] 
**use_smime** | **bool** | Gets or sets a value indicating whether if true, this account supports S/MIME. | [optional] 
**smime_certificate** | **str** | Gets or sets s/MIME signing certificate to be used with the profile. | [optional] 
**smime_encryption_certificate** | **str** | Gets or sets s/MIME encryption certificate to be used with the profile. | [optional] 
**domain** | **str** | Gets or sets user&#39;s email domain. | [optional] 
**user** | **str** | Gets or sets username for the account. | [optional] 
**email_address** | **str** | Gets or sets user&#39;s email address. | [optional] 
**password** | **str** | Gets or sets email account&#39;s password. | [optional] 
**payload_certificate** | **str** | Gets or sets name of the Payload certificate. | [optional] 
**enable_email** | **bool** | Gets or sets a value indicating whether if false, disables access to Email on the AW Email Client. | [optional] 
**enable_calendar** | **bool** | Gets or sets a value indicating whether if false, disables access to calendar on the AW Email Client. | [optional] 
**enable_contacts** | **bool** | Gets or sets a value indicating whether if false, disables access to contacts on the AW Email Client. | [optional] 
**sync_interval** | **int** | Gets or sets frequency of mail synchronization. 0:Auto, 1: 15 mins, 2: 30 mins, 3: 1 hour, 4: 4 hours, 5: Manual. | [optional] 
**email_notifications** | **int** | Gets or sets email Notifications. | [optional] 
**past_days_of_mail_to_sync** | **int** | Gets or sets number of days of mailsynchronization. | [optional] 
**past_days_of_calendar_to_sync** | **int** | Gets or sets number of days of calendar synchronization. | [optional] 
**email_size_in_kilobytes_default_is_unlimited** | **int** | Gets or sets maximum Emailsize allowed in KBs. | [optional] 
**enable_html_email** | **bool** | Gets or sets a value indicating whether specifies if HTML Email is enabled on the device. | [optional] 
**email_signature** | **str** | Gets or sets signature for the Emails. | [optional] 
**enable_signature_editing** | **bool** | Gets or sets a value indicating whether if false, disables editing of Email signature. | [optional] 
**require_passcode** | **bool** | Gets or sets a value indicating whether specifies if passcode is needed on the AW Email Client. | [optional] 
**type** | **int** | Gets or sets specifies if the Email client can be accessed using passcode alone or using a combination of Username and Password. 0: Disabled, 1: Passcode, 2: Username and Password. | [optional] 
**complexity** | **int** | Gets or sets specifies if a simple or an Alphanumeric passcode will be used to access the email client. | [optional] 
**allow_simple_passcode** | **bool** | Gets or sets a value indicating whether specifies if a simple passcode will be used to access the email client. | [optional] 
**minimum_length** | **int** | Gets or sets minimum length of the passcode. | [optional] 
**minimum_number_of_complex_characters** | **int** | Gets or sets minimum number of complex characters necessary in the passcode. | [optional] 
**maximum_age_days** | **int** | Gets or sets maximum days for the passcode before it is expired. | [optional] 
**auto_lock** | **bool** | Gets or sets a value indicating whether if true, the Email client will be locked after the idle period. | [optional] 
**history** | **int** | Gets or sets when the user changes the passcode, it has to be unique within the last N entries in the history. | [optional] 
**grace_period** | **int** | Gets or sets the maximum grace period in minutes, to unlock the Client without entering a passcode. | [optional] 
**maximum_number_of_failed_attempts** | **int** | Gets or sets specifies the number of allowed failed attempts to enter the passcode at the device&#39;s lock screen. | [optional] 
**disabe_copy_paste** | **bool** | Gets or sets a value indicating whether setting this field to true disables copying of Email content on the clipboard. | [optional] 
**disable_attachments** | **bool** | Gets or sets a value indicating whether setting this field to true disables email attachments. | [optional] 
**maximum_attachment_size_mb** | **int** | Gets or sets maximum size of an Email attachment in MB. | [optional] 
**open_all_links_in_air_watch_browser** | **bool** | Gets or sets a value indicating whether setting this field to true forces all links to be open in VMware Browser. | [optional] 
**scl_only_attachments** | **bool** | Gets or sets a value indicating whether setting this field to true forces opening of mail attachments in the Secure Content locker. | [optional] 
**restrict_attachments_to_be_opened_in_following_apps** | **bool** | Gets or sets a value indicating whether setting this value to true, allows attachments to be opened only in the application specified in the Application tag. | [optional] 
**applications** | **list[str]** | Gets or sets application&#39;s bundle IDs in which the email attachments are opened. | [optional] 
**allow_printing** | **bool** | Gets or sets a value indicating whether setting this field to false disables printing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


