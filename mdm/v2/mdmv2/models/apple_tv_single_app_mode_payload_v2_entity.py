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


class AppleTvSingleAppModePayloadV2Entity(object):
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
        'application_bundle_id': 'str',
        'disable_touch_screen': 'bool',
        'disable_auto_lock': 'bool',
        'enable_voice_over': 'bool',
        'allow_user_to_adjust_voice_over': 'bool',
        'enable_zoom': 'bool',
        'allow_user_to_adjust_zoom': 'bool',
        'enable_invert_colors': 'bool',
        'allow_user_to_adjust_invert_colors': 'bool'
    }

    attribute_map = {
        'application_bundle_id': 'applicationBundleID',
        'disable_touch_screen': 'disableTouchScreen',
        'disable_auto_lock': 'disableAutoLock',
        'enable_voice_over': 'enableVoiceOver',
        'allow_user_to_adjust_voice_over': 'allowUserToAdjustVoiceOver',
        'enable_zoom': 'enableZoom',
        'allow_user_to_adjust_zoom': 'allowUserToAdjustZoom',
        'enable_invert_colors': 'enableInvertColors',
        'allow_user_to_adjust_invert_colors': 'allowUserToAdjustInvertColors'
    }

    def __init__(self, application_bundle_id=None, disable_touch_screen=None, disable_auto_lock=None, enable_voice_over=None, allow_user_to_adjust_voice_over=None, enable_zoom=None, allow_user_to_adjust_zoom=None, enable_invert_colors=None, allow_user_to_adjust_invert_colors=None, _configuration=None):  # noqa: E501
        """AppleTvSingleAppModePayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_bundle_id = None
        self._disable_touch_screen = None
        self._disable_auto_lock = None
        self._enable_voice_over = None
        self._allow_user_to_adjust_voice_over = None
        self._enable_zoom = None
        self._allow_user_to_adjust_zoom = None
        self._enable_invert_colors = None
        self._allow_user_to_adjust_invert_colors = None
        self.discriminator = None

        if application_bundle_id is not None:
            self.application_bundle_id = application_bundle_id
        if disable_touch_screen is not None:
            self.disable_touch_screen = disable_touch_screen
        if disable_auto_lock is not None:
            self.disable_auto_lock = disable_auto_lock
        if enable_voice_over is not None:
            self.enable_voice_over = enable_voice_over
        if allow_user_to_adjust_voice_over is not None:
            self.allow_user_to_adjust_voice_over = allow_user_to_adjust_voice_over
        if enable_zoom is not None:
            self.enable_zoom = enable_zoom
        if allow_user_to_adjust_zoom is not None:
            self.allow_user_to_adjust_zoom = allow_user_to_adjust_zoom
        if enable_invert_colors is not None:
            self.enable_invert_colors = enable_invert_colors
        if allow_user_to_adjust_invert_colors is not None:
            self.allow_user_to_adjust_invert_colors = allow_user_to_adjust_invert_colors

    @property
    def application_bundle_id(self):
        """Gets the application_bundle_id of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501

        Application bundle id  # noqa: E501

        :return: The application_bundle_id of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._application_bundle_id

    @application_bundle_id.setter
    def application_bundle_id(self, application_bundle_id):
        """Sets the application_bundle_id of this AppleTvSingleAppModePayloadV2Entity.

        Application bundle id  # noqa: E501

        :param application_bundle_id: The application_bundle_id of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._application_bundle_id = application_bundle_id

    @property
    def disable_touch_screen(self):
        """Gets the disable_touch_screen of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501

        whether disable touch screen  # noqa: E501

        :return: The disable_touch_screen of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._disable_touch_screen

    @disable_touch_screen.setter
    def disable_touch_screen(self, disable_touch_screen):
        """Sets the disable_touch_screen of this AppleTvSingleAppModePayloadV2Entity.

        whether disable touch screen  # noqa: E501

        :param disable_touch_screen: The disable_touch_screen of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._disable_touch_screen = disable_touch_screen

    @property
    def disable_auto_lock(self):
        """Gets the disable_auto_lock of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501

        whether disable auto lock. If true, the device will not automatically go to sleep after an idle period  # noqa: E501

        :return: The disable_auto_lock of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._disable_auto_lock

    @disable_auto_lock.setter
    def disable_auto_lock(self, disable_auto_lock):
        """Sets the disable_auto_lock of this AppleTvSingleAppModePayloadV2Entity.

        whether disable auto lock. If true, the device will not automatically go to sleep after an idle period  # noqa: E501

        :param disable_auto_lock: The disable_auto_lock of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._disable_auto_lock = disable_auto_lock

    @property
    def enable_voice_over(self):
        """Gets the enable_voice_over of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501

        whether enable VoiceOver  # noqa: E501

        :return: The enable_voice_over of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._enable_voice_over

    @enable_voice_over.setter
    def enable_voice_over(self, enable_voice_over):
        """Sets the enable_voice_over of this AppleTvSingleAppModePayloadV2Entity.

        whether enable VoiceOver  # noqa: E501

        :param enable_voice_over: The enable_voice_over of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._enable_voice_over = enable_voice_over

    @property
    def allow_user_to_adjust_voice_over(self):
        """Gets the allow_user_to_adjust_voice_over of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501

        whether allow VoiceOver adjustment when it is enabled  # noqa: E501

        :return: The allow_user_to_adjust_voice_over of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_user_to_adjust_voice_over

    @allow_user_to_adjust_voice_over.setter
    def allow_user_to_adjust_voice_over(self, allow_user_to_adjust_voice_over):
        """Sets the allow_user_to_adjust_voice_over of this AppleTvSingleAppModePayloadV2Entity.

        whether allow VoiceOver adjustment when it is enabled  # noqa: E501

        :param allow_user_to_adjust_voice_over: The allow_user_to_adjust_voice_over of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_user_to_adjust_voice_over = allow_user_to_adjust_voice_over

    @property
    def enable_zoom(self):
        """Gets the enable_zoom of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501

        whether enable Zoom  # noqa: E501

        :return: The enable_zoom of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._enable_zoom

    @enable_zoom.setter
    def enable_zoom(self, enable_zoom):
        """Sets the enable_zoom of this AppleTvSingleAppModePayloadV2Entity.

        whether enable Zoom  # noqa: E501

        :param enable_zoom: The enable_zoom of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._enable_zoom = enable_zoom

    @property
    def allow_user_to_adjust_zoom(self):
        """Gets the allow_user_to_adjust_zoom of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501

        whether allow Zoom adjustment when it is enabled  # noqa: E501

        :return: The allow_user_to_adjust_zoom of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_user_to_adjust_zoom

    @allow_user_to_adjust_zoom.setter
    def allow_user_to_adjust_zoom(self, allow_user_to_adjust_zoom):
        """Sets the allow_user_to_adjust_zoom of this AppleTvSingleAppModePayloadV2Entity.

        whether allow Zoom adjustment when it is enabled  # noqa: E501

        :param allow_user_to_adjust_zoom: The allow_user_to_adjust_zoom of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_user_to_adjust_zoom = allow_user_to_adjust_zoom

    @property
    def enable_invert_colors(self):
        """Gets the enable_invert_colors of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501

        whether enable Invert Colors  # noqa: E501

        :return: The enable_invert_colors of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._enable_invert_colors

    @enable_invert_colors.setter
    def enable_invert_colors(self, enable_invert_colors):
        """Sets the enable_invert_colors of this AppleTvSingleAppModePayloadV2Entity.

        whether enable Invert Colors  # noqa: E501

        :param enable_invert_colors: The enable_invert_colors of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._enable_invert_colors = enable_invert_colors

    @property
    def allow_user_to_adjust_invert_colors(self):
        """Gets the allow_user_to_adjust_invert_colors of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501

        whether allow Invert Colors adjustment when it is enabled  # noqa: E501

        :return: The allow_user_to_adjust_invert_colors of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_user_to_adjust_invert_colors

    @allow_user_to_adjust_invert_colors.setter
    def allow_user_to_adjust_invert_colors(self, allow_user_to_adjust_invert_colors):
        """Sets the allow_user_to_adjust_invert_colors of this AppleTvSingleAppModePayloadV2Entity.

        whether allow Invert Colors adjustment when it is enabled  # noqa: E501

        :param allow_user_to_adjust_invert_colors: The allow_user_to_adjust_invert_colors of this AppleTvSingleAppModePayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_user_to_adjust_invert_colors = allow_user_to_adjust_invert_colors

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
        if issubclass(AppleTvSingleAppModePayloadV2Entity, dict):
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
        if not isinstance(other, AppleTvSingleAppModePayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleTvSingleAppModePayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()