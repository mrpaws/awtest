# coding: utf-8

"""
    MDM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv2.configuration import Configuration


class AndroidForWorkAppPermissionsV2Entity(object):
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
        'product_id': 'str',
        'kind': 'str',
        'permission': 'list[AndroidForWorkAppRuntimePermissionV2Entity]'
    }

    attribute_map = {
        'product_id': 'ProductId',
        'kind': 'Kind',
        'permission': 'Permission'
    }

    def __init__(self, product_id=None, kind=None, permission=None, _configuration=None):  # noqa: E501
        """AndroidForWorkAppPermissionsV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_id = None
        self._kind = None
        self._permission = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if kind is not None:
            self.kind = kind
        if permission is not None:
            self.permission = permission

    @property
    def product_id(self):
        """Gets the product_id of this AndroidForWorkAppPermissionsV2Entity.  # noqa: E501

        Gets or sets application/Product Idententifier.  # noqa: E501

        :return: The product_id of this AndroidForWorkAppPermissionsV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this AndroidForWorkAppPermissionsV2Entity.

        Gets or sets application/Product Idententifier.  # noqa: E501

        :param product_id: The product_id of this AndroidForWorkAppPermissionsV2Entity.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def kind(self):
        """Gets the kind of this AndroidForWorkAppPermissionsV2Entity.  # noqa: E501

        Gets or sets kind -\"androidenterprise#productPermissions\".  # noqa: E501

        :return: The kind of this AndroidForWorkAppPermissionsV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this AndroidForWorkAppPermissionsV2Entity.

        Gets or sets kind -\"androidenterprise#productPermissions\".  # noqa: E501

        :param kind: The kind of this AndroidForWorkAppPermissionsV2Entity.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def permission(self):
        """Gets the permission of this AndroidForWorkAppPermissionsV2Entity.  # noqa: E501

        Gets or sets list of app permission.  # noqa: E501

        :return: The permission of this AndroidForWorkAppPermissionsV2Entity.  # noqa: E501
        :rtype: list[AndroidForWorkAppRuntimePermissionV2Entity]
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this AndroidForWorkAppPermissionsV2Entity.

        Gets or sets list of app permission.  # noqa: E501

        :param permission: The permission of this AndroidForWorkAppPermissionsV2Entity.  # noqa: E501
        :type: list[AndroidForWorkAppRuntimePermissionV2Entity]
        """

        self._permission = permission

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
        if issubclass(AndroidForWorkAppPermissionsV2Entity, dict):
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
        if not isinstance(other, AndroidForWorkAppPermissionsV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkAppPermissionsV2Entity):
            return True

        return self.to_dict() != other.to_dict()
