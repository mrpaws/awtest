# coding: utf-8

"""
    MDM API V3

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv3.configuration import Configuration


class DeviceCellularInfoModelV2(object):
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
        'carrier_name': 'str',
        'card_id': 'str',
        'device_mmc': 'DeviceMccV2',
        'phone_number': 'str',
        'is_roaming': 'bool'
    }

    attribute_map = {
        'carrier_name': 'carrier_name',
        'card_id': 'card_id',
        'device_mmc': 'device_mmc',
        'phone_number': 'phone_number',
        'is_roaming': 'is_roaming'
    }

    def __init__(self, carrier_name=None, card_id=None, device_mmc=None, phone_number=None, is_roaming=None, _configuration=None):  # noqa: E501
        """DeviceCellularInfoModelV2 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._carrier_name = None
        self._card_id = None
        self._device_mmc = None
        self._phone_number = None
        self._is_roaming = None
        self.discriminator = None

        if carrier_name is not None:
            self.carrier_name = carrier_name
        if card_id is not None:
            self.card_id = card_id
        if device_mmc is not None:
            self.device_mmc = device_mmc
        if phone_number is not None:
            self.phone_number = phone_number
        if is_roaming is not None:
            self.is_roaming = is_roaming

    @property
    def carrier_name(self):
        """Gets the carrier_name of this DeviceCellularInfoModelV2.  # noqa: E501

        Operator / Carrier name.  # noqa: E501

        :return: The carrier_name of this DeviceCellularInfoModelV2.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this DeviceCellularInfoModelV2.

        Operator / Carrier name.  # noqa: E501

        :param carrier_name: The carrier_name of this DeviceCellularInfoModelV2.  # noqa: E501
        :type: str
        """

        self._carrier_name = carrier_name

    @property
    def card_id(self):
        """Gets the card_id of this DeviceCellularInfoModelV2.  # noqa: E501

        Circuit card identifier.  # noqa: E501

        :return: The card_id of this DeviceCellularInfoModelV2.  # noqa: E501
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this DeviceCellularInfoModelV2.

        Circuit card identifier.  # noqa: E501

        :param card_id: The card_id of this DeviceCellularInfoModelV2.  # noqa: E501
        :type: str
        """

        self._card_id = card_id

    @property
    def device_mmc(self):
        """Gets the device_mmc of this DeviceCellularInfoModelV2.  # noqa: E501

        Information about Device Mobile Country Code.  # noqa: E501

        :return: The device_mmc of this DeviceCellularInfoModelV2.  # noqa: E501
        :rtype: DeviceMccV2
        """
        return self._device_mmc

    @device_mmc.setter
    def device_mmc(self, device_mmc):
        """Sets the device_mmc of this DeviceCellularInfoModelV2.

        Information about Device Mobile Country Code.  # noqa: E501

        :param device_mmc: The device_mmc of this DeviceCellularInfoModelV2.  # noqa: E501
        :type: DeviceMccV2
        """

        self._device_mmc = device_mmc

    @property
    def phone_number(self):
        """Gets the phone_number of this DeviceCellularInfoModelV2.  # noqa: E501

        Phone number of the device.  # noqa: E501

        :return: The phone_number of this DeviceCellularInfoModelV2.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this DeviceCellularInfoModelV2.

        Phone number of the device.  # noqa: E501

        :param phone_number: The phone_number of this DeviceCellularInfoModelV2.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def is_roaming(self):
        """Gets the is_roaming of this DeviceCellularInfoModelV2.  # noqa: E501

        This gives information about the roaming status of the device.  # noqa: E501

        :return: The is_roaming of this DeviceCellularInfoModelV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_roaming

    @is_roaming.setter
    def is_roaming(self, is_roaming):
        """Sets the is_roaming of this DeviceCellularInfoModelV2.

        This gives information about the roaming status of the device.  # noqa: E501

        :param is_roaming: The is_roaming of this DeviceCellularInfoModelV2.  # noqa: E501
        :type: bool
        """

        self._is_roaming = is_roaming

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
        if issubclass(DeviceCellularInfoModelV2, dict):
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
        if not isinstance(other, DeviceCellularInfoModelV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceCellularInfoModelV2):
            return True

        return self.to_dict() != other.to_dict()
