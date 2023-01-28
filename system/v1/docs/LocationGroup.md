# LocationGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the location group name. | [optional] 
**group_id** | **str** | Gets or sets the location group&#39;s tenant code. | [optional] 
**location_group_type** | **str** | Gets or sets location group type like Business segment, Customer etc... | [optional] 
**country** | **str** | Gets or sets country name like United States, India etc. | [optional] 
**locale** | **str** | Gets or sets locale information for Location Group like. | [optional] 
**parent_location_group** | [**EntityReference_**](EntityReference_.md) | Gets or sets the parent location group. | [optional] 
**add_default_location** | **str** | Gets or sets this tells whether default location to be created while creating Location Group. | [optional] 
**created_on** | **str** | Gets or sets date and time when Location group was created. | [optional] 
**lg_level** | **int** | Gets or sets location Group Hierarchy level, like 0[Operating Location group], 1[immediate children],2 etc... This value is valid when retrieving children for location group. | [optional] 
**users** | **str** | Gets or sets this contains total number of Enrollment users in this Location Group. | [optional] 
**admins** | **str** | Gets or sets this contains total number of Admin users in this Location Group. | [optional] 
**devices** | **str** | Gets or sets this contains total nummber of devices in this Location group. | [optional] 
**id** | [**EntityId_**](EntityId_.md) |  | [optional] 
**uuid** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


