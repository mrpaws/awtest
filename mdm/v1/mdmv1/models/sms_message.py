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


class SmsMessage(object):
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
        'message_body': 'str',
        'phone_number': 'str',
        'bulk_values': 'BulkValues_'
    }

    attribute_map = {
        'message_body': 'MessageBody',
        'phone_number': 'PhoneNumber',
        'bulk_values': 'BulkValues'
    }

    def __init__(self, message_body=None, phone_number=None, bulk_values=None, _configuration=None):  # noqa: E501
        """SmsMessage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message_body = None
        self._phone_number = None
        self._bulk_values = None
        self.discriminator = None

        if message_body is not None:
            self.message_body = message_body
        if phone_number is not None:
            self.phone_number = phone_number
        if bulk_values is not None:
            self.bulk_values = bulk_values

    @property
    def message_body(self):
        """Gets the message_body of this SmsMessage.  # noqa: E501

        Gets or sets contents of the SMS message.  # noqa: E501

        :return: The message_body of this SmsMessage.  # noqa: E501
        :rtype: str
        """
        return self._message_body

    @message_body.setter
    def message_body(self, message_body):
        """Sets the message_body of this SmsMessage.

        Gets or sets contents of the SMS message.  # noqa: E501

        :param message_body: The message_body of this SmsMessage.  # noqa: E501
        :type: str
        """

        self._message_body = message_body

    @property
    def phone_number(self):
        """Gets the phone_number of this SmsMessage.  # noqa: E501

        Gets or sets recipient Phonenumber.  # noqa: E501

        :return: The phone_number of this SmsMessage.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this SmsMessage.

        Gets or sets recipient Phonenumber.  # noqa: E501

        :param phone_number: The phone_number of this SmsMessage.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def bulk_values(self):
        """Gets the bulk_values of this SmsMessage.  # noqa: E501

        Gets or sets list of devices that will receive the message.  # noqa: E501

        :return: The bulk_values of this SmsMessage.  # noqa: E501
        :rtype: BulkValues_
        """
        return self._bulk_values

    @bulk_values.setter
    def bulk_values(self, bulk_values):
        """Sets the bulk_values of this SmsMessage.

        Gets or sets list of devices that will receive the message.  # noqa: E501

        :param bulk_values: The bulk_values of this SmsMessage.  # noqa: E501
        :type: BulkValues_
        """

        self._bulk_values = bulk_values

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
        if issubclass(SmsMessage, dict):
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
        if not isinstance(other, SmsMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmsMessage):
            return True

        return self.to_dict() != other.to_dict()
