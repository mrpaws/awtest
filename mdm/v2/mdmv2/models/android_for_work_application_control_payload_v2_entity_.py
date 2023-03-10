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


class AndroidForWorkApplicationControlPayloadV2Entity_(object):
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
        'prevent_uninstall_required_apps': 'bool',
        'disable_access_to_blacklisted_apps': 'bool',
        'enable_system_apps_inside_androidfor_work': 'bool',
        'managed_devices': 'bool',
        'work_profiles': 'bool'
    }

    attribute_map = {
        'prevent_uninstall_required_apps': 'PreventUninstallRequiredApps',
        'disable_access_to_blacklisted_apps': 'DisableAccessToBlacklistedApps',
        'enable_system_apps_inside_androidfor_work': 'EnableSystemAppsInsideAndroidforWork',
        'managed_devices': 'ManagedDevices',
        'work_profiles': 'WorkProfiles'
    }

    def __init__(self, prevent_uninstall_required_apps=None, disable_access_to_blacklisted_apps=None, enable_system_apps_inside_androidfor_work=None, managed_devices=None, work_profiles=None, _configuration=None):  # noqa: E501
        """AndroidForWorkApplicationControlPayloadV2Entity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._prevent_uninstall_required_apps = None
        self._disable_access_to_blacklisted_apps = None
        self._enable_system_apps_inside_androidfor_work = None
        self._managed_devices = None
        self._work_profiles = None
        self.discriminator = None

        if prevent_uninstall_required_apps is not None:
            self.prevent_uninstall_required_apps = prevent_uninstall_required_apps
        if disable_access_to_blacklisted_apps is not None:
            self.disable_access_to_blacklisted_apps = disable_access_to_blacklisted_apps
        if enable_system_apps_inside_androidfor_work is not None:
            self.enable_system_apps_inside_androidfor_work = enable_system_apps_inside_androidfor_work
        if managed_devices is not None:
            self.managed_devices = managed_devices
        if work_profiles is not None:
            self.work_profiles = work_profiles

    @property
    def prevent_uninstall_required_apps(self):
        """Gets the prevent_uninstall_required_apps of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether [prevent uninstall required apps].  # noqa: E501

        :return: The prevent_uninstall_required_apps of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._prevent_uninstall_required_apps

    @prevent_uninstall_required_apps.setter
    def prevent_uninstall_required_apps(self, prevent_uninstall_required_apps):
        """Sets the prevent_uninstall_required_apps of this AndroidForWorkApplicationControlPayloadV2Entity_.

        Gets or sets a value indicating whether [prevent uninstall required apps].  # noqa: E501

        :param prevent_uninstall_required_apps: The prevent_uninstall_required_apps of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._prevent_uninstall_required_apps = prevent_uninstall_required_apps

    @property
    def disable_access_to_blacklisted_apps(self):
        """Gets the disable_access_to_blacklisted_apps of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether [prevent install blacklisted apps].  # noqa: E501

        :return: The disable_access_to_blacklisted_apps of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._disable_access_to_blacklisted_apps

    @disable_access_to_blacklisted_apps.setter
    def disable_access_to_blacklisted_apps(self, disable_access_to_blacklisted_apps):
        """Sets the disable_access_to_blacklisted_apps of this AndroidForWorkApplicationControlPayloadV2Entity_.

        Gets or sets a value indicating whether [prevent install blacklisted apps].  # noqa: E501

        :param disable_access_to_blacklisted_apps: The disable_access_to_blacklisted_apps of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._disable_access_to_blacklisted_apps = disable_access_to_blacklisted_apps

    @property
    def enable_system_apps_inside_androidfor_work(self):
        """Gets the enable_system_apps_inside_androidfor_work of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether [enable system apps in work profile].  # noqa: E501

        :return: The enable_system_apps_inside_androidfor_work of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._enable_system_apps_inside_androidfor_work

    @enable_system_apps_inside_androidfor_work.setter
    def enable_system_apps_inside_androidfor_work(self, enable_system_apps_inside_androidfor_work):
        """Sets the enable_system_apps_inside_androidfor_work of this AndroidForWorkApplicationControlPayloadV2Entity_.

        Gets or sets a value indicating whether [enable system apps in work profile].  # noqa: E501

        :param enable_system_apps_inside_androidfor_work: The enable_system_apps_inside_androidfor_work of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._enable_system_apps_inside_androidfor_work = enable_system_apps_inside_androidfor_work

    @property
    def managed_devices(self):
        """Gets the managed_devices of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501

        Gets or sets managed Devices (DO) settings.  # noqa: E501

        :return: The managed_devices of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._managed_devices

    @managed_devices.setter
    def managed_devices(self, managed_devices):
        """Sets the managed_devices of this AndroidForWorkApplicationControlPayloadV2Entity_.

        Gets or sets managed Devices (DO) settings.  # noqa: E501

        :param managed_devices: The managed_devices of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._managed_devices = managed_devices

    @property
    def work_profiles(self):
        """Gets the work_profiles of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501

        Gets or sets work Profiles (PO) settings.  # noqa: E501

        :return: The work_profiles of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._work_profiles

    @work_profiles.setter
    def work_profiles(self, work_profiles):
        """Sets the work_profiles of this AndroidForWorkApplicationControlPayloadV2Entity_.

        Gets or sets work Profiles (PO) settings.  # noqa: E501

        :param work_profiles: The work_profiles of this AndroidForWorkApplicationControlPayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._work_profiles = work_profiles

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
        if issubclass(AndroidForWorkApplicationControlPayloadV2Entity_, dict):
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
        if not isinstance(other, AndroidForWorkApplicationControlPayloadV2Entity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkApplicationControlPayloadV2Entity_):
            return True

        return self.to_dict() != other.to_dict()
