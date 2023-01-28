# coding: utf-8

"""
    MDM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv2.configuration import Configuration


class AndroidForWorkSamsungDateTimePayloadV2Entity_(object):
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
        'date_format': 'str',
        'automatic_time': 'bool',
        'date_time': 'str',
        'time_format': 'int',
        'region': 'str',
        'time_zone': 'str',
        'url': 'str',
        'enable_periodic_sync': 'bool',
        'sync_interval_days': 'int',
        'set_time_zone': 'bool'
    }

    attribute_map = {
        'date_format': 'DateFormat',
        'automatic_time': 'AutomaticTime',
        'date_time': 'DateTime',
        'time_format': 'TimeFormat',
        'region': 'Region',
        'time_zone': 'TimeZone',
        'url': 'URL',
        'enable_periodic_sync': 'EnablePeriodicSync',
        'sync_interval_days': 'SyncIntervalDays',
        'set_time_zone': 'SetTimeZone'
    }

    def __init__(self, date_format=None, automatic_time=None, date_time=None, time_format=None, region=None, time_zone=None, url=None, enable_periodic_sync=None, sync_interval_days=None, set_time_zone=None, _configuration=None):  # noqa: E501
        """AndroidForWorkSamsungDateTimePayloadV2Entity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._date_format = None
        self._automatic_time = None
        self._date_time = None
        self._time_format = None
        self._region = None
        self._time_zone = None
        self._url = None
        self._enable_periodic_sync = None
        self._sync_interval_days = None
        self._set_time_zone = None
        self.discriminator = None

        self.date_format = date_format
        if automatic_time is not None:
            self.automatic_time = automatic_time
        self.date_time = date_time
        self.time_format = time_format
        if region is not None:
            self.region = region
        if time_zone is not None:
            self.time_zone = time_zone
        if url is not None:
            self.url = url
        if enable_periodic_sync is not None:
            self.enable_periodic_sync = enable_periodic_sync
        if sync_interval_days is not None:
            self.sync_interval_days = sync_interval_days
        if set_time_zone is not None:
            self.set_time_zone = set_time_zone

    @property
    def date_format(self):
        """Gets the date_format of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501

        Gets or sets date format.  # noqa: E501

        :return: The date_format of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this AndroidForWorkSamsungDateTimePayloadV2Entity_.

        Gets or sets date format.  # noqa: E501

        :param date_format: The date_format of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and date_format is None:
            raise ValueError("Invalid value for `date_format`, must not be `None`")  # noqa: E501

        self._date_format = date_format

    @property
    def automatic_time(self):
        """Gets the automatic_time of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501

        Gets or sets a value indicating whether indicates whether automatic time is used in the date.  # noqa: E501

        :return: The automatic_time of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_time

    @automatic_time.setter
    def automatic_time(self, automatic_time):
        """Sets the automatic_time of this AndroidForWorkSamsungDateTimePayloadV2Entity_.

        Gets or sets a value indicating whether indicates whether automatic time is used in the date.  # noqa: E501

        :param automatic_time: The automatic_time of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._automatic_time = automatic_time

    @property
    def date_time(self):
        """Gets the date_time of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501

        Gets or sets dateTime value in specified date format.  # noqa: E501

        :return: The date_time of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this AndroidForWorkSamsungDateTimePayloadV2Entity_.

        Gets or sets dateTime value in specified date format.  # noqa: E501

        :param date_time: The date_time of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and date_time is None:
            raise ValueError("Invalid value for `date_time`, must not be `None`")  # noqa: E501

        self._date_time = date_time

    @property
    def time_format(self):
        """Gets the time_format of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501

        Gets or sets time format.  # noqa: E501

        :return: The time_format of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this AndroidForWorkSamsungDateTimePayloadV2Entity_.

        Gets or sets time format.  # noqa: E501

        :param time_format: The time_format of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and time_format is None:
            raise ValueError("Invalid value for `time_format`, must not be `None`")  # noqa: E501

        self._time_format = time_format

    @property
    def region(self):
        """Gets the region of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501

        Gets or sets region - for timezones.  # noqa: E501

        :return: The region of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AndroidForWorkSamsungDateTimePayloadV2Entity_.

        Gets or sets region - for timezones.  # noqa: E501

        :param region: The region of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def time_zone(self):
        """Gets the time_zone of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501

        Gets or sets timezone.  # noqa: E501

        :return: The time_zone of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this AndroidForWorkSamsungDateTimePayloadV2Entity_.

        Gets or sets timezone.  # noqa: E501

        :param time_zone: The time_zone of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def url(self):
        """Gets the url of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501

        Gets or sets url of server setting date time value.  # noqa: E501

        :return: The url of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AndroidForWorkSamsungDateTimePayloadV2Entity_.

        Gets or sets url of server setting date time value.  # noqa: E501

        :param url: The url of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def enable_periodic_sync(self):
        """Gets the enable_periodic_sync of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501

        Gets or sets indicates whether periodic sync is enabled or not.  # noqa: E501

        :return: The enable_periodic_sync of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._enable_periodic_sync

    @enable_periodic_sync.setter
    def enable_periodic_sync(self, enable_periodic_sync):
        """Sets the enable_periodic_sync of this AndroidForWorkSamsungDateTimePayloadV2Entity_.

        Gets or sets indicates whether periodic sync is enabled or not.  # noqa: E501

        :param enable_periodic_sync: The enable_periodic_sync of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._enable_periodic_sync = enable_periodic_sync

    @property
    def sync_interval_days(self):
        """Gets the sync_interval_days of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501

        Gets or sets indicates the length of a sync interval.  # noqa: E501

        :return: The sync_interval_days of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :rtype: int
        """
        return self._sync_interval_days

    @sync_interval_days.setter
    def sync_interval_days(self, sync_interval_days):
        """Sets the sync_interval_days of this AndroidForWorkSamsungDateTimePayloadV2Entity_.

        Gets or sets indicates the length of a sync interval.  # noqa: E501

        :param sync_interval_days: The sync_interval_days of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :type: int
        """

        self._sync_interval_days = sync_interval_days

    @property
    def set_time_zone(self):
        """Gets the set_time_zone of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501

        Gets or sets indicates whether specific timezone is set.  # noqa: E501

        :return: The set_time_zone of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :rtype: bool
        """
        return self._set_time_zone

    @set_time_zone.setter
    def set_time_zone(self, set_time_zone):
        """Sets the set_time_zone of this AndroidForWorkSamsungDateTimePayloadV2Entity_.

        Gets or sets indicates whether specific timezone is set.  # noqa: E501

        :param set_time_zone: The set_time_zone of this AndroidForWorkSamsungDateTimePayloadV2Entity_.  # noqa: E501
        :type: bool
        """

        self._set_time_zone = set_time_zone

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
        if issubclass(AndroidForWorkSamsungDateTimePayloadV2Entity_, dict):
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
        if not isinstance(other, AndroidForWorkSamsungDateTimePayloadV2Entity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkSamsungDateTimePayloadV2Entity_):
            return True

        return self.to_dict() != other.to_dict()
