# FilesActionsDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Gets or sets files/Actions Identifier. | [optional] 
**name** | **str** | Gets or sets name of Files/Actions. | [optional] 
**description** | **str** | Gets or sets description for the Files/Actions. | [optional] 
**version** | **int** | Gets or sets version of Files/Actions. | [optional] 
**platform** | **str** | Gets or sets platform in which the Files/Actions will be applied. | [optional] 
**organization_group_id** | **int** | Gets or sets managed Organization Group ID. | [optional] 
**modified_on** | **str** | Gets or sets last date time at which Files/Actions is modified. | [optional] 
**files** | [**list[ProductFileDetials]**](ProductFileDetials.md) | Gets or sets details of Files to download to the device. | [optional] 
**install_manifests** | [**list[ActionManifest]**](ActionManifest.md) | Gets or sets the details of actions to perform in sequence when the file/action is installed on the devicem. | [optional] 
**uninstall_manifests** | [**list[ActionManifest]**](ActionManifest.md) | Gets or sets the details of actions to perform in sequence when the file/action is uninstalled from the device. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


