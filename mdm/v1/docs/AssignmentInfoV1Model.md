# AssignmentInfoV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_status** | **str** | Assignment status of the app. The possible values are [Assigned, NotAssigned] | 
**assigned_version** | **str** | The version of app assigned to the device | [optional] 
**effective_date** | **datetime** | The effective date of the app assignment in YYYY-MM-DDTHH:MM:SSZ format. | [optional] 
**latest_uem_action** | **str** | The latest server side action for the application. The possible values are [Unknown, PendingRelease, InstallCommandReadyForDevice, InstallCommandDispatched, InstallCommandFailed, RemoveAppCommandInHeldState, PendingRemoval, RemoveCommandSuccessful, RemoveApplicationFailed, VppLicenseNotAvailable, RequestRejected, RequestError, PendingApproval, RequestExpired, ProvisioningCommandDeleted, UserDeferredInstall] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


