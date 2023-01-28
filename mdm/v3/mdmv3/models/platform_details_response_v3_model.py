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


class PlatformDetailsResponseV3Model(object):
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
        'device_type': 'int',
        'platform_name': 'str',
        'oem_info': 'str',
        'model_identifier': 'str',
        'model': 'str',
        'os_version': 'str'
    }

    attribute_map = {
        'device_type': 'device_type',
        'platform_name': 'platform_name',
        'oem_info': 'oem_info',
        'model_identifier': 'model_identifier',
        'model': 'model',
        'os_version': 'os_version'
    }

    def __init__(self, device_type=None, platform_name=None, oem_info=None, model_identifier=None, model=None, os_version=None, _configuration=None):  # noqa: E501
        """PlatformDetailsResponseV3Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_type = None
        self._platform_name = None
        self._oem_info = None
        self._model_identifier = None
        self._model = None
        self._os_version = None
        self.discriminator = None

        if device_type is not None:
            self.device_type = device_type
        if platform_name is not None:
            self.platform_name = platform_name
        if oem_info is not None:
            self.oem_info = oem_info
        if model_identifier is not None:
            self.model_identifier = model_identifier
        if model is not None:
            self.model = model
        if os_version is not None:
            self.os_version = os_version

    @property
    def device_type(self):
        """Gets the device_type of this PlatformDetailsResponseV3Model.  # noqa: E501

        Type of the device.  # noqa: E501

        :return: The device_type of this PlatformDetailsResponseV3Model.  # noqa: E501
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this PlatformDetailsResponseV3Model.

        Type of the device.  # noqa: E501

        :param device_type: The device_type of this PlatformDetailsResponseV3Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 100, 101, 102, 103, 104, 105, 200, 201]  # noqa: E501
        if (self._configuration.client_side_validation and
                device_type not in allowed_values):
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def platform_name(self):
        """Gets the platform_name of this PlatformDetailsResponseV3Model.  # noqa: E501

        Name of the platform.  # noqa: E501

        :return: The platform_name of this PlatformDetailsResponseV3Model.  # noqa: E501
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """Sets the platform_name of this PlatformDetailsResponseV3Model.

        Name of the platform.  # noqa: E501

        :param platform_name: The platform_name of this PlatformDetailsResponseV3Model.  # noqa: E501
        :type: str
        """

        self._platform_name = platform_name

    @property
    def oem_info(self):
        """Gets the oem_info of this PlatformDetailsResponseV3Model.  # noqa: E501

        Name of the device manufacturer.  # noqa: E501

        :return: The oem_info of this PlatformDetailsResponseV3Model.  # noqa: E501
        :rtype: str
        """
        return self._oem_info

    @oem_info.setter
    def oem_info(self, oem_info):
        """Sets the oem_info of this PlatformDetailsResponseV3Model.

        Name of the device manufacturer.  # noqa: E501

        :param oem_info: The oem_info of this PlatformDetailsResponseV3Model.  # noqa: E501
        :type: str
        """

        self._oem_info = oem_info

    @property
    def model_identifier(self):
        """Gets the model_identifier of this PlatformDetailsResponseV3Model.  # noqa: E501

        Device model identifier.  # noqa: E501

        :return: The model_identifier of this PlatformDetailsResponseV3Model.  # noqa: E501
        :rtype: str
        """
        return self._model_identifier

    @model_identifier.setter
    def model_identifier(self, model_identifier):
        """Sets the model_identifier of this PlatformDetailsResponseV3Model.

        Device model identifier.  # noqa: E501

        :param model_identifier: The model_identifier of this PlatformDetailsResponseV3Model.  # noqa: E501
        :type: str
        """

        self._model_identifier = model_identifier

    @property
    def model(self):
        """Gets the model of this PlatformDetailsResponseV3Model.  # noqa: E501

        Model name of the device.  # noqa: E501

        :return: The model of this PlatformDetailsResponseV3Model.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PlatformDetailsResponseV3Model.

        Model name of the device.  # noqa: E501

        :param model: The model of this PlatformDetailsResponseV3Model.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def os_version(self):
        """Gets the os_version of this PlatformDetailsResponseV3Model.  # noqa: E501

        Version of the operating system installed on the device.  # noqa: E501

        :return: The os_version of this PlatformDetailsResponseV3Model.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this PlatformDetailsResponseV3Model.

        Version of the operating system installed on the device.  # noqa: E501

        :param os_version: The os_version of this PlatformDetailsResponseV3Model.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

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
        if issubclass(PlatformDetailsResponseV3Model, dict):
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
        if not isinstance(other, PlatformDetailsResponseV3Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlatformDetailsResponseV3Model):
            return True

        return self.to_dict() != other.to_dict()