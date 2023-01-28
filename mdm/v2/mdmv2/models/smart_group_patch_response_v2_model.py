# coding: utf-8

"""
    MDM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv2.configuration import Configuration


class SmartGroupPatchResponseV2Model(object):
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
        'name': 'str',
        'managed_by': 'str',
        'organization_groups': 'list[str]',
        'ownerships': 'list[str]',
        'platforms': 'list[str]',
        'tags': 'list[int]',
        'user_groups': 'list[str]',
        'users': 'list[str]',
        'devices': 'list[str]',
        'management_types': 'list[str]',
        'enrollment_categories': 'list[str]',
        'oem_and_models': 'list[OEMAndModels]',
        'cpu_architectures': 'list[str]',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'managed_by': 'managedBy',
        'organization_groups': 'organizationGroups',
        'ownerships': 'ownerships',
        'platforms': 'platforms',
        'tags': 'tags',
        'user_groups': 'userGroups',
        'users': 'users',
        'devices': 'devices',
        'management_types': 'managementTypes',
        'enrollment_categories': 'enrollmentCategories',
        'oem_and_models': 'OEMAndModels',
        'cpu_architectures': 'cpuArchitectures',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, name=None, managed_by=None, organization_groups=None, ownerships=None, platforms=None, tags=None, user_groups=None, users=None, devices=None, management_types=None, enrollment_categories=None, oem_and_models=None, cpu_architectures=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """SmartGroupPatchResponseV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._managed_by = None
        self._organization_groups = None
        self._ownerships = None
        self._platforms = None
        self._tags = None
        self._user_groups = None
        self._users = None
        self._devices = None
        self._management_types = None
        self._enrollment_categories = None
        self._oem_and_models = None
        self._cpu_architectures = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if managed_by is not None:
            self.managed_by = managed_by
        if organization_groups is not None:
            self.organization_groups = organization_groups
        if ownerships is not None:
            self.ownerships = ownerships
        if platforms is not None:
            self.platforms = platforms
        if tags is not None:
            self.tags = tags
        if user_groups is not None:
            self.user_groups = user_groups
        if users is not None:
            self.users = users
        if devices is not None:
            self.devices = devices
        if management_types is not None:
            self.management_types = management_types
        if enrollment_categories is not None:
            self.enrollment_categories = enrollment_categories
        if oem_and_models is not None:
            self.oem_and_models = oem_and_models
        if cpu_architectures is not None:
            self.cpu_architectures = cpu_architectures
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def name(self):
        """Gets the name of this SmartGroupPatchResponseV2Model.  # noqa: E501

        Name of Smart Group  # noqa: E501

        :return: The name of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SmartGroupPatchResponseV2Model.

        Name of Smart Group  # noqa: E501

        :param name: The name of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def managed_by(self):
        """Gets the managed_by of this SmartGroupPatchResponseV2Model.  # noqa: E501

        Organization group name at which smart group is managed  # noqa: E501

        :return: The managed_by of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: str
        """
        return self._managed_by

    @managed_by.setter
    def managed_by(self, managed_by):
        """Sets the managed_by of this SmartGroupPatchResponseV2Model.

        Organization group name at which smart group is managed  # noqa: E501

        :param managed_by: The managed_by of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: str
        """

        self._managed_by = managed_by

    @property
    def organization_groups(self):
        """Gets the organization_groups of this SmartGroupPatchResponseV2Model.  # noqa: E501

        List of organization groups added in Smart groups rule  # noqa: E501

        :return: The organization_groups of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._organization_groups

    @organization_groups.setter
    def organization_groups(self, organization_groups):
        """Sets the organization_groups of this SmartGroupPatchResponseV2Model.

        List of organization groups added in Smart groups rule  # noqa: E501

        :param organization_groups: The organization_groups of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: list[str]
        """

        self._organization_groups = organization_groups

    @property
    def ownerships(self):
        """Gets the ownerships of this SmartGroupPatchResponseV2Model.  # noqa: E501

        List of device ownerships added in Smart groups rule  # noqa: E501

        :return: The ownerships of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._ownerships

    @ownerships.setter
    def ownerships(self, ownerships):
        """Sets the ownerships of this SmartGroupPatchResponseV2Model.

        List of device ownerships added in Smart groups rule  # noqa: E501

        :param ownerships: The ownerships of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: list[str]
        """

        self._ownerships = ownerships

    @property
    def platforms(self):
        """Gets the platforms of this SmartGroupPatchResponseV2Model.  # noqa: E501

        List of platforms added in Smart groups rule  # noqa: E501

        :return: The platforms of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._platforms

    @platforms.setter
    def platforms(self, platforms):
        """Sets the platforms of this SmartGroupPatchResponseV2Model.

        List of platforms added in Smart groups rule  # noqa: E501

        :param platforms: The platforms of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: list[str]
        """

        self._platforms = platforms

    @property
    def tags(self):
        """Gets the tags of this SmartGroupPatchResponseV2Model.  # noqa: E501

        List of tags added in Smart groups rule  # noqa: E501

        :return: The tags of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: list[int]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SmartGroupPatchResponseV2Model.

        List of tags added in Smart groups rule  # noqa: E501

        :param tags: The tags of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: list[int]
        """

        self._tags = tags

    @property
    def user_groups(self):
        """Gets the user_groups of this SmartGroupPatchResponseV2Model.  # noqa: E501

        List of user groups added in Smart groups rule  # noqa: E501

        :return: The user_groups of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this SmartGroupPatchResponseV2Model.

        List of user groups added in Smart groups rule  # noqa: E501

        :param user_groups: The user_groups of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: list[str]
        """

        self._user_groups = user_groups

    @property
    def users(self):
        """Gets the users of this SmartGroupPatchResponseV2Model.  # noqa: E501

        List of users added in Smart groups rule  # noqa: E501

        :return: The users of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this SmartGroupPatchResponseV2Model.

        List of users added in Smart groups rule  # noqa: E501

        :param users: The users of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def devices(self):
        """Gets the devices of this SmartGroupPatchResponseV2Model.  # noqa: E501

        List of devices added in Smart groups rule  # noqa: E501

        :return: The devices of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this SmartGroupPatchResponseV2Model.

        List of devices added in Smart groups rule  # noqa: E501

        :param devices: The devices of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: list[str]
        """

        self._devices = devices

    @property
    def management_types(self):
        """Gets the management_types of this SmartGroupPatchResponseV2Model.  # noqa: E501

        List of device management type added in Smart groups rule  # noqa: E501

        :return: The management_types of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._management_types

    @management_types.setter
    def management_types(self, management_types):
        """Sets the management_types of this SmartGroupPatchResponseV2Model.

        List of device management type added in Smart groups rule  # noqa: E501

        :param management_types: The management_types of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: list[str]
        """

        self._management_types = management_types

    @property
    def enrollment_categories(self):
        """Gets the enrollment_categories of this SmartGroupPatchResponseV2Model.  # noqa: E501

        List of device enrollment category added in Smart groups rule  # noqa: E501

        :return: The enrollment_categories of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._enrollment_categories

    @enrollment_categories.setter
    def enrollment_categories(self, enrollment_categories):
        """Sets the enrollment_categories of this SmartGroupPatchResponseV2Model.

        List of device enrollment category added in Smart groups rule  # noqa: E501

        :param enrollment_categories: The enrollment_categories of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: list[str]
        """

        self._enrollment_categories = enrollment_categories

    @property
    def oem_and_models(self):
        """Gets the oem_and_models of this SmartGroupPatchResponseV2Model.  # noqa: E501

        Contains list of device OEM and model criteria for smart group  # noqa: E501

        :return: The oem_and_models of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: list[OEMAndModels]
        """
        return self._oem_and_models

    @oem_and_models.setter
    def oem_and_models(self, oem_and_models):
        """Sets the oem_and_models of this SmartGroupPatchResponseV2Model.

        Contains list of device OEM and model criteria for smart group  # noqa: E501

        :param oem_and_models: The oem_and_models of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: list[OEMAndModels]
        """

        self._oem_and_models = oem_and_models

    @property
    def cpu_architectures(self):
        """Gets the cpu_architectures of this SmartGroupPatchResponseV2Model.  # noqa: E501

        Contains list of device CPU Architecture criteria for smart group  # noqa: E501

        :return: The cpu_architectures of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._cpu_architectures

    @cpu_architectures.setter
    def cpu_architectures(self, cpu_architectures):
        """Sets the cpu_architectures of this SmartGroupPatchResponseV2Model.

        Contains list of device CPU Architecture criteria for smart group  # noqa: E501

        :param cpu_architectures: The cpu_architectures of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: list[str]
        """

        self._cpu_architectures = cpu_architectures

    @property
    def id(self):
        """Gets the id of this SmartGroupPatchResponseV2Model.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmartGroupPatchResponseV2Model.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this SmartGroupPatchResponseV2Model.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this SmartGroupPatchResponseV2Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this SmartGroupPatchResponseV2Model.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this SmartGroupPatchResponseV2Model.  # noqa: E501
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
        if issubclass(SmartGroupPatchResponseV2Model, dict):
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
        if not isinstance(other, SmartGroupPatchResponseV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartGroupPatchResponseV2Model):
            return True

        return self.to_dict() != other.to_dict()
