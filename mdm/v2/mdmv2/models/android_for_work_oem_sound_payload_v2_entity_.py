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


class AndroidForWorkOemSoundPayloadV2Entity_(object):
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
        'enable_sound_setting': 'bool',
        'set_system_volume': 'int',
        'set_media_volume': 'int',
        'set_phone_volume': 'int',
        'set_default_notification': 'bool',
        'set_dialpad_touchtones': 'bool',
        'set_touch_sounds': 'bool',
        'set_screen_lock_sounds': 'bool',
        'set_vibrate_on_touch': 'bool'
    }

    attribute_map = {
        'enable_sound_setting': 'EnableSoundSetting',
        'set_system_volume': 'SetSystemVolume',
        'set_media_volume': 'SetMediaVolume',
        'set_phone_volume': 'SetPhoneVolume',
        'set_default_notification': 'SetDefaultNotification',
        'set_dialpad_touchtones': 'SetDialpadTouchtones',
        'set_touch_sounds': 'SetTouchSounds',
        'set_screen_lock_sounds': 'SetScreenLockSounds',
        'set_vibrate_on_touch': 'SetVibrateOnTouch'
    }

    def __init__(self, enable_sound_setting=None, set_system_volume=None, set_media_volume=None, set_phone_volume=None, set_default_notification=None, set_dialpad_touchtones=None, set_touch_sounds=None, set_screen_lock_sounds=None, set_vibrate_on_touch=None, _configuration=None):  # noqa: E501
        """AndroidForWorkOemSoundPayloadV2Entity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable_sound_setting = None
        self._set_system_volume = None
        self._set_media_volume = None
        self._set_phone_volume = None
        self._set_default_notification = None
        self._set_dialpad_touchtones = None
        self._set_touch_sounds = None
        self._set_screen_lock_sounds = None
        self._set_vibrate_on_touch = None
        self.discriminator = None

        if enable_sound_setting is not None:
            self.enable_sound_setting = enable_sound_setting
        if set_system_volume is not None:
            self.set_system_volume = set_system_volume
        if set_media_volume is not None:
            self.set_media_volume = set_media_volume
        if set_phone_volume is not None:
            self.set_phone_volume = set_phone_volume
        if set_default_notification is not None:
            self.set_default_notification = set_default_notification
        if set_dialpad_touchtones is not None:
            self.set_dialpad_touchtones = set_dialpad_touchtones
        if set_touch_sounds is not None:
            self.set_touch_sounds = set_touch_sounds
        if set_screen_lock_sounds is not None:
            self.set_screen_lock_sounds = set_screen_lock_sounds
        if set_vibrate_on_touch is not None:
            self.set_vibrate_on_touch = set_vibrate_on_touch

    @property
    def enable_sound_setting(self):
        """Gets the enable_sound_setting of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether enable sound setting.  # noqa: E501

        :return: The enable_sound_setting of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._enable_sound_setting

    @enable_sound_setting.setter
    def enable_sound_setting(self, enable_sound_setting):
        """Sets the enable_sound_setting of this AndroidForWorkOemSoundPayloadV2Entity_.

        Gets or sets a value indicating whether enable sound setting.  # noqa: E501

        :param enable_sound_setting: The enable_sound_setting of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._enable_sound_setting = enable_sound_setting

    @property
    def set_system_volume(self):
        """Gets the set_system_volume of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501

        Gets or sets system volume.  # noqa: E501

        :return: The set_system_volume of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._set_system_volume

    @set_system_volume.setter
    def set_system_volume(self, set_system_volume):
        """Sets the set_system_volume of this AndroidForWorkOemSoundPayloadV2Entity_.

        Gets or sets system volume.  # noqa: E501

        :param set_system_volume: The set_system_volume of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._set_system_volume = set_system_volume

    @property
    def set_media_volume(self):
        """Gets the set_media_volume of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501

        Gets or sets media volume.  # noqa: E501

        :return: The set_media_volume of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._set_media_volume

    @set_media_volume.setter
    def set_media_volume(self, set_media_volume):
        """Sets the set_media_volume of this AndroidForWorkOemSoundPayloadV2Entity_.

        Gets or sets media volume.  # noqa: E501

        :param set_media_volume: The set_media_volume of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._set_media_volume = set_media_volume

    @property
    def set_phone_volume(self):
        """Gets the set_phone_volume of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501

        Gets or sets phone volume.  # noqa: E501

        :return: The set_phone_volume of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._set_phone_volume

    @set_phone_volume.setter
    def set_phone_volume(self, set_phone_volume):
        """Sets the set_phone_volume of this AndroidForWorkOemSoundPayloadV2Entity_.

        Gets or sets phone volume.  # noqa: E501

        :param set_phone_volume: The set_phone_volume of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._set_phone_volume = set_phone_volume

    @property
    def set_default_notification(self):
        """Gets the set_default_notification of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether indicates whether default notification is enabled.  # noqa: E501

        :return: The set_default_notification of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._set_default_notification

    @set_default_notification.setter
    def set_default_notification(self, set_default_notification):
        """Sets the set_default_notification of this AndroidForWorkOemSoundPayloadV2Entity_.

        Gets or sets a value indicating whether indicates whether default notification is enabled.  # noqa: E501

        :param set_default_notification: The set_default_notification of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._set_default_notification = set_default_notification

    @property
    def set_dialpad_touchtones(self):
        """Gets the set_dialpad_touchtones of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether enable dialpad touchtones.  # noqa: E501

        :return: The set_dialpad_touchtones of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._set_dialpad_touchtones

    @set_dialpad_touchtones.setter
    def set_dialpad_touchtones(self, set_dialpad_touchtones):
        """Sets the set_dialpad_touchtones of this AndroidForWorkOemSoundPayloadV2Entity_.

        Gets or sets a value indicating whether enable dialpad touchtones.  # noqa: E501

        :param set_dialpad_touchtones: The set_dialpad_touchtones of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._set_dialpad_touchtones = set_dialpad_touchtones

    @property
    def set_touch_sounds(self):
        """Gets the set_touch_sounds of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether enable touch sounds.  # noqa: E501

        :return: The set_touch_sounds of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._set_touch_sounds

    @set_touch_sounds.setter
    def set_touch_sounds(self, set_touch_sounds):
        """Sets the set_touch_sounds of this AndroidForWorkOemSoundPayloadV2Entity_.

        Gets or sets a value indicating whether enable touch sounds.  # noqa: E501

        :param set_touch_sounds: The set_touch_sounds of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._set_touch_sounds = set_touch_sounds

    @property
    def set_screen_lock_sounds(self):
        """Gets the set_screen_lock_sounds of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether enable screen lock sounds.  # noqa: E501

        :return: The set_screen_lock_sounds of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._set_screen_lock_sounds

    @set_screen_lock_sounds.setter
    def set_screen_lock_sounds(self, set_screen_lock_sounds):
        """Sets the set_screen_lock_sounds of this AndroidForWorkOemSoundPayloadV2Entity_.

        Gets or sets a value indicating whether enable screen lock sounds.  # noqa: E501

        :param set_screen_lock_sounds: The set_screen_lock_sounds of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._set_screen_lock_sounds = set_screen_lock_sounds

    @property
    def set_vibrate_on_touch(self):
        """Gets the set_vibrate_on_touch of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether enable vibrate on touch.  # noqa: E501

        :return: The set_vibrate_on_touch of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._set_vibrate_on_touch

    @set_vibrate_on_touch.setter
    def set_vibrate_on_touch(self, set_vibrate_on_touch):
        """Sets the set_vibrate_on_touch of this AndroidForWorkOemSoundPayloadV2Entity_.

        Gets or sets a value indicating whether enable vibrate on touch.  # noqa: E501

        :param set_vibrate_on_touch: The set_vibrate_on_touch of this AndroidForWorkOemSoundPayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._set_vibrate_on_touch = set_vibrate_on_touch

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
        if issubclass(AndroidForWorkOemSoundPayloadV2Entity_, dict):
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
        if not isinstance(other, AndroidForWorkOemSoundPayloadV2Entity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkOemSoundPayloadV2Entity_):
            return True

        return self.to_dict() != other.to_dict()
