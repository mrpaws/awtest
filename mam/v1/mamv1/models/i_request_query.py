# coding: utf-8

"""
    MAM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv1.configuration import Configuration


class IRequestQuery(object):
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
        '_query_params': 'dict(str, str)',
        'tenant_context': 'ITenantContext',
        'request_method': 'HttpMethod',
        'action_name': 'str',
        'allowed_uri_query_chars': 'list[str]'
    }

    attribute_map = {
        '_query_params': 'QueryParams',
        'tenant_context': 'TenantContext',
        'request_method': 'RequestMethod',
        'action_name': 'ActionName',
        'allowed_uri_query_chars': 'AllowedUriQueryChars'
    }

    def __init__(self, _query_params=None, tenant_context=None, request_method=None, action_name=None, allowed_uri_query_chars=None, _configuration=None):  # noqa: E501
        """IRequestQuery - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__query_params = None
        self._tenant_context = None
        self._request_method = None
        self._action_name = None
        self._allowed_uri_query_chars = None
        self.discriminator = None

        if _query_params is not None:
            self._query_params = _query_params
        if tenant_context is not None:
            self.tenant_context = tenant_context
        if request_method is not None:
            self.request_method = request_method
        if action_name is not None:
            self.action_name = action_name
        if allowed_uri_query_chars is not None:
            self.allowed_uri_query_chars = allowed_uri_query_chars

    @property
    def _query_params(self):
        """Gets the _query_params of this IRequestQuery.  # noqa: E501

        Gets or sets Query Parameters. For e.g. any query string parameters will be extracted to key,value pair and stored here.  # noqa: E501

        :return: The _query_params of this IRequestQuery.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self.__query_params

    @_query_params.setter
    def _query_params(self, _query_params):
        """Sets the _query_params of this IRequestQuery.

        Gets or sets Query Parameters. For e.g. any query string parameters will be extracted to key,value pair and stored here.  # noqa: E501

        :param _query_params: The _query_params of this IRequestQuery.  # noqa: E501
        :type: dict(str, str)
        """

        self.__query_params = _query_params

    @property
    def tenant_context(self):
        """Gets the tenant_context of this IRequestQuery.  # noqa: E501

        Gets or sets IAwTenantContext. Will hold the tenant details, which will be filled as part of the tenant validation handler.  # noqa: E501

        :return: The tenant_context of this IRequestQuery.  # noqa: E501
        :rtype: ITenantContext
        """
        return self._tenant_context

    @tenant_context.setter
    def tenant_context(self, tenant_context):
        """Sets the tenant_context of this IRequestQuery.

        Gets or sets IAwTenantContext. Will hold the tenant details, which will be filled as part of the tenant validation handler.  # noqa: E501

        :param tenant_context: The tenant_context of this IRequestQuery.  # noqa: E501
        :type: ITenantContext
        """

        self._tenant_context = tenant_context

    @property
    def request_method(self):
        """Gets the request_method of this IRequestQuery.  # noqa: E501

        Gets or sets RequestMethod. Will be used to write custom rules.  # noqa: E501

        :return: The request_method of this IRequestQuery.  # noqa: E501
        :rtype: HttpMethod
        """
        return self._request_method

    @request_method.setter
    def request_method(self, request_method):
        """Sets the request_method of this IRequestQuery.

        Gets or sets RequestMethod. Will be used to write custom rules.  # noqa: E501

        :param request_method: The request_method of this IRequestQuery.  # noqa: E501
        :type: HttpMethod
        """

        self._request_method = request_method

    @property
    def action_name(self):
        """Gets the action_name of this IRequestQuery.  # noqa: E501

        Gets or sets ActionName.  # noqa: E501

        :return: The action_name of this IRequestQuery.  # noqa: E501
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this IRequestQuery.

        Gets or sets ActionName.  # noqa: E501

        :param action_name: The action_name of this IRequestQuery.  # noqa: E501
        :type: str
        """

        self._action_name = action_name

    @property
    def allowed_uri_query_chars(self):
        """Gets the allowed_uri_query_chars of this IRequestQuery.  # noqa: E501

        Gets or sets allowed Characters in Query String.  # noqa: E501

        :return: The allowed_uri_query_chars of this IRequestQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_uri_query_chars

    @allowed_uri_query_chars.setter
    def allowed_uri_query_chars(self, allowed_uri_query_chars):
        """Sets the allowed_uri_query_chars of this IRequestQuery.

        Gets or sets allowed Characters in Query String.  # noqa: E501

        :param allowed_uri_query_chars: The allowed_uri_query_chars of this IRequestQuery.  # noqa: E501
        :type: list[str]
        """

        self._allowed_uri_query_chars = allowed_uri_query_chars

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
        if issubclass(IRequestQuery, dict):
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
        if not isinstance(other, IRequestQuery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IRequestQuery):
            return True

        return self.to_dict() != other.to_dict()
