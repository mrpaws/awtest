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


class StatusInfo(object):
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
        'code': 'int',
        'execution_id': 'str',
        'data': 'dict(str, str)',
        'status_code_value': 'str'
    }

    attribute_map = {
        'code': 'code',
        'execution_id': 'execution_id',
        'data': 'data',
        'status_code_value': 'status_code_value'
    }

    def __init__(self, code=None, execution_id=None, data=None, status_code_value=None, _configuration=None):  # noqa: E501
        """StatusInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._execution_id = None
        self._data = None
        self._status_code_value = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if execution_id is not None:
            self.execution_id = execution_id
        if data is not None:
            self.data = data
        if status_code_value is not None:
            self.status_code_value = status_code_value

    @property
    def code(self):
        """Gets the code of this StatusInfo.  # noqa: E501


        :return: The code of this StatusInfo.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StatusInfo.


        :param code: The code of this StatusInfo.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def execution_id(self):
        """Gets the execution_id of this StatusInfo.  # noqa: E501


        :return: The execution_id of this StatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this StatusInfo.


        :param execution_id: The execution_id of this StatusInfo.  # noqa: E501
        :type: str
        """

        self._execution_id = execution_id

    @property
    def data(self):
        """Gets the data of this StatusInfo.  # noqa: E501


        :return: The data of this StatusInfo.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this StatusInfo.


        :param data: The data of this StatusInfo.  # noqa: E501
        :type: dict(str, str)
        """

        self._data = data

    @property
    def status_code_value(self):
        """Gets the status_code_value of this StatusInfo.  # noqa: E501


        :return: The status_code_value of this StatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._status_code_value

    @status_code_value.setter
    def status_code_value(self, status_code_value):
        """Sets the status_code_value of this StatusInfo.


        :param status_code_value: The status_code_value of this StatusInfo.  # noqa: E501
        :type: str
        """

        self._status_code_value = status_code_value

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
        if issubclass(StatusInfo, dict):
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
        if not isinstance(other, StatusInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatusInfo):
            return True

        return self.to_dict() != other.to_dict()
