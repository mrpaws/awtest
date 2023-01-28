# DeviceApplicationInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | Gets or sets the name of application. | [optional] 
**version** | **str** | Gets or sets application version. | [optional] 
**build_version** | **str** | Gets or sets application build version. | [optional] 
**status** | **int** | Gets or sets status of the application, installation status [Pending Install, Installed, Pending Removal, Removed, Unknown]. | [optional] 
**device_id** | [**EntityReference_**](EntityReference_.md) | Gets or sets link to the Device where the Application belongs to. | [optional] 
**size** | **str** | Gets or sets represents the size of Application in Bytes. | [optional] 
**application_identifier** | **str** | Gets or sets identifier of the application i.e. Bundle Id or Package Id. | [optional] 
**type** | **str** | Gets or sets application type... for e.g. System/Internal/Public etc. | [optional] 
**is_managed** | **bool** | Gets or sets a value indicating whether this instance is managed. | [optional] 
**app_version** | **str** | Gets or sets application version. | [optional] 
**app_store_vendable** | **bool** | Gets or sets indicates whether the app came from the store and can participate in store features. Available in iOS 11.3 and later. | [optional] 
**device_based_vpp** | **bool** | Gets or sets indicates whether the app is distributed to the device without requiring an Apple ID. Available in iOS 11.3 and later. | [optional] 
**beta_app** | **bool** | Gets or sets indicates whether the app is part of the Beta program. Available in iOS 11.3 and later. | [optional] 
**ad_hoc_code_signed** | **bool** | Gets or sets indicates whether the app is ad-hoc code signed. Available in iOS 11.3 and later. | [optional] 
**has_update_available** | **bool** | Gets or sets indicates whether the app has an update available. Available in iOS 11.3 and later and in macOS 10.13.4 and later. | [optional] 
**id** | [**EntityId_**](EntityId_.md) |  | [optional] 
**uuid** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


