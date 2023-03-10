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


class ResourceValidationResponseV1Model(object):
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
        'resource_uuid': 'str',
        'action': 'int',
        'threshold_count': 'int'
    }

    attribute_map = {
        'resource_uuid': 'resource_uuid',
        'action': 'action',
        'threshold_count': 'threshold_count'
    }

    def __init__(self, resource_uuid=None, action=None, threshold_count=None, _configuration=None):  # noqa: E501
        """ResourceValidationResponseV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_uuid = None
        self._action = None
        self._threshold_count = None
        self.discriminator = None

        if resource_uuid is not None:
            self.resource_uuid = resource_uuid
        if action is not None:
            self.action = action
        if threshold_count is not None:
            self.threshold_count = threshold_count

    @property
    def resource_uuid(self):
        """Gets the resource_uuid of this ResourceValidationResponseV1Model.  # noqa: E501

        Identifier of the resource.  # noqa: E501

        :return: The resource_uuid of this ResourceValidationResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._resource_uuid

    @resource_uuid.setter
    def resource_uuid(self, resource_uuid):
        """Sets the resource_uuid of this ResourceValidationResponseV1Model.

        Identifier of the resource.  # noqa: E501

        :param resource_uuid: The resource_uuid of this ResourceValidationResponseV1Model.  # noqa: E501
        :type: str
        """

        self._resource_uuid = resource_uuid

    @property
    def action(self):
        """Gets the action of this ResourceValidationResponseV1Model.  # noqa: E501

        Resource action on which the device will decide.  # noqa: E501

        :return: The action of this ResourceValidationResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ResourceValidationResponseV1Model.

        Resource action on which the device will decide.  # noqa: E501

        :param action: The action of this ResourceValidationResponseV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if (self._configuration.client_side_validation and
                action not in allowed_values):
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def threshold_count(self):
        """Gets the threshold_count of this ResourceValidationResponseV1Model.  # noqa: E501

        Latest threshold count on the server  # noqa: E501

        :return: The threshold_count of this ResourceValidationResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._threshold_count

    @threshold_count.setter
    def threshold_count(self, threshold_count):
        """Sets the threshold_count of this ResourceValidationResponseV1Model.

        Latest threshold count on the server  # noqa: E501

        :param threshold_count: The threshold_count of this ResourceValidationResponseV1Model.  # noqa: E501
        :type: int
        """

        self._threshold_count = threshold_count

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
        if issubclass(ResourceValidationResponseV1Model, dict):
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
        if not isinstance(other, ResourceValidationResponseV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceValidationResponseV1Model):
            return True

        return self.to_dict() != other.to_dict()
