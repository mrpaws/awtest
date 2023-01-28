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


class AppleCustomSettingsPayloadV2Entity(object):
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
        'custom_settings': 'str'
    }

    attribute_map = {
        'custom_settings': 'CustomSettings'
    }

    def __init__(self, custom_settings=None, _configuration=None):  # noqa: E501
        """AppleCustomSettingsPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_settings = None
        self.discriminator = None

        if custom_settings is not None:
            self.custom_settings = custom_settings

    @property
    def custom_settings(self):
        """Gets the custom_settings of this AppleCustomSettingsPayloadV2Entity.  # noqa: E501

        Gets or sets custom settings for the device profile.  # noqa: E501

        :return: The custom_settings of this AppleCustomSettingsPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._custom_settings

    @custom_settings.setter
    def custom_settings(self, custom_settings):
        """Sets the custom_settings of this AppleCustomSettingsPayloadV2Entity.

        Gets or sets custom settings for the device profile.  # noqa: E501

        :param custom_settings: The custom_settings of this AppleCustomSettingsPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._custom_settings = custom_settings

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
        if issubclass(AppleCustomSettingsPayloadV2Entity, dict):
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
        if not isinstance(other, AppleCustomSettingsPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleCustomSettingsPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
