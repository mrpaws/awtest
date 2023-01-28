# CreateGroupRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **list[str]** | Schemas of the group to be created. | [optional] 
**external_id** | **str** | An identifier for the resource as defined by the provisioning client.  The \&quot;externalId\&quot; may simplify identification of a   resource between the provisioning client and the service provider by allowing the client to use a filter to locate the   resource with an identifier from the provisioning domain, obviating the need to store a local mapping between the provisioning   domain&#39;s identifier of the resource and the identifier used by the service provider.  Each resource MAY include a non-empty \&quot;externalId\&quot; value. | [optional] 
**display_name** | **str** | Name of the group. | [optional] 
**urnscimschemasextensionworkspace1_0_group** | [**GroupExtensions**](GroupExtensions.md) | Extension to group schema. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


