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


class CustomAttribute(object):
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
        'name': 'str',
        'value': 'str',
        'source': 'str',
        'application': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'value': 'Value',
        'source': 'Source',
        'application': 'Application'
    }

    def __init__(self, name=None, value=None, source=None, application=None, _configuration=None):  # noqa: E501
        """CustomAttribute - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._value = None
        self._source = None
        self._application = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if source is not None:
            self.source = source
        if application is not None:
            self.application = application

    @property
    def name(self):
        """Gets the name of this CustomAttribute.  # noqa: E501

        Gets or sets custom Attribute Name.  # noqa: E501

        :return: The name of this CustomAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomAttribute.

        Gets or sets custom Attribute Name.  # noqa: E501

        :param name: The name of this CustomAttribute.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and not re.search(r'^[^*:?\"<>|\\\/;,\\[\\]\\(\\)]+$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[^*:?\"<>|\\\/;,\\[\\]\\(\\)]+$/`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this CustomAttribute.  # noqa: E501

        Gets or sets custom Attribute Value.  # noqa: E501

        :return: The value of this CustomAttribute.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomAttribute.

        Gets or sets custom Attribute Value.  # noqa: E501

        :param value: The value of this CustomAttribute.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                value is not None and not re.search(r'^[^*:?\"<>|\\\/;,\\[\\]\\(\\)]+$', value)):  # noqa: E501
            raise ValueError(r"Invalid value for `value`, must be a follow pattern or equal to `/^[^*:?\"<>|\\\/;,\\[\\]\\(\\)]+$/`")  # noqa: E501

        self._value = value

    @property
    def source(self):
        """Gets the source of this CustomAttribute.  # noqa: E501

        Gets or sets custom Attribute Source. Device Sourced/Console Sourced.  # noqa: E501

        :return: The source of this CustomAttribute.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CustomAttribute.

        Gets or sets custom Attribute Source. Device Sourced/Console Sourced.  # noqa: E501

        :param source: The source of this CustomAttribute.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def application(self):
        """Gets the application of this CustomAttribute.  # noqa: E501

        Gets or sets custom Attribute Application Name.  # noqa: E501

        :return: The application of this CustomAttribute.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this CustomAttribute.

        Gets or sets custom Attribute Application Name.  # noqa: E501

        :param application: The application of this CustomAttribute.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                application is not None and not re.search(r'^[^*:?\"<>|\\\/;,\\[\\]\\(\\)]+$', application)):  # noqa: E501
            raise ValueError(r"Invalid value for `application`, must be a follow pattern or equal to `/^[^*:?\"<>|\\\/;,\\[\\]\\(\\)]+$/`")  # noqa: E501

        self._application = application

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
        if issubclass(CustomAttribute, dict):
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
        if not isinstance(other, CustomAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomAttribute):
            return True

        return self.to_dict() != other.to_dict()
