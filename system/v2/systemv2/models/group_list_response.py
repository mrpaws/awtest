# coding: utf-8

"""
    System API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv2.configuration import Configuration


class GroupListResponse(object):
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
        'schemas': 'list[str]',
        'total_results': 'int',
        'resources': 'list[GroupResponse]',
        'start_index': 'int',
        'items_per_page': 'int'
    }

    attribute_map = {
        'schemas': 'schemas',
        'total_results': 'totalResults',
        'resources': 'Resources',
        'start_index': 'startIndex',
        'items_per_page': 'itemsPerPage'
    }

    def __init__(self, schemas=None, total_results=None, resources=None, start_index=None, items_per_page=None, _configuration=None):  # noqa: E501
        """GroupListResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._schemas = None
        self._total_results = None
        self._resources = None
        self._start_index = None
        self._items_per_page = None
        self.discriminator = None

        if schemas is not None:
            self.schemas = schemas
        if total_results is not None:
            self.total_results = total_results
        if resources is not None:
            self.resources = resources
        if start_index is not None:
            self.start_index = start_index
        if items_per_page is not None:
            self.items_per_page = items_per_page

    @property
    def schemas(self):
        """Gets the schemas of this GroupListResponse.  # noqa: E501

        Schemas used to compose a group list response.  # noqa: E501

        :return: The schemas of this GroupListResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this GroupListResponse.

        Schemas used to compose a group list response.  # noqa: E501

        :param schemas: The schemas of this GroupListResponse.  # noqa: E501
        :type: list[str]
        """

        self._schemas = schemas

    @property
    def total_results(self):
        """Gets the total_results of this GroupListResponse.  # noqa: E501

        The total number of results returned by the list or query operation.  # noqa: E501

        :return: The total_results of this GroupListResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this GroupListResponse.

        The total number of results returned by the list or query operation.  # noqa: E501

        :param total_results: The total_results of this GroupListResponse.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

    @property
    def resources(self):
        """Gets the resources of this GroupListResponse.  # noqa: E501

        A multi-valued list of groups.  # noqa: E501

        :return: The resources of this GroupListResponse.  # noqa: E501
        :rtype: list[GroupResponse]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this GroupListResponse.

        A multi-valued list of groups.  # noqa: E501

        :param resources: The resources of this GroupListResponse.  # noqa: E501
        :type: list[GroupResponse]
        """

        self._resources = resources

    @property
    def start_index(self):
        """Gets the start_index of this GroupListResponse.  # noqa: E501

        The 1-based index of the first result in the current list of groups.  # noqa: E501

        :return: The start_index of this GroupListResponse.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this GroupListResponse.

        The 1-based index of the first result in the current list of groups.  # noqa: E501

        :param start_index: The start_index of this GroupListResponse.  # noqa: E501
        :type: int
        """

        self._start_index = start_index

    @property
    def items_per_page(self):
        """Gets the items_per_page of this GroupListResponse.  # noqa: E501

        The number of groups returned.  # noqa: E501

        :return: The items_per_page of this GroupListResponse.  # noqa: E501
        :rtype: int
        """
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, items_per_page):
        """Sets the items_per_page of this GroupListResponse.

        The number of groups returned.  # noqa: E501

        :param items_per_page: The items_per_page of this GroupListResponse.  # noqa: E501
        :type: int
        """

        self._items_per_page = items_per_page

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
        if issubclass(GroupListResponse, dict):
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
        if not isinstance(other, GroupListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupListResponse):
            return True

        return self.to_dict() != other.to_dict()
