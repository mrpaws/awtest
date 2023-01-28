# MsiDeploymentParameterModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_line_arguments** | **str** | Gets or sets command line options to be used when calling MSIEXEC.exe. | [optional] 
**install_timeout_in_minutes** | **int** | Gets or sets amount of time, in minutes that the installation process can run before the installer  considers the installation may have failed and no longer monitors the installation operation.Range 0-60. | [optional] 
**retry_count** | **int** | Gets or sets the number of times the download and installation operation will be retried before the installation will be marked as failed. With a limit of ‘10&#39; attempts. | [optional] 
**retry_interval_in_minutes** | **int** | Gets or sets amount of time, in minutes between retry operations. Range 0-10. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


