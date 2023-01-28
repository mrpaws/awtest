# coding: utf-8

"""
    MCM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mcmv1.configuration import Configuration


class ContentGatewayCustomSettingsV3(object):
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
        'key': 'str',
        'value_type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value_type': 'value_type',
        'value': 'value'
    }

    def __init__(self, key=None, value_type=None, value=None, _configuration=None):  # noqa: E501
        """ContentGatewayCustomSettingsV3 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._value_type = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value_type = value_type
        self.value = value

    @property
    def key(self):
        """Gets the key of this ContentGatewayCustomSettingsV3.  # noqa: E501

        Custom gateway settings key  # noqa: E501

        :return: The key of this ContentGatewayCustomSettingsV3.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ContentGatewayCustomSettingsV3.

        Custom gateway settings key  # noqa: E501

        :param key: The key of this ContentGatewayCustomSettingsV3.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value_type(self):
        """Gets the value_type of this ContentGatewayCustomSettingsV3.  # noqa: E501

        Data type of the value  # noqa: E501

        :return: The value_type of this ContentGatewayCustomSettingsV3.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this ContentGatewayCustomSettingsV3.

        Data type of the value  # noqa: E501

        :param value_type: The value_type of this ContentGatewayCustomSettingsV3.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and value_type is None:
            raise ValueError("Invalid value for `value_type`, must not be `None`")  # noqa: E501

        self._value_type = value_type

    @property
    def value(self):
        """Gets the value of this ContentGatewayCustomSettingsV3.  # noqa: E501

        Custom gateway settings value  # noqa: E501

        :return: The value of this ContentGatewayCustomSettingsV3.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ContentGatewayCustomSettingsV3.

        Custom gateway settings value  # noqa: E501

        :param value: The value of this ContentGatewayCustomSettingsV3.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(ContentGatewayCustomSettingsV3, dict):
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
        if not isinstance(other, ContentGatewayCustomSettingsV3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContentGatewayCustomSettingsV3):
            return True

        return self.to_dict() != other.to_dict()
