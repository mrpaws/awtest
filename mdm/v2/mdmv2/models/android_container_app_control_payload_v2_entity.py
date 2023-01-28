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


class AndroidContainerAppControlPayloadV2Entity(object):
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
        'blacklist_application_name': 'str',
        'blacklist_application_id': 'str',
        'prevent_install_blacklisted_apps': 'bool',
        'whitelist_application_name': 'str',
        'whitelist_application_id': 'str',
        'allow_only_whitelisted_apps': 'bool',
        'required_application_name': 'str',
        'required_application_id': 'str',
        'prevent_uninstall_required_apps': 'bool'
    }

    attribute_map = {
        'blacklist_application_name': 'BlacklistApplicationName',
        'blacklist_application_id': 'BlacklistApplicationID',
        'prevent_install_blacklisted_apps': 'PreventInstallBlacklistedApps',
        'whitelist_application_name': 'WhitelistApplicationName',
        'whitelist_application_id': 'WhitelistApplicationID',
        'allow_only_whitelisted_apps': 'AllowOnlyWhitelistedApps',
        'required_application_name': 'RequiredApplicationName',
        'required_application_id': 'RequiredApplicationId',
        'prevent_uninstall_required_apps': 'PreventUninstallRequiredApps'
    }

    def __init__(self, blacklist_application_name=None, blacklist_application_id=None, prevent_install_blacklisted_apps=None, whitelist_application_name=None, whitelist_application_id=None, allow_only_whitelisted_apps=None, required_application_name=None, required_application_id=None, prevent_uninstall_required_apps=None, _configuration=None):  # noqa: E501
        """AndroidContainerAppControlPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._blacklist_application_name = None
        self._blacklist_application_id = None
        self._prevent_install_blacklisted_apps = None
        self._whitelist_application_name = None
        self._whitelist_application_id = None
        self._allow_only_whitelisted_apps = None
        self._required_application_name = None
        self._required_application_id = None
        self._prevent_uninstall_required_apps = None
        self.discriminator = None

        if blacklist_application_name is not None:
            self.blacklist_application_name = blacklist_application_name
        if blacklist_application_id is not None:
            self.blacklist_application_id = blacklist_application_id
        if prevent_install_blacklisted_apps is not None:
            self.prevent_install_blacklisted_apps = prevent_install_blacklisted_apps
        if whitelist_application_name is not None:
            self.whitelist_application_name = whitelist_application_name
        if whitelist_application_id is not None:
            self.whitelist_application_id = whitelist_application_id
        if allow_only_whitelisted_apps is not None:
            self.allow_only_whitelisted_apps = allow_only_whitelisted_apps
        if required_application_name is not None:
            self.required_application_name = required_application_name
        if required_application_id is not None:
            self.required_application_id = required_application_id
        if prevent_uninstall_required_apps is not None:
            self.prevent_uninstall_required_apps = prevent_uninstall_required_apps

    @property
    def blacklist_application_name(self):
        """Gets the blacklist_application_name of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501

        Gets or sets BlacklistApplicationName.  # noqa: E501

        :return: The blacklist_application_name of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._blacklist_application_name

    @blacklist_application_name.setter
    def blacklist_application_name(self, blacklist_application_name):
        """Sets the blacklist_application_name of this AndroidContainerAppControlPayloadV2Entity.

        Gets or sets BlacklistApplicationName.  # noqa: E501

        :param blacklist_application_name: The blacklist_application_name of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._blacklist_application_name = blacklist_application_name

    @property
    def blacklist_application_id(self):
        """Gets the blacklist_application_id of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501

        Gets or sets BlacklistApplicationID.  # noqa: E501

        :return: The blacklist_application_id of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._blacklist_application_id

    @blacklist_application_id.setter
    def blacklist_application_id(self, blacklist_application_id):
        """Sets the blacklist_application_id of this AndroidContainerAppControlPayloadV2Entity.

        Gets or sets BlacklistApplicationID.  # noqa: E501

        :param blacklist_application_id: The blacklist_application_id of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._blacklist_application_id = blacklist_application_id

    @property
    def prevent_install_blacklisted_apps(self):
        """Gets the prevent_install_blacklisted_apps of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501

        Gets or sets PreventInstallBlacklistedApps.  # noqa: E501

        :return: The prevent_install_blacklisted_apps of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._prevent_install_blacklisted_apps

    @prevent_install_blacklisted_apps.setter
    def prevent_install_blacklisted_apps(self, prevent_install_blacklisted_apps):
        """Sets the prevent_install_blacklisted_apps of this AndroidContainerAppControlPayloadV2Entity.

        Gets or sets PreventInstallBlacklistedApps.  # noqa: E501

        :param prevent_install_blacklisted_apps: The prevent_install_blacklisted_apps of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._prevent_install_blacklisted_apps = prevent_install_blacklisted_apps

    @property
    def whitelist_application_name(self):
        """Gets the whitelist_application_name of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501

        Gets or sets WhitelistApplicationName.  # noqa: E501

        :return: The whitelist_application_name of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._whitelist_application_name

    @whitelist_application_name.setter
    def whitelist_application_name(self, whitelist_application_name):
        """Sets the whitelist_application_name of this AndroidContainerAppControlPayloadV2Entity.

        Gets or sets WhitelistApplicationName.  # noqa: E501

        :param whitelist_application_name: The whitelist_application_name of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._whitelist_application_name = whitelist_application_name

    @property
    def whitelist_application_id(self):
        """Gets the whitelist_application_id of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501

        Gets or sets WhitelistApplicationID.  # noqa: E501

        :return: The whitelist_application_id of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._whitelist_application_id

    @whitelist_application_id.setter
    def whitelist_application_id(self, whitelist_application_id):
        """Sets the whitelist_application_id of this AndroidContainerAppControlPayloadV2Entity.

        Gets or sets WhitelistApplicationID.  # noqa: E501

        :param whitelist_application_id: The whitelist_application_id of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._whitelist_application_id = whitelist_application_id

    @property
    def allow_only_whitelisted_apps(self):
        """Gets the allow_only_whitelisted_apps of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501

        Gets or sets AllowOnlyWhitelistedApps.  # noqa: E501

        :return: The allow_only_whitelisted_apps of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_only_whitelisted_apps

    @allow_only_whitelisted_apps.setter
    def allow_only_whitelisted_apps(self, allow_only_whitelisted_apps):
        """Sets the allow_only_whitelisted_apps of this AndroidContainerAppControlPayloadV2Entity.

        Gets or sets AllowOnlyWhitelistedApps.  # noqa: E501

        :param allow_only_whitelisted_apps: The allow_only_whitelisted_apps of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._allow_only_whitelisted_apps = allow_only_whitelisted_apps

    @property
    def required_application_name(self):
        """Gets the required_application_name of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501

        Gets or sets RequiredApplicationName.  # noqa: E501

        :return: The required_application_name of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._required_application_name

    @required_application_name.setter
    def required_application_name(self, required_application_name):
        """Sets the required_application_name of this AndroidContainerAppControlPayloadV2Entity.

        Gets or sets RequiredApplicationName.  # noqa: E501

        :param required_application_name: The required_application_name of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._required_application_name = required_application_name

    @property
    def required_application_id(self):
        """Gets the required_application_id of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501

        Gets or sets RequiredApplicationId.  # noqa: E501

        :return: The required_application_id of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._required_application_id

    @required_application_id.setter
    def required_application_id(self, required_application_id):
        """Sets the required_application_id of this AndroidContainerAppControlPayloadV2Entity.

        Gets or sets RequiredApplicationId.  # noqa: E501

        :param required_application_id: The required_application_id of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._required_application_id = required_application_id

    @property
    def prevent_uninstall_required_apps(self):
        """Gets the prevent_uninstall_required_apps of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501

        Gets or sets PreventUninstallRequiredApps.  # noqa: E501

        :return: The prevent_uninstall_required_apps of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._prevent_uninstall_required_apps

    @prevent_uninstall_required_apps.setter
    def prevent_uninstall_required_apps(self, prevent_uninstall_required_apps):
        """Sets the prevent_uninstall_required_apps of this AndroidContainerAppControlPayloadV2Entity.

        Gets or sets PreventUninstallRequiredApps.  # noqa: E501

        :param prevent_uninstall_required_apps: The prevent_uninstall_required_apps of this AndroidContainerAppControlPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._prevent_uninstall_required_apps = prevent_uninstall_required_apps

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
        if issubclass(AndroidContainerAppControlPayloadV2Entity, dict):
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
        if not isinstance(other, AndroidContainerAppControlPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidContainerAppControlPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()