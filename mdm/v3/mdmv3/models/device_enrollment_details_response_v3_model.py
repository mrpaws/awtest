# coding: utf-8

"""
    MDM API V3

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv3.configuration import Configuration


class DeviceEnrollmentDetailsResponseV3Model(object):
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
        'enrollment_status': 'int',
        'compliance_status': 'int',
        'enrollment_timestamp': 'datetime',
        'last_seen_timestamp': 'datetime',
        'ownership': 'int',
        'organization_group_uuid': 'str',
        'organization_group_name': 'str',
        'enrollment_user_name': 'str',
        'enrollment_user_uuid': 'str',
        'enrollment_user_email_address': 'str',
        'managed_by': 'int'
    }

    attribute_map = {
        'enrollment_status': 'enrollment_status',
        'compliance_status': 'compliance_status',
        'enrollment_timestamp': 'enrollment_timestamp',
        'last_seen_timestamp': 'last_seen_timestamp',
        'ownership': 'ownership',
        'organization_group_uuid': 'organization_group_uuid',
        'organization_group_name': 'organization_group_name',
        'enrollment_user_name': 'enrollment_user_name',
        'enrollment_user_uuid': 'enrollment_user_uuid',
        'enrollment_user_email_address': 'enrollment_user_email_address',
        'managed_by': 'managed_by'
    }

    def __init__(self, enrollment_status=None, compliance_status=None, enrollment_timestamp=None, last_seen_timestamp=None, ownership=None, organization_group_uuid=None, organization_group_name=None, enrollment_user_name=None, enrollment_user_uuid=None, enrollment_user_email_address=None, managed_by=None, _configuration=None):  # noqa: E501
        """DeviceEnrollmentDetailsResponseV3Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enrollment_status = None
        self._compliance_status = None
        self._enrollment_timestamp = None
        self._last_seen_timestamp = None
        self._ownership = None
        self._organization_group_uuid = None
        self._organization_group_name = None
        self._enrollment_user_name = None
        self._enrollment_user_uuid = None
        self._enrollment_user_email_address = None
        self._managed_by = None
        self.discriminator = None

        if enrollment_status is not None:
            self.enrollment_status = enrollment_status
        if compliance_status is not None:
            self.compliance_status = compliance_status
        if enrollment_timestamp is not None:
            self.enrollment_timestamp = enrollment_timestamp
        if last_seen_timestamp is not None:
            self.last_seen_timestamp = last_seen_timestamp
        if ownership is not None:
            self.ownership = ownership
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if organization_group_name is not None:
            self.organization_group_name = organization_group_name
        if enrollment_user_name is not None:
            self.enrollment_user_name = enrollment_user_name
        if enrollment_user_uuid is not None:
            self.enrollment_user_uuid = enrollment_user_uuid
        if enrollment_user_email_address is not None:
            self.enrollment_user_email_address = enrollment_user_email_address
        if managed_by is not None:
            self.managed_by = managed_by

    @property
    def enrollment_status(self):
        """Gets the enrollment_status of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501

        Enrollment status of the device.  # noqa: E501

        :return: The enrollment_status of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :rtype: int
        """
        return self._enrollment_status

    @enrollment_status.setter
    def enrollment_status(self, enrollment_status):
        """Sets the enrollment_status of this DeviceEnrollmentDetailsResponseV3Model.

        Enrollment status of the device.  # noqa: E501

        :param enrollment_status: The enrollment_status of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16]  # noqa: E501
        if (self._configuration.client_side_validation and
                enrollment_status not in allowed_values):
            raise ValueError(
                "Invalid value for `enrollment_status` ({0}), must be one of {1}"  # noqa: E501
                .format(enrollment_status, allowed_values)
            )

        self._enrollment_status = enrollment_status

    @property
    def compliance_status(self):
        """Gets the compliance_status of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501

        Compliance status of the device.  # noqa: E501

        :return: The compliance_status of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :rtype: int
        """
        return self._compliance_status

    @compliance_status.setter
    def compliance_status(self, compliance_status):
        """Sets the compliance_status of this DeviceEnrollmentDetailsResponseV3Model.

        Compliance status of the device.  # noqa: E501

        :param compliance_status: The compliance_status of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # noqa: E501
        if (self._configuration.client_side_validation and
                compliance_status not in allowed_values):
            raise ValueError(
                "Invalid value for `compliance_status` ({0}), must be one of {1}"  # noqa: E501
                .format(compliance_status, allowed_values)
            )

        self._compliance_status = compliance_status

    @property
    def enrollment_timestamp(self):
        """Gets the enrollment_timestamp of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501

        Date-Time of last enrollment date.  # noqa: E501

        :return: The enrollment_timestamp of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :rtype: datetime
        """
        return self._enrollment_timestamp

    @enrollment_timestamp.setter
    def enrollment_timestamp(self, enrollment_timestamp):
        """Sets the enrollment_timestamp of this DeviceEnrollmentDetailsResponseV3Model.

        Date-Time of last enrollment date.  # noqa: E501

        :param enrollment_timestamp: The enrollment_timestamp of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :type: datetime
        """

        self._enrollment_timestamp = enrollment_timestamp

    @property
    def last_seen_timestamp(self):
        """Gets the last_seen_timestamp of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501

        Date Time when the device last reported any status.  # noqa: E501

        :return: The last_seen_timestamp of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen_timestamp

    @last_seen_timestamp.setter
    def last_seen_timestamp(self, last_seen_timestamp):
        """Sets the last_seen_timestamp of this DeviceEnrollmentDetailsResponseV3Model.

        Date Time when the device last reported any status.  # noqa: E501

        :param last_seen_timestamp: The last_seen_timestamp of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :type: datetime
        """

        self._last_seen_timestamp = last_seen_timestamp

    @property
    def ownership(self):
        """Gets the ownership of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501

        Ownership type of the device.  # noqa: E501

        :return: The ownership of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :rtype: int
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        """Sets the ownership of this DeviceEnrollmentDetailsResponseV3Model.

        Ownership type of the device.  # noqa: E501

        :param ownership: The ownership of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4]  # noqa: E501
        if (self._configuration.client_side_validation and
                ownership not in allowed_values):
            raise ValueError(
                "Invalid value for `ownership` ({0}), must be one of {1}"  # noqa: E501
                .format(ownership, allowed_values)
            )

        self._ownership = ownership

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501

        UUID of the organization group.  # noqa: E501

        :return: The organization_group_uuid of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this DeviceEnrollmentDetailsResponseV3Model.

        UUID of the organization group.  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def organization_group_name(self):
        """Gets the organization_group_name of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501

        Organization group name where the device is enrolled.  # noqa: E501

        :return: The organization_group_name of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_name

    @organization_group_name.setter
    def organization_group_name(self, organization_group_name):
        """Sets the organization_group_name of this DeviceEnrollmentDetailsResponseV3Model.

        Organization group name where the device is enrolled.  # noqa: E501

        :param organization_group_name: The organization_group_name of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :type: str
        """

        self._organization_group_name = organization_group_name

    @property
    def enrollment_user_name(self):
        """Gets the enrollment_user_name of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501

        Name of the user device is enrolled under.  # noqa: E501

        :return: The enrollment_user_name of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_user_name

    @enrollment_user_name.setter
    def enrollment_user_name(self, enrollment_user_name):
        """Sets the enrollment_user_name of this DeviceEnrollmentDetailsResponseV3Model.

        Name of the user device is enrolled under.  # noqa: E501

        :param enrollment_user_name: The enrollment_user_name of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :type: str
        """

        self._enrollment_user_name = enrollment_user_name

    @property
    def enrollment_user_uuid(self):
        """Gets the enrollment_user_uuid of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501

        UUID of the user device is enrolled under.  # noqa: E501

        :return: The enrollment_user_uuid of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_user_uuid

    @enrollment_user_uuid.setter
    def enrollment_user_uuid(self, enrollment_user_uuid):
        """Sets the enrollment_user_uuid of this DeviceEnrollmentDetailsResponseV3Model.

        UUID of the user device is enrolled under.  # noqa: E501

        :param enrollment_user_uuid: The enrollment_user_uuid of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :type: str
        """

        self._enrollment_user_uuid = enrollment_user_uuid

    @property
    def enrollment_user_email_address(self):
        """Gets the enrollment_user_email_address of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501

        E-mail address of the user the device is enrolled under.  # noqa: E501

        :return: The enrollment_user_email_address of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_user_email_address

    @enrollment_user_email_address.setter
    def enrollment_user_email_address(self, enrollment_user_email_address):
        """Sets the enrollment_user_email_address of this DeviceEnrollmentDetailsResponseV3Model.

        E-mail address of the user the device is enrolled under.  # noqa: E501

        :param enrollment_user_email_address: The enrollment_user_email_address of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :type: str
        """

        self._enrollment_user_email_address = enrollment_user_email_address

    @property
    def managed_by(self):
        """Gets the managed_by of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501

        Device managed by.  # noqa: E501

        :return: The managed_by of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :rtype: int
        """
        return self._managed_by

    @managed_by.setter
    def managed_by(self, managed_by):
        """Sets the managed_by of this DeviceEnrollmentDetailsResponseV3Model.

        Device managed by.  # noqa: E501

        :param managed_by: The managed_by of this DeviceEnrollmentDetailsResponseV3Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6]  # noqa: E501
        if (self._configuration.client_side_validation and
                managed_by not in allowed_values):
            raise ValueError(
                "Invalid value for `managed_by` ({0}), must be one of {1}"  # noqa: E501
                .format(managed_by, allowed_values)
            )

        self._managed_by = managed_by

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
        if issubclass(DeviceEnrollmentDetailsResponseV3Model, dict):
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
        if not isinstance(other, DeviceEnrollmentDetailsResponseV3Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceEnrollmentDetailsResponseV3Model):
            return True

        return self.to_dict() != other.to_dict()