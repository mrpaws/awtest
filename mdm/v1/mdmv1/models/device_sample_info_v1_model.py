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


class DeviceSampleInfoV1Model(object):
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
        'installed_status': 'str',
        'installed_version': 'str',
        'latest_app_reason': 'str',
        'latest_app_reason_time': 'datetime',
        'latest_app_sample_event': 'str'
    }

    attribute_map = {
        'installed_status': 'installed_status',
        'installed_version': 'installed_version',
        'latest_app_reason': 'latest_app_reason',
        'latest_app_reason_time': 'latest_app_reason_time',
        'latest_app_sample_event': 'latest_app_sample_event'
    }

    def __init__(self, installed_status=None, installed_version=None, latest_app_reason=None, latest_app_reason_time=None, latest_app_sample_event=None, _configuration=None):  # noqa: E501
        """DeviceSampleInfoV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._installed_status = None
        self._installed_version = None
        self._latest_app_reason = None
        self._latest_app_reason_time = None
        self._latest_app_sample_event = None
        self.discriminator = None

        self.installed_status = installed_status
        if installed_version is not None:
            self.installed_version = installed_version
        if latest_app_reason is not None:
            self.latest_app_reason = latest_app_reason
        if latest_app_reason_time is not None:
            self.latest_app_reason_time = latest_app_reason_time
        if latest_app_sample_event is not None:
            self.latest_app_sample_event = latest_app_sample_event

    @property
    def installed_status(self):
        """Gets the installed_status of this DeviceSampleInfoV1Model.  # noqa: E501

        Installation status of the app on the device. The possible values are [Installed, NotInstalled]  # noqa: E501

        :return: The installed_status of this DeviceSampleInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._installed_status

    @installed_status.setter
    def installed_status(self, installed_status):
        """Sets the installed_status of this DeviceSampleInfoV1Model.

        Installation status of the app on the device. The possible values are [Installed, NotInstalled]  # noqa: E501

        :param installed_status: The installed_status of this DeviceSampleInfoV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and installed_status is None:
            raise ValueError("Invalid value for `installed_status`, must not be `None`")  # noqa: E501

        self._installed_status = installed_status

    @property
    def installed_version(self):
        """Gets the installed_version of this DeviceSampleInfoV1Model.  # noqa: E501

        The version of app installed on the device  # noqa: E501

        :return: The installed_version of this DeviceSampleInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._installed_version

    @installed_version.setter
    def installed_version(self, installed_version):
        """Sets the installed_version of this DeviceSampleInfoV1Model.

        The version of app installed on the device  # noqa: E501

        :param installed_version: The installed_version of this DeviceSampleInfoV1Model.  # noqa: E501
        :type: str
        """

        self._installed_version = installed_version

    @property
    def latest_app_reason(self):
        """Gets the latest_app_reason of this DeviceSampleInfoV1Model.  # noqa: E501

        The application reason reported by the device. The possible values are [NeedsRedemption, Redeeming, Prompting, Installing, Managed, MDMRemoval, MDMRemoved, ManagedButUninstalled, UserRejected, Failed, Unknown, UserInstalledApp, AwaitingInstallOnDevice, Updating, ManagementRejected, PromptingForManagement, DownloadInProgress, DownloadFailed, RemoveApplicationFailed, FinalDetectionFailed, DeviceEligibilityCheckFailed, ExecutionFailed, DependentAppValidationFailed, CheckingDeviceEligibility, ValidatingDependentApps, PendingReboot]  # noqa: E501

        :return: The latest_app_reason of this DeviceSampleInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._latest_app_reason

    @latest_app_reason.setter
    def latest_app_reason(self, latest_app_reason):
        """Sets the latest_app_reason of this DeviceSampleInfoV1Model.

        The application reason reported by the device. The possible values are [NeedsRedemption, Redeeming, Prompting, Installing, Managed, MDMRemoval, MDMRemoved, ManagedButUninstalled, UserRejected, Failed, Unknown, UserInstalledApp, AwaitingInstallOnDevice, Updating, ManagementRejected, PromptingForManagement, DownloadInProgress, DownloadFailed, RemoveApplicationFailed, FinalDetectionFailed, DeviceEligibilityCheckFailed, ExecutionFailed, DependentAppValidationFailed, CheckingDeviceEligibility, ValidatingDependentApps, PendingReboot]  # noqa: E501

        :param latest_app_reason: The latest_app_reason of this DeviceSampleInfoV1Model.  # noqa: E501
        :type: str
        """

        self._latest_app_reason = latest_app_reason

    @property
    def latest_app_reason_time(self):
        """Gets the latest_app_reason_time of this DeviceSampleInfoV1Model.  # noqa: E501

        The time at which the reason was reported by the device  # noqa: E501

        :return: The latest_app_reason_time of this DeviceSampleInfoV1Model.  # noqa: E501
        :rtype: datetime
        """
        return self._latest_app_reason_time

    @latest_app_reason_time.setter
    def latest_app_reason_time(self, latest_app_reason_time):
        """Sets the latest_app_reason_time of this DeviceSampleInfoV1Model.

        The time at which the reason was reported by the device  # noqa: E501

        :param latest_app_reason_time: The latest_app_reason_time of this DeviceSampleInfoV1Model.  # noqa: E501
        :type: datetime
        """

        self._latest_app_reason_time = latest_app_reason_time

    @property
    def latest_app_sample_event(self):
        """Gets the latest_app_sample_event of this DeviceSampleInfoV1Model.  # noqa: E501

        The latest transient reason reported by the device. The possible values are [NeedsRedemption, Redeeming, Prompting, MDMRemoved, UserRejected, Failed, UserInstalledApp, AwaitingInstallOnDevice, Updating, ManagementRejected, PromptingForManagement, DownloadInProgress, RemoveApplicationFailed, CheckingDeviceEligibility, ValidatingDependentApps, PendingReboot]  # noqa: E501

        :return: The latest_app_sample_event of this DeviceSampleInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._latest_app_sample_event

    @latest_app_sample_event.setter
    def latest_app_sample_event(self, latest_app_sample_event):
        """Sets the latest_app_sample_event of this DeviceSampleInfoV1Model.

        The latest transient reason reported by the device. The possible values are [NeedsRedemption, Redeeming, Prompting, MDMRemoved, UserRejected, Failed, UserInstalledApp, AwaitingInstallOnDevice, Updating, ManagementRejected, PromptingForManagement, DownloadInProgress, RemoveApplicationFailed, CheckingDeviceEligibility, ValidatingDependentApps, PendingReboot]  # noqa: E501

        :param latest_app_sample_event: The latest_app_sample_event of this DeviceSampleInfoV1Model.  # noqa: E501
        :type: str
        """

        self._latest_app_sample_event = latest_app_sample_event

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
        if issubclass(DeviceSampleInfoV1Model, dict):
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
        if not isinstance(other, DeviceSampleInfoV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceSampleInfoV1Model):
            return True

        return self.to_dict() != other.to_dict()
