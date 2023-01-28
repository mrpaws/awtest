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


class AndroidContainerVpnNetMotionSettings(object):
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
        'validate_server': 'bool',
        'server_suffix': 'str',
        'domain': 'str',
        'device_name': 'str',
        'debug_logging_enabled': 'bool',
        'show_warnings': 'bool'
    }

    attribute_map = {
        'validate_server': 'ValidateServer',
        'server_suffix': 'ServerSuffix',
        'domain': 'Domain',
        'device_name': 'DeviceName',
        'debug_logging_enabled': 'DebugLoggingEnabled',
        'show_warnings': 'ShowWarnings'
    }

    def __init__(self, validate_server=None, server_suffix=None, domain=None, device_name=None, debug_logging_enabled=None, show_warnings=None, _configuration=None):  # noqa: E501
        """AndroidContainerVpnNetMotionSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._validate_server = None
        self._server_suffix = None
        self._domain = None
        self._device_name = None
        self._debug_logging_enabled = None
        self._show_warnings = None
        self.discriminator = None

        if validate_server is not None:
            self.validate_server = validate_server
        if server_suffix is not None:
            self.server_suffix = server_suffix
        if domain is not None:
            self.domain = domain
        if device_name is not None:
            self.device_name = device_name
        if debug_logging_enabled is not None:
            self.debug_logging_enabled = debug_logging_enabled
        if show_warnings is not None:
            self.show_warnings = show_warnings

    @property
    def validate_server(self):
        """Gets the validate_server of this AndroidContainerVpnNetMotionSettings.  # noqa: E501

        Gets or sets EnforceServerValidation.  # noqa: E501

        :return: The validate_server of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._validate_server

    @validate_server.setter
    def validate_server(self, validate_server):
        """Sets the validate_server of this AndroidContainerVpnNetMotionSettings.

        Gets or sets EnforceServerValidation.  # noqa: E501

        :param validate_server: The validate_server of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :type: bool
        """

        self._validate_server = validate_server

    @property
    def server_suffix(self):
        """Gets the server_suffix of this AndroidContainerVpnNetMotionSettings.  # noqa: E501

        Gets or sets ServerSuffix.  # noqa: E501

        :return: The server_suffix of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :rtype: str
        """
        return self._server_suffix

    @server_suffix.setter
    def server_suffix(self, server_suffix):
        """Sets the server_suffix of this AndroidContainerVpnNetMotionSettings.

        Gets or sets ServerSuffix.  # noqa: E501

        :param server_suffix: The server_suffix of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :type: str
        """

        self._server_suffix = server_suffix

    @property
    def domain(self):
        """Gets the domain of this AndroidContainerVpnNetMotionSettings.  # noqa: E501

        Gets or sets Domain.  # noqa: E501

        :return: The domain of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AndroidContainerVpnNetMotionSettings.

        Gets or sets Domain.  # noqa: E501

        :param domain: The domain of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def device_name(self):
        """Gets the device_name of this AndroidContainerVpnNetMotionSettings.  # noqa: E501

        Gets or sets DeviceName.  # noqa: E501

        :return: The device_name of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this AndroidContainerVpnNetMotionSettings.

        Gets or sets DeviceName.  # noqa: E501

        :param device_name: The device_name of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def debug_logging_enabled(self):
        """Gets the debug_logging_enabled of this AndroidContainerVpnNetMotionSettings.  # noqa: E501

        Gets or sets EnableDebugLogging.  # noqa: E501

        :return: The debug_logging_enabled of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._debug_logging_enabled

    @debug_logging_enabled.setter
    def debug_logging_enabled(self, debug_logging_enabled):
        """Sets the debug_logging_enabled of this AndroidContainerVpnNetMotionSettings.

        Gets or sets EnableDebugLogging.  # noqa: E501

        :param debug_logging_enabled: The debug_logging_enabled of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :type: bool
        """

        self._debug_logging_enabled = debug_logging_enabled

    @property
    def show_warnings(self):
        """Gets the show_warnings of this AndroidContainerVpnNetMotionSettings.  # noqa: E501

        Gets or sets ShowWarings.  # noqa: E501

        :return: The show_warnings of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_warnings

    @show_warnings.setter
    def show_warnings(self, show_warnings):
        """Sets the show_warnings of this AndroidContainerVpnNetMotionSettings.

        Gets or sets ShowWarings.  # noqa: E501

        :param show_warnings: The show_warnings of this AndroidContainerVpnNetMotionSettings.  # noqa: E501
        :type: bool
        """

        self._show_warnings = show_warnings

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
        if issubclass(AndroidContainerVpnNetMotionSettings, dict):
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
        if not isinstance(other, AndroidContainerVpnNetMotionSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidContainerVpnNetMotionSettings):
            return True

        return self.to_dict() != other.to_dict()
