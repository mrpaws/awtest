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


class ProductSetInquiryResponseModel(object):
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
        'product_set_id': 'int',
        'product_set_name': 'str',
        'location_group_id': 'int',
        'products': 'list[ProductInquiryResponseModel]'
    }

    attribute_map = {
        'product_set_id': 'ProductSetID',
        'product_set_name': 'ProductSetName',
        'location_group_id': 'LocationGroupID',
        'products': 'Products'
    }

    def __init__(self, product_set_id=None, product_set_name=None, location_group_id=None, products=None, _configuration=None):  # noqa: E501
        """ProductSetInquiryResponseModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_set_id = None
        self._product_set_name = None
        self._location_group_id = None
        self._products = None
        self.discriminator = None

        if product_set_id is not None:
            self.product_set_id = product_set_id
        if product_set_name is not None:
            self.product_set_name = product_set_name
        if location_group_id is not None:
            self.location_group_id = location_group_id
        if products is not None:
            self.products = products

    @property
    def product_set_id(self):
        """Gets the product_set_id of this ProductSetInquiryResponseModel.  # noqa: E501

        Gets or sets iD of the Product Set.  # noqa: E501

        :return: The product_set_id of this ProductSetInquiryResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._product_set_id

    @product_set_id.setter
    def product_set_id(self, product_set_id):
        """Sets the product_set_id of this ProductSetInquiryResponseModel.

        Gets or sets iD of the Product Set.  # noqa: E501

        :param product_set_id: The product_set_id of this ProductSetInquiryResponseModel.  # noqa: E501
        :type: int
        """

        self._product_set_id = product_set_id

    @property
    def product_set_name(self):
        """Gets the product_set_name of this ProductSetInquiryResponseModel.  # noqa: E501

        Gets or sets name of the Product Set.  # noqa: E501

        :return: The product_set_name of this ProductSetInquiryResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._product_set_name

    @product_set_name.setter
    def product_set_name(self, product_set_name):
        """Sets the product_set_name of this ProductSetInquiryResponseModel.

        Gets or sets name of the Product Set.  # noqa: E501

        :param product_set_name: The product_set_name of this ProductSetInquiryResponseModel.  # noqa: E501
        :type: str
        """

        self._product_set_name = product_set_name

    @property
    def location_group_id(self):
        """Gets the location_group_id of this ProductSetInquiryResponseModel.  # noqa: E501

        Gets or sets iD of the Organization Group to which the Product Set belong.  # noqa: E501

        :return: The location_group_id of this ProductSetInquiryResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._location_group_id

    @location_group_id.setter
    def location_group_id(self, location_group_id):
        """Sets the location_group_id of this ProductSetInquiryResponseModel.

        Gets or sets iD of the Organization Group to which the Product Set belong.  # noqa: E501

        :param location_group_id: The location_group_id of this ProductSetInquiryResponseModel.  # noqa: E501
        :type: int
        """

        self._location_group_id = location_group_id

    @property
    def products(self):
        """Gets the products of this ProductSetInquiryResponseModel.  # noqa: E501

        Gets or sets details of all products in the Product Set.  # noqa: E501

        :return: The products of this ProductSetInquiryResponseModel.  # noqa: E501
        :rtype: list[ProductInquiryResponseModel]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this ProductSetInquiryResponseModel.

        Gets or sets details of all products in the Product Set.  # noqa: E501

        :param products: The products of this ProductSetInquiryResponseModel.  # noqa: E501
        :type: list[ProductInquiryResponseModel]
        """

        self._products = products

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
        if issubclass(ProductSetInquiryResponseModel, dict):
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
        if not isinstance(other, ProductSetInquiryResponseModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductSetInquiryResponseModel):
            return True

        return self.to_dict() != other.to_dict()
