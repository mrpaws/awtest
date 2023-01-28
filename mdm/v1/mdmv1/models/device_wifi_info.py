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


class DeviceWifiInfo(object):
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
        'wifi_mac_address': 'str',
        'signal_strength': 'str'
    }

    attribute_map = {
        'wifi_mac_address': 'WifiMacAddress',
        'signal_strength': 'SignalStrength'
    }

    def __init__(self, wifi_mac_address=None, signal_strength=None, _configuration=None):  # noqa: E501
        """DeviceWifiInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._wifi_mac_address = None
        self._signal_strength = None
        self.discriminator = None

        if wifi_mac_address is not None:
            self.wifi_mac_address = wifi_mac_address
        if signal_strength is not None:
            self.signal_strength = signal_strength

    @property
    def wifi_mac_address(self):
        """Gets the wifi_mac_address of this DeviceWifiInfo.  # noqa: E501

        Gets or sets wifi Mac address of the device.  # noqa: E501

        :return: The wifi_mac_address of this DeviceWifiInfo.  # noqa: E501
        :rtype: str
        """
        return self._wifi_mac_address

    @wifi_mac_address.setter
    def wifi_mac_address(self, wifi_mac_address):
        """Sets the wifi_mac_address of this DeviceWifiInfo.

        Gets or sets wifi Mac address of the device.  # noqa: E501

        :param wifi_mac_address: The wifi_mac_address of this DeviceWifiInfo.  # noqa: E501
        :type: str
        """

        self._wifi_mac_address = wifi_mac_address

    @property
    def signal_strength(self):
        """Gets the signal_strength of this DeviceWifiInfo.  # noqa: E501

        Gets or sets wifi signal strength.  # noqa: E501

        :return: The signal_strength of this DeviceWifiInfo.  # noqa: E501
        :rtype: str
        """
        return self._signal_strength

    @signal_strength.setter
    def signal_strength(self, signal_strength):
        """Sets the signal_strength of this DeviceWifiInfo.

        Gets or sets wifi signal strength.  # noqa: E501

        :param signal_strength: The signal_strength of this DeviceWifiInfo.  # noqa: E501
        :type: str
        """

        self._signal_strength = signal_strength

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
        if issubclass(DeviceWifiInfo, dict):
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
        if not isinstance(other, DeviceWifiInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceWifiInfo):
            return True

        return self.to_dict() != other.to_dict()