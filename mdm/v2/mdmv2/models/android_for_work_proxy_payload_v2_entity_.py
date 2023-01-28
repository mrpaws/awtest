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


class AndroidForWorkProxyPayloadV2Entity_(object):
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
        'proxy_mode': 'str',
        'proxy_pac_url': 'str',
        'proxy_server': 'str',
        'proxy_bypass_list': 'list[str]'
    }

    attribute_map = {
        'proxy_mode': 'ProxyMode',
        'proxy_pac_url': 'ProxyPacUrl',
        'proxy_server': 'ProxyServer',
        'proxy_bypass_list': 'ProxyBypassList'
    }

    def __init__(self, proxy_mode=None, proxy_pac_url=None, proxy_server=None, proxy_bypass_list=None, _configuration=None):  # noqa: E501
        """AndroidForWorkProxyPayloadV2Entity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._proxy_mode = None
        self._proxy_pac_url = None
        self._proxy_server = None
        self._proxy_bypass_list = None
        self.discriminator = None

        if proxy_mode is not None:
            self.proxy_mode = proxy_mode
        if proxy_pac_url is not None:
            self.proxy_pac_url = proxy_pac_url
        if proxy_server is not None:
            self.proxy_server = proxy_server
        if proxy_bypass_list is not None:
            self.proxy_bypass_list = proxy_bypass_list

    @property
    def proxy_mode(self):
        """Gets the proxy_mode of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501

        Gets or sets ProxyMode.  # noqa: E501

        :return: The proxy_mode of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._proxy_mode

    @proxy_mode.setter
    def proxy_mode(self, proxy_mode):
        """Sets the proxy_mode of this AndroidForWorkProxyPayloadV2Entity_.

        Gets or sets ProxyMode.  # noqa: E501

        :param proxy_mode: The proxy_mode of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._proxy_mode = proxy_mode

    @property
    def proxy_pac_url(self):
        """Gets the proxy_pac_url of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501

        Gets or sets ProxyPacUrl.  # noqa: E501

        :return: The proxy_pac_url of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._proxy_pac_url

    @proxy_pac_url.setter
    def proxy_pac_url(self, proxy_pac_url):
        """Sets the proxy_pac_url of this AndroidForWorkProxyPayloadV2Entity_.

        Gets or sets ProxyPacUrl.  # noqa: E501

        :param proxy_pac_url: The proxy_pac_url of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._proxy_pac_url = proxy_pac_url

    @property
    def proxy_server(self):
        """Gets the proxy_server of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501

        Gets or sets ProxyServer.  # noqa: E501

        :return: The proxy_server of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._proxy_server

    @proxy_server.setter
    def proxy_server(self, proxy_server):
        """Sets the proxy_server of this AndroidForWorkProxyPayloadV2Entity_.

        Gets or sets ProxyServer.  # noqa: E501

        :param proxy_server: The proxy_server of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._proxy_server = proxy_server

    @property
    def proxy_bypass_list(self):
        """Gets the proxy_bypass_list of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501

        Gets or sets ProxyBypass List.  # noqa: E501

        :return: The proxy_bypass_list of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501
        :rtype: list[str]
        """
        return self._proxy_bypass_list

    @proxy_bypass_list.setter
    def proxy_bypass_list(self, proxy_bypass_list):
        """Sets the proxy_bypass_list of this AndroidForWorkProxyPayloadV2Entity_.

        Gets or sets ProxyBypass List.  # noqa: E501

        :param proxy_bypass_list: The proxy_bypass_list of this AndroidForWorkProxyPayloadV2Entity_.  # noqa: E501
        :type: list[str]
        """

        self._proxy_bypass_list = proxy_bypass_list

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
        if issubclass(AndroidForWorkProxyPayloadV2Entity_, dict):
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
        if not isinstance(other, AndroidForWorkProxyPayloadV2Entity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkProxyPayloadV2Entity_):
            return True

        return self.to_dict() != other.to_dict()
