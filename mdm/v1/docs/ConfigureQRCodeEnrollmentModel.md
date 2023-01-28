# ConfigureQRCodeEnrollmentModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_device_connect_to_wifi_prior_to_enrollment** | **bool** | Is Device needs to Connect to Wifi Prior To Enrollment. | [optional] 
**wi_fi_ssid** | **str** | WiFi SSID. This property is effective only if &#39;IsDeviceConnectToWifiPriorToEnrollment&#39; is set to &#39;true&#39; | [optional] 
**wi_fi_password** | **str** | WiFi Password. This property is effective only if &#39;IsDeviceConnectToWifiPriorToEnrollment&#39; is set to &#39;true&#39; | [optional] 
**agent_package_source** | **int** | The Agent Package download location. | [optional] 
**package_url** | **str** | Agent Package URL. This property is effective only if &#39;AgentPackageSource&#39; is set to &#39;HostedOnAnExternalUrl&#39; | [optional] 
**is_lg_configuration_enabled** | **bool** | Enrollment LocationGroup Enabled Flag. | [optional] 
**enrollment_location_group_id** | **str** | Enrollment LocationGroup ID. This property is effective only if &#39;IsLgConfigurationEnabled&#39; is set to &#39;true&#39; | [optional] 
**is_login_credentials_enabled** | **bool** | Is Login Credentials Enabled Flag. | [optional] 
**username** | **str** | Enrollment Username. This property is effective only if &#39;IsLoginCredentialsEnabled&#39; is set to &#39;true&#39; | [optional] 
**password** | **str** | Enrollment Password. This property is effective only if &#39;IsLoginCredentialsEnabled&#39; is set to &#39;true&#39; | [optional] 
**is_system_apps_enabled** | **bool** | Is System Apps Enabled Flag. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


