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


class DeviceCountPerStatusV1Model(object):
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
        'devices_count': 'int',
        'reason_name': 'str'
    }

    attribute_map = {
        'devices_count': 'devicesCount',
        'reason_name': 'reasonName'
    }

    def __init__(self, devices_count=None, reason_name=None, _configuration=None):  # noqa: E501
        """DeviceCountPerStatusV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._devices_count = None
        self._reason_name = None
        self.discriminator = None

        if devices_count is not None:
            self.devices_count = devices_count
        if reason_name is not None:
            self.reason_name = reason_name

    @property
    def devices_count(self):
        """Gets the devices_count of this DeviceCountPerStatusV1Model.  # noqa: E501

        Device Count for the particular status of app or profile  # noqa: E501

        :return: The devices_count of this DeviceCountPerStatusV1Model.  # noqa: E501
        :rtype: int
        """
        return self._devices_count

    @devices_count.setter
    def devices_count(self, devices_count):
        """Sets the devices_count of this DeviceCountPerStatusV1Model.

        Device Count for the particular status of app or profile  # noqa: E501

        :param devices_count: The devices_count of this DeviceCountPerStatusV1Model.  # noqa: E501
        :type: int
        """

        self._devices_count = devices_count

    @property
    def reason_name(self):
        """Gets the reason_name of this DeviceCountPerStatusV1Model.  # noqa: E501

        Reason or Status Name of app or profile  # noqa: E501

        :return: The reason_name of this DeviceCountPerStatusV1Model.  # noqa: E501
        :rtype: str
        """
        return self._reason_name

    @reason_name.setter
    def reason_name(self, reason_name):
        """Sets the reason_name of this DeviceCountPerStatusV1Model.

        Reason or Status Name of app or profile  # noqa: E501

        :param reason_name: The reason_name of this DeviceCountPerStatusV1Model.  # noqa: E501
        :type: str
        """

        self._reason_name = reason_name

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
        if issubclass(DeviceCountPerStatusV1Model, dict):
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
        if not isinstance(other, DeviceCountPerStatusV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceCountPerStatusV1Model):
            return True

        return self.to_dict() != other.to_dict()
