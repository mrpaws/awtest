# AppleOsXDiskEncryptionAirWatchPayloadEntity_

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_key** | **bool** | Gets or sets indicates whether the recovery key should be stored in AirWatch. | [optional] 
**rotate_key_after** | **int** | Gets or sets the number of days until the recovery key rotates. | [optional] 
**use_intelligent_hub** | **bool** | Gets or sets indicate whether to use the intelligent hub for enforcement. | [optional] 
**notify_user_for_encryption** | **bool** | Gets or sets indicate whether to notify the user if encryption is disabled. | [optional] 
**encryption_notification_title** | **str** | Gets or sets notification title for encryption. | [optional] 
**encryption_notification_message** | **str** | Gets or sets notification message for encryption. | [optional] 
**encryption_max_notify_attempts** | **int** | Gets or sets maximum number of times to display the notification for encryption. | [optional] 
**encryption_notification_retry_interval_in_hours** | **int** | Gets or sets retry interval in hours between dismissals of the notification for rotating recovery key. | [optional] 
**encryption_action_after_last_notification** | **int** | Gets or sets action to be taken after the dismissal of the last notification, Force Logout (1), Do Nothing (2). | [optional] 
**enable_recovery_key** | **bool** | Gets or sets indicate whether to prompt for the user&#39;s password if the encryption is enabled to rotate recovery key. | [optional] 
**recovery_key_notification_title** | **str** | Gets or sets notification title for rotating recovery key. | [optional] 
**recovery_key_notification_message** | **str** | Gets or sets notification message for rotating recovery key. | [optional] 
**recovery_key_notification_retry_interval_in_hours** | **int** | Gets or sets retry interval in hours between dismissals of the notification for rotating recovery key. | [optional] 
**recovery_key_prompt_title** | **str** | Gets or sets prompt title for rotating recovery key. | [optional] 
**recovery_key_prompt_message** | **str** | Gets or sets prompt message for rotating recovery key. | [optional] 
**recovery_key_success_title** | **str** | Gets or sets success title for rotating recovery key. | [optional] 
**recovery_key_success_message** | **str** | Gets or sets success message for rotating recovery key. | [optional] 
**recovery_key_error_title** | **str** | Gets or sets error title for rotating recovery key. | [optional] 
**recovery_key_error_message** | **str** | Gets or sets error message for rotating recovery key. | [optional] 
**recovery_key_max_failure_count** | **int** | Gets or sets maximum number of times to rotate recovery key on failure. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


