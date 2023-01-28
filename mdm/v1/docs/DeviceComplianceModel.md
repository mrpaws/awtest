# DeviceComplianceModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**EntityId_**](EntityId_.md) | The model&#39;s assigned unique id. | [optional] 
**uuid** | **str** | The model&#39;s universally unique identifier (UUID). | [optional] 
**compliant_status** | **bool** | Indicates whether the device is compliant or not. | [optional] 
**compliance_pending** | **bool** | Indicates whether the compliance status is pending for the device. | [optional] 
**policy_name** | **str** | The name of the compliance policy for the device. | [optional] 
**policy_detail** | **str** | The description of the compliance policy. | [optional] 
**last_compliance_check** | **datetime** | The date and time of the last compliance check. | [optional] 
**next_compliance_check** | **datetime** | The date and time of the next compliance check. | [optional] 
**action_taken** | [**list[ComplianceActionTakenModel]**](ComplianceActionTakenModel.md) | The compliance action taken on the device. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


