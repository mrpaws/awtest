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


class DeviceUpdateDeploymentUpdateV1Model(object):
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
        'deployment_start_time': 'datetime',
        'deployment_type': 'str',
        'smart_group_uuids': 'list[str]',
        'notifications': 'list[NotificationV1Model]'
    }

    attribute_map = {
        'name': 'name',
        'deployment_start_time': 'deployment_start_time',
        'deployment_type': 'deployment_type',
        'smart_group_uuids': 'smart_group_uuids',
        'notifications': 'notifications'
    }

    def __init__(self, name=None, deployment_start_time=None, deployment_type=None, smart_group_uuids=None, notifications=None, _configuration=None):  # noqa: E501
        """DeviceUpdateDeploymentUpdateV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._deployment_start_time = None
        self._deployment_type = None
        self._smart_group_uuids = None
        self._notifications = None
        self.discriminator = None

        self.name = name
        self.deployment_start_time = deployment_start_time
        self.deployment_type = deployment_type
        self.smart_group_uuids = smart_group_uuids
        if notifications is not None:
            self.notifications = notifications

    @property
    def name(self):
        """Gets the name of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501

        Gets or sets the name of the deployment.  # noqa: E501

        :return: The name of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceUpdateDeploymentUpdateV1Model.

        Gets or sets the name of the deployment.  # noqa: E501

        :param name: The name of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def deployment_start_time(self):
        """Gets the deployment_start_time of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501

        Gets or sets the deployment start time.  # noqa: E501

        :return: The deployment_start_time of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501
        :rtype: datetime
        """
        return self._deployment_start_time

    @deployment_start_time.setter
    def deployment_start_time(self, deployment_start_time):
        """Sets the deployment_start_time of this DeviceUpdateDeploymentUpdateV1Model.

        Gets or sets the deployment start time.  # noqa: E501

        :param deployment_start_time: The deployment_start_time of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and deployment_start_time is None:
            raise ValueError("Invalid value for `deployment_start_time`, must not be `None`")  # noqa: E501

        self._deployment_start_time = deployment_start_time

    @property
    def deployment_type(self):
        """Gets the deployment_type of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501

        Gets or sets the deployment type. Possible Values [DOWNLOAD_AND_INSTALL, DOWNLOAD_ONLY, INSTALL_ONLY].  # noqa: E501

        :return: The deployment_type of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this DeviceUpdateDeploymentUpdateV1Model.

        Gets or sets the deployment type. Possible Values [DOWNLOAD_AND_INSTALL, DOWNLOAD_ONLY, INSTALL_ONLY].  # noqa: E501

        :param deployment_type: The deployment_type of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and deployment_type is None:
            raise ValueError("Invalid value for `deployment_type`, must not be `None`")  # noqa: E501
        allowed_values = ["UNKNOWN", "DOWNLOAD_AND_INSTALL", "DOWNLOAD_ONLY", "INSTALL_ONLY"]  # noqa: E501
        if (self._configuration.client_side_validation and
                deployment_type not in allowed_values):
            raise ValueError(
                "Invalid value for `deployment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_type, allowed_values)
            )

        self._deployment_type = deployment_type

    @property
    def smart_group_uuids(self):
        """Gets the smart_group_uuids of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501

        Gets or sets the list of smart group UUID where update needs to be deployed.  # noqa: E501

        :return: The smart_group_uuids of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._smart_group_uuids

    @smart_group_uuids.setter
    def smart_group_uuids(self, smart_group_uuids):
        """Sets the smart_group_uuids of this DeviceUpdateDeploymentUpdateV1Model.

        Gets or sets the list of smart group UUID where update needs to be deployed.  # noqa: E501

        :param smart_group_uuids: The smart_group_uuids of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and smart_group_uuids is None:
            raise ValueError("Invalid value for `smart_group_uuids`, must not be `None`")  # noqa: E501

        self._smart_group_uuids = smart_group_uuids

    @property
    def notifications(self):
        """Gets the notifications of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501

        Gets or sets the list of notification preferences for the deployment.  # noqa: E501

        :return: The notifications of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501
        :rtype: list[NotificationV1Model]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this DeviceUpdateDeploymentUpdateV1Model.

        Gets or sets the list of notification preferences for the deployment.  # noqa: E501

        :param notifications: The notifications of this DeviceUpdateDeploymentUpdateV1Model.  # noqa: E501
        :type: list[NotificationV1Model]
        """

        self._notifications = notifications

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
        if issubclass(DeviceUpdateDeploymentUpdateV1Model, dict):
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
        if not isinstance(other, DeviceUpdateDeploymentUpdateV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceUpdateDeploymentUpdateV1Model):
            return True

        return self.to_dict() != other.to_dict()
