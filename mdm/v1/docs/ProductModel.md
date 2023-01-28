# ProductModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**EntityId_**](EntityId_.md) | Gets or sets product Identifier. | [optional] 
**platform_id** | **int** | Gets or sets the platform identifier. | [optional] 
**name** | **str** | Gets or sets product Name. | [optional] 
**managed_by_organization_group_id** | **str** | Gets or sets managedBy Root Organization Group Identifier. | [optional] 
**description** | **str** | Gets or sets product Description. | [optional] 
**managed_by_organization_group_name** | **str** | Gets or sets managedBy Root Organization Group Name. | [optional] 
**active** | **bool** | Gets or sets a value indicating whether specifies whether the product is active or not, true -&amp;gt; active, false -&amp;gt; inactive. | [optional] 
**platform** | **str** | Gets or sets platform name of the Product. | [optional] 
**smart_groups** | [**list[ProductSmartGroup]**](ProductSmartGroup.md) | Gets or sets smart group details which are assigned to current Product. | [optional] 
**manifest** | [**Manifest_**](Manifest_.md) | Gets or sets manifesr Resource. | [optional] 
**conditions** | [**list[ProductCondition1]**](ProductCondition1.md) | Gets or sets device Policy Conditions that are associated with the current Product. | [optional] 
**total_assigned** | **int** | Gets or sets total number of devices which are assigned. | [optional] 
**compliant** | **int** | Gets or sets number of devices which are compliant. | [optional] 
**in_progress** | **int** | Gets or sets number of devices for which provisioning is in progress. | [optional] 
**failed** | **int** | Gets or sets number of devices for which product provisioning got failed. | [optional] 
**rule_logic** | **str** | Gets or sets product Rule. | [optional] 
**activation_date_time** | **str** | Gets or sets product Activation time. | [optional] 
**deactivation_date_time** | **str** | Gets or sets product Deactivation time. | [optional] 
**pause_resume** | **bool** | Gets or sets a value indicating whether pause Resume. | [optional] 
**deployment_mode** | **int** | Gets or sets deployment Mode. | [optional] 
**device_policy_type_id** | **int** | Gets or sets device Policy Type ID. | [optional] 
**device_policy_type** | **str** | Gets or sets device Policy Type Name. | [optional] 
**activation_or_deactivation_type** | **str** | Gets or sets activation or Deactivation type, like \&quot;Auto\&quot;, \&quot;Partial Auto\&quot;, \&quot;Manual\&quot; etc. | [optional] 
**compliance_override_rule** | **str** | Gets or sets compliance Override  Rule. | [optional] 
**auto_retry** | **bool** | Gets or sets a value indicating whether [automatic retry]. | [optional] 
**device_reprocess** | **bool** | Gets or sets a value indicating whether device reprocess is enabled or not. | [optional] 
**device_policy_uuid** | **str** | Gets or sets the device policy uuid. | [optional] 
**is_expedited** | **bool** | Gets or sets a value indicating whether product expedited. | [optional] 
**version** | **int** | Gets or sets the version of a product. | [optional] 
**product_e_tag** | **str** | Gets or sets the product ETag. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


