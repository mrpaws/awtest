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


class MaintainProductSetModel(object):
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
        'maintain_general_input': 'MaintainGeneralAPIModel_',
        'name': 'str',
        'description': 'str',
        'platform_id': 'int',
        'product_ranks': 'list[MaintainProductRankModel]',
        'products': 'list[MaintainProduct]'
    }

    attribute_map = {
        'maintain_general_input': 'MaintainGeneralInput',
        'name': 'Name',
        'description': 'Description',
        'platform_id': 'PlatformID',
        'product_ranks': 'ProductRanks',
        'products': 'Products'
    }

    def __init__(self, maintain_general_input=None, name=None, description=None, platform_id=None, product_ranks=None, products=None, _configuration=None):  # noqa: E501
        """MaintainProductSetModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._maintain_general_input = None
        self._name = None
        self._description = None
        self._platform_id = None
        self._product_ranks = None
        self._products = None
        self.discriminator = None

        if maintain_general_input is not None:
            self.maintain_general_input = maintain_general_input
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if platform_id is not None:
            self.platform_id = platform_id
        if product_ranks is not None:
            self.product_ranks = product_ranks
        if products is not None:
            self.products = products

    @property
    def maintain_general_input(self):
        """Gets the maintain_general_input of this MaintainProductSetModel.  # noqa: E501

        Gets or sets maintaint General API Model.  # noqa: E501

        :return: The maintain_general_input of this MaintainProductSetModel.  # noqa: E501
        :rtype: MaintainGeneralAPIModel_
        """
        return self._maintain_general_input

    @maintain_general_input.setter
    def maintain_general_input(self, maintain_general_input):
        """Sets the maintain_general_input of this MaintainProductSetModel.

        Gets or sets maintaint General API Model.  # noqa: E501

        :param maintain_general_input: The maintain_general_input of this MaintainProductSetModel.  # noqa: E501
        :type: MaintainGeneralAPIModel_
        """

        self._maintain_general_input = maintain_general_input

    @property
    def name(self):
        """Gets the name of this MaintainProductSetModel.  # noqa: E501

        Gets or sets name.  # noqa: E501

        :return: The name of this MaintainProductSetModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MaintainProductSetModel.

        Gets or sets name.  # noqa: E501

        :param name: The name of this MaintainProductSetModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this MaintainProductSetModel.  # noqa: E501

        Gets or sets description.  # noqa: E501

        :return: The description of this MaintainProductSetModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MaintainProductSetModel.

        Gets or sets description.  # noqa: E501

        :param description: The description of this MaintainProductSetModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def platform_id(self):
        """Gets the platform_id of this MaintainProductSetModel.  # noqa: E501

        Gets or sets platformID.  # noqa: E501

        :return: The platform_id of this MaintainProductSetModel.  # noqa: E501
        :rtype: int
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this MaintainProductSetModel.

        Gets or sets platformID.  # noqa: E501

        :param platform_id: The platform_id of this MaintainProductSetModel.  # noqa: E501
        :type: int
        """

        self._platform_id = platform_id

    @property
    def product_ranks(self):
        """Gets the product_ranks of this MaintainProductSetModel.  # noqa: E501

        Gets or sets list of Product Ranks.  # noqa: E501

        :return: The product_ranks of this MaintainProductSetModel.  # noqa: E501
        :rtype: list[MaintainProductRankModel]
        """
        return self._product_ranks

    @product_ranks.setter
    def product_ranks(self, product_ranks):
        """Sets the product_ranks of this MaintainProductSetModel.

        Gets or sets list of Product Ranks.  # noqa: E501

        :param product_ranks: The product_ranks of this MaintainProductSetModel.  # noqa: E501
        :type: list[MaintainProductRankModel]
        """

        self._product_ranks = product_ranks

    @property
    def products(self):
        """Gets the products of this MaintainProductSetModel.  # noqa: E501

        Gets or sets list of Products.  # noqa: E501

        :return: The products of this MaintainProductSetModel.  # noqa: E501
        :rtype: list[MaintainProduct]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this MaintainProductSetModel.

        Gets or sets list of Products.  # noqa: E501

        :param products: The products of this MaintainProductSetModel.  # noqa: E501
        :type: list[MaintainProduct]
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
        if issubclass(MaintainProductSetModel, dict):
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
        if not isinstance(other, MaintainProductSetModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MaintainProductSetModel):
            return True

        return self.to_dict() != other.to_dict()