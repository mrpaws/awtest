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


class MacOsSsoExtensionPayloadV2Entity(object):
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
        'extension_type': 'int',
        'extension_identifier': 'str',
        'type': 'str',
        'realm': 'str',
        'team_identifier': 'str',
        'hosts': 'list[str]',
        'urls': 'list[str]',
        'custom_xml': 'str',
        'certificate_uuid': 'str',
        'certificate_name': 'str',
        'use_site_auto_discovery': 'bool',
        'allow_automatic_login': 'bool',
        'require_user_touch_id_or_password': 'bool',
        'credential_bundle_ids': 'list[str]',
        'allow_password_change': 'bool',
        'sync_local_password': 'bool',
        'match_ad_password_complexity': 'bool',
        'password_change_message': 'str',
        'minimum_password_length': 'int',
        'password_history_count': 'int',
        'password_minimum_age': 'int',
        'password_expire_notification_days': 'int'
    }

    attribute_map = {
        'extension_type': 'ExtensionType',
        'extension_identifier': 'ExtensionIdentifier',
        'type': 'Type',
        'realm': 'Realm',
        'team_identifier': 'TeamIdentifier',
        'hosts': 'Hosts',
        'urls': 'URLs',
        'custom_xml': 'CustomXml',
        'certificate_uuid': 'certificateUUID',
        'certificate_name': 'CertificateName',
        'use_site_auto_discovery': 'UseSiteAutoDiscovery',
        'allow_automatic_login': 'AllowAutomaticLogin',
        'require_user_touch_id_or_password': 'RequireUserTouchIdOrPassword',
        'credential_bundle_ids': 'CredentialBundleIds',
        'allow_password_change': 'AllowPasswordChange',
        'sync_local_password': 'SyncLocalPassword',
        'match_ad_password_complexity': 'MatchADPasswordComplexity',
        'password_change_message': 'PasswordChangeMessage',
        'minimum_password_length': 'MinimumPasswordLength',
        'password_history_count': 'PasswordHistoryCount',
        'password_minimum_age': 'PasswordMinimumAge',
        'password_expire_notification_days': 'PasswordExpireNotificationDays'
    }

    def __init__(self, extension_type=None, extension_identifier=None, type=None, realm=None, team_identifier=None, hosts=None, urls=None, custom_xml=None, certificate_uuid=None, certificate_name=None, use_site_auto_discovery=None, allow_automatic_login=None, require_user_touch_id_or_password=None, credential_bundle_ids=None, allow_password_change=None, sync_local_password=None, match_ad_password_complexity=None, password_change_message=None, minimum_password_length=None, password_history_count=None, password_minimum_age=None, password_expire_notification_days=None, _configuration=None):  # noqa: E501
        """MacOsSsoExtensionPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._extension_type = None
        self._extension_identifier = None
        self._type = None
        self._realm = None
        self._team_identifier = None
        self._hosts = None
        self._urls = None
        self._custom_xml = None
        self._certificate_uuid = None
        self._certificate_name = None
        self._use_site_auto_discovery = None
        self._allow_automatic_login = None
        self._require_user_touch_id_or_password = None
        self._credential_bundle_ids = None
        self._allow_password_change = None
        self._sync_local_password = None
        self._match_ad_password_complexity = None
        self._password_change_message = None
        self._minimum_password_length = None
        self._password_history_count = None
        self._password_minimum_age = None
        self._password_expire_notification_days = None
        self.discriminator = None

        if extension_type is not None:
            self.extension_type = extension_type
        if extension_identifier is not None:
            self.extension_identifier = extension_identifier
        if type is not None:
            self.type = type
        if realm is not None:
            self.realm = realm
        if team_identifier is not None:
            self.team_identifier = team_identifier
        if hosts is not None:
            self.hosts = hosts
        if urls is not None:
            self.urls = urls
        if custom_xml is not None:
            self.custom_xml = custom_xml
        if certificate_uuid is not None:
            self.certificate_uuid = certificate_uuid
        if certificate_name is not None:
            self.certificate_name = certificate_name
        if use_site_auto_discovery is not None:
            self.use_site_auto_discovery = use_site_auto_discovery
        if allow_automatic_login is not None:
            self.allow_automatic_login = allow_automatic_login
        if require_user_touch_id_or_password is not None:
            self.require_user_touch_id_or_password = require_user_touch_id_or_password
        if credential_bundle_ids is not None:
            self.credential_bundle_ids = credential_bundle_ids
        if allow_password_change is not None:
            self.allow_password_change = allow_password_change
        if sync_local_password is not None:
            self.sync_local_password = sync_local_password
        if match_ad_password_complexity is not None:
            self.match_ad_password_complexity = match_ad_password_complexity
        if password_change_message is not None:
            self.password_change_message = password_change_message
        if minimum_password_length is not None:
            self.minimum_password_length = minimum_password_length
        if password_history_count is not None:
            self.password_history_count = password_history_count
        if password_minimum_age is not None:
            self.password_minimum_age = password_minimum_age
        if password_expire_notification_days is not None:
            self.password_expire_notification_days = password_expire_notification_days

    @property
    def extension_type(self):
        """Gets the extension_type of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets extension type: Generic, Kerberos.  # noqa: E501

        :return: The extension_type of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._extension_type

    @extension_type.setter
    def extension_type(self, extension_type):
        """Sets the extension_type of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets extension type: Generic, Kerberos.  # noqa: E501

        :param extension_type: The extension_type of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._extension_type = extension_type

    @property
    def extension_identifier(self):
        """Gets the extension_identifier of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets application extension that performs single sign-on.  # noqa: E501

        :return: The extension_identifier of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._extension_identifier

    @extension_identifier.setter
    def extension_identifier(self, extension_identifier):
        """Sets the extension_identifier of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets application extension that performs single sign-on.  # noqa: E501

        :param extension_identifier: The extension_identifier of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._extension_identifier = extension_identifier

    @property
    def type(self):
        """Gets the type of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets single sign-on extension type.  # noqa: E501

        :return: The type of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets single sign-on extension type.  # noqa: E501

        :param type: The type of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def realm(self):
        """Gets the realm of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets realm name for SSO extension.  # noqa: E501

        :return: The realm of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets realm name for SSO extension.  # noqa: E501

        :param realm: The realm of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._realm = realm

    @property
    def team_identifier(self):
        """Gets the team_identifier of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets team identifier of the app extension.  # noqa: E501

        :return: The team_identifier of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._team_identifier

    @team_identifier.setter
    def team_identifier(self, team_identifier):
        """Sets the team_identifier of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets team identifier of the app extension.  # noqa: E501

        :param team_identifier: The team_identifier of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._team_identifier = team_identifier

    @property
    def hosts(self):
        """Gets the hosts of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets list of hosts for which the app extension performs single sign-on.  # noqa: E501

        :return: The hosts of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets list of hosts for which the app extension performs single sign-on.  # noqa: E501

        :param hosts: The hosts of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: list[str]
        """

        self._hosts = hosts

    @property
    def urls(self):
        """Gets the urls of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets list of URLs for which the app extension performs single sign-on.  # noqa: E501

        :return: The urls of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets list of URLs for which the app extension performs single sign-on.  # noqa: E501

        :param urls: The urls of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: list[str]
        """

        self._urls = urls

    @property
    def custom_xml(self):
        """Gets the custom_xml of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets custom XML for SSO extension data.  # noqa: E501

        :return: The custom_xml of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._custom_xml

    @custom_xml.setter
    def custom_xml(self, custom_xml):
        """Sets the custom_xml of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets custom XML for SSO extension data.  # noqa: E501

        :param custom_xml: The custom_xml of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._custom_xml = custom_xml

    @property
    def certificate_uuid(self):
        """Gets the certificate_uuid of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets certificate UUID for SSO extension data.  # noqa: E501

        :return: The certificate_uuid of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._certificate_uuid

    @certificate_uuid.setter
    def certificate_uuid(self, certificate_uuid):
        """Sets the certificate_uuid of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets certificate UUID for SSO extension data.  # noqa: E501

        :param certificate_uuid: The certificate_uuid of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._certificate_uuid = certificate_uuid

    @property
    def certificate_name(self):
        """Gets the certificate_name of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets certificate name for SSO extension data.  # noqa: E501

        :return: The certificate_name of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """Sets the certificate_name of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets certificate name for SSO extension data.  # noqa: E501

        :param certificate_name: The certificate_name of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._certificate_name = certificate_name

    @property
    def use_site_auto_discovery(self):
        """Gets the use_site_auto_discovery of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether use site auto discovery flag for kerberos single sign-on.  # noqa: E501

        :return: The use_site_auto_discovery of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._use_site_auto_discovery

    @use_site_auto_discovery.setter
    def use_site_auto_discovery(self, use_site_auto_discovery):
        """Sets the use_site_auto_discovery of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets a value indicating whether use site auto discovery flag for kerberos single sign-on.  # noqa: E501

        :param use_site_auto_discovery: The use_site_auto_discovery of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._use_site_auto_discovery = use_site_auto_discovery

    @property
    def allow_automatic_login(self):
        """Gets the allow_automatic_login of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether allow automatic login flag for kerberos single sign-on.  # noqa: E501

        :return: The allow_automatic_login of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_automatic_login

    @allow_automatic_login.setter
    def allow_automatic_login(self, allow_automatic_login):
        """Sets the allow_automatic_login of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets a value indicating whether allow automatic login flag for kerberos single sign-on.  # noqa: E501

        :param allow_automatic_login: The allow_automatic_login of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_automatic_login = allow_automatic_login

    @property
    def require_user_touch_id_or_password(self):
        """Gets the require_user_touch_id_or_password of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether require user presence flag for kerberos single sign-on.  # noqa: E501

        :return: The require_user_touch_id_or_password of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._require_user_touch_id_or_password

    @require_user_touch_id_or_password.setter
    def require_user_touch_id_or_password(self, require_user_touch_id_or_password):
        """Sets the require_user_touch_id_or_password of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets a value indicating whether require user presence flag for kerberos single sign-on.  # noqa: E501

        :param require_user_touch_id_or_password: The require_user_touch_id_or_password of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._require_user_touch_id_or_password = require_user_touch_id_or_password

    @property
    def credential_bundle_ids(self):
        """Gets the credential_bundle_ids of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets list of allowed bundle ids for kerberos single sign-on.  # noqa: E501

        :return: The credential_bundle_ids of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: list[str]
        """
        return self._credential_bundle_ids

    @credential_bundle_ids.setter
    def credential_bundle_ids(self, credential_bundle_ids):
        """Sets the credential_bundle_ids of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets list of allowed bundle ids for kerberos single sign-on.  # noqa: E501

        :param credential_bundle_ids: The credential_bundle_ids of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: list[str]
        """

        self._credential_bundle_ids = credential_bundle_ids

    @property
    def allow_password_change(self):
        """Gets the allow_password_change of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether allow password change flag for kerberos single sign-on.  # noqa: E501

        :return: The allow_password_change of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_password_change

    @allow_password_change.setter
    def allow_password_change(self, allow_password_change):
        """Sets the allow_password_change of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets a value indicating whether allow password change flag for kerberos single sign-on.  # noqa: E501

        :param allow_password_change: The allow_password_change of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_password_change = allow_password_change

    @property
    def sync_local_password(self):
        """Gets the sync_local_password of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether sync local password flag for kerberos single sign-on.  # noqa: E501

        :return: The sync_local_password of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._sync_local_password

    @sync_local_password.setter
    def sync_local_password(self, sync_local_password):
        """Sets the sync_local_password of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets a value indicating whether sync local password flag for kerberos single sign-on.  # noqa: E501

        :param sync_local_password: The sync_local_password of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._sync_local_password = sync_local_password

    @property
    def match_ad_password_complexity(self):
        """Gets the match_ad_password_complexity of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether match active directory password complexity flag for kerberos single sign-on.  # noqa: E501

        :return: The match_ad_password_complexity of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._match_ad_password_complexity

    @match_ad_password_complexity.setter
    def match_ad_password_complexity(self, match_ad_password_complexity):
        """Sets the match_ad_password_complexity of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets a value indicating whether match active directory password complexity flag for kerberos single sign-on.  # noqa: E501

        :param match_ad_password_complexity: The match_ad_password_complexity of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._match_ad_password_complexity = match_ad_password_complexity

    @property
    def password_change_message(self):
        """Gets the password_change_message of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets password change message for kerberos single sign-on.  # noqa: E501

        :return: The password_change_message of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._password_change_message

    @password_change_message.setter
    def password_change_message(self, password_change_message):
        """Sets the password_change_message of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets password change message for kerberos single sign-on.  # noqa: E501

        :param password_change_message: The password_change_message of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._password_change_message = password_change_message

    @property
    def minimum_password_length(self):
        """Gets the minimum_password_length of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets minimum password length of characters for kerberos single sign-on.  # noqa: E501

        :return: The minimum_password_length of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._minimum_password_length

    @minimum_password_length.setter
    def minimum_password_length(self, minimum_password_length):
        """Sets the minimum_password_length of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets minimum password length of characters for kerberos single sign-on.  # noqa: E501

        :param minimum_password_length: The minimum_password_length of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._minimum_password_length = minimum_password_length

    @property
    def password_history_count(self):
        """Gets the password_history_count of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets password history count for kerberos single sign-on.  # noqa: E501

        :return: The password_history_count of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._password_history_count

    @password_history_count.setter
    def password_history_count(self, password_history_count):
        """Sets the password_history_count of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets password history count for kerberos single sign-on.  # noqa: E501

        :param password_history_count: The password_history_count of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._password_history_count = password_history_count

    @property
    def password_minimum_age(self):
        """Gets the password_minimum_age of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets password minimum age days for kerberos single sign-on.  # noqa: E501

        :return: The password_minimum_age of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._password_minimum_age

    @password_minimum_age.setter
    def password_minimum_age(self, password_minimum_age):
        """Sets the password_minimum_age of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets password minimum age days for kerberos single sign-on.  # noqa: E501

        :param password_minimum_age: The password_minimum_age of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._password_minimum_age = password_minimum_age

    @property
    def password_expire_notification_days(self):
        """Gets the password_expire_notification_days of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501

        Gets or sets password expire notification days for kerberos single sign-on.  # noqa: E501

        :return: The password_expire_notification_days of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._password_expire_notification_days

    @password_expire_notification_days.setter
    def password_expire_notification_days(self, password_expire_notification_days):
        """Sets the password_expire_notification_days of this MacOsSsoExtensionPayloadV2Entity.

        Gets or sets password expire notification days for kerberos single sign-on.  # noqa: E501

        :param password_expire_notification_days: The password_expire_notification_days of this MacOsSsoExtensionPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._password_expire_notification_days = password_expire_notification_days

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
        if issubclass(MacOsSsoExtensionPayloadV2Entity, dict):
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
        if not isinstance(other, MacOsSsoExtensionPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MacOsSsoExtensionPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
