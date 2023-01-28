# coding: utf-8

"""
    System API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv1.configuration import Configuration


class TagSearchResult(object):
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
        'ogid': 'EntityReference_',
        'tags': 'list[Tag]',
        'page': 'int',
        'page_size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'ogid': 'OGId',
        'tags': 'Tags',
        'page': 'Page',
        'page_size': 'PageSize',
        'total': 'Total'
    }

    def __init__(self, ogid=None, tags=None, page=None, page_size=None, total=None, _configuration=None):  # noqa: E501
        """TagSearchResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ogid = None
        self._tags = None
        self._page = None
        self._page_size = None
        self._total = None
        self.discriminator = None

        if ogid is not None:
            self.ogid = ogid
        if tags is not None:
            self.tags = tags
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total is not None:
            self.total = total

    @property
    def ogid(self):
        """Gets the ogid of this TagSearchResult.  # noqa: E501

        Gets or sets link to the OG where the Tag belongs to.  # noqa: E501

        :return: The ogid of this TagSearchResult.  # noqa: E501
        :rtype: EntityReference_
        """
        return self._ogid

    @ogid.setter
    def ogid(self, ogid):
        """Sets the ogid of this TagSearchResult.

        Gets or sets link to the OG where the Tag belongs to.  # noqa: E501

        :param ogid: The ogid of this TagSearchResult.  # noqa: E501
        :type: EntityReference_
        """

        self._ogid = ogid

    @property
    def tags(self):
        """Gets the tags of this TagSearchResult.  # noqa: E501

        Gets or sets list of OG Tags resulted in the search operation.  # noqa: E501

        :return: The tags of this TagSearchResult.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TagSearchResult.

        Gets or sets list of OG Tags resulted in the search operation.  # noqa: E501

        :param tags: The tags of this TagSearchResult.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def page(self):
        """Gets the page of this TagSearchResult.  # noqa: E501


        :return: The page of this TagSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this TagSearchResult.


        :param page: The page of this TagSearchResult.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this TagSearchResult.  # noqa: E501


        :return: The page_size of this TagSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this TagSearchResult.


        :param page_size: The page_size of this TagSearchResult.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total(self):
        """Gets the total of this TagSearchResult.  # noqa: E501


        :return: The total of this TagSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TagSearchResult.


        :param total: The total of this TagSearchResult.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(TagSearchResult, dict):
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
        if not isinstance(other, TagSearchResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TagSearchResult):
            return True

        return self.to_dict() != other.to_dict()
