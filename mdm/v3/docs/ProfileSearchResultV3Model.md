# ProfileSearchResultV3Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Profile uuid. | [optional] 
**name** | **str** | Profile name. | [optional] 
**status** | **str** | Profile status. | [optional] 
**assignment_type** | **str** | Profile Assignment type. | [optional] 
**managed_by** | **str** | Managed by organization group name. | [optional] 
**organization_group_uuid** | **str** | Profile organization group uuid | [optional] 
**platform** | **str** | Profile platform. | [optional] 
**configuration_type** | **str** | Profile configuration type. | [optional] 
**context** | **str** | Profile context. | [optional] 
**assigned_smart_groups** | [**list[ProfileSmartGroupV3Model]**](ProfileSmartGroupV3Model.md) | Assigned smart group. | [optional] 
**excluded_smart_groups** | [**list[ProfileSmartGroupV3Model]**](ProfileSmartGroupV3Model.md) | Excluded smart group. | [optional] 
**configured_payload** | [**list[ProfilePayloadV3Model]**](ProfilePayloadV3Model.md) | List of payloads configured for a profile. | [optional] 
**created_by_resource_profile** | **bool** | Flag to indicate whether the device profile created during resource profile creation or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


