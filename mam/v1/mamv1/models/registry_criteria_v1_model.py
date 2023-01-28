# coding: utf-8

"""
    MAM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv1.configuration import Configuration


class RegistryCriteriaV1Model(object):
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
        'path': 'str',
        'key_name': 'str',
        'key_type': 'int',
        'key_value': 'str'
    }

    attribute_map = {
        'path': 'path',
        'key_name': 'key_name',
        'key_type': 'key_type',
        'key_value': 'key_value'
    }

    def __init__(self, path=None, key_name=None, key_type=None, key_value=None, _configuration=None):  # noqa: E501
        """RegistryCriteriaV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._path = None
        self._key_name = None
        self._key_type = None
        self._key_value = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if key_name is not None:
            self.key_name = key_name
        if key_type is not None:
            self.key_type = key_type
        if key_value is not None:
            self.key_value = key_value

    @property
    def path(self):
        """Gets the path of this RegistryCriteriaV1Model.  # noqa: E501

        Gets or sets the path of the key in the registry.  # noqa: E501

        :return: The path of this RegistryCriteriaV1Model.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RegistryCriteriaV1Model.

        Gets or sets the path of the key in the registry.  # noqa: E501

        :param path: The path of this RegistryCriteriaV1Model.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def key_name(self):
        """Gets the key_name of this RegistryCriteriaV1Model.  # noqa: E501

        Gets or sets the name of new key to be created in the registry.  # noqa: E501

        :return: The key_name of this RegistryCriteriaV1Model.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this RegistryCriteriaV1Model.

        Gets or sets the name of new key to be created in the registry.  # noqa: E501

        :param key_name: The key_name of this RegistryCriteriaV1Model.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

    @property
    def key_type(self):
        """Gets the key_type of this RegistryCriteriaV1Model.  # noqa: E501

        Gets or sets the type of key to be created in the registry. Supported values : String = 1, Binary = 2, DWord = 3, QWord = 4, MultiString = 5, ExpandableString = 6, Version = 7.  # noqa: E501

        :return: The key_type of this RegistryCriteriaV1Model.  # noqa: E501
        :rtype: int
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this RegistryCriteriaV1Model.

        Gets or sets the type of key to be created in the registry. Supported values : String = 1, Binary = 2, DWord = 3, QWord = 4, MultiString = 5, ExpandableString = 6, Version = 7.  # noqa: E501

        :param key_type: The key_type of this RegistryCriteriaV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7]  # noqa: E501
        if (self._configuration.client_side_validation and
                key_type not in allowed_values):
            raise ValueError(
                "Invalid value for `key_type` ({0}), must be one of {1}"  # noqa: E501
                .format(key_type, allowed_values)
            )

        self._key_type = key_type

    @property
    def key_value(self):
        """Gets the key_value of this RegistryCriteriaV1Model.  # noqa: E501

        Gets or sets the value of the key to be created in the registry.  # noqa: E501

        :return: The key_value of this RegistryCriteriaV1Model.  # noqa: E501
        :rtype: str
        """
        return self._key_value

    @key_value.setter
    def key_value(self, key_value):
        """Sets the key_value of this RegistryCriteriaV1Model.

        Gets or sets the value of the key to be created in the registry.  # noqa: E501

        :param key_value: The key_value of this RegistryCriteriaV1Model.  # noqa: E501
        :type: str
        """

        self._key_value = key_value

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
        if issubclass(RegistryCriteriaV1Model, dict):
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
        if not isinstance(other, RegistryCriteriaV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistryCriteriaV1Model):
            return True

        return self.to_dict() != other.to_dict()