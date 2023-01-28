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


class SearchResult11(object):
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
        'search_results': 'list[ScriptResourceLite]',
        'record_count': 'int'
    }

    attribute_map = {
        'search_results': 'SearchResults',
        'record_count': 'RecordCount'
    }

    def __init__(self, search_results=None, record_count=None, _configuration=None):  # noqa: E501
        """SearchResult11 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._search_results = None
        self._record_count = None
        self.discriminator = None

        if search_results is not None:
            self.search_results = search_results
        if record_count is not None:
            self.record_count = record_count

    @property
    def search_results(self):
        """Gets the search_results of this SearchResult11.  # noqa: E501


        :return: The search_results of this SearchResult11.  # noqa: E501
        :rtype: list[ScriptResourceLite]
        """
        return self._search_results

    @search_results.setter
    def search_results(self, search_results):
        """Sets the search_results of this SearchResult11.


        :param search_results: The search_results of this SearchResult11.  # noqa: E501
        :type: list[ScriptResourceLite]
        """

        self._search_results = search_results

    @property
    def record_count(self):
        """Gets the record_count of this SearchResult11.  # noqa: E501


        :return: The record_count of this SearchResult11.  # noqa: E501
        :rtype: int
        """
        return self._record_count

    @record_count.setter
    def record_count(self, record_count):
        """Sets the record_count of this SearchResult11.


        :param record_count: The record_count of this SearchResult11.  # noqa: E501
        :type: int
        """

        self._record_count = record_count

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
        if issubclass(SearchResult11, dict):
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
        if not isinstance(other, SearchResult11):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchResult11):
            return True

        return self.to_dict() != other.to_dict()
