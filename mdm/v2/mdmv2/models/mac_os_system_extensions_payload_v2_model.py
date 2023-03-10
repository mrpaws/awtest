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


class MacOsSystemExtensionsPayloadV2Model(object):
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
        'allow_user_overrides': 'bool',
        'allowed_system_extension_types': 'list[MacOsAllowedSystemExtensionTypesV2Model_]',
        'allowed_system_extensions': 'list[MacOsAllowedSystemExtensionV2Model_]'
    }

    attribute_map = {
        'allow_user_overrides': 'AllowUserOverrides',
        'allowed_system_extension_types': 'AllowedSystemExtensionTypes',
        'allowed_system_extensions': 'AllowedSystemExtensions'
    }

    def __init__(self, allow_user_overrides=None, allowed_system_extension_types=None, allowed_system_extensions=None, _configuration=None):  # noqa: E501
        """MacOsSystemExtensionsPayloadV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_user_overrides = None
        self._allowed_system_extension_types = None
        self._allowed_system_extensions = None
        self.discriminator = None

        if allow_user_overrides is not None:
            self.allow_user_overrides = allow_user_overrides
        if allowed_system_extension_types is not None:
            self.allowed_system_extension_types = allowed_system_extension_types
        if allowed_system_extensions is not None:
            self.allowed_system_extensions = allowed_system_extensions

    @property
    def allow_user_overrides(self):
        """Gets the allow_user_overrides of this MacOsSystemExtensionsPayloadV2Model.  # noqa: E501

        Gets or sets a value indicating whether if false, restricts users from approving additional system extensions.  # noqa: E501

        :return: The allow_user_overrides of this MacOsSystemExtensionsPayloadV2Model.  # noqa: E501
        :rtype: bool
        """
        return self._allow_user_overrides

    @allow_user_overrides.setter
    def allow_user_overrides(self, allow_user_overrides):
        """Sets the allow_user_overrides of this MacOsSystemExtensionsPayloadV2Model.

        Gets or sets a value indicating whether if false, restricts users from approving additional system extensions.  # noqa: E501

        :param allow_user_overrides: The allow_user_overrides of this MacOsSystemExtensionsPayloadV2Model.  # noqa: E501
        :type: bool
        """

        self._allow_user_overrides = allow_user_overrides

    @property
    def allowed_system_extension_types(self):
        """Gets the allowed_system_extension_types of this MacOsSystemExtensionsPayloadV2Model.  # noqa: E501

        Gets or sets includes a list of team identifiers with types of system extensions allowed or not allowed.  Team identifier Value \"*\" indicates the global team identifier.  # noqa: E501

        :return: The allowed_system_extension_types of this MacOsSystemExtensionsPayloadV2Model.  # noqa: E501
        :rtype: list[MacOsAllowedSystemExtensionTypesV2Model_]
        """
        return self._allowed_system_extension_types

    @allowed_system_extension_types.setter
    def allowed_system_extension_types(self, allowed_system_extension_types):
        """Sets the allowed_system_extension_types of this MacOsSystemExtensionsPayloadV2Model.

        Gets or sets includes a list of team identifiers with types of system extensions allowed or not allowed.  Team identifier Value \"*\" indicates the global team identifier.  # noqa: E501

        :param allowed_system_extension_types: The allowed_system_extension_types of this MacOsSystemExtensionsPayloadV2Model.  # noqa: E501
        :type: list[MacOsAllowedSystemExtensionTypesV2Model_]
        """

        self._allowed_system_extension_types = allowed_system_extension_types

    @property
    def allowed_system_extensions(self):
        """Gets the allowed_system_extensions of this MacOsSystemExtensionsPayloadV2Model.  # noqa: E501

        Gets or sets includes a list of team identifier and bundle identifier pairs defining the system extension to be installed.  Either Identifier is optional, but both can be included.  # noqa: E501

        :return: The allowed_system_extensions of this MacOsSystemExtensionsPayloadV2Model.  # noqa: E501
        :rtype: list[MacOsAllowedSystemExtensionV2Model_]
        """
        return self._allowed_system_extensions

    @allowed_system_extensions.setter
    def allowed_system_extensions(self, allowed_system_extensions):
        """Sets the allowed_system_extensions of this MacOsSystemExtensionsPayloadV2Model.

        Gets or sets includes a list of team identifier and bundle identifier pairs defining the system extension to be installed.  Either Identifier is optional, but both can be included.  # noqa: E501

        :param allowed_system_extensions: The allowed_system_extensions of this MacOsSystemExtensionsPayloadV2Model.  # noqa: E501
        :type: list[MacOsAllowedSystemExtensionV2Model_]
        """

        self._allowed_system_extensions = allowed_system_extensions

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
        if issubclass(MacOsSystemExtensionsPayloadV2Model, dict):
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
        if not isinstance(other, MacOsSystemExtensionsPayloadV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MacOsSystemExtensionsPayloadV2Model):
            return True

        return self.to_dict() != other.to_dict()
