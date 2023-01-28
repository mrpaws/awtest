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


class WorkflowStatusCount(object):
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
        'workflow_uuid': 'str',
        'status_count': 'list[DeviceWorkflowStatusCount]'
    }

    attribute_map = {
        'workflow_uuid': 'workflow_uuid',
        'status_count': 'status_count'
    }

    def __init__(self, workflow_uuid=None, status_count=None, _configuration=None):  # noqa: E501
        """WorkflowStatusCount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._workflow_uuid = None
        self._status_count = None
        self.discriminator = None

        if workflow_uuid is not None:
            self.workflow_uuid = workflow_uuid
        if status_count is not None:
            self.status_count = status_count

    @property
    def workflow_uuid(self):
        """Gets the workflow_uuid of this WorkflowStatusCount.  # noqa: E501


        :return: The workflow_uuid of this WorkflowStatusCount.  # noqa: E501
        :rtype: str
        """
        return self._workflow_uuid

    @workflow_uuid.setter
    def workflow_uuid(self, workflow_uuid):
        """Sets the workflow_uuid of this WorkflowStatusCount.


        :param workflow_uuid: The workflow_uuid of this WorkflowStatusCount.  # noqa: E501
        :type: str
        """

        self._workflow_uuid = workflow_uuid

    @property
    def status_count(self):
        """Gets the status_count of this WorkflowStatusCount.  # noqa: E501


        :return: The status_count of this WorkflowStatusCount.  # noqa: E501
        :rtype: list[DeviceWorkflowStatusCount]
        """
        return self._status_count

    @status_count.setter
    def status_count(self, status_count):
        """Sets the status_count of this WorkflowStatusCount.


        :param status_count: The status_count of this WorkflowStatusCount.  # noqa: E501
        :type: list[DeviceWorkflowStatusCount]
        """

        self._status_count = status_count

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
        if issubclass(WorkflowStatusCount, dict):
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
        if not isinstance(other, WorkflowStatusCount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowStatusCount):
            return True

        return self.to_dict() != other.to_dict()
