# PolicyModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**uuid** | **str** | Unique identifier of the policy | 
**name** | **str** | Name of the policy | 
**path** | **str** | The path to the policy | [optional] 
**_class** | **str** | The classification of the policy (Machine/User/Both) | [optional] 
**class_name** | **str** | The classification of the policy (Machine/User/Both) | [optional] 
**explanation** | **str** | Help text associated with the policy | [optional] 
**status** | **int** | policy state | [optional] 
**available_states** | **list[str]** | The allowed states for this policy | [optional] 
**layout** | [**list[BaseElementModel]**](BaseElementModel.md) | The policy options | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


