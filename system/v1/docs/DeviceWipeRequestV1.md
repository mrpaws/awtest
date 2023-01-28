# DeviceWipeRequestV1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_text** | **str** | The search text string which the device wipe results will be filtered by. | [optional] 
**start_date** | **datetime** | The start of the date range which the results will be filtered by. | [optional] 
**end_date** | **datetime** | The end of the date range which the results will be filtered by. | [optional] 
**wipe_type** | **str** | The wipe action type which the results will be filtered by. Supported values are DEVICE_WIPE, ENTERPRISE_WIPE. | [optional] 
**wipe_status** | **str** | The status of the wipe action by which the results will be filtered. Supported values are APPROVED, HELD, QUEUED, ABORTED. | [optional] 
**wipe_source** | **str** | The source of the wipe source by which the results will be filtered. | [optional] 
**ownership** | **list[str]** | The device ownership types by which the results will be filtered. Supported values are UNKNOWN, CORPORATE_DEDICATED, EMPLOYEE_OWNED, CORPORATE_SHARED. | [optional] 
**sort_column** | **str** | The name of the column the results should be ordered by, default is DATE. | [optional] 
**sort_direction** | **str** | The sort order by direction. Default is ASC. | [optional] 
**export_format** | **str** | Report&#39;s export format. Default is XLSX. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


