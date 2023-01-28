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


class AppContentStorageEntity(object):
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
        'application_capacity': 'str',
        'application_overage': 'str',
        'application_max_file_size': 'str',
        'content_capacity': 'str',
        'content_overage': 'str',
        'content_max_file_size': 'str'
    }

    attribute_map = {
        'application_capacity': 'ApplicationCapacity',
        'application_overage': 'ApplicationOverage',
        'application_max_file_size': 'ApplicationMaxFileSize',
        'content_capacity': 'ContentCapacity',
        'content_overage': 'ContentOverage',
        'content_max_file_size': 'ContentMaxFileSize'
    }

    def __init__(self, application_capacity=None, application_overage=None, application_max_file_size=None, content_capacity=None, content_overage=None, content_max_file_size=None, _configuration=None):  # noqa: E501
        """AppContentStorageEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_capacity = None
        self._application_overage = None
        self._application_max_file_size = None
        self._content_capacity = None
        self._content_overage = None
        self._content_max_file_size = None
        self.discriminator = None

        if application_capacity is not None:
            self.application_capacity = application_capacity
        if application_overage is not None:
            self.application_overage = application_overage
        if application_max_file_size is not None:
            self.application_max_file_size = application_max_file_size
        if content_capacity is not None:
            self.content_capacity = content_capacity
        if content_overage is not None:
            self.content_overage = content_overage
        if content_max_file_size is not None:
            self.content_max_file_size = content_max_file_size

    @property
    def application_capacity(self):
        """Gets the application_capacity of this AppContentStorageEntity.  # noqa: E501

        Gets or sets storage capacity alloted for the applications.  # noqa: E501

        :return: The application_capacity of this AppContentStorageEntity.  # noqa: E501
        :rtype: str
        """
        return self._application_capacity

    @application_capacity.setter
    def application_capacity(self, application_capacity):
        """Sets the application_capacity of this AppContentStorageEntity.

        Gets or sets storage capacity alloted for the applications.  # noqa: E501

        :param application_capacity: The application_capacity of this AppContentStorageEntity.  # noqa: E501
        :type: str
        """

        self._application_capacity = application_capacity

    @property
    def application_overage(self):
        """Gets the application_overage of this AppContentStorageEntity.  # noqa: E501

        Gets or sets overage usage associated with the application.  # noqa: E501

        :return: The application_overage of this AppContentStorageEntity.  # noqa: E501
        :rtype: str
        """
        return self._application_overage

    @application_overage.setter
    def application_overage(self, application_overage):
        """Sets the application_overage of this AppContentStorageEntity.

        Gets or sets overage usage associated with the application.  # noqa: E501

        :param application_overage: The application_overage of this AppContentStorageEntity.  # noqa: E501
        :type: str
        """

        self._application_overage = application_overage

    @property
    def application_max_file_size(self):
        """Gets the application_max_file_size of this AppContentStorageEntity.  # noqa: E501

        Gets or sets maximum file size of application that can be uploaded.  # noqa: E501

        :return: The application_max_file_size of this AppContentStorageEntity.  # noqa: E501
        :rtype: str
        """
        return self._application_max_file_size

    @application_max_file_size.setter
    def application_max_file_size(self, application_max_file_size):
        """Sets the application_max_file_size of this AppContentStorageEntity.

        Gets or sets maximum file size of application that can be uploaded.  # noqa: E501

        :param application_max_file_size: The application_max_file_size of this AppContentStorageEntity.  # noqa: E501
        :type: str
        """

        self._application_max_file_size = application_max_file_size

    @property
    def content_capacity(self):
        """Gets the content_capacity of this AppContentStorageEntity.  # noqa: E501

        Gets or sets storage capacity alloted for the Admin content.  # noqa: E501

        :return: The content_capacity of this AppContentStorageEntity.  # noqa: E501
        :rtype: str
        """
        return self._content_capacity

    @content_capacity.setter
    def content_capacity(self, content_capacity):
        """Sets the content_capacity of this AppContentStorageEntity.

        Gets or sets storage capacity alloted for the Admin content.  # noqa: E501

        :param content_capacity: The content_capacity of this AppContentStorageEntity.  # noqa: E501
        :type: str
        """

        self._content_capacity = content_capacity

    @property
    def content_overage(self):
        """Gets the content_overage of this AppContentStorageEntity.  # noqa: E501

        Gets or sets overage usage associated with the Admin content.  # noqa: E501

        :return: The content_overage of this AppContentStorageEntity.  # noqa: E501
        :rtype: str
        """
        return self._content_overage

    @content_overage.setter
    def content_overage(self, content_overage):
        """Sets the content_overage of this AppContentStorageEntity.

        Gets or sets overage usage associated with the Admin content.  # noqa: E501

        :param content_overage: The content_overage of this AppContentStorageEntity.  # noqa: E501
        :type: str
        """

        self._content_overage = content_overage

    @property
    def content_max_file_size(self):
        """Gets the content_max_file_size of this AppContentStorageEntity.  # noqa: E501

        Gets or sets maximum file size of Admin content that can be uploaded.  # noqa: E501

        :return: The content_max_file_size of this AppContentStorageEntity.  # noqa: E501
        :rtype: str
        """
        return self._content_max_file_size

    @content_max_file_size.setter
    def content_max_file_size(self, content_max_file_size):
        """Sets the content_max_file_size of this AppContentStorageEntity.

        Gets or sets maximum file size of Admin content that can be uploaded.  # noqa: E501

        :param content_max_file_size: The content_max_file_size of this AppContentStorageEntity.  # noqa: E501
        :type: str
        """

        self._content_max_file_size = content_max_file_size

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
        if issubclass(AppContentStorageEntity, dict):
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
        if not isinstance(other, AppContentStorageEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppContentStorageEntity):
            return True

        return self.to_dict() != other.to_dict()
