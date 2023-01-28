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


class NotificationV1Model(object):
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
        'message': 'str',
        'message_template_id': 'int',
        'action': 'str'
    }

    attribute_map = {
        'message': 'message',
        'message_template_id': 'message_template_id',
        'action': 'action'
    }

    def __init__(self, message=None, message_template_id=None, action=None, _configuration=None):  # noqa: E501
        """NotificationV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._message_template_id = None
        self._action = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if message_template_id is not None:
            self.message_template_id = message_template_id
        if action is not None:
            self.action = action

    @property
    def message(self):
        """Gets the message of this NotificationV1Model.  # noqa: E501

        Gets or sets the message for the push notification.  # noqa: E501

        :return: The message of this NotificationV1Model.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NotificationV1Model.

        Gets or sets the message for the push notification.  # noqa: E501

        :param message: The message of this NotificationV1Model.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def message_template_id(self):
        """Gets the message_template_id of this NotificationV1Model.  # noqa: E501

        Gets or sets the message template id for the email notification.  # noqa: E501

        :return: The message_template_id of this NotificationV1Model.  # noqa: E501
        :rtype: int
        """
        return self._message_template_id

    @message_template_id.setter
    def message_template_id(self, message_template_id):
        """Sets the message_template_id of this NotificationV1Model.

        Gets or sets the message template id for the email notification.  # noqa: E501

        :param message_template_id: The message_template_id of this NotificationV1Model.  # noqa: E501
        :type: int
        """

        self._message_template_id = message_template_id

    @property
    def action(self):
        """Gets the action of this NotificationV1Model.  # noqa: E501

        Gets or sets the action that causes the notification. Possible values [DOWNLOAD_SUCCESS, INSTALL_SUCCESS].  # noqa: E501

        :return: The action of this NotificationV1Model.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NotificationV1Model.

        Gets or sets the action that causes the notification. Possible values [DOWNLOAD_SUCCESS, INSTALL_SUCCESS].  # noqa: E501

        :param action: The action of this NotificationV1Model.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "DOWNLOAD_SUCCESS", "INSTALL_SUCCESS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                action not in allowed_values):
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

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
        if issubclass(NotificationV1Model, dict):
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
        if not isinstance(other, NotificationV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationV1Model):
            return True

        return self.to_dict() != other.to_dict()
