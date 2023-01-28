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


class OEMAndModels(object):
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
        'oem': 'OEMV2',
        'models': 'list[ModelV2]'
    }

    attribute_map = {
        'oem': 'OEM',
        'models': 'Models'
    }

    def __init__(self, oem=None, models=None, _configuration=None):  # noqa: E501
        """OEMAndModels - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._oem = None
        self._models = None
        self.discriminator = None

        if oem is not None:
            self.oem = oem
        if models is not None:
            self.models = models

    @property
    def oem(self):
        """Gets the oem of this OEMAndModels.  # noqa: E501

        Device OEM  # noqa: E501

        :return: The oem of this OEMAndModels.  # noqa: E501
        :rtype: OEMV2
        """
        return self._oem

    @oem.setter
    def oem(self, oem):
        """Sets the oem of this OEMAndModels.

        Device OEM  # noqa: E501

        :param oem: The oem of this OEMAndModels.  # noqa: E501
        :type: OEMV2
        """

        self._oem = oem

    @property
    def models(self):
        """Gets the models of this OEMAndModels.  # noqa: E501

        Device ModelDetail  # noqa: E501

        :return: The models of this OEMAndModels.  # noqa: E501
        :rtype: list[ModelV2]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this OEMAndModels.

        Device ModelDetail  # noqa: E501

        :param models: The models of this OEMAndModels.  # noqa: E501
        :type: list[ModelV2]
        """

        self._models = models

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
        if issubclass(OEMAndModels, dict):
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
        if not isinstance(other, OEMAndModels):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OEMAndModels):
            return True

        return self.to_dict() != other.to_dict()
