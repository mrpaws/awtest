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


class MacOsSetupAssistantPayloadEntity_(object):
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
        'skip_appearance': 'bool',
        'skip_apple_id': 'bool',
        'skipi_cloud_storage': 'bool',
        'skip_privacy': 'bool',
        'skip_screen_time': 'bool',
        'skip_siri': 'bool',
        'skip_touch_id': 'bool',
        'skip_true_tone': 'bool'
    }

    attribute_map = {
        'skip_appearance': 'SkipAppearance',
        'skip_apple_id': 'SkipAppleID',
        'skipi_cloud_storage': 'SkipiCloudStorage',
        'skip_privacy': 'SkipPrivacy',
        'skip_screen_time': 'SkipScreenTime',
        'skip_siri': 'SkipSiri',
        'skip_touch_id': 'SkipTouchID',
        'skip_true_tone': 'SkipTrueTone'
    }

    def __init__(self, skip_appearance=None, skip_apple_id=None, skipi_cloud_storage=None, skip_privacy=None, skip_screen_time=None, skip_siri=None, skip_touch_id=None, skip_true_tone=None, _configuration=None):  # noqa: E501
        """MacOsSetupAssistantPayloadEntity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._skip_appearance = None
        self._skip_apple_id = None
        self._skipi_cloud_storage = None
        self._skip_privacy = None
        self._skip_screen_time = None
        self._skip_siri = None
        self._skip_touch_id = None
        self._skip_true_tone = None
        self.discriminator = None

        if skip_appearance is not None:
            self.skip_appearance = skip_appearance
        if skip_apple_id is not None:
            self.skip_apple_id = skip_apple_id
        if skipi_cloud_storage is not None:
            self.skipi_cloud_storage = skipi_cloud_storage
        if skip_privacy is not None:
            self.skip_privacy = skip_privacy
        if skip_screen_time is not None:
            self.skip_screen_time = skip_screen_time
        if skip_siri is not None:
            self.skip_siri = skip_siri
        if skip_touch_id is not None:
            self.skip_touch_id = skip_touch_id
        if skip_true_tone is not None:
            self.skip_true_tone = skip_true_tone

    @property
    def skip_appearance(self):
        """Gets the skip_appearance of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether Appearance screen has to be skipped.  # noqa: E501

        :return: The skip_appearance of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._skip_appearance

    @skip_appearance.setter
    def skip_appearance(self, skip_appearance):
        """Sets the skip_appearance of this MacOsSetupAssistantPayloadEntity_.

        Gets or sets a value indicating whether Appearance screen has to be skipped.  # noqa: E501

        :param skip_appearance: The skip_appearance of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._skip_appearance = skip_appearance

    @property
    def skip_apple_id(self):
        """Gets the skip_apple_id of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether the Apple ID screen has to be skipped.  # noqa: E501

        :return: The skip_apple_id of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._skip_apple_id

    @skip_apple_id.setter
    def skip_apple_id(self, skip_apple_id):
        """Sets the skip_apple_id of this MacOsSetupAssistantPayloadEntity_.

        Gets or sets a value indicating whether the Apple ID screen has to be skipped.  # noqa: E501

        :param skip_apple_id: The skip_apple_id of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._skip_apple_id = skip_apple_id

    @property
    def skipi_cloud_storage(self):
        """Gets the skipi_cloud_storage of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether the iCloud storage screen has to be skipped.  # noqa: E501

        :return: The skipi_cloud_storage of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._skipi_cloud_storage

    @skipi_cloud_storage.setter
    def skipi_cloud_storage(self, skipi_cloud_storage):
        """Sets the skipi_cloud_storage of this MacOsSetupAssistantPayloadEntity_.

        Gets or sets a value indicating whether the iCloud storage screen has to be skipped.  # noqa: E501

        :param skipi_cloud_storage: The skipi_cloud_storage of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._skipi_cloud_storage = skipi_cloud_storage

    @property
    def skip_privacy(self):
        """Gets the skip_privacy of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether Privacy screen has to be skipped.  # noqa: E501

        :return: The skip_privacy of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._skip_privacy

    @skip_privacy.setter
    def skip_privacy(self, skip_privacy):
        """Sets the skip_privacy of this MacOsSetupAssistantPayloadEntity_.

        Gets or sets a value indicating whether Privacy screen has to be skipped.  # noqa: E501

        :param skip_privacy: The skip_privacy of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._skip_privacy = skip_privacy

    @property
    def skip_screen_time(self):
        """Gets the skip_screen_time of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether the Screen Time screen has to be skipped.  # noqa: E501

        :return: The skip_screen_time of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._skip_screen_time

    @skip_screen_time.setter
    def skip_screen_time(self, skip_screen_time):
        """Sets the skip_screen_time of this MacOsSetupAssistantPayloadEntity_.

        Gets or sets a value indicating whether the Screen Time screen has to be skipped.  # noqa: E501

        :param skip_screen_time: The skip_screen_time of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._skip_screen_time = skip_screen_time

    @property
    def skip_siri(self):
        """Gets the skip_siri of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether the Siri screen has to be skipped.  # noqa: E501

        :return: The skip_siri of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._skip_siri

    @skip_siri.setter
    def skip_siri(self, skip_siri):
        """Sets the skip_siri of this MacOsSetupAssistantPayloadEntity_.

        Gets or sets a value indicating whether the Siri screen has to be skipped.  # noqa: E501

        :param skip_siri: The skip_siri of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._skip_siri = skip_siri

    @property
    def skip_touch_id(self):
        """Gets the skip_touch_id of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether the Touch ID has to be skipped.  # noqa: E501

        :return: The skip_touch_id of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._skip_touch_id

    @skip_touch_id.setter
    def skip_touch_id(self, skip_touch_id):
        """Sets the skip_touch_id of this MacOsSetupAssistantPayloadEntity_.

        Gets or sets a value indicating whether the Touch ID has to be skipped.  # noqa: E501

        :param skip_touch_id: The skip_touch_id of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._skip_touch_id = skip_touch_id

    @property
    def skip_true_tone(self):
        """Gets the skip_true_tone of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether the True Tone screen has to be skipped.  # noqa: E501

        :return: The skip_true_tone of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._skip_true_tone

    @skip_true_tone.setter
    def skip_true_tone(self, skip_true_tone):
        """Sets the skip_true_tone of this MacOsSetupAssistantPayloadEntity_.

        Gets or sets a value indicating whether the True Tone screen has to be skipped.  # noqa: E501

        :param skip_true_tone: The skip_true_tone of this MacOsSetupAssistantPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._skip_true_tone = skip_true_tone

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
        if issubclass(MacOsSetupAssistantPayloadEntity_, dict):
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
        if not isinstance(other, MacOsSetupAssistantPayloadEntity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MacOsSetupAssistantPayloadEntity_):
            return True

        return self.to_dict() != other.to_dict()
