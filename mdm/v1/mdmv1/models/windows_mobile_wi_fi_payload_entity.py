# coding: utf-8

"""
    MDM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv1.configuration import Configuration


class WindowsMobileWiFiPayloadEntity(object):
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
        'motorola_adapter_type': 'str',
        'service_set_identifier': 'str',
        'user_name': 'str',
        'password': 'str',
        'server_certificate': 'str',
        'security_type': 'str',
        'pre_shared_key': 'str'
    }

    attribute_map = {
        'motorola_adapter_type': 'MotorolaAdapterType',
        'service_set_identifier': 'ServiceSetIdentifier',
        'user_name': 'UserName',
        'password': 'Password',
        'server_certificate': 'ServerCertificate',
        'security_type': 'SecurityType',
        'pre_shared_key': 'PreSharedKey'
    }

    def __init__(self, motorola_adapter_type=None, service_set_identifier=None, user_name=None, password=None, server_certificate=None, security_type=None, pre_shared_key=None, _configuration=None):  # noqa: E501
        """WindowsMobileWiFiPayloadEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._motorola_adapter_type = None
        self._service_set_identifier = None
        self._user_name = None
        self._password = None
        self._server_certificate = None
        self._security_type = None
        self._pre_shared_key = None
        self.discriminator = None

        if motorola_adapter_type is not None:
            self.motorola_adapter_type = motorola_adapter_type
        if service_set_identifier is not None:
            self.service_set_identifier = service_set_identifier
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
        if server_certificate is not None:
            self.server_certificate = server_certificate
        if security_type is not None:
            self.security_type = security_type
        if pre_shared_key is not None:
            self.pre_shared_key = pre_shared_key

    @property
    def motorola_adapter_type(self):
        """Gets the motorola_adapter_type of this WindowsMobileWiFiPayloadEntity.  # noqa: E501

        Gets or sets motorola Adapter Type to be used for the connection.  # noqa: E501

        :return: The motorola_adapter_type of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :rtype: str
        """
        return self._motorola_adapter_type

    @motorola_adapter_type.setter
    def motorola_adapter_type(self, motorola_adapter_type):
        """Sets the motorola_adapter_type of this WindowsMobileWiFiPayloadEntity.

        Gets or sets motorola Adapter Type to be used for the connection.  # noqa: E501

        :param motorola_adapter_type: The motorola_adapter_type of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :type: str
        """

        self._motorola_adapter_type = motorola_adapter_type

    @property
    def service_set_identifier(self):
        """Gets the service_set_identifier of this WindowsMobileWiFiPayloadEntity.  # noqa: E501

        Gets or sets serviceSetIdentifier.  # noqa: E501

        :return: The service_set_identifier of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :rtype: str
        """
        return self._service_set_identifier

    @service_set_identifier.setter
    def service_set_identifier(self, service_set_identifier):
        """Sets the service_set_identifier of this WindowsMobileWiFiPayloadEntity.

        Gets or sets serviceSetIdentifier.  # noqa: E501

        :param service_set_identifier: The service_set_identifier of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :type: str
        """

        self._service_set_identifier = service_set_identifier

    @property
    def user_name(self):
        """Gets the user_name of this WindowsMobileWiFiPayloadEntity.  # noqa: E501

        Gets or sets userName for network connection.  # noqa: E501

        :return: The user_name of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this WindowsMobileWiFiPayloadEntity.

        Gets or sets userName for network connection.  # noqa: E501

        :param user_name: The user_name of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this WindowsMobileWiFiPayloadEntity.  # noqa: E501

        Gets or sets password for network connection.  # noqa: E501

        :return: The password of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this WindowsMobileWiFiPayloadEntity.

        Gets or sets password for network connection.  # noqa: E501

        :param password: The password of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def server_certificate(self):
        """Gets the server_certificate of this WindowsMobileWiFiPayloadEntity.  # noqa: E501

        Gets or sets name of the server certificate.  # noqa: E501

        :return: The server_certificate of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :rtype: str
        """
        return self._server_certificate

    @server_certificate.setter
    def server_certificate(self, server_certificate):
        """Sets the server_certificate of this WindowsMobileWiFiPayloadEntity.

        Gets or sets name of the server certificate.  # noqa: E501

        :param server_certificate: The server_certificate of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :type: str
        """

        self._server_certificate = server_certificate

    @property
    def security_type(self):
        """Gets the security_type of this WindowsMobileWiFiPayloadEntity.  # noqa: E501

        Gets or sets security type used for the network connection.  # noqa: E501

        :return: The security_type of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :rtype: str
        """
        return self._security_type

    @security_type.setter
    def security_type(self, security_type):
        """Sets the security_type of this WindowsMobileWiFiPayloadEntity.

        Gets or sets security type used for the network connection.  # noqa: E501

        :param security_type: The security_type of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :type: str
        """

        self._security_type = security_type

    @property
    def pre_shared_key(self):
        """Gets the pre_shared_key of this WindowsMobileWiFiPayloadEntity.  # noqa: E501

        Gets or sets preShared network key.  # noqa: E501

        :return: The pre_shared_key of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :rtype: str
        """
        return self._pre_shared_key

    @pre_shared_key.setter
    def pre_shared_key(self, pre_shared_key):
        """Sets the pre_shared_key of this WindowsMobileWiFiPayloadEntity.

        Gets or sets preShared network key.  # noqa: E501

        :param pre_shared_key: The pre_shared_key of this WindowsMobileWiFiPayloadEntity.  # noqa: E501
        :type: str
        """

        self._pre_shared_key = pre_shared_key

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
        if issubclass(WindowsMobileWiFiPayloadEntity, dict):
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
        if not isinstance(other, WindowsMobileWiFiPayloadEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WindowsMobileWiFiPayloadEntity):
            return True

        return self.to_dict() != other.to_dict()