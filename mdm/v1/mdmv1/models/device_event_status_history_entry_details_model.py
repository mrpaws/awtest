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


class DeviceEventStatusHistoryEntryDetailsModel(object):
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
        'user_name': 'str',
        'date_time': 'str',
        'status': 'str'
    }

    attribute_map = {
        'user_name': 'UserName',
        'date_time': 'DateTime',
        'status': 'Status'
    }

    def __init__(self, user_name=None, date_time=None, status=None, _configuration=None):  # noqa: E501
        """DeviceEventStatusHistoryEntryDetailsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_name = None
        self._date_time = None
        self._status = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if date_time is not None:
            self.date_time = date_time
        if status is not None:
            self.status = status

    @property
    def user_name(self):
        """Gets the user_name of this DeviceEventStatusHistoryEntryDetailsModel.  # noqa: E501

        Gets or sets the user name.  # noqa: E501

        :return: The user_name of this DeviceEventStatusHistoryEntryDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this DeviceEventStatusHistoryEntryDetailsModel.

        Gets or sets the user name.  # noqa: E501

        :param user_name: The user_name of this DeviceEventStatusHistoryEntryDetailsModel.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def date_time(self):
        """Gets the date_time of this DeviceEventStatusHistoryEntryDetailsModel.  # noqa: E501

        Gets or sets the date time.  # noqa: E501

        :return: The date_time of this DeviceEventStatusHistoryEntryDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this DeviceEventStatusHistoryEntryDetailsModel.

        Gets or sets the date time.  # noqa: E501

        :param date_time: The date_time of this DeviceEventStatusHistoryEntryDetailsModel.  # noqa: E501
        :type: str
        """

        self._date_time = date_time

    @property
    def status(self):
        """Gets the status of this DeviceEventStatusHistoryEntryDetailsModel.  # noqa: E501

        Gets or sets the status.  # noqa: E501

        :return: The status of this DeviceEventStatusHistoryEntryDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeviceEventStatusHistoryEntryDetailsModel.

        Gets or sets the status.  # noqa: E501

        :param status: The status of this DeviceEventStatusHistoryEntryDetailsModel.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(DeviceEventStatusHistoryEntryDetailsModel, dict):
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
        if not isinstance(other, DeviceEventStatusHistoryEntryDetailsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceEventStatusHistoryEntryDetailsModel):
            return True

        return self.to_dict() != other.to_dict()
