# PurchasedApplicationV2Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Application&#39;s UUID. | [optional] 
**organization_group_uuid** | **str** | Application&#39;s organization group UUID. | [optional] 
**name** | **str** | Application&#39;s name. | [optional] 
**identifier** | **str** | Application&#39;s identifier. | [optional] 
**adam_id** | **str** | Application&#39;s iTunes Store Identifier. | [optional] 
**vpp_app_eligibility** | **int** | Type of licensing that the application is eligbile for. | [optional] 
**product_type** | **int** | Product type. | [optional] 
**categories** | **list[str]** | Application&#39;s categories. | [optional] 
**licenses_summary** | [**LicensesSummaryV2Model**](LicensesSummaryV2Model.md) | Licenses summary of the purchased application. | [optional] 
**assignments** | [**list[VppAssignmentV2Model]**](VppAssignmentV2Model.md) | Application&#39;s assignments. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


