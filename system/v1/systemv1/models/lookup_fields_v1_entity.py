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


class LookupFieldsV1Entity(object):
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
        'key': 'str',
        'description': 'str',
        'id': 'int'
    }

    attribute_map = {
        'key': 'key',
        'description': 'description',
        'id': 'id'
    }

    def __init__(self, key=None, description=None, id=None, _configuration=None):  # noqa: E501
        """LookupFieldsV1Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._description = None
        self._id = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id

    @property
    def key(self):
        """Gets the key of this LookupFieldsV1Entity.  # noqa: E501

        Lookup value key  # noqa: E501

        :return: The key of this LookupFieldsV1Entity.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LookupFieldsV1Entity.

        Lookup value key  # noqa: E501

        :param key: The key of this LookupFieldsV1Entity.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def description(self):
        """Gets the description of this LookupFieldsV1Entity.  # noqa: E501

        Description of the lookup value key  # noqa: E501

        :return: The description of this LookupFieldsV1Entity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LookupFieldsV1Entity.

        Description of the lookup value key  # noqa: E501

        :param description: The description of this LookupFieldsV1Entity.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this LookupFieldsV1Entity.  # noqa: E501

        ID of the given lookup value key  # noqa: E501

        :return: The id of this LookupFieldsV1Entity.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LookupFieldsV1Entity.

        ID of the given lookup value key  # noqa: E501

        :param id: The id of this LookupFieldsV1Entity.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(LookupFieldsV1Entity, dict):
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
        if not isinstance(other, LookupFieldsV1Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LookupFieldsV1Entity):
            return True

        return self.to_dict() != other.to_dict()
