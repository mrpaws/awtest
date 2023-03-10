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


class ProductFileDetials(object):
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
        'file_id': 'int',
        'name': 'str',
        'path': 'str'
    }

    attribute_map = {
        'file_id': 'FileId',
        'name': 'Name',
        'path': 'Path'
    }

    def __init__(self, file_id=None, name=None, path=None, _configuration=None):  # noqa: E501
        """ProductFileDetials - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_id = None
        self._name = None
        self._path = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path

    @property
    def file_id(self):
        """Gets the file_id of this ProductFileDetials.  # noqa: E501

        Gets or sets file Identifier.  # noqa: E501

        :return: The file_id of this ProductFileDetials.  # noqa: E501
        :rtype: int
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this ProductFileDetials.

        Gets or sets file Identifier.  # noqa: E501

        :param file_id: The file_id of this ProductFileDetials.  # noqa: E501
        :type: int
        """

        self._file_id = file_id

    @property
    def name(self):
        """Gets the name of this ProductFileDetials.  # noqa: E501

        Gets or sets name of the file.  # noqa: E501

        :return: The name of this ProductFileDetials.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductFileDetials.

        Gets or sets name of the file.  # noqa: E501

        :param name: The name of this ProductFileDetials.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this ProductFileDetials.  # noqa: E501

        Gets or sets path of the file.  # noqa: E501

        :return: The path of this ProductFileDetials.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ProductFileDetials.

        Gets or sets path of the file.  # noqa: E501

        :param path: The path of this ProductFileDetials.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if issubclass(ProductFileDetials, dict):
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
        if not isinstance(other, ProductFileDetials):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductFileDetials):
            return True

        return self.to_dict() != other.to_dict()
