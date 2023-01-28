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


class LicensesSummaryV2Model(object):
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
        'total': 'int',
        'on_hold': 'int',
        'redeemed': 'int',
        'allocated': 'int',
        'unallocated': 'int'
    }

    attribute_map = {
        'total': 'total',
        'on_hold': 'on_hold',
        'redeemed': 'redeemed',
        'allocated': 'allocated',
        'unallocated': 'unallocated'
    }

    def __init__(self, total=None, on_hold=None, redeemed=None, allocated=None, unallocated=None, _configuration=None):  # noqa: E501
        """LicensesSummaryV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._total = None
        self._on_hold = None
        self._redeemed = None
        self._allocated = None
        self._unallocated = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if on_hold is not None:
            self.on_hold = on_hold
        if redeemed is not None:
            self.redeemed = redeemed
        if allocated is not None:
            self.allocated = allocated
        if unallocated is not None:
            self.unallocated = unallocated

    @property
    def total(self):
        """Gets the total of this LicensesSummaryV2Model.  # noqa: E501

        Total number of licenses.  # noqa: E501

        :return: The total of this LicensesSummaryV2Model.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this LicensesSummaryV2Model.

        Total number of licenses.  # noqa: E501

        :param total: The total of this LicensesSummaryV2Model.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def on_hold(self):
        """Gets the on_hold of this LicensesSummaryV2Model.  # noqa: E501

        Number of licenses on hold.  # noqa: E501

        :return: The on_hold of this LicensesSummaryV2Model.  # noqa: E501
        :rtype: int
        """
        return self._on_hold

    @on_hold.setter
    def on_hold(self, on_hold):
        """Sets the on_hold of this LicensesSummaryV2Model.

        Number of licenses on hold.  # noqa: E501

        :param on_hold: The on_hold of this LicensesSummaryV2Model.  # noqa: E501
        :type: int
        """

        self._on_hold = on_hold

    @property
    def redeemed(self):
        """Gets the redeemed of this LicensesSummaryV2Model.  # noqa: E501

        Number of redeemed licenses.  # noqa: E501

        :return: The redeemed of this LicensesSummaryV2Model.  # noqa: E501
        :rtype: int
        """
        return self._redeemed

    @redeemed.setter
    def redeemed(self, redeemed):
        """Sets the redeemed of this LicensesSummaryV2Model.

        Number of redeemed licenses.  # noqa: E501

        :param redeemed: The redeemed of this LicensesSummaryV2Model.  # noqa: E501
        :type: int
        """

        self._redeemed = redeemed

    @property
    def allocated(self):
        """Gets the allocated of this LicensesSummaryV2Model.  # noqa: E501

        Number of allocated licenses.  # noqa: E501

        :return: The allocated of this LicensesSummaryV2Model.  # noqa: E501
        :rtype: int
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this LicensesSummaryV2Model.

        Number of allocated licenses.  # noqa: E501

        :param allocated: The allocated of this LicensesSummaryV2Model.  # noqa: E501
        :type: int
        """

        self._allocated = allocated

    @property
    def unallocated(self):
        """Gets the unallocated of this LicensesSummaryV2Model.  # noqa: E501

        Number of unallocated licenses.  # noqa: E501

        :return: The unallocated of this LicensesSummaryV2Model.  # noqa: E501
        :rtype: int
        """
        return self._unallocated

    @unallocated.setter
    def unallocated(self, unallocated):
        """Sets the unallocated of this LicensesSummaryV2Model.

        Number of unallocated licenses.  # noqa: E501

        :param unallocated: The unallocated of this LicensesSummaryV2Model.  # noqa: E501
        :type: int
        """

        self._unallocated = unallocated

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
        if issubclass(LicensesSummaryV2Model, dict):
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
        if not isinstance(other, LicensesSummaryV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicensesSummaryV2Model):
            return True

        return self.to_dict() != other.to_dict()
