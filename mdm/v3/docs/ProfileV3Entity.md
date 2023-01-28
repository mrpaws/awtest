# ProfileV3Entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payloads** | [**list[BasePayloadV3Entity]**](BasePayloadV3Entity.md) | Gets or sets different types for profile payloads. | [optional] 
**add_version** | **bool** | Gets or sets flag to indicate whether to add a new version during update operation. | [optional] 
**allow_removal** | **str** | Gets or sets allow removal type (Always, WithAuthorization, Never). | [optional] 
**assigned_schedule** | **list[int]** | Gets or sets assigned time schedule ids. | [optional] 
**assigned_smart_groups** | **list[str]** | Gets or Sets AssignedSmartGroups. | [optional] 
**assignment_type** | **str** | Gets or sets assignment type (Auto, Optional, Compliance). | [optional] 
**deployment** | **str** | Gets or sets is managed or not. | [optional] 
**description** | **str** | Gets or sets brief description of the profile. | [optional] 
**excluded_smart_groups** | **list[str]** | Gets or sets excluded smart groups. | [optional] 
**expiration_date** | **datetime** | Gets or sets expiration date of the profile. | [optional] 
**is_active** | **bool** | Gets or sets is active or not. | [optional] 
**managed_organization_group_uuid** | **str** | Gets or sets managed organization group uuid. | [optional] 
**name** | **str** | Gets or sets profile name. | [optional] 
**platform** | **str** | Gets or sets platform for profile. | [optional] 
**profile_context** | **str** | Gets or sets context of profile (Device, User). | [optional] 
**profile_uuid** | **str** | Gets or sets unique identifier for profile. | [optional] 
**removal_authorization_password** | **str** | Gets or sets password is required, when allow_removal is WITH_AUTHORIZATION. | [optional] 
**version** | **int** | Gets or sets profile version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


