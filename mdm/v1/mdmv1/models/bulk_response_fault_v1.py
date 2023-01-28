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


class BulkResponseFaultV1(object):
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
        'request_item': 'object',
        'message': 'str',
        'error_code': 'int'
    }

    attribute_map = {
        'request_item': 'request_item',
        'message': 'message',
        'error_code': 'error_code'
    }

    def __init__(self, request_item=None, message=None, error_code=None, _configuration=None):  # noqa: E501
        """BulkResponseFaultV1 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._request_item = None
        self._message = None
        self._error_code = None
        self.discriminator = None

        if request_item is not None:
            self.request_item = request_item
        if message is not None:
            self.message = message
        if error_code is not None:
            self.error_code = error_code

    @property
    def request_item(self):
        """Gets the request_item of this BulkResponseFaultV1.  # noqa: E501

        The identifier of the failed request item.  # noqa: E501

        :return: The request_item of this BulkResponseFaultV1.  # noqa: E501
        :rtype: object
        """
        return self._request_item

    @request_item.setter
    def request_item(self, request_item):
        """Sets the request_item of this BulkResponseFaultV1.

        The identifier of the failed request item.  # noqa: E501

        :param request_item: The request_item of this BulkResponseFaultV1.  # noqa: E501
        :type: object
        """

        self._request_item = request_item

    @property
    def message(self):
        """Gets the message of this BulkResponseFaultV1.  # noqa: E501

        The error message for the failure of request item.  # noqa: E501

        :return: The message of this BulkResponseFaultV1.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BulkResponseFaultV1.

        The error message for the failure of request item.  # noqa: E501

        :param message: The message of this BulkResponseFaultV1.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def error_code(self):
        """Gets the error_code of this BulkResponseFaultV1.  # noqa: E501

        The error code for the failure of request item.  # noqa: E501

        :return: The error_code of this BulkResponseFaultV1.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this BulkResponseFaultV1.

        The error code for the failure of request item.  # noqa: E501

        :param error_code: The error_code of this BulkResponseFaultV1.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

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
        if issubclass(BulkResponseFaultV1, dict):
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
        if not isinstance(other, BulkResponseFaultV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkResponseFaultV1):
            return True

        return self.to_dict() != other.to_dict()
