# ExportStatusModelV1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | report export status | [optional] 
**status_reason** | **str** | Details status reason, this field has data only in case of failure else returns blank for non failure status | [optional] 
**report_uuid** | **str** | report uuid, it will be blank in case of all other status except complete | [optional] 
**href** | **str** | HyperLink to the exported report, it will be blank in case of all other status except complete | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


