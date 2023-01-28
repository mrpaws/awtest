# ApplicationGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_group_id** | **str** | Gets or sets application Group ID. | [optional] 
**name** | **str** | Gets or sets name of Application Group. | [optional] 
**platform** | **str** | Gets or sets device Platform Name. | [optional] 
**app_group_type** | **str** | Gets or sets type of Application Group. | [optional] 
**description** | **str** | Gets or sets application Group description. | [optional] 
**managed_by_organization_group_id** | **str** | Gets or sets organization group ID in which Application group is managed. | [optional] 
**organization_groups** | [**list[AppGroupOG]**](AppGroupOG.md) | Gets or sets list of Organization Groups to which this App Group is assigned. | [optional] 
**user_groups** | [**list[AppGroupUserGroup]**](AppGroupUserGroup.md) | Gets or sets list of User Groups to which this App Group is assigned. | [optional] 
**device_ownership** | **str** | Gets or sets device Ownership Name. | [optional] 
**device_model** | **str** | Gets or sets device Model. | [optional] 
**device_operating_system** | **str** | Gets or sets device Operating System. | [optional] 
**is_active** | **bool** | Gets or sets a value indicating whether app Group status. | [optional] 
**app_count** | **str** | Gets or sets number of Applications in the App Group. | [optional] 
**applications** | [**list[ApplicationGroupItem]**](ApplicationGroupItem.md) | Gets or sets application Items required to create app group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


