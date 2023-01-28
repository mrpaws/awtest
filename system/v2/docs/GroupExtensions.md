# GroupExtensions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **int** | Name of the domain. | [optional] 
**group_type** | **int** | Type of group. | [optional] 
**external_type** | **str** | Type of directory group. | [optional] 
**create_group_at_organization_group** | **str** | The organization group uuid where the group needs to be created. | [optional] 
**organization_group_assignment** | **str** | This assignment takes effect only when &#39;Automatically Select Based on User Group&#39; is selected as the Group ID   Assignment Mode in All Settings &amp;gt; Devices &amp;gt; Users &amp;gt; General &amp;gt; Enrollment &amp;gt; Grouping | [optional] 
**managed_by_organization_group** | **str** | Managed by organization. | [optional] 
**distinguished_name** | **str** | Distinguished name of the group as found in directory service. This attribute is not required if externalType is CustomQuery. | [optional] 
**base_dn** | **str** | The point from which a server will search for groups. | [optional] 
**directory_domain** | **str** | Directory domain where the group search needs to be done. | [optional] 
**custom_logic** | **str** | Additional query used to search for directory entity. This attribute MUST only be passed when directoryGroupType is set to CustomQuery. | [optional] 
**auto_sync** | **bool** | If enabled, the scheduler will automatically sync with LDAP and collect all group changes. If not passed, will apply internally configured value. | [optional] 
**auto_merge** | **bool** | If enabled, the scheduler will automatically merge changes into Workspace One UEM. If not passed, will apply internally configured value. | [optional] 
**maximum_allowable_changes** | **int** | The scheduler needs Admin approval if the changes exceed this amount. This attribute MUST be passed only if AutoMerge enabled.   If not passed, will apply internally configured value. The value should be between 1 and 99999. | [optional] 
**add_group_members_automatically** | **bool** | If enabled, will add missing users automatically to the group. If not passed, will apply internally configured value. | [optional] 
**send_email_to_users_when_adding_missing_users** | **bool** | If enabled, will send emails to users while adding missing users automatically to the group.   This attribute MUST be sent only if addGroupMembersAutomatically is enabled. If not passed, will apply internally configured value. | [optional] 
**message_template_name** | **str** | The name of the message template that would be used to send emails to users while adding missing users automatically to the group.   This attribute MUST be sent only if sendEmailToUsersWhenAddingMissingUsers is enabled. | [optional] 
**allow_all_administrators_to_manage_this_user_group** | **bool** | If enabled, will allow all administrators to manage this user group. If not passed, will apply internally configured value. | [optional] 
**default_enrollment_role_name** | **str** | The name of the default role to which the enrollment users of the group would have access to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


