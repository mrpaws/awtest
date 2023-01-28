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


class SmartGroupOperatingSystem(object):
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
        'device_type': 'str',
        'operator': 'str',
        'value': 'str'
    }

    attribute_map = {
        'device_type': 'DeviceType',
        'operator': 'Operator',
        'value': 'Value'
    }

    def __init__(self, device_type=None, operator=None, value=None, _configuration=None):  # noqa: E501
        """SmartGroupOperatingSystem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_type = None
        self._operator = None
        self._value = None
        self.discriminator = None

        if device_type is not None:
            self.device_type = device_type
        if operator is not None:
            self.operator = operator
        if value is not None:
            self.value = value

    @property
    def device_type(self):
        """Gets the device_type of this SmartGroupOperatingSystem.  # noqa: E501

        Gets or sets device Type name.  # noqa: E501

        :return: The device_type of this SmartGroupOperatingSystem.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this SmartGroupOperatingSystem.

        Gets or sets device Type name.  # noqa: E501

        :param device_type: The device_type of this SmartGroupOperatingSystem.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def operator(self):
        """Gets the operator of this SmartGroupOperatingSystem.  # noqa: E501

        Gets or sets operator for the Device OS value comparison like, Greater Than, Less Than etc...  # noqa: E501

        :return: The operator of this SmartGroupOperatingSystem.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this SmartGroupOperatingSystem.

        Gets or sets operator for the Device OS value comparison like, Greater Than, Less Than etc...  # noqa: E501

        :param operator: The operator of this SmartGroupOperatingSystem.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this SmartGroupOperatingSystem.  # noqa: E501

        Gets or sets operating System Version of device.  # noqa: E501

        :return: The value of this SmartGroupOperatingSystem.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SmartGroupOperatingSystem.

        Gets or sets operating System Version of device.  # noqa: E501

        :param value: The value of this SmartGroupOperatingSystem.  # noqa: E501
        :type: str
        """

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
        if issubclass(SmartGroupOperatingSystem, dict):
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
        if not isinstance(other, SmartGroupOperatingSystem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartGroupOperatingSystem):
            return True

        return self.to_dict() != other.to_dict()
