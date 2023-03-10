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


class UsersBatchesV1ResultModel(object):
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
        'search_result': 'list[UsersBatchesV1Model]',
        'total_records': 'int'
    }

    attribute_map = {
        'search_result': 'search_result',
        'total_records': 'total_records'
    }

    def __init__(self, search_result=None, total_records=None, _configuration=None):  # noqa: E501
        """UsersBatchesV1ResultModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._search_result = None
        self._total_records = None
        self.discriminator = None

        if search_result is not None:
            self.search_result = search_result
        if total_records is not None:
            self.total_records = total_records

    @property
    def search_result(self):
        """Gets the search_result of this UsersBatchesV1ResultModel.  # noqa: E501

        List of users batches that match the search criteria.  # noqa: E501

        :return: The search_result of this UsersBatchesV1ResultModel.  # noqa: E501
        :rtype: list[UsersBatchesV1Model]
        """
        return self._search_result

    @search_result.setter
    def search_result(self, search_result):
        """Sets the search_result of this UsersBatchesV1ResultModel.

        List of users batches that match the search criteria.  # noqa: E501

        :param search_result: The search_result of this UsersBatchesV1ResultModel.  # noqa: E501
        :type: list[UsersBatchesV1Model]
        """

        self._search_result = search_result

    @property
    def total_records(self):
        """Gets the total_records of this UsersBatchesV1ResultModel.  # noqa: E501

        Total number of batches that match the search criteria.  # noqa: E501

        :return: The total_records of this UsersBatchesV1ResultModel.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this UsersBatchesV1ResultModel.

        Total number of batches that match the search criteria.  # noqa: E501

        :param total_records: The total_records of this UsersBatchesV1ResultModel.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

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
        if issubclass(UsersBatchesV1ResultModel, dict):
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
        if not isinstance(other, UsersBatchesV1ResultModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsersBatchesV1ResultModel):
            return True

        return self.to_dict() != other.to_dict()
