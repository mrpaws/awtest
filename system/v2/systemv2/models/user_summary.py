# coding: utf-8

"""
    System API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv2.configuration import Configuration


class UserSummary(object):
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
        'display': 'str',
        'value': 'str',
        'ref': 'str'
    }

    attribute_map = {
        'display': 'display',
        'value': 'value',
        'ref': '$ref'
    }

    def __init__(self, display=None, value=None, ref=None, _configuration=None):  # noqa: E501
        """UserSummary - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display = None
        self._value = None
        self._ref = None
        self.discriminator = None

        if display is not None:
            self.display = display
        if value is not None:
            self.value = value
        if ref is not None:
            self.ref = ref

    @property
    def display(self):
        """Gets the display of this UserSummary.  # noqa: E501

        Name of the user.  # noqa: E501

        :return: The display of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this UserSummary.

        Name of the user.  # noqa: E501

        :param display: The display of this UserSummary.  # noqa: E501
        :type: str
        """

        self._display = display

    @property
    def value(self):
        """Gets the value of this UserSummary.  # noqa: E501

        Unique identifier for User.  # noqa: E501

        :return: The value of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UserSummary.

        Unique identifier for User.  # noqa: E501

        :param value: The value of this UserSummary.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def ref(self):
        """Gets the ref of this UserSummary.  # noqa: E501

        User location URI  # noqa: E501

        :return: The ref of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this UserSummary.

        User location URI  # noqa: E501

        :param ref: The ref of this UserSummary.  # noqa: E501
        :type: str
        """

        self._ref = ref

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
        if issubclass(UserSummary, dict):
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
        if not isinstance(other, UserSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSummary):
            return True

        return self.to_dict() != other.to_dict()
