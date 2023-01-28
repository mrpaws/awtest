# coding: utf-8

"""
    System API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv1.configuration import Configuration


class LicenseModel(object):
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
        'multi_license_key': 'str',
        'quantity_purchased': 'int',
        'effective_date': 'datetime',
        'expiration_date': 'datetime',
        'overage_tolerance': 'int',
        'license_type': 'int',
        'shutdown_mode': 'int',
        'warning_date': 'datetime',
        'lockout_date': 'datetime',
        'devices_per_user': 'int',
        'organization_group_id': 'int',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'multi_license_key': 'MultiLicenseKey',
        'quantity_purchased': 'QuantityPurchased',
        'effective_date': 'EffectiveDate',
        'expiration_date': 'ExpirationDate',
        'overage_tolerance': 'OverageTolerance',
        'license_type': 'LicenseType',
        'shutdown_mode': 'ShutdownMode',
        'warning_date': 'WarningDate',
        'lockout_date': 'LockoutDate',
        'devices_per_user': 'DevicesPerUser',
        'organization_group_id': 'OrganizationGroupId',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, multi_license_key=None, quantity_purchased=None, effective_date=None, expiration_date=None, overage_tolerance=None, license_type=None, shutdown_mode=None, warning_date=None, lockout_date=None, devices_per_user=None, organization_group_id=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """LicenseModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._multi_license_key = None
        self._quantity_purchased = None
        self._effective_date = None
        self._expiration_date = None
        self._overage_tolerance = None
        self._license_type = None
        self._shutdown_mode = None
        self._warning_date = None
        self._lockout_date = None
        self._devices_per_user = None
        self._organization_group_id = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if multi_license_key is not None:
            self.multi_license_key = multi_license_key
        if quantity_purchased is not None:
            self.quantity_purchased = quantity_purchased
        if effective_date is not None:
            self.effective_date = effective_date
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if overage_tolerance is not None:
            self.overage_tolerance = overage_tolerance
        if license_type is not None:
            self.license_type = license_type
        if shutdown_mode is not None:
            self.shutdown_mode = shutdown_mode
        if warning_date is not None:
            self.warning_date = warning_date
        if lockout_date is not None:
            self.lockout_date = lockout_date
        if devices_per_user is not None:
            self.devices_per_user = devices_per_user
        if organization_group_id is not None:
            self.organization_group_id = organization_group_id
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def multi_license_key(self):
        """Gets the multi_license_key of this LicenseModel.  # noqa: E501

        Gets or sets multi license key.  # noqa: E501

        :return: The multi_license_key of this LicenseModel.  # noqa: E501
        :rtype: str
        """
        return self._multi_license_key

    @multi_license_key.setter
    def multi_license_key(self, multi_license_key):
        """Sets the multi_license_key of this LicenseModel.

        Gets or sets multi license key.  # noqa: E501

        :param multi_license_key: The multi_license_key of this LicenseModel.  # noqa: E501
        :type: str
        """

        self._multi_license_key = multi_license_key

    @property
    def quantity_purchased(self):
        """Gets the quantity_purchased of this LicenseModel.  # noqa: E501

        Gets or sets quantity purchased.  # noqa: E501

        :return: The quantity_purchased of this LicenseModel.  # noqa: E501
        :rtype: int
        """
        return self._quantity_purchased

    @quantity_purchased.setter
    def quantity_purchased(self, quantity_purchased):
        """Sets the quantity_purchased of this LicenseModel.

        Gets or sets quantity purchased.  # noqa: E501

        :param quantity_purchased: The quantity_purchased of this LicenseModel.  # noqa: E501
        :type: int
        """

        self._quantity_purchased = quantity_purchased

    @property
    def effective_date(self):
        """Gets the effective_date of this LicenseModel.  # noqa: E501

        Gets or sets effective date of license.  # noqa: E501

        :return: The effective_date of this LicenseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this LicenseModel.

        Gets or sets effective date of license.  # noqa: E501

        :param effective_date: The effective_date of this LicenseModel.  # noqa: E501
        :type: datetime
        """

        self._effective_date = effective_date

    @property
    def expiration_date(self):
        """Gets the expiration_date of this LicenseModel.  # noqa: E501

        Gets or sets expiration date of license.  # noqa: E501

        :return: The expiration_date of this LicenseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this LicenseModel.

        Gets or sets expiration date of license.  # noqa: E501

        :param expiration_date: The expiration_date of this LicenseModel.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def overage_tolerance(self):
        """Gets the overage_tolerance of this LicenseModel.  # noqa: E501

        Gets or sets overage tolerance of license.  # noqa: E501

        :return: The overage_tolerance of this LicenseModel.  # noqa: E501
        :rtype: int
        """
        return self._overage_tolerance

    @overage_tolerance.setter
    def overage_tolerance(self, overage_tolerance):
        """Sets the overage_tolerance of this LicenseModel.

        Gets or sets overage tolerance of license.  # noqa: E501

        :param overage_tolerance: The overage_tolerance of this LicenseModel.  # noqa: E501
        :type: int
        """

        self._overage_tolerance = overage_tolerance

    @property
    def license_type(self):
        """Gets the license_type of this LicenseModel.  # noqa: E501

        Gets or sets license type.  # noqa: E501

        :return: The license_type of this LicenseModel.  # noqa: E501
        :rtype: int
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """Sets the license_type of this LicenseModel.

        Gets or sets license type.  # noqa: E501

        :param license_type: The license_type of this LicenseModel.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4, 5]  # noqa: E501
        if (self._configuration.client_side_validation and
                license_type not in allowed_values):
            raise ValueError(
                "Invalid value for `license_type` ({0}), must be one of {1}"  # noqa: E501
                .format(license_type, allowed_values)
            )

        self._license_type = license_type

    @property
    def shutdown_mode(self):
        """Gets the shutdown_mode of this LicenseModel.  # noqa: E501

        Gets or sets shutdown mode of license.  # noqa: E501

        :return: The shutdown_mode of this LicenseModel.  # noqa: E501
        :rtype: int
        """
        return self._shutdown_mode

    @shutdown_mode.setter
    def shutdown_mode(self, shutdown_mode):
        """Sets the shutdown_mode of this LicenseModel.

        Gets or sets shutdown mode of license.  # noqa: E501

        :param shutdown_mode: The shutdown_mode of this LicenseModel.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if (self._configuration.client_side_validation and
                shutdown_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `shutdown_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(shutdown_mode, allowed_values)
            )

        self._shutdown_mode = shutdown_mode

    @property
    def warning_date(self):
        """Gets the warning_date of this LicenseModel.  # noqa: E501

        Gets or sets warning date for the license.  # noqa: E501

        :return: The warning_date of this LicenseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._warning_date

    @warning_date.setter
    def warning_date(self, warning_date):
        """Sets the warning_date of this LicenseModel.

        Gets or sets warning date for the license.  # noqa: E501

        :param warning_date: The warning_date of this LicenseModel.  # noqa: E501
        :type: datetime
        """

        self._warning_date = warning_date

    @property
    def lockout_date(self):
        """Gets the lockout_date of this LicenseModel.  # noqa: E501

        Gets or sets lockout date for the license.  # noqa: E501

        :return: The lockout_date of this LicenseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._lockout_date

    @lockout_date.setter
    def lockout_date(self, lockout_date):
        """Sets the lockout_date of this LicenseModel.

        Gets or sets lockout date for the license.  # noqa: E501

        :param lockout_date: The lockout_date of this LicenseModel.  # noqa: E501
        :type: datetime
        """

        self._lockout_date = lockout_date

    @property
    def devices_per_user(self):
        """Gets the devices_per_user of this LicenseModel.  # noqa: E501

        Gets or sets devices per user for the license.  # noqa: E501

        :return: The devices_per_user of this LicenseModel.  # noqa: E501
        :rtype: int
        """
        return self._devices_per_user

    @devices_per_user.setter
    def devices_per_user(self, devices_per_user):
        """Sets the devices_per_user of this LicenseModel.

        Gets or sets devices per user for the license.  # noqa: E501

        :param devices_per_user: The devices_per_user of this LicenseModel.  # noqa: E501
        :type: int
        """

        self._devices_per_user = devices_per_user

    @property
    def organization_group_id(self):
        """Gets the organization_group_id of this LicenseModel.  # noqa: E501

        Gets or sets organization group id against which license is to be added.  # noqa: E501

        :return: The organization_group_id of this LicenseModel.  # noqa: E501
        :rtype: int
        """
        return self._organization_group_id

    @organization_group_id.setter
    def organization_group_id(self, organization_group_id):
        """Sets the organization_group_id of this LicenseModel.

        Gets or sets organization group id against which license is to be added.  # noqa: E501

        :param organization_group_id: The organization_group_id of this LicenseModel.  # noqa: E501
        :type: int
        """

        self._organization_group_id = organization_group_id

    @property
    def id(self):
        """Gets the id of this LicenseModel.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this LicenseModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LicenseModel.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this LicenseModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this LicenseModel.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this LicenseModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this LicenseModel.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this LicenseModel.  # noqa: E501
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
        if issubclass(LicenseModel, dict):
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
        if not isinstance(other, LicenseModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicenseModel):
            return True

        return self.to_dict() != other.to_dict()