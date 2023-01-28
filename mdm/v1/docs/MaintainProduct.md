# MaintainProduct

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets name of the product. | [optional] 
**product_id** | **int** | Gets or sets iD of the product. | [optional] 
**description** | **str** | Gets or sets description of the product. | [optional] 
**platform** | **int** | Gets or sets platform ID in which product is deployed. | [optional] 
**applicability_rule** | **str** | Gets or sets assignment rules to filter out devices within a Smart Group. | [optional] 
**pause_resume** | **bool** | Gets or sets a value indicating whether whether the product is in Pause or resume state. | [optional] 
**product_type** | **int** | Gets or sets the type of Product. | [optional] 
**activation_date** | **str** | Gets or sets date of Activation. | [optional] 
**deactivation_date** | **str** | Gets or sets date of Deactivation. | [optional] 
**auto_retry** | **bool** | Gets or sets a value indicating whether [automatic retry]. | [optional] 
**device_reprocess** | **bool** | Gets or sets a value indicating whether device reprocess for this product is applicable or not. | [optional] 
**deployment_mode** | **int** | Gets or sets deployment Mode (Possible Values are RelayServerWithDeviceServicesBackup, RelayServerOnly). | [optional] 
**dependencies** | [**list[DevicePolicyDependencyEntity]**](DevicePolicyDependencyEntity.md) | Gets the list of products in which the given product is dependent on. | [optional] 
**down_load_conditions** | [**list[MaintainProductCondition]**](MaintainProductCondition.md) | Gets or sets list of conditions for download. | [optional] 
**install_conditions** | [**list[MaintainProductCondition]**](MaintainProductCondition.md) | Gets or sets list of conditions for install. | [optional] 
**smart_groups** | [**list[MaintainProductSmartGroup]**](MaintainProductSmartGroup.md) | Gets or sets details of the Smart Group to which Product belong. | [optional] 
**steps** | [**list[MaintainProductStep]**](MaintainProductStep.md) | Gets or sets steps details of the product. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


