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


class CulturesResponseV1Model(object):
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
        'active_cultures': 'list[CulturesV1Model]'
    }

    attribute_map = {
        'active_cultures': 'active_cultures'
    }

    def __init__(self, active_cultures=None, _configuration=None):  # noqa: E501
        """CulturesResponseV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_cultures = None
        self.discriminator = None

        if active_cultures is not None:
            self.active_cultures = active_cultures

    @property
    def active_cultures(self):
        """Gets the active_cultures of this CulturesResponseV1Model.  # noqa: E501

        List of CultureResponseV1Model.  # noqa: E501

        :return: The active_cultures of this CulturesResponseV1Model.  # noqa: E501
        :rtype: list[CulturesV1Model]
        """
        return self._active_cultures

    @active_cultures.setter
    def active_cultures(self, active_cultures):
        """Sets the active_cultures of this CulturesResponseV1Model.

        List of CultureResponseV1Model.  # noqa: E501

        :param active_cultures: The active_cultures of this CulturesResponseV1Model.  # noqa: E501
        :type: list[CulturesV1Model]
        """

        self._active_cultures = active_cultures

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
        if issubclass(CulturesResponseV1Model, dict):
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
        if not isinstance(other, CulturesResponseV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CulturesResponseV1Model):
            return True

        return self.to_dict() != other.to_dict()
