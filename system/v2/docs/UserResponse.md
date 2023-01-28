# UserResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for a user | [optional] 
**external_id** | **str** | An identifier for the resource as defined by the provisioning client.    The \&quot;externalId\&quot; may simplify identification of a resource between the   provisioning client and the service provider by allowing the client to   use a filter to locate the resource with an identifier from the provisioning   domain, obviating the need to store a local mapping between the provisioning   domain&#39;s identifier of the resource and the identifier used by the service provider.  Each resource MAY include a non-empty \&quot;externalId\&quot; value. | [optional] 
**user_name** | **str** | Unique identifier for the user, used by the user to directly authenticate.   Often displayed to the user as their unique identifier within the system   (as opposed to \&quot;id\&quot; or \&quot;externalId\&quot;, which are generally opaque and not user-friendly   identifiers).  Each User MUST include a non-empty userName value.  This identifier MUST   be unique across entire set of Users.  This attribute is REQUIRED and is case insensitive. | 
**schemas** | **list[str]** | Schemas used to compose a user entity | 
**urnscimschemasextensionworkspace1_0_user** | [**UserExtensions**](UserExtensions.md) | Extension to user schema. | [optional] 
**groups** | [**list[GroupSummary]**](GroupSummary.md) | A list of groups to which the user belongs, either through direct membership, through   nested groups, or dynamically calculated. | [optional] 
**meta** | [**Metadata**](Metadata.md) | Resource metadata | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


