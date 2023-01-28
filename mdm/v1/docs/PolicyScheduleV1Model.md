# PolicyScheduleV1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_mode** | **int** | The install mode for the update. | [optional] 
**device_time_zone_offset** | **int** | The UTC offset of the device&#39;s time zone. | [optional] 
**duration** | **int** | The duration for which the update is valid. | [optional] 
**start_time** | **str** | The start time for the update. | [optional] 
**end_time** | **str** | The end time for the update. | [optional] 
**auto_update_delay** | **int** | The auto update delay in days (must be in range 1-10). | [optional] 
**allow_user_to_postpone** | **bool** | Indicates whether user is allowed to postpone the update or not. | [optional] 
**postpone_duration** | **int** | The postpone duration in hours (must be in range 1-24), to be considered only when allow_user_to_postpone is true. | [optional] 
**postpone_message** | **str** | The postpone message, to be considered only when allow_user_to_postpone is true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


