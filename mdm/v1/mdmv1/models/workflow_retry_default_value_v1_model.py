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


class WorkflowRetryDefaultValueV1Model(object):
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
        'time_interval_in_minutes': 'WorkflowTimeDefaultValueV1Model',
        'attempts': 'WorkflowRetryAttemptsV1Model',
        'backoff_rate': 'WorkflowRetryBackoffRateV1Model'
    }

    attribute_map = {
        'time_interval_in_minutes': 'time_interval_in_minutes',
        'attempts': 'attempts',
        'backoff_rate': 'backoff_rate'
    }

    def __init__(self, time_interval_in_minutes=None, attempts=None, backoff_rate=None, _configuration=None):  # noqa: E501
        """WorkflowRetryDefaultValueV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._time_interval_in_minutes = None
        self._attempts = None
        self._backoff_rate = None
        self.discriminator = None

        if time_interval_in_minutes is not None:
            self.time_interval_in_minutes = time_interval_in_minutes
        if attempts is not None:
            self.attempts = attempts
        if backoff_rate is not None:
            self.backoff_rate = backoff_rate

    @property
    def time_interval_in_minutes(self):
        """Gets the time_interval_in_minutes of this WorkflowRetryDefaultValueV1Model.  # noqa: E501

        Workflow retry time interval in minutes.  # noqa: E501

        :return: The time_interval_in_minutes of this WorkflowRetryDefaultValueV1Model.  # noqa: E501
        :rtype: WorkflowTimeDefaultValueV1Model
        """
        return self._time_interval_in_minutes

    @time_interval_in_minutes.setter
    def time_interval_in_minutes(self, time_interval_in_minutes):
        """Sets the time_interval_in_minutes of this WorkflowRetryDefaultValueV1Model.

        Workflow retry time interval in minutes.  # noqa: E501

        :param time_interval_in_minutes: The time_interval_in_minutes of this WorkflowRetryDefaultValueV1Model.  # noqa: E501
        :type: WorkflowTimeDefaultValueV1Model
        """

        self._time_interval_in_minutes = time_interval_in_minutes

    @property
    def attempts(self):
        """Gets the attempts of this WorkflowRetryDefaultValueV1Model.  # noqa: E501

        Workflow retry attempts.  # noqa: E501

        :return: The attempts of this WorkflowRetryDefaultValueV1Model.  # noqa: E501
        :rtype: WorkflowRetryAttemptsV1Model
        """
        return self._attempts

    @attempts.setter
    def attempts(self, attempts):
        """Sets the attempts of this WorkflowRetryDefaultValueV1Model.

        Workflow retry attempts.  # noqa: E501

        :param attempts: The attempts of this WorkflowRetryDefaultValueV1Model.  # noqa: E501
        :type: WorkflowRetryAttemptsV1Model
        """

        self._attempts = attempts

    @property
    def backoff_rate(self):
        """Gets the backoff_rate of this WorkflowRetryDefaultValueV1Model.  # noqa: E501

        Workflow retry back off rate.  # noqa: E501

        :return: The backoff_rate of this WorkflowRetryDefaultValueV1Model.  # noqa: E501
        :rtype: WorkflowRetryBackoffRateV1Model
        """
        return self._backoff_rate

    @backoff_rate.setter
    def backoff_rate(self, backoff_rate):
        """Sets the backoff_rate of this WorkflowRetryDefaultValueV1Model.

        Workflow retry back off rate.  # noqa: E501

        :param backoff_rate: The backoff_rate of this WorkflowRetryDefaultValueV1Model.  # noqa: E501
        :type: WorkflowRetryBackoffRateV1Model
        """

        self._backoff_rate = backoff_rate

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
        if issubclass(WorkflowRetryDefaultValueV1Model, dict):
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
        if not isinstance(other, WorkflowRetryDefaultValueV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowRetryDefaultValueV1Model):
            return True

        return self.to_dict() != other.to_dict()