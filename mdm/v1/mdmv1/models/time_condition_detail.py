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


class TimeConditionDetail(object):
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
        'month_start': 'str',
        'day_start': 'str',
        'year_start': 'str',
        'hour_start': 'str',
        'minute_start': 'str',
        'month_end': 'str',
        'day_end': 'str',
        'year_end': 'str',
        'hour_end': 'str',
        'minute_end': 'str'
    }

    attribute_map = {
        'month_start': 'MonthStart',
        'day_start': 'DayStart',
        'year_start': 'YearStart',
        'hour_start': 'HourStart',
        'minute_start': 'MinuteStart',
        'month_end': 'MonthEnd',
        'day_end': 'DayEnd',
        'year_end': 'YearEnd',
        'hour_end': 'HourEnd',
        'minute_end': 'MinuteEnd'
    }

    def __init__(self, month_start=None, day_start=None, year_start=None, hour_start=None, minute_start=None, month_end=None, day_end=None, year_end=None, hour_end=None, minute_end=None, _configuration=None):  # noqa: E501
        """TimeConditionDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._month_start = None
        self._day_start = None
        self._year_start = None
        self._hour_start = None
        self._minute_start = None
        self._month_end = None
        self._day_end = None
        self._year_end = None
        self._hour_end = None
        self._minute_end = None
        self.discriminator = None

        if month_start is not None:
            self.month_start = month_start
        if day_start is not None:
            self.day_start = day_start
        if year_start is not None:
            self.year_start = year_start
        if hour_start is not None:
            self.hour_start = hour_start
        if minute_start is not None:
            self.minute_start = minute_start
        if month_end is not None:
            self.month_end = month_end
        if day_end is not None:
            self.day_end = day_end
        if year_end is not None:
            self.year_end = year_end
        if hour_end is not None:
            self.hour_end = hour_end
        if minute_end is not None:
            self.minute_end = minute_end

    @property
    def month_start(self):
        """Gets the month_start of this TimeConditionDetail.  # noqa: E501

        Gets or sets month in which time condition will first become available.  # noqa: E501

        :return: The month_start of this TimeConditionDetail.  # noqa: E501
        :rtype: str
        """
        return self._month_start

    @month_start.setter
    def month_start(self, month_start):
        """Sets the month_start of this TimeConditionDetail.

        Gets or sets month in which time condition will first become available.  # noqa: E501

        :param month_start: The month_start of this TimeConditionDetail.  # noqa: E501
        :type: str
        """

        self._month_start = month_start

    @property
    def day_start(self):
        """Gets the day_start of this TimeConditionDetail.  # noqa: E501

        Gets or sets day in which time condition will first become available.  # noqa: E501

        :return: The day_start of this TimeConditionDetail.  # noqa: E501
        :rtype: str
        """
        return self._day_start

    @day_start.setter
    def day_start(self, day_start):
        """Sets the day_start of this TimeConditionDetail.

        Gets or sets day in which time condition will first become available.  # noqa: E501

        :param day_start: The day_start of this TimeConditionDetail.  # noqa: E501
        :type: str
        """

        self._day_start = day_start

    @property
    def year_start(self):
        """Gets the year_start of this TimeConditionDetail.  # noqa: E501

        Gets or sets year in which time condition will first become available.  # noqa: E501

        :return: The year_start of this TimeConditionDetail.  # noqa: E501
        :rtype: str
        """
        return self._year_start

    @year_start.setter
    def year_start(self, year_start):
        """Sets the year_start of this TimeConditionDetail.

        Gets or sets year in which time condition will first become available.  # noqa: E501

        :param year_start: The year_start of this TimeConditionDetail.  # noqa: E501
        :type: str
        """

        self._year_start = year_start

    @property
    def hour_start(self):
        """Gets the hour_start of this TimeConditionDetail.  # noqa: E501

        Gets or sets hour in which time condition will first become available.  # noqa: E501

        :return: The hour_start of this TimeConditionDetail.  # noqa: E501
        :rtype: str
        """
        return self._hour_start

    @hour_start.setter
    def hour_start(self, hour_start):
        """Sets the hour_start of this TimeConditionDetail.

        Gets or sets hour in which time condition will first become available.  # noqa: E501

        :param hour_start: The hour_start of this TimeConditionDetail.  # noqa: E501
        :type: str
        """

        self._hour_start = hour_start

    @property
    def minute_start(self):
        """Gets the minute_start of this TimeConditionDetail.  # noqa: E501

        Gets or sets minute in which time condition will first become available.  # noqa: E501

        :return: The minute_start of this TimeConditionDetail.  # noqa: E501
        :rtype: str
        """
        return self._minute_start

    @minute_start.setter
    def minute_start(self, minute_start):
        """Sets the minute_start of this TimeConditionDetail.

        Gets or sets minute in which time condition will first become available.  # noqa: E501

        :param minute_start: The minute_start of this TimeConditionDetail.  # noqa: E501
        :type: str
        """

        self._minute_start = minute_start

    @property
    def month_end(self):
        """Gets the month_end of this TimeConditionDetail.  # noqa: E501

        Gets or sets month in which time condition will stop being available.  # noqa: E501

        :return: The month_end of this TimeConditionDetail.  # noqa: E501
        :rtype: str
        """
        return self._month_end

    @month_end.setter
    def month_end(self, month_end):
        """Sets the month_end of this TimeConditionDetail.

        Gets or sets month in which time condition will stop being available.  # noqa: E501

        :param month_end: The month_end of this TimeConditionDetail.  # noqa: E501
        :type: str
        """

        self._month_end = month_end

    @property
    def day_end(self):
        """Gets the day_end of this TimeConditionDetail.  # noqa: E501

        Gets or sets day in which time condition will stop being available.  # noqa: E501

        :return: The day_end of this TimeConditionDetail.  # noqa: E501
        :rtype: str
        """
        return self._day_end

    @day_end.setter
    def day_end(self, day_end):
        """Sets the day_end of this TimeConditionDetail.

        Gets or sets day in which time condition will stop being available.  # noqa: E501

        :param day_end: The day_end of this TimeConditionDetail.  # noqa: E501
        :type: str
        """

        self._day_end = day_end

    @property
    def year_end(self):
        """Gets the year_end of this TimeConditionDetail.  # noqa: E501

        Gets or sets year in which time condition will stop being available.  # noqa: E501

        :return: The year_end of this TimeConditionDetail.  # noqa: E501
        :rtype: str
        """
        return self._year_end

    @year_end.setter
    def year_end(self, year_end):
        """Sets the year_end of this TimeConditionDetail.

        Gets or sets year in which time condition will stop being available.  # noqa: E501

        :param year_end: The year_end of this TimeConditionDetail.  # noqa: E501
        :type: str
        """

        self._year_end = year_end

    @property
    def hour_end(self):
        """Gets the hour_end of this TimeConditionDetail.  # noqa: E501

        Gets or sets hour in which time condition will stop being available.  # noqa: E501

        :return: The hour_end of this TimeConditionDetail.  # noqa: E501
        :rtype: str
        """
        return self._hour_end

    @hour_end.setter
    def hour_end(self, hour_end):
        """Sets the hour_end of this TimeConditionDetail.

        Gets or sets hour in which time condition will stop being available.  # noqa: E501

        :param hour_end: The hour_end of this TimeConditionDetail.  # noqa: E501
        :type: str
        """

        self._hour_end = hour_end

    @property
    def minute_end(self):
        """Gets the minute_end of this TimeConditionDetail.  # noqa: E501

        Gets or sets minute in which time condition will stop being available.  # noqa: E501

        :return: The minute_end of this TimeConditionDetail.  # noqa: E501
        :rtype: str
        """
        return self._minute_end

    @minute_end.setter
    def minute_end(self, minute_end):
        """Sets the minute_end of this TimeConditionDetail.

        Gets or sets minute in which time condition will stop being available.  # noqa: E501

        :param minute_end: The minute_end of this TimeConditionDetail.  # noqa: E501
        :type: str
        """

        self._minute_end = minute_end

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
        if issubclass(TimeConditionDetail, dict):
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
        if not isinstance(other, TimeConditionDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeConditionDetail):
            return True

        return self.to_dict() != other.to_dict()
