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


class AndroidForWorkAutoUpdatePayloadV2Entity(object):
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
        'auto_update_install_policy': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'auto_update_install_policy': 'AutoUpdateInstallPolicy',
        'start_time': 'StartTime',
        'end_time': 'EndTime'
    }

    def __init__(self, auto_update_install_policy=None, start_time=None, end_time=None, _configuration=None):  # noqa: E501
        """AndroidForWorkAutoUpdatePayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_update_install_policy = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.auto_update_install_policy = auto_update_install_policy
        self.start_time = start_time
        self.end_time = end_time

    @property
    def auto_update_install_policy(self):
        """Gets the auto_update_install_policy of this AndroidForWorkAutoUpdatePayloadV2Entity.  # noqa: E501

        Gets or sets the application update install policy.  # noqa: E501

        :return: The auto_update_install_policy of this AndroidForWorkAutoUpdatePayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._auto_update_install_policy

    @auto_update_install_policy.setter
    def auto_update_install_policy(self, auto_update_install_policy):
        """Sets the auto_update_install_policy of this AndroidForWorkAutoUpdatePayloadV2Entity.

        Gets or sets the application update install policy.  # noqa: E501

        :param auto_update_install_policy: The auto_update_install_policy of this AndroidForWorkAutoUpdatePayloadV2Entity.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and auto_update_install_policy is None:
            raise ValueError("Invalid value for `auto_update_install_policy`, must not be `None`")  # noqa: E501

        self._auto_update_install_policy = auto_update_install_policy

    @property
    def start_time(self):
        """Gets the start_time of this AndroidForWorkAutoUpdatePayloadV2Entity.  # noqa: E501

        Gets or sets the maintenance window start time in HH:mm format.  # noqa: E501

        :return: The start_time of this AndroidForWorkAutoUpdatePayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AndroidForWorkAutoUpdatePayloadV2Entity.

        Gets or sets the maintenance window start time in HH:mm format.  # noqa: E501

        :param start_time: The start_time of this AndroidForWorkAutoUpdatePayloadV2Entity.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                start_time is not None and not re.search(r'^(0[1-9]|1[0-9]|2[0-3]):[0-5][0-9]\\s*$', start_time)):  # noqa: E501
            raise ValueError(r"Invalid value for `start_time`, must be a follow pattern or equal to `/^(0[1-9]|1[0-9]|2[0-3]):[0-5][0-9]\\s*$/`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this AndroidForWorkAutoUpdatePayloadV2Entity.  # noqa: E501

        Gets or sets the maintenance window end time in HH:mm format.  # noqa: E501

        :return: The end_time of this AndroidForWorkAutoUpdatePayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AndroidForWorkAutoUpdatePayloadV2Entity.

        Gets or sets the maintenance window end time in HH:mm format.  # noqa: E501

        :param end_time: The end_time of this AndroidForWorkAutoUpdatePayloadV2Entity.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                end_time is not None and not re.search(r'^(0[1-9]|1[0-9]|2[0-3]):[0-5][0-9]\\s*$', end_time)):  # noqa: E501
            raise ValueError(r"Invalid value for `end_time`, must be a follow pattern or equal to `/^(0[1-9]|1[0-9]|2[0-3]):[0-5][0-9]\\s*$/`")  # noqa: E501

        self._end_time = end_time

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
        if issubclass(AndroidForWorkAutoUpdatePayloadV2Entity, dict):
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
        if not isinstance(other, AndroidForWorkAutoUpdatePayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidForWorkAutoUpdatePayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
