# PurchasedAppDeploymentModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_type** | **str** | Gets or sets assignment Type, Auto or OnDemand. | [optional] 
**remove_on_unenroll** | **bool** | Gets or sets a value indicating whether whether remove the app once device is un-enrolled. | [optional] 
**prevent_application_backup** | **bool** | Gets or sets a value indicating whether whether prevent the application back up. | [optional] 
**allow_management** | **bool** | Gets or sets a value indicating whether true if admin chooses to assume management of user installed apps. | [optional] 
**use_vpn** | **bool** | Gets or sets a value indicating whether whether use VPN for the application. If true, needs to provide the VPNProfileId. | [optional] 
**vpn_profile_id** | **int** | Gets or sets a value indicating the ID for the VPN profile associated with the application, required if UseVPN is true. | [optional] 
**id** | **int** | Gets or sets identifier. | [optional] 
**uuid** | **str** | Gets or sets current objects UUID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


