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


class MaintainProductInputModel(object):
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
        'product': 'MaintainProductModel_'
    }

    attribute_map = {
        'maintain_general_input': 'MaintainGeneralInput',
        'product': 'Product'
    }

    def __init__(self, maintain_general_input=None, product=None, _configuration=None):  # noqa: E501
        """MaintainProductInputModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._maintain_general_input = None
        self._product = None
        self.discriminator = None

        if maintain_general_input is not None:
            self.maintain_general_input = maintain_general_input
        if product is not None:
            self.product = product

    @property
    def maintain_general_input(self):
        """Gets the maintain_general_input of this MaintainProductInputModel.  # noqa: E501

        Gets or sets the maintain general input.  # noqa: E501

        :return: The maintain_general_input of this MaintainProductInputModel.  # noqa: E501
        :rtype: MaintainGeneralAPIModel_
        """
        return self._maintain_general_input

    @maintain_general_input.setter
    def maintain_general_input(self, maintain_general_input):
        """Sets the maintain_general_input of this MaintainProductInputModel.

        Gets or sets the maintain general input.  # noqa: E501

        :param maintain_general_input: The maintain_general_input of this MaintainProductInputModel.  # noqa: E501
        :type: MaintainGeneralAPIModel_
        """

        self._maintain_general_input = maintain_general_input

    @property
    def product(self):
        """Gets the product of this MaintainProductInputModel.  # noqa: E501

        Gets or sets the product.  # noqa: E501

        :return: The product of this MaintainProductInputModel.  # noqa: E501
        :rtype: MaintainProductModel_
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this MaintainProductInputModel.

        Gets or sets the product.  # noqa: E501

        :param product: The product of this MaintainProductInputModel.  # noqa: E501
        :type: MaintainProductModel_
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
        if issubclass(MaintainProductInputModel, dict):
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
        if not isinstance(other, MaintainProductInputModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MaintainProductInputModel):
            return True

        return self.to_dict() != other.to_dict()
