# coding: utf-8

"""
    System API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv2.configuration import Configuration


class OrganizationGroup_(object):
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
        'name': 'str',
        'group_id': 'str',
        'location_group_type': 'str',
        'country': 'str',
        'locale': 'str',
        'add_default_location': 'str',
        'devices': 'str',
        'enable_rest_api_access': 'bool',
        'timezone': 'int',
        'timezone_code': 'str',
        'customer_industry_type': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'group_id': 'GroupId',
        'location_group_type': 'LocationGroupType',
        'country': 'Country',
        'locale': 'Locale',
        'add_default_location': 'AddDefaultLocation',
        'devices': 'Devices',
        'enable_rest_api_access': 'EnableRestApiAccess',
        'timezone': 'Timezone',
        'timezone_code': 'timezone_code',
        'customer_industry_type': 'customer_industry_type'
    }

    def __init__(self, name=None, group_id=None, location_group_type=None, country=None, locale=None, add_default_location=None, devices=None, enable_rest_api_access=None, timezone=None, timezone_code=None, customer_industry_type=None, _configuration=None):  # noqa: E501
        """OrganizationGroup_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._group_id = None
        self._location_group_type = None
        self._country = None
        self._locale = None
        self._add_default_location = None
        self._devices = None
        self._enable_rest_api_access = None
        self._timezone = None
        self._timezone_code = None
        self._customer_industry_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if group_id is not None:
            self.group_id = group_id
        if location_group_type is not None:
            self.location_group_type = location_group_type
        if country is not None:
            self.country = country
        if locale is not None:
            self.locale = locale
        if add_default_location is not None:
            self.add_default_location = add_default_location
        if devices is not None:
            self.devices = devices
        if enable_rest_api_access is not None:
            self.enable_rest_api_access = enable_rest_api_access
        if timezone is not None:
            self.timezone = timezone
        if timezone_code is not None:
            self.timezone_code = timezone_code
        if customer_industry_type is not None:
            self.customer_industry_type = customer_industry_type

    @property
    def name(self):
        """Gets the name of this OrganizationGroup_.  # noqa: E501

        Gets or sets location group name.  # noqa: E501

        :return: The name of this OrganizationGroup_.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationGroup_.

        Gets or sets location group name.  # noqa: E501

        :param name: The name of this OrganizationGroup_.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def group_id(self):
        """Gets the group_id of this OrganizationGroup_.  # noqa: E501

        Gets or sets the location group's tenant code.  # noqa: E501

        :return: The group_id of this OrganizationGroup_.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this OrganizationGroup_.

        Gets or sets the location group's tenant code.  # noqa: E501

        :param group_id: The group_id of this OrganizationGroup_.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def location_group_type(self):
        """Gets the location_group_type of this OrganizationGroup_.  # noqa: E501

        Gets or sets location group type like Business segment, Customer etc...  # noqa: E501

        :return: The location_group_type of this OrganizationGroup_.  # noqa: E501
        :rtype: str
        """
        return self._location_group_type

    @location_group_type.setter
    def location_group_type(self, location_group_type):
        """Sets the location_group_type of this OrganizationGroup_.

        Gets or sets location group type like Business segment, Customer etc...  # noqa: E501

        :param location_group_type: The location_group_type of this OrganizationGroup_.  # noqa: E501
        :type: str
        """

        self._location_group_type = location_group_type

    @property
    def country(self):
        """Gets the country of this OrganizationGroup_.  # noqa: E501

        Gets or sets country name like United States, India etc.  # noqa: E501

        :return: The country of this OrganizationGroup_.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this OrganizationGroup_.

        Gets or sets country name like United States, India etc.  # noqa: E501

        :param country: The country of this OrganizationGroup_.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def locale(self):
        """Gets the locale of this OrganizationGroup_.  # noqa: E501

        Gets or sets Locale information for Location Group like.  # noqa: E501

        :return: The locale of this OrganizationGroup_.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this OrganizationGroup_.

        Gets or sets Locale information for Location Group like.  # noqa: E501

        :param locale: The locale of this OrganizationGroup_.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def add_default_location(self):
        """Gets the add_default_location of this OrganizationGroup_.  # noqa: E501

        Gets or sets this tells whether default location to be created while creating Location Group.  # noqa: E501

        :return: The add_default_location of this OrganizationGroup_.  # noqa: E501
        :rtype: str
        """
        return self._add_default_location

    @add_default_location.setter
    def add_default_location(self, add_default_location):
        """Sets the add_default_location of this OrganizationGroup_.

        Gets or sets this tells whether default location to be created while creating Location Group.  # noqa: E501

        :param add_default_location: The add_default_location of this OrganizationGroup_.  # noqa: E501
        :type: str
        """

        self._add_default_location = add_default_location

    @property
    def devices(self):
        """Gets the devices of this OrganizationGroup_.  # noqa: E501

        Gets or sets this contains total nummber of devices in this Location group.  # noqa: E501

        :return: The devices of this OrganizationGroup_.  # noqa: E501
        :rtype: str
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this OrganizationGroup_.

        Gets or sets this contains total nummber of devices in this Location group.  # noqa: E501

        :param devices: The devices of this OrganizationGroup_.  # noqa: E501
        :type: str
        """

        self._devices = devices

    @property
    def enable_rest_api_access(self):
        """Gets the enable_rest_api_access of this OrganizationGroup_.  # noqa: E501

        Gets or sets a value indicating whether this is a value indicating whether enable rest api access.  # noqa: E501

        :return: The enable_rest_api_access of this OrganizationGroup_.  # noqa: E501
        :rtype: bool
        """
        return self._enable_rest_api_access

    @enable_rest_api_access.setter
    def enable_rest_api_access(self, enable_rest_api_access):
        """Sets the enable_rest_api_access of this OrganizationGroup_.

        Gets or sets a value indicating whether this is a value indicating whether enable rest api access.  # noqa: E501

        :param enable_rest_api_access: The enable_rest_api_access of this OrganizationGroup_.  # noqa: E501
        :type: bool
        """

        self._enable_rest_api_access = enable_rest_api_access

    @property
    def timezone(self):
        """Gets the timezone of this OrganizationGroup_.  # noqa: E501

        Gets or sets Timezone id of Location like 62[EST, GMT-5.00] etc..  # noqa: E501

        :return: The timezone of this OrganizationGroup_.  # noqa: E501
        :rtype: int
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this OrganizationGroup_.

        Gets or sets Timezone id of Location like 62[EST, GMT-5.00] etc..  # noqa: E501

        :param timezone: The timezone of this OrganizationGroup_.  # noqa: E501
        :type: int
        """

        self._timezone = timezone

    @property
    def timezone_code(self):
        """Gets the timezone_code of this OrganizationGroup_.  # noqa: E501

        Gets or sets Organization group timezone code.  # noqa: E501

        :return: The timezone_code of this OrganizationGroup_.  # noqa: E501
        :rtype: str
        """
        return self._timezone_code

    @timezone_code.setter
    def timezone_code(self, timezone_code):
        """Sets the timezone_code of this OrganizationGroup_.

        Gets or sets Organization group timezone code.  # noqa: E501

        :param timezone_code: The timezone_code of this OrganizationGroup_.  # noqa: E501
        :type: str
        """

        self._timezone_code = timezone_code

    @property
    def customer_industry_type(self):
        """Gets the customer_industry_type of this OrganizationGroup_.  # noqa: E501

        Gets or sets Organization Group Customer industry type.  # noqa: E501

        :return: The customer_industry_type of this OrganizationGroup_.  # noqa: E501
        :rtype: int
        """
        return self._customer_industry_type

    @customer_industry_type.setter
    def customer_industry_type(self, customer_industry_type):
        """Sets the customer_industry_type of this OrganizationGroup_.

        Gets or sets Organization Group Customer industry type.  # noqa: E501

        :param customer_industry_type: The customer_industry_type of this OrganizationGroup_.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7]  # noqa: E501
        if (self._configuration.client_side_validation and
                customer_industry_type not in allowed_values):
            raise ValueError(
                "Invalid value for `customer_industry_type` ({0}), must be one of {1}"  # noqa: E501
                .format(customer_industry_type, allowed_values)
            )

        self._customer_industry_type = customer_industry_type

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
        if issubclass(OrganizationGroup_, dict):
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
        if not isinstance(other, OrganizationGroup_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationGroup_):
            return True

        return self.to_dict() != other.to_dict()
