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


class ProductLicenseResponseV1Model(object):
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
        'licenses': 'list[ProductLicenseV1Model]',
        'total_count': 'int'
    }

    attribute_map = {
        'licenses': 'licenses',
        'total_count': 'total_count'
    }

    def __init__(self, licenses=None, total_count=None, _configuration=None):  # noqa: E501
        """ProductLicenseResponseV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._licenses = None
        self._total_count = None
        self.discriminator = None

        self.licenses = licenses
        self.total_count = total_count

    @property
    def licenses(self):
        """Gets the licenses of this ProductLicenseResponseV1Model.  # noqa: E501

          # noqa: E501

        :return: The licenses of this ProductLicenseResponseV1Model.  # noqa: E501
        :rtype: list[ProductLicenseV1Model]
        """
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        """Sets the licenses of this ProductLicenseResponseV1Model.

          # noqa: E501

        :param licenses: The licenses of this ProductLicenseResponseV1Model.  # noqa: E501
        :type: list[ProductLicenseV1Model]
        """
        if self._configuration.client_side_validation and licenses is None:
            raise ValueError("Invalid value for `licenses`, must not be `None`")  # noqa: E501

        self._licenses = licenses

    @property
    def total_count(self):
        """Gets the total_count of this ProductLicenseResponseV1Model.  # noqa: E501

        The total number of licensed products in the results.  # noqa: E501

        :return: The total_count of this ProductLicenseResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ProductLicenseResponseV1Model.

        The total number of licensed products in the results.  # noqa: E501

        :param total_count: The total_count of this ProductLicenseResponseV1Model.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

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
        if issubclass(ProductLicenseResponseV1Model, dict):
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
        if not isinstance(other, ProductLicenseResponseV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductLicenseResponseV1Model):
            return True

        return self.to_dict() != other.to_dict()
