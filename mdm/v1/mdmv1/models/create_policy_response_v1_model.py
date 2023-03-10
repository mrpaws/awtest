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


class CreatePolicyResponseV1Model(object):
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
        'policy_uuid': 'str',
        'policy_version_uuid': 'str'
    }

    attribute_map = {
        'policy_uuid': 'policy_uuid',
        'policy_version_uuid': 'policy_version_uuid'
    }

    def __init__(self, policy_uuid=None, policy_version_uuid=None, _configuration=None):  # noqa: E501
        """CreatePolicyResponseV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._policy_uuid = None
        self._policy_version_uuid = None
        self.discriminator = None

        if policy_uuid is not None:
            self.policy_uuid = policy_uuid
        if policy_version_uuid is not None:
            self.policy_version_uuid = policy_version_uuid

    @property
    def policy_uuid(self):
        """Gets the policy_uuid of this CreatePolicyResponseV1Model.  # noqa: E501

        The UUID of the Policy.  # noqa: E501

        :return: The policy_uuid of this CreatePolicyResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._policy_uuid

    @policy_uuid.setter
    def policy_uuid(self, policy_uuid):
        """Sets the policy_uuid of this CreatePolicyResponseV1Model.

        The UUID of the Policy.  # noqa: E501

        :param policy_uuid: The policy_uuid of this CreatePolicyResponseV1Model.  # noqa: E501
        :type: str
        """

        self._policy_uuid = policy_uuid

    @property
    def policy_version_uuid(self):
        """Gets the policy_version_uuid of this CreatePolicyResponseV1Model.  # noqa: E501

        The policy version UUID of the Policy.  # noqa: E501

        :return: The policy_version_uuid of this CreatePolicyResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._policy_version_uuid

    @policy_version_uuid.setter
    def policy_version_uuid(self, policy_version_uuid):
        """Sets the policy_version_uuid of this CreatePolicyResponseV1Model.

        The policy version UUID of the Policy.  # noqa: E501

        :param policy_version_uuid: The policy_version_uuid of this CreatePolicyResponseV1Model.  # noqa: E501
        :type: str
        """

        self._policy_version_uuid = policy_version_uuid

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
        if issubclass(CreatePolicyResponseV1Model, dict):
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
        if not isinstance(other, CreatePolicyResponseV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreatePolicyResponseV1Model):
            return True

        return self.to_dict() != other.to_dict()
