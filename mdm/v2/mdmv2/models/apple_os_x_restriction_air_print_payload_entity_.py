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


class AppleOsXRestrictionAirPrintPayloadEntity_(object):
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
        'allow_air_print': 'bool',
        'force_air_print_trusted_tls_requirement': 'bool',
        'allow_air_printi_beacon_discovery': 'bool'
    }

    attribute_map = {
        'allow_air_print': 'AllowAirPrint',
        'force_air_print_trusted_tls_requirement': 'ForceAirPrintTrustedTLSRequirement',
        'allow_air_printi_beacon_discovery': 'AllowAirPrintiBeaconDiscovery'
    }

    def __init__(self, allow_air_print=None, force_air_print_trusted_tls_requirement=None, allow_air_printi_beacon_discovery=None, _configuration=None):  # noqa: E501
        """AppleOsXRestrictionAirPrintPayloadEntity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_air_print = None
        self._force_air_print_trusted_tls_requirement = None
        self._allow_air_printi_beacon_discovery = None
        self.discriminator = None

        if allow_air_print is not None:
            self.allow_air_print = allow_air_print
        if force_air_print_trusted_tls_requirement is not None:
            self.force_air_print_trusted_tls_requirement = force_air_print_trusted_tls_requirement
        if allow_air_printi_beacon_discovery is not None:
            self.allow_air_printi_beacon_discovery = allow_air_printi_beacon_discovery

    @property
    def allow_air_print(self):
        """Gets the allow_air_print of this AppleOsXRestrictionAirPrintPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disallows AirPrint on macOS 10.13+.  # noqa: E501

        :return: The allow_air_print of this AppleOsXRestrictionAirPrintPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_air_print

    @allow_air_print.setter
    def allow_air_print(self, allow_air_print):
        """Sets the allow_air_print of this AppleOsXRestrictionAirPrintPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disallows AirPrint on macOS 10.13+.  # noqa: E501

        :param allow_air_print: The allow_air_print of this AppleOsXRestrictionAirPrintPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_air_print = allow_air_print

    @property
    def force_air_print_trusted_tls_requirement(self):
        """Gets the force_air_print_trusted_tls_requirement of this AppleOsXRestrictionAirPrintPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to true, requires trusted certificates for TLS printing communication on macOS 10.13+.  # noqa: E501

        :return: The force_air_print_trusted_tls_requirement of this AppleOsXRestrictionAirPrintPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._force_air_print_trusted_tls_requirement

    @force_air_print_trusted_tls_requirement.setter
    def force_air_print_trusted_tls_requirement(self, force_air_print_trusted_tls_requirement):
        """Sets the force_air_print_trusted_tls_requirement of this AppleOsXRestrictionAirPrintPayloadEntity_.

        Gets or sets a value indicating whether if set to true, requires trusted certificates for TLS printing communication on macOS 10.13+.  # noqa: E501

        :param force_air_print_trusted_tls_requirement: The force_air_print_trusted_tls_requirement of this AppleOsXRestrictionAirPrintPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._force_air_print_trusted_tls_requirement = force_air_print_trusted_tls_requirement

    @property
    def allow_air_printi_beacon_discovery(self):
        """Gets the allow_air_printi_beacon_discovery of this AppleOsXRestrictionAirPrintPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disables iBeacon discovery of AirPrint printers on macOS 10.13+.  # noqa: E501

        :return: The allow_air_printi_beacon_discovery of this AppleOsXRestrictionAirPrintPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_air_printi_beacon_discovery

    @allow_air_printi_beacon_discovery.setter
    def allow_air_printi_beacon_discovery(self, allow_air_printi_beacon_discovery):
        """Sets the allow_air_printi_beacon_discovery of this AppleOsXRestrictionAirPrintPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disables iBeacon discovery of AirPrint printers on macOS 10.13+.  # noqa: E501

        :param allow_air_printi_beacon_discovery: The allow_air_printi_beacon_discovery of this AppleOsXRestrictionAirPrintPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_air_printi_beacon_discovery = allow_air_printi_beacon_discovery

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
        if issubclass(AppleOsXRestrictionAirPrintPayloadEntity_, dict):
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
        if not isinstance(other, AppleOsXRestrictionAirPrintPayloadEntity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleOsXRestrictionAirPrintPayloadEntity_):
            return True

        return self.to_dict() != other.to_dict()
