# AssignmentV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the assignment. | 
**description** | **str** | Description about the assignment. | [optional] 
**organization_group_uuid** | **str** | UUID of the Organization Group. | 
**deployment_mode** | **int** | The deployment mode of the workflow. | 
**show_in_catalog** | **bool** | Gets or sets a value indicating whether to show resource in catalog. | [optional] 
**priority** | **int** | The priority of the assignment. Must be greater than 0 and should be unique for a workflow. | [optional] 
**assigned_smartgroup_uuids** | **list[str]** | The smart group UUIDs to which this workflow need to be assigned. | [optional] 
**workflow_assignment_state** | **int** | Gets or sets the workflow assignment state. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


