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


class QnxDeviceProfileEntity(object):
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
        'custom_attribute_payload': 'QnxCustomAttributePayloadEntity',
        'general': 'GeneralPayloadV2Entity'
    }

    attribute_map = {
        'custom_attribute_payload': 'CustomAttributePayload',
        'general': 'General'
    }

    def __init__(self, custom_attribute_payload=None, general=None, _configuration=None):  # noqa: E501
        """QnxDeviceProfileEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_attribute_payload = None
        self._general = None
        self.discriminator = None

        if custom_attribute_payload is not None:
            self.custom_attribute_payload = custom_attribute_payload
        if general is not None:
            self.general = general

    @property
    def custom_attribute_payload(self):
        """Gets the custom_attribute_payload of this QnxDeviceProfileEntity.  # noqa: E501


        :return: The custom_attribute_payload of this QnxDeviceProfileEntity.  # noqa: E501
        :rtype: QnxCustomAttributePayloadEntity
        """
        return self._custom_attribute_payload

    @custom_attribute_payload.setter
    def custom_attribute_payload(self, custom_attribute_payload):
        """Sets the custom_attribute_payload of this QnxDeviceProfileEntity.


        :param custom_attribute_payload: The custom_attribute_payload of this QnxDeviceProfileEntity.  # noqa: E501
        :type: QnxCustomAttributePayloadEntity
        """

        self._custom_attribute_payload = custom_attribute_payload

    @property
    def general(self):
        """Gets the general of this QnxDeviceProfileEntity.  # noqa: E501


        :return: The general of this QnxDeviceProfileEntity.  # noqa: E501
        :rtype: GeneralPayloadV2Entity
        """
        return self._general

    @general.setter
    def general(self, general):
        """Sets the general of this QnxDeviceProfileEntity.


        :param general: The general of this QnxDeviceProfileEntity.  # noqa: E501
        :type: GeneralPayloadV2Entity
        """

        self._general = general

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
        if issubclass(QnxDeviceProfileEntity, dict):
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
        if not isinstance(other, QnxDeviceProfileEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QnxDeviceProfileEntity):
            return True

        return self.to_dict() != other.to_dict()
