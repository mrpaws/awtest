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


class DeviceDataV2Model(object):
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
        'udid': 'str',
        'uuid': 'str',
        'server': 'DeviceActionModel_'
    }

    attribute_map = {
        'udid': 'udid',
        'uuid': 'uuid',
        'server': 'server'
    }

    def __init__(self, udid=None, uuid=None, server=None, _configuration=None):  # noqa: E501
        """DeviceDataV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._udid = None
        self._uuid = None
        self._server = None
        self.discriminator = None

        if udid is not None:
            self.udid = udid
        if uuid is not None:
            self.uuid = uuid
        if server is not None:
            self.server = server

    @property
    def udid(self):
        """Gets the udid of this DeviceDataV2Model.  # noqa: E501

        Gets or sets Device UDID.  # noqa: E501

        :return: The udid of this DeviceDataV2Model.  # noqa: E501
        :rtype: str
        """
        return self._udid

    @udid.setter
    def udid(self, udid):
        """Sets the udid of this DeviceDataV2Model.

        Gets or sets Device UDID.  # noqa: E501

        :param udid: The udid of this DeviceDataV2Model.  # noqa: E501
        :type: str
        """

        self._udid = udid

    @property
    def uuid(self):
        """Gets the uuid of this DeviceDataV2Model.  # noqa: E501

        Gets or sets Device UUID.  # noqa: E501

        :return: The uuid of this DeviceDataV2Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DeviceDataV2Model.

        Gets or sets Device UUID.  # noqa: E501

        :param uuid: The uuid of this DeviceDataV2Model.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def server(self):
        """Gets the server of this DeviceDataV2Model.  # noqa: E501

        Gets or sets the server action.  # noqa: E501

        :return: The server of this DeviceDataV2Model.  # noqa: E501
        :rtype: DeviceActionModel_
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this DeviceDataV2Model.

        Gets or sets the server action.  # noqa: E501

        :param server: The server of this DeviceDataV2Model.  # noqa: E501
        :type: DeviceActionModel_
        """

        self._server = server

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
        if issubclass(DeviceDataV2Model, dict):
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
        if not isinstance(other, DeviceDataV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceDataV2Model):
            return True

        return self.to_dict() != other.to_dict()
