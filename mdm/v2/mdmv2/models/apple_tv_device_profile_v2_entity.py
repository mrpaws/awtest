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


class AppleTvDeviceProfileV2Entity(object):
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
        'conference_room_display': 'AppleTvConferenceModePayloadV2Entity',
        'single_app_mode': 'AppleTvSingleAppModePayloadV2Entity',
        'general': 'GeneralPayloadV2Entity'
    }

    attribute_map = {
        'conference_room_display': 'conferenceRoomDisplay',
        'single_app_mode': 'singleAppMode',
        'general': 'General'
    }

    def __init__(self, conference_room_display=None, single_app_mode=None, general=None, _configuration=None):  # noqa: E501
        """AppleTvDeviceProfileV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._conference_room_display = None
        self._single_app_mode = None
        self._general = None
        self.discriminator = None

        if conference_room_display is not None:
            self.conference_room_display = conference_room_display
        if single_app_mode is not None:
            self.single_app_mode = single_app_mode
        if general is not None:
            self.general = general

    @property
    def conference_room_display(self):
        """Gets the conference_room_display of this AppleTvDeviceProfileV2Entity.  # noqa: E501


        :return: The conference_room_display of this AppleTvDeviceProfileV2Entity.  # noqa: E501
        :rtype: AppleTvConferenceModePayloadV2Entity
        """
        return self._conference_room_display

    @conference_room_display.setter
    def conference_room_display(self, conference_room_display):
        """Sets the conference_room_display of this AppleTvDeviceProfileV2Entity.


        :param conference_room_display: The conference_room_display of this AppleTvDeviceProfileV2Entity.  # noqa: E501
        :type: AppleTvConferenceModePayloadV2Entity
        """

        self._conference_room_display = conference_room_display

    @property
    def single_app_mode(self):
        """Gets the single_app_mode of this AppleTvDeviceProfileV2Entity.  # noqa: E501


        :return: The single_app_mode of this AppleTvDeviceProfileV2Entity.  # noqa: E501
        :rtype: AppleTvSingleAppModePayloadV2Entity
        """
        return self._single_app_mode

    @single_app_mode.setter
    def single_app_mode(self, single_app_mode):
        """Sets the single_app_mode of this AppleTvDeviceProfileV2Entity.


        :param single_app_mode: The single_app_mode of this AppleTvDeviceProfileV2Entity.  # noqa: E501
        :type: AppleTvSingleAppModePayloadV2Entity
        """

        self._single_app_mode = single_app_mode

    @property
    def general(self):
        """Gets the general of this AppleTvDeviceProfileV2Entity.  # noqa: E501


        :return: The general of this AppleTvDeviceProfileV2Entity.  # noqa: E501
        :rtype: GeneralPayloadV2Entity
        """
        return self._general

    @general.setter
    def general(self, general):
        """Sets the general of this AppleTvDeviceProfileV2Entity.


        :param general: The general of this AppleTvDeviceProfileV2Entity.  # noqa: E501
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
        if issubclass(AppleTvDeviceProfileV2Entity, dict):
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
        if not isinstance(other, AppleTvDeviceProfileV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleTvDeviceProfileV2Entity):
            return True

        return self.to_dict() != other.to_dict()
