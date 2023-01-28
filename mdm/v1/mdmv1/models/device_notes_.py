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


class DeviceNotes_(object):
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
        'id': 'int',
        'device_id': 'int',
        'note': 'str',
        'modified_on': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'device_id': 'DeviceId',
        'note': 'Note',
        'modified_on': 'ModifiedOn'
    }

    def __init__(self, id=None, device_id=None, note=None, modified_on=None, _configuration=None):  # noqa: E501
        """DeviceNotes_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._device_id = None
        self._note = None
        self._modified_on = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if device_id is not None:
            self.device_id = device_id
        if note is not None:
            self.note = note
        if modified_on is not None:
            self.modified_on = modified_on

    @property
    def id(self):
        """Gets the id of this DeviceNotes_.  # noqa: E501


        :return: The id of this DeviceNotes_.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceNotes_.


        :param id: The id of this DeviceNotes_.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device_id(self):
        """Gets the device_id of this DeviceNotes_.  # noqa: E501


        :return: The device_id of this DeviceNotes_.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceNotes_.


        :param device_id: The device_id of this DeviceNotes_.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def note(self):
        """Gets the note of this DeviceNotes_.  # noqa: E501


        :return: The note of this DeviceNotes_.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this DeviceNotes_.


        :param note: The note of this DeviceNotes_.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def modified_on(self):
        """Gets the modified_on of this DeviceNotes_.  # noqa: E501


        :return: The modified_on of this DeviceNotes_.  # noqa: E501
        :rtype: str
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this DeviceNotes_.


        :param modified_on: The modified_on of this DeviceNotes_.  # noqa: E501
        :type: str
        """

        self._modified_on = modified_on

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
        if issubclass(DeviceNotes_, dict):
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
        if not isinstance(other, DeviceNotes_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceNotes_):
            return True

        return self.to_dict() != other.to_dict()
