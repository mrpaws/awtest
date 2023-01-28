# StageNowBarcodeV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staging_profile_id** | **int** | Staging Definition Id | 
**organization_group_uuid** | **str** | Organizational Group Uuid. | [optional] 
**organization_group_id** | **int** | Organizational Group Id. Needed only if OrganizationGroupUuid is not set. | [optional] 
**universal_barcode** | **bool** | Whether to use universal barcode | [optional] 
**device_owner_mode** | **bool** | Whether a Device Owner mode barcode is generated. Used only when generating an Universal barcode or in an &#39;Android for Work&#39; Organization group with enrollment restrictions set to &#39;Exempt smart groups from Android(Legacy)&#39; | [optional] 
**staging_relay_server_id** | **int** | Id of Relay Server that will contain the staging files | 
**wifi_profile_id** | **int** | Staging Profile used for WiFi while staging | [optional] 
**barcode_instructions** | **str** | Comment or instructions included on barcode page | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


