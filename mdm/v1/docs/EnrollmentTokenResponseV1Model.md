# EnrollmentTokenResponseV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_group_name** | **str** | Organization group where the token is created. | [optional] 
**friendly_name** | **str** | Friendly name of the token. | [optional] 
**udid** | **str** | UDID of the device | [optional] 
**serial_number** | **str** | Serial number of the device | [optional] 
**imei** | **str** | Device IMEI hardware identifier. | [optional] 
**asset_number** | **str** | Device asset number. | [optional] 
**operating_system** | **str** | Operating system of the device. | [optional] 
**platform** | **int** | Platform type of the device | [optional] 
**model_name** | **str** | Model of the device. | [optional] 
**enrollment_status** | **int** | Enrollment status of the device. | [optional] 
**status** | **int** | Enrollment token status. | [optional] 
**source** | **int** | Enrollment token source. | [optional] 
**type** | **int** | Enrollment token type. | [optional] 
**registration_date** | **datetime** | Enrollment token registration date. | [optional] 
**expiration_date** | **datetime** | Enrollment token expiration date. | [optional] 
**user_name** | **str** | User name associated with the device. | [optional] 
**ownership_type** | **str** | Ownership type of the device (CorporateDedicated, EmployeeOwned, CorporateShared). | [optional] 
**tags** | **list[str]** | Tags associated with the token. | [optional] 
**user_info** | [**EnrollmentUserInfoV1Model**](EnrollmentUserInfoV1Model.md) | Enrollment user information. | [optional] 
**message_type** | **int** | Message Type like Email or SMS. | [optional] 
**send_to** | **str** | Email/Phone number where the message template will be sent. | [optional] 
**dep_token** | **str** | DEP enrollment token. | [optional] 
**profile_name** | **str** | DEP profile name. | [optional] 
**profile_status** | **int** | DEP profile status | [optional] 
**profile_user_name** | **str** | User name associated with the profile. | [optional] 
**auto_enrollment_sync_status** | **int** | Sync status for auto enrollment mode. | [optional] 
**qr_code_image_uri** | **str** | Data URI for the QR CODE image. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


