# coding: utf-8

"""
    MAM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv2.configuration import Configuration


class AppConfigTemplateV2Model(object):
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
        'type': 'int',
        'nested_configurations': 'list[AppConfigTemplateV2Model]'
    }

    attribute_map = {
        'key': 'key',
        'type': 'type',
        'nested_configurations': 'nested_configurations'
    }

    def __init__(self, key=None, type=None, nested_configurations=None, _configuration=None):  # noqa: E501
        """AppConfigTemplateV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._type = None
        self._nested_configurations = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if type is not None:
            self.type = type
        if nested_configurations is not None:
            self.nested_configurations = nested_configurations

    @property
    def key(self):
        """Gets the key of this AppConfigTemplateV2Model.  # noqa: E501

        The key of the application configuration  # noqa: E501

        :return: The key of this AppConfigTemplateV2Model.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AppConfigTemplateV2Model.

        The key of the application configuration  # noqa: E501

        :param key: The key of this AppConfigTemplateV2Model.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def type(self):
        """Gets the type of this AppConfigTemplateV2Model.  # noqa: E501

        Application configuration type  # noqa: E501

        :return: The type of this AppConfigTemplateV2Model.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AppConfigTemplateV2Model.

        Application configuration type  # noqa: E501

        :param type: The type of this AppConfigTemplateV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 5, 7, 9, 10, 11, 13, 14, 15, 16]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def nested_configurations(self):
        """Gets the nested_configurations of this AppConfigTemplateV2Model.  # noqa: E501

          # noqa: E501

        :return: The nested_configurations of this AppConfigTemplateV2Model.  # noqa: E501
        :rtype: list[AppConfigTemplateV2Model]
        """
        return self._nested_configurations

    @nested_configurations.setter
    def nested_configurations(self, nested_configurations):
        """Sets the nested_configurations of this AppConfigTemplateV2Model.

          # noqa: E501

        :param nested_configurations: The nested_configurations of this AppConfigTemplateV2Model.  # noqa: E501
        :type: list[AppConfigTemplateV2Model]
        """

        self._nested_configurations = nested_configurations

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
        if issubclass(AppConfigTemplateV2Model, dict):
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
        if not isinstance(other, AppConfigTemplateV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppConfigTemplateV2Model):
            return True

        return self.to_dict() != other.to_dict()
