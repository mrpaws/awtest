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


class OSUpdateResultModel(object):
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
        'os_update_list': 'list[OSUpdateModel]',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'os_update_list': 'OSUpdateList',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, os_update_list=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """OSUpdateResultModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._os_update_list = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if os_update_list is not None:
            self.os_update_list = os_update_list
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def os_update_list(self):
        """Gets the os_update_list of this OSUpdateResultModel.  # noqa: E501

        The list of OS updates available for a device  # noqa: E501

        :return: The os_update_list of this OSUpdateResultModel.  # noqa: E501
        :rtype: list[OSUpdateModel]
        """
        return self._os_update_list

    @os_update_list.setter
    def os_update_list(self, os_update_list):
        """Sets the os_update_list of this OSUpdateResultModel.

        The list of OS updates available for a device  # noqa: E501

        :param os_update_list: The os_update_list of this OSUpdateResultModel.  # noqa: E501
        :type: list[OSUpdateModel]
        """

        self._os_update_list = os_update_list

    @property
    def id(self):
        """Gets the id of this OSUpdateResultModel.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this OSUpdateResultModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OSUpdateResultModel.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this OSUpdateResultModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this OSUpdateResultModel.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this OSUpdateResultModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this OSUpdateResultModel.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this OSUpdateResultModel.  # noqa: E501
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
        if issubclass(OSUpdateResultModel, dict):
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
        if not isinstance(other, OSUpdateResultModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OSUpdateResultModel):
            return True

        return self.to_dict() != other.to_dict()
