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


class RelayServerBulkResponseModel(object):
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
        'created': 'list[RelayServerModel]',
        'total_items': 'int',
        'accepted_items': 'int',
        'failed_items': 'int',
        'faults': 'Faults_'
    }

    attribute_map = {
        'created': 'Created',
        'total_items': 'TotalItems',
        'accepted_items': 'AcceptedItems',
        'failed_items': 'FailedItems',
        'faults': 'Faults'
    }

    def __init__(self, created=None, total_items=None, accepted_items=None, failed_items=None, faults=None, _configuration=None):  # noqa: E501
        """RelayServerBulkResponseModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._total_items = None
        self._accepted_items = None
        self._failed_items = None
        self._faults = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if total_items is not None:
            self.total_items = total_items
        if accepted_items is not None:
            self.accepted_items = accepted_items
        if failed_items is not None:
            self.failed_items = failed_items
        if faults is not None:
            self.faults = faults

    @property
    def created(self):
        """Gets the created of this RelayServerBulkResponseModel.  # noqa: E501

        Gets or sets id and Name of created relay servers.  # noqa: E501

        :return: The created of this RelayServerBulkResponseModel.  # noqa: E501
        :rtype: list[RelayServerModel]
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this RelayServerBulkResponseModel.

        Gets or sets id and Name of created relay servers.  # noqa: E501

        :param created: The created of this RelayServerBulkResponseModel.  # noqa: E501
        :type: list[RelayServerModel]
        """

        self._created = created

    @property
    def total_items(self):
        """Gets the total_items of this RelayServerBulkResponseModel.  # noqa: E501

        Gets or sets total Items count sent for processing.  # noqa: E501

        :return: The total_items of this RelayServerBulkResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this RelayServerBulkResponseModel.

        Gets or sets total Items count sent for processing.  # noqa: E501

        :param total_items: The total_items of this RelayServerBulkResponseModel.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def accepted_items(self):
        """Gets the accepted_items of this RelayServerBulkResponseModel.  # noqa: E501

        Gets or sets item count accepted for processing.  # noqa: E501

        :return: The accepted_items of this RelayServerBulkResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._accepted_items

    @accepted_items.setter
    def accepted_items(self, accepted_items):
        """Sets the accepted_items of this RelayServerBulkResponseModel.

        Gets or sets item count accepted for processing.  # noqa: E501

        :param accepted_items: The accepted_items of this RelayServerBulkResponseModel.  # noqa: E501
        :type: int
        """

        self._accepted_items = accepted_items

    @property
    def failed_items(self):
        """Gets the failed_items of this RelayServerBulkResponseModel.  # noqa: E501

        Gets or sets item count not accepted for processing.  # noqa: E501

        :return: The failed_items of this RelayServerBulkResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._failed_items

    @failed_items.setter
    def failed_items(self, failed_items):
        """Sets the failed_items of this RelayServerBulkResponseModel.

        Gets or sets item count not accepted for processing.  # noqa: E501

        :param failed_items: The failed_items of this RelayServerBulkResponseModel.  # noqa: E501
        :type: int
        """

        self._failed_items = failed_items

    @property
    def faults(self):
        """Gets the faults of this RelayServerBulkResponseModel.  # noqa: E501

        Gets or sets details of the error.  # noqa: E501

        :return: The faults of this RelayServerBulkResponseModel.  # noqa: E501
        :rtype: Faults_
        """
        return self._faults

    @faults.setter
    def faults(self, faults):
        """Sets the faults of this RelayServerBulkResponseModel.

        Gets or sets details of the error.  # noqa: E501

        :param faults: The faults of this RelayServerBulkResponseModel.  # noqa: E501
        :type: Faults_
        """

        self._faults = faults

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
        if issubclass(RelayServerBulkResponseModel, dict):
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
        if not isinstance(other, RelayServerBulkResponseModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelayServerBulkResponseModel):
            return True

        return self.to_dict() != other.to_dict()