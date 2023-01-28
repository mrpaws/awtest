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


class AppleNotificationPayloadV2Entity(object):
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
        'app_notification_settings': 'list[AppNotificationV2Entity_]'
    }

    attribute_map = {
        'app_notification_settings': 'AppNotificationSettings'
    }

    def __init__(self, app_notification_settings=None, _configuration=None):  # noqa: E501
        """AppleNotificationPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._app_notification_settings = None
        self.discriminator = None

        if app_notification_settings is not None:
            self.app_notification_settings = app_notification_settings

    @property
    def app_notification_settings(self):
        """Gets the app_notification_settings of this AppleNotificationPayloadV2Entity.  # noqa: E501

        Gets or sets list of Notification settings.  # noqa: E501

        :return: The app_notification_settings of this AppleNotificationPayloadV2Entity.  # noqa: E501
        :rtype: list[AppNotificationV2Entity_]
        """
        return self._app_notification_settings

    @app_notification_settings.setter
    def app_notification_settings(self, app_notification_settings):
        """Sets the app_notification_settings of this AppleNotificationPayloadV2Entity.

        Gets or sets list of Notification settings.  # noqa: E501

        :param app_notification_settings: The app_notification_settings of this AppleNotificationPayloadV2Entity.  # noqa: E501
        :type: list[AppNotificationV2Entity_]
        """

        self._app_notification_settings = app_notification_settings

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
        if issubclass(AppleNotificationPayloadV2Entity, dict):
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
        if not isinstance(other, AppleNotificationPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleNotificationPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
