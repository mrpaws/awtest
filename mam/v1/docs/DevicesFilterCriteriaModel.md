# DevicesFilterCriteriaModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_identifier** | **str** | The bundle identifier of an application | [optional] 
**organization_group_uuid** | **str** | The Organization Group identifier where the device list needs to be fetched. If not set it will be defaulted to admin Organization Group identifier. | [optional] 
**app_organization_group_uuid** | **str** | The Organization Group identifier in which the app was created. | [optional] 
**device_type** | **str** | The platform of the application | [optional] 
**search_text** | **str** | If provided, the records matching this text will be selected. The search will be applied on the following properties [username, phone number, Organization Group name, supported model, user domain, device model name]. The default value will be empty string. | [optional] 
**assignment_type** | **str** | Assignment status of an application to the device supported values. is \&quot;ASSIGNED\&quot; | [optional] 
**is_installed_version_equals_to_assigned_version** | **bool** | Flag to get the devices where install application versions are same as assigned application version. | [optional] 
**is_installed_version_not_equals_to_assigned_version** | **bool** | Flag to get the devices where install application versions are different assigned application version. | [optional] 
**is_application_version_not_installed** | **bool** | Flag to get the devices where application is not installed. | [optional] 
**applications_status** | **list[int]** | List of device reported status. If nothing is passed, all the assigned devices will be returned based on the other filters. The possible values are [NeedsRedemption, Redeeming, Prompting, Installing, Managed, MDMRemoval, MDMRemoved, ManagedButUninstalled, UserRejected, Failed, Unknown, UserInstalledApp, AwaitingInstallOnDevice, Updating, ManagementRejected, PromptingForManagement, DownloadInProgress, DownloadFailed, RemoveApplicationFailed, FinalDetectionFailed, DeviceEligibilityCheckFailed, ExecutionFailed, DependentAppValidationFailed, CheckingDeviceEligibility, ValidatingDependentApps, PendingReboot] | [optional] 
**last_action_taken** | **list[int]** | List of possible server side action. If nothing is passed, all the assigned devices will be returned based on the other filters. The possible values are [Unknown, PendingRelease, InstallCommandReadyForDevice, InstallCommandDispatched, InstallCommandFailed, RemoveAppCommandInHeldState, PendingRemoval, RemoveCommandSuccessful, RemoveApplicationFailed, VppLicenseNotAvailable, RequestRejected, RequestError, PendingApproval, RequestExpired, ProvisioningCommandDeleted, UserDeferredInstall] | [optional] 
**smart_group_uuids** | **list[str]** | List of smart group identifiers | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


