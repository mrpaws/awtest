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


class RemoteManagementSessionRequestV2Model(object):
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
        'remote_management_tool_name': 'str'
    }

    attribute_map = {
        'remote_management_tool_name': 'remote_management_tool_name'
    }

    def __init__(self, remote_management_tool_name=None, _configuration=None):  # noqa: E501
        """RemoteManagementSessionRequestV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._remote_management_tool_name = None
        self.discriminator = None

        if remote_management_tool_name is not None:
            self.remote_management_tool_name = remote_management_tool_name

    @property
    def remote_management_tool_name(self):
        """Gets the remote_management_tool_name of this RemoteManagementSessionRequestV2Model.  # noqa: E501

        Tool name for Remote Management session with the device.  # noqa: E501

        :return: The remote_management_tool_name of this RemoteManagementSessionRequestV2Model.  # noqa: E501
        :rtype: str
        """
        return self._remote_management_tool_name

    @remote_management_tool_name.setter
    def remote_management_tool_name(self, remote_management_tool_name):
        """Sets the remote_management_tool_name of this RemoteManagementSessionRequestV2Model.

        Tool name for Remote Management session with the device.  # noqa: E501

        :param remote_management_tool_name: The remote_management_tool_name of this RemoteManagementSessionRequestV2Model.  # noqa: E501
        :type: str
        """
        allowed_values = ["ScreenShare", "FileManager", "RemoteShell", "RegistryEditor"]  # noqa: E501
        if (self._configuration.client_side_validation and
                remote_management_tool_name not in allowed_values):
            raise ValueError(
                "Invalid value for `remote_management_tool_name` ({0}), must be one of {1}"  # noqa: E501
                .format(remote_management_tool_name, allowed_values)
            )

        self._remote_management_tool_name = remote_management_tool_name

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
        if issubclass(RemoteManagementSessionRequestV2Model, dict):
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
        if not isinstance(other, RemoteManagementSessionRequestV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteManagementSessionRequestV2Model):
            return True

        return self.to_dict() != other.to_dict()