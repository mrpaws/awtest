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


class AppDetailsV1Model(object):
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
        'identifier': 'str',
        'type': 'list[str]',
        'total_size': 'int'
    }

    attribute_map = {
        'identifier': 'identifier',
        'type': 'type',
        'total_size': 'total_size'
    }

    def __init__(self, identifier=None, type=None, total_size=None, _configuration=None):  # noqa: E501
        """AppDetailsV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._identifier = None
        self._type = None
        self._total_size = None
        self.discriminator = None

        self.identifier = identifier
        self.type = type
        if total_size is not None:
            self.total_size = total_size

    @property
    def identifier(self):
        """Gets the identifier of this AppDetailsV1Model.  # noqa: E501

        The bundle identifier of the application  # noqa: E501

        :return: The identifier of this AppDetailsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this AppDetailsV1Model.

        The bundle identifier of the application  # noqa: E501

        :param identifier: The identifier of this AppDetailsV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def type(self):
        """Gets the type of this AppDetailsV1Model.  # noqa: E501

        The application types which are associated with the bundle identifier. There will be one or more entries from [System, Internal, Public, Purchased]  # noqa: E501

        :return: The type of this AppDetailsV1Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AppDetailsV1Model.

        The application types which are associated with the bundle identifier. There will be one or more entries from [System, Internal, Public, Purchased]  # noqa: E501

        :param type: The type of this AppDetailsV1Model.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def total_size(self):
        """Gets the total_size of this AppDetailsV1Model.  # noqa: E501

        The total size of the application  # noqa: E501

        :return: The total_size of this AppDetailsV1Model.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this AppDetailsV1Model.

        The total size of the application  # noqa: E501

        :param total_size: The total_size of this AppDetailsV1Model.  # noqa: E501
        :type: int
        """

        self._total_size = total_size

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
        if issubclass(AppDetailsV1Model, dict):
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
        if not isinstance(other, AppDetailsV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppDetailsV1Model):
            return True

        return self.to_dict() != other.to_dict()
