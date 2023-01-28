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


class AppAssignmentRestrictionV1Model(object):
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
        'remove_on_unenroll': 'bool',
        'prevent_application_backup': 'bool',
        'make_app_mdm_managed': 'bool',
        'managed_access': 'bool',
        'desired_state_management': 'bool',
        'prevent_removal': 'bool'
    }

    attribute_map = {
        'remove_on_unenroll': 'remove_on_unenroll',
        'prevent_application_backup': 'prevent_application_backup',
        'make_app_mdm_managed': 'make_app_mdm_managed',
        'managed_access': 'managed_access',
        'desired_state_management': 'desired_state_management',
        'prevent_removal': 'prevent_removal'
    }

    def __init__(self, remove_on_unenroll=None, prevent_application_backup=None, make_app_mdm_managed=None, managed_access=None, desired_state_management=None, prevent_removal=None, _configuration=None):  # noqa: E501
        """AppAssignmentRestrictionV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._remove_on_unenroll = None
        self._prevent_application_backup = None
        self._make_app_mdm_managed = None
        self._managed_access = None
        self._desired_state_management = None
        self._prevent_removal = None
        self.discriminator = None

        if remove_on_unenroll is not None:
            self.remove_on_unenroll = remove_on_unenroll
        if prevent_application_backup is not None:
            self.prevent_application_backup = prevent_application_backup
        if make_app_mdm_managed is not None:
            self.make_app_mdm_managed = make_app_mdm_managed
        if managed_access is not None:
            self.managed_access = managed_access
        if desired_state_management is not None:
            self.desired_state_management = desired_state_management
        if prevent_removal is not None:
            self.prevent_removal = prevent_removal

    @property
    def remove_on_unenroll(self):
        """Gets the remove_on_unenroll of this AppAssignmentRestrictionV1Model.  # noqa: E501

        Removes the application from end user device when the device unenrolls and applicable for Apple, macOS and Android apps.  # noqa: E501

        :return: The remove_on_unenroll of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._remove_on_unenroll

    @remove_on_unenroll.setter
    def remove_on_unenroll(self, remove_on_unenroll):
        """Sets the remove_on_unenroll of this AppAssignmentRestrictionV1Model.

        Removes the application from end user device when the device unenrolls and applicable for Apple, macOS and Android apps.  # noqa: E501

        :param remove_on_unenroll: The remove_on_unenroll of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :type: bool
        """

        self._remove_on_unenroll = remove_on_unenroll

    @property
    def prevent_application_backup(self):
        """Gets the prevent_application_backup of this AppAssignmentRestrictionV1Model.  # noqa: E501

        Prevent backing up application data to iCloud(iOS only)  # noqa: E501

        :return: The prevent_application_backup of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._prevent_application_backup

    @prevent_application_backup.setter
    def prevent_application_backup(self, prevent_application_backup):
        """Sets the prevent_application_backup of this AppAssignmentRestrictionV1Model.

        Prevent backing up application data to iCloud(iOS only)  # noqa: E501

        :param prevent_application_backup: The prevent_application_backup of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :type: bool
        """

        self._prevent_application_backup = prevent_application_backup

    @property
    def make_app_mdm_managed(self):
        """Gets the make_app_mdm_managed of this AppAssignmentRestrictionV1Model.  # noqa: E501

        This flag allows admin to take over management of user installed application so that additional actions like Removals,  Application configuration can be applied to the end user device.  This flag is applicable for iOS and Windows SFD apps.  # noqa: E501

        :return: The make_app_mdm_managed of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._make_app_mdm_managed

    @make_app_mdm_managed.setter
    def make_app_mdm_managed(self, make_app_mdm_managed):
        """Sets the make_app_mdm_managed of this AppAssignmentRestrictionV1Model.

        This flag allows admin to take over management of user installed application so that additional actions like Removals,  Application configuration can be applied to the end user device.  This flag is applicable for iOS and Windows SFD apps.  # noqa: E501

        :param make_app_mdm_managed: The make_app_mdm_managed of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :type: bool
        """

        self._make_app_mdm_managed = make_app_mdm_managed

    @property
    def managed_access(self):
        """Gets the managed_access of this AppAssignmentRestrictionV1Model.  # noqa: E501

        If Managed access is enabled, by default Require Management will be enabled  # noqa: E501

        :return: The managed_access of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._managed_access

    @managed_access.setter
    def managed_access(self, managed_access):
        """Sets the managed_access of this AppAssignmentRestrictionV1Model.

        If Managed access is enabled, by default Require Management will be enabled  # noqa: E501

        :param managed_access: The managed_access of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :type: bool
        """

        self._managed_access = managed_access

    @property
    def desired_state_management(self):
        """Gets the desired_state_management of this AppAssignmentRestrictionV1Model.  # noqa: E501

        Desired state management flag and applicable for macOS SFD apps &amp; Windows Desktop SFD apps.  # noqa: E501

        :return: The desired_state_management of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._desired_state_management

    @desired_state_management.setter
    def desired_state_management(self, desired_state_management):
        """Sets the desired_state_management of this AppAssignmentRestrictionV1Model.

        Desired state management flag and applicable for macOS SFD apps &amp; Windows Desktop SFD apps.  # noqa: E501

        :param desired_state_management: The desired_state_management of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :type: bool
        """

        self._desired_state_management = desired_state_management

    @property
    def prevent_removal(self):
        """Gets the prevent_removal of this AppAssignmentRestrictionV1Model.  # noqa: E501

        If prevent removal is enabled, then it will  prevent an app from being removed from devices after installation  or conversion to management.  # noqa: E501

        :return: The prevent_removal of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._prevent_removal

    @prevent_removal.setter
    def prevent_removal(self, prevent_removal):
        """Sets the prevent_removal of this AppAssignmentRestrictionV1Model.

        If prevent removal is enabled, then it will  prevent an app from being removed from devices after installation  or conversion to management.  # noqa: E501

        :param prevent_removal: The prevent_removal of this AppAssignmentRestrictionV1Model.  # noqa: E501
        :type: bool
        """

        self._prevent_removal = prevent_removal

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
        if issubclass(AppAssignmentRestrictionV1Model, dict):
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
        if not isinstance(other, AppAssignmentRestrictionV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppAssignmentRestrictionV1Model):
            return True

        return self.to_dict() != other.to_dict()