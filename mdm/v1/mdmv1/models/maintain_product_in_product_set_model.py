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


class MaintainProductInProductSetModel(object):
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
        'product_set_id': 'int',
        'product_rank': 'MaintainProductRankModel_',
        'product': 'MaintainProduct_'
    }

    attribute_map = {
        'maintain_general_input': 'MaintainGeneralInput',
        'name': 'Name',
        'product_set_id': 'ProductSetID',
        'product_rank': 'ProductRank',
        'product': 'Product'
    }

    def __init__(self, maintain_general_input=None, name=None, product_set_id=None, product_rank=None, product=None, _configuration=None):  # noqa: E501
        """MaintainProductInProductSetModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._maintain_general_input = None
        self._name = None
        self._product_set_id = None
        self._product_rank = None
        self._product = None
        self.discriminator = None

        if maintain_general_input is not None:
            self.maintain_general_input = maintain_general_input
        if name is not None:
            self.name = name
        if product_set_id is not None:
            self.product_set_id = product_set_id
        if product_rank is not None:
            self.product_rank = product_rank
        if product is not None:
            self.product = product

    @property
    def maintain_general_input(self):
        """Gets the maintain_general_input of this MaintainProductInProductSetModel.  # noqa: E501

        Gets or sets maintainGeneralInput.  # noqa: E501

        :return: The maintain_general_input of this MaintainProductInProductSetModel.  # noqa: E501
        :rtype: MaintainGeneralAPIModel_
        """
        return self._maintain_general_input

    @maintain_general_input.setter
    def maintain_general_input(self, maintain_general_input):
        """Sets the maintain_general_input of this MaintainProductInProductSetModel.

        Gets or sets maintainGeneralInput.  # noqa: E501

        :param maintain_general_input: The maintain_general_input of this MaintainProductInProductSetModel.  # noqa: E501
        :type: MaintainGeneralAPIModel_
        """

        self._maintain_general_input = maintain_general_input

    @property
    def name(self):
        """Gets the name of this MaintainProductInProductSetModel.  # noqa: E501

        Gets or sets name.  # noqa: E501

        :return: The name of this MaintainProductInProductSetModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MaintainProductInProductSetModel.

        Gets or sets name.  # noqa: E501

        :param name: The name of this MaintainProductInProductSetModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def product_set_id(self):
        """Gets the product_set_id of this MaintainProductInProductSetModel.  # noqa: E501

        Gets or sets productSetID.  # noqa: E501

        :return: The product_set_id of this MaintainProductInProductSetModel.  # noqa: E501
        :rtype: int
        """
        return self._product_set_id

    @product_set_id.setter
    def product_set_id(self, product_set_id):
        """Sets the product_set_id of this MaintainProductInProductSetModel.

        Gets or sets productSetID.  # noqa: E501

        :param product_set_id: The product_set_id of this MaintainProductInProductSetModel.  # noqa: E501
        :type: int
        """

        self._product_set_id = product_set_id

    @property
    def product_rank(self):
        """Gets the product_rank of this MaintainProductInProductSetModel.  # noqa: E501

        Gets or sets rank.  # noqa: E501

        :return: The product_rank of this MaintainProductInProductSetModel.  # noqa: E501
        :rtype: MaintainProductRankModel_
        """
        return self._product_rank

    @product_rank.setter
    def product_rank(self, product_rank):
        """Sets the product_rank of this MaintainProductInProductSetModel.

        Gets or sets rank.  # noqa: E501

        :param product_rank: The product_rank of this MaintainProductInProductSetModel.  # noqa: E501
        :type: MaintainProductRankModel_
        """

        self._product_rank = product_rank

    @property
    def product(self):
        """Gets the product of this MaintainProductInProductSetModel.  # noqa: E501

        Gets or sets product.  # noqa: E501

        :return: The product of this MaintainProductInProductSetModel.  # noqa: E501
        :rtype: MaintainProduct_
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this MaintainProductInProductSetModel.

        Gets or sets product.  # noqa: E501

        :param product: The product of this MaintainProductInProductSetModel.  # noqa: E501
        :type: MaintainProduct_
        """

        self._product = product

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
        if issubclass(MaintainProductInProductSetModel, dict):
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
        if not isinstance(other, MaintainProductInProductSetModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MaintainProductInProductSetModel):
            return True

        return self.to_dict() != other.to_dict()