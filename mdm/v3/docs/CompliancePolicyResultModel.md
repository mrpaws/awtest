# CompliancePolicyResultModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The policy&#39;s universally unique identifier (UUID). | [optional] 
**compliance_status** | **int** | The compliance evaluation of the policy. | [optional] 
**policy_name** | **str** | The name of the compliance policy for the device. | [optional] 
**policy_description** | **str** | The description of the compliance policy. | [optional] 
**last_compliance_check** | **datetime** | The date and time of the last compliance check in UTC. | [optional] 
**next_compliance_check** | **datetime** | The date and time of the next compliance check in UTC. | [optional] 
**actions_taken** | [**list[ComplianceActionTakenV2Model]**](ComplianceActionTakenV2Model.md) | The compliance actions taken on the device due to non-compliance policy evaluation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


