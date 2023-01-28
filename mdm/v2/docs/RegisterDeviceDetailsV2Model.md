# RegisterDeviceDetailsV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **str** | Enrollment user identifier | 
**friendly_name** | **str** | Device friendly name | 
**ownership_type** | **str** | Device ownership type | [optional] 
**platform_id** | **int** | Device platform identifier | [optional] 
**model_id** | **int** | Device model identifier | [optional] 
**operating_system_id** | **int** | Device operating system identifier | [optional] 
**device_udid** | **str** | UDID of the device | [optional] 
**serial_number** | **str** | Device serial number | [optional] 
**imei** | **str** | Device imei number | [optional] 
**asset_number** | **str** | Device asset number | [optional] 
**message_template_id** | **int** | Message template identifier | [optional] 
**sim** | **str** | SIM details | [optional] 
**to_email_address** | **str** | User&#39;s email address | [optional] 
**to_phone_number** | **str** | User&#39;s phone number | [optional] 
**is_migration** | **bool** | Value indicating whether this instance is migration | [optional] 
**message_type** | **int** | The message type for device enrollment as NONE, EMAIL, SMS, QRCODE | [optional] 
**tags** | [**list[TagV2Model]**](TagV2Model.md) | Tags for the device | [optional] 
**custom_attributes** | [**list[CustomAttributeNameValueApplicationV2Model]**](CustomAttributeNameValueApplicationV2Model.md) | Custom attributes for the device | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


