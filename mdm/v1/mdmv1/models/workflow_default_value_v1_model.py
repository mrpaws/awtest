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


class WorkflowDefaultValueV1Model(object):
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
        'time_interval_in_minutes': 'int',
        'max_attempts': 'int',
        'backoff_rate': 'float',
        'timeout_in_minutes': 'int',
        'timeout_format': 'int',
        'time_interval_format': 'int'
    }

    attribute_map = {
        'time_interval_in_minutes': 'time_interval_in_minutes',
        'max_attempts': 'max_attempts',
        'backoff_rate': 'backoff_rate',
        'timeout_in_minutes': 'timeout_in_minutes',
        'timeout_format': 'timeout_format',
        'time_interval_format': 'time_interval_format'
    }

    def __init__(self, time_interval_in_minutes=None, max_attempts=None, backoff_rate=None, timeout_in_minutes=None, timeout_format=None, time_interval_format=None, _configuration=None):  # noqa: E501
        """WorkflowDefaultValueV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._time_interval_in_minutes = None
        self._max_attempts = None
        self._backoff_rate = None
        self._timeout_in_minutes = None
        self._timeout_format = None
        self._time_interval_format = None
        self.discriminator = None

        if time_interval_in_minutes is not None:
            self.time_interval_in_minutes = time_interval_in_minutes
        if max_attempts is not None:
            self.max_attempts = max_attempts
        if backoff_rate is not None:
            self.backoff_rate = backoff_rate
        if timeout_in_minutes is not None:
            self.timeout_in_minutes = timeout_in_minutes
        if timeout_format is not None:
            self.timeout_format = timeout_format
        if time_interval_format is not None:
            self.time_interval_format = time_interval_format

    @property
    def time_interval_in_minutes(self):
        """Gets the time_interval_in_minutes of this WorkflowDefaultValueV1Model.  # noqa: E501

        The time interval in minutes.  # noqa: E501

        :return: The time_interval_in_minutes of this WorkflowDefaultValueV1Model.  # noqa: E501
        :rtype: int
        """
        return self._time_interval_in_minutes

    @time_interval_in_minutes.setter
    def time_interval_in_minutes(self, time_interval_in_minutes):
        """Sets the time_interval_in_minutes of this WorkflowDefaultValueV1Model.

        The time interval in minutes.  # noqa: E501

        :param time_interval_in_minutes: The time_interval_in_minutes of this WorkflowDefaultValueV1Model.  # noqa: E501
        :type: int
        """

        self._time_interval_in_minutes = time_interval_in_minutes

    @property
    def max_attempts(self):
        """Gets the max_attempts of this WorkflowDefaultValueV1Model.  # noqa: E501

        The max value of number of attempts.  # noqa: E501

        :return: The max_attempts of this WorkflowDefaultValueV1Model.  # noqa: E501
        :rtype: int
        """
        return self._max_attempts

    @max_attempts.setter
    def max_attempts(self, max_attempts):
        """Sets the max_attempts of this WorkflowDefaultValueV1Model.

        The max value of number of attempts.  # noqa: E501

        :param max_attempts: The max_attempts of this WorkflowDefaultValueV1Model.  # noqa: E501
        :type: int
        """

        self._max_attempts = max_attempts

    @property
    def backoff_rate(self):
        """Gets the backoff_rate of this WorkflowDefaultValueV1Model.  # noqa: E501

        The backoff rate value.  # noqa: E501

        :return: The backoff_rate of this WorkflowDefaultValueV1Model.  # noqa: E501
        :rtype: float
        """
        return self._backoff_rate

    @backoff_rate.setter
    def backoff_rate(self, backoff_rate):
        """Sets the backoff_rate of this WorkflowDefaultValueV1Model.

        The backoff rate value.  # noqa: E501

        :param backoff_rate: The backoff_rate of this WorkflowDefaultValueV1Model.  # noqa: E501
        :type: float
        """

        self._backoff_rate = backoff_rate

    @property
    def timeout_in_minutes(self):
        """Gets the timeout_in_minutes of this WorkflowDefaultValueV1Model.  # noqa: E501

        The default value in minutes.  # noqa: E501

        :return: The timeout_in_minutes of this WorkflowDefaultValueV1Model.  # noqa: E501
        :rtype: int
        """
        return self._timeout_in_minutes

    @timeout_in_minutes.setter
    def timeout_in_minutes(self, timeout_in_minutes):
        """Sets the timeout_in_minutes of this WorkflowDefaultValueV1Model.

        The default value in minutes.  # noqa: E501

        :param timeout_in_minutes: The timeout_in_minutes of this WorkflowDefaultValueV1Model.  # noqa: E501
        :type: int
        """

        self._timeout_in_minutes = timeout_in_minutes

    @property
    def timeout_format(self):
        """Gets the timeout_format of this WorkflowDefaultValueV1Model.  # noqa: E501

        Time format selection for timeout.  # noqa: E501

        :return: The timeout_format of this WorkflowDefaultValueV1Model.  # noqa: E501
        :rtype: int
        """
        return self._timeout_format

    @timeout_format.setter
    def timeout_format(self, timeout_format):
        """Sets the timeout_format of this WorkflowDefaultValueV1Model.

        Time format selection for timeout.  # noqa: E501

        :param timeout_format: The timeout_format of this WorkflowDefaultValueV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if (self._configuration.client_side_validation and
                timeout_format not in allowed_values):
            raise ValueError(
                "Invalid value for `timeout_format` ({0}), must be one of {1}"  # noqa: E501
                .format(timeout_format, allowed_values)
            )

        self._timeout_format = timeout_format

    @property
    def time_interval_format(self):
        """Gets the time_interval_format of this WorkflowDefaultValueV1Model.  # noqa: E501

        Time format selection for retry time interval.  # noqa: E501

        :return: The time_interval_format of this WorkflowDefaultValueV1Model.  # noqa: E501
        :rtype: int
        """
        return self._time_interval_format

    @time_interval_format.setter
    def time_interval_format(self, time_interval_format):
        """Sets the time_interval_format of this WorkflowDefaultValueV1Model.

        Time format selection for retry time interval.  # noqa: E501

        :param time_interval_format: The time_interval_format of this WorkflowDefaultValueV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if (self._configuration.client_side_validation and
                time_interval_format not in allowed_values):
            raise ValueError(
                "Invalid value for `time_interval_format` ({0}), must be one of {1}"  # noqa: E501
                .format(time_interval_format, allowed_values)
            )

        self._time_interval_format = time_interval_format

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
        if issubclass(WorkflowDefaultValueV1Model, dict):
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
        if not isinstance(other, WorkflowDefaultValueV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowDefaultValueV1Model):
            return True

        return self.to_dict() != other.to_dict()
