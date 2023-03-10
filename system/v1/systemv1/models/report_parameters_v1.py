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


class ReportParametersV1(object):
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
        'search_text': 'str',
        'format': 'str',
        'sort_column': 'int',
        'export_type': 'int',
        'sort_direction': 'int',
        'start_date': 'datetime',
        'end_date': 'datetime'
    }

    attribute_map = {
        'search_text': 'search_text',
        'format': 'format',
        'sort_column': 'sort_column',
        'export_type': 'export_type',
        'sort_direction': 'sort_direction',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, search_text=None, format=None, sort_column=None, export_type=None, sort_direction=None, start_date=None, end_date=None, _configuration=None):  # noqa: E501
        """ReportParametersV1 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._search_text = None
        self._format = None
        self._sort_column = None
        self._export_type = None
        self._sort_direction = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if search_text is not None:
            self.search_text = search_text
        if format is not None:
            self.format = format
        if sort_column is not None:
            self.sort_column = sort_column
        if export_type is not None:
            self.export_type = export_type
        if sort_direction is not None:
            self.sort_direction = sort_direction
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def search_text(self):
        """Gets the search_text of this ReportParametersV1.  # noqa: E501

        The search text string which the exported reports results will be filtered by.  # noqa: E501

        :return: The search_text of this ReportParametersV1.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this ReportParametersV1.

        The search text string which the exported reports results will be filtered by.  # noqa: E501

        :param search_text: The search_text of this ReportParametersV1.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

    @property
    def format(self):
        """Gets the format of this ReportParametersV1.  # noqa: E501

        Report's export format.  # noqa: E501

        :return: The format of this ReportParametersV1.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ReportParametersV1.

        Report's export format.  # noqa: E501

        :param format: The format of this ReportParametersV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["XLSX", "CSV"]  # noqa: E501
        if (self._configuration.client_side_validation and
                format not in allowed_values):
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def sort_column(self):
        """Gets the sort_column of this ReportParametersV1.  # noqa: E501

        Sort column to filter for reports.  # noqa: E501

        :return: The sort_column of this ReportParametersV1.  # noqa: E501
        :rtype: int
        """
        return self._sort_column

    @sort_column.setter
    def sort_column(self, sort_column):
        """Sets the sort_column of this ReportParametersV1.

        Sort column to filter for reports.  # noqa: E501

        :param sort_column: The sort_column of this ReportParametersV1.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5]  # noqa: E501
        if (self._configuration.client_side_validation and
                sort_column not in allowed_values):
            raise ValueError(
                "Invalid value for `sort_column` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_column, allowed_values)
            )

        self._sort_column = sort_column

    @property
    def export_type(self):
        """Gets the export_type of this ReportParametersV1.  # noqa: E501

        Export type to filter for reports.  # noqa: E501

        :return: The export_type of this ReportParametersV1.  # noqa: E501
        :rtype: int
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        """Sets the export_type of this ReportParametersV1.

        Export type to filter for reports.  # noqa: E501

        :param export_type: The export_type of this ReportParametersV1.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3]  # noqa: E501
        if (self._configuration.client_side_validation and
                export_type not in allowed_values):
            raise ValueError(
                "Invalid value for `export_type` ({0}), must be one of {1}"  # noqa: E501
                .format(export_type, allowed_values)
            )

        self._export_type = export_type

    @property
    def sort_direction(self):
        """Gets the sort_direction of this ReportParametersV1.  # noqa: E501

        Sort direction for reports.  # noqa: E501

        :return: The sort_direction of this ReportParametersV1.  # noqa: E501
        :rtype: int
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction):
        """Sets the sort_direction of this ReportParametersV1.

        Sort direction for reports.  # noqa: E501

        :param sort_direction: The sort_direction of this ReportParametersV1.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if (self._configuration.client_side_validation and
                sort_direction not in allowed_values):
            raise ValueError(
                "Invalid value for `sort_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_direction, allowed_values)
            )

        self._sort_direction = sort_direction

    @property
    def start_date(self):
        """Gets the start_date of this ReportParametersV1.  # noqa: E501

        The creation date in UTC by which the results will be filtered. Format of the date is YYYY-MM-DD.  # noqa: E501

        :return: The start_date of this ReportParametersV1.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ReportParametersV1.

        The creation date in UTC by which the results will be filtered. Format of the date is YYYY-MM-DD.  # noqa: E501

        :param start_date: The start_date of this ReportParametersV1.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ReportParametersV1.  # noqa: E501

        The expiration date in UTC by which the results will be filtered. Format of the date is YYYY-MM-DD.  # noqa: E501

        :return: The end_date of this ReportParametersV1.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ReportParametersV1.

        The expiration date in UTC by which the results will be filtered. Format of the date is YYYY-MM-DD.  # noqa: E501

        :param end_date: The end_date of this ReportParametersV1.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

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
        if issubclass(ReportParametersV1, dict):
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
        if not isinstance(other, ReportParametersV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportParametersV1):
            return True

        return self.to_dict() != other.to_dict()
