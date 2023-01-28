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


class AllowRule(object):
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
        'hostname': 'str',
        'port': 'str',
        'port_location': 'str',
        'network_interface': 'str',
        'package_name': 'str'
    }

    attribute_map = {
        'hostname': 'Hostname',
        'port': 'Port',
        'port_location': 'PortLocation',
        'network_interface': 'NetworkInterface',
        'package_name': 'PackageName'
    }

    def __init__(self, hostname=None, port=None, port_location=None, network_interface=None, package_name=None, _configuration=None):  # noqa: E501
        """AllowRule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._hostname = None
        self._port = None
        self._port_location = None
        self._network_interface = None
        self._package_name = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if port is not None:
            self.port = port
        if port_location is not None:
            self.port_location = port_location
        if network_interface is not None:
            self.network_interface = network_interface
        if package_name is not None:
            self.package_name = package_name

    @property
    def hostname(self):
        """Gets the hostname of this AllowRule.  # noqa: E501

        Gets or sets Hostname.  # noqa: E501

        :return: The hostname of this AllowRule.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this AllowRule.

        Gets or sets Hostname.  # noqa: E501

        :param hostname: The hostname of this AllowRule.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def port(self):
        """Gets the port of this AllowRule.  # noqa: E501

        Gets or sets Port.  # noqa: E501

        :return: The port of this AllowRule.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AllowRule.

        Gets or sets Port.  # noqa: E501

        :param port: The port of this AllowRule.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def port_location(self):
        """Gets the port_location of this AllowRule.  # noqa: E501

        Gets or sets PortLocation.  # noqa: E501

        :return: The port_location of this AllowRule.  # noqa: E501
        :rtype: str
        """
        return self._port_location

    @port_location.setter
    def port_location(self, port_location):
        """Sets the port_location of this AllowRule.

        Gets or sets PortLocation.  # noqa: E501

        :param port_location: The port_location of this AllowRule.  # noqa: E501
        :type: str
        """

        self._port_location = port_location

    @property
    def network_interface(self):
        """Gets the network_interface of this AllowRule.  # noqa: E501

        Gets or sets NetworkInterface.  # noqa: E501

        :return: The network_interface of this AllowRule.  # noqa: E501
        :rtype: str
        """
        return self._network_interface

    @network_interface.setter
    def network_interface(self, network_interface):
        """Sets the network_interface of this AllowRule.

        Gets or sets NetworkInterface.  # noqa: E501

        :param network_interface: The network_interface of this AllowRule.  # noqa: E501
        :type: str
        """

        self._network_interface = network_interface

    @property
    def package_name(self):
        """Gets the package_name of this AllowRule.  # noqa: E501

        Gets or sets PackageName.  # noqa: E501

        :return: The package_name of this AllowRule.  # noqa: E501
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this AllowRule.

        Gets or sets PackageName.  # noqa: E501

        :param package_name: The package_name of this AllowRule.  # noqa: E501
        :type: str
        """

        self._package_name = package_name

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
        if issubclass(AllowRule, dict):
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
        if not isinstance(other, AllowRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllowRule):
            return True

        return self.to_dict() != other.to_dict()
