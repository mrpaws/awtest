# coding: utf-8

"""
    MAM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv1.configuration import Configuration


class AppSupportedV1Model_(object):
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
        'model_id': 'int',
        'model_name': 'str'
    }

    attribute_map = {
        'model_id': 'model_id',
        'model_name': 'model_name'
    }

    def __init__(self, model_id=None, model_name=None, _configuration=None):  # noqa: E501
        """AppSupportedV1Model_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._model_id = None
        self._model_name = None
        self.discriminator = None

        if model_id is not None:
            self.model_id = model_id
        if model_name is not None:
            self.model_name = model_name

    @property
    def model_id(self):
        """Gets the model_id of this AppSupportedV1Model_.  # noqa: E501

        Gets or sets model id of the device.  # noqa: E501

        :return: The model_id of this AppSupportedV1Model_.  # noqa: E501
        :rtype: int
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this AppSupportedV1Model_.

        Gets or sets model id of the device.  # noqa: E501

        :param model_id: The model_id of this AppSupportedV1Model_.  # noqa: E501
        :type: int
        """

        self._model_id = model_id

    @property
    def model_name(self):
        """Gets the model_name of this AppSupportedV1Model_.  # noqa: E501

        Gets or sets the model name of the device.  # noqa: E501

        :return: The model_name of this AppSupportedV1Model_.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this AppSupportedV1Model_.

        Gets or sets the model name of the device.  # noqa: E501

        :param model_name: The model_name of this AppSupportedV1Model_.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

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
        if issubclass(AppSupportedV1Model_, dict):
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
        if not isinstance(other, AppSupportedV1Model_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppSupportedV1Model_):
            return True

        return self.to_dict() != other.to_dict()
