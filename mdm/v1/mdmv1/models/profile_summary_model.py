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


class ProfileSummaryModel(object):
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
        'assigned_count': 'int',
        'installed_count': 'int',
        'not_installed_count': 'int',
        'cloud_profile': 'bool',
        'device_type': 'int',
        'last_profile_published_version': 'int',
        'active': 'bool',
        'profile_name': 'str',
        'device_profile_assignment_type': 'int'
    }

    attribute_map = {
        'assigned_count': 'assigned_count',
        'installed_count': 'installed_count',
        'not_installed_count': 'not_installed_count',
        'cloud_profile': 'cloud_profile',
        'device_type': 'device_type',
        'last_profile_published_version': 'last_profile_published_version',
        'active': 'active',
        'profile_name': 'profile_name',
        'device_profile_assignment_type': 'device_profile_assignment_type'
    }

    def __init__(self, assigned_count=None, installed_count=None, not_installed_count=None, cloud_profile=None, device_type=None, last_profile_published_version=None, active=None, profile_name=None, device_profile_assignment_type=None, _configuration=None):  # noqa: E501
        """ProfileSummaryModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assigned_count = None
        self._installed_count = None
        self._not_installed_count = None
        self._cloud_profile = None
        self._device_type = None
        self._last_profile_published_version = None
        self._active = None
        self._profile_name = None
        self._device_profile_assignment_type = None
        self.discriminator = None

        if assigned_count is not None:
            self.assigned_count = assigned_count
        if installed_count is not None:
            self.installed_count = installed_count
        if not_installed_count is not None:
            self.not_installed_count = not_installed_count
        if cloud_profile is not None:
            self.cloud_profile = cloud_profile
        if device_type is not None:
            self.device_type = device_type
        if last_profile_published_version is not None:
            self.last_profile_published_version = last_profile_published_version
        if active is not None:
            self.active = active
        if profile_name is not None:
            self.profile_name = profile_name
        if device_profile_assignment_type is not None:
            self.device_profile_assignment_type = device_profile_assignment_type

    @property
    def assigned_count(self):
        """Gets the assigned_count of this ProfileSummaryModel.  # noqa: E501

        The number of devices for which the profile is assigned.  # noqa: E501

        :return: The assigned_count of this ProfileSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._assigned_count

    @assigned_count.setter
    def assigned_count(self, assigned_count):
        """Sets the assigned_count of this ProfileSummaryModel.

        The number of devices for which the profile is assigned.  # noqa: E501

        :param assigned_count: The assigned_count of this ProfileSummaryModel.  # noqa: E501
        :type: int
        """

        self._assigned_count = assigned_count

    @property
    def installed_count(self):
        """Gets the installed_count of this ProfileSummaryModel.  # noqa: E501

        The number of devices for which the profile is assigned and installed.  # noqa: E501

        :return: The installed_count of this ProfileSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._installed_count

    @installed_count.setter
    def installed_count(self, installed_count):
        """Sets the installed_count of this ProfileSummaryModel.

        The number of devices for which the profile is assigned and installed.  # noqa: E501

        :param installed_count: The installed_count of this ProfileSummaryModel.  # noqa: E501
        :type: int
        """

        self._installed_count = installed_count

    @property
    def not_installed_count(self):
        """Gets the not_installed_count of this ProfileSummaryModel.  # noqa: E501

        The number of devices for which the profile is assigned but not installed.  # noqa: E501

        :return: The not_installed_count of this ProfileSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._not_installed_count

    @not_installed_count.setter
    def not_installed_count(self, not_installed_count):
        """Sets the not_installed_count of this ProfileSummaryModel.

        The number of devices for which the profile is assigned but not installed.  # noqa: E501

        :param not_installed_count: The not_installed_count of this ProfileSummaryModel.  # noqa: E501
        :type: int
        """

        self._not_installed_count = not_installed_count

    @property
    def cloud_profile(self):
        """Gets the cloud_profile of this ProfileSummaryModel.  # noqa: E501

        Indicates whether the profile is user profile.  # noqa: E501

        :return: The cloud_profile of this ProfileSummaryModel.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_profile

    @cloud_profile.setter
    def cloud_profile(self, cloud_profile):
        """Sets the cloud_profile of this ProfileSummaryModel.

        Indicates whether the profile is user profile.  # noqa: E501

        :param cloud_profile: The cloud_profile of this ProfileSummaryModel.  # noqa: E501
        :type: bool
        """

        self._cloud_profile = cloud_profile

    @property
    def device_type(self):
        """Gets the device_type of this ProfileSummaryModel.  # noqa: E501

        Value indicating device type.  # noqa: E501

        :return: The device_type of this ProfileSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ProfileSummaryModel.

        Value indicating device type.  # noqa: E501

        :param device_type: The device_type of this ProfileSummaryModel.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 100, 101, 102, 103, 104, 105]  # noqa: E501
        if (self._configuration.client_side_validation and
                device_type not in allowed_values):
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def last_profile_published_version(self):
        """Gets the last_profile_published_version of this ProfileSummaryModel.  # noqa: E501

        Value indicating published profile version.  # noqa: E501

        :return: The last_profile_published_version of this ProfileSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._last_profile_published_version

    @last_profile_published_version.setter
    def last_profile_published_version(self, last_profile_published_version):
        """Sets the last_profile_published_version of this ProfileSummaryModel.

        Value indicating published profile version.  # noqa: E501

        :param last_profile_published_version: The last_profile_published_version of this ProfileSummaryModel.  # noqa: E501
        :type: int
        """

        self._last_profile_published_version = last_profile_published_version

    @property
    def active(self):
        """Gets the active of this ProfileSummaryModel.  # noqa: E501

        Indicates whether the profile is active or not.  # noqa: E501

        :return: The active of this ProfileSummaryModel.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ProfileSummaryModel.

        Indicates whether the profile is active or not.  # noqa: E501

        :param active: The active of this ProfileSummaryModel.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def profile_name(self):
        """Gets the profile_name of this ProfileSummaryModel.  # noqa: E501

        Indicates name of the profile.  # noqa: E501

        :return: The profile_name of this ProfileSummaryModel.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this ProfileSummaryModel.

        Indicates name of the profile.  # noqa: E501

        :param profile_name: The profile_name of this ProfileSummaryModel.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    @property
    def device_profile_assignment_type(self):
        """Gets the device_profile_assignment_type of this ProfileSummaryModel.  # noqa: E501

        Indicates profile assignment type.  # noqa: E501

        :return: The device_profile_assignment_type of this ProfileSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._device_profile_assignment_type

    @device_profile_assignment_type.setter
    def device_profile_assignment_type(self, device_profile_assignment_type):
        """Sets the device_profile_assignment_type of this ProfileSummaryModel.

        Indicates profile assignment type.  # noqa: E501

        :param device_profile_assignment_type: The device_profile_assignment_type of this ProfileSummaryModel.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4, 5]  # noqa: E501
        if (self._configuration.client_side_validation and
                device_profile_assignment_type not in allowed_values):
            raise ValueError(
                "Invalid value for `device_profile_assignment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_profile_assignment_type, allowed_values)
            )

        self._device_profile_assignment_type = device_profile_assignment_type

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
        if issubclass(ProfileSummaryModel, dict):
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
        if not isinstance(other, ProfileSummaryModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProfileSummaryModel):
            return True

        return self.to_dict() != other.to_dict()
