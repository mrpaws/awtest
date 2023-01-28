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


class AndroidPasscodePayloadV2Entity_(object):
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
        'minimum_passcode_length': 'int',
        'passcode_content': 'int',
        'maximum_number_of_failed_attempts': 'str',
        'grace_period_for_passcode_change': 'int',
        'maximum_repeat_characters': 'str',
        'maximum_length_of_numeric_sequences': 'str',
        'minimum_number_of_numerical_digits': 'str',
        'minimum_number_of_letters': 'int',
        'minimum_number_of_lower_case_letters': 'int',
        'minimum_number_of_upper_case_letters': 'int',
        'minimum_number_of_non_letters': 'int',
        'minimum_number_of_symbols': 'int',
        'maximum_passcode_age': 'int',
        'device_lock_timeout_in_minutes': 'int',
        'passcode_history': 'str',
        'enable_passcode_visibility': 'bool',
        'allow_fingerprint_unlock': 'bool',
        'require_storage_encryption': 'bool',
        'require_sd_card_encryption': 'bool',
        'require_storage_encryption_always': 'bool',
        'require_storage_encryption_native_email': 'bool',
        'require_passcode': 'bool',
        'predefine_passcode': 'bool',
        'passcode': 'str'
    }

    attribute_map = {
        'minimum_passcode_length': 'MinimumPasscodeLength',
        'passcode_content': 'PasscodeContent',
        'maximum_number_of_failed_attempts': 'MaximumNumberOfFailedAttempts',
        'grace_period_for_passcode_change': 'GracePeriodForPasscodeChange',
        'maximum_repeat_characters': 'MaximumRepeatCharacters',
        'maximum_length_of_numeric_sequences': 'MaximumLengthOfNumericSequences',
        'minimum_number_of_numerical_digits': 'MinimumNumberOfNumericalDigits',
        'minimum_number_of_letters': 'MinimumNumberOfLetters',
        'minimum_number_of_lower_case_letters': 'MinimumNumberOfLowerCaseLetters',
        'minimum_number_of_upper_case_letters': 'MinimumNumberOfUpperCaseLetters',
        'minimum_number_of_non_letters': 'MinimumNumberOfNonLetters',
        'minimum_number_of_symbols': 'MinimumNumberOfSymbols',
        'maximum_passcode_age': 'MaximumPasscodeAge',
        'device_lock_timeout_in_minutes': 'DeviceLockTimeoutInMinutes',
        'passcode_history': 'PasscodeHistory',
        'enable_passcode_visibility': 'EnablePasscodeVisibility',
        'allow_fingerprint_unlock': 'AllowFingerprintUnlock',
        'require_storage_encryption': 'RequireStorageEncryption',
        'require_sd_card_encryption': 'RequireSDCardEncryption',
        'require_storage_encryption_always': 'requireStorageEncryptionAlways',
        'require_storage_encryption_native_email': 'requireStorageEncryptionNativeEmail',
        'require_passcode': 'RequirePasscode',
        'predefine_passcode': 'PredefinePasscode',
        'passcode': 'Passcode'
    }

    def __init__(self, minimum_passcode_length=None, passcode_content=None, maximum_number_of_failed_attempts=None, grace_period_for_passcode_change=None, maximum_repeat_characters=None, maximum_length_of_numeric_sequences=None, minimum_number_of_numerical_digits=None, minimum_number_of_letters=None, minimum_number_of_lower_case_letters=None, minimum_number_of_upper_case_letters=None, minimum_number_of_non_letters=None, minimum_number_of_symbols=None, maximum_passcode_age=None, device_lock_timeout_in_minutes=None, passcode_history=None, enable_passcode_visibility=None, allow_fingerprint_unlock=None, require_storage_encryption=None, require_sd_card_encryption=None, require_storage_encryption_always=None, require_storage_encryption_native_email=None, require_passcode=None, predefine_passcode=None, passcode=None, _configuration=None):  # noqa: E501
        """AndroidPasscodePayloadV2Entity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._minimum_passcode_length = None
        self._passcode_content = None
        self._maximum_number_of_failed_attempts = None
        self._grace_period_for_passcode_change = None
        self._maximum_repeat_characters = None
        self._maximum_length_of_numeric_sequences = None
        self._minimum_number_of_numerical_digits = None
        self._minimum_number_of_letters = None
        self._minimum_number_of_lower_case_letters = None
        self._minimum_number_of_upper_case_letters = None
        self._minimum_number_of_non_letters = None
        self._minimum_number_of_symbols = None
        self._maximum_passcode_age = None
        self._device_lock_timeout_in_minutes = None
        self._passcode_history = None
        self._enable_passcode_visibility = None
        self._allow_fingerprint_unlock = None
        self._require_storage_encryption = None
        self._require_sd_card_encryption = None
        self._require_storage_encryption_always = None
        self._require_storage_encryption_native_email = None
        self._require_passcode = None
        self._predefine_passcode = None
        self._passcode = None
        self.discriminator = None

        if minimum_passcode_length is not None:
            self.minimum_passcode_length = minimum_passcode_length
        if passcode_content is not None:
            self.passcode_content = passcode_content
        if maximum_number_of_failed_attempts is not None:
            self.maximum_number_of_failed_attempts = maximum_number_of_failed_attempts
        if grace_period_for_passcode_change is not None:
            self.grace_period_for_passcode_change = grace_period_for_passcode_change
        if maximum_repeat_characters is not None:
            self.maximum_repeat_characters = maximum_repeat_characters
        if maximum_length_of_numeric_sequences is not None:
            self.maximum_length_of_numeric_sequences = maximum_length_of_numeric_sequences
        if minimum_number_of_numerical_digits is not None:
            self.minimum_number_of_numerical_digits = minimum_number_of_numerical_digits
        if minimum_number_of_letters is not None:
            self.minimum_number_of_letters = minimum_number_of_letters
        if minimum_number_of_lower_case_letters is not None:
            self.minimum_number_of_lower_case_letters = minimum_number_of_lower_case_letters
        if minimum_number_of_upper_case_letters is not None:
            self.minimum_number_of_upper_case_letters = minimum_number_of_upper_case_letters
        if minimum_number_of_non_letters is not None:
            self.minimum_number_of_non_letters = minimum_number_of_non_letters
        if minimum_number_of_symbols is not None:
            self.minimum_number_of_symbols = minimum_number_of_symbols
        if maximum_passcode_age is not None:
            self.maximum_passcode_age = maximum_passcode_age
        if device_lock_timeout_in_minutes is not None:
            self.device_lock_timeout_in_minutes = device_lock_timeout_in_minutes
        if passcode_history is not None:
            self.passcode_history = passcode_history
        if enable_passcode_visibility is not None:
            self.enable_passcode_visibility = enable_passcode_visibility
        if allow_fingerprint_unlock is not None:
            self.allow_fingerprint_unlock = allow_fingerprint_unlock
        if require_storage_encryption is not None:
            self.require_storage_encryption = require_storage_encryption
        if require_sd_card_encryption is not None:
            self.require_sd_card_encryption = require_sd_card_encryption
        if require_storage_encryption_always is not None:
            self.require_storage_encryption_always = require_storage_encryption_always
        if require_storage_encryption_native_email is not None:
            self.require_storage_encryption_native_email = require_storage_encryption_native_email
        if require_passcode is not None:
            self.require_passcode = require_passcode
        if predefine_passcode is not None:
            self.predefine_passcode = predefine_passcode
        if passcode is not None:
            self.passcode = passcode

    @property
    def minimum_passcode_length(self):
        """Gets the minimum_passcode_length of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the minimum length.  # noqa: E501

        :return: The minimum_passcode_length of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._minimum_passcode_length

    @minimum_passcode_length.setter
    def minimum_passcode_length(self, minimum_passcode_length):
        """Sets the minimum_passcode_length of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the minimum length.  # noqa: E501

        :param minimum_passcode_length: The minimum_passcode_length of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._minimum_passcode_length = minimum_passcode_length

    @property
    def passcode_content(self):
        """Gets the passcode_content of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the quality.  # noqa: E501

        :return: The passcode_content of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._passcode_content

    @passcode_content.setter
    def passcode_content(self, passcode_content):
        """Sets the passcode_content of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the quality.  # noqa: E501

        :param passcode_content: The passcode_content of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._passcode_content = passcode_content

    @property
    def maximum_number_of_failed_attempts(self):
        """Gets the maximum_number_of_failed_attempts of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the maximum failed attempts.  # noqa: E501

        :return: The maximum_number_of_failed_attempts of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._maximum_number_of_failed_attempts

    @maximum_number_of_failed_attempts.setter
    def maximum_number_of_failed_attempts(self, maximum_number_of_failed_attempts):
        """Sets the maximum_number_of_failed_attempts of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the maximum failed attempts.  # noqa: E501

        :param maximum_number_of_failed_attempts: The maximum_number_of_failed_attempts of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._maximum_number_of_failed_attempts = maximum_number_of_failed_attempts

    @property
    def grace_period_for_passcode_change(self):
        """Gets the grace_period_for_passcode_change of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the grace period.  # noqa: E501

        :return: The grace_period_for_passcode_change of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._grace_period_for_passcode_change

    @grace_period_for_passcode_change.setter
    def grace_period_for_passcode_change(self, grace_period_for_passcode_change):
        """Sets the grace_period_for_passcode_change of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the grace period.  # noqa: E501

        :param grace_period_for_passcode_change: The grace_period_for_passcode_change of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._grace_period_for_passcode_change = grace_period_for_passcode_change

    @property
    def maximum_repeat_characters(self):
        """Gets the maximum_repeat_characters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the maximum repeating characters.  # noqa: E501

        :return: The maximum_repeat_characters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._maximum_repeat_characters

    @maximum_repeat_characters.setter
    def maximum_repeat_characters(self, maximum_repeat_characters):
        """Sets the maximum_repeat_characters of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the maximum repeating characters.  # noqa: E501

        :param maximum_repeat_characters: The maximum_repeat_characters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._maximum_repeat_characters = maximum_repeat_characters

    @property
    def maximum_length_of_numeric_sequences(self):
        """Gets the maximum_length_of_numeric_sequences of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the maximum length of numeric sequences.  # noqa: E501

        :return: The maximum_length_of_numeric_sequences of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._maximum_length_of_numeric_sequences

    @maximum_length_of_numeric_sequences.setter
    def maximum_length_of_numeric_sequences(self, maximum_length_of_numeric_sequences):
        """Sets the maximum_length_of_numeric_sequences of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the maximum length of numeric sequences.  # noqa: E501

        :param maximum_length_of_numeric_sequences: The maximum_length_of_numeric_sequences of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._maximum_length_of_numeric_sequences = maximum_length_of_numeric_sequences

    @property
    def minimum_number_of_numerical_digits(self):
        """Gets the minimum_number_of_numerical_digits of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the minimum numeric.  # noqa: E501

        :return: The minimum_number_of_numerical_digits of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._minimum_number_of_numerical_digits

    @minimum_number_of_numerical_digits.setter
    def minimum_number_of_numerical_digits(self, minimum_number_of_numerical_digits):
        """Sets the minimum_number_of_numerical_digits of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the minimum numeric.  # noqa: E501

        :param minimum_number_of_numerical_digits: The minimum_number_of_numerical_digits of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._minimum_number_of_numerical_digits = minimum_number_of_numerical_digits

    @property
    def minimum_number_of_letters(self):
        """Gets the minimum_number_of_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the minimum letters.  # noqa: E501

        :return: The minimum_number_of_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._minimum_number_of_letters

    @minimum_number_of_letters.setter
    def minimum_number_of_letters(self, minimum_number_of_letters):
        """Sets the minimum_number_of_letters of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the minimum letters.  # noqa: E501

        :param minimum_number_of_letters: The minimum_number_of_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._minimum_number_of_letters = minimum_number_of_letters

    @property
    def minimum_number_of_lower_case_letters(self):
        """Gets the minimum_number_of_lower_case_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the minimum lower case.  # noqa: E501

        :return: The minimum_number_of_lower_case_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._minimum_number_of_lower_case_letters

    @minimum_number_of_lower_case_letters.setter
    def minimum_number_of_lower_case_letters(self, minimum_number_of_lower_case_letters):
        """Sets the minimum_number_of_lower_case_letters of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the minimum lower case.  # noqa: E501

        :param minimum_number_of_lower_case_letters: The minimum_number_of_lower_case_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._minimum_number_of_lower_case_letters = minimum_number_of_lower_case_letters

    @property
    def minimum_number_of_upper_case_letters(self):
        """Gets the minimum_number_of_upper_case_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the minimum upper case.  # noqa: E501

        :return: The minimum_number_of_upper_case_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._minimum_number_of_upper_case_letters

    @minimum_number_of_upper_case_letters.setter
    def minimum_number_of_upper_case_letters(self, minimum_number_of_upper_case_letters):
        """Sets the minimum_number_of_upper_case_letters of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the minimum upper case.  # noqa: E501

        :param minimum_number_of_upper_case_letters: The minimum_number_of_upper_case_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._minimum_number_of_upper_case_letters = minimum_number_of_upper_case_letters

    @property
    def minimum_number_of_non_letters(self):
        """Gets the minimum_number_of_non_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the minimum non letter.  # noqa: E501

        :return: The minimum_number_of_non_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._minimum_number_of_non_letters

    @minimum_number_of_non_letters.setter
    def minimum_number_of_non_letters(self, minimum_number_of_non_letters):
        """Sets the minimum_number_of_non_letters of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the minimum non letter.  # noqa: E501

        :param minimum_number_of_non_letters: The minimum_number_of_non_letters of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._minimum_number_of_non_letters = minimum_number_of_non_letters

    @property
    def minimum_number_of_symbols(self):
        """Gets the minimum_number_of_symbols of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the minimum symbols.  # noqa: E501

        :return: The minimum_number_of_symbols of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._minimum_number_of_symbols

    @minimum_number_of_symbols.setter
    def minimum_number_of_symbols(self, minimum_number_of_symbols):
        """Sets the minimum_number_of_symbols of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the minimum symbols.  # noqa: E501

        :param minimum_number_of_symbols: The minimum_number_of_symbols of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._minimum_number_of_symbols = minimum_number_of_symbols

    @property
    def maximum_passcode_age(self):
        """Gets the maximum_passcode_age of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the expiration timeout days.  # noqa: E501

        :return: The maximum_passcode_age of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._maximum_passcode_age

    @maximum_passcode_age.setter
    def maximum_passcode_age(self, maximum_passcode_age):
        """Sets the maximum_passcode_age of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the expiration timeout days.  # noqa: E501

        :param maximum_passcode_age: The maximum_passcode_age of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._maximum_passcode_age = maximum_passcode_age

    @property
    def device_lock_timeout_in_minutes(self):
        """Gets the device_lock_timeout_in_minutes of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the device lock timeout minutes.  # noqa: E501

        :return: The device_lock_timeout_in_minutes of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._device_lock_timeout_in_minutes

    @device_lock_timeout_in_minutes.setter
    def device_lock_timeout_in_minutes(self, device_lock_timeout_in_minutes):
        """Sets the device_lock_timeout_in_minutes of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the device lock timeout minutes.  # noqa: E501

        :param device_lock_timeout_in_minutes: The device_lock_timeout_in_minutes of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._device_lock_timeout_in_minutes = device_lock_timeout_in_minutes

    @property
    def passcode_history(self):
        """Gets the passcode_history of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the length of the history.  # noqa: E501

        :return: The passcode_history of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._passcode_history

    @passcode_history.setter
    def passcode_history(self, passcode_history):
        """Sets the passcode_history of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the length of the history.  # noqa: E501

        :param passcode_history: The passcode_history of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._passcode_history = passcode_history

    @property
    def enable_passcode_visibility(self):
        """Gets the enable_passcode_visibility of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether [passcode visible].  # noqa: E501

        :return: The enable_passcode_visibility of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._enable_passcode_visibility

    @enable_passcode_visibility.setter
    def enable_passcode_visibility(self, enable_passcode_visibility):
        """Sets the enable_passcode_visibility of this AndroidPasscodePayloadV2Entity_.

        Gets or sets a value indicating whether [passcode visible].  # noqa: E501

        :param enable_passcode_visibility: The enable_passcode_visibility of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._enable_passcode_visibility = enable_passcode_visibility

    @property
    def allow_fingerprint_unlock(self):
        """Gets the allow_fingerprint_unlock of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether [enable fingerprint authentication].  # noqa: E501

        :return: The allow_fingerprint_unlock of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_fingerprint_unlock

    @allow_fingerprint_unlock.setter
    def allow_fingerprint_unlock(self, allow_fingerprint_unlock):
        """Sets the allow_fingerprint_unlock of this AndroidPasscodePayloadV2Entity_.

        Gets or sets a value indicating whether [enable fingerprint authentication].  # noqa: E501

        :param allow_fingerprint_unlock: The allow_fingerprint_unlock of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._allow_fingerprint_unlock = allow_fingerprint_unlock

    @property
    def require_storage_encryption(self):
        """Gets the require_storage_encryption of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether [require storage encryption].  # noqa: E501

        :return: The require_storage_encryption of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._require_storage_encryption

    @require_storage_encryption.setter
    def require_storage_encryption(self, require_storage_encryption):
        """Sets the require_storage_encryption of this AndroidPasscodePayloadV2Entity_.

        Gets or sets a value indicating whether [require storage encryption].  # noqa: E501

        :param require_storage_encryption: The require_storage_encryption of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._require_storage_encryption = require_storage_encryption

    @property
    def require_sd_card_encryption(self):
        """Gets the require_sd_card_encryption of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether [require sd card encryption].  # noqa: E501

        :return: The require_sd_card_encryption of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._require_sd_card_encryption

    @require_sd_card_encryption.setter
    def require_sd_card_encryption(self, require_sd_card_encryption):
        """Sets the require_sd_card_encryption of this AndroidPasscodePayloadV2Entity_.

        Gets or sets a value indicating whether [require sd card encryption].  # noqa: E501

        :param require_sd_card_encryption: The require_sd_card_encryption of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._require_sd_card_encryption = require_sd_card_encryption

    @property
    def require_storage_encryption_always(self):
        """Gets the require_storage_encryption_always of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether [require storage encryption always].  # noqa: E501

        :return: The require_storage_encryption_always of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._require_storage_encryption_always

    @require_storage_encryption_always.setter
    def require_storage_encryption_always(self, require_storage_encryption_always):
        """Sets the require_storage_encryption_always of this AndroidPasscodePayloadV2Entity_.

        Gets or sets a value indicating whether [require storage encryption always].  # noqa: E501

        :param require_storage_encryption_always: The require_storage_encryption_always of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._require_storage_encryption_always = require_storage_encryption_always

    @property
    def require_storage_encryption_native_email(self):
        """Gets the require_storage_encryption_native_email of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether [require storage encryption native email].  # noqa: E501

        :return: The require_storage_encryption_native_email of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._require_storage_encryption_native_email

    @require_storage_encryption_native_email.setter
    def require_storage_encryption_native_email(self, require_storage_encryption_native_email):
        """Sets the require_storage_encryption_native_email of this AndroidPasscodePayloadV2Entity_.

        Gets or sets a value indicating whether [require storage encryption native email].  # noqa: E501

        :param require_storage_encryption_native_email: The require_storage_encryption_native_email of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._require_storage_encryption_native_email = require_storage_encryption_native_email

    @property
    def require_passcode(self):
        """Gets the require_passcode of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether [require sd card encryption passcode].  # noqa: E501

        :return: The require_passcode of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._require_passcode

    @require_passcode.setter
    def require_passcode(self, require_passcode):
        """Sets the require_passcode of this AndroidPasscodePayloadV2Entity_.

        Gets or sets a value indicating whether [require sd card encryption passcode].  # noqa: E501

        :param require_passcode: The require_passcode of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._require_passcode = require_passcode

    @property
    def predefine_passcode(self):
        """Gets the predefine_passcode of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether [predefine passcode].  # noqa: E501

        :return: The predefine_passcode of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._predefine_passcode

    @predefine_passcode.setter
    def predefine_passcode(self, predefine_passcode):
        """Sets the predefine_passcode of this AndroidPasscodePayloadV2Entity_.

        Gets or sets a value indicating whether [predefine passcode].  # noqa: E501

        :param predefine_passcode: The predefine_passcode of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._predefine_passcode = predefine_passcode

    @property
    def passcode(self):
        """Gets the passcode of this AndroidPasscodePayloadV2Entity_.  # noqa: E501

        Gets or sets the passcode.  # noqa: E501

        :return: The passcode of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._passcode

    @passcode.setter
    def passcode(self, passcode):
        """Sets the passcode of this AndroidPasscodePayloadV2Entity_.

        Gets or sets the passcode.  # noqa: E501

        :param passcode: The passcode of this AndroidPasscodePayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._passcode = passcode

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
        if issubclass(AndroidPasscodePayloadV2Entity_, dict):
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
        if not isinstance(other, AndroidPasscodePayloadV2Entity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidPasscodePayloadV2Entity_):
            return True

        return self.to_dict() != other.to_dict()