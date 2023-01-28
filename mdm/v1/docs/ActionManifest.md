# ActionManifest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | Gets or sets action to run on the device. | [optional] 
**critical** | **str** | Gets or sets flag variable, 3 options:  Continue - always continue regardless if manifest step fails  Continue on Success - Only continue to next manifest step if that step was successful, otherwise the product install process stops  Continue on Error - Continues when a error code of failed is returned. | [optional] 
**file_path_and_name** | **str** | Gets or sets path and name of File. | [optional] 
**source_file_path_and_name** | **str** | Gets or sets path and name of Source File. | [optional] 
**target_file_path_and_name** | **str** | Gets or sets path and name of Target File. | [optional] 
**path_and_name_of_folder** | **str** | Gets or sets path and name of folder. | [optional] 
**target_folder_path_and_name** | **str** | Gets or sets path and name of the Target folder. | [optional] 
**command_line_and_arguments_to_run** | **str** | Gets or sets command line And arguments to run. | [optional] 
**time_out** | **str** | Gets or sets how long to wait – 0: No Wait, -1: Wait Indefinitely, or &amp;gt; 0 Wait X seconds. | [optional] 
**process_or_app_to_terminate** | **str** | Gets or sets process or app to terminate. | [optional] 
**name_of_program_to_uninstall** | **str** | Gets or sets name of program to uninstall. | [optional] 
**airwatch_mdm_agent_upgrade_file** | **str** | Gets or sets airwatch Mdm Agent Upgrade File. | [optional] 
**execute_as_root** | **str** | Gets or sets whether to execute As Root [Specific to AppleOsX]. | [optional] 
**wait** | **str** | Gets or sets whether to wait for the action to complete [Specific to WindowsPc]. | [optional] 
**os_file** | **str** | Gets or sets file provided for OS Upgrade. | [optional] 
**install_un_managed_app** | **str** | Gets or sets the UnManaged App that is to be installed. | [optional] 
**un_install_un_managed_app** | **str** | Gets or sets the Unmanaged App that is to be uninstalled. | [optional] 
**script_file_path_and_name** | **str** | Gets or sets path and Name of the Script file. | [optional] 
**script_to_execute** | **str** | Gets or sets script to be executed. | [optional] 
**software_to_install** | **str** | Gets or sets software to be installed. | [optional] 
**install_file_path** | **str** | Gets or sets path of the file to be installed. | [optional] 
**custom_settings_file** | **str** | Gets or sets to apply Custom settings [specific to Android]. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


