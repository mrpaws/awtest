# AppAssignmentV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** | Priority of an assignment policy with 0 being the highest priority. | 
**distribution** | [**AppAssignmentDistributionV1Model**](AppAssignmentDistributionV1Model.md) | App assignment distribution model | 
**restriction** | [**AppAssignmentRestrictionV1Model**](AppAssignmentRestrictionV1Model.md) | App assignment restriction model | [optional] 
**tunnel** | [**AppAssignmentTunnelV1Model**](AppAssignmentTunnelV1Model.md) | App assignment tunnel model | [optional] 
**application_configuration** | [**list[AppConfigurationV1Model]**](AppConfigurationV1Model.md) | List of application configurations. | [optional] 
**application_attributes** | [**list[AppConfigurationV1Model]**](AppConfigurationV1Model.md) | List of application attributes. | [optional] 
**is_dynamic_template_saved** | **bool** | Flag to check if the assignment configuration is being saved through DDUI. | [optional] 
**is_apple_education_assignment** | **bool** | Gets or sets a value indicating whether an Apple education assignment is configured or not.  Edu assignment does not allow deletion on assignment page, this is used to group edu assignment separately  with other assignment. | [optional] 
**is_android_enterprise_config_template** | **bool** | Gets or sets a value indicating whether the configuration was saved from managed configuration enterprise template. | [optional] 
**app_profiles_mapping** | [**list[ApplicationDeploymentProfileMapV1Model]**](ApplicationDeploymentProfileMapV1Model.md) | Gets or sets a SDK profile, modular SDK profile mappings with the assignment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


