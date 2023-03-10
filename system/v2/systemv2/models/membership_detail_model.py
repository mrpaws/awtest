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


class MembershipDetailModel(object):
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
        'user_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'organization_group_name': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'organization_group_name': 'organization_group_name'
    }

    def __init__(self, user_name=None, first_name=None, last_name=None, organization_group_name=None, _configuration=None):  # noqa: E501
        """MembershipDetailModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_name = None
        self._first_name = None
        self._last_name = None
        self._organization_group_name = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if organization_group_name is not None:
            self.organization_group_name = organization_group_name

    @property
    def user_name(self):
        """Gets the user_name of this MembershipDetailModel.  # noqa: E501

        username  # noqa: E501

        :return: The user_name of this MembershipDetailModel.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this MembershipDetailModel.

        username  # noqa: E501

        :param user_name: The user_name of this MembershipDetailModel.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def first_name(self):
        """Gets the first_name of this MembershipDetailModel.  # noqa: E501

        firstname  # noqa: E501

        :return: The first_name of this MembershipDetailModel.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this MembershipDetailModel.

        firstname  # noqa: E501

        :param first_name: The first_name of this MembershipDetailModel.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this MembershipDetailModel.  # noqa: E501

        lastname  # noqa: E501

        :return: The last_name of this MembershipDetailModel.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this MembershipDetailModel.

        lastname  # noqa: E501

        :param last_name: The last_name of this MembershipDetailModel.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def organization_group_name(self):
        """Gets the organization_group_name of this MembershipDetailModel.  # noqa: E501

        Organization group name  # noqa: E501

        :return: The organization_group_name of this MembershipDetailModel.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_name

    @organization_group_name.setter
    def organization_group_name(self, organization_group_name):
        """Sets the organization_group_name of this MembershipDetailModel.

        Organization group name  # noqa: E501

        :param organization_group_name: The organization_group_name of this MembershipDetailModel.  # noqa: E501
        :type: str
        """

        self._organization_group_name = organization_group_name

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
        if issubclass(MembershipDetailModel, dict):
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
        if not isinstance(other, MembershipDetailModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MembershipDetailModel):
            return True

        return self.to_dict() != other.to_dict()
