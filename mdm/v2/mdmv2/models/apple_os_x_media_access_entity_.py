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


class AppleOsXMediaAccessEntity_(object):
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
        'allow': 'bool',
        'authenticate': 'bool',
        'read_only': 'bool'
    }

    attribute_map = {
        'allow': 'Allow',
        'authenticate': 'Authenticate',
        'read_only': 'Read-Only'
    }

    def __init__(self, allow=None, authenticate=None, read_only=None, _configuration=None):  # noqa: E501
        """AppleOsXMediaAccessEntity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow = None
        self._authenticate = None
        self._read_only = None
        self.discriminator = None

        if allow is not None:
            self.allow = allow
        if authenticate is not None:
            self.authenticate = authenticate
        if read_only is not None:
            self.read_only = read_only

    @property
    def allow(self):
        """Gets the allow of this AppleOsXMediaAccessEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, the media will not be mounted.  # noqa: E501

        :return: The allow of this AppleOsXMediaAccessEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """Sets the allow of this AppleOsXMediaAccessEntity_.

        Gets or sets a value indicating whether if set to false, the media will not be mounted.  # noqa: E501

        :param allow: The allow of this AppleOsXMediaAccessEntity_.  # noqa: E501
        :type: bool
        """

        self._allow = allow

    @property
    def authenticate(self):
        """Gets the authenticate of this AppleOsXMediaAccessEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to true, the user will be authenticated before the media is mounted.  # noqa: E501

        :return: The authenticate of this AppleOsXMediaAccessEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._authenticate

    @authenticate.setter
    def authenticate(self, authenticate):
        """Sets the authenticate of this AppleOsXMediaAccessEntity_.

        Gets or sets a value indicating whether if set to true, the user will be authenticated before the media is mounted.  # noqa: E501

        :param authenticate: The authenticate of this AppleOsXMediaAccessEntity_.  # noqa: E501
        :type: bool
        """

        self._authenticate = authenticate

    @property
    def read_only(self):
        """Gets the read_only of this AppleOsXMediaAccessEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to true, the media will be mounted as read-only.  # noqa: E501

        :return: The read_only of this AppleOsXMediaAccessEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this AppleOsXMediaAccessEntity_.

        Gets or sets a value indicating whether if set to true, the media will be mounted as read-only.  # noqa: E501

        :param read_only: The read_only of this AppleOsXMediaAccessEntity_.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

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
        if issubclass(AppleOsXMediaAccessEntity_, dict):
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
        if not isinstance(other, AppleOsXMediaAccessEntity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleOsXMediaAccessEntity_):
            return True

        return self.to_dict() != other.to_dict()
