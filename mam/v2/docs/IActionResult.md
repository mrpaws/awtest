# IActionResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_query** | [**IRequestQuery**](IRequestQuery.md) | Gets or sets the RequestQuery. | [optional] 
**request_message** | **object** | Gets or sets the RequestMessage. | [optional] 
**http_status_code** | **int** | Gets or sets HttpStatusCode. | [optional] 
**retry_after** | **str** | Gets or sets retry-after value. | [optional] 
**model** | **object** | Gets or sets Model. | [optional] 
**stream** | [**Stream**](Stream.md) | Gets or sets Stream. | [optional] 
**partial_content_range** | [**RangeHeaderValue**](RangeHeaderValue.md) | Gets or sets partial content range. | [optional] 
**byte_array** | **str** | Gets or sets ByteArray. | [optional] 
**file_name** | **str** | Gets or sets FileName {Will be set in the content-disposition header}. | [optional] 
**media_type** | **str** | Gets or sets MediaType. | [optional] 
**on_stream_available** | [**Action3**](Action3.md) | Gets or sets OnStreamAvailable. | [optional] 
**e_tag_header_value** | [**EntityTagHeaderValue**](EntityTagHeaderValue.md) | Gets or sets ETagHeaderValue. | [optional] 
**accepts_byte_ranges** | **bool** | Gets or sets a value indicating whether gets or sets a value which indicates whether a range byte request for a stream is accepted or not. | [optional] 
**send_e_tag_header_value** | **bool** | Gets or sets a value indicating whether gets or sets the option to include ETagHeaderValue. | [optional] 
**location_header_value** | **str** | Gets or sets LocationHeaderValue. | [optional] 
**cache_control_value** | [**CacheControlHeaderValue**](CacheControlHeaderValue.md) | Gets or sets CacheControlValue. | [optional] 
**content_length** | **int** | Gets or sets ContentLength. | [optional] 
**response_date_time_format** | **str** | Gets or sets dateTime format for response. | [optional] 
**http_response_message** | **object** | Gets or sets HttpResponseMessage. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


