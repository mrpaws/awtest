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


class AndroidConatinerVPNPulseSecureSettings(object):
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
        'proxy_type': 'int',
        'server': 'str',
        'port': 'str',
        'proxy_user_name': 'str',
        'proxy_password': 'str',
        'pac_url': 'str'
    }

    attribute_map = {
        'proxy_type': 'ProxyType',
        'server': 'Server',
        'port': 'Port',
        'proxy_user_name': 'ProxyUserName',
        'proxy_password': 'ProxyPassword',
        'pac_url': 'PacUrl'
    }

    def __init__(self, proxy_type=None, server=None, port=None, proxy_user_name=None, proxy_password=None, pac_url=None, _configuration=None):  # noqa: E501
        """AndroidConatinerVPNPulseSecureSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._proxy_type = None
        self._server = None
        self._port = None
        self._proxy_user_name = None
        self._proxy_password = None
        self._pac_url = None
        self.discriminator = None

        if proxy_type is not None:
            self.proxy_type = proxy_type
        if server is not None:
            self.server = server
        if port is not None:
            self.port = port
        if proxy_user_name is not None:
            self.proxy_user_name = proxy_user_name
        if proxy_password is not None:
            self.proxy_password = proxy_password
        if pac_url is not None:
            self.pac_url = pac_url

    @property
    def proxy_type(self):
        """Gets the proxy_type of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501

        Gets or sets the proxy.  # noqa: E501

        :return: The proxy_type of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :rtype: int
        """
        return self._proxy_type

    @proxy_type.setter
    def proxy_type(self, proxy_type):
        """Sets the proxy_type of this AndroidConatinerVPNPulseSecureSettings.

        Gets or sets the proxy.  # noqa: E501

        :param proxy_type: The proxy_type of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :type: int
        """

        self._proxy_type = proxy_type

    @property
    def server(self):
        """Gets the server of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501

        Gets or sets the proxy server.  # noqa: E501

        :return: The server of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this AndroidConatinerVPNPulseSecureSettings.

        Gets or sets the proxy server.  # noqa: E501

        :param server: The server of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def port(self):
        """Gets the port of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501

        Gets or sets the proxy port.  # noqa: E501

        :return: The port of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AndroidConatinerVPNPulseSecureSettings.

        Gets or sets the proxy port.  # noqa: E501

        :param port: The port of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def proxy_user_name(self):
        """Gets the proxy_user_name of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501

        Gets or sets the proxy username.  # noqa: E501

        :return: The proxy_user_name of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :rtype: str
        """
        return self._proxy_user_name

    @proxy_user_name.setter
    def proxy_user_name(self, proxy_user_name):
        """Sets the proxy_user_name of this AndroidConatinerVPNPulseSecureSettings.

        Gets or sets the proxy username.  # noqa: E501

        :param proxy_user_name: The proxy_user_name of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :type: str
        """

        self._proxy_user_name = proxy_user_name

    @property
    def proxy_password(self):
        """Gets the proxy_password of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501

        Gets or sets the proxy password.  # noqa: E501

        :return: The proxy_password of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :rtype: str
        """
        return self._proxy_password

    @proxy_password.setter
    def proxy_password(self, proxy_password):
        """Sets the proxy_password of this AndroidConatinerVPNPulseSecureSettings.

        Gets or sets the proxy password.  # noqa: E501

        :param proxy_password: The proxy_password of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :type: str
        """

        self._proxy_password = proxy_password

    @property
    def pac_url(self):
        """Gets the pac_url of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501

        Gets or sets the proxy pacurl.  # noqa: E501

        :return: The pac_url of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :rtype: str
        """
        return self._pac_url

    @pac_url.setter
    def pac_url(self, pac_url):
        """Sets the pac_url of this AndroidConatinerVPNPulseSecureSettings.

        Gets or sets the proxy pacurl.  # noqa: E501

        :param pac_url: The pac_url of this AndroidConatinerVPNPulseSecureSettings.  # noqa: E501
        :type: str
        """

        self._pac_url = pac_url

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
        if issubclass(AndroidConatinerVPNPulseSecureSettings, dict):
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
        if not isinstance(other, AndroidConatinerVPNPulseSecureSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidConatinerVPNPulseSecureSettings):
            return True

        return self.to_dict() != other.to_dict()