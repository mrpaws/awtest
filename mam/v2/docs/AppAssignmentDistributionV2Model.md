# AppAssignmentDistributionV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the assignment group. | 
**description** | **str** | Description of the assignment group. | [optional] 
**smart_groups** | **list[str]** | Collection of smart group uuids. | [optional] 
**bsp_assignments** | [**AppAssignmentBspV1Model**](AppAssignmentBspV1Model.md) | BSP app assignments with smart groups applicable for online and offline licenses. | [optional] 
**vpp_app_details** | [**AppAssignmentVppV1Model**](AppAssignmentVppV1Model.md) | Purchased application assignments with VPP licenses. | [optional] 
**app_delivery_method** | **int** | App Delivery Method | [optional] 
**pre_release_version** | **int** | App pre release version applicable for Android For Work apps. | [optional] 
**app_track_id** | **str** | App track id for Android For Work Apps. | [optional] 
**effective_date** | **datetime** | The effective datetime for the application in Admin&#39;s timezone. Applicable for internal application only.  If effective datetime is null or not provided then current admin&#39;s datetime will be considered. | [optional] 
**auto_update_devices_with_previous_versions** | **bool** | Auto update devices with previous versions is applicable for Android, iOS and Windows internal apps. | [optional] 
**display_in_app_catalog** | **bool** | Display in App Catalog flag is applicable for macOS and Windows SFD internal apps. | [optional] 
**requires_approval** | **bool** | Requires approval flag is applicable only for Windows SFD apps. | [optional] 
**hide_notifications** | **bool** | Hide notifications flag is applicable only for Windows SFD apps. | [optional] 
**application_transforms** | **list[str]** | Collection of application transforms uuids applicable only for Windows SFD apps. | [optional] 
**installer_deferral_allowed** | **bool** | Gets or sets whether installer deferral is allowed. | [optional] 
**installer_deferral_interval** | **int** | Gets or sets the number of hours of installer deferral interval. | [optional] 
**installer_deferral_exit_code** | **str** | Gets or sets the installer deferral exit code. | [optional] 
**is_default_assignment** | **bool** | Flag to check if the assignment is default. | [optional] 
**reboot_override** | **bool** | Flag to check the reboot override option. | [optional] 
**msi_deployment_override_params** | [**MsiDeploymentOptionsV1Model**](MsiDeploymentOptionsV1Model.md) | Reboot option in case of override | [optional] 
**keep_app_updated_automatically** | **bool** | Keep app updated automatically (To push the application to the eligible devices). This is supposed to be only for macOS. | [optional] 
**allow_user_to_uninstall_from_catalog** | **bool** | Allow user to uninstall from catalog hub. This is supposed to be only for macOS. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


