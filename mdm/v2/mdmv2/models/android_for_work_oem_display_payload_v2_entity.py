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


class AndroidForWorkOemDisplayPayloadV2Entity(object):
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
        'enable_display_setting': 'bool',
        'display_brightness': 'int',
        'enable_auto_rotate_screen': 'bool',
        'set_sleep_mins': 'int'
    }

    attribute_map = {
        'enable_display_setting': 'EnableDisplaySetting',
        'display_brightness': 'DisplayBrightness',
        'enable_auto_rotate_screen': 'EnableAutoRotateScreen',
        'set_sleep_mins': 'SetSleepMins'
    }

    def __init__(self, enable_display_setting=None, display_brightness=None, enable_auto_rotate_screen=None, set_sleep_mins=None, _configuration=None):  # noqa: E501
        """AndroidForWorkOemDisplayPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable_display_setting = None
        self._display_brightness = None
        self._enable_auto_rotate_screen = None
        self._set_sleep_mins = None
        self.discriminator = None

        if enable_display_setting is not None:
            self.enable_display_setting = enable_display_setting
        if display_brightness is not None:
            self.display_brightness = display_brightness
        if enable_auto_rotate_screen is not None:
            self.enable_auto_rotate_screen = enable_auto_rotate_screen
        if set_sleep_mins is not None:
            self.set_sleep_mins = set_sleep_mins

    @property
    def enable_display_setting(self):
        """Gets the enable_display_setting of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether enable sound settings.  # noqa: E501

        :return: The enable_display_setting of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._enable_display_setting

    @enable_display_setting.setter
    def enable_display_setting(self, enable_display_setting):
        """Sets the enable_display_setting of this AndroidForWorkOemDisplayPayloadV2Entity.

        Gets or sets a value indicating whether enable sound settings.  # noqa: E501

        :param enable_display_setting: The enable_display_setting of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._enable_display_setting = enable_display_setting

    @property
    def display_brightness(self):
        """Gets the display_brightness of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501

        Gets or sets brightness of the display screen.  # noqa: E501

        :return: The display_brightness of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._display_brightness

    @display_brightness.setter
    def display_brightness(self, display_brightness):
        """Sets the display_brightness of this AndroidForWorkOemDisplayPayloadV2Entity.

        Gets or sets brightness of the display screen.  # noqa: E501

        :param display_brightness: The display_brightness of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._display_brightness = display_brightness

    @property
    def enable_auto_rotate_screen(self):
        """Gets the enable_auto_rotate_screen of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether enable screen auto-rotate.  # noqa: E501

        :return: The enable_auto_rotate_screen of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._enable_auto_rotate_screen

    @enable_auto_rotate_screen.setter
    def enable_auto_rotate_screen(self, enable_auto_rotate_screen):
        """Sets the enable_auto_rotate_screen of this AndroidForWorkOemDisplayPayloadV2Entity.

        Gets or sets a value indicating whether enable screen auto-rotate.  # noqa: E501

        :param enable_auto_rotate_screen: The enable_auto_rotate_screen of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._enable_auto_rotate_screen = enable_auto_rotate_screen

    @property
    def set_sleep_mins(self):
        """Gets the set_sleep_mins of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501

        Gets or sets time interval before screen goes to sleep.  # noqa: E501

        :return: The set_sleep_mins of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._set_sleep_mins

    @set_sleep_mins.setter
    def set_sleep_mins(self, set_sleep_mins):
        """Sets the set_sleep_mins of this AndroidForWorkOemDisplayPayloadV2Entity.

        Gets or sets time interval before screen goes to sleep.  # noqa: E501

        :param set_sleep_mins: The set_sleep_mins of this AndroidForWorkOemDisplayPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._set_sleep_mins = set_sleep_mins

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
        if issubclass(AndroidForWorkOemDisplayPayloadV2Entity, dict):
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
        if not isinstance(other, AndroidForWorkOemDisplayPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkOemDisplayPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
