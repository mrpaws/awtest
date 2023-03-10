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


class CustomAttributeChange(object):
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
        'custom_attribute_name': 'str',
        'old_value': 'str',
        'new_value': 'str',
        'modified_date': 'str',
        'location_group_id': 'str',
        'location_group_name': 'str',
        'application_group': 'str',
        'source': 'str'
    }

    attribute_map = {
        'custom_attribute_name': 'CustomAttributeName',
        'old_value': 'OldValue',
        'new_value': 'NewValue',
        'modified_date': 'ModifiedDate',
        'location_group_id': 'LocationGroupID',
        'location_group_name': 'LocationGroupName',
        'application_group': 'ApplicationGroup',
        'source': 'Source'
    }

    def __init__(self, custom_attribute_name=None, old_value=None, new_value=None, modified_date=None, location_group_id=None, location_group_name=None, application_group=None, source=None, _configuration=None):  # noqa: E501
        """CustomAttributeChange - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_attribute_name = None
        self._old_value = None
        self._new_value = None
        self._modified_date = None
        self._location_group_id = None
        self._location_group_name = None
        self._application_group = None
        self._source = None
        self.discriminator = None

        if custom_attribute_name is not None:
            self.custom_attribute_name = custom_attribute_name
        if old_value is not None:
            self.old_value = old_value
        if new_value is not None:
            self.new_value = new_value
        if modified_date is not None:
            self.modified_date = modified_date
        if location_group_id is not None:
            self.location_group_id = location_group_id
        if location_group_name is not None:
            self.location_group_name = location_group_name
        if application_group is not None:
            self.application_group = application_group
        if source is not None:
            self.source = source

    @property
    def custom_attribute_name(self):
        """Gets the custom_attribute_name of this CustomAttributeChange.  # noqa: E501

        Gets or sets custom Attrbute Name.  # noqa: E501

        :return: The custom_attribute_name of this CustomAttributeChange.  # noqa: E501
        :rtype: str
        """
        return self._custom_attribute_name

    @custom_attribute_name.setter
    def custom_attribute_name(self, custom_attribute_name):
        """Sets the custom_attribute_name of this CustomAttributeChange.

        Gets or sets custom Attrbute Name.  # noqa: E501

        :param custom_attribute_name: The custom_attribute_name of this CustomAttributeChange.  # noqa: E501
        :type: str
        """

        self._custom_attribute_name = custom_attribute_name

    @property
    def old_value(self):
        """Gets the old_value of this CustomAttributeChange.  # noqa: E501

        Gets or sets old Custom Attrbute Value.  # noqa: E501

        :return: The old_value of this CustomAttributeChange.  # noqa: E501
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this CustomAttributeChange.

        Gets or sets old Custom Attrbute Value.  # noqa: E501

        :param old_value: The old_value of this CustomAttributeChange.  # noqa: E501
        :type: str
        """

        self._old_value = old_value

    @property
    def new_value(self):
        """Gets the new_value of this CustomAttributeChange.  # noqa: E501

        Gets or sets new Custom Attrbute Value.  # noqa: E501

        :return: The new_value of this CustomAttributeChange.  # noqa: E501
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this CustomAttributeChange.

        Gets or sets new Custom Attrbute Value.  # noqa: E501

        :param new_value: The new_value of this CustomAttributeChange.  # noqa: E501
        :type: str
        """

        self._new_value = new_value

    @property
    def modified_date(self):
        """Gets the modified_date of this CustomAttributeChange.  # noqa: E501

        Gets or sets date Custom Attrbute was modified.  # noqa: E501

        :return: The modified_date of this CustomAttributeChange.  # noqa: E501
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this CustomAttributeChange.

        Gets or sets date Custom Attrbute was modified.  # noqa: E501

        :param modified_date: The modified_date of this CustomAttributeChange.  # noqa: E501
        :type: str
        """

        self._modified_date = modified_date

    @property
    def location_group_id(self):
        """Gets the location_group_id of this CustomAttributeChange.  # noqa: E501

        Gets or sets date Custom Attrbute was modified.  # noqa: E501

        :return: The location_group_id of this CustomAttributeChange.  # noqa: E501
        :rtype: str
        """
        return self._location_group_id

    @location_group_id.setter
    def location_group_id(self, location_group_id):
        """Sets the location_group_id of this CustomAttributeChange.

        Gets or sets date Custom Attrbute was modified.  # noqa: E501

        :param location_group_id: The location_group_id of this CustomAttributeChange.  # noqa: E501
        :type: str
        """

        self._location_group_id = location_group_id

    @property
    def location_group_name(self):
        """Gets the location_group_name of this CustomAttributeChange.  # noqa: E501

        Gets or sets date Custom Attrbute was modified.  # noqa: E501

        :return: The location_group_name of this CustomAttributeChange.  # noqa: E501
        :rtype: str
        """
        return self._location_group_name

    @location_group_name.setter
    def location_group_name(self, location_group_name):
        """Sets the location_group_name of this CustomAttributeChange.

        Gets or sets date Custom Attrbute was modified.  # noqa: E501

        :param location_group_name: The location_group_name of this CustomAttributeChange.  # noqa: E501
        :type: str
        """

        self._location_group_name = location_group_name

    @property
    def application_group(self):
        """Gets the application_group of this CustomAttributeChange.  # noqa: E501

        Gets or sets application Group.  # noqa: E501

        :return: The application_group of this CustomAttributeChange.  # noqa: E501
        :rtype: str
        """
        return self._application_group

    @application_group.setter
    def application_group(self, application_group):
        """Sets the application_group of this CustomAttributeChange.

        Gets or sets application Group.  # noqa: E501

        :param application_group: The application_group of this CustomAttributeChange.  # noqa: E501
        :type: str
        """

        self._application_group = application_group

    @property
    def source(self):
        """Gets the source of this CustomAttributeChange.  # noqa: E501

        Gets or sets source.  # noqa: E501

        :return: The source of this CustomAttributeChange.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CustomAttributeChange.

        Gets or sets source.  # noqa: E501

        :param source: The source of this CustomAttributeChange.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if issubclass(CustomAttributeChange, dict):
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
        if not isinstance(other, CustomAttributeChange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomAttributeChange):
            return True

        return self.to_dict() != other.to_dict()
