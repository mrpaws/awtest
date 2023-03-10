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


class AppleSetupAssistantPayloadEntity(object):
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
        'skip_android': 'bool',
        'skip_apperance': 'bool',
        'skip_apple_id': 'bool',
        'skip_biometric': 'bool',
        'skip_device_migration': 'bool',
        'skip_diagnostics': 'bool',
        'skip_display_tone': 'bool',
        'skip_home_button_sensitivity': 'bool',
        'skip_imessage_and_facetime': 'bool',
        'skip_location': 'bool',
        'skip_passcode': 'bool',
        'skip_payment': 'bool',
        'skip_privacy': 'bool',
        'skip_restore': 'bool',
        'skip_restore_completed': 'bool',
        'skip_screen_time': 'bool',
        'skip_sim_setup': 'bool',
        'skip_siri': 'bool',
        'skip_software_update': 'bool',
        'skip_terms_and_conditions': 'bool',
        'skip_update_completed': 'bool',
        'skip_watch_migration': 'bool',
        'skip_welcome': 'bool',
        'skip_zoom': 'bool'
    }

    attribute_map = {
        'skip_android': 'SkipAndroid',
        'skip_apperance': 'SkipApperance',
        'skip_apple_id': 'SkipAppleID',
        'skip_biometric': 'SkipBiometric',
        'skip_device_migration': 'SkipDeviceMigration',
        'skip_diagnostics': 'SkipDiagnostics',
        'skip_display_tone': 'SkipDisplayTone',
        'skip_home_button_sensitivity': 'SkipHomeButtonSensitivity',
        'skip_imessage_and_facetime': 'SkipImessageAndFacetime',
        'skip_location': 'SkipLocation',
        'skip_passcode': 'SkipPasscode',
        'skip_payment': 'SkipPayment',
        'skip_privacy': 'SkipPrivacy',
        'skip_restore': 'SkipRestore',
        'skip_restore_completed': 'SkipRestoreCompleted',
        'skip_screen_time': 'SkipScreenTime',
        'skip_sim_setup': 'SkipSimSetup',
        'skip_siri': 'SkipSiri',
        'skip_software_update': 'SkipSoftwareUpdate',
        'skip_terms_and_conditions': 'SkipTermsAndConditions',
        'skip_update_completed': 'SkipUpdateCompleted',
        'skip_watch_migration': 'SkipWatchMigration',
        'skip_welcome': 'SkipWelcome',
        'skip_zoom': 'SkipZoom'
    }

    def __init__(self, skip_android=None, skip_apperance=None, skip_apple_id=None, skip_biometric=None, skip_device_migration=None, skip_diagnostics=None, skip_display_tone=None, skip_home_button_sensitivity=None, skip_imessage_and_facetime=None, skip_location=None, skip_passcode=None, skip_payment=None, skip_privacy=None, skip_restore=None, skip_restore_completed=None, skip_screen_time=None, skip_sim_setup=None, skip_siri=None, skip_software_update=None, skip_terms_and_conditions=None, skip_update_completed=None, skip_watch_migration=None, skip_welcome=None, skip_zoom=None, _configuration=None):  # noqa: E501
        """AppleSetupAssistantPayloadEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._skip_android = None
        self._skip_apperance = None
        self._skip_apple_id = None
        self._skip_biometric = None
        self._skip_device_migration = None
        self._skip_diagnostics = None
        self._skip_display_tone = None
        self._skip_home_button_sensitivity = None
        self._skip_imessage_and_facetime = None
        self._skip_location = None
        self._skip_passcode = None
        self._skip_payment = None
        self._skip_privacy = None
        self._skip_restore = None
        self._skip_restore_completed = None
        self._skip_screen_time = None
        self._skip_sim_setup = None
        self._skip_siri = None
        self._skip_software_update = None
        self._skip_terms_and_conditions = None
        self._skip_update_completed = None
        self._skip_watch_migration = None
        self._skip_welcome = None
        self._skip_zoom = None
        self.discriminator = None

        if skip_android is not None:
            self.skip_android = skip_android
        if skip_apperance is not None:
            self.skip_apperance = skip_apperance
        if skip_apple_id is not None:
            self.skip_apple_id = skip_apple_id
        if skip_biometric is not None:
            self.skip_biometric = skip_biometric
        if skip_device_migration is not None:
            self.skip_device_migration = skip_device_migration
        if skip_diagnostics is not None:
            self.skip_diagnostics = skip_diagnostics
        if skip_display_tone is not None:
            self.skip_display_tone = skip_display_tone
        if skip_home_button_sensitivity is not None:
            self.skip_home_button_sensitivity = skip_home_button_sensitivity
        if skip_imessage_and_facetime is not None:
            self.skip_imessage_and_facetime = skip_imessage_and_facetime
        if skip_location is not None:
            self.skip_location = skip_location
        if skip_passcode is not None:
            self.skip_passcode = skip_passcode
        if skip_payment is not None:
            self.skip_payment = skip_payment
        if skip_privacy is not None:
            self.skip_privacy = skip_privacy
        if skip_restore is not None:
            self.skip_restore = skip_restore
        if skip_restore_completed is not None:
            self.skip_restore_completed = skip_restore_completed
        if skip_screen_time is not None:
            self.skip_screen_time = skip_screen_time
        if skip_sim_setup is not None:
            self.skip_sim_setup = skip_sim_setup
        if skip_siri is not None:
            self.skip_siri = skip_siri
        if skip_software_update is not None:
            self.skip_software_update = skip_software_update
        if skip_terms_and_conditions is not None:
            self.skip_terms_and_conditions = skip_terms_and_conditions
        if skip_update_completed is not None:
            self.skip_update_completed = skip_update_completed
        if skip_watch_migration is not None:
            self.skip_watch_migration = skip_watch_migration
        if skip_welcome is not None:
            self.skip_welcome = skip_welcome
        if skip_zoom is not None:
            self.skip_zoom = skip_zoom

    @property
    def skip_android(self):
        """Gets the skip_android of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether Android screen in Setup Assistant has to be skipped.  # noqa: E501

        :return: The skip_android of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_android

    @skip_android.setter
    def skip_android(self, skip_android):
        """Sets the skip_android of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether Android screen in Setup Assistant has to be skipped.  # noqa: E501

        :param skip_android: The skip_android of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_android = skip_android

    @property
    def skip_apperance(self):
        """Gets the skip_apperance of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Appearance screen has to be skipped.  # noqa: E501

        :return: The skip_apperance of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_apperance

    @skip_apperance.setter
    def skip_apperance(self, skip_apperance):
        """Sets the skip_apperance of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Appearance screen has to be skipped.  # noqa: E501

        :param skip_apperance: The skip_apperance of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_apperance = skip_apperance

    @property
    def skip_apple_id(self):
        """Gets the skip_apple_id of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Apple ID screen has to be skipped.  # noqa: E501

        :return: The skip_apple_id of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_apple_id

    @skip_apple_id.setter
    def skip_apple_id(self, skip_apple_id):
        """Sets the skip_apple_id of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Apple ID screen has to be skipped.  # noqa: E501

        :param skip_apple_id: The skip_apple_id of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_apple_id = skip_apple_id

    @property
    def skip_biometric(self):
        """Gets the skip_biometric of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Biometric screen has to be skipped.  # noqa: E501

        :return: The skip_biometric of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_biometric

    @skip_biometric.setter
    def skip_biometric(self, skip_biometric):
        """Sets the skip_biometric of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Biometric screen has to be skipped.  # noqa: E501

        :param skip_biometric: The skip_biometric of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_biometric = skip_biometric

    @property
    def skip_device_migration(self):
        """Gets the skip_device_migration of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Device to device migration screen has to be skipped.  # noqa: E501

        :return: The skip_device_migration of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_device_migration

    @skip_device_migration.setter
    def skip_device_migration(self, skip_device_migration):
        """Sets the skip_device_migration of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Device to device migration screen has to be skipped.  # noqa: E501

        :param skip_device_migration: The skip_device_migration of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_device_migration = skip_device_migration

    @property
    def skip_diagnostics(self):
        """Gets the skip_diagnostics of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the diagnostics screen has to be skipped.  # noqa: E501

        :return: The skip_diagnostics of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_diagnostics

    @skip_diagnostics.setter
    def skip_diagnostics(self, skip_diagnostics):
        """Sets the skip_diagnostics of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the diagnostics screen has to be skipped.  # noqa: E501

        :param skip_diagnostics: The skip_diagnostics of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_diagnostics = skip_diagnostics

    @property
    def skip_display_tone(self):
        """Gets the skip_display_tone of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Display tone screen has to be skipped.  # noqa: E501

        :return: The skip_display_tone of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_display_tone

    @skip_display_tone.setter
    def skip_display_tone(self, skip_display_tone):
        """Sets the skip_display_tone of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Display tone screen has to be skipped.  # noqa: E501

        :param skip_display_tone: The skip_display_tone of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_display_tone = skip_display_tone

    @property
    def skip_home_button_sensitivity(self):
        """Gets the skip_home_button_sensitivity of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Home button sensitivty screen has to be skipped.  # noqa: E501

        :return: The skip_home_button_sensitivity of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_home_button_sensitivity

    @skip_home_button_sensitivity.setter
    def skip_home_button_sensitivity(self, skip_home_button_sensitivity):
        """Sets the skip_home_button_sensitivity of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Home button sensitivty screen has to be skipped.  # noqa: E501

        :param skip_home_button_sensitivity: The skip_home_button_sensitivity of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_home_button_sensitivity = skip_home_button_sensitivity

    @property
    def skip_imessage_and_facetime(self):
        """Gets the skip_imessage_and_facetime of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the iMessage and Facetime screen has to be skipped.  # noqa: E501

        :return: The skip_imessage_and_facetime of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_imessage_and_facetime

    @skip_imessage_and_facetime.setter
    def skip_imessage_and_facetime(self, skip_imessage_and_facetime):
        """Sets the skip_imessage_and_facetime of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the iMessage and Facetime screen has to be skipped.  # noqa: E501

        :param skip_imessage_and_facetime: The skip_imessage_and_facetime of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_imessage_and_facetime = skip_imessage_and_facetime

    @property
    def skip_location(self):
        """Gets the skip_location of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Location screen has to be skipped.  # noqa: E501

        :return: The skip_location of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_location

    @skip_location.setter
    def skip_location(self, skip_location):
        """Sets the skip_location of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Location screen has to be skipped.  # noqa: E501

        :param skip_location: The skip_location of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_location = skip_location

    @property
    def skip_passcode(self):
        """Gets the skip_passcode of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the passcode screen has to be skipped.  # noqa: E501

        :return: The skip_passcode of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_passcode

    @skip_passcode.setter
    def skip_passcode(self, skip_passcode):
        """Sets the skip_passcode of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the passcode screen has to be skipped.  # noqa: E501

        :param skip_passcode: The skip_passcode of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_passcode = skip_passcode

    @property
    def skip_payment(self):
        """Gets the skip_payment of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the payment screen has to be skipped.  # noqa: E501

        :return: The skip_payment of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_payment

    @skip_payment.setter
    def skip_payment(self, skip_payment):
        """Sets the skip_payment of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the payment screen has to be skipped.  # noqa: E501

        :param skip_payment: The skip_payment of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_payment = skip_payment

    @property
    def skip_privacy(self):
        """Gets the skip_privacy of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Privacy screen has to be skipped.  # noqa: E501

        :return: The skip_privacy of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_privacy

    @skip_privacy.setter
    def skip_privacy(self, skip_privacy):
        """Sets the skip_privacy of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Privacy screen has to be skipped.  # noqa: E501

        :param skip_privacy: The skip_privacy of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_privacy = skip_privacy

    @property
    def skip_restore(self):
        """Gets the skip_restore of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Restore screen has to be skipped.  # noqa: E501

        :return: The skip_restore of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_restore

    @skip_restore.setter
    def skip_restore(self, skip_restore):
        """Sets the skip_restore of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Restore screen has to be skipped.  # noqa: E501

        :param skip_restore: The skip_restore of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_restore = skip_restore

    @property
    def skip_restore_completed(self):
        """Gets the skip_restore_completed of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Restore Completed screen has to be skipped.  # noqa: E501

        :return: The skip_restore_completed of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_restore_completed

    @skip_restore_completed.setter
    def skip_restore_completed(self, skip_restore_completed):
        """Sets the skip_restore_completed of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Restore Completed screen has to be skipped.  # noqa: E501

        :param skip_restore_completed: The skip_restore_completed of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_restore_completed = skip_restore_completed

    @property
    def skip_screen_time(self):
        """Gets the skip_screen_time of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the ScreenTime screen has to be skipped.  # noqa: E501

        :return: The skip_screen_time of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_screen_time

    @skip_screen_time.setter
    def skip_screen_time(self, skip_screen_time):
        """Sets the skip_screen_time of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the ScreenTime screen has to be skipped.  # noqa: E501

        :param skip_screen_time: The skip_screen_time of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_screen_time = skip_screen_time

    @property
    def skip_sim_setup(self):
        """Gets the skip_sim_setup of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the SIM setup screen has to be skipped.  # noqa: E501

        :return: The skip_sim_setup of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_sim_setup

    @skip_sim_setup.setter
    def skip_sim_setup(self, skip_sim_setup):
        """Sets the skip_sim_setup of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the SIM setup screen has to be skipped.  # noqa: E501

        :param skip_sim_setup: The skip_sim_setup of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_sim_setup = skip_sim_setup

    @property
    def skip_siri(self):
        """Gets the skip_siri of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Siri setup screen has to be skipped.  # noqa: E501

        :return: The skip_siri of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_siri

    @skip_siri.setter
    def skip_siri(self, skip_siri):
        """Sets the skip_siri of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Siri setup screen has to be skipped.  # noqa: E501

        :param skip_siri: The skip_siri of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_siri = skip_siri

    @property
    def skip_software_update(self):
        """Gets the skip_software_update of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Software Update screen has to be skipped.  # noqa: E501

        :return: The skip_software_update of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_software_update

    @skip_software_update.setter
    def skip_software_update(self, skip_software_update):
        """Sets the skip_software_update of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Software Update screen has to be skipped.  # noqa: E501

        :param skip_software_update: The skip_software_update of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_software_update = skip_software_update

    @property
    def skip_terms_and_conditions(self):
        """Gets the skip_terms_and_conditions of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Terms of service screen has to be skipped.  # noqa: E501

        :return: The skip_terms_and_conditions of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_terms_and_conditions

    @skip_terms_and_conditions.setter
    def skip_terms_and_conditions(self, skip_terms_and_conditions):
        """Sets the skip_terms_and_conditions of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Terms of service screen has to be skipped.  # noqa: E501

        :param skip_terms_and_conditions: The skip_terms_and_conditions of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_terms_and_conditions = skip_terms_and_conditions

    @property
    def skip_update_completed(self):
        """Gets the skip_update_completed of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Update completed screen has to be skipped.  # noqa: E501

        :return: The skip_update_completed of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_update_completed

    @skip_update_completed.setter
    def skip_update_completed(self, skip_update_completed):
        """Sets the skip_update_completed of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Update completed screen has to be skipped.  # noqa: E501

        :param skip_update_completed: The skip_update_completed of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_update_completed = skip_update_completed

    @property
    def skip_watch_migration(self):
        """Gets the skip_watch_migration of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Watch migration screen has to be skipped.  # noqa: E501

        :return: The skip_watch_migration of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_watch_migration

    @skip_watch_migration.setter
    def skip_watch_migration(self, skip_watch_migration):
        """Sets the skip_watch_migration of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Watch migration screen has to be skipped.  # noqa: E501

        :param skip_watch_migration: The skip_watch_migration of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_watch_migration = skip_watch_migration

    @property
    def skip_welcome(self):
        """Gets the skip_welcome of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Welcome screen has to be skipped.  # noqa: E501

        :return: The skip_welcome of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_welcome

    @skip_welcome.setter
    def skip_welcome(self, skip_welcome):
        """Sets the skip_welcome of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Welcome screen has to be skipped.  # noqa: E501

        :param skip_welcome: The skip_welcome of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_welcome = skip_welcome

    @property
    def skip_zoom(self):
        """Gets the skip_zoom of this AppleSetupAssistantPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether the Zoom setup screen has to be skipped.  # noqa: E501

        :return: The skip_zoom of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._skip_zoom

    @skip_zoom.setter
    def skip_zoom(self, skip_zoom):
        """Sets the skip_zoom of this AppleSetupAssistantPayloadEntity.

        Gets or sets a value indicating whether the Zoom setup screen has to be skipped.  # noqa: E501

        :param skip_zoom: The skip_zoom of this AppleSetupAssistantPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._skip_zoom = skip_zoom

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
        if issubclass(AppleSetupAssistantPayloadEntity, dict):
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
        if not isinstance(other, AppleSetupAssistantPayloadEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleSetupAssistantPayloadEntity):
            return True

        return self.to_dict() != other.to_dict()
