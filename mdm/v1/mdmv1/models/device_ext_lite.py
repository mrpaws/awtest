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


class DeviceExtLite(object):
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
        'device_id': 'int',
        'device_uuid': 'str',
        'udid': 'str',
        'device_friendly_name': 'str',
        'organization_group_id': 'int',
        'organization_group_uuid': 'str',
        'device_network_info': 'list[DeviceNetworkInfo]',
        'last_seen': 'datetime',
        'custom_attributes': 'list[DeviceCustomAttribute]'
    }

    attribute_map = {
        'device_id': 'DeviceId',
        'device_uuid': 'DeviceUuid',
        'udid': 'Udid',
        'device_friendly_name': 'DeviceFriendlyName',
        'organization_group_id': 'OrganizationGroupId',
        'organization_group_uuid': 'OrganizationGroupUuid',
        'device_network_info': 'DeviceNetworkInfo',
        'last_seen': 'LastSeen',
        'custom_attributes': 'CustomAttributes'
    }

    def __init__(self, device_id=None, device_uuid=None, udid=None, device_friendly_name=None, organization_group_id=None, organization_group_uuid=None, device_network_info=None, last_seen=None, custom_attributes=None, _configuration=None):  # noqa: E501
        """DeviceExtLite - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_id = None
        self._device_uuid = None
        self._udid = None
        self._device_friendly_name = None
        self._organization_group_id = None
        self._organization_group_uuid = None
        self._device_network_info = None
        self._last_seen = None
        self._custom_attributes = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if device_uuid is not None:
            self.device_uuid = device_uuid
        if udid is not None:
            self.udid = udid
        if device_friendly_name is not None:
            self.device_friendly_name = device_friendly_name
        if organization_group_id is not None:
            self.organization_group_id = organization_group_id
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if device_network_info is not None:
            self.device_network_info = device_network_info
        if last_seen is not None:
            self.last_seen = last_seen
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes

    @property
    def device_id(self):
        """Gets the device_id of this DeviceExtLite.  # noqa: E501

        Gets or sets device identifier.  # noqa: E501

        :return: The device_id of this DeviceExtLite.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceExtLite.

        Gets or sets device identifier.  # noqa: E501

        :param device_id: The device_id of this DeviceExtLite.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def device_uuid(self):
        """Gets the device_uuid of this DeviceExtLite.  # noqa: E501

        Gets or sets device UUID.  # noqa: E501

        :return: The device_uuid of this DeviceExtLite.  # noqa: E501
        :rtype: str
        """
        return self._device_uuid

    @device_uuid.setter
    def device_uuid(self, device_uuid):
        """Sets the device_uuid of this DeviceExtLite.

        Gets or sets device UUID.  # noqa: E501

        :param device_uuid: The device_uuid of this DeviceExtLite.  # noqa: E501
        :type: str
        """

        self._device_uuid = device_uuid

    @property
    def udid(self):
        """Gets the udid of this DeviceExtLite.  # noqa: E501

        Gets or sets the device's unique identifier.  # noqa: E501

        :return: The udid of this DeviceExtLite.  # noqa: E501
        :rtype: str
        """
        return self._udid

    @udid.setter
    def udid(self, udid):
        """Sets the udid of this DeviceExtLite.

        Gets or sets the device's unique identifier.  # noqa: E501

        :param udid: The udid of this DeviceExtLite.  # noqa: E501
        :type: str
        """

        self._udid = udid

    @property
    def device_friendly_name(self):
        """Gets the device_friendly_name of this DeviceExtLite.  # noqa: E501

        Gets or sets the friendly name.  # noqa: E501

        :return: The device_friendly_name of this DeviceExtLite.  # noqa: E501
        :rtype: str
        """
        return self._device_friendly_name

    @device_friendly_name.setter
    def device_friendly_name(self, device_friendly_name):
        """Sets the device_friendly_name of this DeviceExtLite.

        Gets or sets the friendly name.  # noqa: E501

        :param device_friendly_name: The device_friendly_name of this DeviceExtLite.  # noqa: E501
        :type: str
        """

        self._device_friendly_name = device_friendly_name

    @property
    def organization_group_id(self):
        """Gets the organization_group_id of this DeviceExtLite.  # noqa: E501

        Gets or sets the Organization Group ID the device belongs to.  # noqa: E501

        :return: The organization_group_id of this DeviceExtLite.  # noqa: E501
        :rtype: int
        """
        return self._organization_group_id

    @organization_group_id.setter
    def organization_group_id(self, organization_group_id):
        """Sets the organization_group_id of this DeviceExtLite.

        Gets or sets the Organization Group ID the device belongs to.  # noqa: E501

        :param organization_group_id: The organization_group_id of this DeviceExtLite.  # noqa: E501
        :type: int
        """

        self._organization_group_id = organization_group_id

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this DeviceExtLite.  # noqa: E501

        Gets or sets the Organization Group UUID the device belongs to.  # noqa: E501

        :return: The organization_group_uuid of this DeviceExtLite.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this DeviceExtLite.

        Gets or sets the Organization Group UUID the device belongs to.  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this DeviceExtLite.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def device_network_info(self):
        """Gets the device_network_info of this DeviceExtLite.  # noqa: E501

        Gets or sets network information of the current device.  # noqa: E501

        :return: The device_network_info of this DeviceExtLite.  # noqa: E501
        :rtype: list[DeviceNetworkInfo]
        """
        return self._device_network_info

    @device_network_info.setter
    def device_network_info(self, device_network_info):
        """Sets the device_network_info of this DeviceExtLite.

        Gets or sets network information of the current device.  # noqa: E501

        :param device_network_info: The device_network_info of this DeviceExtLite.  # noqa: E501
        :type: list[DeviceNetworkInfo]
        """

        self._device_network_info = device_network_info

    @property
    def last_seen(self):
        """Gets the last_seen of this DeviceExtLite.  # noqa: E501

        Gets or sets the time the device last reported any status with AirWatch.  # noqa: E501

        :return: The last_seen of this DeviceExtLite.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this DeviceExtLite.

        Gets or sets the time the device last reported any status with AirWatch.  # noqa: E501

        :param last_seen: The last_seen of this DeviceExtLite.  # noqa: E501
        :type: datetime
        """

        self._last_seen = last_seen

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this DeviceExtLite.  # noqa: E501

        Gets or sets details of the CustomAttributes, which are assigned to the Current Device.  # noqa: E501

        :return: The custom_attributes of this DeviceExtLite.  # noqa: E501
        :rtype: list[DeviceCustomAttribute]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this DeviceExtLite.

        Gets or sets details of the CustomAttributes, which are assigned to the Current Device.  # noqa: E501

        :param custom_attributes: The custom_attributes of this DeviceExtLite.  # noqa: E501
        :type: list[DeviceCustomAttribute]
        """

        self._custom_attributes = custom_attributes

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
        if issubclass(DeviceExtLite, dict):
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
        if not isinstance(other, DeviceExtLite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceExtLite):
            return True

        return self.to_dict() != other.to_dict()