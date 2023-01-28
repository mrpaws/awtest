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


class AppleOsXDiskEncryptionAirWatchPayloadEntity_(object):
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
        'store_key': 'bool',
        'rotate_key_after': 'int',
        'use_intelligent_hub': 'bool',
        'notify_user_for_encryption': 'bool',
        'encryption_notification_title': 'str',
        'encryption_notification_message': 'str',
        'encryption_max_notify_attempts': 'int',
        'encryption_notification_retry_interval_in_hours': 'int',
        'encryption_action_after_last_notification': 'int',
        'enable_recovery_key': 'bool',
        'recovery_key_notification_title': 'str',
        'recovery_key_notification_message': 'str',
        'recovery_key_notification_retry_interval_in_hours': 'int',
        'recovery_key_prompt_title': 'str',
        'recovery_key_prompt_message': 'str',
        'recovery_key_success_title': 'str',
        'recovery_key_success_message': 'str',
        'recovery_key_error_title': 'str',
        'recovery_key_error_message': 'str',
        'recovery_key_max_failure_count': 'int'
    }

    attribute_map = {
        'store_key': 'StoreKey',
        'rotate_key_after': 'RotateKeyAfter',
        'use_intelligent_hub': 'UseIntelligentHub',
        'notify_user_for_encryption': 'NotifyUserForEncryption',
        'encryption_notification_title': 'EncryptionNotificationTitle',
        'encryption_notification_message': 'EncryptionNotificationMessage',
        'encryption_max_notify_attempts': 'EncryptionMaxNotifyAttempts',
        'encryption_notification_retry_interval_in_hours': 'EncryptionNotificationRetryIntervalInHours',
        'encryption_action_after_last_notification': 'EncryptionActionAfterLastNotification',
        'enable_recovery_key': 'EnableRecoveryKey',
        'recovery_key_notification_title': 'RecoveryKeyNotificationTitle',
        'recovery_key_notification_message': 'RecoveryKeyNotificationMessage',
        'recovery_key_notification_retry_interval_in_hours': 'RecoveryKeyNotificationRetryIntervalInHours',
        'recovery_key_prompt_title': 'RecoveryKeyPromptTitle',
        'recovery_key_prompt_message': 'RecoveryKeyPromptMessage',
        'recovery_key_success_title': 'RecoveryKeySuccessTitle',
        'recovery_key_success_message': 'RecoveryKeySuccessMessage',
        'recovery_key_error_title': 'RecoveryKeyErrorTitle',
        'recovery_key_error_message': 'RecoveryKeyErrorMessage',
        'recovery_key_max_failure_count': 'RecoveryKeyMaxFailureCount'
    }

    def __init__(self, store_key=None, rotate_key_after=None, use_intelligent_hub=None, notify_user_for_encryption=None, encryption_notification_title=None, encryption_notification_message=None, encryption_max_notify_attempts=None, encryption_notification_retry_interval_in_hours=None, encryption_action_after_last_notification=None, enable_recovery_key=None, recovery_key_notification_title=None, recovery_key_notification_message=None, recovery_key_notification_retry_interval_in_hours=None, recovery_key_prompt_title=None, recovery_key_prompt_message=None, recovery_key_success_title=None, recovery_key_success_message=None, recovery_key_error_title=None, recovery_key_error_message=None, recovery_key_max_failure_count=None, _configuration=None):  # noqa: E501
        """AppleOsXDiskEncryptionAirWatchPayloadEntity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._store_key = None
        self._rotate_key_after = None
        self._use_intelligent_hub = None
        self._notify_user_for_encryption = None
        self._encryption_notification_title = None
        self._encryption_notification_message = None
        self._encryption_max_notify_attempts = None
        self._encryption_notification_retry_interval_in_hours = None
        self._encryption_action_after_last_notification = None
        self._enable_recovery_key = None
        self._recovery_key_notification_title = None
        self._recovery_key_notification_message = None
        self._recovery_key_notification_retry_interval_in_hours = None
        self._recovery_key_prompt_title = None
        self._recovery_key_prompt_message = None
        self._recovery_key_success_title = None
        self._recovery_key_success_message = None
        self._recovery_key_error_title = None
        self._recovery_key_error_message = None
        self._recovery_key_max_failure_count = None
        self.discriminator = None

        if store_key is not None:
            self.store_key = store_key
        if rotate_key_after is not None:
            self.rotate_key_after = rotate_key_after
        if use_intelligent_hub is not None:
            self.use_intelligent_hub = use_intelligent_hub
        if notify_user_for_encryption is not None:
            self.notify_user_for_encryption = notify_user_for_encryption
        if encryption_notification_title is not None:
            self.encryption_notification_title = encryption_notification_title
        if encryption_notification_message is not None:
            self.encryption_notification_message = encryption_notification_message
        if encryption_max_notify_attempts is not None:
            self.encryption_max_notify_attempts = encryption_max_notify_attempts
        if encryption_notification_retry_interval_in_hours is not None:
            self.encryption_notification_retry_interval_in_hours = encryption_notification_retry_interval_in_hours
        if encryption_action_after_last_notification is not None:
            self.encryption_action_after_last_notification = encryption_action_after_last_notification
        if enable_recovery_key is not None:
            self.enable_recovery_key = enable_recovery_key
        if recovery_key_notification_title is not None:
            self.recovery_key_notification_title = recovery_key_notification_title
        if recovery_key_notification_message is not None:
            self.recovery_key_notification_message = recovery_key_notification_message
        if recovery_key_notification_retry_interval_in_hours is not None:
            self.recovery_key_notification_retry_interval_in_hours = recovery_key_notification_retry_interval_in_hours
        if recovery_key_prompt_title is not None:
            self.recovery_key_prompt_title = recovery_key_prompt_title
        if recovery_key_prompt_message is not None:
            self.recovery_key_prompt_message = recovery_key_prompt_message
        if recovery_key_success_title is not None:
            self.recovery_key_success_title = recovery_key_success_title
        if recovery_key_success_message is not None:
            self.recovery_key_success_message = recovery_key_success_message
        if recovery_key_error_title is not None:
            self.recovery_key_error_title = recovery_key_error_title
        if recovery_key_error_message is not None:
            self.recovery_key_error_message = recovery_key_error_message
        if recovery_key_max_failure_count is not None:
            self.recovery_key_max_failure_count = recovery_key_max_failure_count

    @property
    def store_key(self):
        """Gets the store_key of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets indicates whether the recovery key should be stored in AirWatch.  # noqa: E501

        :return: The store_key of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._store_key

    @store_key.setter
    def store_key(self, store_key):
        """Sets the store_key of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets indicates whether the recovery key should be stored in AirWatch.  # noqa: E501

        :param store_key: The store_key of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._store_key = store_key

    @property
    def rotate_key_after(self):
        """Gets the rotate_key_after of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets the number of days until the recovery key rotates.  # noqa: E501

        :return: The rotate_key_after of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: int
        """
        return self._rotate_key_after

    @rotate_key_after.setter
    def rotate_key_after(self, rotate_key_after):
        """Sets the rotate_key_after of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets the number of days until the recovery key rotates.  # noqa: E501

        :param rotate_key_after: The rotate_key_after of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: int
        """

        self._rotate_key_after = rotate_key_after

    @property
    def use_intelligent_hub(self):
        """Gets the use_intelligent_hub of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets indicate whether to use the intelligent hub for enforcement.  # noqa: E501

        :return: The use_intelligent_hub of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._use_intelligent_hub

    @use_intelligent_hub.setter
    def use_intelligent_hub(self, use_intelligent_hub):
        """Sets the use_intelligent_hub of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets indicate whether to use the intelligent hub for enforcement.  # noqa: E501

        :param use_intelligent_hub: The use_intelligent_hub of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._use_intelligent_hub = use_intelligent_hub

    @property
    def notify_user_for_encryption(self):
        """Gets the notify_user_for_encryption of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets indicate whether to notify the user if encryption is disabled.  # noqa: E501

        :return: The notify_user_for_encryption of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._notify_user_for_encryption

    @notify_user_for_encryption.setter
    def notify_user_for_encryption(self, notify_user_for_encryption):
        """Sets the notify_user_for_encryption of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets indicate whether to notify the user if encryption is disabled.  # noqa: E501

        :param notify_user_for_encryption: The notify_user_for_encryption of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._notify_user_for_encryption = notify_user_for_encryption

    @property
    def encryption_notification_title(self):
        """Gets the encryption_notification_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets notification title for encryption.  # noqa: E501

        :return: The encryption_notification_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._encryption_notification_title

    @encryption_notification_title.setter
    def encryption_notification_title(self, encryption_notification_title):
        """Sets the encryption_notification_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets notification title for encryption.  # noqa: E501

        :param encryption_notification_title: The encryption_notification_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                encryption_notification_title is not None and len(encryption_notification_title) > 29):
            raise ValueError("Invalid value for `encryption_notification_title`, length must be less than or equal to `29`")  # noqa: E501
        if (self._configuration.client_side_validation and
                encryption_notification_title is not None and len(encryption_notification_title) < 0):
            raise ValueError("Invalid value for `encryption_notification_title`, length must be greater than or equal to `0`")  # noqa: E501
        if (self._configuration.client_side_validation and
                encryption_notification_title is not None and not re.search(r'^[  a-zA-Z0-9_#,;:\'?.\"!@{}+-]*$', encryption_notification_title)):  # noqa: E501
            raise ValueError(r"Invalid value for `encryption_notification_title`, must be a follow pattern or equal to `/^[  a-zA-Z0-9_#,;:'?.\"!@{}+-]*$/`")  # noqa: E501

        self._encryption_notification_title = encryption_notification_title

    @property
    def encryption_notification_message(self):
        """Gets the encryption_notification_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets notification message for encryption.  # noqa: E501

        :return: The encryption_notification_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._encryption_notification_message

    @encryption_notification_message.setter
    def encryption_notification_message(self, encryption_notification_message):
        """Sets the encryption_notification_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets notification message for encryption.  # noqa: E501

        :param encryption_notification_message: The encryption_notification_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                encryption_notification_message is not None and not re.search(r'^[  a-zA-Z0-9_#,;:\'?.\"!@{}+-]*$', encryption_notification_message)):  # noqa: E501
            raise ValueError(r"Invalid value for `encryption_notification_message`, must be a follow pattern or equal to `/^[  a-zA-Z0-9_#,;:'?.\"!@{}+-]*$/`")  # noqa: E501

        self._encryption_notification_message = encryption_notification_message

    @property
    def encryption_max_notify_attempts(self):
        """Gets the encryption_max_notify_attempts of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets maximum number of times to display the notification for encryption.  # noqa: E501

        :return: The encryption_max_notify_attempts of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: int
        """
        return self._encryption_max_notify_attempts

    @encryption_max_notify_attempts.setter
    def encryption_max_notify_attempts(self, encryption_max_notify_attempts):
        """Sets the encryption_max_notify_attempts of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets maximum number of times to display the notification for encryption.  # noqa: E501

        :param encryption_max_notify_attempts: The encryption_max_notify_attempts of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: int
        """

        self._encryption_max_notify_attempts = encryption_max_notify_attempts

    @property
    def encryption_notification_retry_interval_in_hours(self):
        """Gets the encryption_notification_retry_interval_in_hours of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets retry interval in hours between dismissals of the notification for rotating recovery key.  # noqa: E501

        :return: The encryption_notification_retry_interval_in_hours of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: int
        """
        return self._encryption_notification_retry_interval_in_hours

    @encryption_notification_retry_interval_in_hours.setter
    def encryption_notification_retry_interval_in_hours(self, encryption_notification_retry_interval_in_hours):
        """Sets the encryption_notification_retry_interval_in_hours of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets retry interval in hours between dismissals of the notification for rotating recovery key.  # noqa: E501

        :param encryption_notification_retry_interval_in_hours: The encryption_notification_retry_interval_in_hours of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: int
        """

        self._encryption_notification_retry_interval_in_hours = encryption_notification_retry_interval_in_hours

    @property
    def encryption_action_after_last_notification(self):
        """Gets the encryption_action_after_last_notification of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets action to be taken after the dismissal of the last notification, Force Logout (1), Do Nothing (2).  # noqa: E501

        :return: The encryption_action_after_last_notification of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: int
        """
        return self._encryption_action_after_last_notification

    @encryption_action_after_last_notification.setter
    def encryption_action_after_last_notification(self, encryption_action_after_last_notification):
        """Sets the encryption_action_after_last_notification of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets action to be taken after the dismissal of the last notification, Force Logout (1), Do Nothing (2).  # noqa: E501

        :param encryption_action_after_last_notification: The encryption_action_after_last_notification of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if (self._configuration.client_side_validation and
                encryption_action_after_last_notification not in allowed_values):
            raise ValueError(
                "Invalid value for `encryption_action_after_last_notification` ({0}), must be one of {1}"  # noqa: E501
                .format(encryption_action_after_last_notification, allowed_values)
            )

        self._encryption_action_after_last_notification = encryption_action_after_last_notification

    @property
    def enable_recovery_key(self):
        """Gets the enable_recovery_key of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets indicate whether to prompt for the user's password if the encryption is enabled to rotate recovery key.  # noqa: E501

        :return: The enable_recovery_key of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._enable_recovery_key

    @enable_recovery_key.setter
    def enable_recovery_key(self, enable_recovery_key):
        """Sets the enable_recovery_key of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets indicate whether to prompt for the user's password if the encryption is enabled to rotate recovery key.  # noqa: E501

        :param enable_recovery_key: The enable_recovery_key of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._enable_recovery_key = enable_recovery_key

    @property
    def recovery_key_notification_title(self):
        """Gets the recovery_key_notification_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets notification title for rotating recovery key.  # noqa: E501

        :return: The recovery_key_notification_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._recovery_key_notification_title

    @recovery_key_notification_title.setter
    def recovery_key_notification_title(self, recovery_key_notification_title):
        """Sets the recovery_key_notification_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets notification title for rotating recovery key.  # noqa: E501

        :param recovery_key_notification_title: The recovery_key_notification_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                recovery_key_notification_title is not None and len(recovery_key_notification_title) > 29):
            raise ValueError("Invalid value for `recovery_key_notification_title`, length must be less than or equal to `29`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_notification_title is not None and len(recovery_key_notification_title) < 0):
            raise ValueError("Invalid value for `recovery_key_notification_title`, length must be greater than or equal to `0`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_notification_title is not None and not re.search(r'^[  a-zA-Z0-9_#,;:\'?.\"!@{}+-]*$', recovery_key_notification_title)):  # noqa: E501
            raise ValueError(r"Invalid value for `recovery_key_notification_title`, must be a follow pattern or equal to `/^[  a-zA-Z0-9_#,;:'?.\"!@{}+-]*$/`")  # noqa: E501

        self._recovery_key_notification_title = recovery_key_notification_title

    @property
    def recovery_key_notification_message(self):
        """Gets the recovery_key_notification_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets notification message for rotating recovery key.  # noqa: E501

        :return: The recovery_key_notification_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._recovery_key_notification_message

    @recovery_key_notification_message.setter
    def recovery_key_notification_message(self, recovery_key_notification_message):
        """Sets the recovery_key_notification_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets notification message for rotating recovery key.  # noqa: E501

        :param recovery_key_notification_message: The recovery_key_notification_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                recovery_key_notification_message is not None and not re.search(r'^[  a-zA-Z0-9_#,;:\'?.\"!@{}+-]*$', recovery_key_notification_message)):  # noqa: E501
            raise ValueError(r"Invalid value for `recovery_key_notification_message`, must be a follow pattern or equal to `/^[  a-zA-Z0-9_#,;:'?.\"!@{}+-]*$/`")  # noqa: E501

        self._recovery_key_notification_message = recovery_key_notification_message

    @property
    def recovery_key_notification_retry_interval_in_hours(self):
        """Gets the recovery_key_notification_retry_interval_in_hours of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets retry interval in hours between dismissals of the notification for rotating recovery key.  # noqa: E501

        :return: The recovery_key_notification_retry_interval_in_hours of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: int
        """
        return self._recovery_key_notification_retry_interval_in_hours

    @recovery_key_notification_retry_interval_in_hours.setter
    def recovery_key_notification_retry_interval_in_hours(self, recovery_key_notification_retry_interval_in_hours):
        """Sets the recovery_key_notification_retry_interval_in_hours of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets retry interval in hours between dismissals of the notification for rotating recovery key.  # noqa: E501

        :param recovery_key_notification_retry_interval_in_hours: The recovery_key_notification_retry_interval_in_hours of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: int
        """

        self._recovery_key_notification_retry_interval_in_hours = recovery_key_notification_retry_interval_in_hours

    @property
    def recovery_key_prompt_title(self):
        """Gets the recovery_key_prompt_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets prompt title for rotating recovery key.  # noqa: E501

        :return: The recovery_key_prompt_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._recovery_key_prompt_title

    @recovery_key_prompt_title.setter
    def recovery_key_prompt_title(self, recovery_key_prompt_title):
        """Sets the recovery_key_prompt_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets prompt title for rotating recovery key.  # noqa: E501

        :param recovery_key_prompt_title: The recovery_key_prompt_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                recovery_key_prompt_title is not None and len(recovery_key_prompt_title) > 50):
            raise ValueError("Invalid value for `recovery_key_prompt_title`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_prompt_title is not None and len(recovery_key_prompt_title) < 0):
            raise ValueError("Invalid value for `recovery_key_prompt_title`, length must be greater than or equal to `0`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_prompt_title is not None and not re.search(r'^[  a-zA-Z0-9_#,;:\'?.\"!@{}+-]*$', recovery_key_prompt_title)):  # noqa: E501
            raise ValueError(r"Invalid value for `recovery_key_prompt_title`, must be a follow pattern or equal to `/^[  a-zA-Z0-9_#,;:'?.\"!@{}+-]*$/`")  # noqa: E501

        self._recovery_key_prompt_title = recovery_key_prompt_title

    @property
    def recovery_key_prompt_message(self):
        """Gets the recovery_key_prompt_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets prompt message for rotating recovery key.  # noqa: E501

        :return: The recovery_key_prompt_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._recovery_key_prompt_message

    @recovery_key_prompt_message.setter
    def recovery_key_prompt_message(self, recovery_key_prompt_message):
        """Sets the recovery_key_prompt_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets prompt message for rotating recovery key.  # noqa: E501

        :param recovery_key_prompt_message: The recovery_key_prompt_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                recovery_key_prompt_message is not None and len(recovery_key_prompt_message) > 150):
            raise ValueError("Invalid value for `recovery_key_prompt_message`, length must be less than or equal to `150`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_prompt_message is not None and len(recovery_key_prompt_message) < 0):
            raise ValueError("Invalid value for `recovery_key_prompt_message`, length must be greater than or equal to `0`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_prompt_message is not None and not re.search(r'^[  a-zA-Z0-9_#,;:\'?.\"!@{}+-]*$', recovery_key_prompt_message)):  # noqa: E501
            raise ValueError(r"Invalid value for `recovery_key_prompt_message`, must be a follow pattern or equal to `/^[  a-zA-Z0-9_#,;:'?.\"!@{}+-]*$/`")  # noqa: E501

        self._recovery_key_prompt_message = recovery_key_prompt_message

    @property
    def recovery_key_success_title(self):
        """Gets the recovery_key_success_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets success title for rotating recovery key.  # noqa: E501

        :return: The recovery_key_success_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._recovery_key_success_title

    @recovery_key_success_title.setter
    def recovery_key_success_title(self, recovery_key_success_title):
        """Sets the recovery_key_success_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets success title for rotating recovery key.  # noqa: E501

        :param recovery_key_success_title: The recovery_key_success_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                recovery_key_success_title is not None and len(recovery_key_success_title) > 50):
            raise ValueError("Invalid value for `recovery_key_success_title`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_success_title is not None and len(recovery_key_success_title) < 0):
            raise ValueError("Invalid value for `recovery_key_success_title`, length must be greater than or equal to `0`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_success_title is not None and not re.search(r'^[  a-zA-Z0-9_#,;:\'?.\"!@{}+-]*$', recovery_key_success_title)):  # noqa: E501
            raise ValueError(r"Invalid value for `recovery_key_success_title`, must be a follow pattern or equal to `/^[  a-zA-Z0-9_#,;:'?.\"!@{}+-]*$/`")  # noqa: E501

        self._recovery_key_success_title = recovery_key_success_title

    @property
    def recovery_key_success_message(self):
        """Gets the recovery_key_success_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets success message for rotating recovery key.  # noqa: E501

        :return: The recovery_key_success_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._recovery_key_success_message

    @recovery_key_success_message.setter
    def recovery_key_success_message(self, recovery_key_success_message):
        """Sets the recovery_key_success_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets success message for rotating recovery key.  # noqa: E501

        :param recovery_key_success_message: The recovery_key_success_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                recovery_key_success_message is not None and len(recovery_key_success_message) > 150):
            raise ValueError("Invalid value for `recovery_key_success_message`, length must be less than or equal to `150`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_success_message is not None and len(recovery_key_success_message) < 0):
            raise ValueError("Invalid value for `recovery_key_success_message`, length must be greater than or equal to `0`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_success_message is not None and not re.search(r'^[  a-zA-Z0-9_#,;:\'?.\"!@{}+-]*$', recovery_key_success_message)):  # noqa: E501
            raise ValueError(r"Invalid value for `recovery_key_success_message`, must be a follow pattern or equal to `/^[  a-zA-Z0-9_#,;:'?.\"!@{}+-]*$/`")  # noqa: E501

        self._recovery_key_success_message = recovery_key_success_message

    @property
    def recovery_key_error_title(self):
        """Gets the recovery_key_error_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets error title for rotating recovery key.  # noqa: E501

        :return: The recovery_key_error_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._recovery_key_error_title

    @recovery_key_error_title.setter
    def recovery_key_error_title(self, recovery_key_error_title):
        """Sets the recovery_key_error_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets error title for rotating recovery key.  # noqa: E501

        :param recovery_key_error_title: The recovery_key_error_title of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                recovery_key_error_title is not None and len(recovery_key_error_title) > 50):
            raise ValueError("Invalid value for `recovery_key_error_title`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_error_title is not None and len(recovery_key_error_title) < 0):
            raise ValueError("Invalid value for `recovery_key_error_title`, length must be greater than or equal to `0`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_error_title is not None and not re.search(r'^[  a-zA-Z0-9_#,;:\'?.\"!@{}+-]*$', recovery_key_error_title)):  # noqa: E501
            raise ValueError(r"Invalid value for `recovery_key_error_title`, must be a follow pattern or equal to `/^[  a-zA-Z0-9_#,;:'?.\"!@{}+-]*$/`")  # noqa: E501

        self._recovery_key_error_title = recovery_key_error_title

    @property
    def recovery_key_error_message(self):
        """Gets the recovery_key_error_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets error message for rotating recovery key.  # noqa: E501

        :return: The recovery_key_error_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._recovery_key_error_message

    @recovery_key_error_message.setter
    def recovery_key_error_message(self, recovery_key_error_message):
        """Sets the recovery_key_error_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets error message for rotating recovery key.  # noqa: E501

        :param recovery_key_error_message: The recovery_key_error_message of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                recovery_key_error_message is not None and len(recovery_key_error_message) > 150):
            raise ValueError("Invalid value for `recovery_key_error_message`, length must be less than or equal to `150`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_error_message is not None and len(recovery_key_error_message) < 0):
            raise ValueError("Invalid value for `recovery_key_error_message`, length must be greater than or equal to `0`")  # noqa: E501
        if (self._configuration.client_side_validation and
                recovery_key_error_message is not None and not re.search(r'^[  a-zA-Z0-9_#,;:\'?.\"!@{}+-]*$', recovery_key_error_message)):  # noqa: E501
            raise ValueError(r"Invalid value for `recovery_key_error_message`, must be a follow pattern or equal to `/^[  a-zA-Z0-9_#,;:'?.\"!@{}+-]*$/`")  # noqa: E501

        self._recovery_key_error_message = recovery_key_error_message

    @property
    def recovery_key_max_failure_count(self):
        """Gets the recovery_key_max_failure_count of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501

        Gets or sets maximum number of times to rotate recovery key on failure.  # noqa: E501

        :return: The recovery_key_max_failure_count of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :rtype: int
        """
        return self._recovery_key_max_failure_count

    @recovery_key_max_failure_count.setter
    def recovery_key_max_failure_count(self, recovery_key_max_failure_count):
        """Sets the recovery_key_max_failure_count of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.

        Gets or sets maximum number of times to rotate recovery key on failure.  # noqa: E501

        :param recovery_key_max_failure_count: The recovery_key_max_failure_count of this AppleOsXDiskEncryptionAirWatchPayloadEntity_.  # noqa: E501
        :type: int
        """

        self._recovery_key_max_failure_count = recovery_key_max_failure_count

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
        if issubclass(AppleOsXDiskEncryptionAirWatchPayloadEntity_, dict):
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
        if not isinstance(other, AppleOsXDiskEncryptionAirWatchPayloadEntity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleOsXDiskEncryptionAirWatchPayloadEntity_):
            return True

        return self.to_dict() != other.to_dict()
