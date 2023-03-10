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


class AppleOsXEasNativeMailClientPayloadEntity_(object):
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
        'account_name': 'str',
        'user_name': 'str',
        'email_address': 'str',
        'password': 'str',
        'payload_certificate': 'str',
        'internal_exchange_host': 'str',
        'internall_port': 'str',
        'internal_server_path': 'str',
        'use_ssl_for_internal_exchange_host': 'bool',
        'external_exchange_host': 'str',
        'external_port': 'str',
        'external_server_path': 'str',
        'use_ssl_for_external_exchange_host': 'bool'
    }

    attribute_map = {
        'account_name': 'AccountName',
        'user_name': 'UserName',
        'email_address': 'EmailAddress',
        'password': 'Password',
        'payload_certificate': 'PayloadCertificate',
        'internal_exchange_host': 'InternalExchangeHost',
        'internall_port': 'InternallPort',
        'internal_server_path': 'InternalServerPath',
        'use_ssl_for_internal_exchange_host': 'UseSslForInternalExchangeHost',
        'external_exchange_host': 'ExternalExchangeHost',
        'external_port': 'ExternalPort',
        'external_server_path': 'ExternalServerPath',
        'use_ssl_for_external_exchange_host': 'UseSslForExternalExchangeHost'
    }

    def __init__(self, account_name=None, user_name=None, email_address=None, password=None, payload_certificate=None, internal_exchange_host=None, internall_port=None, internal_server_path=None, use_ssl_for_internal_exchange_host=None, external_exchange_host=None, external_port=None, external_server_path=None, use_ssl_for_external_exchange_host=None, _configuration=None):  # noqa: E501
        """AppleOsXEasNativeMailClientPayloadEntity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_name = None
        self._user_name = None
        self._email_address = None
        self._password = None
        self._payload_certificate = None
        self._internal_exchange_host = None
        self._internall_port = None
        self._internal_server_path = None
        self._use_ssl_for_internal_exchange_host = None
        self._external_exchange_host = None
        self._external_port = None
        self._external_server_path = None
        self._use_ssl_for_external_exchange_host = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if user_name is not None:
            self.user_name = user_name
        if email_address is not None:
            self.email_address = email_address
        if password is not None:
            self.password = password
        if payload_certificate is not None:
            self.payload_certificate = payload_certificate
        if internal_exchange_host is not None:
            self.internal_exchange_host = internal_exchange_host
        if internall_port is not None:
            self.internall_port = internall_port
        if internal_server_path is not None:
            self.internal_server_path = internal_server_path
        if use_ssl_for_internal_exchange_host is not None:
            self.use_ssl_for_internal_exchange_host = use_ssl_for_internal_exchange_host
        if external_exchange_host is not None:
            self.external_exchange_host = external_exchange_host
        if external_port is not None:
            self.external_port = external_port
        if external_server_path is not None:
            self.external_server_path = external_server_path
        if use_ssl_for_external_exchange_host is not None:
            self.use_ssl_for_external_exchange_host = use_ssl_for_external_exchange_host

    @property
    def account_name(self):
        """Gets the account_name of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets name of the account.  # noqa: E501

        :return: The account_name of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets name of the account.  # noqa: E501

        :param account_name: The account_name of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def user_name(self):
        """Gets the user_name of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets username for the account.  # noqa: E501

        :return: The user_name of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets username for the account.  # noqa: E501

        :param user_name: The user_name of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def email_address(self):
        """Gets the email_address of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets user's email address.  # noqa: E501

        :return: The email_address of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets user's email address.  # noqa: E501

        :param email_address: The email_address of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def password(self):
        """Gets the password of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets email account's password.  # noqa: E501

        :return: The password of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets email account's password.  # noqa: E501

        :param password: The password of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def payload_certificate(self):
        """Gets the payload_certificate of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets name of the Payload certificate.  # noqa: E501

        :return: The payload_certificate of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._payload_certificate

    @payload_certificate.setter
    def payload_certificate(self, payload_certificate):
        """Sets the payload_certificate of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets name of the Payload certificate.  # noqa: E501

        :param payload_certificate: The payload_certificate of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: str
        """

        self._payload_certificate = payload_certificate

    @property
    def internal_exchange_host(self):
        """Gets the internal_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets the name(or IP address) of the secure server for EAS use.  # noqa: E501

        :return: The internal_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._internal_exchange_host

    @internal_exchange_host.setter
    def internal_exchange_host(self, internal_exchange_host):
        """Sets the internal_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets the name(or IP address) of the secure server for EAS use.  # noqa: E501

        :param internal_exchange_host: The internal_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: str
        """

        self._internal_exchange_host = internal_exchange_host

    @property
    def internall_port(self):
        """Gets the internall_port of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets the port number assigned for communication with the internal Exchange host.  # noqa: E501

        :return: The internall_port of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._internall_port

    @internall_port.setter
    def internall_port(self, internall_port):
        """Sets the internall_port of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets the port number assigned for communication with the internal Exchange host.  # noqa: E501

        :param internall_port: The internall_port of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: str
        """

        self._internall_port = internall_port

    @property
    def internal_server_path(self):
        """Gets the internal_server_path of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets the location of the secure server for EAS use.  # noqa: E501

        :return: The internal_server_path of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._internal_server_path

    @internal_server_path.setter
    def internal_server_path(self, internal_server_path):
        """Sets the internal_server_path of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets the location of the secure server for EAS use.  # noqa: E501

        :param internal_server_path: The internal_server_path of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: str
        """

        self._internal_server_path = internal_server_path

    @property
    def use_ssl_for_internal_exchange_host(self):
        """Gets the use_ssl_for_internal_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to true, uses SSL for the internal Exchange host.  # noqa: E501

        :return: The use_ssl_for_internal_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl_for_internal_exchange_host

    @use_ssl_for_internal_exchange_host.setter
    def use_ssl_for_internal_exchange_host(self, use_ssl_for_internal_exchange_host):
        """Sets the use_ssl_for_internal_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets a value indicating whether if set to true, uses SSL for the internal Exchange host.  # noqa: E501

        :param use_ssl_for_internal_exchange_host: The use_ssl_for_internal_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._use_ssl_for_internal_exchange_host = use_ssl_for_internal_exchange_host

    @property
    def external_exchange_host(self):
        """Gets the external_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets specifies the Exchange server host name(or IP address).  # noqa: E501

        :return: The external_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._external_exchange_host

    @external_exchange_host.setter
    def external_exchange_host(self, external_exchange_host):
        """Sets the external_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets specifies the Exchange server host name(or IP address).  # noqa: E501

        :param external_exchange_host: The external_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: str
        """

        self._external_exchange_host = external_exchange_host

    @property
    def external_port(self):
        """Gets the external_port of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets the port number assigned for communication with the external Exchange host.  # noqa: E501

        :return: The external_port of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._external_port

    @external_port.setter
    def external_port(self, external_port):
        """Sets the external_port of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets the port number assigned for communication with the external Exchange host.  # noqa: E501

        :param external_port: The external_port of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: str
        """

        self._external_port = external_port

    @property
    def external_server_path(self):
        """Gets the external_server_path of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets the location of the external server for EAS use.  # noqa: E501

        :return: The external_server_path of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: str
        """
        return self._external_server_path

    @external_server_path.setter
    def external_server_path(self, external_server_path):
        """Sets the external_server_path of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets the location of the external server for EAS use.  # noqa: E501

        :param external_server_path: The external_server_path of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: str
        """

        self._external_server_path = external_server_path

    @property
    def use_ssl_for_external_exchange_host(self):
        """Gets the use_ssl_for_external_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether if set to true, uses SSL for the external Exchange host.  # noqa: E501

        :return: The use_ssl_for_external_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl_for_external_exchange_host

    @use_ssl_for_external_exchange_host.setter
    def use_ssl_for_external_exchange_host(self, use_ssl_for_external_exchange_host):
        """Sets the use_ssl_for_external_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.

        Gets or sets a value indicating whether if set to true, uses SSL for the external Exchange host.  # noqa: E501

        :param use_ssl_for_external_exchange_host: The use_ssl_for_external_exchange_host of this AppleOsXEasNativeMailClientPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._use_ssl_for_external_exchange_host = use_ssl_for_external_exchange_host

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
        if issubclass(AppleOsXEasNativeMailClientPayloadEntity_, dict):
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
        if not isinstance(other, AppleOsXEasNativeMailClientPayloadEntity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleOsXEasNativeMailClientPayloadEntity_):
            return True

        return self.to_dict() != other.to_dict()
