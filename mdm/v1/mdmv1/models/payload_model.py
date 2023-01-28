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


class PayloadModel(object):
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
        'payload_type': 'str',
        'payload_id': 'str',
        'payload_attributes': 'dict(str, object)'
    }

    attribute_map = {
        'payload_type': 'payloadType',
        'payload_id': 'payloadID',
        'payload_attributes': 'payloadAttributes'
    }

    def __init__(self, payload_type=None, payload_id=None, payload_attributes=None, _configuration=None):  # noqa: E501
        """PayloadModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._payload_type = None
        self._payload_id = None
        self._payload_attributes = None
        self.discriminator = None

        if payload_type is not None:
            self.payload_type = payload_type
        if payload_id is not None:
            self.payload_id = payload_id
        if payload_attributes is not None:
            self.payload_attributes = payload_attributes

    @property
    def payload_type(self):
        """Gets the payload_type of this PayloadModel.  # noqa: E501

        Gets or sets type for payload.  # noqa: E501

        :return: The payload_type of this PayloadModel.  # noqa: E501
        :rtype: str
        """
        return self._payload_type

    @payload_type.setter
    def payload_type(self, payload_type):
        """Sets the payload_type of this PayloadModel.

        Gets or sets type for payload.  # noqa: E501

        :param payload_type: The payload_type of this PayloadModel.  # noqa: E501
        :type: str
        """

        self._payload_type = payload_type

    @property
    def payload_id(self):
        """Gets the payload_id of this PayloadModel.  # noqa: E501

        Gets or sets PayloadID as GUID.  # noqa: E501

        :return: The payload_id of this PayloadModel.  # noqa: E501
        :rtype: str
        """
        return self._payload_id

    @payload_id.setter
    def payload_id(self, payload_id):
        """Sets the payload_id of this PayloadModel.

        Gets or sets PayloadID as GUID.  # noqa: E501

        :param payload_id: The payload_id of this PayloadModel.  # noqa: E501
        :type: str
        """

        self._payload_id = payload_id

    @property
    def payload_attributes(self):
        """Gets the payload_attributes of this PayloadModel.  # noqa: E501

        Gets or sets type for payload.  # noqa: E501

        :return: The payload_attributes of this PayloadModel.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._payload_attributes

    @payload_attributes.setter
    def payload_attributes(self, payload_attributes):
        """Sets the payload_attributes of this PayloadModel.

        Gets or sets type for payload.  # noqa: E501

        :param payload_attributes: The payload_attributes of this PayloadModel.  # noqa: E501
        :type: dict(str, object)
        """

        self._payload_attributes = payload_attributes

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
        if issubclass(PayloadModel, dict):
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
        if not isinstance(other, PayloadModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PayloadModel):
            return True

        return self.to_dict() != other.to_dict()
