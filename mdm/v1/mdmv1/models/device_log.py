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


class DeviceLog(object):
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
        'uuid': 'str',
        'generated_at': 'str',
        'log_data': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'generated_at': 'generated_at',
        'log_data': 'log_data'
    }

    def __init__(self, uuid=None, generated_at=None, log_data=None, _configuration=None):  # noqa: E501
        """DeviceLog - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._uuid = None
        self._generated_at = None
        self._log_data = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if generated_at is not None:
            self.generated_at = generated_at
        if log_data is not None:
            self.log_data = log_data

    @property
    def uuid(self):
        """Gets the uuid of this DeviceLog.  # noqa: E501


        :return: The uuid of this DeviceLog.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DeviceLog.


        :param uuid: The uuid of this DeviceLog.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def generated_at(self):
        """Gets the generated_at of this DeviceLog.  # noqa: E501


        :return: The generated_at of this DeviceLog.  # noqa: E501
        :rtype: str
        """
        return self._generated_at

    @generated_at.setter
    def generated_at(self, generated_at):
        """Sets the generated_at of this DeviceLog.


        :param generated_at: The generated_at of this DeviceLog.  # noqa: E501
        :type: str
        """

        self._generated_at = generated_at

    @property
    def log_data(self):
        """Gets the log_data of this DeviceLog.  # noqa: E501


        :return: The log_data of this DeviceLog.  # noqa: E501
        :rtype: str
        """
        return self._log_data

    @log_data.setter
    def log_data(self, log_data):
        """Sets the log_data of this DeviceLog.


        :param log_data: The log_data of this DeviceLog.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                log_data is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', log_data)):  # noqa: E501
            raise ValueError(r"Invalid value for `log_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._log_data = log_data

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
        if issubclass(DeviceLog, dict):
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
        if not isinstance(other, DeviceLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceLog):
            return True

        return self.to_dict() != other.to_dict()
