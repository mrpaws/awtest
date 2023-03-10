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


class DeviceNetworkInfo(object):
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
        'connection_type': 'str',
        'ip_address': 'str',
        'mac_address': 'str',
        'name': 'str',
        'vendor': 'str'
    }

    attribute_map = {
        'connection_type': 'ConnectionType',
        'ip_address': 'IPAddress',
        'mac_address': 'MACAddress',
        'name': 'Name',
        'vendor': 'Vendor'
    }

    def __init__(self, connection_type=None, ip_address=None, mac_address=None, name=None, vendor=None, _configuration=None):  # noqa: E501
        """DeviceNetworkInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connection_type = None
        self._ip_address = None
        self._mac_address = None
        self._name = None
        self._vendor = None
        self.discriminator = None

        if connection_type is not None:
            self.connection_type = connection_type
        if ip_address is not None:
            self.ip_address = ip_address
        if mac_address is not None:
            self.mac_address = mac_address
        if name is not None:
            self.name = name
        if vendor is not None:
            self.vendor = vendor

    @property
    def connection_type(self):
        """Gets the connection_type of this DeviceNetworkInfo.  # noqa: E501


        :return: The connection_type of this DeviceNetworkInfo.  # noqa: E501
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this DeviceNetworkInfo.


        :param connection_type: The connection_type of this DeviceNetworkInfo.  # noqa: E501
        :type: str
        """

        self._connection_type = connection_type

    @property
    def ip_address(self):
        """Gets the ip_address of this DeviceNetworkInfo.  # noqa: E501


        :return: The ip_address of this DeviceNetworkInfo.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DeviceNetworkInfo.


        :param ip_address: The ip_address of this DeviceNetworkInfo.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def mac_address(self):
        """Gets the mac_address of this DeviceNetworkInfo.  # noqa: E501


        :return: The mac_address of this DeviceNetworkInfo.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this DeviceNetworkInfo.


        :param mac_address: The mac_address of this DeviceNetworkInfo.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def name(self):
        """Gets the name of this DeviceNetworkInfo.  # noqa: E501


        :return: The name of this DeviceNetworkInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceNetworkInfo.


        :param name: The name of this DeviceNetworkInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def vendor(self):
        """Gets the vendor of this DeviceNetworkInfo.  # noqa: E501


        :return: The vendor of this DeviceNetworkInfo.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this DeviceNetworkInfo.


        :param vendor: The vendor of this DeviceNetworkInfo.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

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
        if issubclass(DeviceNetworkInfo, dict):
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
        if not isinstance(other, DeviceNetworkInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceNetworkInfo):
            return True

        return self.to_dict() != other.to_dict()
