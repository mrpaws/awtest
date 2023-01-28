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


class CustomScriptModel1_(object):
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
        'custom_script_type': 'str',
        'uninstall_command': 'str',
        'uninstall_script_blob_id': 'int'
    }

    attribute_map = {
        'custom_script_type': 'CustomScriptType',
        'uninstall_command': 'UninstallCommand',
        'uninstall_script_blob_id': 'UninstallScriptBlobId'
    }

    def __init__(self, custom_script_type=None, uninstall_command=None, uninstall_script_blob_id=None, _configuration=None):  # noqa: E501
        """CustomScriptModel1_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_script_type = None
        self._uninstall_command = None
        self._uninstall_script_blob_id = None
        self.discriminator = None

        if custom_script_type is not None:
            self.custom_script_type = custom_script_type
        if uninstall_command is not None:
            self.uninstall_command = uninstall_command
        if uninstall_script_blob_id is not None:
            self.uninstall_script_blob_id = uninstall_script_blob_id

    @property
    def custom_script_type(self):
        """Gets the custom_script_type of this CustomScriptModel1_.  # noqa: E501

        Gets or sets the custom script type (Supported values: Input = 1, Upload = 2).  # noqa: E501

        :return: The custom_script_type of this CustomScriptModel1_.  # noqa: E501
        :rtype: str
        """
        return self._custom_script_type

    @custom_script_type.setter
    def custom_script_type(self, custom_script_type):
        """Sets the custom_script_type of this CustomScriptModel1_.

        Gets or sets the custom script type (Supported values: Input = 1, Upload = 2).  # noqa: E501

        :param custom_script_type: The custom_script_type of this CustomScriptModel1_.  # noqa: E501
        :type: str
        """

        self._custom_script_type = custom_script_type

    @property
    def uninstall_command(self):
        """Gets the uninstall_command of this CustomScriptModel1_.  # noqa: E501

        Gets or sets the application uninstall command provided.  # noqa: E501

        :return: The uninstall_command of this CustomScriptModel1_.  # noqa: E501
        :rtype: str
        """
        return self._uninstall_command

    @uninstall_command.setter
    def uninstall_command(self, uninstall_command):
        """Sets the uninstall_command of this CustomScriptModel1_.

        Gets or sets the application uninstall command provided.  # noqa: E501

        :param uninstall_command: The uninstall_command of this CustomScriptModel1_.  # noqa: E501
        :type: str
        """

        self._uninstall_command = uninstall_command

    @property
    def uninstall_script_blob_id(self):
        """Gets the uninstall_script_blob_id of this CustomScriptModel1_.  # noqa: E501

        Gets or sets the ID value of the uninstall script file uploaded on the console.  Supported file types : js,jse,ps1,ps1xml,psc1,psd1,psm1,pssc,cdxml,vbs,vbe,wsf,wsc.  # noqa: E501

        :return: The uninstall_script_blob_id of this CustomScriptModel1_.  # noqa: E501
        :rtype: int
        """
        return self._uninstall_script_blob_id

    @uninstall_script_blob_id.setter
    def uninstall_script_blob_id(self, uninstall_script_blob_id):
        """Sets the uninstall_script_blob_id of this CustomScriptModel1_.

        Gets or sets the ID value of the uninstall script file uploaded on the console.  Supported file types : js,jse,ps1,ps1xml,psc1,psd1,psm1,pssc,cdxml,vbs,vbe,wsf,wsc.  # noqa: E501

        :param uninstall_script_blob_id: The uninstall_script_blob_id of this CustomScriptModel1_.  # noqa: E501
        :type: int
        """

        self._uninstall_script_blob_id = uninstall_script_blob_id

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
        if issubclass(CustomScriptModel1_, dict):
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
        if not isinstance(other, CustomScriptModel1_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomScriptModel1_):
            return True

        return self.to_dict() != other.to_dict()
