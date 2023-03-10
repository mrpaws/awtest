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


class HomeScreenLayoutFolderV2Entity(object):
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
        'folder_name': 'str',
        'folder_apps': 'list[str]'
    }

    attribute_map = {
        'folder_name': 'FolderName',
        'folder_apps': 'FolderApps'
    }

    def __init__(self, folder_name=None, folder_apps=None, _configuration=None):  # noqa: E501
        """HomeScreenLayoutFolderV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._folder_name = None
        self._folder_apps = None
        self.discriminator = None

        if folder_name is not None:
            self.folder_name = folder_name
        if folder_apps is not None:
            self.folder_apps = folder_apps

    @property
    def folder_name(self):
        """Gets the folder_name of this HomeScreenLayoutFolderV2Entity.  # noqa: E501

        Gets or sets folder name.  # noqa: E501

        :return: The folder_name of this HomeScreenLayoutFolderV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this HomeScreenLayoutFolderV2Entity.

        Gets or sets folder name.  # noqa: E501

        :param folder_name: The folder_name of this HomeScreenLayoutFolderV2Entity.  # noqa: E501
        :type: str
        """

        self._folder_name = folder_name

    @property
    def folder_apps(self):
        """Gets the folder_apps of this HomeScreenLayoutFolderV2Entity.  # noqa: E501

        Gets or sets apps to be shown in the folder.  # noqa: E501

        :return: The folder_apps of this HomeScreenLayoutFolderV2Entity.  # noqa: E501
        :rtype: list[str]
        """
        return self._folder_apps

    @folder_apps.setter
    def folder_apps(self, folder_apps):
        """Sets the folder_apps of this HomeScreenLayoutFolderV2Entity.

        Gets or sets apps to be shown in the folder.  # noqa: E501

        :param folder_apps: The folder_apps of this HomeScreenLayoutFolderV2Entity.  # noqa: E501
        :type: list[str]
        """

        self._folder_apps = folder_apps

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
        if issubclass(HomeScreenLayoutFolderV2Entity, dict):
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
        if not isinstance(other, HomeScreenLayoutFolderV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HomeScreenLayoutFolderV2Entity):
            return True

        return self.to_dict() != other.to_dict()
