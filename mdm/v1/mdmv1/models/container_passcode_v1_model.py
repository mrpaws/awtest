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


class ContainerPasscodeV1Model(object):
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
        'passcode': 'str'
    }

    attribute_map = {
        'passcode': 'Passcode'
    }

    def __init__(self, passcode=None, _configuration=None):  # noqa: E501
        """ContainerPasscodeV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._passcode = None
        self.discriminator = None

        self.passcode = passcode

    @property
    def passcode(self):
        """Gets the passcode of this ContainerPasscodeV1Model.  # noqa: E501

        Container passcode value  # noqa: E501

        :return: The passcode of this ContainerPasscodeV1Model.  # noqa: E501
        :rtype: str
        """
        return self._passcode

    @passcode.setter
    def passcode(self, passcode):
        """Sets the passcode of this ContainerPasscodeV1Model.

        Container passcode value  # noqa: E501

        :param passcode: The passcode of this ContainerPasscodeV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and passcode is None:
            raise ValueError("Invalid value for `passcode`, must not be `None`")  # noqa: E501

        self._passcode = passcode

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
        if issubclass(ContainerPasscodeV1Model, dict):
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
        if not isinstance(other, ContainerPasscodeV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerPasscodeV1Model):
            return True

        return self.to_dict() != other.to_dict()