# coding: utf-8

"""
    MDM API V3

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv3.configuration import Configuration


class ComplianceActionTakenV2Model(object):
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
        'action_type': 'int'
    }

    attribute_map = {
        'action_type': 'action_type'
    }

    def __init__(self, action_type=None, _configuration=None):  # noqa: E501
        """ComplianceActionTakenV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action_type = None
        self.discriminator = None

        if action_type is not None:
            self.action_type = action_type

    @property
    def action_type(self):
        """Gets the action_type of this ComplianceActionTakenV2Model.  # noqa: E501

        An enum representing the compliance action.  # noqa: E501

        :return: The action_type of this ComplianceActionTakenV2Model.  # noqa: E501
        :rtype: int
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ComplianceActionTakenV2Model.

        An enum representing the compliance action.  # noqa: E501

        :param action_type: The action_type of this ComplianceActionTakenV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21]  # noqa: E501
        if (self._configuration.client_side_validation and
                action_type not in allowed_values):
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

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
        if issubclass(ComplianceActionTakenV2Model, dict):
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
        if not isinstance(other, ComplianceActionTakenV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplianceActionTakenV2Model):
            return True

        return self.to_dict() != other.to_dict()
