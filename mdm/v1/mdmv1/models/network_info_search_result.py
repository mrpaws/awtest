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


class NetworkInfoSearchResult(object):
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
        'device_network_details': 'list[DeviceNetworkSearchDetails]',
        'page': 'int',
        'page_size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'device_network_details': 'DeviceNetworkDetails',
        'page': 'Page',
        'page_size': 'PageSize',
        'total': 'Total'
    }

    def __init__(self, device_network_details=None, page=None, page_size=None, total=None, _configuration=None):  # noqa: E501
        """NetworkInfoSearchResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_network_details = None
        self._page = None
        self._page_size = None
        self._total = None
        self.discriminator = None

        if device_network_details is not None:
            self.device_network_details = device_network_details
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total is not None:
            self.total = total

    @property
    def device_network_details(self):
        """Gets the device_network_details of this NetworkInfoSearchResult.  # noqa: E501

        Gets or sets device Network information.  # noqa: E501

        :return: The device_network_details of this NetworkInfoSearchResult.  # noqa: E501
        :rtype: list[DeviceNetworkSearchDetails]
        """
        return self._device_network_details

    @device_network_details.setter
    def device_network_details(self, device_network_details):
        """Sets the device_network_details of this NetworkInfoSearchResult.

        Gets or sets device Network information.  # noqa: E501

        :param device_network_details: The device_network_details of this NetworkInfoSearchResult.  # noqa: E501
        :type: list[DeviceNetworkSearchDetails]
        """

        self._device_network_details = device_network_details

    @property
    def page(self):
        """Gets the page of this NetworkInfoSearchResult.  # noqa: E501


        :return: The page of this NetworkInfoSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this NetworkInfoSearchResult.


        :param page: The page of this NetworkInfoSearchResult.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this NetworkInfoSearchResult.  # noqa: E501


        :return: The page_size of this NetworkInfoSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this NetworkInfoSearchResult.


        :param page_size: The page_size of this NetworkInfoSearchResult.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total(self):
        """Gets the total of this NetworkInfoSearchResult.  # noqa: E501


        :return: The total of this NetworkInfoSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NetworkInfoSearchResult.


        :param total: The total of this NetworkInfoSearchResult.  # noqa: E501
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
        if issubclass(NetworkInfoSearchResult, dict):
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
        if not isinstance(other, NetworkInfoSearchResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkInfoSearchResult):
            return True

        return self.to_dict() != other.to_dict()
