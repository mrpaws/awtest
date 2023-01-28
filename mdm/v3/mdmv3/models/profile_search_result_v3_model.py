# coding: utf-8

"""
    MDM API V3

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv3.configuration import Configuration


class ProfileSearchResultV3Model(object):
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
        'uuid': 'str',
        'name': 'str',
        'status': 'str',
        'assignment_type': 'str',
        'managed_by': 'str',
        'organization_group_uuid': 'str',
        'platform': 'str',
        'configuration_type': 'str',
        'context': 'str',
        'assigned_smart_groups': 'list[ProfileSmartGroupV3Model]',
        'excluded_smart_groups': 'list[ProfileSmartGroupV3Model]',
        'configured_payload': 'list[ProfilePayloadV3Model]',
        'created_by_resource_profile': 'bool'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'status': 'status',
        'assignment_type': 'assignment_type',
        'managed_by': 'managed_by',
        'organization_group_uuid': 'organization_group_uuid',
        'platform': 'platform',
        'configuration_type': 'configuration_type',
        'context': 'context',
        'assigned_smart_groups': 'assigned_smart_groups',
        'excluded_smart_groups': 'excluded_smart_groups',
        'configured_payload': 'configured_payload',
        'created_by_resource_profile': 'created_by_resource_profile'
    }

    def __init__(self, uuid=None, name=None, status=None, assignment_type=None, managed_by=None, organization_group_uuid=None, platform=None, configuration_type=None, context=None, assigned_smart_groups=None, excluded_smart_groups=None, configured_payload=None, created_by_resource_profile=None, _configuration=None):  # noqa: E501
        """ProfileSearchResultV3Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._uuid = None
        self._name = None
        self._status = None
        self._assignment_type = None
        self._managed_by = None
        self._organization_group_uuid = None
        self._platform = None
        self._configuration_type = None
        self._context = None
        self._assigned_smart_groups = None
        self._excluded_smart_groups = None
        self._configured_payload = None
        self._created_by_resource_profile = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if assignment_type is not None:
            self.assignment_type = assignment_type
        if managed_by is not None:
            self.managed_by = managed_by
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if platform is not None:
            self.platform = platform
        if configuration_type is not None:
            self.configuration_type = configuration_type
        if context is not None:
            self.context = context
        if assigned_smart_groups is not None:
            self.assigned_smart_groups = assigned_smart_groups
        if excluded_smart_groups is not None:
            self.excluded_smart_groups = excluded_smart_groups
        if configured_payload is not None:
            self.configured_payload = configured_payload
        if created_by_resource_profile is not None:
            self.created_by_resource_profile = created_by_resource_profile

    @property
    def uuid(self):
        """Gets the uuid of this ProfileSearchResultV3Model.  # noqa: E501

        Profile uuid.  # noqa: E501

        :return: The uuid of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ProfileSearchResultV3Model.

        Profile uuid.  # noqa: E501

        :param uuid: The uuid of this ProfileSearchResultV3Model.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this ProfileSearchResultV3Model.  # noqa: E501

        Profile name.  # noqa: E501

        :return: The name of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProfileSearchResultV3Model.

        Profile name.  # noqa: E501

        :param name: The name of this ProfileSearchResultV3Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this ProfileSearchResultV3Model.  # noqa: E501

        Profile status.  # noqa: E501

        :return: The status of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProfileSearchResultV3Model.

        Profile status.  # noqa: E501

        :param status: The status of this ProfileSearchResultV3Model.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def assignment_type(self):
        """Gets the assignment_type of this ProfileSearchResultV3Model.  # noqa: E501

        Profile Assignment type.  # noqa: E501

        :return: The assignment_type of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: str
        """
        return self._assignment_type

    @assignment_type.setter
    def assignment_type(self, assignment_type):
        """Sets the assignment_type of this ProfileSearchResultV3Model.

        Profile Assignment type.  # noqa: E501

        :param assignment_type: The assignment_type of this ProfileSearchResultV3Model.  # noqa: E501
        :type: str
        """

        self._assignment_type = assignment_type

    @property
    def managed_by(self):
        """Gets the managed_by of this ProfileSearchResultV3Model.  # noqa: E501

        Managed by organization group name.  # noqa: E501

        :return: The managed_by of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: str
        """
        return self._managed_by

    @managed_by.setter
    def managed_by(self, managed_by):
        """Sets the managed_by of this ProfileSearchResultV3Model.

        Managed by organization group name.  # noqa: E501

        :param managed_by: The managed_by of this ProfileSearchResultV3Model.  # noqa: E501
        :type: str
        """

        self._managed_by = managed_by

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this ProfileSearchResultV3Model.  # noqa: E501

        Profile organization group uuid  # noqa: E501

        :return: The organization_group_uuid of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this ProfileSearchResultV3Model.

        Profile organization group uuid  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this ProfileSearchResultV3Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def platform(self):
        """Gets the platform of this ProfileSearchResultV3Model.  # noqa: E501

        Profile platform.  # noqa: E501

        :return: The platform of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ProfileSearchResultV3Model.

        Profile platform.  # noqa: E501

        :param platform: The platform of this ProfileSearchResultV3Model.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def configuration_type(self):
        """Gets the configuration_type of this ProfileSearchResultV3Model.  # noqa: E501

        Profile configuration type.  # noqa: E501

        :return: The configuration_type of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: str
        """
        return self._configuration_type

    @configuration_type.setter
    def configuration_type(self, configuration_type):
        """Sets the configuration_type of this ProfileSearchResultV3Model.

        Profile configuration type.  # noqa: E501

        :param configuration_type: The configuration_type of this ProfileSearchResultV3Model.  # noqa: E501
        :type: str
        """

        self._configuration_type = configuration_type

    @property
    def context(self):
        """Gets the context of this ProfileSearchResultV3Model.  # noqa: E501

        Profile context.  # noqa: E501

        :return: The context of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ProfileSearchResultV3Model.

        Profile context.  # noqa: E501

        :param context: The context of this ProfileSearchResultV3Model.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def assigned_smart_groups(self):
        """Gets the assigned_smart_groups of this ProfileSearchResultV3Model.  # noqa: E501

        Assigned smart group.  # noqa: E501

        :return: The assigned_smart_groups of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: list[ProfileSmartGroupV3Model]
        """
        return self._assigned_smart_groups

    @assigned_smart_groups.setter
    def assigned_smart_groups(self, assigned_smart_groups):
        """Sets the assigned_smart_groups of this ProfileSearchResultV3Model.

        Assigned smart group.  # noqa: E501

        :param assigned_smart_groups: The assigned_smart_groups of this ProfileSearchResultV3Model.  # noqa: E501
        :type: list[ProfileSmartGroupV3Model]
        """

        self._assigned_smart_groups = assigned_smart_groups

    @property
    def excluded_smart_groups(self):
        """Gets the excluded_smart_groups of this ProfileSearchResultV3Model.  # noqa: E501

        Excluded smart group.  # noqa: E501

        :return: The excluded_smart_groups of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: list[ProfileSmartGroupV3Model]
        """
        return self._excluded_smart_groups

    @excluded_smart_groups.setter
    def excluded_smart_groups(self, excluded_smart_groups):
        """Sets the excluded_smart_groups of this ProfileSearchResultV3Model.

        Excluded smart group.  # noqa: E501

        :param excluded_smart_groups: The excluded_smart_groups of this ProfileSearchResultV3Model.  # noqa: E501
        :type: list[ProfileSmartGroupV3Model]
        """

        self._excluded_smart_groups = excluded_smart_groups

    @property
    def configured_payload(self):
        """Gets the configured_payload of this ProfileSearchResultV3Model.  # noqa: E501

        List of payloads configured for a profile.  # noqa: E501

        :return: The configured_payload of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: list[ProfilePayloadV3Model]
        """
        return self._configured_payload

    @configured_payload.setter
    def configured_payload(self, configured_payload):
        """Sets the configured_payload of this ProfileSearchResultV3Model.

        List of payloads configured for a profile.  # noqa: E501

        :param configured_payload: The configured_payload of this ProfileSearchResultV3Model.  # noqa: E501
        :type: list[ProfilePayloadV3Model]
        """

        self._configured_payload = configured_payload

    @property
    def created_by_resource_profile(self):
        """Gets the created_by_resource_profile of this ProfileSearchResultV3Model.  # noqa: E501

        Flag to indicate whether the device profile created during resource profile creation or not.  # noqa: E501

        :return: The created_by_resource_profile of this ProfileSearchResultV3Model.  # noqa: E501
        :rtype: bool
        """
        return self._created_by_resource_profile

    @created_by_resource_profile.setter
    def created_by_resource_profile(self, created_by_resource_profile):
        """Sets the created_by_resource_profile of this ProfileSearchResultV3Model.

        Flag to indicate whether the device profile created during resource profile creation or not.  # noqa: E501

        :param created_by_resource_profile: The created_by_resource_profile of this ProfileSearchResultV3Model.  # noqa: E501
        :type: bool
        """

        self._created_by_resource_profile = created_by_resource_profile

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
        if issubclass(ProfileSearchResultV3Model, dict):
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
        if not isinstance(other, ProfileSearchResultV3Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProfileSearchResultV3Model):
            return True

        return self.to_dict() != other.to_dict()