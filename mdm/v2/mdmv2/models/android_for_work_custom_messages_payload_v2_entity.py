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


class AndroidForWorkCustomMessagesPayloadV2Entity(object):
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
        'lock_screen_message': 'str',
        'short_support_message': 'str',
        'long_support_message': 'str'
    }

    attribute_map = {
        'lock_screen_message': 'LockScreenMessage',
        'short_support_message': 'ShortSupportMessage',
        'long_support_message': 'LongSupportMessage'
    }

    def __init__(self, lock_screen_message=None, short_support_message=None, long_support_message=None, _configuration=None):  # noqa: E501
        """AndroidForWorkCustomMessagesPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._lock_screen_message = None
        self._short_support_message = None
        self._long_support_message = None
        self.discriminator = None

        if lock_screen_message is not None:
            self.lock_screen_message = lock_screen_message
        if short_support_message is not None:
            self.short_support_message = short_support_message
        if long_support_message is not None:
            self.long_support_message = long_support_message

    @property
    def lock_screen_message(self):
        """Gets the lock_screen_message of this AndroidForWorkCustomMessagesPayloadV2Entity.  # noqa: E501

        Gets or sets set a lockscreen message.  # noqa: E501

        :return: The lock_screen_message of this AndroidForWorkCustomMessagesPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._lock_screen_message

    @lock_screen_message.setter
    def lock_screen_message(self, lock_screen_message):
        """Sets the lock_screen_message of this AndroidForWorkCustomMessagesPayloadV2Entity.

        Gets or sets set a lockscreen message.  # noqa: E501

        :param lock_screen_message: The lock_screen_message of this AndroidForWorkCustomMessagesPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._lock_screen_message = lock_screen_message

    @property
    def short_support_message(self):
        """Gets the short_support_message of this AndroidForWorkCustomMessagesPayloadV2Entity.  # noqa: E501

        Gets or sets set a short message for blocked setting.  # noqa: E501

        :return: The short_support_message of this AndroidForWorkCustomMessagesPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._short_support_message

    @short_support_message.setter
    def short_support_message(self, short_support_message):
        """Sets the short_support_message of this AndroidForWorkCustomMessagesPayloadV2Entity.

        Gets or sets set a short message for blocked setting.  # noqa: E501

        :param short_support_message: The short_support_message of this AndroidForWorkCustomMessagesPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._short_support_message = short_support_message

    @property
    def long_support_message(self):
        """Gets the long_support_message of this AndroidForWorkCustomMessagesPayloadV2Entity.  # noqa: E501

        Gets or sets set a long message for users to view in settings.  # noqa: E501

        :return: The long_support_message of this AndroidForWorkCustomMessagesPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._long_support_message

    @long_support_message.setter
    def long_support_message(self, long_support_message):
        """Sets the long_support_message of this AndroidForWorkCustomMessagesPayloadV2Entity.

        Gets or sets set a long message for users to view in settings.  # noqa: E501

        :param long_support_message: The long_support_message of this AndroidForWorkCustomMessagesPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._long_support_message = long_support_message

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
        if issubclass(AndroidForWorkCustomMessagesPayloadV2Entity, dict):
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
        if not isinstance(other, AndroidForWorkCustomMessagesPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkCustomMessagesPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
