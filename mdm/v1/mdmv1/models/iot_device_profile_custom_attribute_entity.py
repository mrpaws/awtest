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


class IOTDeviceProfileCustomAttributeEntity(object):
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
        'name': 'str',
        'value': 'str',
        'is_dynamic': 'bool'
    }

    attribute_map = {
        'name': 'Name',
        'value': 'Value',
        'is_dynamic': 'IsDynamic'
    }

    def __init__(self, name=None, value=None, is_dynamic=None, _configuration=None):  # noqa: E501
        """IOTDeviceProfileCustomAttributeEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._value = None
        self._is_dynamic = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if is_dynamic is not None:
            self.is_dynamic = is_dynamic

    @property
    def name(self):
        """Gets the name of this IOTDeviceProfileCustomAttributeEntity.  # noqa: E501

        Gets or sets custom Attribute Name.  # noqa: E501

        :return: The name of this IOTDeviceProfileCustomAttributeEntity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IOTDeviceProfileCustomAttributeEntity.

        Gets or sets custom Attribute Name.  # noqa: E501

        :param name: The name of this IOTDeviceProfileCustomAttributeEntity.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this IOTDeviceProfileCustomAttributeEntity.  # noqa: E501

        Gets or sets custom Attribute Value.  # noqa: E501

        :return: The value of this IOTDeviceProfileCustomAttributeEntity.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IOTDeviceProfileCustomAttributeEntity.

        Gets or sets custom Attribute Value.  # noqa: E501

        :param value: The value of this IOTDeviceProfileCustomAttributeEntity.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def is_dynamic(self):
        """Gets the is_dynamic of this IOTDeviceProfileCustomAttributeEntity.  # noqa: E501

        Gets or sets a value indicating whether is Dynamic.  # noqa: E501

        :return: The is_dynamic of this IOTDeviceProfileCustomAttributeEntity.  # noqa: E501
        :rtype: bool
        """
        return self._is_dynamic

    @is_dynamic.setter
    def is_dynamic(self, is_dynamic):
        """Sets the is_dynamic of this IOTDeviceProfileCustomAttributeEntity.

        Gets or sets a value indicating whether is Dynamic.  # noqa: E501

        :param is_dynamic: The is_dynamic of this IOTDeviceProfileCustomAttributeEntity.  # noqa: E501
        :type: bool
        """

        self._is_dynamic = is_dynamic

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
        if issubclass(IOTDeviceProfileCustomAttributeEntity, dict):
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
        if not isinstance(other, IOTDeviceProfileCustomAttributeEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IOTDeviceProfileCustomAttributeEntity):
            return True

        return self.to_dict() != other.to_dict()
