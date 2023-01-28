# coding: utf-8

"""
    MDM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv1.configuration import Configuration


class Profile(object):
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
        'profile_name': 'str',
        'organization_group_id': 'str',
        'profile_status': 'str',
        'platform': 'str',
        'profile_scope': 'str',
        'operating_system': 'str',
        'model': 'str',
        'ownership': 'str',
        'managed_by': 'str',
        'type': 'str',
        'assigned_organization_groups': 'ProfileAssignedOrganizationGroups_',
        'id': 'EntityId_',
        'uuid': 'str'
    }

    attribute_map = {
        'profile_name': 'ProfileName',
        'organization_group_id': 'OrganizationGroupId',
        'profile_status': 'ProfileStatus',
        'platform': 'Platform',
        'profile_scope': 'ProfileScope',
        'operating_system': 'OperatingSystem',
        'model': 'Model',
        'ownership': 'Ownership',
        'managed_by': 'ManagedBy',
        'type': 'Type',
        'assigned_organization_groups': 'AssignedOrganizationGroups',
        'id': 'Id',
        'uuid': 'Uuid'
    }

    def __init__(self, profile_name=None, organization_group_id=None, profile_status=None, platform=None, profile_scope=None, operating_system=None, model=None, ownership=None, managed_by=None, type=None, assigned_organization_groups=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """Profile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._profile_name = None
        self._organization_group_id = None
        self._profile_status = None
        self._platform = None
        self._profile_scope = None
        self._operating_system = None
        self._model = None
        self._ownership = None
        self._managed_by = None
        self._type = None
        self._assigned_organization_groups = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if profile_name is not None:
            self.profile_name = profile_name
        if organization_group_id is not None:
            self.organization_group_id = organization_group_id
        if profile_status is not None:
            self.profile_status = profile_status
        if platform is not None:
            self.platform = platform
        if profile_scope is not None:
            self.profile_scope = profile_scope
        if operating_system is not None:
            self.operating_system = operating_system
        if model is not None:
            self.model = model
        if ownership is not None:
            self.ownership = ownership
        if managed_by is not None:
            self.managed_by = managed_by
        if type is not None:
            self.type = type
        if assigned_organization_groups is not None:
            self.assigned_organization_groups = assigned_organization_groups
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def profile_name(self):
        """Gets the profile_name of this Profile.  # noqa: E501

        Gets or sets the name of the Profile.  # noqa: E501

        :return: The profile_name of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this Profile.

        Gets or sets the name of the Profile.  # noqa: E501

        :param profile_name: The profile_name of this Profile.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    @property
    def organization_group_id(self):
        """Gets the organization_group_id of this Profile.  # noqa: E501

        Gets or sets the profile's Organization Group.  # noqa: E501

        :return: The organization_group_id of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_id

    @organization_group_id.setter
    def organization_group_id(self, organization_group_id):
        """Sets the organization_group_id of this Profile.

        Gets or sets the profile's Organization Group.  # noqa: E501

        :param organization_group_id: The organization_group_id of this Profile.  # noqa: E501
        :type: str
        """

        self._organization_group_id = organization_group_id

    @property
    def profile_status(self):
        """Gets the profile_status of this Profile.  # noqa: E501

        Gets or sets the status of the Profile.  # noqa: E501

        :return: The profile_status of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._profile_status

    @profile_status.setter
    def profile_status(self, profile_status):
        """Sets the profile_status of this Profile.

        Gets or sets the status of the Profile.  # noqa: E501

        :param profile_status: The profile_status of this Profile.  # noqa: E501
        :type: str
        """

        self._profile_status = profile_status

    @property
    def platform(self):
        """Gets the platform of this Profile.  # noqa: E501

        Gets or sets the platform name.  # noqa: E501

        :return: The platform of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this Profile.

        Gets or sets the platform name.  # noqa: E501

        :param platform: The platform of this Profile.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def profile_scope(self):
        """Gets the profile_scope of this Profile.  # noqa: E501

        Gets or sets profileScope.  # noqa: E501

        :return: The profile_scope of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._profile_scope

    @profile_scope.setter
    def profile_scope(self, profile_scope):
        """Sets the profile_scope of this Profile.

        Gets or sets profileScope.  # noqa: E501

        :param profile_scope: The profile_scope of this Profile.  # noqa: E501
        :type: str
        """

        self._profile_scope = profile_scope

    @property
    def operating_system(self):
        """Gets the operating_system of this Profile.  # noqa: E501

        Gets or sets the Operating System.  # noqa: E501

        :return: The operating_system of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this Profile.

        Gets or sets the Operating System.  # noqa: E501

        :param operating_system: The operating_system of this Profile.  # noqa: E501
        :type: str
        """

        self._operating_system = operating_system

    @property
    def model(self):
        """Gets the model of this Profile.  # noqa: E501

        Gets or sets the device model.  # noqa: E501

        :return: The model of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Profile.

        Gets or sets the device model.  # noqa: E501

        :param model: The model of this Profile.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def ownership(self):
        """Gets the ownership of this Profile.  # noqa: E501

        Gets or sets the Ownership type.  # noqa: E501

        :return: The ownership of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        """Sets the ownership of this Profile.

        Gets or sets the Ownership type.  # noqa: E501

        :param ownership: The ownership of this Profile.  # noqa: E501
        :type: str
        """

        self._ownership = ownership

    @property
    def managed_by(self):
        """Gets the managed_by of this Profile.  # noqa: E501

        Gets or sets profile Managed by.  # noqa: E501

        :return: The managed_by of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._managed_by

    @managed_by.setter
    def managed_by(self, managed_by):
        """Sets the managed_by of this Profile.

        Gets or sets profile Managed by.  # noqa: E501

        :param managed_by: The managed_by of this Profile.  # noqa: E501
        :type: str
        """

        self._managed_by = managed_by

    @property
    def type(self):
        """Gets the type of this Profile.  # noqa: E501

        Gets or sets profile Type.  # noqa: E501

        :return: The type of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Profile.

        Gets or sets profile Type.  # noqa: E501

        :param type: The type of this Profile.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def assigned_organization_groups(self):
        """Gets the assigned_organization_groups of this Profile.  # noqa: E501

        Gets or sets profile Assigned LGs.  # noqa: E501

        :return: The assigned_organization_groups of this Profile.  # noqa: E501
        :rtype: ProfileAssignedOrganizationGroups_
        """
        return self._assigned_organization_groups

    @assigned_organization_groups.setter
    def assigned_organization_groups(self, assigned_organization_groups):
        """Sets the assigned_organization_groups of this Profile.

        Gets or sets profile Assigned LGs.  # noqa: E501

        :param assigned_organization_groups: The assigned_organization_groups of this Profile.  # noqa: E501
        :type: ProfileAssignedOrganizationGroups_
        """

        self._assigned_organization_groups = assigned_organization_groups

    @property
    def id(self):
        """Gets the id of this Profile.  # noqa: E501


        :return: The id of this Profile.  # noqa: E501
        :rtype: EntityId_
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Profile.


        :param id: The id of this Profile.  # noqa: E501
        :type: EntityId_
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this Profile.  # noqa: E501


        :return: The uuid of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Profile.


        :param uuid: The uuid of this Profile.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(Profile, dict):
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
        if not isinstance(other, Profile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Profile):
            return True

        return self.to_dict() != other.to_dict()
