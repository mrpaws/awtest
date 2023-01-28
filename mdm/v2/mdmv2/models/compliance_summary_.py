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


class ComplianceSummary_(object):
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
        'device_compliance': 'list[DeviceCompliance]'
    }

    attribute_map = {
        'device_compliance': 'DeviceCompliance'
    }

    def __init__(self, device_compliance=None, _configuration=None):  # noqa: E501
        """ComplianceSummary_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_compliance = None
        self.discriminator = None

        if device_compliance is not None:
            self.device_compliance = device_compliance

    @property
    def device_compliance(self):
        """Gets the device_compliance of this ComplianceSummary_.  # noqa: E501

        Gets or sets device compliance details.  # noqa: E501

        :return: The device_compliance of this ComplianceSummary_.  # noqa: E501
        :rtype: list[DeviceCompliance]
        """
        return self._device_compliance

    @device_compliance.setter
    def device_compliance(self, device_compliance):
        """Sets the device_compliance of this ComplianceSummary_.

        Gets or sets device compliance details.  # noqa: E501

        :param device_compliance: The device_compliance of this ComplianceSummary_.  # noqa: E501
        :type: list[DeviceCompliance]
        """

        self._device_compliance = device_compliance

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
        if issubclass(ComplianceSummary_, dict):
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
        if not isinstance(other, ComplianceSummary_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplianceSummary_):
            return True

        return self.to_dict() != other.to_dict()
