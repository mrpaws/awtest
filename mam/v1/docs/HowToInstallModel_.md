# HowToInstallModel_

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_context** | **str** | Gets or sets install context (Supported values:  Device, User) where the package has to be installed. | [optional] 
**install_command** | **str** | Gets or sets the install command to install a package using the command line ex: \&quot;/quiet\&quot;. | [optional] 
**admin_privileges** | **bool** | Gets or sets a value indicating whether value indicating whether admin privileges are needed for the installation of a package. | [optional] 
**device_restart** | **str** | Gets or sets the device restart option. Supported values: DoNotRestart, ForceRestart, RestartIfNeeded. | [optional] 
**retry_count** | **int** | Gets or sets the number of times package installation operation will be retried.  Valid range 0 - 10. | [optional] 
**retry_interval_in_minutes** | **int** | Gets or sets the amount of time in minutes between retry operations.  Valid range 0 - 10. | [optional] 
**install_timeout_in_minutes** | **int** | Gets or sets the amount of time in minutes that the installation process can run before the installer considers the installation may have failed.  Valid range 0 - 60. | [optional] 
**installer_reboot_exit_code** | **str** | Gets or sets the success exit code. | [optional] 
**installer_success_exit_code** | **str** | Gets or sets the success exit code. | [optional] 
**restart_deadline_in_days** | **int** | Gets or sets the number of days within which device should reboot. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


