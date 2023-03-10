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


class EpsonPrinterProfileV2Model(object):
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
        'scep_list': 'list[EpsonSCEPPayloadV2Model]',
        'general': 'GeneralPayloadV2Entity'
    }

    attribute_map = {
        'scep_list': 'SCEPList',
        'general': 'General'
    }

    def __init__(self, scep_list=None, general=None, _configuration=None):  # noqa: E501
        """EpsonPrinterProfileV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._scep_list = None
        self._general = None
        self.discriminator = None

        if scep_list is not None:
            self.scep_list = scep_list
        if general is not None:
            self.general = general

    @property
    def scep_list(self):
        """Gets the scep_list of this EpsonPrinterProfileV2Model.  # noqa: E501


        :return: The scep_list of this EpsonPrinterProfileV2Model.  # noqa: E501
        :rtype: list[EpsonSCEPPayloadV2Model]
        """
        return self._scep_list

    @scep_list.setter
    def scep_list(self, scep_list):
        """Sets the scep_list of this EpsonPrinterProfileV2Model.


        :param scep_list: The scep_list of this EpsonPrinterProfileV2Model.  # noqa: E501
        :type: list[EpsonSCEPPayloadV2Model]
        """

        self._scep_list = scep_list

    @property
    def general(self):
        """Gets the general of this EpsonPrinterProfileV2Model.  # noqa: E501


        :return: The general of this EpsonPrinterProfileV2Model.  # noqa: E501
        :rtype: GeneralPayloadV2Entity
        """
        return self._general

    @general.setter
    def general(self, general):
        """Sets the general of this EpsonPrinterProfileV2Model.


        :param general: The general of this EpsonPrinterProfileV2Model.  # noqa: E501
        :type: GeneralPayloadV2Entity
        """

        self._general = general

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
        if issubclass(EpsonPrinterProfileV2Model, dict):
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
        if not isinstance(other, EpsonPrinterProfileV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EpsonPrinterProfileV2Model):
            return True

        return self.to_dict() != other.to_dict()
