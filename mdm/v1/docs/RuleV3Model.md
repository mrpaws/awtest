# RuleV3Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial_number** | **str** | The serial number of the rule. | [optional] 
**action** | [**DeviceTrafficRuleActionModel**](DeviceTrafficRuleActionModel.md) | Action to be taken by application(s) for the configured domains | [optional] 
**destinations** | **list[str]** | Configured domains for whom the action will be taken | [optional] 
**applications** | [**list[DeviceTrafficRuleApplicationModel]**](DeviceTrafficRuleApplicationModel.md) | One or more tunnel applications configured that will honor the rule | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


