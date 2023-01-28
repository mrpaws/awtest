# DeviceBranchCacheStatisticsModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uuid** | **str** | The device UUID of the device to be queried. | [optional] 
**download_sources** | **str** | The download sources that was used for an application download for that device. | [optional] 
**branchcache_enabled** | **str** | If BranchCache was leveraged for the application download for that device. | [optional] 
**client_mode** | **str** | The configured BranchCache mode for the device. | [optional] 
**hosted_servers** | **list[str]** | The list of hosted server names if the device is configured in Hosted mode. | [optional] 
**cache_bytes** | **int** | The number of bytes from the cache/peers for the application download for that device. | [optional] 
**server_bytes** | **int** | The number of bytes from the server for the application download for that device. | [optional] 
**application_uuid** | **str** | The application UUID. | [optional] 
**application_size** | **int** | The application size in bytes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


