# coding: utf-8

"""
    System API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv2.configuration import Configuration


class GroupExtensions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'domain': 'int',
        'group_type': 'int',
        'external_type': 'str',
        'create_group_at_organization_group': 'str',
        'organization_group_assignment': 'str',
        'managed_by_organization_group': 'str',
        'distinguished_name': 'str',
        'base_dn': 'str',
        'directory_domain': 'str',
        'custom_logic': 'str',
        'auto_sync': 'bool',
        'auto_merge': 'bool',
        'maximum_allowable_changes': 'int',
        'add_group_members_automatically': 'bool',
        'send_email_to_users_when_adding_missing_users': 'bool',
        'message_template_name': 'str',
        'allow_all_administrators_to_manage_this_user_group': 'bool',
        'default_enrollment_role_name': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'group_type': 'groupType',
        'external_type': 'externalType',
        'create_group_at_organization_group': 'createGroupAtOrganizationGroup',
        'organization_group_assignment': 'organizationGroupAssignment',
        'managed_by_organization_group': 'managedByOrganizationGroup',
        'distinguished_name': 'distinguishedName',
        'base_dn': 'baseDN',
        'directory_domain': 'directoryDomain',
        'custom_logic': 'customLogic',
        'auto_sync': 'autoSync',
        'auto_merge': 'autoMerge',
        'maximum_allowable_changes': 'maximumAllowableChanges',
        'add_group_members_automatically': 'addGroupMembersAutomatically',
        'send_email_to_users_when_adding_missing_users': 'sendEmailToUsersWhenAddingMissingUsers',
        'message_template_name': 'messageTemplateName',
        'allow_all_administrators_to_manage_this_user_group': 'allowAllAdministratorsToManageThisUserGroup',
        'default_enrollment_role_name': 'defaultEnrollmentRoleName'
    }

    def __init__(self, domain=None, group_type=None, external_type=None, create_group_at_organization_group=None, organization_group_assignment=None, managed_by_organization_group=None, distinguished_name=None, base_dn=None, directory_domain=None, custom_logic=None, auto_sync=None, auto_merge=None, maximum_allowable_changes=None, add_group_members_automatically=None, send_email_to_users_when_adding_missing_users=None, message_template_name=None, allow_all_administrators_to_manage_this_user_group=None, default_enrollment_role_name=None, _configuration=None):  # noqa: E501
        """GroupExtensions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain = None
        self._group_type = None
        self._external_type = None
        self._create_group_at_organization_group = None
        self._organization_group_assignment = None
        self._managed_by_organization_group = None
        self._distinguished_name = None
        self._base_dn = None
        self._directory_domain = None
        self._custom_logic = None
        self._auto_sync = None
        self._auto_merge = None
        self._maximum_allowable_changes = None
        self._add_group_members_automatically = None
        self._send_email_to_users_when_adding_missing_users = None
        self._message_template_name = None
        self._allow_all_administrators_to_manage_this_user_group = None
        self._default_enrollment_role_name = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if group_type is not None:
            self.group_type = group_type
        if external_type is not None:
            self.external_type = external_type
        if create_group_at_organization_group is not None:
            self.create_group_at_organization_group = create_group_at_organization_group
        if organization_group_assignment is not None:
            self.organization_group_assignment = organization_group_assignment
        if managed_by_organization_group is not None:
            self.managed_by_organization_group = managed_by_organization_group
        if distinguished_name is not None:
            self.distinguished_name = distinguished_name
        if base_dn is not None:
            self.base_dn = base_dn
        if directory_domain is not None:
            self.directory_domain = directory_domain
        if custom_logic is not None:
            self.custom_logic = custom_logic
        if auto_sync is not None:
            self.auto_sync = auto_sync
        if auto_merge is not None:
            self.auto_merge = auto_merge
        if maximum_allowable_changes is not None:
            self.maximum_allowable_changes = maximum_allowable_changes
        if add_group_members_automatically is not None:
            self.add_group_members_automatically = add_group_members_automatically
        if send_email_to_users_when_adding_missing_users is not None:
            self.send_email_to_users_when_adding_missing_users = send_email_to_users_when_adding_missing_users
        if message_template_name is not None:
            self.message_template_name = message_template_name
        if allow_all_administrators_to_manage_this_user_group is not None:
            self.allow_all_administrators_to_manage_this_user_group = allow_all_administrators_to_manage_this_user_group
        if default_enrollment_role_name is not None:
            self.default_enrollment_role_name = default_enrollment_role_name

    @property
    def domain(self):
        """Gets the domain of this GroupExtensions.  # noqa: E501

        Name of the domain.  # noqa: E501

        :return: The domain of this GroupExtensions.  # noqa: E501
        :rtype: int
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this GroupExtensions.

        Name of the domain.  # noqa: E501

        :param domain: The domain of this GroupExtensions.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if (self._configuration.client_side_validation and
                domain not in allowed_values):
            raise ValueError(
                "Invalid value for `domain` ({0}), must be one of {1}"  # noqa: E501
                .format(domain, allowed_values)
            )

        self._domain = domain

    @property
    def group_type(self):
        """Gets the group_type of this GroupExtensions.  # noqa: E501

        Type of group.  # noqa: E501

        :return: The group_type of this GroupExtensions.  # noqa: E501
        :rtype: int
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this GroupExtensions.

        Type of group.  # noqa: E501

        :param group_type: The group_type of this GroupExtensions.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if (self._configuration.client_side_validation and
                group_type not in allowed_values):
            raise ValueError(
                "Invalid value for `group_type` ({0}), must be one of {1}"  # noqa: E501
                .format(group_type, allowed_values)
            )

        self._group_type = group_type

    @property
    def external_type(self):
        """Gets the external_type of this GroupExtensions.  # noqa: E501

        Type of directory group.  # noqa: E501

        :return: The external_type of this GroupExtensions.  # noqa: E501
        :rtype: str
        """
        return self._external_type

    @external_type.setter
    def external_type(self, external_type):
        """Sets the external_type of this GroupExtensions.

        Type of directory group.  # noqa: E501

        :param external_type: The external_type of this GroupExtensions.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "GROUP", "ORGANIZATIONAL_UNIT", "CUSTOM_QUERY"]  # noqa: E501
        if (self._configuration.client_side_validation and
                external_type not in allowed_values):
            raise ValueError(
                "Invalid value for `external_type` ({0}), must be one of {1}"  # noqa: E501
                .format(external_type, allowed_values)
            )

        self._external_type = external_type

    @property
    def create_group_at_organization_group(self):
        """Gets the create_group_at_organization_group of this GroupExtensions.  # noqa: E501

        The organization group uuid where the group needs to be created.  # noqa: E501

        :return: The create_group_at_organization_group of this GroupExtensions.  # noqa: E501
        :rtype: str
        """
        return self._create_group_at_organization_group

    @create_group_at_organization_group.setter
    def create_group_at_organization_group(self, create_group_at_organization_group):
        """Sets the create_group_at_organization_group of this GroupExtensions.

        The organization group uuid where the group needs to be created.  # noqa: E501

        :param create_group_at_organization_group: The create_group_at_organization_group of this GroupExtensions.  # noqa: E501
        :type: str
        """

        self._create_group_at_organization_group = create_group_at_organization_group

    @property
    def organization_group_assignment(self):
        """Gets the organization_group_assignment of this GroupExtensions.  # noqa: E501

        This assignment takes effect only when 'Automatically Select Based on User Group' is selected as the Group ID   Assignment Mode in All Settings &gt; Devices &gt; Users &gt; General &gt; Enrollment &gt; Grouping  # noqa: E501

        :return: The organization_group_assignment of this GroupExtensions.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_assignment

    @organization_group_assignment.setter
    def organization_group_assignment(self, organization_group_assignment):
        """Sets the organization_group_assignment of this GroupExtensions.

        This assignment takes effect only when 'Automatically Select Based on User Group' is selected as the Group ID   Assignment Mode in All Settings &gt; Devices &gt; Users &gt; General &gt; Enrollment &gt; Grouping  # noqa: E501

        :param organization_group_assignment: The organization_group_assignment of this GroupExtensions.  # noqa: E501
        :type: str
        """

        self._organization_group_assignment = organization_group_assignment

    @property
    def managed_by_organization_group(self):
        """Gets the managed_by_organization_group of this GroupExtensions.  # noqa: E501

        Managed by organization.  # noqa: E501

        :return: The managed_by_organization_group of this GroupExtensions.  # noqa: E501
        :rtype: str
        """
        return self._managed_by_organization_group

    @managed_by_organization_group.setter
    def managed_by_organization_group(self, managed_by_organization_group):
        """Sets the managed_by_organization_group of this GroupExtensions.

        Managed by organization.  # noqa: E501

        :param managed_by_organization_group: The managed_by_organization_group of this GroupExtensions.  # noqa: E501
        :type: str
        """

        self._managed_by_organization_group = managed_by_organization_group

    @property
    def distinguished_name(self):
        """Gets the distinguished_name of this GroupExtensions.  # noqa: E501

        Distinguished name of the group as found in directory service. This attribute is not required if externalType is CustomQuery.  # noqa: E501

        :return: The distinguished_name of this GroupExtensions.  # noqa: E501
        :rtype: str
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """Sets the distinguished_name of this GroupExtensions.

        Distinguished name of the group as found in directory service. This attribute is not required if externalType is CustomQuery.  # noqa: E501

        :param distinguished_name: The distinguished_name of this GroupExtensions.  # noqa: E501
        :type: str
        """

        self._distinguished_name = distinguished_name

    @property
    def base_dn(self):
        """Gets the base_dn of this GroupExtensions.  # noqa: E501

        The point from which a server will search for groups.  # noqa: E501

        :return: The base_dn of this GroupExtensions.  # noqa: E501
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this GroupExtensions.

        The point from which a server will search for groups.  # noqa: E501

        :param base_dn: The base_dn of this GroupExtensions.  # noqa: E501
        :type: str
        """

        self._base_dn = base_dn

    @property
    def directory_domain(self):
        """Gets the directory_domain of this GroupExtensions.  # noqa: E501

        Directory domain where the group search needs to be done.  # noqa: E501

        :return: The directory_domain of this GroupExtensions.  # noqa: E501
        :rtype: str
        """
        return self._directory_domain

    @directory_domain.setter
    def directory_domain(self, directory_domain):
        """Sets the directory_domain of this GroupExtensions.

        Directory domain where the group search needs to be done.  # noqa: E501

        :param directory_domain: The directory_domain of this GroupExtensions.  # noqa: E501
        :type: str
        """

        self._directory_domain = directory_domain

    @property
    def custom_logic(self):
        """Gets the custom_logic of this GroupExtensions.  # noqa: E501

        Additional query used to search for directory entity. This attribute MUST only be passed when directoryGroupType is set to CustomQuery.  # noqa: E501

        :return: The custom_logic of this GroupExtensions.  # noqa: E501
        :rtype: str
        """
        return self._custom_logic

    @custom_logic.setter
    def custom_logic(self, custom_logic):
        """Sets the custom_logic of this GroupExtensions.

        Additional query used to search for directory entity. This attribute MUST only be passed when directoryGroupType is set to CustomQuery.  # noqa: E501

        :param custom_logic: The custom_logic of this GroupExtensions.  # noqa: E501
        :type: str
        """

        self._custom_logic = custom_logic

    @property
    def auto_sync(self):
        """Gets the auto_sync of this GroupExtensions.  # noqa: E501

        If enabled, the scheduler will automatically sync with LDAP and collect all group changes. If not passed, will apply internally configured value.  # noqa: E501

        :return: The auto_sync of this GroupExtensions.  # noqa: E501
        :rtype: bool
        """
        return self._auto_sync

    @auto_sync.setter
    def auto_sync(self, auto_sync):
        """Sets the auto_sync of this GroupExtensions.

        If enabled, the scheduler will automatically sync with LDAP and collect all group changes. If not passed, will apply internally configured value.  # noqa: E501

        :param auto_sync: The auto_sync of this GroupExtensions.  # noqa: E501
        :type: bool
        """

        self._auto_sync = auto_sync

    @property
    def auto_merge(self):
        """Gets the auto_merge of this GroupExtensions.  # noqa: E501

        If enabled, the scheduler will automatically merge changes into Workspace One UEM. If not passed, will apply internally configured value.  # noqa: E501

        :return: The auto_merge of this GroupExtensions.  # noqa: E501
        :rtype: bool
        """
        return self._auto_merge

    @auto_merge.setter
    def auto_merge(self, auto_merge):
        """Sets the auto_merge of this GroupExtensions.

        If enabled, the scheduler will automatically merge changes into Workspace One UEM. If not passed, will apply internally configured value.  # noqa: E501

        :param auto_merge: The auto_merge of this GroupExtensions.  # noqa: E501
        :type: bool
        """

        self._auto_merge = auto_merge

    @property
    def maximum_allowable_changes(self):
        """Gets the maximum_allowable_changes of this GroupExtensions.  # noqa: E501

        The scheduler needs Admin approval if the changes exceed this amount. This attribute MUST be passed only if AutoMerge enabled.   If not passed, will apply internally configured value. The value should be between 1 and 99999.  # noqa: E501

        :return: The maximum_allowable_changes of this GroupExtensions.  # noqa: E501
        :rtype: int
        """
        return self._maximum_allowable_changes

    @maximum_allowable_changes.setter
    def maximum_allowable_changes(self, maximum_allowable_changes):
        """Sets the maximum_allowable_changes of this GroupExtensions.

        The scheduler needs Admin approval if the changes exceed this amount. This attribute MUST be passed only if AutoMerge enabled.   If not passed, will apply internally configured value. The value should be between 1 and 99999.  # noqa: E501

        :param maximum_allowable_changes: The maximum_allowable_changes of this GroupExtensions.  # noqa: E501
        :type: int
        """

        self._maximum_allowable_changes = maximum_allowable_changes

    @property
    def add_group_members_automatically(self):
        """Gets the add_group_members_automatically of this GroupExtensions.  # noqa: E501

        If enabled, will add missing users automatically to the group. If not passed, will apply internally configured value.  # noqa: E501

        :return: The add_group_members_automatically of this GroupExtensions.  # noqa: E501
        :rtype: bool
        """
        return self._add_group_members_automatically

    @add_group_members_automatically.setter
    def add_group_members_automatically(self, add_group_members_automatically):
        """Sets the add_group_members_automatically of this GroupExtensions.

        If enabled, will add missing users automatically to the group. If not passed, will apply internally configured value.  # noqa: E501

        :param add_group_members_automatically: The add_group_members_automatically of this GroupExtensions.  # noqa: E501
        :type: bool
        """

        self._add_group_members_automatically = add_group_members_automatically

    @property
    def send_email_to_users_when_adding_missing_users(self):
        """Gets the send_email_to_users_when_adding_missing_users of this GroupExtensions.  # noqa: E501

        If enabled, will send emails to users while adding missing users automatically to the group.   This attribute MUST be sent only if addGroupMembersAutomatically is enabled. If not passed, will apply internally configured value.  # noqa: E501

        :return: The send_email_to_users_when_adding_missing_users of this GroupExtensions.  # noqa: E501
        :rtype: bool
        """
        return self._send_email_to_users_when_adding_missing_users

    @send_email_to_users_when_adding_missing_users.setter
    def send_email_to_users_when_adding_missing_users(self, send_email_to_users_when_adding_missing_users):
        """Sets the send_email_to_users_when_adding_missing_users of this GroupExtensions.

        If enabled, will send emails to users while adding missing users automatically to the group.   This attribute MUST be sent only if addGroupMembersAutomatically is enabled. If not passed, will apply internally configured value.  # noqa: E501

        :param send_email_to_users_when_adding_missing_users: The send_email_to_users_when_adding_missing_users of this GroupExtensions.  # noqa: E501
        :type: bool
        """

        self._send_email_to_users_when_adding_missing_users = send_email_to_users_when_adding_missing_users

    @property
    def message_template_name(self):
        """Gets the message_template_name of this GroupExtensions.  # noqa: E501

        The name of the message template that would be used to send emails to users while adding missing users automatically to the group.   This attribute MUST be sent only if sendEmailToUsersWhenAddingMissingUsers is enabled.  # noqa: E501

        :return: The message_template_name of this GroupExtensions.  # noqa: E501
        :rtype: str
        """
        return self._message_template_name

    @message_template_name.setter
    def message_template_name(self, message_template_name):
        """Sets the message_template_name of this GroupExtensions.

        The name of the message template that would be used to send emails to users while adding missing users automatically to the group.   This attribute MUST be sent only if sendEmailToUsersWhenAddingMissingUsers is enabled.  # noqa: E501

        :param message_template_name: The message_template_name of this GroupExtensions.  # noqa: E501
        :type: str
        """

        self._message_template_name = message_template_name

    @property
    def allow_all_administrators_to_manage_this_user_group(self):
        """Gets the allow_all_administrators_to_manage_this_user_group of this GroupExtensions.  # noqa: E501

        If enabled, will allow all administrators to manage this user group. If not passed, will apply internally configured value.  # noqa: E501

        :return: The allow_all_administrators_to_manage_this_user_group of this GroupExtensions.  # noqa: E501
        :rtype: bool
        """
        return self._allow_all_administrators_to_manage_this_user_group

    @allow_all_administrators_to_manage_this_user_group.setter
    def allow_all_administrators_to_manage_this_user_group(self, allow_all_administrators_to_manage_this_user_group):
        """Sets the allow_all_administrators_to_manage_this_user_group of this GroupExtensions.

        If enabled, will allow all administrators to manage this user group. If not passed, will apply internally configured value.  # noqa: E501

        :param allow_all_administrators_to_manage_this_user_group: The allow_all_administrators_to_manage_this_user_group of this GroupExtensions.  # noqa: E501
        :type: bool
        """

        self._allow_all_administrators_to_manage_this_user_group = allow_all_administrators_to_manage_this_user_group

    @property
    def default_enrollment_role_name(self):
        """Gets the default_enrollment_role_name of this GroupExtensions.  # noqa: E501

        The name of the default role to which the enrollment users of the group would have access to.  # noqa: E501

        :return: The default_enrollment_role_name of this GroupExtensions.  # noqa: E501
        :rtype: str
        """
        return self._default_enrollment_role_name

    @default_enrollment_role_name.setter
    def default_enrollment_role_name(self, default_enrollment_role_name):
        """Sets the default_enrollment_role_name of this GroupExtensions.

        The name of the default role to which the enrollment users of the group would have access to.  # noqa: E501

        :param default_enrollment_role_name: The default_enrollment_role_name of this GroupExtensions.  # noqa: E501
        :type: str
        """

        self._default_enrollment_role_name = default_enrollment_role_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GroupExtensions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GroupExtensions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupExtensions):
            return True

        return self.to_dict() != other.to_dict()
