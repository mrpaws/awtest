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


class FailedBulkUpdateDeviceCustomAttributeResponseV1Model(object):
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
        'name': 'str',
        'application_group': 'str',
        'error_code': 'int',
        'message': 'str',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'application_group': 'applicationGroup',
        'error_code': 'errorCode',
        'message': 'message',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, name=None, application_group=None, error_code=None, message=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """FailedBulkUpdateDeviceCustomAttributeResponseV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._application_group = None
        self._error_code = None
        self._message = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        self.name = name
        self.application_group = application_group
        self.error_code = error_code
        self.message = message
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def name(self):
        """Gets the name of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501

        The custom attribute name  # noqa: E501

        :return: The name of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.

        The custom attribute name  # noqa: E501

        :param name: The name of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def application_group(self):
        """Gets the application_group of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501

        The custom attribute's application group  # noqa: E501

        :return: The application_group of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._application_group

    @application_group.setter
    def application_group(self, application_group):
        """Sets the application_group of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.

        The custom attribute's application group  # noqa: E501

        :param application_group: The application_group of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and application_group is None:
            raise ValueError("Invalid value for `application_group`, must not be `None`")  # noqa: E501

        self._application_group = application_group

    @property
    def error_code(self):
        """Gets the error_code of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501

        Error code for the failure  # noqa: E501

        :return: The error_code of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.

        Error code for the failure  # noqa: E501

        :param error_code: The error_code of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def message(self):
        """Gets the message of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501

        The error message  # noqa: E501

        :return: The message of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.

        The error message  # noqa: E501

        :param message: The message of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def id(self):
        """Gets the id of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this FailedBulkUpdateDeviceCustomAttributeResponseV1Model.  # noqa: E501
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
        if issubclass(FailedBulkUpdateDeviceCustomAttributeResponseV1Model, dict):
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
        if not isinstance(other, FailedBulkUpdateDeviceCustomAttributeResponseV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FailedBulkUpdateDeviceCustomAttributeResponseV1Model):
            return True

        return self.to_dict() != other.to_dict()