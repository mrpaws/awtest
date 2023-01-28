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


class BaseExceptionModel(object):
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
        'error_code': 'int',
        'message': 'object',
        'activity_id': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'message': 'message',
        'activity_id': 'activityId',
        'links': 'links'
    }

    def __init__(self, error_code=None, message=None, activity_id=None, links=None, _configuration=None):  # noqa: E501
        """BaseExceptionModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error_code = None
        self._message = None
        self._activity_id = None
        self._links = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if message is not None:
            self.message = message
        if activity_id is not None:
            self.activity_id = activity_id
        if links is not None:
            self.links = links

    @property
    def error_code(self):
        """Gets the error_code of this BaseExceptionModel.  # noqa: E501

        Gets or sets application error code.  # noqa: E501

        :return: The error_code of this BaseExceptionModel.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this BaseExceptionModel.

        Gets or sets application error code.  # noqa: E501

        :param error_code: The error_code of this BaseExceptionModel.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def message(self):
        """Gets the message of this BaseExceptionModel.  # noqa: E501

        Gets or sets friendly error message.  # noqa: E501

        :return: The message of this BaseExceptionModel.  # noqa: E501
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BaseExceptionModel.

        Gets or sets friendly error message.  # noqa: E501

        :param message: The message of this BaseExceptionModel.  # noqa: E501
        :type: object
        """

        self._message = message

    @property
    def activity_id(self):
        """Gets the activity_id of this BaseExceptionModel.  # noqa: E501

        Gets or sets transactionId of the request.  # noqa: E501

        :return: The activity_id of this BaseExceptionModel.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this BaseExceptionModel.

        Gets or sets transactionId of the request.  # noqa: E501

        :param activity_id: The activity_id of this BaseExceptionModel.  # noqa: E501
        :type: str
        """

        self._activity_id = activity_id

    @property
    def links(self):
        """Gets the links of this BaseExceptionModel.  # noqa: E501

        Gets or sets list of hypermedia link.  # noqa: E501

        :return: The links of this BaseExceptionModel.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BaseExceptionModel.

        Gets or sets list of hypermedia link.  # noqa: E501

        :param links: The links of this BaseExceptionModel.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if issubclass(BaseExceptionModel, dict):
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
        if not isinstance(other, BaseExceptionModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseExceptionModel):
            return True

        return self.to_dict() != other.to_dict()