# VppDeploymentParametersV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_type** | **int** | Type to deploy the application. | [optional] 
**remove_on_unenroll** | **bool** | Indicates whether to remove the application on device&#39;s unenrollment. | [optional] 
**prevent_application_backup** | **bool** | Indicates whether to prevent the application&#39;s backup. | [optional] 
**allow_management** | **bool** | Indicates whether to assume management of the user installed application. | [optional] 
**use_vpn** | **bool** | Indicates whether to use the VPN profile. | [optional] 
**vpn_profile_uuid** | **str** | VPN profile&#39;s UUID. | [optional] 
**send_application_configuration** | **bool** | Indicates whether to send the application configuration. | [optional] 
**application_configurations** | [**list[ApplicationConfigurationV2Model]**](ApplicationConfigurationV2Model.md) | Application&#39;s configurations. | [optional] 
**send_application_attributes** | **bool** | Indicates whether to send the application attributes. | [optional] 
**prevent_removal** | **bool** | Indicates whether to send the prevent removal application attributes. | [optional] 
**application_attributes** | [**list[ApplicationConfigurationV2Model]**](ApplicationConfigurationV2Model.md) | Application&#39;s attributes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


