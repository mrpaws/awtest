# MaintainEventActionInputEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maintain_general_input** | [**MaintainGeneralAPIEntity_**](MaintainGeneralAPIEntity_.md) | Gets or sets holds Organization Group ID and whether there is permission to insert to the Organization Group or not. | [optional] 
**name** | **str** | Gets or sets name of the Event Action. | [optional] 
**description** | **str** | Gets or sets description of the Event Action. | [optional] 
**device_platform_id** | **int** | Gets or sets device platform for which Event Action will be created for. | [optional] 
**action_interval** | **int** | Gets or sets action Interval for Event Action. | [optional] 
**actions** | [**list[MaintainEventActionAction]**](MaintainEventActionAction.md) | Gets or sets details of Actions to be excecuted in the Event Action. | [optional] 
**conditions** | [**list[MaintainEventActionCondition]**](MaintainEventActionCondition.md) | Gets or sets details of Condtions in the Event Action. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


