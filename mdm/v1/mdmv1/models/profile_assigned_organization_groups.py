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


class ProfileAssignedOrganizationGroups(object):
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
        'assigned_og': 'list[ProfileAssignedOrganizationGroup]'
    }

    attribute_map = {
        'assigned_og': 'AssignedOg'
    }

    def __init__(self, assigned_og=None, _configuration=None):  # noqa: E501
        """ProfileAssignedOrganizationGroups - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assigned_og = None
        self.discriminator = None

        if assigned_og is not None:
            self.assigned_og = assigned_og

    @property
    def assigned_og(self):
        """Gets the assigned_og of this ProfileAssignedOrganizationGroups.  # noqa: E501

        Gets or sets list of application supported models.  # noqa: E501

        :return: The assigned_og of this ProfileAssignedOrganizationGroups.  # noqa: E501
        :rtype: list[ProfileAssignedOrganizationGroup]
        """
        return self._assigned_og

    @assigned_og.setter
    def assigned_og(self, assigned_og):
        """Sets the assigned_og of this ProfileAssignedOrganizationGroups.

        Gets or sets list of application supported models.  # noqa: E501

        :param assigned_og: The assigned_og of this ProfileAssignedOrganizationGroups.  # noqa: E501
        :type: list[ProfileAssignedOrganizationGroup]
        """

        self._assigned_og = assigned_og

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
        if issubclass(ProfileAssignedOrganizationGroups, dict):
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
        if not isinstance(other, ProfileAssignedOrganizationGroups):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProfileAssignedOrganizationGroups):
            return True

        return self.to_dict() != other.to_dict()
