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


class ApplicationUnInstallProcessModel1_(object):
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
        'use_custom_script': 'bool',
        'custom_script': 'CustomScriptModel1_'
    }

    attribute_map = {
        'use_custom_script': 'UseCustomScript',
        'custom_script': 'CustomScript'
    }

    def __init__(self, use_custom_script=None, custom_script=None, _configuration=None):  # noqa: E501
        """ApplicationUnInstallProcessModel1_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._use_custom_script = None
        self._custom_script = None
        self.discriminator = None

        if use_custom_script is not None:
            self.use_custom_script = use_custom_script
        if custom_script is not None:
            self.custom_script = custom_script

    @property
    def use_custom_script(self):
        """Gets the use_custom_script of this ApplicationUnInstallProcessModel1_.  # noqa: E501

        Gets or sets a value indicating whether value indicating whether custom script is used or not.  # noqa: E501

        :return: The use_custom_script of this ApplicationUnInstallProcessModel1_.  # noqa: E501
        :rtype: bool
        """
        return self._use_custom_script

    @use_custom_script.setter
    def use_custom_script(self, use_custom_script):
        """Sets the use_custom_script of this ApplicationUnInstallProcessModel1_.

        Gets or sets a value indicating whether value indicating whether custom script is used or not.  # noqa: E501

        :param use_custom_script: The use_custom_script of this ApplicationUnInstallProcessModel1_.  # noqa: E501
        :type: bool
        """

        self._use_custom_script = use_custom_script

    @property
    def custom_script(self):
        """Gets the custom_script of this ApplicationUnInstallProcessModel1_.  # noqa: E501

        Gets or sets the custom script.  # noqa: E501

        :return: The custom_script of this ApplicationUnInstallProcessModel1_.  # noqa: E501
        :rtype: CustomScriptModel1_
        """
        return self._custom_script

    @custom_script.setter
    def custom_script(self, custom_script):
        """Sets the custom_script of this ApplicationUnInstallProcessModel1_.

        Gets or sets the custom script.  # noqa: E501

        :param custom_script: The custom_script of this ApplicationUnInstallProcessModel1_.  # noqa: E501
        :type: CustomScriptModel1_
        """

        self._custom_script = custom_script

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
        if issubclass(ApplicationUnInstallProcessModel1_, dict):
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
        if not isinstance(other, ApplicationUnInstallProcessModel1_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationUnInstallProcessModel1_):
            return True

        return self.to_dict() != other.to_dict()
