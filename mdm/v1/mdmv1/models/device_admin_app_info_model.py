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


class DeviceAdminAppInfoModel(object):
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
        'version': 'str',
        'identifier': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'version': 'Version',
        'identifier': 'Identifier'
    }

    def __init__(self, name=None, version=None, identifier=None, _configuration=None):  # noqa: E501
        """DeviceAdminAppInfoModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._version = None
        self._identifier = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if identifier is not None:
            self.identifier = identifier

    @property
    def name(self):
        """Gets the name of this DeviceAdminAppInfoModel.  # noqa: E501

        Gets or sets the name.  # noqa: E501

        :return: The name of this DeviceAdminAppInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceAdminAppInfoModel.

        Gets or sets the name.  # noqa: E501

        :param name: The name of this DeviceAdminAppInfoModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this DeviceAdminAppInfoModel.  # noqa: E501

        Gets or sets the version.  # noqa: E501

        :return: The version of this DeviceAdminAppInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeviceAdminAppInfoModel.

        Gets or sets the version.  # noqa: E501

        :param version: The version of this DeviceAdminAppInfoModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def identifier(self):
        """Gets the identifier of this DeviceAdminAppInfoModel.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The identifier of this DeviceAdminAppInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this DeviceAdminAppInfoModel.

        Gets or sets the identifier.  # noqa: E501

        :param identifier: The identifier of this DeviceAdminAppInfoModel.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

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
        if issubclass(DeviceAdminAppInfoModel, dict):
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
        if not isinstance(other, DeviceAdminAppInfoModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceAdminAppInfoModel):
            return True

        return self.to_dict() != other.to_dict()
