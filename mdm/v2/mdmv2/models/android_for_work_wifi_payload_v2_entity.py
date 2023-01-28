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


class AndroidForWorkWifiPayloadV2Entity(object):
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
        'service_set_identifier': 'str',
        'security_type': 'str',
        'password': 'str',
        'set_as_active_network': 'bool',
        'hidden_network': 'bool',
        'use_two_factor_authentication': 'bool',
        'sfa_type': 'str',
        'tfa_type': 'str',
        'identity': 'str',
        'anonymous_identity': 'str',
        'enterprise_username': 'str',
        'enterprise_password': 'str',
        'payload_certificate_name': 'str',
        'ca_payload_certificate_name': 'str',
        'proxy_pac_url': 'str',
        'proxy_address': 'str',
        'proxy_port': 'int',
        'proxy_bypass': 'list[str]'
    }

    attribute_map = {
        'service_set_identifier': 'ServiceSetIdentifier',
        'security_type': 'SecurityType',
        'password': 'Password',
        'set_as_active_network': 'SetAsActiveNetwork',
        'hidden_network': 'HiddenNetwork',
        'use_two_factor_authentication': 'UseTwoFactorAuthentication',
        'sfa_type': 'SFAType',
        'tfa_type': 'TFAType',
        'identity': 'Identity',
        'anonymous_identity': 'AnonymousIdentity',
        'enterprise_username': 'EnterpriseUsername',
        'enterprise_password': 'EnterprisePassword',
        'payload_certificate_name': 'PayloadCertificateName',
        'ca_payload_certificate_name': 'CAPayloadCertificateName',
        'proxy_pac_url': 'ProxyPacUrl',
        'proxy_address': 'ProxyAddress',
        'proxy_port': 'ProxyPort',
        'proxy_bypass': 'ProxyBypass'
    }

    def __init__(self, service_set_identifier=None, security_type=None, password=None, set_as_active_network=None, hidden_network=None, use_two_factor_authentication=None, sfa_type=None, tfa_type=None, identity=None, anonymous_identity=None, enterprise_username=None, enterprise_password=None, payload_certificate_name=None, ca_payload_certificate_name=None, proxy_pac_url=None, proxy_address=None, proxy_port=None, proxy_bypass=None, _configuration=None):  # noqa: E501
        """AndroidForWorkWifiPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._service_set_identifier = None
        self._security_type = None
        self._password = None
        self._set_as_active_network = None
        self._hidden_network = None
        self._use_two_factor_authentication = None
        self._sfa_type = None
        self._tfa_type = None
        self._identity = None
        self._anonymous_identity = None
        self._enterprise_username = None
        self._enterprise_password = None
        self._payload_certificate_name = None
        self._ca_payload_certificate_name = None
        self._proxy_pac_url = None
        self._proxy_address = None
        self._proxy_port = None
        self._proxy_bypass = None
        self.discriminator = None

        if service_set_identifier is not None:
            self.service_set_identifier = service_set_identifier
        if security_type is not None:
            self.security_type = security_type
        if password is not None:
            self.password = password
        if set_as_active_network is not None:
            self.set_as_active_network = set_as_active_network
        if hidden_network is not None:
            self.hidden_network = hidden_network
        if use_two_factor_authentication is not None:
            self.use_two_factor_authentication = use_two_factor_authentication
        if sfa_type is not None:
            self.sfa_type = sfa_type
        if tfa_type is not None:
            self.tfa_type = tfa_type
        if identity is not None:
            self.identity = identity
        if anonymous_identity is not None:
            self.anonymous_identity = anonymous_identity
        if enterprise_username is not None:
            self.enterprise_username = enterprise_username
        if enterprise_password is not None:
            self.enterprise_password = enterprise_password
        if payload_certificate_name is not None:
            self.payload_certificate_name = payload_certificate_name
        if ca_payload_certificate_name is not None:
            self.ca_payload_certificate_name = ca_payload_certificate_name
        if proxy_pac_url is not None:
            self.proxy_pac_url = proxy_pac_url
        if proxy_address is not None:
            self.proxy_address = proxy_address
        if proxy_port is not None:
            self.proxy_port = proxy_port
        if proxy_bypass is not None:
            self.proxy_bypass = proxy_bypass

    @property
    def service_set_identifier(self):
        """Gets the service_set_identifier of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets SSID_STR.  # noqa: E501

        :return: The service_set_identifier of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._service_set_identifier

    @service_set_identifier.setter
    def service_set_identifier(self, service_set_identifier):
        """Sets the service_set_identifier of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets SSID_STR.  # noqa: E501

        :param service_set_identifier: The service_set_identifier of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._service_set_identifier = service_set_identifier

    @property
    def security_type(self):
        """Gets the security_type of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets EncryptionType.  # noqa: E501

        :return: The security_type of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._security_type

    @security_type.setter
    def security_type(self, security_type):
        """Sets the security_type of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets EncryptionType.  # noqa: E501

        :param security_type: The security_type of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._security_type = security_type

    @property
    def password(self):
        """Gets the password of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets Password.  # noqa: E501

        :return: The password of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets Password.  # noqa: E501

        :param password: The password of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def set_as_active_network(self):
        """Gets the set_as_active_network of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets MakeActive.  # noqa: E501

        :return: The set_as_active_network of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._set_as_active_network

    @set_as_active_network.setter
    def set_as_active_network(self, set_as_active_network):
        """Sets the set_as_active_network of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets MakeActive.  # noqa: E501

        :param set_as_active_network: The set_as_active_network of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._set_as_active_network = set_as_active_network

    @property
    def hidden_network(self):
        """Gets the hidden_network of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets IsHidden.  # noqa: E501

        :return: The hidden_network of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._hidden_network

    @hidden_network.setter
    def hidden_network(self, hidden_network):
        """Sets the hidden_network of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets IsHidden.  # noqa: E501

        :param hidden_network: The hidden_network of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._hidden_network = hidden_network

    @property
    def use_two_factor_authentication(self):
        """Gets the use_two_factor_authentication of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets UseTwoFactorAuthentication.  # noqa: E501

        :return: The use_two_factor_authentication of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._use_two_factor_authentication

    @use_two_factor_authentication.setter
    def use_two_factor_authentication(self, use_two_factor_authentication):
        """Sets the use_two_factor_authentication of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets UseTwoFactorAuthentication.  # noqa: E501

        :param use_two_factor_authentication: The use_two_factor_authentication of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._use_two_factor_authentication = use_two_factor_authentication

    @property
    def sfa_type(self):
        """Gets the sfa_type of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets EAP.  # noqa: E501

        :return: The sfa_type of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._sfa_type

    @sfa_type.setter
    def sfa_type(self, sfa_type):
        """Sets the sfa_type of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets EAP.  # noqa: E501

        :param sfa_type: The sfa_type of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._sfa_type = sfa_type

    @property
    def tfa_type(self):
        """Gets the tfa_type of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets SecondPhaseAuth.  # noqa: E501

        :return: The tfa_type of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._tfa_type

    @tfa_type.setter
    def tfa_type(self, tfa_type):
        """Sets the tfa_type of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets SecondPhaseAuth.  # noqa: E501

        :param tfa_type: The tfa_type of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._tfa_type = tfa_type

    @property
    def identity(self):
        """Gets the identity of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets Identity.  # noqa: E501

        :return: The identity of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets Identity.  # noqa: E501

        :param identity: The identity of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def anonymous_identity(self):
        """Gets the anonymous_identity of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets AnonymousIdentity.  # noqa: E501

        :return: The anonymous_identity of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._anonymous_identity

    @anonymous_identity.setter
    def anonymous_identity(self, anonymous_identity):
        """Sets the anonymous_identity of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets AnonymousIdentity.  # noqa: E501

        :param anonymous_identity: The anonymous_identity of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._anonymous_identity = anonymous_identity

    @property
    def enterprise_username(self):
        """Gets the enterprise_username of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets EnterpriseUsername.  # noqa: E501

        :return: The enterprise_username of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._enterprise_username

    @enterprise_username.setter
    def enterprise_username(self, enterprise_username):
        """Sets the enterprise_username of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets EnterpriseUsername.  # noqa: E501

        :param enterprise_username: The enterprise_username of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._enterprise_username = enterprise_username

    @property
    def enterprise_password(self):
        """Gets the enterprise_password of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets EnterprisePassword.  # noqa: E501

        :return: The enterprise_password of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._enterprise_password

    @enterprise_password.setter
    def enterprise_password(self, enterprise_password):
        """Sets the enterprise_password of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets EnterprisePassword.  # noqa: E501

        :param enterprise_password: The enterprise_password of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._enterprise_password = enterprise_password

    @property
    def payload_certificate_name(self):
        """Gets the payload_certificate_name of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets payloadCertificateName is used to find corresponding certificate in the AndroidForWorkCredentials payload.  # noqa: E501

        :return: The payload_certificate_name of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._payload_certificate_name

    @payload_certificate_name.setter
    def payload_certificate_name(self, payload_certificate_name):
        """Sets the payload_certificate_name of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets payloadCertificateName is used to find corresponding certificate in the AndroidForWorkCredentials payload.  # noqa: E501

        :param payload_certificate_name: The payload_certificate_name of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._payload_certificate_name = payload_certificate_name

    @property
    def ca_payload_certificate_name(self):
        """Gets the ca_payload_certificate_name of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets cAPayloadCertificateName is used to find corresponding certificate in the AndroidForWorkCredentials payload.  That is used to store CAPayloadCertificateUUID in the DB.  # noqa: E501

        :return: The ca_payload_certificate_name of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._ca_payload_certificate_name

    @ca_payload_certificate_name.setter
    def ca_payload_certificate_name(self, ca_payload_certificate_name):
        """Sets the ca_payload_certificate_name of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets cAPayloadCertificateName is used to find corresponding certificate in the AndroidForWorkCredentials payload.  That is used to store CAPayloadCertificateUUID in the DB.  # noqa: E501

        :param ca_payload_certificate_name: The ca_payload_certificate_name of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._ca_payload_certificate_name = ca_payload_certificate_name

    @property
    def proxy_pac_url(self):
        """Gets the proxy_pac_url of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets ProxyPacUrl.  # noqa: E501

        :return: The proxy_pac_url of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._proxy_pac_url

    @proxy_pac_url.setter
    def proxy_pac_url(self, proxy_pac_url):
        """Sets the proxy_pac_url of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets ProxyPacUrl.  # noqa: E501

        :param proxy_pac_url: The proxy_pac_url of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._proxy_pac_url = proxy_pac_url

    @property
    def proxy_address(self):
        """Gets the proxy_address of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets ProxyServer.  # noqa: E501

        :return: The proxy_address of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._proxy_address

    @proxy_address.setter
    def proxy_address(self, proxy_address):
        """Sets the proxy_address of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets ProxyServer.  # noqa: E501

        :param proxy_address: The proxy_address of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._proxy_address = proxy_address

    @property
    def proxy_port(self):
        """Gets the proxy_port of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets ProxyMode.  # noqa: E501

        :return: The proxy_port of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, proxy_port):
        """Sets the proxy_port of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets ProxyMode.  # noqa: E501

        :param proxy_port: The proxy_port of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._proxy_port = proxy_port

    @property
    def proxy_bypass(self):
        """Gets the proxy_bypass of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501

        Gets or sets ProxyBypass List.  # noqa: E501

        :return: The proxy_bypass of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :rtype: list[str]
        """
        return self._proxy_bypass

    @proxy_bypass.setter
    def proxy_bypass(self, proxy_bypass):
        """Sets the proxy_bypass of this AndroidForWorkWifiPayloadV2Entity.

        Gets or sets ProxyBypass List.  # noqa: E501

        :param proxy_bypass: The proxy_bypass of this AndroidForWorkWifiPayloadV2Entity.  # noqa: E501
        :type: list[str]
        """

        self._proxy_bypass = proxy_bypass

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
        if issubclass(AndroidForWorkWifiPayloadV2Entity, dict):
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
        if not isinstance(other, AndroidForWorkWifiPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkWifiPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()