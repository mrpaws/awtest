# coding: utf-8

"""
    MCM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mcmv1.configuration import Configuration


class Link(object):
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
        'rel': 'str',
        'href': 'str',
        'title': 'str'
    }

    attribute_map = {
        'rel': 'Rel',
        'href': 'Href',
        'title': 'Title'
    }

    def __init__(self, rel=None, href=None, title=None, _configuration=None):  # noqa: E501
        """Link - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rel = None
        self._href = None
        self._title = None
        self.discriminator = None

        if rel is not None:
            self.rel = rel
        if href is not None:
            self.href = href
        if title is not None:
            self.title = title

    @property
    def rel(self):
        """Gets the rel of this Link.  # noqa: E501

        Gets or sets relational links.  # noqa: E501

        :return: The rel of this Link.  # noqa: E501
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this Link.

        Gets or sets relational links.  # noqa: E501

        :param rel: The rel of this Link.  # noqa: E501
        :type: str
        """

        self._rel = rel

    @property
    def href(self):
        """Gets the href of this Link.  # noqa: E501

        Gets or sets hyper text reference.  # noqa: E501

        :return: The href of this Link.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Link.

        Gets or sets hyper text reference.  # noqa: E501

        :param href: The href of this Link.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def title(self):
        """Gets the title of this Link.  # noqa: E501

        Gets or sets title of the link.  # noqa: E501

        :return: The title of this Link.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Link.

        Gets or sets title of the link.  # noqa: E501

        :param title: The title of this Link.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(Link, dict):
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
        if not isinstance(other, Link):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Link):
            return True

        return self.to_dict() != other.to_dict()
