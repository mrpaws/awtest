# SmartGroupEditV1Model_

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets smart Group Name. | [optional] 
**criteria_type** | **str** | Gets or sets smart Group Criteria Type (example: \&quot;All\&quot;, \&quot;UserDevice\&quot;). | [optional] 
**managed_by_organization_group_id** | **str** | Gets or sets managedBy Organization Group Identifier. | [optional] 
**organization_groups** | [**list[SmartGroupOG]**](SmartGroupOG.md) | Gets or sets organizationGroups List. | [optional] 
**user_groups** | [**list[SmartGroupUserGroup]**](SmartGroupUserGroup.md) | Gets or sets userGroups List. | [optional] 
**tags** | [**list[SmartGroupTag]**](SmartGroupTag.md) | Gets or sets smartGroup Tags List. | [optional] 
**ownerships** | **list[str]** | Gets or sets ownerships List (example : CorporateDedicated, CorporateShared, EmployeeOwned, AllOwnerships). | [optional] 
**platforms** | **list[str]** | Gets or sets platforms List (example : WindowsMobile, Apple, BlackBerry, Android, WindowsPhone, WindowsPc, AppleOsX, WindowsPhone8, WinRT, etc ). | [optional] 
**models** | **list[str]** | Gets or sets models (example : iPad). | [optional] 
**operating_systems** | [**list[SmartGroupOperatingSystem]**](SmartGroupOperatingSystem.md) | Gets or sets operating Systems List. | [optional] 
**user_additions** | [**list[SmartGroupUser]**](SmartGroupUser.md) | Gets or sets list of explicitly added users. | [optional] 
**device_additions** | [**list[SmartGroupDevice_]**](SmartGroupDevice_.md) | Gets or sets list of explicitly added devices. | [optional] 
**user_exclusions** | [**list[SmartGroupUser]**](SmartGroupUser.md) | Gets or sets list of excluded users. | [optional] 
**device_exclusions** | [**list[SmartGroupDevice_]**](SmartGroupDevice_.md) | Gets or sets list of excluded devices. | [optional] 
**user_group_exclusions** | [**list[SmartGroupUserGroup]**](SmartGroupUserGroup.md) | Gets or sets list of excluded user groups. | [optional] 
**management_types** | **list[str]** | Gets or sets management Type list (example : MdmEnrolled, ApplicationManaged). | [optional] 
**enrollment_categories** | **list[str]** | Gets or sets enrollment Category list (example :  DepEnrolled, Supervised, UserApprovedMdmEnrolled , SharedIpad, AndroidLegacy,  AndroidEnterprise, AadEnrolled). | [optional] 
**oem_and_models** | [**list[OEMAndModel]**](OEMAndModel.md) | Gets or sets device Manufacturer/OEM and Model. | [optional] 
**cpu_architectures** | **list[str]** | Gets or sets device cpu architectures. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


