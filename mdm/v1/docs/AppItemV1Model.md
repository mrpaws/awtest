# AppItemV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the application | [optional] 
**assignment_status** | **str** | Assignment status of the app. The possible values are [Assigned, NotAssigned] | [optional] 
**assigned_version** | **str** | The version of app assigned to the device | [optional] 
**installed_status** | **str** | Installation status of the app on the device. The possible values are [Installed, NotInstalled] | [optional] 
**installed_version** | **str** | The version of app installed on the device | [optional] 
**latest_uem_action** | **str** | The latest server side trigger for the application. The possible values are [Unknown, PendingRelease, InstallCommandReadyForDevice, InstallCommandDispatched, InstallCommandFailed, RemoveAppCommandInHeldState, PendingRemoval, RemoveCommandSuccessful, RemoveApplicationFailed, VppLicenseNotAvailable, RequestRejected, RequestError, PendingApproval, RequestExpired, ProvisioningCommandDeleted, UserDeferredInstall] | [optional] 
**latest_uem_action_time** | **datetime** | The time of the latest server side trigger in YYYY-MM-DDTHH:MM:SSZ format. | [optional] 
**bundle_id** | **str** | Gets or sets the unique bundle identifier of the application, e.g. com.hotels.HotelsNearMe. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


