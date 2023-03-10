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


class AppNotificationV2Entity_(object):
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
        'bundle_identifier': 'str',
        'notifications_enabled': 'bool',
        'show_in_notification_center': 'bool',
        'show_in_lock_screen': 'bool',
        'badges_enabled': 'bool',
        'sounds_enabled': 'bool',
        'critical_alert_enabled': 'bool',
        'show_in_car_play': 'bool',
        'alert_type': 'int',
        'group_notification_type': 'int',
        'preview_notification_type': 'int'
    }

    attribute_map = {
        'bundle_identifier': 'BundleIdentifier',
        'notifications_enabled': 'NotificationsEnabled',
        'show_in_notification_center': 'ShowInNotificationCenter',
        'show_in_lock_screen': 'ShowInLockScreen',
        'badges_enabled': 'BadgesEnabled',
        'sounds_enabled': 'SoundsEnabled',
        'critical_alert_enabled': 'CriticalAlertEnabled',
        'show_in_car_play': 'ShowInCarPlay',
        'alert_type': 'AlertType',
        'group_notification_type': 'GroupNotificationType',
        'preview_notification_type': 'PreviewNotificationType'
    }

    def __init__(self, bundle_identifier=None, notifications_enabled=None, show_in_notification_center=None, show_in_lock_screen=None, badges_enabled=None, sounds_enabled=None, critical_alert_enabled=None, show_in_car_play=None, alert_type=None, group_notification_type=None, preview_notification_type=None, _configuration=None):  # noqa: E501
        """AppNotificationV2Entity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bundle_identifier = None
        self._notifications_enabled = None
        self._show_in_notification_center = None
        self._show_in_lock_screen = None
        self._badges_enabled = None
        self._sounds_enabled = None
        self._critical_alert_enabled = None
        self._show_in_car_play = None
        self._alert_type = None
        self._group_notification_type = None
        self._preview_notification_type = None
        self.discriminator = None

        if bundle_identifier is not None:
            self.bundle_identifier = bundle_identifier
        if notifications_enabled is not None:
            self.notifications_enabled = notifications_enabled
        if show_in_notification_center is not None:
            self.show_in_notification_center = show_in_notification_center
        if show_in_lock_screen is not None:
            self.show_in_lock_screen = show_in_lock_screen
        if badges_enabled is not None:
            self.badges_enabled = badges_enabled
        if sounds_enabled is not None:
            self.sounds_enabled = sounds_enabled
        if critical_alert_enabled is not None:
            self.critical_alert_enabled = critical_alert_enabled
        if show_in_car_play is not None:
            self.show_in_car_play = show_in_car_play
        if alert_type is not None:
            self.alert_type = alert_type
        if group_notification_type is not None:
            self.group_notification_type = group_notification_type
        if preview_notification_type is not None:
            self.preview_notification_type = preview_notification_type

    @property
    def bundle_identifier(self):
        """Gets the bundle_identifier of this AppNotificationV2Entity_.  # noqa: E501

        Gets or sets bundle identifier of app to which to apply these notification settings.  # noqa: E501

        :return: The bundle_identifier of this AppNotificationV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._bundle_identifier

    @bundle_identifier.setter
    def bundle_identifier(self, bundle_identifier):
        """Sets the bundle_identifier of this AppNotificationV2Entity_.

        Gets or sets bundle identifier of app to which to apply these notification settings.  # noqa: E501

        :param bundle_identifier: The bundle_identifier of this AppNotificationV2Entity_.  # noqa: E501
        :type: str
        """

        self._bundle_identifier = bundle_identifier

    @property
    def notifications_enabled(self):
        """Gets the notifications_enabled of this AppNotificationV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether whether notifications are allowed for this app.  # noqa: E501

        :return: The notifications_enabled of this AppNotificationV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._notifications_enabled

    @notifications_enabled.setter
    def notifications_enabled(self, notifications_enabled):
        """Sets the notifications_enabled of this AppNotificationV2Entity_.

        Gets or sets a value indicating whether whether notifications are allowed for this app.  # noqa: E501

        :param notifications_enabled: The notifications_enabled of this AppNotificationV2Entity_.  # noqa: E501
        :type: bool
        """

        self._notifications_enabled = notifications_enabled

    @property
    def show_in_notification_center(self):
        """Gets the show_in_notification_center of this AppNotificationV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether whether notifications can be shown in notification center.  # noqa: E501

        :return: The show_in_notification_center of this AppNotificationV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_notification_center

    @show_in_notification_center.setter
    def show_in_notification_center(self, show_in_notification_center):
        """Sets the show_in_notification_center of this AppNotificationV2Entity_.

        Gets or sets a value indicating whether whether notifications can be shown in notification center.  # noqa: E501

        :param show_in_notification_center: The show_in_notification_center of this AppNotificationV2Entity_.  # noqa: E501
        :type: bool
        """

        self._show_in_notification_center = show_in_notification_center

    @property
    def show_in_lock_screen(self):
        """Gets the show_in_lock_screen of this AppNotificationV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether whether notifications can be shown in the lock screen.  # noqa: E501

        :return: The show_in_lock_screen of this AppNotificationV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_lock_screen

    @show_in_lock_screen.setter
    def show_in_lock_screen(self, show_in_lock_screen):
        """Sets the show_in_lock_screen of this AppNotificationV2Entity_.

        Gets or sets a value indicating whether whether notifications can be shown in the lock screen.  # noqa: E501

        :param show_in_lock_screen: The show_in_lock_screen of this AppNotificationV2Entity_.  # noqa: E501
        :type: bool
        """

        self._show_in_lock_screen = show_in_lock_screen

    @property
    def badges_enabled(self):
        """Gets the badges_enabled of this AppNotificationV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether whether badges are allowed for this app.  # noqa: E501

        :return: The badges_enabled of this AppNotificationV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._badges_enabled

    @badges_enabled.setter
    def badges_enabled(self, badges_enabled):
        """Sets the badges_enabled of this AppNotificationV2Entity_.

        Gets or sets a value indicating whether whether badges are allowed for this app.  # noqa: E501

        :param badges_enabled: The badges_enabled of this AppNotificationV2Entity_.  # noqa: E501
        :type: bool
        """

        self._badges_enabled = badges_enabled

    @property
    def sounds_enabled(self):
        """Gets the sounds_enabled of this AppNotificationV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether whether sounds are allowed for this app.  # noqa: E501

        :return: The sounds_enabled of this AppNotificationV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._sounds_enabled

    @sounds_enabled.setter
    def sounds_enabled(self, sounds_enabled):
        """Sets the sounds_enabled of this AppNotificationV2Entity_.

        Gets or sets a value indicating whether whether sounds are allowed for this app.  # noqa: E501

        :param sounds_enabled: The sounds_enabled of this AppNotificationV2Entity_.  # noqa: E501
        :type: bool
        """

        self._sounds_enabled = sounds_enabled

    @property
    def critical_alert_enabled(self):
        """Gets the critical_alert_enabled of this AppNotificationV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether gets or sets a value which indicates whether an app can bypass \"Do Not Disturb\" and ringer settings or not.  # noqa: E501

        :return: The critical_alert_enabled of this AppNotificationV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._critical_alert_enabled

    @critical_alert_enabled.setter
    def critical_alert_enabled(self, critical_alert_enabled):
        """Sets the critical_alert_enabled of this AppNotificationV2Entity_.

        Gets or sets a value indicating whether gets or sets a value which indicates whether an app can bypass \"Do Not Disturb\" and ringer settings or not.  # noqa: E501

        :param critical_alert_enabled: The critical_alert_enabled of this AppNotificationV2Entity_.  # noqa: E501
        :type: bool
        """

        self._critical_alert_enabled = critical_alert_enabled

    @property
    def show_in_car_play(self):
        """Gets the show_in_car_play of this AppNotificationV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether gets or sets a value which indicates whether an app can bypass \"Do Not Disturb\" and ringer settings or not.  # noqa: E501

        :return: The show_in_car_play of this AppNotificationV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_car_play

    @show_in_car_play.setter
    def show_in_car_play(self, show_in_car_play):
        """Sets the show_in_car_play of this AppNotificationV2Entity_.

        Gets or sets a value indicating whether gets or sets a value which indicates whether an app can bypass \"Do Not Disturb\" and ringer settings or not.  # noqa: E501

        :param show_in_car_play: The show_in_car_play of this AppNotificationV2Entity_.  # noqa: E501
        :type: bool
        """

        self._show_in_car_play = show_in_car_play

    @property
    def alert_type(self):
        """Gets the alert_type of this AppNotificationV2Entity_.  # noqa: E501

        Gets or sets the type of alert for notifications for this app: 0: None 1: Banner 2: Modal Alert.  # noqa: E501

        :return: The alert_type of this AppNotificationV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this AppNotificationV2Entity_.

        Gets or sets the type of alert for notifications for this app: 0: None 1: Banner 2: Modal Alert.  # noqa: E501

        :param alert_type: The alert_type of this AppNotificationV2Entity_.  # noqa: E501
        :type: int
        """

        self._alert_type = alert_type

    @property
    def group_notification_type(self):
        """Gets the group_notification_type of this AppNotificationV2Entity_.  # noqa: E501

        Gets or sets group notification type  0: Group into app specified groups  1: Group into one group  2: Do not group.  # noqa: E501

        :return: The group_notification_type of this AppNotificationV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._group_notification_type

    @group_notification_type.setter
    def group_notification_type(self, group_notification_type):
        """Sets the group_notification_type of this AppNotificationV2Entity_.

        Gets or sets group notification type  0: Group into app specified groups  1: Group into one group  2: Do not group.  # noqa: E501

        :param group_notification_type: The group_notification_type of this AppNotificationV2Entity_.  # noqa: E501
        :type: int
        """

        self._group_notification_type = group_notification_type

    @property
    def preview_notification_type(self):
        """Gets the preview_notification_type of this AppNotificationV2Entity_.  # noqa: E501

        Gets or sets preview notification type  0: Always preview notification  1: When the device is unlocked  2: Never.  # noqa: E501

        :return: The preview_notification_type of this AppNotificationV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._preview_notification_type

    @preview_notification_type.setter
    def preview_notification_type(self, preview_notification_type):
        """Sets the preview_notification_type of this AppNotificationV2Entity_.

        Gets or sets preview notification type  0: Always preview notification  1: When the device is unlocked  2: Never.  # noqa: E501

        :param preview_notification_type: The preview_notification_type of this AppNotificationV2Entity_.  # noqa: E501
        :type: int
        """

        self._preview_notification_type = preview_notification_type

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
        if issubclass(AppNotificationV2Entity_, dict):
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
        if not isinstance(other, AppNotificationV2Entity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppNotificationV2Entity_):
            return True

        return self.to_dict() != other.to_dict()
