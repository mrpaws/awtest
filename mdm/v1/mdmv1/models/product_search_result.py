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


class ProductSearchResult(object):
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
        'products': 'list[ProductModel_]',
        'page': 'int',
        'page_size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'products': 'Products',
        'page': 'Page',
        'page_size': 'PageSize',
        'total': 'Total'
    }

    def __init__(self, products=None, page=None, page_size=None, total=None, _configuration=None):  # noqa: E501
        """ProductSearchResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._products = None
        self._page = None
        self._page_size = None
        self._total = None
        self.discriminator = None

        if products is not None:
            self.products = products
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total is not None:
            self.total = total

    @property
    def products(self):
        """Gets the products of this ProductSearchResult.  # noqa: E501

        Gets or sets list of Product details resulted in the search operation.  # noqa: E501

        :return: The products of this ProductSearchResult.  # noqa: E501
        :rtype: list[ProductModel_]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this ProductSearchResult.

        Gets or sets list of Product details resulted in the search operation.  # noqa: E501

        :param products: The products of this ProductSearchResult.  # noqa: E501
        :type: list[ProductModel_]
        """

        self._products = products

    @property
    def page(self):
        """Gets the page of this ProductSearchResult.  # noqa: E501

        Gets or sets the result set page index.  # noqa: E501

        :return: The page of this ProductSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ProductSearchResult.

        Gets or sets the result set page index.  # noqa: E501

        :param page: The page of this ProductSearchResult.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ProductSearchResult.  # noqa: E501

        Gets or sets the  result set page size.  # noqa: E501

        :return: The page_size of this ProductSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ProductSearchResult.

        Gets or sets the  result set page size.  # noqa: E501

        :param page_size: The page_size of this ProductSearchResult.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total(self):
        """Gets the total of this ProductSearchResult.  # noqa: E501

        Gets or sets the  total number of results.  # noqa: E501

        :return: The total of this ProductSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ProductSearchResult.

        Gets or sets the  total number of results.  # noqa: E501

        :param total: The total of this ProductSearchResult.  # noqa: E501
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
        if issubclass(ProductSearchResult, dict):
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
        if not isinstance(other, ProductSearchResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductSearchResult):
            return True

        return self.to_dict() != other.to_dict()
