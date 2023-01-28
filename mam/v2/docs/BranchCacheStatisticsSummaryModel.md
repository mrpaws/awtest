# BranchCacheStatisticsSummaryModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_devices_branchcache_mode_enabled** | **int** | Total number of devices with BranchCache mode enabled i.e. BranchCache mode on device is distributed/local/hosted | [optional] 
**total_devices_utilized_branchcache** | **int** | Total number of devices that utilized BranchCache in the application deployments i.e. application bytes from cache/peers was greater than zero for those devices. | [optional] 
**total_devices_not_utilized_branchcache** | **int** | Total number of devices that did not utilize BranchCache in the application deployments i.e. application bytes from cache/peers was equal to zero for those devices. | [optional] 
**total_device_count** | **int** | Total number of devices that have the applications installed. | [optional] 
**total_cache_bytes** | **int** | Total number of bytes from the cache/peers for the application downloads for all devices. | [optional] 
**total_server_bytes** | **int** | Total number of bytes from the server for the application downloads for all devices. | [optional] 
**total_savings_percent** | **int** | The savings as a percentage that is the bytes downloaded from the cache/peers over total application sizes for the device(s). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


