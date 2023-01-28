# GeneralPayloadV4Entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **int** | Gets or sets profileId. | [optional] 
**afw_oem_settings_enabled** | **bool** | Gets or sets tracks if AFW OEM settings are enabled. | [optional] 
**afw_oem_type** | **int** | Gets or sets tracks what OEM settings have been included. | [optional] 
**name** | **str** | Gets or sets name. | [optional] 
**description** | **str** | Gets or sets description. | [optional] 
**profile_scope** | **str** | Gets or sets device Profile Scope. | [optional] 
**version** | **int** | Gets or sets version. | [optional] 
**create_new_version** | **bool** | Gets or sets a value indicating whether add New Version. | [optional] 
**assignment_type** | **str** | Gets or sets assignment Type. | [optional] 
**profile_context** | **str** | Gets or sets the profile context. | [optional] 
**enable_provisioning** | **bool** | Gets or sets a value indicating whether flag to indicate Profile will be used for Product Provisioning. Valid values: true, false. | [optional] 
**is_active** | **bool** | Gets or sets a value indicating whether flag to indicate Profile Status. | [optional] 
**is_managed** | **bool** | Gets or sets a value indicating whether is Managed. | [optional] 
**password** | **str** | Gets or sets unlock Password. | [optional] 
**allow_removal** | **str** | Gets or sets the allow removal. | [optional] 
**assigned_smart_groups** | [**list[SmartGroupEntity]**](SmartGroupEntity.md) | Gets or sets the smart groups. | [optional] 
**excluded_smart_groups** | [**list[SmartGroupEntity]**](SmartGroupEntity.md) | Gets or sets the excluded groups. | [optional] 
**managed_location_group_id** | **int** | Gets or sets the ID of the RootLocationGroup. | [optional] 
**assigned_geofence_area** | **list[int]** | Gets or sets the area ids. | [optional] 
**assigned_schedule** | **list[int]** | Gets or sets the scheduled ids. | [optional] 
**expiration_date** | **str** | Gets or sets expiration Date of the Profile [Applicable for Apple Profiles]. | [optional] 
**profile_uuid** | **str** | Gets or sets the Profile Unique Identifier. | [optional] 
**is_provisioned_for_oobe** | **bool** | Gets or sets a value indicating whether is profile to be included for oobe provisioning. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


