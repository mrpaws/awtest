# DeviceSampleInfoV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installed_status** | **str** | Installation status of the app on the device. The possible values are [Installed, NotInstalled] | 
**installed_version** | **str** | The version of app installed on the device | [optional] 
**latest_app_reason** | **str** | The application reason reported by the device. The possible values are [NeedsRedemption, Redeeming, Prompting, Installing, Managed, MDMRemoval, MDMRemoved, ManagedButUninstalled, UserRejected, Failed, Unknown, UserInstalledApp, AwaitingInstallOnDevice, Updating, ManagementRejected, PromptingForManagement, DownloadInProgress, DownloadFailed, RemoveApplicationFailed, FinalDetectionFailed, DeviceEligibilityCheckFailed, ExecutionFailed, DependentAppValidationFailed, CheckingDeviceEligibility, ValidatingDependentApps, PendingReboot] | [optional] 
**latest_app_reason_time** | **datetime** | The time at which the reason was reported by the device | [optional] 
**latest_app_sample_event** | **str** | The latest transient reason reported by the device. The possible values are [NeedsRedemption, Redeeming, Prompting, MDMRemoved, UserRejected, Failed, UserInstalledApp, AwaitingInstallOnDevice, Updating, ManagementRejected, PromptingForManagement, DownloadInProgress, RemoveApplicationFailed, CheckingDeviceEligibility, ValidatingDependentApps, PendingReboot] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


