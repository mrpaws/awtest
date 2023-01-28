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


class WhenToInstallModel(object):
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
        'data_contingencies': 'list[DeploymentByCriteriaModel]',
        'disk_space_required_in_kb': 'int',
        'device_power_required': 'int',
        'ram_required_in_mb': 'int'
    }

    attribute_map = {
        'data_contingencies': 'DataContingencies',
        'disk_space_required_in_kb': 'DiskSpaceRequiredInKb',
        'device_power_required': 'DevicePowerRequired',
        'ram_required_in_mb': 'RamRequiredInMb'
    }

    def __init__(self, data_contingencies=None, disk_space_required_in_kb=None, device_power_required=None, ram_required_in_mb=None, _configuration=None):  # noqa: E501
        """WhenToInstallModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data_contingencies = None
        self._disk_space_required_in_kb = None
        self._device_power_required = None
        self._ram_required_in_mb = None
        self.discriminator = None

        if data_contingencies is not None:
            self.data_contingencies = data_contingencies
        if disk_space_required_in_kb is not None:
            self.disk_space_required_in_kb = disk_space_required_in_kb
        if device_power_required is not None:
            self.device_power_required = device_power_required
        if ram_required_in_mb is not None:
            self.ram_required_in_mb = ram_required_in_mb

    @property
    def data_contingencies(self):
        """Gets the data_contingencies of this WhenToInstallModel.  # noqa: E501

        Gets or sets data Contingencies.  # noqa: E501

        :return: The data_contingencies of this WhenToInstallModel.  # noqa: E501
        :rtype: list[DeploymentByCriteriaModel]
        """
        return self._data_contingencies

    @data_contingencies.setter
    def data_contingencies(self, data_contingencies):
        """Sets the data_contingencies of this WhenToInstallModel.

        Gets or sets data Contingencies.  # noqa: E501

        :param data_contingencies: The data_contingencies of this WhenToInstallModel.  # noqa: E501
        :type: list[DeploymentByCriteriaModel]
        """

        self._data_contingencies = data_contingencies

    @property
    def disk_space_required_in_kb(self):
        """Gets the disk_space_required_in_kb of this WhenToInstallModel.  # noqa: E501

        Gets or sets the disk space required for installation of the package in KB.  # noqa: E501

        :return: The disk_space_required_in_kb of this WhenToInstallModel.  # noqa: E501
        :rtype: int
        """
        return self._disk_space_required_in_kb

    @disk_space_required_in_kb.setter
    def disk_space_required_in_kb(self, disk_space_required_in_kb):
        """Sets the disk_space_required_in_kb of this WhenToInstallModel.

        Gets or sets the disk space required for installation of the package in KB.  # noqa: E501

        :param disk_space_required_in_kb: The disk_space_required_in_kb of this WhenToInstallModel.  # noqa: E501
        :type: int
        """

        self._disk_space_required_in_kb = disk_space_required_in_kb

    @property
    def device_power_required(self):
        """Gets the device_power_required of this WhenToInstallModel.  # noqa: E501

        Gets or sets the device power required for installation of the package. Valid range 0 - 100.  # noqa: E501

        :return: The device_power_required of this WhenToInstallModel.  # noqa: E501
        :rtype: int
        """
        return self._device_power_required

    @device_power_required.setter
    def device_power_required(self, device_power_required):
        """Sets the device_power_required of this WhenToInstallModel.

        Gets or sets the device power required for installation of the package. Valid range 0 - 100.  # noqa: E501

        :param device_power_required: The device_power_required of this WhenToInstallModel.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                device_power_required is not None and device_power_required > 100):  # noqa: E501
            raise ValueError("Invalid value for `device_power_required`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                device_power_required is not None and device_power_required < 0):  # noqa: E501
            raise ValueError("Invalid value for `device_power_required`, must be a value greater than or equal to `0`")  # noqa: E501

        self._device_power_required = device_power_required

    @property
    def ram_required_in_mb(self):
        """Gets the ram_required_in_mb of this WhenToInstallModel.  # noqa: E501

        Gets or sets the RAM required for the installation of the page in MB.  # noqa: E501

        :return: The ram_required_in_mb of this WhenToInstallModel.  # noqa: E501
        :rtype: int
        """
        return self._ram_required_in_mb

    @ram_required_in_mb.setter
    def ram_required_in_mb(self, ram_required_in_mb):
        """Sets the ram_required_in_mb of this WhenToInstallModel.

        Gets or sets the RAM required for the installation of the page in MB.  # noqa: E501

        :param ram_required_in_mb: The ram_required_in_mb of this WhenToInstallModel.  # noqa: E501
        :type: int
        """

        self._ram_required_in_mb = ram_required_in_mb

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
        if issubclass(WhenToInstallModel, dict):
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
        if not isinstance(other, WhenToInstallModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WhenToInstallModel):
            return True

        return self.to_dict() != other.to_dict()
