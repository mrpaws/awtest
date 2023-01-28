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


class AppDeploymentOptionsModel_(object):
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
        'when_to_install': 'WhenToInstallApiModel_',
        'how_to_install': 'HowToInstallApiModel_',
        'when_to_call_install_complete': 'WhenToCallInstallCompleteApiModel_'
    }

    attribute_map = {
        'when_to_install': 'WhenToInstall',
        'how_to_install': 'HowToInstall',
        'when_to_call_install_complete': 'WhenToCallInstallComplete'
    }

    def __init__(self, when_to_install=None, how_to_install=None, when_to_call_install_complete=None, _configuration=None):  # noqa: E501
        """AppDeploymentOptionsModel_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._when_to_install = None
        self._how_to_install = None
        self._when_to_call_install_complete = None
        self.discriminator = None

        if when_to_install is not None:
            self.when_to_install = when_to_install
        if how_to_install is not None:
            self.how_to_install = how_to_install
        if when_to_call_install_complete is not None:
            self.when_to_call_install_complete = when_to_call_install_complete

    @property
    def when_to_install(self):
        """Gets the when_to_install of this AppDeploymentOptionsModel_.  # noqa: E501

        Gets or sets when to install options.  # noqa: E501

        :return: The when_to_install of this AppDeploymentOptionsModel_.  # noqa: E501
        :rtype: WhenToInstallApiModel_
        """
        return self._when_to_install

    @when_to_install.setter
    def when_to_install(self, when_to_install):
        """Sets the when_to_install of this AppDeploymentOptionsModel_.

        Gets or sets when to install options.  # noqa: E501

        :param when_to_install: The when_to_install of this AppDeploymentOptionsModel_.  # noqa: E501
        :type: WhenToInstallApiModel_
        """

        self._when_to_install = when_to_install

    @property
    def how_to_install(self):
        """Gets the how_to_install of this AppDeploymentOptionsModel_.  # noqa: E501

        Gets or sets how to install options.  # noqa: E501

        :return: The how_to_install of this AppDeploymentOptionsModel_.  # noqa: E501
        :rtype: HowToInstallApiModel_
        """
        return self._how_to_install

    @how_to_install.setter
    def how_to_install(self, how_to_install):
        """Sets the how_to_install of this AppDeploymentOptionsModel_.

        Gets or sets how to install options.  # noqa: E501

        :param how_to_install: The how_to_install of this AppDeploymentOptionsModel_.  # noqa: E501
        :type: HowToInstallApiModel_
        """

        self._how_to_install = how_to_install

    @property
    def when_to_call_install_complete(self):
        """Gets the when_to_call_install_complete of this AppDeploymentOptionsModel_.  # noqa: E501

        Gets or sets when to call install complete options.  # noqa: E501

        :return: The when_to_call_install_complete of this AppDeploymentOptionsModel_.  # noqa: E501
        :rtype: WhenToCallInstallCompleteApiModel_
        """
        return self._when_to_call_install_complete

    @when_to_call_install_complete.setter
    def when_to_call_install_complete(self, when_to_call_install_complete):
        """Sets the when_to_call_install_complete of this AppDeploymentOptionsModel_.

        Gets or sets when to call install complete options.  # noqa: E501

        :param when_to_call_install_complete: The when_to_call_install_complete of this AppDeploymentOptionsModel_.  # noqa: E501
        :type: WhenToCallInstallCompleteApiModel_
        """

        self._when_to_call_install_complete = when_to_call_install_complete

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
        if issubclass(AppDeploymentOptionsModel_, dict):
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
        if not isinstance(other, AppDeploymentOptionsModel_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppDeploymentOptionsModel_):
            return True

        return self.to_dict() != other.to_dict()
