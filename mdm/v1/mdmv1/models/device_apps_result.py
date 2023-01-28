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


class DeviceAppsResult(object):
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
        'device_apps': 'list[DeviceApplicationInfo]',
        'page': 'int',
        'page_size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'device_apps': 'DeviceApps',
        'page': 'Page',
        'page_size': 'PageSize',
        'total': 'Total'
    }

    def __init__(self, device_apps=None, page=None, page_size=None, total=None, _configuration=None):  # noqa: E501
        """DeviceAppsResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_apps = None
        self._page = None
        self._page_size = None
        self._total = None
        self.discriminator = None

        if device_apps is not None:
            self.device_apps = device_apps
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total is not None:
            self.total = total

    @property
    def device_apps(self):
        """Gets the device_apps of this DeviceAppsResult.  # noqa: E501

        Gets or sets list of application details for the device.  # noqa: E501

        :return: The device_apps of this DeviceAppsResult.  # noqa: E501
        :rtype: list[DeviceApplicationInfo]
        """
        return self._device_apps

    @device_apps.setter
    def device_apps(self, device_apps):
        """Sets the device_apps of this DeviceAppsResult.

        Gets or sets list of application details for the device.  # noqa: E501

        :param device_apps: The device_apps of this DeviceAppsResult.  # noqa: E501
        :type: list[DeviceApplicationInfo]
        """

        self._device_apps = device_apps

    @property
    def page(self):
        """Gets the page of this DeviceAppsResult.  # noqa: E501


        :return: The page of this DeviceAppsResult.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this DeviceAppsResult.


        :param page: The page of this DeviceAppsResult.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this DeviceAppsResult.  # noqa: E501


        :return: The page_size of this DeviceAppsResult.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DeviceAppsResult.


        :param page_size: The page_size of this DeviceAppsResult.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total(self):
        """Gets the total of this DeviceAppsResult.  # noqa: E501


        :return: The total of this DeviceAppsResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DeviceAppsResult.


        :param total: The total of this DeviceAppsResult.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(DeviceAppsResult, dict):
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
        if not isinstance(other, DeviceAppsResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceAppsResult):
            return True

        return self.to_dict() != other.to_dict()