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


class MacOsAllowedSystemExtensionTypesV2Model(object):
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
        'team_identifier': 'str',
        'allow_driver_extension_type': 'bool',
        'allow_endpoint_security_extension_type': 'bool',
        'allow_network_extension_type': 'bool'
    }

    attribute_map = {
        'team_identifier': 'TeamIdentifier',
        'allow_driver_extension_type': 'AllowDriverExtensionType',
        'allow_endpoint_security_extension_type': 'AllowEndpointSecurityExtensionType',
        'allow_network_extension_type': 'AllowNetworkExtensionType'
    }

    def __init__(self, team_identifier=None, allow_driver_extension_type=None, allow_endpoint_security_extension_type=None, allow_network_extension_type=None, _configuration=None):  # noqa: E501
        """MacOsAllowedSystemExtensionTypesV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._team_identifier = None
        self._allow_driver_extension_type = None
        self._allow_endpoint_security_extension_type = None
        self._allow_network_extension_type = None
        self.discriminator = None

        if team_identifier is not None:
            self.team_identifier = team_identifier
        if allow_driver_extension_type is not None:
            self.allow_driver_extension_type = allow_driver_extension_type
        if allow_endpoint_security_extension_type is not None:
            self.allow_endpoint_security_extension_type = allow_endpoint_security_extension_type
        if allow_network_extension_type is not None:
            self.allow_network_extension_type = allow_network_extension_type

    @property
    def team_identifier(self):
        """Gets the team_identifier of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501

        Gets or sets team identifier mapping to types of system extension.  \"*\" indicates the global team identifier.  # noqa: E501

        :return: The team_identifier of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501
        :rtype: str
        """
        return self._team_identifier

    @team_identifier.setter
    def team_identifier(self, team_identifier):
        """Sets the team_identifier of this MacOsAllowedSystemExtensionTypesV2Model.

        Gets or sets team identifier mapping to types of system extension.  \"*\" indicates the global team identifier.  # noqa: E501

        :param team_identifier: The team_identifier of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501
        :type: str
        """

        self._team_identifier = team_identifier

    @property
    def allow_driver_extension_type(self):
        """Gets the allow_driver_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501

        Gets or sets a value indicating whether indicates whether or not to allow driver extension type for given team identifier.  # noqa: E501

        :return: The allow_driver_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501
        :rtype: bool
        """
        return self._allow_driver_extension_type

    @allow_driver_extension_type.setter
    def allow_driver_extension_type(self, allow_driver_extension_type):
        """Sets the allow_driver_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.

        Gets or sets a value indicating whether indicates whether or not to allow driver extension type for given team identifier.  # noqa: E501

        :param allow_driver_extension_type: The allow_driver_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501
        :type: bool
        """

        self._allow_driver_extension_type = allow_driver_extension_type

    @property
    def allow_endpoint_security_extension_type(self):
        """Gets the allow_endpoint_security_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501

        Gets or sets a value indicating whether indicates whether or not to allow endpoint security extension type for the given team identifier.  # noqa: E501

        :return: The allow_endpoint_security_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501
        :rtype: bool
        """
        return self._allow_endpoint_security_extension_type

    @allow_endpoint_security_extension_type.setter
    def allow_endpoint_security_extension_type(self, allow_endpoint_security_extension_type):
        """Sets the allow_endpoint_security_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.

        Gets or sets a value indicating whether indicates whether or not to allow endpoint security extension type for the given team identifier.  # noqa: E501

        :param allow_endpoint_security_extension_type: The allow_endpoint_security_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501
        :type: bool
        """

        self._allow_endpoint_security_extension_type = allow_endpoint_security_extension_type

    @property
    def allow_network_extension_type(self):
        """Gets the allow_network_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501

        Gets or sets a value indicating whether indicates whether or not to allow Network extension type for the given team identifier.  # noqa: E501

        :return: The allow_network_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501
        :rtype: bool
        """
        return self._allow_network_extension_type

    @allow_network_extension_type.setter
    def allow_network_extension_type(self, allow_network_extension_type):
        """Sets the allow_network_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.

        Gets or sets a value indicating whether indicates whether or not to allow Network extension type for the given team identifier.  # noqa: E501

        :param allow_network_extension_type: The allow_network_extension_type of this MacOsAllowedSystemExtensionTypesV2Model.  # noqa: E501
        :type: bool
        """

        self._allow_network_extension_type = allow_network_extension_type

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
        if issubclass(MacOsAllowedSystemExtensionTypesV2Model, dict):
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
        if not isinstance(other, MacOsAllowedSystemExtensionTypesV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MacOsAllowedSystemExtensionTypesV2Model):
            return True

        return self.to_dict() != other.to_dict()
