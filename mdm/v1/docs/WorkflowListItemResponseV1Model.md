# WorkflowListItemResponseV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_uuid** | **str** | Identifier of the Workflow. | [optional] 
**name** | **str** | Name of the workflow. | [optional] 
**description** | **str** | Description of the workflow. | [optional] 
**created_on** | **datetime** | The date when the workflow was created. | [optional] 
**version** | **str** | Workflow version. | [optional] 
**assignment_uuids** | **list[str]** | The assignment UUIDs to which this workflow is assigned. | [optional] 
**workflow_entities** | [**list[WorkflowEntityTypeMap]**](WorkflowEntityTypeMap.md) | Gets or sets a list of the uuid of the entities contained within the workflow. | [optional] 
**created_by** | **str** | Gets or sets the username uuid who created the workflow. | [optional] 
**modified_on** | **datetime** | Gets or sets the time the workflow was last modified. | [optional] 
**published_on** | **datetime** | Gets or sets the time the workflow was last published. | [optional] 
**organization_group_uuid** | **str** | Gets or sets the organization group UUID. | [optional] 
**device_type** | **int** | Gets or sets the device type that the workflow targets. | [optional] 
**assignments** | [**list[WorkflowAssignmentSmartGroupMapModel]**](WorkflowAssignmentSmartGroupMapModel.md) | Gets or sets a list of the assignment and smartgoups mappings. | [optional] 
**catalog_display** | [**CatalogDisplayInfo**](CatalogDisplayInfo.md) | Gets or sets the optional, hub datalog display attributes. | [optional] 
**implicit_workflow** | **bool** | Gets or sets a value indicating whether the workflow is created by internal components implicitly. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


