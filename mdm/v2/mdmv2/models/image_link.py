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


class ImageLink(object):
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
        'href': 'str',
        'use_default': 'bool'
    }

    attribute_map = {
        'href': 'href',
        'use_default': 'use_default'
    }

    def __init__(self, href=None, use_default=None, _configuration=None):  # noqa: E501
        """ImageLink - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._href = None
        self._use_default = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if use_default is not None:
            self.use_default = use_default

    @property
    def href(self):
        """Gets the href of this ImageLink.  # noqa: E501


        :return: The href of this ImageLink.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ImageLink.


        :param href: The href of this ImageLink.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def use_default(self):
        """Gets the use_default of this ImageLink.  # noqa: E501


        :return: The use_default of this ImageLink.  # noqa: E501
        :rtype: bool
        """
        return self._use_default

    @use_default.setter
    def use_default(self, use_default):
        """Sets the use_default of this ImageLink.


        :param use_default: The use_default of this ImageLink.  # noqa: E501
        :type: bool
        """

        self._use_default = use_default

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
        if issubclass(ImageLink, dict):
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
        if not isinstance(other, ImageLink):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageLink):
            return True

        return self.to_dict() != other.to_dict()
