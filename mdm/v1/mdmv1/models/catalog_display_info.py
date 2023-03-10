# coding: utf-8

"""
    MDM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv1.configuration import Configuration


class CatalogDisplayInfo(object):
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
        'display_images': 'list[ImageLink]',
        'actions': 'list[ResourceAction]',
        'categories': 'list[int]',
        'display_name': 'str',
        'display_description': 'str'
    }

    attribute_map = {
        'display_images': 'display_images',
        'actions': 'actions',
        'categories': 'categories',
        'display_name': 'display_name',
        'display_description': 'display_description'
    }

    def __init__(self, display_images=None, actions=None, categories=None, display_name=None, display_description=None, _configuration=None):  # noqa: E501
        """CatalogDisplayInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display_images = None
        self._actions = None
        self._categories = None
        self._display_name = None
        self._display_description = None
        self.discriminator = None

        if display_images is not None:
            self.display_images = display_images
        if actions is not None:
            self.actions = actions
        if categories is not None:
            self.categories = categories
        if display_name is not None:
            self.display_name = display_name
        if display_description is not None:
            self.display_description = display_description

    @property
    def display_images(self):
        """Gets the display_images of this CatalogDisplayInfo.  # noqa: E501


        :return: The display_images of this CatalogDisplayInfo.  # noqa: E501
        :rtype: list[ImageLink]
        """
        return self._display_images

    @display_images.setter
    def display_images(self, display_images):
        """Sets the display_images of this CatalogDisplayInfo.


        :param display_images: The display_images of this CatalogDisplayInfo.  # noqa: E501
        :type: list[ImageLink]
        """

        self._display_images = display_images

    @property
    def actions(self):
        """Gets the actions of this CatalogDisplayInfo.  # noqa: E501


        :return: The actions of this CatalogDisplayInfo.  # noqa: E501
        :rtype: list[ResourceAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this CatalogDisplayInfo.


        :param actions: The actions of this CatalogDisplayInfo.  # noqa: E501
        :type: list[ResourceAction]
        """

        self._actions = actions

    @property
    def categories(self):
        """Gets the categories of this CatalogDisplayInfo.  # noqa: E501


        :return: The categories of this CatalogDisplayInfo.  # noqa: E501
        :rtype: list[int]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CatalogDisplayInfo.


        :param categories: The categories of this CatalogDisplayInfo.  # noqa: E501
        :type: list[int]
        """

        self._categories = categories

    @property
    def display_name(self):
        """Gets the display_name of this CatalogDisplayInfo.  # noqa: E501


        :return: The display_name of this CatalogDisplayInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CatalogDisplayInfo.


        :param display_name: The display_name of this CatalogDisplayInfo.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def display_description(self):
        """Gets the display_description of this CatalogDisplayInfo.  # noqa: E501


        :return: The display_description of this CatalogDisplayInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_description

    @display_description.setter
    def display_description(self, display_description):
        """Sets the display_description of this CatalogDisplayInfo.


        :param display_description: The display_description of this CatalogDisplayInfo.  # noqa: E501
        :type: str
        """

        self._display_description = display_description

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
        if issubclass(CatalogDisplayInfo, dict):
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
        if not isinstance(other, CatalogDisplayInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogDisplayInfo):
            return True

        return self.to_dict() != other.to_dict()
