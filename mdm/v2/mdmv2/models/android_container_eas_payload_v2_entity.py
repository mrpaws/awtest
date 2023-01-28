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


class AndroidContainerEasPayloadV2Entity(object):
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
        'mail_client_type': 'int',
        'email_address': 'str',
        'max_email_age_filter': 'int',
        'sync_interval': 'int',
        'peak_days': 'int',
        'peak_start_minute': 'int',
        'peak_end_minute': 'int',
        'peak_sync_schedule': 'int',
        'off_peak_sync_schedule': 'int',
        'roaming_sync_schedule': 'int',
        'retrieval_size': 'int',
        'period_calendar': 'int',
        'sender_name': 'str',
        'account_name': 'str',
        'use_ssl': 'bool',
        'use_tls': 'bool',
        'protocol': 'str',
        'host': 'str',
        'domain': 'str',
        'username': 'str',
        'password': 'str',
        'path_prefix': 'str',
        'certificate_payload_uuid': 'str',
        'accept_certs': 'bool',
        'allow_vibrate_on_notification': 'bool',
        'allow_silent_notification': 'bool',
        'email_signature': 'str',
        'default_account': 'bool',
        'allow_email_forwarding': 'bool',
        'allow_html_email': 'bool',
        'smime_cert_payload_uuid': 'str',
        'allow_smime_cert_select': 'bool',
        'require_encrypted_smime': 'bool',
        'require_signed_smime': 'bool'
    }

    attribute_map = {
        'mail_client_type': 'MailClientType',
        'email_address': 'EmailAddress',
        'max_email_age_filter': 'MaxEmailAgeFilter',
        'sync_interval': 'SyncInterval',
        'peak_days': 'PeakDays',
        'peak_start_minute': 'peakStartMinute',
        'peak_end_minute': 'peakEndMinute',
        'peak_sync_schedule': 'peakSyncSchedule',
        'off_peak_sync_schedule': 'offPeakSyncSchedule',
        'roaming_sync_schedule': 'RoamingSyncSchedule',
        'retrieval_size': 'RetrievalSize',
        'period_calendar': 'PeriodCalendar',
        'sender_name': 'SenderName',
        'account_name': 'AccountName',
        'use_ssl': 'UseSSL',
        'use_tls': 'UseTLS',
        'protocol': 'Protocol',
        'host': 'Host',
        'domain': 'Domain',
        'username': 'Username',
        'password': 'Password',
        'path_prefix': 'PathPrefix',
        'certificate_payload_uuid': 'CertificatePayloadUUID',
        'accept_certs': 'AcceptCerts',
        'allow_vibrate_on_notification': 'allowVibrateOnNotification',
        'allow_silent_notification': 'allowSilentNotification',
        'email_signature': 'EmailSignature',
        'default_account': 'DefaultAccount',
        'allow_email_forwarding': 'AllowEmailForwarding',
        'allow_html_email': 'AllowHTMLEmail',
        'smime_cert_payload_uuid': 'SMIMECertPayloadUUID',
        'allow_smime_cert_select': 'AllowSMIMECertSelect',
        'require_encrypted_smime': 'RequireEncryptedSMIME',
        'require_signed_smime': 'RequireSignedSMIME'
    }

    def __init__(self, mail_client_type=None, email_address=None, max_email_age_filter=None, sync_interval=None, peak_days=None, peak_start_minute=None, peak_end_minute=None, peak_sync_schedule=None, off_peak_sync_schedule=None, roaming_sync_schedule=None, retrieval_size=None, period_calendar=None, sender_name=None, account_name=None, use_ssl=None, use_tls=None, protocol=None, host=None, domain=None, username=None, password=None, path_prefix=None, certificate_payload_uuid=None, accept_certs=None, allow_vibrate_on_notification=None, allow_silent_notification=None, email_signature=None, default_account=None, allow_email_forwarding=None, allow_html_email=None, smime_cert_payload_uuid=None, allow_smime_cert_select=None, require_encrypted_smime=None, require_signed_smime=None, _configuration=None):  # noqa: E501
        """AndroidContainerEasPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._mail_client_type = None
        self._email_address = None
        self._max_email_age_filter = None
        self._sync_interval = None
        self._peak_days = None
        self._peak_start_minute = None
        self._peak_end_minute = None
        self._peak_sync_schedule = None
        self._off_peak_sync_schedule = None
        self._roaming_sync_schedule = None
        self._retrieval_size = None
        self._period_calendar = None
        self._sender_name = None
        self._account_name = None
        self._use_ssl = None
        self._use_tls = None
        self._protocol = None
        self._host = None
        self._domain = None
        self._username = None
        self._password = None
        self._path_prefix = None
        self._certificate_payload_uuid = None
        self._accept_certs = None
        self._allow_vibrate_on_notification = None
        self._allow_silent_notification = None
        self._email_signature = None
        self._default_account = None
        self._allow_email_forwarding = None
        self._allow_html_email = None
        self._smime_cert_payload_uuid = None
        self._allow_smime_cert_select = None
        self._require_encrypted_smime = None
        self._require_signed_smime = None
        self.discriminator = None

        if mail_client_type is not None:
            self.mail_client_type = mail_client_type
        if email_address is not None:
            self.email_address = email_address
        if max_email_age_filter is not None:
            self.max_email_age_filter = max_email_age_filter
        if sync_interval is not None:
            self.sync_interval = sync_interval
        if peak_days is not None:
            self.peak_days = peak_days
        if peak_start_minute is not None:
            self.peak_start_minute = peak_start_minute
        if peak_end_minute is not None:
            self.peak_end_minute = peak_end_minute
        if peak_sync_schedule is not None:
            self.peak_sync_schedule = peak_sync_schedule
        if off_peak_sync_schedule is not None:
            self.off_peak_sync_schedule = off_peak_sync_schedule
        if roaming_sync_schedule is not None:
            self.roaming_sync_schedule = roaming_sync_schedule
        if retrieval_size is not None:
            self.retrieval_size = retrieval_size
        if period_calendar is not None:
            self.period_calendar = period_calendar
        if sender_name is not None:
            self.sender_name = sender_name
        if account_name is not None:
            self.account_name = account_name
        if use_ssl is not None:
            self.use_ssl = use_ssl
        if use_tls is not None:
            self.use_tls = use_tls
        if protocol is not None:
            self.protocol = protocol
        if host is not None:
            self.host = host
        if domain is not None:
            self.domain = domain
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if path_prefix is not None:
            self.path_prefix = path_prefix
        if certificate_payload_uuid is not None:
            self.certificate_payload_uuid = certificate_payload_uuid
        if accept_certs is not None:
            self.accept_certs = accept_certs
        if allow_vibrate_on_notification is not None:
            self.allow_vibrate_on_notification = allow_vibrate_on_notification
        if allow_silent_notification is not None:
            self.allow_silent_notification = allow_silent_notification
        if email_signature is not None:
            self.email_signature = email_signature
        if default_account is not None:
            self.default_account = default_account
        if allow_email_forwarding is not None:
            self.allow_email_forwarding = allow_email_forwarding
        if allow_html_email is not None:
            self.allow_html_email = allow_html_email
        if smime_cert_payload_uuid is not None:
            self.smime_cert_payload_uuid = smime_cert_payload_uuid
        if allow_smime_cert_select is not None:
            self.allow_smime_cert_select = allow_smime_cert_select
        if require_encrypted_smime is not None:
            self.require_encrypted_smime = require_encrypted_smime
        if require_signed_smime is not None:
            self.require_signed_smime = require_signed_smime

    @property
    def mail_client_type(self):
        """Gets the mail_client_type of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets MailClientType.  # noqa: E501

        :return: The mail_client_type of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._mail_client_type

    @mail_client_type.setter
    def mail_client_type(self, mail_client_type):
        """Sets the mail_client_type of this AndroidContainerEasPayloadV2Entity.

        Gets or sets MailClientType.  # noqa: E501

        :param mail_client_type: The mail_client_type of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._mail_client_type = mail_client_type

    @property
    def email_address(self):
        """Gets the email_address of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets EmailAddress.  # noqa: E501

        :return: The email_address of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this AndroidContainerEasPayloadV2Entity.

        Gets or sets EmailAddress.  # noqa: E501

        :param email_address: The email_address of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def max_email_age_filter(self):
        """Gets the max_email_age_filter of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets MaxEmailAgeFilter.  # noqa: E501

        :return: The max_email_age_filter of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._max_email_age_filter

    @max_email_age_filter.setter
    def max_email_age_filter(self, max_email_age_filter):
        """Sets the max_email_age_filter of this AndroidContainerEasPayloadV2Entity.

        Gets or sets MaxEmailAgeFilter.  # noqa: E501

        :param max_email_age_filter: The max_email_age_filter of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._max_email_age_filter = max_email_age_filter

    @property
    def sync_interval(self):
        """Gets the sync_interval of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets SyncInterval.  # noqa: E501

        :return: The sync_interval of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._sync_interval

    @sync_interval.setter
    def sync_interval(self, sync_interval):
        """Sets the sync_interval of this AndroidContainerEasPayloadV2Entity.

        Gets or sets SyncInterval.  # noqa: E501

        :param sync_interval: The sync_interval of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._sync_interval = sync_interval

    @property
    def peak_days(self):
        """Gets the peak_days of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets PeakDays.  # noqa: E501

        :return: The peak_days of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._peak_days

    @peak_days.setter
    def peak_days(self, peak_days):
        """Sets the peak_days of this AndroidContainerEasPayloadV2Entity.

        Gets or sets PeakDays.  # noqa: E501

        :param peak_days: The peak_days of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._peak_days = peak_days

    @property
    def peak_start_minute(self):
        """Gets the peak_start_minute of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets peakStartMinute.  # noqa: E501

        :return: The peak_start_minute of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._peak_start_minute

    @peak_start_minute.setter
    def peak_start_minute(self, peak_start_minute):
        """Sets the peak_start_minute of this AndroidContainerEasPayloadV2Entity.

        Gets or sets peakStartMinute.  # noqa: E501

        :param peak_start_minute: The peak_start_minute of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._peak_start_minute = peak_start_minute

    @property
    def peak_end_minute(self):
        """Gets the peak_end_minute of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets PeakEndMinute.  # noqa: E501

        :return: The peak_end_minute of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._peak_end_minute

    @peak_end_minute.setter
    def peak_end_minute(self, peak_end_minute):
        """Sets the peak_end_minute of this AndroidContainerEasPayloadV2Entity.

        Gets or sets PeakEndMinute.  # noqa: E501

        :param peak_end_minute: The peak_end_minute of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._peak_end_minute = peak_end_minute

    @property
    def peak_sync_schedule(self):
        """Gets the peak_sync_schedule of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets peakSyncSchedule.  # noqa: E501

        :return: The peak_sync_schedule of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._peak_sync_schedule

    @peak_sync_schedule.setter
    def peak_sync_schedule(self, peak_sync_schedule):
        """Sets the peak_sync_schedule of this AndroidContainerEasPayloadV2Entity.

        Gets or sets peakSyncSchedule.  # noqa: E501

        :param peak_sync_schedule: The peak_sync_schedule of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._peak_sync_schedule = peak_sync_schedule

    @property
    def off_peak_sync_schedule(self):
        """Gets the off_peak_sync_schedule of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets OffPeakSyncSchedule.  # noqa: E501

        :return: The off_peak_sync_schedule of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._off_peak_sync_schedule

    @off_peak_sync_schedule.setter
    def off_peak_sync_schedule(self, off_peak_sync_schedule):
        """Sets the off_peak_sync_schedule of this AndroidContainerEasPayloadV2Entity.

        Gets or sets OffPeakSyncSchedule.  # noqa: E501

        :param off_peak_sync_schedule: The off_peak_sync_schedule of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._off_peak_sync_schedule = off_peak_sync_schedule

    @property
    def roaming_sync_schedule(self):
        """Gets the roaming_sync_schedule of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets RoamingSyncSchedule.  # noqa: E501

        :return: The roaming_sync_schedule of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._roaming_sync_schedule

    @roaming_sync_schedule.setter
    def roaming_sync_schedule(self, roaming_sync_schedule):
        """Sets the roaming_sync_schedule of this AndroidContainerEasPayloadV2Entity.

        Gets or sets RoamingSyncSchedule.  # noqa: E501

        :param roaming_sync_schedule: The roaming_sync_schedule of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._roaming_sync_schedule = roaming_sync_schedule

    @property
    def retrieval_size(self):
        """Gets the retrieval_size of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets RetrievalSize.  # noqa: E501

        :return: The retrieval_size of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._retrieval_size

    @retrieval_size.setter
    def retrieval_size(self, retrieval_size):
        """Sets the retrieval_size of this AndroidContainerEasPayloadV2Entity.

        Gets or sets RetrievalSize.  # noqa: E501

        :param retrieval_size: The retrieval_size of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._retrieval_size = retrieval_size

    @property
    def period_calendar(self):
        """Gets the period_calendar of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets PeriodCalendar.  # noqa: E501

        :return: The period_calendar of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._period_calendar

    @period_calendar.setter
    def period_calendar(self, period_calendar):
        """Sets the period_calendar of this AndroidContainerEasPayloadV2Entity.

        Gets or sets PeriodCalendar.  # noqa: E501

        :param period_calendar: The period_calendar of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._period_calendar = period_calendar

    @property
    def sender_name(self):
        """Gets the sender_name of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets SenderName.  # noqa: E501

        :return: The sender_name of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """Sets the sender_name of this AndroidContainerEasPayloadV2Entity.

        Gets or sets SenderName.  # noqa: E501

        :param sender_name: The sender_name of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._sender_name = sender_name

    @property
    def account_name(self):
        """Gets the account_name of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets AccountName.  # noqa: E501

        :return: The account_name of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AndroidContainerEasPayloadV2Entity.

        Gets or sets AccountName.  # noqa: E501

        :param account_name: The account_name of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def use_ssl(self):
        """Gets the use_ssl of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets UseSSL.  # noqa: E501

        :return: The use_ssl of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this AndroidContainerEasPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets UseSSL.  # noqa: E501

        :param use_ssl: The use_ssl of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def use_tls(self):
        """Gets the use_tls of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets UseTLS.  # noqa: E501

        :return: The use_tls of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._use_tls

    @use_tls.setter
    def use_tls(self, use_tls):
        """Sets the use_tls of this AndroidContainerEasPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets UseTLS.  # noqa: E501

        :param use_tls: The use_tls of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._use_tls = use_tls

    @property
    def protocol(self):
        """Gets the protocol of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets Protocol.  # noqa: E501

        :return: The protocol of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this AndroidContainerEasPayloadV2Entity.

        Gets or sets Protocol.  # noqa: E501

        :param protocol: The protocol of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def host(self):
        """Gets the host of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets Host.  # noqa: E501

        :return: The host of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this AndroidContainerEasPayloadV2Entity.

        Gets or sets Host.  # noqa: E501

        :param host: The host of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def domain(self):
        """Gets the domain of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets Domain.  # noqa: E501

        :return: The domain of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AndroidContainerEasPayloadV2Entity.

        Gets or sets Domain.  # noqa: E501

        :param domain: The domain of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def username(self):
        """Gets the username of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets Username.  # noqa: E501

        :return: The username of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AndroidContainerEasPayloadV2Entity.

        Gets or sets Username.  # noqa: E501

        :param username: The username of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets Password.  # noqa: E501

        :return: The password of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AndroidContainerEasPayloadV2Entity.

        Gets or sets Password.  # noqa: E501

        :param password: The password of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def path_prefix(self):
        """Gets the path_prefix of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets PathPrefix.  # noqa: E501

        :return: The path_prefix of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._path_prefix

    @path_prefix.setter
    def path_prefix(self, path_prefix):
        """Sets the path_prefix of this AndroidContainerEasPayloadV2Entity.

        Gets or sets PathPrefix.  # noqa: E501

        :param path_prefix: The path_prefix of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._path_prefix = path_prefix

    @property
    def certificate_payload_uuid(self):
        """Gets the certificate_payload_uuid of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets CertificatePayloadUUID.  # noqa: E501

        :return: The certificate_payload_uuid of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._certificate_payload_uuid

    @certificate_payload_uuid.setter
    def certificate_payload_uuid(self, certificate_payload_uuid):
        """Sets the certificate_payload_uuid of this AndroidContainerEasPayloadV2Entity.

        Gets or sets CertificatePayloadUUID.  # noqa: E501

        :param certificate_payload_uuid: The certificate_payload_uuid of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._certificate_payload_uuid = certificate_payload_uuid

    @property
    def accept_certs(self):
        """Gets the accept_certs of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets AcceptCerts.  # noqa: E501

        :return: The accept_certs of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._accept_certs

    @accept_certs.setter
    def accept_certs(self, accept_certs):
        """Sets the accept_certs of this AndroidContainerEasPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets AcceptCerts.  # noqa: E501

        :param accept_certs: The accept_certs of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._accept_certs = accept_certs

    @property
    def allow_vibrate_on_notification(self):
        """Gets the allow_vibrate_on_notification of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets AllowVibrateOnNotification.  # noqa: E501

        :return: The allow_vibrate_on_notification of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_vibrate_on_notification

    @allow_vibrate_on_notification.setter
    def allow_vibrate_on_notification(self, allow_vibrate_on_notification):
        """Sets the allow_vibrate_on_notification of this AndroidContainerEasPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets AllowVibrateOnNotification.  # noqa: E501

        :param allow_vibrate_on_notification: The allow_vibrate_on_notification of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_vibrate_on_notification = allow_vibrate_on_notification

    @property
    def allow_silent_notification(self):
        """Gets the allow_silent_notification of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets allowSilentNotification.  # noqa: E501

        :return: The allow_silent_notification of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_silent_notification

    @allow_silent_notification.setter
    def allow_silent_notification(self, allow_silent_notification):
        """Sets the allow_silent_notification of this AndroidContainerEasPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets allowSilentNotification.  # noqa: E501

        :param allow_silent_notification: The allow_silent_notification of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_silent_notification = allow_silent_notification

    @property
    def email_signature(self):
        """Gets the email_signature of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets EmailSignature.  # noqa: E501

        :return: The email_signature of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._email_signature

    @email_signature.setter
    def email_signature(self, email_signature):
        """Sets the email_signature of this AndroidContainerEasPayloadV2Entity.

        Gets or sets EmailSignature.  # noqa: E501

        :param email_signature: The email_signature of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._email_signature = email_signature

    @property
    def default_account(self):
        """Gets the default_account of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets DefaultAccount.  # noqa: E501

        :return: The default_account of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._default_account

    @default_account.setter
    def default_account(self, default_account):
        """Sets the default_account of this AndroidContainerEasPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets DefaultAccount.  # noqa: E501

        :param default_account: The default_account of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._default_account = default_account

    @property
    def allow_email_forwarding(self):
        """Gets the allow_email_forwarding of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets AllowEmailForwarding.  # noqa: E501

        :return: The allow_email_forwarding of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_email_forwarding

    @allow_email_forwarding.setter
    def allow_email_forwarding(self, allow_email_forwarding):
        """Sets the allow_email_forwarding of this AndroidContainerEasPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets AllowEmailForwarding.  # noqa: E501

        :param allow_email_forwarding: The allow_email_forwarding of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_email_forwarding = allow_email_forwarding

    @property
    def allow_html_email(self):
        """Gets the allow_html_email of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets AllowHTMLEmail.  # noqa: E501

        :return: The allow_html_email of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_html_email

    @allow_html_email.setter
    def allow_html_email(self, allow_html_email):
        """Sets the allow_html_email of this AndroidContainerEasPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets AllowHTMLEmail.  # noqa: E501

        :param allow_html_email: The allow_html_email of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_html_email = allow_html_email

    @property
    def smime_cert_payload_uuid(self):
        """Gets the smime_cert_payload_uuid of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets SMIMECertPayloadUUID.  # noqa: E501

        :return: The smime_cert_payload_uuid of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._smime_cert_payload_uuid

    @smime_cert_payload_uuid.setter
    def smime_cert_payload_uuid(self, smime_cert_payload_uuid):
        """Sets the smime_cert_payload_uuid of this AndroidContainerEasPayloadV2Entity.

        Gets or sets SMIMECertPayloadUUID.  # noqa: E501

        :param smime_cert_payload_uuid: The smime_cert_payload_uuid of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._smime_cert_payload_uuid = smime_cert_payload_uuid

    @property
    def allow_smime_cert_select(self):
        """Gets the allow_smime_cert_select of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets AllowSMIMECertSelect.  # noqa: E501

        :return: The allow_smime_cert_select of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_smime_cert_select

    @allow_smime_cert_select.setter
    def allow_smime_cert_select(self, allow_smime_cert_select):
        """Sets the allow_smime_cert_select of this AndroidContainerEasPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets AllowSMIMECertSelect.  # noqa: E501

        :param allow_smime_cert_select: The allow_smime_cert_select of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_smime_cert_select = allow_smime_cert_select

    @property
    def require_encrypted_smime(self):
        """Gets the require_encrypted_smime of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets RequireEncryptedSMIME.  # noqa: E501

        :return: The require_encrypted_smime of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._require_encrypted_smime

    @require_encrypted_smime.setter
    def require_encrypted_smime(self, require_encrypted_smime):
        """Sets the require_encrypted_smime of this AndroidContainerEasPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets RequireEncryptedSMIME.  # noqa: E501

        :param require_encrypted_smime: The require_encrypted_smime of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._require_encrypted_smime = require_encrypted_smime

    @property
    def require_signed_smime(self):
        """Gets the require_signed_smime of this AndroidContainerEasPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets RequireSignedSMIME.  # noqa: E501

        :return: The require_signed_smime of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._require_signed_smime

    @require_signed_smime.setter
    def require_signed_smime(self, require_signed_smime):
        """Sets the require_signed_smime of this AndroidContainerEasPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets RequireSignedSMIME.  # noqa: E501

        :param require_signed_smime: The require_signed_smime of this AndroidContainerEasPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._require_signed_smime = require_signed_smime

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
        if issubclass(AndroidContainerEasPayloadV2Entity, dict):
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
        if not isinstance(other, AndroidContainerEasPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidContainerEasPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
