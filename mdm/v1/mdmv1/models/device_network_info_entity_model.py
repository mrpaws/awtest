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


class DeviceNetworkInfoEntityModel(object):
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
        'phone_number': 'str',
        'roaming_status': 'bool',
        'data_roaming_enabled': 'bool',
        'voice_roaming_enabled': 'bool',
        'ip_address': 'dict(str, str)',
        'cellular_network_info': 'DeviceCellularNetworkInfo_',
        'wifi_info': 'DeviceWifiInfo_',
        'public_ip_address': 'str',
        'device_network_info': 'list[DeviceNetworkInfo]',
        'service_subscription': 'list[ServiceSubscription]'
    }

    attribute_map = {
        'phone_number': 'PhoneNumber',
        'roaming_status': 'RoamingStatus',
        'data_roaming_enabled': 'DataRoamingEnabled',
        'voice_roaming_enabled': 'VoiceRoamingEnabled',
        'ip_address': 'IPAddress',
        'cellular_network_info': 'CellularNetworkInfo',
        'wifi_info': 'WifiInfo',
        'public_ip_address': 'PublicIPAddress',
        'device_network_info': 'DeviceNetworkInfo',
        'service_subscription': 'ServiceSubscription'
    }

    def __init__(self, phone_number=None, roaming_status=None, data_roaming_enabled=None, voice_roaming_enabled=None, ip_address=None, cellular_network_info=None, wifi_info=None, public_ip_address=None, device_network_info=None, service_subscription=None, _configuration=None):  # noqa: E501
        """DeviceNetworkInfoEntityModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._phone_number = None
        self._roaming_status = None
        self._data_roaming_enabled = None
        self._voice_roaming_enabled = None
        self._ip_address = None
        self._cellular_network_info = None
        self._wifi_info = None
        self._public_ip_address = None
        self._device_network_info = None
        self._service_subscription = None
        self.discriminator = None

        if phone_number is not None:
            self.phone_number = phone_number
        if roaming_status is not None:
            self.roaming_status = roaming_status
        if data_roaming_enabled is not None:
            self.data_roaming_enabled = data_roaming_enabled
        if voice_roaming_enabled is not None:
            self.voice_roaming_enabled = voice_roaming_enabled
        if ip_address is not None:
            self.ip_address = ip_address
        if cellular_network_info is not None:
            self.cellular_network_info = cellular_network_info
        if wifi_info is not None:
            self.wifi_info = wifi_info
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if device_network_info is not None:
            self.device_network_info = device_network_info
        if service_subscription is not None:
            self.service_subscription = service_subscription

    @property
    def phone_number(self):
        """Gets the phone_number of this DeviceNetworkInfoEntityModel.  # noqa: E501

        Gets or sets phone number of the device.  # noqa: E501

        :return: The phone_number of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this DeviceNetworkInfoEntityModel.

        Gets or sets phone number of the device.  # noqa: E501

        :param phone_number: The phone_number of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def roaming_status(self):
        """Gets the roaming_status of this DeviceNetworkInfoEntityModel.  # noqa: E501

        Gets or sets a value indicating whether whether roaming is enabled or not.  # noqa: E501

        :return: The roaming_status of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :rtype: bool
        """
        return self._roaming_status

    @roaming_status.setter
    def roaming_status(self, roaming_status):
        """Sets the roaming_status of this DeviceNetworkInfoEntityModel.

        Gets or sets a value indicating whether whether roaming is enabled or not.  # noqa: E501

        :param roaming_status: The roaming_status of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :type: bool
        """

        self._roaming_status = roaming_status

    @property
    def data_roaming_enabled(self):
        """Gets the data_roaming_enabled of this DeviceNetworkInfoEntityModel.  # noqa: E501

        Gets or sets a value indicating whether whether data roaming is enabled or not.  # noqa: E501

        :return: The data_roaming_enabled of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :rtype: bool
        """
        return self._data_roaming_enabled

    @data_roaming_enabled.setter
    def data_roaming_enabled(self, data_roaming_enabled):
        """Sets the data_roaming_enabled of this DeviceNetworkInfoEntityModel.

        Gets or sets a value indicating whether whether data roaming is enabled or not.  # noqa: E501

        :param data_roaming_enabled: The data_roaming_enabled of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :type: bool
        """

        self._data_roaming_enabled = data_roaming_enabled

    @property
    def voice_roaming_enabled(self):
        """Gets the voice_roaming_enabled of this DeviceNetworkInfoEntityModel.  # noqa: E501

        Gets or sets a value indicating whether whether voice roaming is enabled or not.  # noqa: E501

        :return: The voice_roaming_enabled of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :rtype: bool
        """
        return self._voice_roaming_enabled

    @voice_roaming_enabled.setter
    def voice_roaming_enabled(self, voice_roaming_enabled):
        """Sets the voice_roaming_enabled of this DeviceNetworkInfoEntityModel.

        Gets or sets a value indicating whether whether voice roaming is enabled or not.  # noqa: E501

        :param voice_roaming_enabled: The voice_roaming_enabled of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :type: bool
        """

        self._voice_roaming_enabled = voice_roaming_enabled

    @property
    def ip_address(self):
        """Gets the ip_address of this DeviceNetworkInfoEntityModel.  # noqa: E501

        Gets or sets the ip address.  # noqa: E501

        :return: The ip_address of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DeviceNetworkInfoEntityModel.

        Gets or sets the ip address.  # noqa: E501

        :param ip_address: The ip_address of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :type: dict(str, str)
        """

        self._ip_address = ip_address

    @property
    def cellular_network_info(self):
        """Gets the cellular_network_info of this DeviceNetworkInfoEntityModel.  # noqa: E501

        Gets or sets cellular information of the device.  # noqa: E501

        :return: The cellular_network_info of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :rtype: DeviceCellularNetworkInfo_
        """
        return self._cellular_network_info

    @cellular_network_info.setter
    def cellular_network_info(self, cellular_network_info):
        """Sets the cellular_network_info of this DeviceNetworkInfoEntityModel.

        Gets or sets cellular information of the device.  # noqa: E501

        :param cellular_network_info: The cellular_network_info of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :type: DeviceCellularNetworkInfo_
        """

        self._cellular_network_info = cellular_network_info

    @property
    def wifi_info(self):
        """Gets the wifi_info of this DeviceNetworkInfoEntityModel.  # noqa: E501

        Gets or sets wifi information of the device.  # noqa: E501

        :return: The wifi_info of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :rtype: DeviceWifiInfo_
        """
        return self._wifi_info

    @wifi_info.setter
    def wifi_info(self, wifi_info):
        """Sets the wifi_info of this DeviceNetworkInfoEntityModel.

        Gets or sets wifi information of the device.  # noqa: E501

        :param wifi_info: The wifi_info of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :type: DeviceWifiInfo_
        """

        self._wifi_info = wifi_info

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this DeviceNetworkInfoEntityModel.  # noqa: E501

        Gets or sets public IP address of the device.  # noqa: E501

        :return: The public_ip_address of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this DeviceNetworkInfoEntityModel.

        Gets or sets public IP address of the device.  # noqa: E501

        :param public_ip_address: The public_ip_address of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :type: str
        """

        self._public_ip_address = public_ip_address

    @property
    def device_network_info(self):
        """Gets the device_network_info of this DeviceNetworkInfoEntityModel.  # noqa: E501

        Gets or sets the device network information of the device.  # noqa: E501

        :return: The device_network_info of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :rtype: list[DeviceNetworkInfo]
        """
        return self._device_network_info

    @device_network_info.setter
    def device_network_info(self, device_network_info):
        """Sets the device_network_info of this DeviceNetworkInfoEntityModel.

        Gets or sets the device network information of the device.  # noqa: E501

        :param device_network_info: The device_network_info of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :type: list[DeviceNetworkInfo]
        """

        self._device_network_info = device_network_info

    @property
    def service_subscription(self):
        """Gets the service_subscription of this DeviceNetworkInfoEntityModel.  # noqa: E501

        Gets or sets the device Service Subscription information of the device.  # noqa: E501

        :return: The service_subscription of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :rtype: list[ServiceSubscription]
        """
        return self._service_subscription

    @service_subscription.setter
    def service_subscription(self, service_subscription):
        """Sets the service_subscription of this DeviceNetworkInfoEntityModel.

        Gets or sets the device Service Subscription information of the device.  # noqa: E501

        :param service_subscription: The service_subscription of this DeviceNetworkInfoEntityModel.  # noqa: E501
        :type: list[ServiceSubscription]
        """

        self._service_subscription = service_subscription

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
        if issubclass(DeviceNetworkInfoEntityModel, dict):
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
        if not isinstance(other, DeviceNetworkInfoEntityModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceNetworkInfoEntityModel):
            return True

        return self.to_dict() != other.to_dict()
