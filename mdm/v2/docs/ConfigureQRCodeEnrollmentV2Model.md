# ConfigureQRCodeEnrollmentV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wi_fi_configuration** | **int** | Wi-Fi Configuration for Device | [optional] 
**wi_fi_ssid** | **str** | WiFi SSID. This property is effective only if &#39;wiFiConfiguration&#39; is set to &#39;Open/Secure&#39; | [optional] 
**wi_fi_password** | **str** | WiFi Password. This property is effective only if &#39;wiFiConfiguration&#39; is set to &#39;Secure&#39; | [optional] 
**agent_package_source** | **int** | The Agent Package download location. | [optional] 
**package_url** | **str** | Agent Package URL. This property is effective only if &#39;AgentPackageSource&#39; is set to &#39;HostedOnAnExternalUrl&#39; | [optional] 
**is_lg_configuration_enabled** | **bool** | Enrollment LocationGroup Enabled Flag. | [optional] 
**enrollment_location_group_id** | **str** | Enrollment LocationGroup ID. This property is effective only if &#39;IsLgConfigurationEnabled&#39; is set to &#39;true&#39; | [optional] 
**is_login_credentials_enabled** | **bool** | Is Login Credentials Enabled Flag. | [optional] 
**username** | **str** | Enrollment Username. This property is effective only if &#39;IsLoginCredentialsEnabled&#39; is set to &#39;true&#39; | [optional] 
**password** | **str** | Enrollment Password. This property is effective only if &#39;IsLoginCredentialsEnabled&#39; is set to &#39;true&#39; | [optional] 
**is_system_apps_enabled** | **bool** | Is System Apps Enabled Flag. | [optional] 
**force_aosp_enrollment** | **bool** | Force AOSP Enrollment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


