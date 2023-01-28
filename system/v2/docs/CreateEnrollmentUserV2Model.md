# CreateEnrollmentUserV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | Enrollment user external id | [optional] 
**user_name** | **str** | Enrollment user username | 
**password** | **str** | Enrollment user password | [optional] 
**first_name** | **str** | Enrollment user firstname | [optional] 
**last_name** | **str** | Enrollment user lastname | [optional] 
**display_name** | **str** | Enrollment user displayname | [optional] 
**user_principal_name** | **str** | Enrollment user userprincipalname | [optional] 
**email_address** | **str** | Enrollment user email address | [optional] 
**email_username** | **str** | Enrollment user email username | [optional] 
**phone_number** | **str** | Enrollment user phone number | [optional] 
**mobile_number** | **str** | Enrollment user mobile number | [optional] 
**message_type** | **str** | Enrollment user message type, available options are None, Email and SMS. | [optional] 
**message_template_uuid** | **str** | Enrollment user message template uuid | [optional] 
**enrollment_role_uuid** | **str** | Enrollment user role uuid | [optional] 
**status** | **bool** | Enrollment user status, indicating whether enrollment user is active | [optional] 
**security_type** | **str** | Enrollment user security type, available options are basic, directory and authenticationProxy. | 
**device_staging_enabled** | **bool** | Enrollment user device staging enabled | [optional] 
**device_staging_type** | **str** | Enrollment user device staging type, available options are StagingDisabled, SingleUserStagingStandard, SingleUserStagingAdvanced, MultipleUserStaging, MultipleUserStagingSingleUserStandard and MultipleUserStagingSingleUserAdvanced. | [optional] 
**organization_group_uuid** | **str** | Enrollment user organization group uuid | [optional] 
**enrollment_organization_group_uuid** | **str** | Enrollment user enrollment organization group uuid | [optional] 
**custom_attribute1** | **str** | The enrollment user customAttribute1 | [optional] 
**custom_attribute2** | **str** | The enrollment user customAttribute2 | [optional] 
**custom_attribute3** | **str** | The enrollment user customAttribute3 | [optional] 
**custom_attribute4** | **str** | The enrollment user customAttribute4 | [optional] 
**custom_attribute5** | **str** | The enrollment user customAttribute5 | [optional] 
**aad_mapping_attribute** | **str** | When using the AirWatch Provisioning Adapter inside of Workspace ONE Access or using the UEM APIs to create users from 3rd party identity stores to create enrollment users, provide AadMappingAttribute to supports Win10 Azure Compliance/OOBE flow. | [optional] 
**department** | **str** | The department that the enrollment user belongs to. | [optional] 
**employee_identifier** | **str** | The employee identifier of enrollment user. | [optional] 
**cost_center** | **str** | The cost center associated to the enrollment user. | [optional] 
**android_shared_device_mode** | **str** | A value indicating the mode used to manage android shared devices. Applicable only for android platform with multi staging enabled. Defaults to Launcher. | [optional] 
**android_shared_device_admin_mode_passcode** | **str** | The Android Shared device admin mode passcode for native check out. | [optional] 
**android_shared_device_system_apps_enabled** | **bool** | Android Shared device system apps enabled for native check out. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


