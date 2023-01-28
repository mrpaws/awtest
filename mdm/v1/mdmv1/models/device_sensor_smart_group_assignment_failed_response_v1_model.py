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


class DeviceSensorSmartGroupAssignmentFailedResponseV1Model(object):
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
        'error_code': 'int',
        'error_message': 'str',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_message': 'error_message',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, error_code=None, error_message=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """DeviceSensorSmartGroupAssignmentFailedResponseV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error_code = None
        self._error_message = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        self.error_code = error_code
        self.error_message = error_message
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def error_code(self):
        """Gets the error_code of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501

        Error code of the failure  # noqa: E501

        :return: The error_code of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.

        Error code of the failure  # noqa: E501

        :param error_code: The error_code of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501

        Error message  # noqa: E501

        :return: The error_message of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.

        Error message  # noqa: E501

        :param error_message: The error_message of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and error_message is None:
            raise ValueError("Invalid value for `error_message`, must not be `None`")  # noqa: E501

        self._error_message = error_message

    @property
    def id(self):
        """Gets the id of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this DeviceSensorSmartGroupAssignmentFailedResponseV1Model.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(DeviceSensorSmartGroupAssignmentFailedResponseV1Model, dict):
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
        if not isinstance(other, DeviceSensorSmartGroupAssignmentFailedResponseV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceSensorSmartGroupAssignmentFailedResponseV1Model):
            return True

        return self.to_dict() != other.to_dict()
