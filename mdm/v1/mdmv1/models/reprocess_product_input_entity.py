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


class ReprocessProductInputEntity(object):
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
        'force_flag': 'bool',
        'device_ids': 'list[ReprocessProductDeviceInputEntity]',
        'product_id': 'int'
    }

    attribute_map = {
        'force_flag': 'ForceFlag',
        'device_ids': 'DeviceIds',
        'product_id': 'ProductID'
    }

    def __init__(self, force_flag=None, device_ids=None, product_id=None, _configuration=None):  # noqa: E501
        """ReprocessProductInputEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._force_flag = None
        self._device_ids = None
        self._product_id = None
        self.discriminator = None

        if force_flag is not None:
            self.force_flag = force_flag
        if device_ids is not None:
            self.device_ids = device_ids
        if product_id is not None:
            self.product_id = product_id

    @property
    def force_flag(self):
        """Gets the force_flag of this ReprocessProductInputEntity.  # noqa: E501

        Gets or sets a value indicating whether the product should be forcibly reprocessed.  # noqa: E501

        :return: The force_flag of this ReprocessProductInputEntity.  # noqa: E501
        :rtype: bool
        """
        return self._force_flag

    @force_flag.setter
    def force_flag(self, force_flag):
        """Sets the force_flag of this ReprocessProductInputEntity.

        Gets or sets a value indicating whether the product should be forcibly reprocessed.  # noqa: E501

        :param force_flag: The force_flag of this ReprocessProductInputEntity.  # noqa: E501
        :type: bool
        """

        self._force_flag = force_flag

    @property
    def device_ids(self):
        """Gets the device_ids of this ReprocessProductInputEntity.  # noqa: E501

        Gets or sets DeviceIds.  # noqa: E501

        :return: The device_ids of this ReprocessProductInputEntity.  # noqa: E501
        :rtype: list[ReprocessProductDeviceInputEntity]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this ReprocessProductInputEntity.

        Gets or sets DeviceIds.  # noqa: E501

        :param device_ids: The device_ids of this ReprocessProductInputEntity.  # noqa: E501
        :type: list[ReprocessProductDeviceInputEntity]
        """

        self._device_ids = device_ids

    @property
    def product_id(self):
        """Gets the product_id of this ReprocessProductInputEntity.  # noqa: E501

        Gets or sets ProductID.  # noqa: E501

        :return: The product_id of this ReprocessProductInputEntity.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ReprocessProductInputEntity.

        Gets or sets ProductID.  # noqa: E501

        :param product_id: The product_id of this ReprocessProductInputEntity.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

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
        if issubclass(ReprocessProductInputEntity, dict):
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
        if not isinstance(other, ReprocessProductInputEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReprocessProductInputEntity):
            return True

        return self.to_dict() != other.to_dict()
