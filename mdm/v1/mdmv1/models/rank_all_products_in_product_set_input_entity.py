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


class RankAllProductsInProductSetInputEntity(object):
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
        'location_group_id': 'int',
        'product_set_name': 'str',
        'product_set_id': 'int',
        'product_ranks': 'list[MaintainProductRank]'
    }

    attribute_map = {
        'location_group_id': 'LocationGroupID',
        'product_set_name': 'ProductSetName',
        'product_set_id': 'ProductSetID',
        'product_ranks': 'ProductRanks'
    }

    def __init__(self, location_group_id=None, product_set_name=None, product_set_id=None, product_ranks=None, _configuration=None):  # noqa: E501
        """RankAllProductsInProductSetInputEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._location_group_id = None
        self._product_set_name = None
        self._product_set_id = None
        self._product_ranks = None
        self.discriminator = None

        if location_group_id is not None:
            self.location_group_id = location_group_id
        if product_set_name is not None:
            self.product_set_name = product_set_name
        if product_set_id is not None:
            self.product_set_id = product_set_id
        if product_ranks is not None:
            self.product_ranks = product_ranks

    @property
    def location_group_id(self):
        """Gets the location_group_id of this RankAllProductsInProductSetInputEntity.  # noqa: E501

        Gets or sets iD of the Location Group to which Product Set belong.  # noqa: E501

        :return: The location_group_id of this RankAllProductsInProductSetInputEntity.  # noqa: E501
        :rtype: int
        """
        return self._location_group_id

    @location_group_id.setter
    def location_group_id(self, location_group_id):
        """Sets the location_group_id of this RankAllProductsInProductSetInputEntity.

        Gets or sets iD of the Location Group to which Product Set belong.  # noqa: E501

        :param location_group_id: The location_group_id of this RankAllProductsInProductSetInputEntity.  # noqa: E501
        :type: int
        """

        self._location_group_id = location_group_id

    @property
    def product_set_name(self):
        """Gets the product_set_name of this RankAllProductsInProductSetInputEntity.  # noqa: E501

        Gets or sets name of the Product Set.  # noqa: E501

        :return: The product_set_name of this RankAllProductsInProductSetInputEntity.  # noqa: E501
        :rtype: str
        """
        return self._product_set_name

    @product_set_name.setter
    def product_set_name(self, product_set_name):
        """Sets the product_set_name of this RankAllProductsInProductSetInputEntity.

        Gets or sets name of the Product Set.  # noqa: E501

        :param product_set_name: The product_set_name of this RankAllProductsInProductSetInputEntity.  # noqa: E501
        :type: str
        """

        self._product_set_name = product_set_name

    @property
    def product_set_id(self):
        """Gets the product_set_id of this RankAllProductsInProductSetInputEntity.  # noqa: E501

        Gets or sets iD of the Product Set.  # noqa: E501

        :return: The product_set_id of this RankAllProductsInProductSetInputEntity.  # noqa: E501
        :rtype: int
        """
        return self._product_set_id

    @product_set_id.setter
    def product_set_id(self, product_set_id):
        """Sets the product_set_id of this RankAllProductsInProductSetInputEntity.

        Gets or sets iD of the Product Set.  # noqa: E501

        :param product_set_id: The product_set_id of this RankAllProductsInProductSetInputEntity.  # noqa: E501
        :type: int
        """

        self._product_set_id = product_set_id

    @property
    def product_ranks(self):
        """Gets the product_ranks of this RankAllProductsInProductSetInputEntity.  # noqa: E501

        Gets or sets ranks details of the products in the Product Set.  # noqa: E501

        :return: The product_ranks of this RankAllProductsInProductSetInputEntity.  # noqa: E501
        :rtype: list[MaintainProductRank]
        """
        return self._product_ranks

    @product_ranks.setter
    def product_ranks(self, product_ranks):
        """Sets the product_ranks of this RankAllProductsInProductSetInputEntity.

        Gets or sets ranks details of the products in the Product Set.  # noqa: E501

        :param product_ranks: The product_ranks of this RankAllProductsInProductSetInputEntity.  # noqa: E501
        :type: list[MaintainProductRank]
        """

        self._product_ranks = product_ranks

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
        if issubclass(RankAllProductsInProductSetInputEntity, dict):
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
        if not isinstance(other, RankAllProductsInProductSetInputEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RankAllProductsInProductSetInputEntity):
            return True

        return self.to_dict() != other.to_dict()
