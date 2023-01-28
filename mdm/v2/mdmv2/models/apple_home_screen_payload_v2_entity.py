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


class AppleHomeScreenPayloadV2Entity(object):
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
        'dock_apps': 'list[str]',
        'pages': 'list[HomeScreenLayoutPageV2Entity_]'
    }

    attribute_map = {
        'dock_apps': 'DockApps',
        'pages': 'Pages'
    }

    def __init__(self, dock_apps=None, pages=None, _configuration=None):  # noqa: E501
        """AppleHomeScreenPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dock_apps = None
        self._pages = None
        self.discriminator = None

        if dock_apps is not None:
            self.dock_apps = dock_apps
        if pages is not None:
            self.pages = pages

    @property
    def dock_apps(self):
        """Gets the dock_apps of this AppleHomeScreenPayloadV2Entity.  # noqa: E501

        Gets or sets apps to be shown in the dock.  # noqa: E501

        :return: The dock_apps of this AppleHomeScreenPayloadV2Entity.  # noqa: E501
        :rtype: list[str]
        """
        return self._dock_apps

    @dock_apps.setter
    def dock_apps(self, dock_apps):
        """Sets the dock_apps of this AppleHomeScreenPayloadV2Entity.

        Gets or sets apps to be shown in the dock.  # noqa: E501

        :param dock_apps: The dock_apps of this AppleHomeScreenPayloadV2Entity.  # noqa: E501
        :type: list[str]
        """

        self._dock_apps = dock_apps

    @property
    def pages(self):
        """Gets the pages of this AppleHomeScreenPayloadV2Entity.  # noqa: E501

        Gets or sets list of Home Screen Layout Pages.  # noqa: E501

        :return: The pages of this AppleHomeScreenPayloadV2Entity.  # noqa: E501
        :rtype: list[HomeScreenLayoutPageV2Entity_]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this AppleHomeScreenPayloadV2Entity.

        Gets or sets list of Home Screen Layout Pages.  # noqa: E501

        :param pages: The pages of this AppleHomeScreenPayloadV2Entity.  # noqa: E501
        :type: list[HomeScreenLayoutPageV2Entity_]
        """

        self._pages = pages

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
        if issubclass(AppleHomeScreenPayloadV2Entity, dict):
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
        if not isinstance(other, AppleHomeScreenPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleHomeScreenPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
