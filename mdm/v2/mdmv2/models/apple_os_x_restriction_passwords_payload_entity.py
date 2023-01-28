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


class AppleOsXRestrictionPasswordsPayloadEntity(object):
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
        'allow_password_auto_fill': 'bool',
        'allow_password_sharing': 'bool',
        'allow_password_proximity_requests': 'bool'
    }

    attribute_map = {
        'allow_password_auto_fill': 'AllowPasswordAutoFill',
        'allow_password_sharing': 'AllowPasswordSharing',
        'allow_password_proximity_requests': 'AllowPasswordProximityRequests'
    }

    def __init__(self, allow_password_auto_fill=None, allow_password_sharing=None, allow_password_proximity_requests=None, _configuration=None):  # noqa: E501
        """AppleOsXRestrictionPasswordsPayloadEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_password_auto_fill = None
        self._allow_password_sharing = None
        self._allow_password_proximity_requests = None
        self.discriminator = None

        if allow_password_auto_fill is not None:
            self.allow_password_auto_fill = allow_password_auto_fill
        if allow_password_sharing is not None:
            self.allow_password_sharing = allow_password_sharing
        if allow_password_proximity_requests is not None:
            self.allow_password_proximity_requests = allow_password_proximity_requests

    @property
    def allow_password_auto_fill(self):
        """Gets the allow_password_auto_fill of this AppleOsXRestrictionPasswordsPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets a value which indicates whether to allow auto filling of passwords is allowed or not on supervised iOS 12.0+.  # noqa: E501

        :return: The allow_password_auto_fill of this AppleOsXRestrictionPasswordsPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_password_auto_fill

    @allow_password_auto_fill.setter
    def allow_password_auto_fill(self, allow_password_auto_fill):
        """Sets the allow_password_auto_fill of this AppleOsXRestrictionPasswordsPayloadEntity.

        Gets or sets a value indicating whether gets or sets a value which indicates whether to allow auto filling of passwords is allowed or not on supervised iOS 12.0+.  # noqa: E501

        :param allow_password_auto_fill: The allow_password_auto_fill of this AppleOsXRestrictionPasswordsPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._allow_password_auto_fill = allow_password_auto_fill

    @property
    def allow_password_sharing(self):
        """Gets the allow_password_sharing of this AppleOsXRestrictionPasswordsPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets a value which indicates whether allow sharing of Wi-Fi passwords is allowed or not on supervised iOS 12.0+.  # noqa: E501

        :return: The allow_password_sharing of this AppleOsXRestrictionPasswordsPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_password_sharing

    @allow_password_sharing.setter
    def allow_password_sharing(self, allow_password_sharing):
        """Sets the allow_password_sharing of this AppleOsXRestrictionPasswordsPayloadEntity.

        Gets or sets a value indicating whether gets or sets a value which indicates whether allow sharing of Wi-Fi passwords is allowed or not on supervised iOS 12.0+.  # noqa: E501

        :param allow_password_sharing: The allow_password_sharing of this AppleOsXRestrictionPasswordsPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._allow_password_sharing = allow_password_sharing

    @property
    def allow_password_proximity_requests(self):
        """Gets the allow_password_proximity_requests of this AppleOsXRestrictionPasswordsPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether requesting passwords from nearby devices is allowed. Requires a supervised device. Available in macOS 10.14 and later.  # noqa: E501

        :return: The allow_password_proximity_requests of this AppleOsXRestrictionPasswordsPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_password_proximity_requests

    @allow_password_proximity_requests.setter
    def allow_password_proximity_requests(self, allow_password_proximity_requests):
        """Sets the allow_password_proximity_requests of this AppleOsXRestrictionPasswordsPayloadEntity.

        Gets or sets a value indicating whether requesting passwords from nearby devices is allowed. Requires a supervised device. Available in macOS 10.14 and later.  # noqa: E501

        :param allow_password_proximity_requests: The allow_password_proximity_requests of this AppleOsXRestrictionPasswordsPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._allow_password_proximity_requests = allow_password_proximity_requests

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
        if issubclass(AppleOsXRestrictionPasswordsPayloadEntity, dict):
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
        if not isinstance(other, AppleOsXRestrictionPasswordsPayloadEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleOsXRestrictionPasswordsPayloadEntity):
            return True

        return self.to_dict() != other.to_dict()