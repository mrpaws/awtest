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


class AppleOsXRestrictionICloudPayloadEntity_(object):
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
        'allow_icloud_documents_and_data': 'bool',
        'allow_use_icloud_password_for_local_accounts': 'bool',
        'allow_icloud_btmm': 'bool',
        'allow_i_cloud_fmm': 'bool',
        'allow_icloud_bookmarks': 'bool',
        'allow_icloud_mail': 'bool',
        'allow_icloud_calendar': 'bool',
        'allow_icloud_reminders': 'bool',
        'allow_icloud_address_book': 'bool',
        'allow_icloud_notes': 'bool',
        'allow_icloud_keychain_sync': 'bool',
        'allow_air_print': 'bool',
        'force_air_print_trusted_tls_requirement': 'bool',
        'allow_air_printi_beacon_discovery': 'bool',
        'allow_cloud_desktop_and_documents': 'bool',
        'allow_password_auto_fill': 'bool',
        'allow_password_sharing': 'bool',
        'allow_deprecated_web_kit_tls': 'bool',
        'allow_password_proximity_requests': 'bool'
    }

    attribute_map = {
        'allow_icloud_documents_and_data': 'AllowIcloudDocumentsAndData',
        'allow_use_icloud_password_for_local_accounts': 'AllowUseIcloudPasswordForLocalAccounts',
        'allow_icloud_btmm': 'AllowIcloudBTMM',
        'allow_i_cloud_fmm': 'AllowICloudFMM',
        'allow_icloud_bookmarks': 'AllowIcloudBookmarks',
        'allow_icloud_mail': 'AllowIcloudMail',
        'allow_icloud_calendar': 'AllowIcloudCalendar',
        'allow_icloud_reminders': 'AllowIcloudReminders',
        'allow_icloud_address_book': 'AllowIcloudAddressBook',
        'allow_icloud_notes': 'AllowIcloudNotes',
        'allow_icloud_keychain_sync': 'AllowIcloudKeychainSync',
        'allow_air_print': 'AllowAirPrint',
        'force_air_print_trusted_tls_requirement': 'ForceAirPrintTrustedTLSRequirement',
        'allow_air_printi_beacon_discovery': 'AllowAirPrintiBeaconDiscovery',
        'allow_cloud_desktop_and_documents': 'AllowCloudDesktopAndDocuments',
        'allow_password_auto_fill': 'AllowPasswordAutoFill',
        'allow_password_sharing': 'AllowPasswordSharing',
        'allow_deprecated_web_kit_tls': 'AllowDeprecatedWebKitTls',
        'allow_password_proximity_requests': 'AllowPasswordProximityRequests'
    }

    def __init__(self, allow_icloud_documents_and_data=None, allow_use_icloud_password_for_local_accounts=None, allow_icloud_btmm=None, allow_i_cloud_fmm=None, allow_icloud_bookmarks=None, allow_icloud_mail=None, allow_icloud_calendar=None, allow_icloud_reminders=None, allow_icloud_address_book=None, allow_icloud_notes=None, allow_icloud_keychain_sync=None, allow_air_print=None, force_air_print_trusted_tls_requirement=None, allow_air_printi_beacon_discovery=None, allow_cloud_desktop_and_documents=None, allow_password_auto_fill=None, allow_password_sharing=None, allow_deprecated_web_kit_tls=None, allow_password_proximity_requests=None, _configuration=None):  # noqa: E501
        """AppleOsXRestrictionICloudPayloadEntity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_icloud_documents_and_data = None
        self._allow_use_icloud_password_for_local_accounts = None
        self._allow_icloud_btmm = None
        self._allow_i_cloud_fmm = None
        self._allow_icloud_bookmarks = None
        self._allow_icloud_mail = None
        self._allow_icloud_calendar = None
        self._allow_icloud_reminders = None
        self._allow_icloud_address_book = None
        self._allow_icloud_notes = None
        self._allow_icloud_keychain_sync = None
        self._allow_air_print = None
        self._force_air_print_trusted_tls_requirement = None
        self._allow_air_printi_beacon_discovery = None
        self._allow_cloud_desktop_and_documents = None
        self._allow_password_auto_fill = None
        self._allow_password_sharing = None
        self._allow_deprecated_web_kit_tls = None
        self._allow_password_proximity_requests = None
        self.discriminator = None

        if allow_icloud_documents_and_data is not None:
            self.allow_icloud_documents_and_data = allow_icloud_documents_and_data
        if allow_use_icloud_password_for_local_accounts is not None:
            self.allow_use_icloud_password_for_local_accounts = allow_use_icloud_password_for_local_accounts
        if allow_icloud_btmm is not None:
            self.allow_icloud_btmm = allow_icloud_btmm
        if allow_i_cloud_fmm is not None:
            self.allow_i_cloud_fmm = allow_i_cloud_fmm
        if allow_icloud_bookmarks is not None:
            self.allow_icloud_bookmarks = allow_icloud_bookmarks
        if allow_icloud_mail is not None:
            self.allow_icloud_mail = allow_icloud_mail
        if allow_icloud_calendar is not None:
            self.allow_icloud_calendar = allow_icloud_calendar
        if allow_icloud_reminders is not None:
            self.allow_icloud_reminders = allow_icloud_reminders
        if allow_icloud_address_book is not None:
            self.allow_icloud_address_book = allow_icloud_address_book
        if allow_icloud_notes is not None:
            self.allow_icloud_notes = allow_icloud_notes
        if allow_icloud_keychain_sync is not None:
            self.allow_icloud_keychain_sync = allow_icloud_keychain_sync
        if allow_air_print is not None:
            self.allow_air_print = allow_air_print
        if force_air_print_trusted_tls_requirement is not None:
            self.force_air_print_trusted_tls_requirement = force_air_print_trusted_tls_requirement
        if allow_air_printi_beacon_discovery is not None:
            self.allow_air_printi_beacon_discovery = allow_air_printi_beacon_discovery
        if allow_cloud_desktop_and_documents is not None:
            self.allow_cloud_desktop_and_documents = allow_cloud_desktop_and_documents
        if allow_password_auto_fill is not None:
            self.allow_password_auto_fill = allow_password_auto_fill
        if allow_password_sharing is not None:
            self.allow_password_sharing = allow_password_sharing
        if allow_deprecated_web_kit_tls is not None:
            self.allow_deprecated_web_kit_tls = allow_deprecated_web_kit_tls
        if allow_password_proximity_requests is not None:
            self.allow_password_proximity_requests = allow_password_proximity_requests

    @property
    def allow_icloud_documents_and_data(self):
        """Gets the allow_icloud_documents_and_data of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disables document and key-value syncing to iCloud on macOS 10.11+.  # noqa: E501

        :return: The allow_icloud_documents_and_data of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_icloud_documents_and_data

    @allow_icloud_documents_and_data.setter
    def allow_icloud_documents_and_data(self, allow_icloud_documents_and_data):
        """Sets the allow_icloud_documents_and_data of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disables document and key-value syncing to iCloud on macOS 10.11+.  # noqa: E501

        :param allow_icloud_documents_and_data: The allow_icloud_documents_and_data of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_icloud_documents_and_data = allow_icloud_documents_and_data

    @property
    def allow_use_icloud_password_for_local_accounts(self):
        """Gets the allow_use_icloud_password_for_local_accounts of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disables use of iCloud password for local accounts.  # noqa: E501

        :return: The allow_use_icloud_password_for_local_accounts of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_use_icloud_password_for_local_accounts

    @allow_use_icloud_password_for_local_accounts.setter
    def allow_use_icloud_password_for_local_accounts(self, allow_use_icloud_password_for_local_accounts):
        """Sets the allow_use_icloud_password_for_local_accounts of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disables use of iCloud password for local accounts.  # noqa: E501

        :param allow_use_icloud_password_for_local_accounts: The allow_use_icloud_password_for_local_accounts of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_use_icloud_password_for_local_accounts = allow_use_icloud_password_for_local_accounts

    @property
    def allow_icloud_btmm(self):
        """Gets the allow_icloud_btmm of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disallows macOS Back to My Mac iCloud service on macOS 10.12+.  # noqa: E501

        :return: The allow_icloud_btmm of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_icloud_btmm

    @allow_icloud_btmm.setter
    def allow_icloud_btmm(self, allow_icloud_btmm):
        """Sets the allow_icloud_btmm of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disallows macOS Back to My Mac iCloud service on macOS 10.12+.  # noqa: E501

        :param allow_icloud_btmm: The allow_icloud_btmm of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_icloud_btmm = allow_icloud_btmm

    @property
    def allow_i_cloud_fmm(self):
        """Gets the allow_i_cloud_fmm of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disallows macOS Find My Mac iCloud service on macOS 10.12+.  # noqa: E501

        :return: The allow_i_cloud_fmm of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_i_cloud_fmm

    @allow_i_cloud_fmm.setter
    def allow_i_cloud_fmm(self, allow_i_cloud_fmm):
        """Sets the allow_i_cloud_fmm of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disallows macOS Find My Mac iCloud service on macOS 10.12+.  # noqa: E501

        :param allow_i_cloud_fmm: The allow_i_cloud_fmm of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_i_cloud_fmm = allow_i_cloud_fmm

    @property
    def allow_icloud_bookmarks(self):
        """Gets the allow_icloud_bookmarks of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disallows macOS iCloud Bookmark sync on macOS 10.12+.  # noqa: E501

        :return: The allow_icloud_bookmarks of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_icloud_bookmarks

    @allow_icloud_bookmarks.setter
    def allow_icloud_bookmarks(self, allow_icloud_bookmarks):
        """Sets the allow_icloud_bookmarks of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disallows macOS iCloud Bookmark sync on macOS 10.12+.  # noqa: E501

        :param allow_icloud_bookmarks: The allow_icloud_bookmarks of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_icloud_bookmarks = allow_icloud_bookmarks

    @property
    def allow_icloud_mail(self):
        """Gets the allow_icloud_mail of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disallows macOS Mail iCloud services on macOS 10.12+.  # noqa: E501

        :return: The allow_icloud_mail of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_icloud_mail

    @allow_icloud_mail.setter
    def allow_icloud_mail(self, allow_icloud_mail):
        """Sets the allow_icloud_mail of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disallows macOS Mail iCloud services on macOS 10.12+.  # noqa: E501

        :param allow_icloud_mail: The allow_icloud_mail of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_icloud_mail = allow_icloud_mail

    @property
    def allow_icloud_calendar(self):
        """Gets the allow_icloud_calendar of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disallows macOS iCloud Calendar services on macOS 10.12+.  # noqa: E501

        :return: The allow_icloud_calendar of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_icloud_calendar

    @allow_icloud_calendar.setter
    def allow_icloud_calendar(self, allow_icloud_calendar):
        """Sets the allow_icloud_calendar of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disallows macOS iCloud Calendar services on macOS 10.12+.  # noqa: E501

        :param allow_icloud_calendar: The allow_icloud_calendar of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_icloud_calendar = allow_icloud_calendar

    @property
    def allow_icloud_reminders(self):
        """Gets the allow_icloud_reminders of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disallows iCloud Reminder services on macOS 10.12+.  # noqa: E501

        :return: The allow_icloud_reminders of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_icloud_reminders

    @allow_icloud_reminders.setter
    def allow_icloud_reminders(self, allow_icloud_reminders):
        """Sets the allow_icloud_reminders of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disallows iCloud Reminder services on macOS 10.12+.  # noqa: E501

        :param allow_icloud_reminders: The allow_icloud_reminders of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_icloud_reminders = allow_icloud_reminders

    @property
    def allow_icloud_address_book(self):
        """Gets the allow_icloud_address_book of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disallows macOS iCloud Address Book services on macOS 10.12+.  # noqa: E501

        :return: The allow_icloud_address_book of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_icloud_address_book

    @allow_icloud_address_book.setter
    def allow_icloud_address_book(self, allow_icloud_address_book):
        """Sets the allow_icloud_address_book of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disallows macOS iCloud Address Book services on macOS 10.12+.  # noqa: E501

        :param allow_icloud_address_book: The allow_icloud_address_book of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_icloud_address_book = allow_icloud_address_book

    @property
    def allow_icloud_notes(self):
        """Gets the allow_icloud_notes of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disallows macOS iCloud Notes services on macOS 10.12+.  # noqa: E501

        :return: The allow_icloud_notes of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_icloud_notes

    @allow_icloud_notes.setter
    def allow_icloud_notes(self, allow_icloud_notes):
        """Sets the allow_icloud_notes of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disallows macOS iCloud Notes services on macOS 10.12+.  # noqa: E501

        :param allow_icloud_notes: The allow_icloud_notes of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_icloud_notes = allow_icloud_notes

    @property
    def allow_icloud_keychain_sync(self):
        """Gets the allow_icloud_keychain_sync of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disables iCloud keychain synchronization on macOS 10.12+.  # noqa: E501

        :return: The allow_icloud_keychain_sync of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_icloud_keychain_sync

    @allow_icloud_keychain_sync.setter
    def allow_icloud_keychain_sync(self, allow_icloud_keychain_sync):
        """Sets the allow_icloud_keychain_sync of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disables iCloud keychain synchronization on macOS 10.12+.  # noqa: E501

        :param allow_icloud_keychain_sync: The allow_icloud_keychain_sync of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_icloud_keychain_sync = allow_icloud_keychain_sync

    @property
    def allow_air_print(self):
        """Gets the allow_air_print of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disallows AirPrint on macOS 10.13+.  # noqa: E501

        :return: The allow_air_print of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_air_print

    @allow_air_print.setter
    def allow_air_print(self, allow_air_print):
        """Sets the allow_air_print of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disallows AirPrint on macOS 10.13+.  # noqa: E501

        :param allow_air_print: The allow_air_print of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_air_print = allow_air_print

    @property
    def force_air_print_trusted_tls_requirement(self):
        """Gets the force_air_print_trusted_tls_requirement of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to true, requires trusted certificates for TLS printing communication on macOS 10.13+.  # noqa: E501

        :return: The force_air_print_trusted_tls_requirement of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._force_air_print_trusted_tls_requirement

    @force_air_print_trusted_tls_requirement.setter
    def force_air_print_trusted_tls_requirement(self, force_air_print_trusted_tls_requirement):
        """Sets the force_air_print_trusted_tls_requirement of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to true, requires trusted certificates for TLS printing communication on macOS 10.13+.  # noqa: E501

        :param force_air_print_trusted_tls_requirement: The force_air_print_trusted_tls_requirement of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._force_air_print_trusted_tls_requirement = force_air_print_trusted_tls_requirement

    @property
    def allow_air_printi_beacon_discovery(self):
        """Gets the allow_air_printi_beacon_discovery of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to false, disables iBeacon discovery of AirPrint printers on macOS 10.13+.  # noqa: E501

        :return: The allow_air_printi_beacon_discovery of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_air_printi_beacon_discovery

    @allow_air_printi_beacon_discovery.setter
    def allow_air_printi_beacon_discovery(self, allow_air_printi_beacon_discovery):
        """Sets the allow_air_printi_beacon_discovery of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether if set to false, disables iBeacon discovery of AirPrint printers on macOS 10.13+.  # noqa: E501

        :param allow_air_printi_beacon_discovery: The allow_air_printi_beacon_discovery of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_air_printi_beacon_discovery = allow_air_printi_beacon_discovery

    @property
    def allow_cloud_desktop_and_documents(self):
        """Gets the allow_cloud_desktop_and_documents of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether [allow cloud desktop and documents].  # noqa: E501

        :return: The allow_cloud_desktop_and_documents of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_cloud_desktop_and_documents

    @allow_cloud_desktop_and_documents.setter
    def allow_cloud_desktop_and_documents(self, allow_cloud_desktop_and_documents):
        """Sets the allow_cloud_desktop_and_documents of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether [allow cloud desktop and documents].  # noqa: E501

        :param allow_cloud_desktop_and_documents: The allow_cloud_desktop_and_documents of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_cloud_desktop_and_documents = allow_cloud_desktop_and_documents

    @property
    def allow_password_auto_fill(self):
        """Gets the allow_password_auto_fill of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether gets or sets a value which indicates whether to allow auto filling of passwords is allowed or not on supervised iOS 12.0+.  # noqa: E501

        :return: The allow_password_auto_fill of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_password_auto_fill

    @allow_password_auto_fill.setter
    def allow_password_auto_fill(self, allow_password_auto_fill):
        """Sets the allow_password_auto_fill of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether gets or sets a value which indicates whether to allow auto filling of passwords is allowed or not on supervised iOS 12.0+.  # noqa: E501

        :param allow_password_auto_fill: The allow_password_auto_fill of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_password_auto_fill = allow_password_auto_fill

    @property
    def allow_password_sharing(self):
        """Gets the allow_password_sharing of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether gets or sets a value which indicates whether allow sharing of Wi-Fi passwords is allowed or not on supervised iOS 12.0+.  # noqa: E501

        :return: The allow_password_sharing of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_password_sharing

    @allow_password_sharing.setter
    def allow_password_sharing(self, allow_password_sharing):
        """Sets the allow_password_sharing of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether gets or sets a value which indicates whether allow sharing of Wi-Fi passwords is allowed or not on supervised iOS 12.0+.  # noqa: E501

        :param allow_password_sharing: The allow_password_sharing of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_password_sharing = allow_password_sharing

    @property
    def allow_deprecated_web_kit_tls(self):
        """Gets the allow_deprecated_web_kit_tls of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether gets or sets a value which indicates whether the deprecated TLS 1.0/1.1 behavior in Safari is allowed. Available in macOS 10.15.4 and later.  # noqa: E501

        :return: The allow_deprecated_web_kit_tls of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_deprecated_web_kit_tls

    @allow_deprecated_web_kit_tls.setter
    def allow_deprecated_web_kit_tls(self, allow_deprecated_web_kit_tls):
        """Sets the allow_deprecated_web_kit_tls of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether gets or sets a value which indicates whether the deprecated TLS 1.0/1.1 behavior in Safari is allowed. Available in macOS 10.15.4 and later.  # noqa: E501

        :param allow_deprecated_web_kit_tls: The allow_deprecated_web_kit_tls of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_deprecated_web_kit_tls = allow_deprecated_web_kit_tls

    @property
    def allow_password_proximity_requests(self):
        """Gets the allow_password_proximity_requests of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether requesting passwords from nearby devices is allowed. Requires a supervised device. Available in macOS 10.14 and later.  # noqa: E501

        :return: The allow_password_proximity_requests of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_password_proximity_requests

    @allow_password_proximity_requests.setter
    def allow_password_proximity_requests(self, allow_password_proximity_requests):
        """Sets the allow_password_proximity_requests of this AppleOsXRestrictionICloudPayloadEntity_.

        Gets or sets a value indicating whether requesting passwords from nearby devices is allowed. Requires a supervised device. Available in macOS 10.14 and later.  # noqa: E501

        :param allow_password_proximity_requests: The allow_password_proximity_requests of this AppleOsXRestrictionICloudPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._allow_password_proximity_requests = allow_password_proximity_requests

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
        if issubclass(AppleOsXRestrictionICloudPayloadEntity_, dict):
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
        if not isinstance(other, AppleOsXRestrictionICloudPayloadEntity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleOsXRestrictionICloudPayloadEntity_):
            return True

        return self.to_dict() != other.to_dict()
