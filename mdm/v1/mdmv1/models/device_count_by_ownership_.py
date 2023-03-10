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


class DeviceCountByOwnership_(object):
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
        'corporate_dedicated': 'int',
        'corporate_shared': 'int',
        'employee_owned': 'int',
        'undefined': 'int'
    }

    attribute_map = {
        'corporate_dedicated': 'CorporateDedicated',
        'corporate_shared': 'CorporateShared',
        'employee_owned': 'EmployeeOwned',
        'undefined': 'Undefined'
    }

    def __init__(self, corporate_dedicated=None, corporate_shared=None, employee_owned=None, undefined=None, _configuration=None):  # noqa: E501
        """DeviceCountByOwnership_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._corporate_dedicated = None
        self._corporate_shared = None
        self._employee_owned = None
        self._undefined = None
        self.discriminator = None

        if corporate_dedicated is not None:
            self.corporate_dedicated = corporate_dedicated
        if corporate_shared is not None:
            self.corporate_shared = corporate_shared
        if employee_owned is not None:
            self.employee_owned = employee_owned
        if undefined is not None:
            self.undefined = undefined

    @property
    def corporate_dedicated(self):
        """Gets the corporate_dedicated of this DeviceCountByOwnership_.  # noqa: E501

        Gets or sets no. of CorporateDedicated Devices.  # noqa: E501

        :return: The corporate_dedicated of this DeviceCountByOwnership_.  # noqa: E501
        :rtype: int
        """
        return self._corporate_dedicated

    @corporate_dedicated.setter
    def corporate_dedicated(self, corporate_dedicated):
        """Sets the corporate_dedicated of this DeviceCountByOwnership_.

        Gets or sets no. of CorporateDedicated Devices.  # noqa: E501

        :param corporate_dedicated: The corporate_dedicated of this DeviceCountByOwnership_.  # noqa: E501
        :type: int
        """

        self._corporate_dedicated = corporate_dedicated

    @property
    def corporate_shared(self):
        """Gets the corporate_shared of this DeviceCountByOwnership_.  # noqa: E501

        Gets or sets no. of CorporateShared Devices.  # noqa: E501

        :return: The corporate_shared of this DeviceCountByOwnership_.  # noqa: E501
        :rtype: int
        """
        return self._corporate_shared

    @corporate_shared.setter
    def corporate_shared(self, corporate_shared):
        """Sets the corporate_shared of this DeviceCountByOwnership_.

        Gets or sets no. of CorporateShared Devices.  # noqa: E501

        :param corporate_shared: The corporate_shared of this DeviceCountByOwnership_.  # noqa: E501
        :type: int
        """

        self._corporate_shared = corporate_shared

    @property
    def employee_owned(self):
        """Gets the employee_owned of this DeviceCountByOwnership_.  # noqa: E501

        Gets or sets no. of EmployeeOwned Devices.  # noqa: E501

        :return: The employee_owned of this DeviceCountByOwnership_.  # noqa: E501
        :rtype: int
        """
        return self._employee_owned

    @employee_owned.setter
    def employee_owned(self, employee_owned):
        """Sets the employee_owned of this DeviceCountByOwnership_.

        Gets or sets no. of EmployeeOwned Devices.  # noqa: E501

        :param employee_owned: The employee_owned of this DeviceCountByOwnership_.  # noqa: E501
        :type: int
        """

        self._employee_owned = employee_owned

    @property
    def undefined(self):
        """Gets the undefined of this DeviceCountByOwnership_.  # noqa: E501

        Gets or sets no. of Devices whose Ownership info is undefined.  # noqa: E501

        :return: The undefined of this DeviceCountByOwnership_.  # noqa: E501
        :rtype: int
        """
        return self._undefined

    @undefined.setter
    def undefined(self, undefined):
        """Sets the undefined of this DeviceCountByOwnership_.

        Gets or sets no. of Devices whose Ownership info is undefined.  # noqa: E501

        :param undefined: The undefined of this DeviceCountByOwnership_.  # noqa: E501
        :type: int
        """

        self._undefined = undefined

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
        if issubclass(DeviceCountByOwnership_, dict):
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
        if not isinstance(other, DeviceCountByOwnership_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceCountByOwnership_):
            return True

        return self.to_dict() != other.to_dict()
