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


class DeviceEnrollmentProgramDevicesResponseV1Model(object):
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
        'device_friendly_name': 'str',
        'device_serial_number': 'str',
        'device_imei': 'str',
        'device_ownership': 'str',
        'username': 'str',
        'enrollment_status': 'str',
        'device_model': 'str',
        'profile_uuid': 'str',
        'device_asset_number': 'str',
        'organization_group_name': 'str',
        'profile_name': 'str',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'device_friendly_name': 'deviceFriendlyName',
        'device_serial_number': 'deviceSerialNumber',
        'device_imei': 'deviceImei',
        'device_ownership': 'deviceOwnership',
        'username': 'username',
        'enrollment_status': 'enrollmentStatus',
        'device_model': 'deviceModel',
        'profile_uuid': 'profileUuid',
        'device_asset_number': 'deviceAssetNumber',
        'organization_group_name': 'organizationGroupName',
        'profile_name': 'profileName',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, device_friendly_name=None, device_serial_number=None, device_imei=None, device_ownership=None, username=None, enrollment_status=None, device_model=None, profile_uuid=None, device_asset_number=None, organization_group_name=None, profile_name=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """DeviceEnrollmentProgramDevicesResponseV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_friendly_name = None
        self._device_serial_number = None
        self._device_imei = None
        self._device_ownership = None
        self._username = None
        self._enrollment_status = None
        self._device_model = None
        self._profile_uuid = None
        self._device_asset_number = None
        self._organization_group_name = None
        self._profile_name = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if device_friendly_name is not None:
            self.device_friendly_name = device_friendly_name
        if device_serial_number is not None:
            self.device_serial_number = device_serial_number
        if device_imei is not None:
            self.device_imei = device_imei
        if device_ownership is not None:
            self.device_ownership = device_ownership
        if username is not None:
            self.username = username
        if enrollment_status is not None:
            self.enrollment_status = enrollment_status
        if device_model is not None:
            self.device_model = device_model
        if profile_uuid is not None:
            self.profile_uuid = profile_uuid
        if device_asset_number is not None:
            self.device_asset_number = device_asset_number
        if organization_group_name is not None:
            self.organization_group_name = organization_group_name
        if profile_name is not None:
            self.profile_name = profile_name
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def device_friendly_name(self):
        """Gets the device_friendly_name of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        Friendly name of the device.  # noqa: E501

        :return: The device_friendly_name of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_friendly_name

    @device_friendly_name.setter
    def device_friendly_name(self, device_friendly_name):
        """Sets the device_friendly_name of this DeviceEnrollmentProgramDevicesResponseV1Model.

        Friendly name of the device.  # noqa: E501

        :param device_friendly_name: The device_friendly_name of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._device_friendly_name = device_friendly_name

    @property
    def device_serial_number(self):
        """Gets the device_serial_number of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        Serial number of the device.  # noqa: E501

        :return: The device_serial_number of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_serial_number

    @device_serial_number.setter
    def device_serial_number(self, device_serial_number):
        """Sets the device_serial_number of this DeviceEnrollmentProgramDevicesResponseV1Model.

        Serial number of the device.  # noqa: E501

        :param device_serial_number: The device_serial_number of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._device_serial_number = device_serial_number

    @property
    def device_imei(self):
        """Gets the device_imei of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        IMEI number of the device.  # noqa: E501

        :return: The device_imei of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_imei

    @device_imei.setter
    def device_imei(self, device_imei):
        """Sets the device_imei of this DeviceEnrollmentProgramDevicesResponseV1Model.

        IMEI number of the device.  # noqa: E501

        :param device_imei: The device_imei of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._device_imei = device_imei

    @property
    def device_ownership(self):
        """Gets the device_ownership of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        Ownership type for the device  # noqa: E501

        :return: The device_ownership of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_ownership

    @device_ownership.setter
    def device_ownership(self, device_ownership):
        """Sets the device_ownership of this DeviceEnrollmentProgramDevicesResponseV1Model.

        Ownership type for the device  # noqa: E501

        :param device_ownership: The device_ownership of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._device_ownership = device_ownership

    @property
    def username(self):
        """Gets the username of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        The username the device is assigned to.  # noqa: E501

        :return: The username of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DeviceEnrollmentProgramDevicesResponseV1Model.

        The username the device is assigned to.  # noqa: E501

        :param username: The username of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def enrollment_status(self):
        """Gets the enrollment_status of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        Current enrollment status of the device.  # noqa: E501

        :return: The enrollment_status of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_status

    @enrollment_status.setter
    def enrollment_status(self, enrollment_status):
        """Sets the enrollment_status of this DeviceEnrollmentProgramDevicesResponseV1Model.

        Current enrollment status of the device.  # noqa: E501

        :param enrollment_status: The enrollment_status of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._enrollment_status = enrollment_status

    @property
    def device_model(self):
        """Gets the device_model of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        The model of the device  # noqa: E501

        :return: The device_model of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """Sets the device_model of this DeviceEnrollmentProgramDevicesResponseV1Model.

        The model of the device  # noqa: E501

        :param device_model: The device_model of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._device_model = device_model

    @property
    def profile_uuid(self):
        """Gets the profile_uuid of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        UUID of the Device Enrollment Program profile.  # noqa: E501

        :return: The profile_uuid of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._profile_uuid

    @profile_uuid.setter
    def profile_uuid(self, profile_uuid):
        """Sets the profile_uuid of this DeviceEnrollmentProgramDevicesResponseV1Model.

        UUID of the Device Enrollment Program profile.  # noqa: E501

        :param profile_uuid: The profile_uuid of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._profile_uuid = profile_uuid

    @property
    def device_asset_number(self):
        """Gets the device_asset_number of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        Asset number of the device.  # noqa: E501

        :return: The device_asset_number of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_asset_number

    @device_asset_number.setter
    def device_asset_number(self, device_asset_number):
        """Sets the device_asset_number of this DeviceEnrollmentProgramDevicesResponseV1Model.

        Asset number of the device.  # noqa: E501

        :param device_asset_number: The device_asset_number of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._device_asset_number = device_asset_number

    @property
    def organization_group_name(self):
        """Gets the organization_group_name of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        The organization group name the device is assigned to.  # noqa: E501

        :return: The organization_group_name of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_name

    @organization_group_name.setter
    def organization_group_name(self, organization_group_name):
        """Sets the organization_group_name of this DeviceEnrollmentProgramDevicesResponseV1Model.

        The organization group name the device is assigned to.  # noqa: E501

        :param organization_group_name: The organization_group_name of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group_name = organization_group_name

    @property
    def profile_name(self):
        """Gets the profile_name of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        The name of the Device Enrollment Program profile.  # noqa: E501

        :return: The profile_name of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this DeviceEnrollmentProgramDevicesResponseV1Model.

        The name of the Device Enrollment Program profile.  # noqa: E501

        :param profile_name: The profile_name of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    @property
    def id(self):
        """Gets the id of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceEnrollmentProgramDevicesResponseV1Model.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DeviceEnrollmentProgramDevicesResponseV1Model.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this DeviceEnrollmentProgramDevicesResponseV1Model.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(DeviceEnrollmentProgramDevicesResponseV1Model, dict):
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
        if not isinstance(other, DeviceEnrollmentProgramDevicesResponseV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceEnrollmentProgramDevicesResponseV1Model):
            return True

        return self.to_dict() != other.to_dict()
