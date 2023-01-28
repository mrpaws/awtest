# MaintainFileActionModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maintain_general_input** | [**MaintainGeneralAPIModel_**](MaintainGeneralAPIModel_.md) | Gets or sets this holds Organization Group ID and whether there is permission to insert to the Organization Group or not. | [optional] 
**name** | **str** | Gets or sets name of the File Action. | [optional] 
**description** | **str** | Gets or sets description of the File Action. | [optional] 
**device_platform_id** | **int** | Gets or sets device platform that file/action will be created for. | [optional] 
**remove_on_uninstall** | **bool** | Gets or sets a value indicating whether flag to indicate if files should automatically be removed on uninstall. | [optional] 
**manifest_install_steps** | [**list[FileActionManifestStepModel]**](FileActionManifestStepModel.md) | Gets or sets details of Manifest Install Steps. | [optional] 
**manifest_un_install_steps** | [**list[FileActionManifestStepModel]**](FileActionManifestStepModel.md) | Gets or sets details of Manifest UnInstall Steps. | [optional] 
**repository_files** | [**list[RepositoryFileModel]**](RepositoryFileModel.md) | Gets or sets details of Repository Files. | [optional] 
**blob_files** | [**list[BlobFileModel]**](BlobFileModel.md) | Gets or sets details of Blob Files. | [optional] 
**file_action_uuid** | **str** | Gets or sets unique identifier of the File Action. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


