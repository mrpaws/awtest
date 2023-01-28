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


class ApnsConfigurationModel(object):
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
        'inherit': 'bool',
        'child_permission': 'str',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'inherit': 'Inherit',
        'child_permission': 'ChildPermission',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, inherit=None, child_permission=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """ApnsConfigurationModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._inherit = None
        self._child_permission = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if inherit is not None:
            self.inherit = inherit
        if child_permission is not None:
            self.child_permission = child_permission
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def inherit(self):
        """Gets the inherit of this ApnsConfigurationModel.  # noqa: E501

        Gets or sets a value indicating whether flag indicating Inherit configuration of Certificate. When it is true, the Certificate will be inherited from parent OG.  # noqa: E501

        :return: The inherit of this ApnsConfigurationModel.  # noqa: E501
        :rtype: bool
        """
        return self._inherit

    @inherit.setter
    def inherit(self, inherit):
        """Sets the inherit of this ApnsConfigurationModel.

        Gets or sets a value indicating whether flag indicating Inherit configuration of Certificate. When it is true, the Certificate will be inherited from parent OG.  # noqa: E501

        :param inherit: The inherit of this ApnsConfigurationModel.  # noqa: E501
        :type: bool
        """

        self._inherit = inherit

    @property
    def child_permission(self):
        """Gets the child_permission of this ApnsConfigurationModel.  # noqa: E501

        Gets or sets child Permissions of the Apns Configuration model.  # noqa: E501

        :return: The child_permission of this ApnsConfigurationModel.  # noqa: E501
        :rtype: str
        """
        return self._child_permission

    @child_permission.setter
    def child_permission(self, child_permission):
        """Sets the child_permission of this ApnsConfigurationModel.

        Gets or sets child Permissions of the Apns Configuration model.  # noqa: E501

        :param child_permission: The child_permission of this ApnsConfigurationModel.  # noqa: E501
        :type: str
        """

        self._child_permission = child_permission

    @property
    def id(self):
        """Gets the id of this ApnsConfigurationModel.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this ApnsConfigurationModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApnsConfigurationModel.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this ApnsConfigurationModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this ApnsConfigurationModel.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this ApnsConfigurationModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ApnsConfigurationModel.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this ApnsConfigurationModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(ApnsConfigurationModel, dict):
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
        if not isinstance(other, ApnsConfigurationModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApnsConfigurationModel):
            return True

        return self.to_dict() != other.to_dict()
