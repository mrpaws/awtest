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


class AppItemV1Model(object):
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
        'name': 'str',
        'assignment_status': 'str',
        'assigned_version': 'str',
        'installed_status': 'str',
        'installed_version': 'str',
        'latest_uem_action': 'str',
        'latest_uem_action_time': 'datetime',
        'bundle_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'assignment_status': 'assignment_status',
        'assigned_version': 'assigned_version',
        'installed_status': 'installed_status',
        'installed_version': 'installed_version',
        'latest_uem_action': 'latest_uem_action',
        'latest_uem_action_time': 'latest_uem_action_time',
        'bundle_id': 'bundle_id'
    }

    def __init__(self, name=None, assignment_status=None, assigned_version=None, installed_status=None, installed_version=None, latest_uem_action=None, latest_uem_action_time=None, bundle_id=None, _configuration=None):  # noqa: E501
        """AppItemV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._assignment_status = None
        self._assigned_version = None
        self._installed_status = None
        self._installed_version = None
        self._latest_uem_action = None
        self._latest_uem_action_time = None
        self._bundle_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if assignment_status is not None:
            self.assignment_status = assignment_status
        if assigned_version is not None:
            self.assigned_version = assigned_version
        if installed_status is not None:
            self.installed_status = installed_status
        if installed_version is not None:
            self.installed_version = installed_version
        if latest_uem_action is not None:
            self.latest_uem_action = latest_uem_action
        if latest_uem_action_time is not None:
            self.latest_uem_action_time = latest_uem_action_time
        if bundle_id is not None:
            self.bundle_id = bundle_id

    @property
    def name(self):
        """Gets the name of this AppItemV1Model.  # noqa: E501

        The name of the application  # noqa: E501

        :return: The name of this AppItemV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppItemV1Model.

        The name of the application  # noqa: E501

        :param name: The name of this AppItemV1Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def assignment_status(self):
        """Gets the assignment_status of this AppItemV1Model.  # noqa: E501

        Assignment status of the app. The possible values are [Assigned, NotAssigned]  # noqa: E501

        :return: The assignment_status of this AppItemV1Model.  # noqa: E501
        :rtype: str
        """
        return self._assignment_status

    @assignment_status.setter
    def assignment_status(self, assignment_status):
        """Sets the assignment_status of this AppItemV1Model.

        Assignment status of the app. The possible values are [Assigned, NotAssigned]  # noqa: E501

        :param assignment_status: The assignment_status of this AppItemV1Model.  # noqa: E501
        :type: str
        """

        self._assignment_status = assignment_status

    @property
    def assigned_version(self):
        """Gets the assigned_version of this AppItemV1Model.  # noqa: E501

        The version of app assigned to the device  # noqa: E501

        :return: The assigned_version of this AppItemV1Model.  # noqa: E501
        :rtype: str
        """
        return self._assigned_version

    @assigned_version.setter
    def assigned_version(self, assigned_version):
        """Sets the assigned_version of this AppItemV1Model.

        The version of app assigned to the device  # noqa: E501

        :param assigned_version: The assigned_version of this AppItemV1Model.  # noqa: E501
        :type: str
        """

        self._assigned_version = assigned_version

    @property
    def installed_status(self):
        """Gets the installed_status of this AppItemV1Model.  # noqa: E501

        Installation status of the app on the device. The possible values are [Installed, NotInstalled]  # noqa: E501

        :return: The installed_status of this AppItemV1Model.  # noqa: E501
        :rtype: str
        """
        return self._installed_status

    @installed_status.setter
    def installed_status(self, installed_status):
        """Sets the installed_status of this AppItemV1Model.

        Installation status of the app on the device. The possible values are [Installed, NotInstalled]  # noqa: E501

        :param installed_status: The installed_status of this AppItemV1Model.  # noqa: E501
        :type: str
        """

        self._installed_status = installed_status

    @property
    def installed_version(self):
        """Gets the installed_version of this AppItemV1Model.  # noqa: E501

        The version of app installed on the device  # noqa: E501

        :return: The installed_version of this AppItemV1Model.  # noqa: E501
        :rtype: str
        """
        return self._installed_version

    @installed_version.setter
    def installed_version(self, installed_version):
        """Sets the installed_version of this AppItemV1Model.

        The version of app installed on the device  # noqa: E501

        :param installed_version: The installed_version of this AppItemV1Model.  # noqa: E501
        :type: str
        """

        self._installed_version = installed_version

    @property
    def latest_uem_action(self):
        """Gets the latest_uem_action of this AppItemV1Model.  # noqa: E501

        The latest server side trigger for the application. The possible values are [Unknown, PendingRelease, InstallCommandReadyForDevice, InstallCommandDispatched, InstallCommandFailed, RemoveAppCommandInHeldState, PendingRemoval, RemoveCommandSuccessful, RemoveApplicationFailed, VppLicenseNotAvailable, RequestRejected, RequestError, PendingApproval, RequestExpired, ProvisioningCommandDeleted, UserDeferredInstall]  # noqa: E501

        :return: The latest_uem_action of this AppItemV1Model.  # noqa: E501
        :rtype: str
        """
        return self._latest_uem_action

    @latest_uem_action.setter
    def latest_uem_action(self, latest_uem_action):
        """Sets the latest_uem_action of this AppItemV1Model.

        The latest server side trigger for the application. The possible values are [Unknown, PendingRelease, InstallCommandReadyForDevice, InstallCommandDispatched, InstallCommandFailed, RemoveAppCommandInHeldState, PendingRemoval, RemoveCommandSuccessful, RemoveApplicationFailed, VppLicenseNotAvailable, RequestRejected, RequestError, PendingApproval, RequestExpired, ProvisioningCommandDeleted, UserDeferredInstall]  # noqa: E501

        :param latest_uem_action: The latest_uem_action of this AppItemV1Model.  # noqa: E501
        :type: str
        """

        self._latest_uem_action = latest_uem_action

    @property
    def latest_uem_action_time(self):
        """Gets the latest_uem_action_time of this AppItemV1Model.  # noqa: E501

        The time of the latest server side trigger in YYYY-MM-DDTHH:MM:SSZ format.  # noqa: E501

        :return: The latest_uem_action_time of this AppItemV1Model.  # noqa: E501
        :rtype: datetime
        """
        return self._latest_uem_action_time

    @latest_uem_action_time.setter
    def latest_uem_action_time(self, latest_uem_action_time):
        """Sets the latest_uem_action_time of this AppItemV1Model.

        The time of the latest server side trigger in YYYY-MM-DDTHH:MM:SSZ format.  # noqa: E501

        :param latest_uem_action_time: The latest_uem_action_time of this AppItemV1Model.  # noqa: E501
        :type: datetime
        """

        self._latest_uem_action_time = latest_uem_action_time

    @property
    def bundle_id(self):
        """Gets the bundle_id of this AppItemV1Model.  # noqa: E501

        Gets or sets the unique bundle identifier of the application, e.g. com.hotels.HotelsNearMe.  # noqa: E501

        :return: The bundle_id of this AppItemV1Model.  # noqa: E501
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this AppItemV1Model.

        Gets or sets the unique bundle identifier of the application, e.g. com.hotels.HotelsNearMe.  # noqa: E501

        :param bundle_id: The bundle_id of this AppItemV1Model.  # noqa: E501
        :type: str
        """

        self._bundle_id = bundle_id

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
        if issubclass(AppItemV1Model, dict):
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
        if not isinstance(other, AppItemV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppItemV1Model):
            return True

        return self.to_dict() != other.to_dict()