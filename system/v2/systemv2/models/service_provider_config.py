# coding: utf-8

"""
    System API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv2.configuration import Configuration


class ServiceProviderConfig(object):
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
        'bulk': 'BulkFeature',
        'change_password': 'ChangePasswordFeature',
        'etag': 'ETagFeature',
        'filter': 'FilterFeature',
        'patch': 'PatchFeature',
        'schemas': 'list[str]',
        'sort': 'SortFeature'
    }

    attribute_map = {
        'bulk': 'bulk',
        'change_password': 'changePassword',
        'etag': 'etag',
        'filter': 'filter',
        'patch': 'patch',
        'schemas': 'schemas',
        'sort': 'sort'
    }

    def __init__(self, bulk=None, change_password=None, etag=None, filter=None, patch=None, schemas=None, sort=None, _configuration=None):  # noqa: E501
        """ServiceProviderConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bulk = None
        self._change_password = None
        self._etag = None
        self._filter = None
        self._patch = None
        self._schemas = None
        self._sort = None
        self.discriminator = None

        self.bulk = bulk
        self.change_password = change_password
        self.etag = etag
        self.filter = filter
        if patch is not None:
            self.patch = patch
        self.schemas = schemas
        self.sort = sort

    @property
    def bulk(self):
        """Gets the bulk of this ServiceProviderConfig.  # noqa: E501

          # noqa: E501

        :return: The bulk of this ServiceProviderConfig.  # noqa: E501
        :rtype: BulkFeature
        """
        return self._bulk

    @bulk.setter
    def bulk(self, bulk):
        """Sets the bulk of this ServiceProviderConfig.

          # noqa: E501

        :param bulk: The bulk of this ServiceProviderConfig.  # noqa: E501
        :type: BulkFeature
        """
        if self._configuration.client_side_validation and bulk is None:
            raise ValueError("Invalid value for `bulk`, must not be `None`")  # noqa: E501

        self._bulk = bulk

    @property
    def change_password(self):
        """Gets the change_password of this ServiceProviderConfig.  # noqa: E501

          # noqa: E501

        :return: The change_password of this ServiceProviderConfig.  # noqa: E501
        :rtype: ChangePasswordFeature
        """
        return self._change_password

    @change_password.setter
    def change_password(self, change_password):
        """Sets the change_password of this ServiceProviderConfig.

          # noqa: E501

        :param change_password: The change_password of this ServiceProviderConfig.  # noqa: E501
        :type: ChangePasswordFeature
        """
        if self._configuration.client_side_validation and change_password is None:
            raise ValueError("Invalid value for `change_password`, must not be `None`")  # noqa: E501

        self._change_password = change_password

    @property
    def etag(self):
        """Gets the etag of this ServiceProviderConfig.  # noqa: E501

          # noqa: E501

        :return: The etag of this ServiceProviderConfig.  # noqa: E501
        :rtype: ETagFeature
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this ServiceProviderConfig.

          # noqa: E501

        :param etag: The etag of this ServiceProviderConfig.  # noqa: E501
        :type: ETagFeature
        """
        if self._configuration.client_side_validation and etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")  # noqa: E501

        self._etag = etag

    @property
    def filter(self):
        """Gets the filter of this ServiceProviderConfig.  # noqa: E501

          # noqa: E501

        :return: The filter of this ServiceProviderConfig.  # noqa: E501
        :rtype: FilterFeature
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ServiceProviderConfig.

          # noqa: E501

        :param filter: The filter of this ServiceProviderConfig.  # noqa: E501
        :type: FilterFeature
        """
        if self._configuration.client_side_validation and filter is None:
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501

        self._filter = filter

    @property
    def patch(self):
        """Gets the patch of this ServiceProviderConfig.  # noqa: E501

          # noqa: E501

        :return: The patch of this ServiceProviderConfig.  # noqa: E501
        :rtype: PatchFeature
        """
        return self._patch

    @patch.setter
    def patch(self, patch):
        """Sets the patch of this ServiceProviderConfig.

          # noqa: E501

        :param patch: The patch of this ServiceProviderConfig.  # noqa: E501
        :type: PatchFeature
        """

        self._patch = patch

    @property
    def schemas(self):
        """Gets the schemas of this ServiceProviderConfig.  # noqa: E501

          # noqa: E501

        :return: The schemas of this ServiceProviderConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this ServiceProviderConfig.

          # noqa: E501

        :param schemas: The schemas of this ServiceProviderConfig.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and schemas is None:
            raise ValueError("Invalid value for `schemas`, must not be `None`")  # noqa: E501

        self._schemas = schemas

    @property
    def sort(self):
        """Gets the sort of this ServiceProviderConfig.  # noqa: E501

          # noqa: E501

        :return: The sort of this ServiceProviderConfig.  # noqa: E501
        :rtype: SortFeature
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ServiceProviderConfig.

          # noqa: E501

        :param sort: The sort of this ServiceProviderConfig.  # noqa: E501
        :type: SortFeature
        """
        if self._configuration.client_side_validation and sort is None:
            raise ValueError("Invalid value for `sort`, must not be `None`")  # noqa: E501

        self._sort = sort

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
        if issubclass(ServiceProviderConfig, dict):
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
        if not isinstance(other, ServiceProviderConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceProviderConfig):
            return True

        return self.to_dict() != other.to_dict()
