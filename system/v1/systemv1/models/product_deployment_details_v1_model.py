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


class ProductDeploymentDetailsV1Model(object):
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
        'historical_data': 'list[ProductHistoricalDataV1Model]',
        'product_status_detail': 'ProductStatusV1Model'
    }

    attribute_map = {
        'historical_data': 'historicalData',
        'product_status_detail': 'productStatusDetail'
    }

    def __init__(self, historical_data=None, product_status_detail=None, _configuration=None):  # noqa: E501
        """ProductDeploymentDetailsV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._historical_data = None
        self._product_status_detail = None
        self.discriminator = None

        if historical_data is not None:
            self.historical_data = historical_data
        if product_status_detail is not None:
            self.product_status_detail = product_status_detail

    @property
    def historical_data(self):
        """Gets the historical_data of this ProductDeploymentDetailsV1Model.  # noqa: E501

        Deployment trend details for the product  # noqa: E501

        :return: The historical_data of this ProductDeploymentDetailsV1Model.  # noqa: E501
        :rtype: list[ProductHistoricalDataV1Model]
        """
        return self._historical_data

    @historical_data.setter
    def historical_data(self, historical_data):
        """Sets the historical_data of this ProductDeploymentDetailsV1Model.

        Deployment trend details for the product  # noqa: E501

        :param historical_data: The historical_data of this ProductDeploymentDetailsV1Model.  # noqa: E501
        :type: list[ProductHistoricalDataV1Model]
        """

        self._historical_data = historical_data

    @property
    def product_status_detail(self):
        """Gets the product_status_detail of this ProductDeploymentDetailsV1Model.  # noqa: E501

        product deployment status detail  # noqa: E501

        :return: The product_status_detail of this ProductDeploymentDetailsV1Model.  # noqa: E501
        :rtype: ProductStatusV1Model
        """
        return self._product_status_detail

    @product_status_detail.setter
    def product_status_detail(self, product_status_detail):
        """Sets the product_status_detail of this ProductDeploymentDetailsV1Model.

        product deployment status detail  # noqa: E501

        :param product_status_detail: The product_status_detail of this ProductDeploymentDetailsV1Model.  # noqa: E501
        :type: ProductStatusV1Model
        """

        self._product_status_detail = product_status_detail

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
        if issubclass(ProductDeploymentDetailsV1Model, dict):
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
        if not isinstance(other, ProductDeploymentDetailsV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductDeploymentDetailsV1Model):
            return True

        return self.to_dict() != other.to_dict()
