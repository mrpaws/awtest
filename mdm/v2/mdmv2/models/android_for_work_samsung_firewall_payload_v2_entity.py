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


class AndroidForWorkSamsungFirewallPayloadV2Entity(object):
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
        'allow_rules': 'list[AllowRule]',
        'deny_rules': 'list[DenyRule]',
        'reroute_rules': 'list[RerouteRule]',
        'redirect_rules': 'list[RedirectRule]'
    }

    attribute_map = {
        'allow_rules': 'AllowRules',
        'deny_rules': 'DenyRules',
        'reroute_rules': 'RerouteRules',
        'redirect_rules': 'RedirectRules'
    }

    def __init__(self, allow_rules=None, deny_rules=None, reroute_rules=None, redirect_rules=None, _configuration=None):  # noqa: E501
        """AndroidForWorkSamsungFirewallPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_rules = None
        self._deny_rules = None
        self._reroute_rules = None
        self._redirect_rules = None
        self.discriminator = None

        if allow_rules is not None:
            self.allow_rules = allow_rules
        if deny_rules is not None:
            self.deny_rules = deny_rules
        if reroute_rules is not None:
            self.reroute_rules = reroute_rules
        if redirect_rules is not None:
            self.redirect_rules = redirect_rules

    @property
    def allow_rules(self):
        """Gets the allow_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501

        Gets or sets AllowRules.  # noqa: E501

        :return: The allow_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501
        :rtype: list[AllowRule]
        """
        return self._allow_rules

    @allow_rules.setter
    def allow_rules(self, allow_rules):
        """Sets the allow_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.

        Gets or sets AllowRules.  # noqa: E501

        :param allow_rules: The allow_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501
        :type: list[AllowRule]
        """

        self._allow_rules = allow_rules

    @property
    def deny_rules(self):
        """Gets the deny_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501

        Gets or sets DenyRules.  # noqa: E501

        :return: The deny_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501
        :rtype: list[DenyRule]
        """
        return self._deny_rules

    @deny_rules.setter
    def deny_rules(self, deny_rules):
        """Sets the deny_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.

        Gets or sets DenyRules.  # noqa: E501

        :param deny_rules: The deny_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501
        :type: list[DenyRule]
        """

        self._deny_rules = deny_rules

    @property
    def reroute_rules(self):
        """Gets the reroute_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501

        Gets or sets RerouteRules.  # noqa: E501

        :return: The reroute_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501
        :rtype: list[RerouteRule]
        """
        return self._reroute_rules

    @reroute_rules.setter
    def reroute_rules(self, reroute_rules):
        """Sets the reroute_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.

        Gets or sets RerouteRules.  # noqa: E501

        :param reroute_rules: The reroute_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501
        :type: list[RerouteRule]
        """

        self._reroute_rules = reroute_rules

    @property
    def redirect_rules(self):
        """Gets the redirect_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501

        Gets or sets RedirectRules.  # noqa: E501

        :return: The redirect_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501
        :rtype: list[RedirectRule]
        """
        return self._redirect_rules

    @redirect_rules.setter
    def redirect_rules(self, redirect_rules):
        """Sets the redirect_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.

        Gets or sets RedirectRules.  # noqa: E501

        :param redirect_rules: The redirect_rules of this AndroidForWorkSamsungFirewallPayloadV2Entity.  # noqa: E501
        :type: list[RedirectRule]
        """

        self._redirect_rules = redirect_rules

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
        if issubclass(AndroidForWorkSamsungFirewallPayloadV2Entity, dict):
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
        if not isinstance(other, AndroidForWorkSamsungFirewallPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkSamsungFirewallPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
