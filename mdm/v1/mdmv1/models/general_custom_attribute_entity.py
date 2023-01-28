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


class GeneralCustomAttributeEntity(object):
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
        'application_group': 'str',
        'custom_attribute_id': 'int',
        'custom_attribute': 'str',
        'attribute_value': 'str',
        'is_dynamic': 'bool',
        'permissions': 'int',
        'create_ca': 'bool'
    }

    attribute_map = {
        'application_group': 'ApplicationGroup',
        'custom_attribute_id': 'CustomAttributeId',
        'custom_attribute': 'CustomAttribute',
        'attribute_value': 'AttributeValue',
        'is_dynamic': 'IsDynamic',
        'permissions': 'Permissions',
        'create_ca': 'CreateCA'
    }

    def __init__(self, application_group=None, custom_attribute_id=None, custom_attribute=None, attribute_value=None, is_dynamic=None, permissions=None, create_ca=None, _configuration=None):  # noqa: E501
        """GeneralCustomAttributeEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_group = None
        self._custom_attribute_id = None
        self._custom_attribute = None
        self._attribute_value = None
        self._is_dynamic = None
        self._permissions = None
        self._create_ca = None
        self.discriminator = None

        if application_group is not None:
            self.application_group = application_group
        if custom_attribute_id is not None:
            self.custom_attribute_id = custom_attribute_id
        if custom_attribute is not None:
            self.custom_attribute = custom_attribute
        if attribute_value is not None:
            self.attribute_value = attribute_value
        if is_dynamic is not None:
            self.is_dynamic = is_dynamic
        if permissions is not None:
            self.permissions = permissions
        if create_ca is not None:
            self.create_ca = create_ca

    @property
    def application_group(self):
        """Gets the application_group of this GeneralCustomAttributeEntity.  # noqa: E501

        Gets or sets applicationGroup to which the custom attribute belong.  # noqa: E501

        :return: The application_group of this GeneralCustomAttributeEntity.  # noqa: E501
        :rtype: str
        """
        return self._application_group

    @application_group.setter
    def application_group(self, application_group):
        """Sets the application_group of this GeneralCustomAttributeEntity.

        Gets or sets applicationGroup to which the custom attribute belong.  # noqa: E501

        :param application_group: The application_group of this GeneralCustomAttributeEntity.  # noqa: E501
        :type: str
        """

        self._application_group = application_group

    @property
    def custom_attribute_id(self):
        """Gets the custom_attribute_id of this GeneralCustomAttributeEntity.  # noqa: E501

        Gets or sets the custom attribute identifier.  # noqa: E501

        :return: The custom_attribute_id of this GeneralCustomAttributeEntity.  # noqa: E501
        :rtype: int
        """
        return self._custom_attribute_id

    @custom_attribute_id.setter
    def custom_attribute_id(self, custom_attribute_id):
        """Sets the custom_attribute_id of this GeneralCustomAttributeEntity.

        Gets or sets the custom attribute identifier.  # noqa: E501

        :param custom_attribute_id: The custom_attribute_id of this GeneralCustomAttributeEntity.  # noqa: E501
        :type: int
        """

        self._custom_attribute_id = custom_attribute_id

    @property
    def custom_attribute(self):
        """Gets the custom_attribute of this GeneralCustomAttributeEntity.  # noqa: E501

        Gets or sets the name of the custom attribute.  # noqa: E501

        :return: The custom_attribute of this GeneralCustomAttributeEntity.  # noqa: E501
        :rtype: str
        """
        return self._custom_attribute

    @custom_attribute.setter
    def custom_attribute(self, custom_attribute):
        """Sets the custom_attribute of this GeneralCustomAttributeEntity.

        Gets or sets the name of the custom attribute.  # noqa: E501

        :param custom_attribute: The custom_attribute of this GeneralCustomAttributeEntity.  # noqa: E501
        :type: str
        """

        self._custom_attribute = custom_attribute

    @property
    def attribute_value(self):
        """Gets the attribute_value of this GeneralCustomAttributeEntity.  # noqa: E501

        Gets or sets the value of the custom attribute.  # noqa: E501

        :return: The attribute_value of this GeneralCustomAttributeEntity.  # noqa: E501
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """Sets the attribute_value of this GeneralCustomAttributeEntity.

        Gets or sets the value of the custom attribute.  # noqa: E501

        :param attribute_value: The attribute_value of this GeneralCustomAttributeEntity.  # noqa: E501
        :type: str
        """

        self._attribute_value = attribute_value

    @property
    def is_dynamic(self):
        """Gets the is_dynamic of this GeneralCustomAttributeEntity.  # noqa: E501

        Gets or sets a value indicating whether whether custom attribute value should be dynamically fetched from device details not.  # noqa: E501

        :return: The is_dynamic of this GeneralCustomAttributeEntity.  # noqa: E501
        :rtype: bool
        """
        return self._is_dynamic

    @is_dynamic.setter
    def is_dynamic(self, is_dynamic):
        """Sets the is_dynamic of this GeneralCustomAttributeEntity.

        Gets or sets a value indicating whether whether custom attribute value should be dynamically fetched from device details not.  # noqa: E501

        :param is_dynamic: The is_dynamic of this GeneralCustomAttributeEntity.  # noqa: E501
        :type: bool
        """

        self._is_dynamic = is_dynamic

    @property
    def permissions(self):
        """Gets the permissions of this GeneralCustomAttributeEntity.  # noqa: E501

        Gets or sets permission level of custom attribue. 0: read-write, 1: read-only.  # noqa: E501

        :return: The permissions of this GeneralCustomAttributeEntity.  # noqa: E501
        :rtype: int
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this GeneralCustomAttributeEntity.

        Gets or sets permission level of custom attribue. 0: read-write, 1: read-only.  # noqa: E501

        :param permissions: The permissions of this GeneralCustomAttributeEntity.  # noqa: E501
        :type: int
        """

        self._permissions = permissions

    @property
    def create_ca(self):
        """Gets the create_ca of this GeneralCustomAttributeEntity.  # noqa: E501

        Gets or sets a value indicating whether whether a new custom attribute has to be created or not.  # noqa: E501

        :return: The create_ca of this GeneralCustomAttributeEntity.  # noqa: E501
        :rtype: bool
        """
        return self._create_ca

    @create_ca.setter
    def create_ca(self, create_ca):
        """Sets the create_ca of this GeneralCustomAttributeEntity.

        Gets or sets a value indicating whether whether a new custom attribute has to be created or not.  # noqa: E501

        :param create_ca: The create_ca of this GeneralCustomAttributeEntity.  # noqa: E501
        :type: bool
        """

        self._create_ca = create_ca

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
        if issubclass(GeneralCustomAttributeEntity, dict):
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
        if not isinstance(other, GeneralCustomAttributeEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneralCustomAttributeEntity):
            return True

        return self.to_dict() != other.to_dict()
