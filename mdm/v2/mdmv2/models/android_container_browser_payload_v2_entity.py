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


class AndroidContainerBrowserPayloadV2Entity(object):
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
        'allow_popups': 'bool',
        'allow_cookies': 'bool',
        'allow_auto_fill': 'bool',
        'allow_java_script': 'bool',
        'force_fraud_warning': 'bool'
    }

    attribute_map = {
        'allow_popups': 'AllowPopups',
        'allow_cookies': 'AllowCookies',
        'allow_auto_fill': 'AllowAutoFill',
        'allow_java_script': 'AllowJavaScript',
        'force_fraud_warning': 'ForceFraudWarning'
    }

    def __init__(self, allow_popups=None, allow_cookies=None, allow_auto_fill=None, allow_java_script=None, force_fraud_warning=None, _configuration=None):  # noqa: E501
        """AndroidContainerBrowserPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_popups = None
        self._allow_cookies = None
        self._allow_auto_fill = None
        self._allow_java_script = None
        self._force_fraud_warning = None
        self.discriminator = None

        if allow_popups is not None:
            self.allow_popups = allow_popups
        if allow_cookies is not None:
            self.allow_cookies = allow_cookies
        if allow_auto_fill is not None:
            self.allow_auto_fill = allow_auto_fill
        if allow_java_script is not None:
            self.allow_java_script = allow_java_script
        if force_fraud_warning is not None:
            self.force_fraud_warning = force_fraud_warning

    @property
    def allow_popups(self):
        """Gets the allow_popups of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets Allow pop ups.  # noqa: E501

        :return: The allow_popups of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_popups

    @allow_popups.setter
    def allow_popups(self, allow_popups):
        """Sets the allow_popups of this AndroidContainerBrowserPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets Allow pop ups.  # noqa: E501

        :param allow_popups: The allow_popups of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_popups = allow_popups

    @property
    def allow_cookies(self):
        """Gets the allow_cookies of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets Allow Cookies.  # noqa: E501

        :return: The allow_cookies of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_cookies

    @allow_cookies.setter
    def allow_cookies(self, allow_cookies):
        """Sets the allow_cookies of this AndroidContainerBrowserPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets Allow Cookies.  # noqa: E501

        :param allow_cookies: The allow_cookies of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_cookies = allow_cookies

    @property
    def allow_auto_fill(self):
        """Gets the allow_auto_fill of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets Allow Auto-Fill.  # noqa: E501

        :return: The allow_auto_fill of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_auto_fill

    @allow_auto_fill.setter
    def allow_auto_fill(self, allow_auto_fill):
        """Sets the allow_auto_fill of this AndroidContainerBrowserPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets Allow Auto-Fill.  # noqa: E501

        :param allow_auto_fill: The allow_auto_fill of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_auto_fill = allow_auto_fill

    @property
    def allow_java_script(self):
        """Gets the allow_java_script of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets Allow JavaScript.  # noqa: E501

        :return: The allow_java_script of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_java_script

    @allow_java_script.setter
    def allow_java_script(self, allow_java_script):
        """Sets the allow_java_script of this AndroidContainerBrowserPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets Allow JavaScript.  # noqa: E501

        :param allow_java_script: The allow_java_script of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_java_script = allow_java_script

    @property
    def force_fraud_warning(self):
        """Gets the force_fraud_warning of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether gets or sets Force Fraud Warning.  # noqa: E501

        :return: The force_fraud_warning of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._force_fraud_warning

    @force_fraud_warning.setter
    def force_fraud_warning(self, force_fraud_warning):
        """Sets the force_fraud_warning of this AndroidContainerBrowserPayloadV2Entity.

        Gets or sets a value indicating whether gets or sets Force Fraud Warning.  # noqa: E501

        :param force_fraud_warning: The force_fraud_warning of this AndroidContainerBrowserPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._force_fraud_warning = force_fraud_warning

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
        if issubclass(AndroidContainerBrowserPayloadV2Entity, dict):
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
        if not isinstance(other, AndroidContainerBrowserPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidContainerBrowserPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
