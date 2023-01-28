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


class DeviceCellularNetworkInfo_(object):
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
        'cellular_technology': 'int',
        'current_operator': 'str',
        'subscriber_carrier_network': 'str',
        'current_sim': 'str',
        'approved_sims': 'list[DeviceSimCard]',
        'carrier_version': 'str',
        'signal_strength': 'str',
        'device_mcc': 'DeviceMcc_',
        'device_mnc': 'DeviceMnc_'
    }

    attribute_map = {
        'cellular_technology': 'CellularTechnology',
        'current_operator': 'CurrentOperator',
        'subscriber_carrier_network': 'SubscriberCarrierNetwork',
        'current_sim': 'CurrentSIM',
        'approved_sims': 'ApprovedSims',
        'carrier_version': 'CarrierVersion',
        'signal_strength': 'SignalStrength',
        'device_mcc': 'DeviceMCC',
        'device_mnc': 'DeviceMNC'
    }

    def __init__(self, cellular_technology=None, current_operator=None, subscriber_carrier_network=None, current_sim=None, approved_sims=None, carrier_version=None, signal_strength=None, device_mcc=None, device_mnc=None, _configuration=None):  # noqa: E501
        """DeviceCellularNetworkInfo_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cellular_technology = None
        self._current_operator = None
        self._subscriber_carrier_network = None
        self._current_sim = None
        self._approved_sims = None
        self._carrier_version = None
        self._signal_strength = None
        self._device_mcc = None
        self._device_mnc = None
        self.discriminator = None

        if cellular_technology is not None:
            self.cellular_technology = cellular_technology
        if current_operator is not None:
            self.current_operator = current_operator
        if subscriber_carrier_network is not None:
            self.subscriber_carrier_network = subscriber_carrier_network
        if current_sim is not None:
            self.current_sim = current_sim
        if approved_sims is not None:
            self.approved_sims = approved_sims
        if carrier_version is not None:
            self.carrier_version = carrier_version
        if signal_strength is not None:
            self.signal_strength = signal_strength
        if device_mcc is not None:
            self.device_mcc = device_mcc
        if device_mnc is not None:
            self.device_mnc = device_mnc

    @property
    def cellular_technology(self):
        """Gets the cellular_technology of this DeviceCellularNetworkInfo_.  # noqa: E501

        Gets or sets device's cellular technology.  # noqa: E501

        :return: The cellular_technology of this DeviceCellularNetworkInfo_.  # noqa: E501
        :rtype: int
        """
        return self._cellular_technology

    @cellular_technology.setter
    def cellular_technology(self, cellular_technology):
        """Sets the cellular_technology of this DeviceCellularNetworkInfo_.

        Gets or sets device's cellular technology.  # noqa: E501

        :param cellular_technology: The cellular_technology of this DeviceCellularNetworkInfo_.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4]  # noqa: E501
        if (self._configuration.client_side_validation and
                cellular_technology not in allowed_values):
            raise ValueError(
                "Invalid value for `cellular_technology` ({0}), must be one of {1}"  # noqa: E501
                .format(cellular_technology, allowed_values)
            )

        self._cellular_technology = cellular_technology

    @property
    def current_operator(self):
        """Gets the current_operator of this DeviceCellularNetworkInfo_.  # noqa: E501

        Gets or sets operator/Carrier.  # noqa: E501

        :return: The current_operator of this DeviceCellularNetworkInfo_.  # noqa: E501
        :rtype: str
        """
        return self._current_operator

    @current_operator.setter
    def current_operator(self, current_operator):
        """Sets the current_operator of this DeviceCellularNetworkInfo_.

        Gets or sets operator/Carrier.  # noqa: E501

        :param current_operator: The current_operator of this DeviceCellularNetworkInfo_.  # noqa: E501
        :type: str
        """

        self._current_operator = current_operator

    @property
    def subscriber_carrier_network(self):
        """Gets the subscriber_carrier_network of this DeviceCellularNetworkInfo_.  # noqa: E501

        Gets or sets home Operator/Carrier.  # noqa: E501

        :return: The subscriber_carrier_network of this DeviceCellularNetworkInfo_.  # noqa: E501
        :rtype: str
        """
        return self._subscriber_carrier_network

    @subscriber_carrier_network.setter
    def subscriber_carrier_network(self, subscriber_carrier_network):
        """Sets the subscriber_carrier_network of this DeviceCellularNetworkInfo_.

        Gets or sets home Operator/Carrier.  # noqa: E501

        :param subscriber_carrier_network: The subscriber_carrier_network of this DeviceCellularNetworkInfo_.  # noqa: E501
        :type: str
        """

        self._subscriber_carrier_network = subscriber_carrier_network

    @property
    def current_sim(self):
        """Gets the current_sim of this DeviceCellularNetworkInfo_.  # noqa: E501

        Gets or sets circuit card identifer.  # noqa: E501

        :return: The current_sim of this DeviceCellularNetworkInfo_.  # noqa: E501
        :rtype: str
        """
        return self._current_sim

    @current_sim.setter
    def current_sim(self, current_sim):
        """Sets the current_sim of this DeviceCellularNetworkInfo_.

        Gets or sets circuit card identifer.  # noqa: E501

        :param current_sim: The current_sim of this DeviceCellularNetworkInfo_.  # noqa: E501
        :type: str
        """

        self._current_sim = current_sim

    @property
    def approved_sims(self):
        """Gets the approved_sims of this DeviceCellularNetworkInfo_.  # noqa: E501

        Gets or sets device Approved SIM(s).  # noqa: E501

        :return: The approved_sims of this DeviceCellularNetworkInfo_.  # noqa: E501
        :rtype: list[DeviceSimCard]
        """
        return self._approved_sims

    @approved_sims.setter
    def approved_sims(self, approved_sims):
        """Sets the approved_sims of this DeviceCellularNetworkInfo_.

        Gets or sets device Approved SIM(s).  # noqa: E501

        :param approved_sims: The approved_sims of this DeviceCellularNetworkInfo_.  # noqa: E501
        :type: list[DeviceSimCard]
        """

        self._approved_sims = approved_sims

    @property
    def carrier_version(self):
        """Gets the carrier_version of this DeviceCellularNetworkInfo_.  # noqa: E501

        Gets or sets carrier settings version.  # noqa: E501

        :return: The carrier_version of this DeviceCellularNetworkInfo_.  # noqa: E501
        :rtype: str
        """
        return self._carrier_version

    @carrier_version.setter
    def carrier_version(self, carrier_version):
        """Sets the carrier_version of this DeviceCellularNetworkInfo_.

        Gets or sets carrier settings version.  # noqa: E501

        :param carrier_version: The carrier_version of this DeviceCellularNetworkInfo_.  # noqa: E501
        :type: str
        """

        self._carrier_version = carrier_version

    @property
    def signal_strength(self):
        """Gets the signal_strength of this DeviceCellularNetworkInfo_.  # noqa: E501

        Gets or sets cellular signal strength.  # noqa: E501

        :return: The signal_strength of this DeviceCellularNetworkInfo_.  # noqa: E501
        :rtype: str
        """
        return self._signal_strength

    @signal_strength.setter
    def signal_strength(self, signal_strength):
        """Sets the signal_strength of this DeviceCellularNetworkInfo_.

        Gets or sets cellular signal strength.  # noqa: E501

        :param signal_strength: The signal_strength of this DeviceCellularNetworkInfo_.  # noqa: E501
        :type: str
        """

        self._signal_strength = signal_strength

    @property
    def device_mcc(self):
        """Gets the device_mcc of this DeviceCellularNetworkInfo_.  # noqa: E501

        Gets or sets this gives the information about Device Mobile Country Code i.e.,SIM and Current MCC.  # noqa: E501

        :return: The device_mcc of this DeviceCellularNetworkInfo_.  # noqa: E501
        :rtype: DeviceMcc_
        """
        return self._device_mcc

    @device_mcc.setter
    def device_mcc(self, device_mcc):
        """Sets the device_mcc of this DeviceCellularNetworkInfo_.

        Gets or sets this gives the information about Device Mobile Country Code i.e.,SIM and Current MCC.  # noqa: E501

        :param device_mcc: The device_mcc of this DeviceCellularNetworkInfo_.  # noqa: E501
        :type: DeviceMcc_
        """

        self._device_mcc = device_mcc

    @property
    def device_mnc(self):
        """Gets the device_mnc of this DeviceCellularNetworkInfo_.  # noqa: E501

        Gets or sets this gives the information about Device Mobile Network Code i.e., SIM and Current MNC.  # noqa: E501

        :return: The device_mnc of this DeviceCellularNetworkInfo_.  # noqa: E501
        :rtype: DeviceMnc_
        """
        return self._device_mnc

    @device_mnc.setter
    def device_mnc(self, device_mnc):
        """Sets the device_mnc of this DeviceCellularNetworkInfo_.

        Gets or sets this gives the information about Device Mobile Network Code i.e., SIM and Current MNC.  # noqa: E501

        :param device_mnc: The device_mnc of this DeviceCellularNetworkInfo_.  # noqa: E501
        :type: DeviceMnc_
        """

        self._device_mnc = device_mnc

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
        if issubclass(DeviceCellularNetworkInfo_, dict):
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
        if not isinstance(other, DeviceCellularNetworkInfo_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceCellularNetworkInfo_):
            return True

        return self.to_dict() != other.to_dict()