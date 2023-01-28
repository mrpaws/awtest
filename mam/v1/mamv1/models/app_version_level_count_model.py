# coding: utf-8

"""
    MAM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv1.configuration import Configuration


class AppVersionLevelCountModel(object):
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
        'application_version': 'str',
        'assigned_count': 'int',
        'installed_count': 'int',
        'sideloaded_count': 'int'
    }

    attribute_map = {
        'application_version': 'application_version',
        'assigned_count': 'assigned_count',
        'installed_count': 'installed_count',
        'sideloaded_count': 'sideloaded_count'
    }

    def __init__(self, application_version=None, assigned_count=None, installed_count=None, sideloaded_count=None, _configuration=None):  # noqa: E501
        """AppVersionLevelCountModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_version = None
        self._assigned_count = None
        self._installed_count = None
        self._sideloaded_count = None
        self.discriminator = None

        if application_version is not None:
            self.application_version = application_version
        if assigned_count is not None:
            self.assigned_count = assigned_count
        if installed_count is not None:
            self.installed_count = installed_count
        if sideloaded_count is not None:
            self.sideloaded_count = sideloaded_count

    @property
    def application_version(self):
        """Gets the application_version of this AppVersionLevelCountModel.  # noqa: E501

        The version of the application  # noqa: E501

        :return: The application_version of this AppVersionLevelCountModel.  # noqa: E501
        :rtype: str
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """Sets the application_version of this AppVersionLevelCountModel.

        The version of the application  # noqa: E501

        :param application_version: The application_version of this AppVersionLevelCountModel.  # noqa: E501
        :type: str
        """

        self._application_version = application_version

    @property
    def assigned_count(self):
        """Gets the assigned_count of this AppVersionLevelCountModel.  # noqa: E501

        The count of assigned devices  # noqa: E501

        :return: The assigned_count of this AppVersionLevelCountModel.  # noqa: E501
        :rtype: int
        """
        return self._assigned_count

    @assigned_count.setter
    def assigned_count(self, assigned_count):
        """Sets the assigned_count of this AppVersionLevelCountModel.

        The count of assigned devices  # noqa: E501

        :param assigned_count: The assigned_count of this AppVersionLevelCountModel.  # noqa: E501
        :type: int
        """

        self._assigned_count = assigned_count

    @property
    def installed_count(self):
        """Gets the installed_count of this AppVersionLevelCountModel.  # noqa: E501

        The count of the devices which have the app assigned and installed  # noqa: E501

        :return: The installed_count of this AppVersionLevelCountModel.  # noqa: E501
        :rtype: int
        """
        return self._installed_count

    @installed_count.setter
    def installed_count(self, installed_count):
        """Sets the installed_count of this AppVersionLevelCountModel.

        The count of the devices which have the app assigned and installed  # noqa: E501

        :param installed_count: The installed_count of this AppVersionLevelCountModel.  # noqa: E501
        :type: int
        """

        self._installed_count = installed_count

    @property
    def sideloaded_count(self):
        """Gets the sideloaded_count of this AppVersionLevelCountModel.  # noqa: E501

        The number of devices that have different versions of this app installed but do not have a valid assignment.  # noqa: E501

        :return: The sideloaded_count of this AppVersionLevelCountModel.  # noqa: E501
        :rtype: int
        """
        return self._sideloaded_count

    @sideloaded_count.setter
    def sideloaded_count(self, sideloaded_count):
        """Sets the sideloaded_count of this AppVersionLevelCountModel.

        The number of devices that have different versions of this app installed but do not have a valid assignment.  # noqa: E501

        :param sideloaded_count: The sideloaded_count of this AppVersionLevelCountModel.  # noqa: E501
        :type: int
        """

        self._sideloaded_count = sideloaded_count

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
        if issubclass(AppVersionLevelCountModel, dict):
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
        if not isinstance(other, AppVersionLevelCountModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppVersionLevelCountModel):
            return True

        return self.to_dict() != other.to_dict()