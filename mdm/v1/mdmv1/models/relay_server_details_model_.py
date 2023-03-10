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


class RelayServerDetailsModel_(object):
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
        'general': 'RelayServerGeneralDetailsModel_',
        'assignment': 'RelayServerAssignmentModel_',
        'device_connection': 'RelayServerDeviceConnectionModel_',
        'console_connection': 'RelayServerConsoleConnectionModel_',
        'pull_connection': 'RelayServerPullConnectionModel_'
    }

    attribute_map = {
        'general': 'General',
        'assignment': 'Assignment',
        'device_connection': 'DeviceConnection',
        'console_connection': 'ConsoleConnection',
        'pull_connection': 'PullConnection'
    }

    def __init__(self, general=None, assignment=None, device_connection=None, console_connection=None, pull_connection=None, _configuration=None):  # noqa: E501
        """RelayServerDetailsModel_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._general = None
        self._assignment = None
        self._device_connection = None
        self._console_connection = None
        self._pull_connection = None
        self.discriminator = None

        if general is not None:
            self.general = general
        if assignment is not None:
            self.assignment = assignment
        if device_connection is not None:
            self.device_connection = device_connection
        if console_connection is not None:
            self.console_connection = console_connection
        if pull_connection is not None:
            self.pull_connection = pull_connection

    @property
    def general(self):
        """Gets the general of this RelayServerDetailsModel_.  # noqa: E501

        Gets or sets the General details of the relay server.  # noqa: E501

        :return: The general of this RelayServerDetailsModel_.  # noqa: E501
        :rtype: RelayServerGeneralDetailsModel_
        """
        return self._general

    @general.setter
    def general(self, general):
        """Sets the general of this RelayServerDetailsModel_.

        Gets or sets the General details of the relay server.  # noqa: E501

        :param general: The general of this RelayServerDetailsModel_.  # noqa: E501
        :type: RelayServerGeneralDetailsModel_
        """

        self._general = general

    @property
    def assignment(self):
        """Gets the assignment of this RelayServerDetailsModel_.  # noqa: E501

        Gets or sets the assignment details of the relay server.  # noqa: E501

        :return: The assignment of this RelayServerDetailsModel_.  # noqa: E501
        :rtype: RelayServerAssignmentModel_
        """
        return self._assignment

    @assignment.setter
    def assignment(self, assignment):
        """Sets the assignment of this RelayServerDetailsModel_.

        Gets or sets the assignment details of the relay server.  # noqa: E501

        :param assignment: The assignment of this RelayServerDetailsModel_.  # noqa: E501
        :type: RelayServerAssignmentModel_
        """

        self._assignment = assignment

    @property
    def device_connection(self):
        """Gets the device_connection of this RelayServerDetailsModel_.  # noqa: E501

        Gets or sets the device connection details of the relay server.  # noqa: E501

        :return: The device_connection of this RelayServerDetailsModel_.  # noqa: E501
        :rtype: RelayServerDeviceConnectionModel_
        """
        return self._device_connection

    @device_connection.setter
    def device_connection(self, device_connection):
        """Sets the device_connection of this RelayServerDetailsModel_.

        Gets or sets the device connection details of the relay server.  # noqa: E501

        :param device_connection: The device_connection of this RelayServerDetailsModel_.  # noqa: E501
        :type: RelayServerDeviceConnectionModel_
        """

        self._device_connection = device_connection

    @property
    def console_connection(self):
        """Gets the console_connection of this RelayServerDetailsModel_.  # noqa: E501

        Gets or sets the console connection details of the relay server.  # noqa: E501

        :return: The console_connection of this RelayServerDetailsModel_.  # noqa: E501
        :rtype: RelayServerConsoleConnectionModel_
        """
        return self._console_connection

    @console_connection.setter
    def console_connection(self, console_connection):
        """Sets the console_connection of this RelayServerDetailsModel_.

        Gets or sets the console connection details of the relay server.  # noqa: E501

        :param console_connection: The console_connection of this RelayServerDetailsModel_.  # noqa: E501
        :type: RelayServerConsoleConnectionModel_
        """

        self._console_connection = console_connection

    @property
    def pull_connection(self):
        """Gets the pull_connection of this RelayServerDetailsModel_.  # noqa: E501

        Gets or sets the Pull connection details of the relay server.  # noqa: E501

        :return: The pull_connection of this RelayServerDetailsModel_.  # noqa: E501
        :rtype: RelayServerPullConnectionModel_
        """
        return self._pull_connection

    @pull_connection.setter
    def pull_connection(self, pull_connection):
        """Sets the pull_connection of this RelayServerDetailsModel_.

        Gets or sets the Pull connection details of the relay server.  # noqa: E501

        :param pull_connection: The pull_connection of this RelayServerDetailsModel_.  # noqa: E501
        :type: RelayServerPullConnectionModel_
        """

        self._pull_connection = pull_connection

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
        if issubclass(RelayServerDetailsModel_, dict):
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
        if not isinstance(other, RelayServerDetailsModel_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelayServerDetailsModel_):
            return True

        return self.to_dict() != other.to_dict()
