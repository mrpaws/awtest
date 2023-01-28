# DeviceInfoModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_sample_last_seen_date** | **datetime** | The last seen app sample time for the device in YYYY-MM-DDTHH:MM:SSZ format. | [optional] 
**app_sample_last_seen** | **str** | The string representation of the time difference since the latest transient reason was reported by the device. | [optional] 
**is_device_up** | **bool** | Indicates if the device is active. | [optional] 
**assignment_status** | **str** | Assignment status of the app. The possible values are [Assigned, NotAssigned] | [optional] 
**assigned_version** | **str** | The version of app assigned to the device | [optional] 
**installed_status** | **str** | Installation status of the app on the device. The possible values are [Installed, NotInstalled] | [optional] 
**installed_version** | **str** | The version of app installed on the device | [optional] 
**last_action_taken** | **str** | The latest server side trigger for the application. The possible values are [Unknown, PendingRelease, InstallCommandReadyForDevice, InstallCommandDispatched, InstallCommandFailed, RemoveAppCommandInHeldState, PendingRemoval, RemoveCommandSuccessful, RemoveApplicationFailed, VppLicenseNotAvailable, RequestRejected, RequestError, PendingApproval, RequestExpired, ProvisioningCommandDeleted, UserDeferredInstall] | [optional] 
**latest_action_taken_date_time** | **datetime** | The time of the latest server side trigger in YYYY-MM-DDTHH:MM:SSZ format. | [optional] 
**latest_action_taken_time** | **str** | The timestamp of the latest server side trigger in YYYY-MM-DDTHH:MM:SSZ format. | [optional] 
**latest_app_reason** | **str** | The application reason reported by the device. The possible values are [NeedsRedemption, RedeemingCode, Prompting, Installing, Managed, MDMRemoval, RemovedByEmm, RemovedByUser, Rejected, Failed, Unknown, InstalledByUser, AwaitingInstallOnDevice, Updating, ManagementRejected, PromptingForManagement, DownloadInProgress, DownloadFailed, RemoveApplicationFailed, FinalDetectionFailed, DeviceEligibilityCheckFailed, ExecutionFailed, DependentAppValidationFailed, CheckingDeviceEligibility, ValidatingDependentApps, PendingReboot] | [optional] 
**latest_app_reason_date_time** | **datetime** | The time at which the reason was reported by the device | [optional] 
**latest_app_reason_time** | **str** | The timestamp at which the reason was reported by the device | [optional] 
**device_uuid** | **str** | The unique identifier of the device | [optional] 
**application_uuid** | **str** | The unique identifier of the application assigned to the device | [optional] 
**friendly_name** | **str** | The friendly name of the device | [optional] 
**management_type** | **str** | The management type of the device. | [optional] 
**ownership_type** | **str** | The ownership type of the device | [optional] 
**enrollment_user_name** | **str** | Username (with domain if present) of the user to which the device is enrolled | [optional] 
**enrollment_user_id** | **int** | The unique identifier of the user to which the device is enrolled | [optional] 
**device_id** | **int** | The unique identifier of the enrolled device | [optional] 
**requires_approval** | **bool** | Indicates if requires approval is enabled for the device | [optional] 
**approval_received** | **bool** | Indicates if approval is received for device if requires approval is true | [optional] 
**assignment_type** | **int** | Value indicating assignment type. The supported values- Default &#x3D; 0, WorkFlowAssigned &#x3D; 1, Both &#x3D; 2, WorkflowDeleted &#x3D; 3 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


