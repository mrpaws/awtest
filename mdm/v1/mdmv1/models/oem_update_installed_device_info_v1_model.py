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


class OemUpdateInstalledDeviceInfoV1Model(object):
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
        'device_uuid': 'str',
        'device_friendly_name': 'str',
        'user_uuid': 'str',
        'user_name': 'str',
        'device_platform': 'str',
        'device_os': 'str',
        'device_model': 'str',
        'user_phone_number': 'str',
        'organization_group_uuid': 'str',
        'organization_group_name': 'str',
        'name': 'str',
        'device_ownership_abbreviation': 'str',
        'device_type': 'int'
    }

    attribute_map = {
        'device_uuid': 'device_uuid',
        'device_friendly_name': 'device_friendly_name',
        'user_uuid': 'user_uuid',
        'user_name': 'user_name',
        'device_platform': 'device_platform',
        'device_os': 'device_os',
        'device_model': 'device_model',
        'user_phone_number': 'user_phone_number',
        'organization_group_uuid': 'organization_group_uuid',
        'organization_group_name': 'organization_group_name',
        'name': 'name',
        'device_ownership_abbreviation': 'deviceOwnershipAbbreviation',
        'device_type': 'device_type'
    }

    def __init__(self, device_uuid=None, device_friendly_name=None, user_uuid=None, user_name=None, device_platform=None, device_os=None, device_model=None, user_phone_number=None, organization_group_uuid=None, organization_group_name=None, name=None, device_ownership_abbreviation=None, device_type=None, _configuration=None):  # noqa: E501
        """OemUpdateInstalledDeviceInfoV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_uuid = None
        self._device_friendly_name = None
        self._user_uuid = None
        self._user_name = None
        self._device_platform = None
        self._device_os = None
        self._device_model = None
        self._user_phone_number = None
        self._organization_group_uuid = None
        self._organization_group_name = None
        self._name = None
        self._device_ownership_abbreviation = None
        self._device_type = None
        self.discriminator = None

        if device_uuid is not None:
            self.device_uuid = device_uuid
        if device_friendly_name is not None:
            self.device_friendly_name = device_friendly_name
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if user_name is not None:
            self.user_name = user_name
        if device_platform is not None:
            self.device_platform = device_platform
        if device_os is not None:
            self.device_os = device_os
        if device_model is not None:
            self.device_model = device_model
        if user_phone_number is not None:
            self.user_phone_number = user_phone_number
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if organization_group_name is not None:
            self.organization_group_name = organization_group_name
        if name is not None:
            self.name = name
        if device_ownership_abbreviation is not None:
            self.device_ownership_abbreviation = device_ownership_abbreviation
        if device_type is not None:
            self.device_type = device_type

    @property
    def device_uuid(self):
        """Gets the device_uuid of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        Device UUID.  # noqa: E501

        :return: The device_uuid of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_uuid

    @device_uuid.setter
    def device_uuid(self, device_uuid):
        """Sets the device_uuid of this OemUpdateInstalledDeviceInfoV1Model.

        Device UUID.  # noqa: E501

        :param device_uuid: The device_uuid of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._device_uuid = device_uuid

    @property
    def device_friendly_name(self):
        """Gets the device_friendly_name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        Friendly Name of the update received from the device.  # noqa: E501

        :return: The device_friendly_name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_friendly_name

    @device_friendly_name.setter
    def device_friendly_name(self, device_friendly_name):
        """Sets the device_friendly_name of this OemUpdateInstalledDeviceInfoV1Model.

        Friendly Name of the update received from the device.  # noqa: E501

        :param device_friendly_name: The device_friendly_name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._device_friendly_name = device_friendly_name

    @property
    def user_uuid(self):
        """Gets the user_uuid of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        User UUID.  # noqa: E501

        :return: The user_uuid of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this OemUpdateInstalledDeviceInfoV1Model.

        User UUID.  # noqa: E501

        :param user_uuid: The user_uuid of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def user_name(self):
        """Gets the user_name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        User name.  # noqa: E501

        :return: The user_name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this OemUpdateInstalledDeviceInfoV1Model.

        User name.  # noqa: E501

        :param user_name: The user_name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def device_platform(self):
        """Gets the device_platform of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        Device Platform.  # noqa: E501

        :return: The device_platform of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_platform

    @device_platform.setter
    def device_platform(self, device_platform):
        """Sets the device_platform of this OemUpdateInstalledDeviceInfoV1Model.

        Device Platform.  # noqa: E501

        :param device_platform: The device_platform of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._device_platform = device_platform

    @property
    def device_os(self):
        """Gets the device_os of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        Device OS.  # noqa: E501

        :return: The device_os of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_os

    @device_os.setter
    def device_os(self, device_os):
        """Sets the device_os of this OemUpdateInstalledDeviceInfoV1Model.

        Device OS.  # noqa: E501

        :param device_os: The device_os of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._device_os = device_os

    @property
    def device_model(self):
        """Gets the device_model of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        Device Model.  # noqa: E501

        :return: The device_model of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """Sets the device_model of this OemUpdateInstalledDeviceInfoV1Model.

        Device Model.  # noqa: E501

        :param device_model: The device_model of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._device_model = device_model

    @property
    def user_phone_number(self):
        """Gets the user_phone_number of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        Phone number.  # noqa: E501

        :return: The user_phone_number of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._user_phone_number

    @user_phone_number.setter
    def user_phone_number(self, user_phone_number):
        """Sets the user_phone_number of this OemUpdateInstalledDeviceInfoV1Model.

        Phone number.  # noqa: E501

        :param user_phone_number: The user_phone_number of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._user_phone_number = user_phone_number

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        Organization group UUID to perform the operation on.  # noqa: E501

        :return: The organization_group_uuid of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this OemUpdateInstalledDeviceInfoV1Model.

        Organization group UUID to perform the operation on.  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def organization_group_name(self):
        """Gets the organization_group_name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        Organization Group.  # noqa: E501

        :return: The organization_group_name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_name

    @organization_group_name.setter
    def organization_group_name(self, organization_group_name):
        """Sets the organization_group_name of this OemUpdateInstalledDeviceInfoV1Model.

        Organization Group.  # noqa: E501

        :param organization_group_name: The organization_group_name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group_name = organization_group_name

    @property
    def name(self):
        """Gets the name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        Name of the update received from the device.  # noqa: E501

        :return: The name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OemUpdateInstalledDeviceInfoV1Model.

        Name of the update received from the device.  # noqa: E501

        :param name: The name of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def device_ownership_abbreviation(self):
        """Gets the device_ownership_abbreviation of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        Device Ownership Abbreviation.  # noqa: E501

        :return: The device_ownership_abbreviation of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_ownership_abbreviation

    @device_ownership_abbreviation.setter
    def device_ownership_abbreviation(self, device_ownership_abbreviation):
        """Sets the device_ownership_abbreviation of this OemUpdateInstalledDeviceInfoV1Model.

        Device Ownership Abbreviation.  # noqa: E501

        :param device_ownership_abbreviation: The device_ownership_abbreviation of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._device_ownership_abbreviation = device_ownership_abbreviation

    @property
    def device_type(self):
        """Gets the device_type of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501

        Device Type.  # noqa: E501

        :return: The device_type of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this OemUpdateInstalledDeviceInfoV1Model.

        Device Type.  # noqa: E501

        :param device_type: The device_type of this OemUpdateInstalledDeviceInfoV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 100, 101, 102, 103, 104, 105, 200, 201, 1000]  # noqa: E501
        if (self._configuration.client_side_validation and
                device_type not in allowed_values):
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

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
        if issubclass(OemUpdateInstalledDeviceInfoV1Model, dict):
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
        if not isinstance(other, OemUpdateInstalledDeviceInfoV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OemUpdateInstalledDeviceInfoV1Model):
            return True

        return self.to_dict() != other.to_dict()
