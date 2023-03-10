# coding: utf-8

"""
    System API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv1.configuration import Configuration


class GetCustomAttributeResult(object):
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
        'custom_attribute': 'list[OgCustomAttribute]'
    }

    attribute_map = {
        'custom_attribute': 'CustomAttribute'
    }

    def __init__(self, custom_attribute=None, _configuration=None):  # noqa: E501
        """GetCustomAttributeResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_attribute = None
        self.discriminator = None

        if custom_attribute is not None:
            self.custom_attribute = custom_attribute

    @property
    def custom_attribute(self):
        """Gets the custom_attribute of this GetCustomAttributeResult.  # noqa: E501

        Gets or sets custom Attribute Details.  # noqa: E501

        :return: The custom_attribute of this GetCustomAttributeResult.  # noqa: E501
        :rtype: list[OgCustomAttribute]
        """
        return self._custom_attribute

    @custom_attribute.setter
    def custom_attribute(self, custom_attribute):
        """Sets the custom_attribute of this GetCustomAttributeResult.

        Gets or sets custom Attribute Details.  # noqa: E501

        :param custom_attribute: The custom_attribute of this GetCustomAttributeResult.  # noqa: E501
        :type: list[OgCustomAttribute]
        """

        self._custom_attribute = custom_attribute

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
        if issubclass(GetCustomAttributeResult, dict):
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
        if not isinstance(other, GetCustomAttributeResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCustomAttributeResult):
            return True

        return self.to_dict() != other.to_dict()
