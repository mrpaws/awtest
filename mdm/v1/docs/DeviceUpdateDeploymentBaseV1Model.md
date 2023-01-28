# DeviceUpdateDeploymentBaseV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name of the deployment. | 
**deployment_start_time** | **datetime** | Gets or sets the deployment start time. | 
**deployment_type** | **str** | Gets or sets the deployment type. Possible Values [DOWNLOAD_AND_INSTALL, DOWNLOAD_ONLY, INSTALL_ONLY]. | 
**smart_group_uuids** | **list[str]** | Gets or sets the list of smart group UUID where update needs to be deployed. | 
**notifications** | [**list[NotificationV1Model]**](NotificationV1Model.md) | Gets or sets the list of notification preferences for the deployment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


