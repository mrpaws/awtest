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


class AndroidForWorkOemRestrictionsPayloadV2Entity(object):
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
        'allow_airplane_mode': 'bool',
        'allow_mock_locations': 'bool',
        'allow_background_data': 'bool',
        'allow_wifi_disconnect_during_sleep': 'int',
        'allow_roaming_data': 'bool',
        'force_wifi_on': 'bool',
        'allow_bluetooth': 'bool',
        'allow_clipboard': 'bool',
        'allow_network_monitored_notification': 'bool'
    }

    attribute_map = {
        'allow_airplane_mode': 'AllowAirplaneMode',
        'allow_mock_locations': 'AllowMockLocations',
        'allow_background_data': 'AllowBackgroundData',
        'allow_wifi_disconnect_during_sleep': 'AllowWifiDisconnectDuringSleep',
        'allow_roaming_data': 'AllowRoamingData',
        'force_wifi_on': 'ForceWifiOn',
        'allow_bluetooth': 'AllowBluetooth',
        'allow_clipboard': 'AllowClipboard',
        'allow_network_monitored_notification': 'AllowNetworkMonitoredNotification'
    }

    def __init__(self, allow_airplane_mode=None, allow_mock_locations=None, allow_background_data=None, allow_wifi_disconnect_during_sleep=None, allow_roaming_data=None, force_wifi_on=None, allow_bluetooth=None, allow_clipboard=None, allow_network_monitored_notification=None, _configuration=None):  # noqa: E501
        """AndroidForWorkOemRestrictionsPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_airplane_mode = None
        self._allow_mock_locations = None
        self._allow_background_data = None
        self._allow_wifi_disconnect_during_sleep = None
        self._allow_roaming_data = None
        self._force_wifi_on = None
        self._allow_bluetooth = None
        self._allow_clipboard = None
        self._allow_network_monitored_notification = None
        self.discriminator = None

        if allow_airplane_mode is not None:
            self.allow_airplane_mode = allow_airplane_mode
        if allow_mock_locations is not None:
            self.allow_mock_locations = allow_mock_locations
        if allow_background_data is not None:
            self.allow_background_data = allow_background_data
        if allow_wifi_disconnect_during_sleep is not None:
            self.allow_wifi_disconnect_during_sleep = allow_wifi_disconnect_during_sleep
        if allow_roaming_data is not None:
            self.allow_roaming_data = allow_roaming_data
        if force_wifi_on is not None:
            self.force_wifi_on = force_wifi_on
        if allow_bluetooth is not None:
            self.allow_bluetooth = allow_bluetooth
        if allow_clipboard is not None:
            self.allow_clipboard = allow_clipboard
        if allow_network_monitored_notification is not None:
            self.allow_network_monitored_notification = allow_network_monitored_notification

    @property
    def allow_airplane_mode(self):
        """Gets the allow_airplane_mode of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether allow Airplane mode.  # noqa: E501

        :return: The allow_airplane_mode of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_airplane_mode

    @allow_airplane_mode.setter
    def allow_airplane_mode(self, allow_airplane_mode):
        """Sets the allow_airplane_mode of this AndroidForWorkOemRestrictionsPayloadV2Entity.

        Gets or sets a value indicating whether allow Airplane mode.  # noqa: E501

        :param allow_airplane_mode: The allow_airplane_mode of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_airplane_mode = allow_airplane_mode

    @property
    def allow_mock_locations(self):
        """Gets the allow_mock_locations of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether allow Mock locations.  # noqa: E501

        :return: The allow_mock_locations of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_mock_locations

    @allow_mock_locations.setter
    def allow_mock_locations(self, allow_mock_locations):
        """Sets the allow_mock_locations of this AndroidForWorkOemRestrictionsPayloadV2Entity.

        Gets or sets a value indicating whether allow Mock locations.  # noqa: E501

        :param allow_mock_locations: The allow_mock_locations of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_mock_locations = allow_mock_locations

    @property
    def allow_background_data(self):
        """Gets the allow_background_data of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether allow Background data.  # noqa: E501

        :return: The allow_background_data of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_background_data

    @allow_background_data.setter
    def allow_background_data(self, allow_background_data):
        """Sets the allow_background_data of this AndroidForWorkOemRestrictionsPayloadV2Entity.

        Gets or sets a value indicating whether allow Background data.  # noqa: E501

        :param allow_background_data: The allow_background_data of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_background_data = allow_background_data

    @property
    def allow_wifi_disconnect_during_sleep(self):
        """Gets the allow_wifi_disconnect_during_sleep of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501

        Gets or sets allow wifi disconnect during sleep.  # noqa: E501

        :return: The allow_wifi_disconnect_during_sleep of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._allow_wifi_disconnect_during_sleep

    @allow_wifi_disconnect_during_sleep.setter
    def allow_wifi_disconnect_during_sleep(self, allow_wifi_disconnect_during_sleep):
        """Sets the allow_wifi_disconnect_during_sleep of this AndroidForWorkOemRestrictionsPayloadV2Entity.

        Gets or sets allow wifi disconnect during sleep.  # noqa: E501

        :param allow_wifi_disconnect_during_sleep: The allow_wifi_disconnect_during_sleep of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._allow_wifi_disconnect_during_sleep = allow_wifi_disconnect_during_sleep

    @property
    def allow_roaming_data(self):
        """Gets the allow_roaming_data of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether allow roaming data.  # noqa: E501

        :return: The allow_roaming_data of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_roaming_data

    @allow_roaming_data.setter
    def allow_roaming_data(self, allow_roaming_data):
        """Sets the allow_roaming_data of this AndroidForWorkOemRestrictionsPayloadV2Entity.

        Gets or sets a value indicating whether allow roaming data.  # noqa: E501

        :param allow_roaming_data: The allow_roaming_data of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_roaming_data = allow_roaming_data

    @property
    def force_wifi_on(self):
        """Gets the force_wifi_on of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether force wifi ON to use data.  # noqa: E501

        :return: The force_wifi_on of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._force_wifi_on

    @force_wifi_on.setter
    def force_wifi_on(self, force_wifi_on):
        """Sets the force_wifi_on of this AndroidForWorkOemRestrictionsPayloadV2Entity.

        Gets or sets a value indicating whether force wifi ON to use data.  # noqa: E501

        :param force_wifi_on: The force_wifi_on of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._force_wifi_on = force_wifi_on

    @property
    def allow_bluetooth(self):
        """Gets the allow_bluetooth of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether allow bluetooth.  # noqa: E501

        :return: The allow_bluetooth of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_bluetooth

    @allow_bluetooth.setter
    def allow_bluetooth(self, allow_bluetooth):
        """Sets the allow_bluetooth of this AndroidForWorkOemRestrictionsPayloadV2Entity.

        Gets or sets a value indicating whether allow bluetooth.  # noqa: E501

        :param allow_bluetooth: The allow_bluetooth of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_bluetooth = allow_bluetooth

    @property
    def allow_clipboard(self):
        """Gets the allow_clipboard of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether allow clipboard.  # noqa: E501

        :return: The allow_clipboard of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_clipboard

    @allow_clipboard.setter
    def allow_clipboard(self, allow_clipboard):
        """Sets the allow_clipboard of this AndroidForWorkOemRestrictionsPayloadV2Entity.

        Gets or sets a value indicating whether allow clipboard.  # noqa: E501

        :param allow_clipboard: The allow_clipboard of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_clipboard = allow_clipboard

    @property
    def allow_network_monitored_notification(self):
        """Gets the allow_network_monitored_notification of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether allow network monitor warning.  # noqa: E501

        :return: The allow_network_monitored_notification of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_network_monitored_notification

    @allow_network_monitored_notification.setter
    def allow_network_monitored_notification(self, allow_network_monitored_notification):
        """Sets the allow_network_monitored_notification of this AndroidForWorkOemRestrictionsPayloadV2Entity.

        Gets or sets a value indicating whether allow network monitor warning.  # noqa: E501

        :param allow_network_monitored_notification: The allow_network_monitored_notification of this AndroidForWorkOemRestrictionsPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_network_monitored_notification = allow_network_monitored_notification

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
        if issubclass(AndroidForWorkOemRestrictionsPayloadV2Entity, dict):
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
        if not isinstance(other, AndroidForWorkOemRestrictionsPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkOemRestrictionsPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
