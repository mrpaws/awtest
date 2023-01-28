# ReadNotificationModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_user_id** | **int** | Gets or sets iD of the admin user assigned to the notification. | [optional] 
**created_on** | **datetime** | Gets or sets datetime when this notification was created. | [optional] 
**globalized_created_on** | **datetime** | Gets or sets notification created datetime in admin&#39;s time zone. | [optional] 
**organization_group_path** | **str** | Gets or sets organization Group Name. | [optional] 
**params** | **list[object]** | Gets or sets notification params to be used as format arguments into the message label key. Params values should be in globalized form. | [optional] 
**action_label_key** | **str** | Gets or sets action Label Key for notification. | [optional] 
**data** | **str** | Gets or sets data for notification. | [optional] 
**organization_group_id** | **int** | Gets or sets organization group ID where this notification was triggered. | [optional] 
**title** | **str** | Gets or sets label key used as the notification title. | [optional] 
**is_acknowledged** | **bool** | Gets or sets a value indicating whether notification acknowledgedment flag. | [optional] 
**acknowledged_on** | **datetime** | Gets or sets datetime when the notification was acknowledged. | [optional] 
**type_id** | **int** | Gets or sets notification type (1 &#x3D; info, 2 &#x3D; warning). | [optional] 
**type_value** | **str** | Gets or sets notification type&#39;s globalized value. | [optional] 
**category_id** | **int** | Gets or sets notification category. | [optional] 
**category_value** | **str** | Gets or sets category&#39;s globalized value. | [optional] 
**resource_key** | **str** | Gets or sets resource required to receive notifications for this category. | [optional] 
**resource_value** | **str** | Gets or sets resource required to receive notifications for this category. | [optional] 
**priority** | **int** | Gets or sets notification priority (1 &#x3D; low, 2 &#x3D; medium, 3 &#x3D; high, 4 &#x3D; critical). | [optional] 
**message** | **str** | Gets or sets label key used as the notification message. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


