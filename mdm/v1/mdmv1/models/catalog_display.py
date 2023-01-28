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


class CatalogDisplay(object):
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
        'display_name': 'str',
        'display_desc': 'str',
        'catalog_icon_url': 'str',
        'use_default_icon': 'bool',
        'pre_action_text': 'str',
        'post_action_text': 'str',
        'action_type': 'str',
        'categories': 'list[int]'
    }

    attribute_map = {
        'display_name': 'display_name',
        'display_desc': 'display_desc',
        'catalog_icon_url': 'catalog_icon_url',
        'use_default_icon': 'use_default_icon',
        'pre_action_text': 'pre_action_text',
        'post_action_text': 'post_action_text',
        'action_type': 'action_type',
        'categories': 'categories'
    }

    def __init__(self, display_name=None, display_desc=None, catalog_icon_url=None, use_default_icon=None, pre_action_text=None, post_action_text=None, action_type=None, categories=None, _configuration=None):  # noqa: E501
        """CatalogDisplay - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display_name = None
        self._display_desc = None
        self._catalog_icon_url = None
        self._use_default_icon = None
        self._pre_action_text = None
        self._post_action_text = None
        self._action_type = None
        self._categories = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if display_desc is not None:
            self.display_desc = display_desc
        if catalog_icon_url is not None:
            self.catalog_icon_url = catalog_icon_url
        if use_default_icon is not None:
            self.use_default_icon = use_default_icon
        if pre_action_text is not None:
            self.pre_action_text = pre_action_text
        if post_action_text is not None:
            self.post_action_text = post_action_text
        if action_type is not None:
            self.action_type = action_type
        if categories is not None:
            self.categories = categories

    @property
    def display_name(self):
        """Gets the display_name of this CatalogDisplay.  # noqa: E501


        :return: The display_name of this CatalogDisplay.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CatalogDisplay.


        :param display_name: The display_name of this CatalogDisplay.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def display_desc(self):
        """Gets the display_desc of this CatalogDisplay.  # noqa: E501


        :return: The display_desc of this CatalogDisplay.  # noqa: E501
        :rtype: str
        """
        return self._display_desc

    @display_desc.setter
    def display_desc(self, display_desc):
        """Sets the display_desc of this CatalogDisplay.


        :param display_desc: The display_desc of this CatalogDisplay.  # noqa: E501
        :type: str
        """

        self._display_desc = display_desc

    @property
    def catalog_icon_url(self):
        """Gets the catalog_icon_url of this CatalogDisplay.  # noqa: E501


        :return: The catalog_icon_url of this CatalogDisplay.  # noqa: E501
        :rtype: str
        """
        return self._catalog_icon_url

    @catalog_icon_url.setter
    def catalog_icon_url(self, catalog_icon_url):
        """Sets the catalog_icon_url of this CatalogDisplay.


        :param catalog_icon_url: The catalog_icon_url of this CatalogDisplay.  # noqa: E501
        :type: str
        """

        self._catalog_icon_url = catalog_icon_url

    @property
    def use_default_icon(self):
        """Gets the use_default_icon of this CatalogDisplay.  # noqa: E501


        :return: The use_default_icon of this CatalogDisplay.  # noqa: E501
        :rtype: bool
        """
        return self._use_default_icon

    @use_default_icon.setter
    def use_default_icon(self, use_default_icon):
        """Sets the use_default_icon of this CatalogDisplay.


        :param use_default_icon: The use_default_icon of this CatalogDisplay.  # noqa: E501
        :type: bool
        """

        self._use_default_icon = use_default_icon

    @property
    def pre_action_text(self):
        """Gets the pre_action_text of this CatalogDisplay.  # noqa: E501


        :return: The pre_action_text of this CatalogDisplay.  # noqa: E501
        :rtype: str
        """
        return self._pre_action_text

    @pre_action_text.setter
    def pre_action_text(self, pre_action_text):
        """Sets the pre_action_text of this CatalogDisplay.


        :param pre_action_text: The pre_action_text of this CatalogDisplay.  # noqa: E501
        :type: str
        """

        self._pre_action_text = pre_action_text

    @property
    def post_action_text(self):
        """Gets the post_action_text of this CatalogDisplay.  # noqa: E501


        :return: The post_action_text of this CatalogDisplay.  # noqa: E501
        :rtype: str
        """
        return self._post_action_text

    @post_action_text.setter
    def post_action_text(self, post_action_text):
        """Sets the post_action_text of this CatalogDisplay.


        :param post_action_text: The post_action_text of this CatalogDisplay.  # noqa: E501
        :type: str
        """

        self._post_action_text = post_action_text

    @property
    def action_type(self):
        """Gets the action_type of this CatalogDisplay.  # noqa: E501


        :return: The action_type of this CatalogDisplay.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this CatalogDisplay.


        :param action_type: The action_type of this CatalogDisplay.  # noqa: E501
        :type: str
        """

        self._action_type = action_type

    @property
    def categories(self):
        """Gets the categories of this CatalogDisplay.  # noqa: E501


        :return: The categories of this CatalogDisplay.  # noqa: E501
        :rtype: list[int]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CatalogDisplay.


        :param categories: The categories of this CatalogDisplay.  # noqa: E501
        :type: list[int]
        """

        self._categories = categories

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
        if issubclass(CatalogDisplay, dict):
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
        if not isinstance(other, CatalogDisplay):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogDisplay):
            return True

        return self.to_dict() != other.to_dict()