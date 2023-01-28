# coding: utf-8

"""
    MAM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv2.configuration import Configuration


class BranchCacheStatisticsSummaryModel(object):
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
        'total_devices_branchcache_mode_enabled': 'int',
        'total_devices_utilized_branchcache': 'int',
        'total_devices_not_utilized_branchcache': 'int',
        'total_device_count': 'int',
        'total_cache_bytes': 'int',
        'total_server_bytes': 'int',
        'total_savings_percent': 'int'
    }

    attribute_map = {
        'total_devices_branchcache_mode_enabled': 'total_devices_branchcache_mode_enabled',
        'total_devices_utilized_branchcache': 'total_devices_utilized_branchcache',
        'total_devices_not_utilized_branchcache': 'total_devices_not_utilized_branchcache',
        'total_device_count': 'total_device_count',
        'total_cache_bytes': 'total_cache_bytes',
        'total_server_bytes': 'total_server_bytes',
        'total_savings_percent': 'total_savings_percent'
    }

    def __init__(self, total_devices_branchcache_mode_enabled=None, total_devices_utilized_branchcache=None, total_devices_not_utilized_branchcache=None, total_device_count=None, total_cache_bytes=None, total_server_bytes=None, total_savings_percent=None, _configuration=None):  # noqa: E501
        """BranchCacheStatisticsSummaryModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._total_devices_branchcache_mode_enabled = None
        self._total_devices_utilized_branchcache = None
        self._total_devices_not_utilized_branchcache = None
        self._total_device_count = None
        self._total_cache_bytes = None
        self._total_server_bytes = None
        self._total_savings_percent = None
        self.discriminator = None

        if total_devices_branchcache_mode_enabled is not None:
            self.total_devices_branchcache_mode_enabled = total_devices_branchcache_mode_enabled
        if total_devices_utilized_branchcache is not None:
            self.total_devices_utilized_branchcache = total_devices_utilized_branchcache
        if total_devices_not_utilized_branchcache is not None:
            self.total_devices_not_utilized_branchcache = total_devices_not_utilized_branchcache
        if total_device_count is not None:
            self.total_device_count = total_device_count
        if total_cache_bytes is not None:
            self.total_cache_bytes = total_cache_bytes
        if total_server_bytes is not None:
            self.total_server_bytes = total_server_bytes
        if total_savings_percent is not None:
            self.total_savings_percent = total_savings_percent

    @property
    def total_devices_branchcache_mode_enabled(self):
        """Gets the total_devices_branchcache_mode_enabled of this BranchCacheStatisticsSummaryModel.  # noqa: E501

        Total number of devices with BranchCache mode enabled i.e. BranchCache mode on device is distributed/local/hosted  # noqa: E501

        :return: The total_devices_branchcache_mode_enabled of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._total_devices_branchcache_mode_enabled

    @total_devices_branchcache_mode_enabled.setter
    def total_devices_branchcache_mode_enabled(self, total_devices_branchcache_mode_enabled):
        """Sets the total_devices_branchcache_mode_enabled of this BranchCacheStatisticsSummaryModel.

        Total number of devices with BranchCache mode enabled i.e. BranchCache mode on device is distributed/local/hosted  # noqa: E501

        :param total_devices_branchcache_mode_enabled: The total_devices_branchcache_mode_enabled of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :type: int
        """

        self._total_devices_branchcache_mode_enabled = total_devices_branchcache_mode_enabled

    @property
    def total_devices_utilized_branchcache(self):
        """Gets the total_devices_utilized_branchcache of this BranchCacheStatisticsSummaryModel.  # noqa: E501

        Total number of devices that utilized BranchCache in the application deployments i.e. application bytes from cache/peers was greater than zero for those devices.  # noqa: E501

        :return: The total_devices_utilized_branchcache of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._total_devices_utilized_branchcache

    @total_devices_utilized_branchcache.setter
    def total_devices_utilized_branchcache(self, total_devices_utilized_branchcache):
        """Sets the total_devices_utilized_branchcache of this BranchCacheStatisticsSummaryModel.

        Total number of devices that utilized BranchCache in the application deployments i.e. application bytes from cache/peers was greater than zero for those devices.  # noqa: E501

        :param total_devices_utilized_branchcache: The total_devices_utilized_branchcache of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :type: int
        """

        self._total_devices_utilized_branchcache = total_devices_utilized_branchcache

    @property
    def total_devices_not_utilized_branchcache(self):
        """Gets the total_devices_not_utilized_branchcache of this BranchCacheStatisticsSummaryModel.  # noqa: E501

        Total number of devices that did not utilize BranchCache in the application deployments i.e. application bytes from cache/peers was equal to zero for those devices.  # noqa: E501

        :return: The total_devices_not_utilized_branchcache of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._total_devices_not_utilized_branchcache

    @total_devices_not_utilized_branchcache.setter
    def total_devices_not_utilized_branchcache(self, total_devices_not_utilized_branchcache):
        """Sets the total_devices_not_utilized_branchcache of this BranchCacheStatisticsSummaryModel.

        Total number of devices that did not utilize BranchCache in the application deployments i.e. application bytes from cache/peers was equal to zero for those devices.  # noqa: E501

        :param total_devices_not_utilized_branchcache: The total_devices_not_utilized_branchcache of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :type: int
        """

        self._total_devices_not_utilized_branchcache = total_devices_not_utilized_branchcache

    @property
    def total_device_count(self):
        """Gets the total_device_count of this BranchCacheStatisticsSummaryModel.  # noqa: E501

        Total number of devices that have the applications installed.  # noqa: E501

        :return: The total_device_count of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._total_device_count

    @total_device_count.setter
    def total_device_count(self, total_device_count):
        """Sets the total_device_count of this BranchCacheStatisticsSummaryModel.

        Total number of devices that have the applications installed.  # noqa: E501

        :param total_device_count: The total_device_count of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :type: int
        """

        self._total_device_count = total_device_count

    @property
    def total_cache_bytes(self):
        """Gets the total_cache_bytes of this BranchCacheStatisticsSummaryModel.  # noqa: E501

        Total number of bytes from the cache/peers for the application downloads for all devices.  # noqa: E501

        :return: The total_cache_bytes of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._total_cache_bytes

    @total_cache_bytes.setter
    def total_cache_bytes(self, total_cache_bytes):
        """Sets the total_cache_bytes of this BranchCacheStatisticsSummaryModel.

        Total number of bytes from the cache/peers for the application downloads for all devices.  # noqa: E501

        :param total_cache_bytes: The total_cache_bytes of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :type: int
        """

        self._total_cache_bytes = total_cache_bytes

    @property
    def total_server_bytes(self):
        """Gets the total_server_bytes of this BranchCacheStatisticsSummaryModel.  # noqa: E501

        Total number of bytes from the server for the application downloads for all devices.  # noqa: E501

        :return: The total_server_bytes of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._total_server_bytes

    @total_server_bytes.setter
    def total_server_bytes(self, total_server_bytes):
        """Sets the total_server_bytes of this BranchCacheStatisticsSummaryModel.

        Total number of bytes from the server for the application downloads for all devices.  # noqa: E501

        :param total_server_bytes: The total_server_bytes of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :type: int
        """

        self._total_server_bytes = total_server_bytes

    @property
    def total_savings_percent(self):
        """Gets the total_savings_percent of this BranchCacheStatisticsSummaryModel.  # noqa: E501

        The savings as a percentage that is the bytes downloaded from the cache/peers over total application sizes for the device(s).  # noqa: E501

        :return: The total_savings_percent of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._total_savings_percent

    @total_savings_percent.setter
    def total_savings_percent(self, total_savings_percent):
        """Sets the total_savings_percent of this BranchCacheStatisticsSummaryModel.

        The savings as a percentage that is the bytes downloaded from the cache/peers over total application sizes for the device(s).  # noqa: E501

        :param total_savings_percent: The total_savings_percent of this BranchCacheStatisticsSummaryModel.  # noqa: E501
        :type: int
        """

        self._total_savings_percent = total_savings_percent

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
        if issubclass(BranchCacheStatisticsSummaryModel, dict):
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
        if not isinstance(other, BranchCacheStatisticsSummaryModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BranchCacheStatisticsSummaryModel):
            return True

        return self.to_dict() != other.to_dict()