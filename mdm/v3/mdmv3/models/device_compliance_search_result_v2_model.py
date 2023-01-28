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


class DeviceComplianceSearchResultV2Model(object):
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
        'compliance_policy_results': 'list[CompliancePolicyResultModel]',
        'overall_compliance_status': 'int',
        'page': 'int',
        'page_size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'compliance_policy_results': 'compliance_policy_results',
        'overall_compliance_status': 'overall_compliance_status',
        'page': 'page',
        'page_size': 'page_size',
        'total': 'total'
    }

    def __init__(self, compliance_policy_results=None, overall_compliance_status=None, page=None, page_size=None, total=None, _configuration=None):  # noqa: E501
        """DeviceComplianceSearchResultV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._compliance_policy_results = None
        self._overall_compliance_status = None
        self._page = None
        self._page_size = None
        self._total = None
        self.discriminator = None

        if compliance_policy_results is not None:
            self.compliance_policy_results = compliance_policy_results
        if overall_compliance_status is not None:
            self.overall_compliance_status = overall_compliance_status
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total is not None:
            self.total = total

    @property
    def compliance_policy_results(self):
        """Gets the compliance_policy_results of this DeviceComplianceSearchResultV2Model.  # noqa: E501

        A list of device compliance policy details and results.  # noqa: E501

        :return: The compliance_policy_results of this DeviceComplianceSearchResultV2Model.  # noqa: E501
        :rtype: list[CompliancePolicyResultModel]
        """
        return self._compliance_policy_results

    @compliance_policy_results.setter
    def compliance_policy_results(self, compliance_policy_results):
        """Sets the compliance_policy_results of this DeviceComplianceSearchResultV2Model.

        A list of device compliance policy details and results.  # noqa: E501

        :param compliance_policy_results: The compliance_policy_results of this DeviceComplianceSearchResultV2Model.  # noqa: E501
        :type: list[CompliancePolicyResultModel]
        """

        self._compliance_policy_results = compliance_policy_results

    @property
    def overall_compliance_status(self):
        """Gets the overall_compliance_status of this DeviceComplianceSearchResultV2Model.  # noqa: E501

        Overall compliance status of the device.  # noqa: E501

        :return: The overall_compliance_status of this DeviceComplianceSearchResultV2Model.  # noqa: E501
        :rtype: int
        """
        return self._overall_compliance_status

    @overall_compliance_status.setter
    def overall_compliance_status(self, overall_compliance_status):
        """Sets the overall_compliance_status of this DeviceComplianceSearchResultV2Model.

        Overall compliance status of the device.  # noqa: E501

        :param overall_compliance_status: The overall_compliance_status of this DeviceComplianceSearchResultV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # noqa: E501
        if (self._configuration.client_side_validation and
                overall_compliance_status not in allowed_values):
            raise ValueError(
                "Invalid value for `overall_compliance_status` ({0}), must be one of {1}"  # noqa: E501
                .format(overall_compliance_status, allowed_values)
            )

        self._overall_compliance_status = overall_compliance_status

    @property
    def page(self):
        """Gets the page of this DeviceComplianceSearchResultV2Model.  # noqa: E501

        The result set page index.  # noqa: E501

        :return: The page of this DeviceComplianceSearchResultV2Model.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this DeviceComplianceSearchResultV2Model.

        The result set page index.  # noqa: E501

        :param page: The page of this DeviceComplianceSearchResultV2Model.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this DeviceComplianceSearchResultV2Model.  # noqa: E501

        Maximum records per page.  # noqa: E501

        :return: The page_size of this DeviceComplianceSearchResultV2Model.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DeviceComplianceSearchResultV2Model.

        Maximum records per page.  # noqa: E501

        :param page_size: The page_size of this DeviceComplianceSearchResultV2Model.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total(self):
        """Gets the total of this DeviceComplianceSearchResultV2Model.  # noqa: E501

        Total number of results.  # noqa: E501

        :return: The total of this DeviceComplianceSearchResultV2Model.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DeviceComplianceSearchResultV2Model.

        Total number of results.  # noqa: E501

        :param total: The total of this DeviceComplianceSearchResultV2Model.  # noqa: E501
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
        if issubclass(DeviceComplianceSearchResultV2Model, dict):
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
        if not isinstance(other, DeviceComplianceSearchResultV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceComplianceSearchResultV2Model):
            return True

        return self.to_dict() != other.to_dict()
