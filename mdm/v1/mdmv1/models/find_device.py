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


class FindDevice(object):
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
        'platform': 'str',
        'application': 'str',
        'message': 'str',
        'number_of_repetitions': 'str',
        'gap_between_repetitions': 'str'
    }

    attribute_map = {
        'platform': 'Platform',
        'application': 'Application',
        'message': 'Message',
        'number_of_repetitions': 'NumberOfRepetitions',
        'gap_between_repetitions': 'GapBetweenRepetitions'
    }

    def __init__(self, platform=None, application=None, message=None, number_of_repetitions=None, gap_between_repetitions=None, _configuration=None):  # noqa: E501
        """FindDevice - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._platform = None
        self._application = None
        self._message = None
        self._number_of_repetitions = None
        self._gap_between_repetitions = None
        self.discriminator = None

        if platform is not None:
            self.platform = platform
        if application is not None:
            self.application = application
        if message is not None:
            self.message = message
        if number_of_repetitions is not None:
            self.number_of_repetitions = number_of_repetitions
        if gap_between_repetitions is not None:
            self.gap_between_repetitions = gap_between_repetitions

    @property
    def platform(self):
        """Gets the platform of this FindDevice.  # noqa: E501

        Gets or sets device Platform.  # noqa: E501

        :return: The platform of this FindDevice.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this FindDevice.

        Gets or sets device Platform.  # noqa: E501

        :param platform: The platform of this FindDevice.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def application(self):
        """Gets the application of this FindDevice.  # noqa: E501

        Gets or sets application to which message has to be sent.  # noqa: E501

        :return: The application of this FindDevice.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this FindDevice.

        Gets or sets application to which message has to be sent.  # noqa: E501

        :param application: The application of this FindDevice.  # noqa: E501
        :type: str
        """

        self._application = application

    @property
    def message(self):
        """Gets the message of this FindDevice.  # noqa: E501

        Gets or sets message to be sent.  # noqa: E501

        :return: The message of this FindDevice.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FindDevice.

        Gets or sets message to be sent.  # noqa: E501

        :param message: The message of this FindDevice.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def number_of_repetitions(self):
        """Gets the number_of_repetitions of this FindDevice.  # noqa: E501

        Gets or sets no of repitition of the device ring.  # noqa: E501

        :return: The number_of_repetitions of this FindDevice.  # noqa: E501
        :rtype: str
        """
        return self._number_of_repetitions

    @number_of_repetitions.setter
    def number_of_repetitions(self, number_of_repetitions):
        """Sets the number_of_repetitions of this FindDevice.

        Gets or sets no of repitition of the device ring.  # noqa: E501

        :param number_of_repetitions: The number_of_repetitions of this FindDevice.  # noqa: E501
        :type: str
        """

        self._number_of_repetitions = number_of_repetitions

    @property
    def gap_between_repetitions(self):
        """Gets the gap_between_repetitions of this FindDevice.  # noqa: E501

        Gets or sets gap between each repitition.  # noqa: E501

        :return: The gap_between_repetitions of this FindDevice.  # noqa: E501
        :rtype: str
        """
        return self._gap_between_repetitions

    @gap_between_repetitions.setter
    def gap_between_repetitions(self, gap_between_repetitions):
        """Sets the gap_between_repetitions of this FindDevice.

        Gets or sets gap between each repitition.  # noqa: E501

        :param gap_between_repetitions: The gap_between_repetitions of this FindDevice.  # noqa: E501
        :type: str
        """

        self._gap_between_repetitions = gap_between_repetitions

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
        if issubclass(FindDevice, dict):
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
        if not isinstance(other, FindDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FindDevice):
            return True

        return self.to_dict() != other.to_dict()
