# AppAssignmentRestrictionV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remove_on_unenroll** | **bool** | Removes the application from end user device when the device unenrolls and applicable for Apple, macOS and Android apps. | [optional] 
**prevent_application_backup** | **bool** | Prevent backing up application data to iCloud(iOS only) | [optional] 
**make_app_mdm_managed** | **bool** | This flag allows admin to take over management of user installed application so that additional actions like Removals,  Application configuration can be applied to the end user device.  This flag is applicable for iOS and Windows SFD apps. | [optional] 
**managed_access** | **bool** | If Managed access is enabled, by default Require Management will be enabled | [optional] 
**desired_state_management** | **bool** | Desired state management flag and applicable for macOS SFD apps &amp;amp; Windows Desktop SFD apps. | [optional] 
**prevent_removal** | **bool** | If prevent removal is enabled, then it will  prevent an app from being removed from devices after installation  or conversion to management. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


