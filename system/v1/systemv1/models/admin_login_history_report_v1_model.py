# coding: utf-8

"""
    System API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv1.configuration import Configuration


class AdminLoginHistoryReportV1Model(object):
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
        'report_format': 'str',
        'organization_group_uuid': 'str',
        'page_size': 'int',
        'page_number': 'int',
        'sort_column': 'int',
        'sort_order': 'int',
        'user_uuid': 'str',
        'search_text': 'str'
    }

    attribute_map = {
        'report_format': 'report_format',
        'organization_group_uuid': 'organization_group_uuid',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'sort_column': 'sort_column',
        'sort_order': 'sort_order',
        'user_uuid': 'user_uuid',
        'search_text': 'search_text'
    }

    def __init__(self, report_format=None, organization_group_uuid=None, page_size=None, page_number=None, sort_column=None, sort_order=None, user_uuid=None, search_text=None, _configuration=None):  # noqa: E501
        """AdminLoginHistoryReportV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._report_format = None
        self._organization_group_uuid = None
        self._page_size = None
        self._page_number = None
        self._sort_column = None
        self._sort_order = None
        self._user_uuid = None
        self._search_text = None
        self.discriminator = None

        if report_format is not None:
            self.report_format = report_format
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if sort_column is not None:
            self.sort_column = sort_column
        if sort_order is not None:
            self.sort_order = sort_order
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if search_text is not None:
            self.search_text = search_text

    @property
    def report_format(self):
        """Gets the report_format of this AdminLoginHistoryReportV1Model.  # noqa: E501

        Report export format.  # noqa: E501

        :return: The report_format of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :rtype: str
        """
        return self._report_format

    @report_format.setter
    def report_format(self, report_format):
        """Sets the report_format of this AdminLoginHistoryReportV1Model.

        Report export format.  # noqa: E501

        :param report_format: The report_format of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :type: str
        """
        allowed_values = ["XLSX", "CSV"]  # noqa: E501
        if (self._configuration.client_side_validation and
                report_format not in allowed_values):
            raise ValueError(
                "Invalid value for `report_format` ({0}), must be one of {1}"  # noqa: E501
                .format(report_format, allowed_values)
            )

        self._report_format = report_format

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this AdminLoginHistoryReportV1Model.  # noqa: E501

        Organization Group UUID.  # noqa: E501

        :return: The organization_group_uuid of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this AdminLoginHistoryReportV1Model.

        Organization Group UUID.  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def page_size(self):
        """Gets the page_size of this AdminLoginHistoryReportV1Model.  # noqa: E501

        Page size.  # noqa: E501

        :return: The page_size of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this AdminLoginHistoryReportV1Model.

        Page size.  # noqa: E501

        :param page_size: The page_size of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this AdminLoginHistoryReportV1Model.  # noqa: E501

        Page number.  # noqa: E501

        :return: The page_number of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this AdminLoginHistoryReportV1Model.

        Page number.  # noqa: E501

        :param page_number: The page_number of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def sort_column(self):
        """Gets the sort_column of this AdminLoginHistoryReportV1Model.  # noqa: E501

        Sort column.  # noqa: E501

        :return: The sort_column of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :rtype: int
        """
        return self._sort_column

    @sort_column.setter
    def sort_column(self, sort_column):
        """Sets the sort_column of this AdminLoginHistoryReportV1Model.

        Sort column.  # noqa: E501

        :param sort_column: The sort_column of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7]  # noqa: E501
        if (self._configuration.client_side_validation and
                sort_column not in allowed_values):
            raise ValueError(
                "Invalid value for `sort_column` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_column, allowed_values)
            )

        self._sort_column = sort_column

    @property
    def sort_order(self):
        """Gets the sort_order of this AdminLoginHistoryReportV1Model.  # noqa: E501

        The order based which on we can sort. Default value is ASC.  # noqa: E501

        :return: The sort_order of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this AdminLoginHistoryReportV1Model.

        The order based which on we can sort. Default value is ASC.  # noqa: E501

        :param sort_order: The sort_order of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if (self._configuration.client_side_validation and
                sort_order not in allowed_values):
            raise ValueError(
                "Invalid value for `sort_order` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_order, allowed_values)
            )

        self._sort_order = sort_order

    @property
    def user_uuid(self):
        """Gets the user_uuid of this AdminLoginHistoryReportV1Model.  # noqa: E501

        User UUID.  # noqa: E501

        :return: The user_uuid of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this AdminLoginHistoryReportV1Model.

        User UUID.  # noqa: E501

        :param user_uuid: The user_uuid of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def search_text(self):
        """Gets the search_text of this AdminLoginHistoryReportV1Model.  # noqa: E501

        Search text.  # noqa: E501

        :return: The search_text of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this AdminLoginHistoryReportV1Model.

        Search text.  # noqa: E501

        :param search_text: The search_text of this AdminLoginHistoryReportV1Model.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

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
        if issubclass(AdminLoginHistoryReportV1Model, dict):
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
        if not isinstance(other, AdminLoginHistoryReportV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdminLoginHistoryReportV1Model):
            return True

        return self.to_dict() != other.to_dict()
