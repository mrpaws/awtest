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


class UserGroupsListModel(object):
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
        'user_group_uuids': 'list[str]',
        'op': 'str'
    }

    attribute_map = {
        'user_group_uuids': 'user_group_uuids',
        'op': 'op'
    }

    def __init__(self, user_group_uuids=None, op=None, _configuration=None):  # noqa: E501
        """UserGroupsListModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_group_uuids = None
        self._op = None
        self.discriminator = None

        if user_group_uuids is not None:
            self.user_group_uuids = user_group_uuids
        if op is not None:
            self.op = op

    @property
    def user_group_uuids(self):
        """Gets the user_group_uuids of this UserGroupsListModel.  # noqa: E501

        user group uuid  # noqa: E501

        :return: The user_group_uuids of this UserGroupsListModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_group_uuids

    @user_group_uuids.setter
    def user_group_uuids(self, user_group_uuids):
        """Sets the user_group_uuids of this UserGroupsListModel.

        user group uuid  # noqa: E501

        :param user_group_uuids: The user_group_uuids of this UserGroupsListModel.  # noqa: E501
        :type: list[str]
        """

        self._user_group_uuids = user_group_uuids

    @property
    def op(self):
        """Gets the op of this UserGroupsListModel.  # noqa: E501

        operation to be performed.  # noqa: E501

        :return: The op of this UserGroupsListModel.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this UserGroupsListModel.

        operation to be performed.  # noqa: E501

        :param op: The op of this UserGroupsListModel.  # noqa: E501
        :type: str
        """

        self._op = op

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
        if issubclass(UserGroupsListModel, dict):
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
        if not isinstance(other, UserGroupsListModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserGroupsListModel):
            return True

        return self.to_dict() != other.to_dict()
