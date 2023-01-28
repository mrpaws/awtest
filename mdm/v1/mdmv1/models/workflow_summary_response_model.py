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


class WorkflowSummaryResponseModel(object):
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
        'total_devices': 'int',
        'status_summary': 'list[WorkflowStatusSummaryModel]'
    }

    attribute_map = {
        'total_devices': 'total_devices',
        'status_summary': 'status_summary'
    }

    def __init__(self, total_devices=None, status_summary=None, _configuration=None):  # noqa: E501
        """WorkflowSummaryResponseModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._total_devices = None
        self._status_summary = None
        self.discriminator = None

        self.total_devices = total_devices
        self.status_summary = status_summary

    @property
    def total_devices(self):
        """Gets the total_devices of this WorkflowSummaryResponseModel.  # noqa: E501

        Total number of matching devices.  # noqa: E501

        :return: The total_devices of this WorkflowSummaryResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._total_devices

    @total_devices.setter
    def total_devices(self, total_devices):
        """Sets the total_devices of this WorkflowSummaryResponseModel.

        Total number of matching devices.  # noqa: E501

        :param total_devices: The total_devices of this WorkflowSummaryResponseModel.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and total_devices is None:
            raise ValueError("Invalid value for `total_devices`, must not be `None`")  # noqa: E501

        self._total_devices = total_devices

    @property
    def status_summary(self):
        """Gets the status_summary of this WorkflowSummaryResponseModel.  # noqa: E501

        A collection of workflow status summaries.  # noqa: E501

        :return: The status_summary of this WorkflowSummaryResponseModel.  # noqa: E501
        :rtype: list[WorkflowStatusSummaryModel]
        """
        return self._status_summary

    @status_summary.setter
    def status_summary(self, status_summary):
        """Sets the status_summary of this WorkflowSummaryResponseModel.

        A collection of workflow status summaries.  # noqa: E501

        :param status_summary: The status_summary of this WorkflowSummaryResponseModel.  # noqa: E501
        :type: list[WorkflowStatusSummaryModel]
        """
        if self._configuration.client_side_validation and status_summary is None:
            raise ValueError("Invalid value for `status_summary`, must not be `None`")  # noqa: E501

        self._status_summary = status_summary

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
        if issubclass(WorkflowSummaryResponseModel, dict):
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
        if not isinstance(other, WorkflowSummaryResponseModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowSummaryResponseModel):
            return True

        return self.to_dict() != other.to_dict()