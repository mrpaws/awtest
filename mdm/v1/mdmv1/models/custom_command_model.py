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


class CustomCommandModel(object):
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
        'command_xml': 'str'
    }

    attribute_map = {
        'command_xml': 'CommandXml'
    }

    def __init__(self, command_xml=None, _configuration=None):  # noqa: E501
        """CustomCommandModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._command_xml = None
        self.discriminator = None

        if command_xml is not None:
            self.command_xml = command_xml

    @property
    def command_xml(self):
        """Gets the command_xml of this CustomCommandModel.  # noqa: E501

        Gets or sets the command xml.  # noqa: E501

        :return: The command_xml of this CustomCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._command_xml

    @command_xml.setter
    def command_xml(self, command_xml):
        """Sets the command_xml of this CustomCommandModel.

        Gets or sets the command xml.  # noqa: E501

        :param command_xml: The command_xml of this CustomCommandModel.  # noqa: E501
        :type: str
        """

        self._command_xml = command_xml

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
        if issubclass(CustomCommandModel, dict):
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
        if not isinstance(other, CustomCommandModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomCommandModel):
            return True

        return self.to_dict() != other.to_dict()
