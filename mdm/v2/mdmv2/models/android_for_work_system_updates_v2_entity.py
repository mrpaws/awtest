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


class AndroidForWorkSystemUpdatesV2Entity(object):
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
        'install_policy_type': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'freeze_periods_list': 'list[AndroidSystemUpdateApiFreezePeriod]'
    }

    attribute_map = {
        'install_policy_type': 'InstallPolicyType',
        'start_time': 'StartTime',
        'end_time': 'EndTime',
        'freeze_periods_list': 'FreezePeriodsList'
    }

    def __init__(self, install_policy_type=None, start_time=None, end_time=None, freeze_periods_list=None, _configuration=None):  # noqa: E501
        """AndroidForWorkSystemUpdatesV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._install_policy_type = None
        self._start_time = None
        self._end_time = None
        self._freeze_periods_list = None
        self.discriminator = None

        if install_policy_type is not None:
            self.install_policy_type = install_policy_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if freeze_periods_list is not None:
            self.freeze_periods_list = freeze_periods_list

    @property
    def install_policy_type(self):
        """Gets the install_policy_type of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501

        Gets or sets the install policy.  # noqa: E501

        :return: The install_policy_type of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._install_policy_type

    @install_policy_type.setter
    def install_policy_type(self, install_policy_type):
        """Sets the install_policy_type of this AndroidForWorkSystemUpdatesV2Entity.

        Gets or sets the install policy.  # noqa: E501

        :param install_policy_type: The install_policy_type of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501
        :type: int
        """

        self._install_policy_type = install_policy_type

    @property
    def start_time(self):
        """Gets the start_time of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501

        Gets or sets the start time in hours.  # noqa: E501

        :return: The start_time of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AndroidForWorkSystemUpdatesV2Entity.

        Gets or sets the start time in hours.  # noqa: E501

        :param start_time: The start_time of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501

        Gets or sets the end time in hours.  # noqa: E501

        :return: The end_time of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AndroidForWorkSystemUpdatesV2Entity.

        Gets or sets the end time in hours.  # noqa: E501

        :param end_time: The end_time of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def freeze_periods_list(self):
        """Gets the freeze_periods_list of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501

        Gets or sets the freeze periods list.  # noqa: E501

        :return: The freeze_periods_list of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501
        :rtype: list[AndroidSystemUpdateApiFreezePeriod]
        """
        return self._freeze_periods_list

    @freeze_periods_list.setter
    def freeze_periods_list(self, freeze_periods_list):
        """Sets the freeze_periods_list of this AndroidForWorkSystemUpdatesV2Entity.

        Gets or sets the freeze periods list.  # noqa: E501

        :param freeze_periods_list: The freeze_periods_list of this AndroidForWorkSystemUpdatesV2Entity.  # noqa: E501
        :type: list[AndroidSystemUpdateApiFreezePeriod]
        """

        self._freeze_periods_list = freeze_periods_list

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
        if issubclass(AndroidForWorkSystemUpdatesV2Entity, dict):
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
        if not isinstance(other, AndroidForWorkSystemUpdatesV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkSystemUpdatesV2Entity):
            return True

        return self.to_dict() != other.to_dict()
