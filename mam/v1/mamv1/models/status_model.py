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


class StatusModel(object):
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
        'status': 'str',
        'status_code': 'int',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'status': 'status',
        'status_code': 'statusCode',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, status=None, status_code=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """StatusModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._status_code = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if status_code is not None:
            self.status_code = status_code
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def status(self):
        """Gets the status of this StatusModel.  # noqa: E501

        Gets or sets satus for the last Sync Asset job, InProgress/Complete/CompletedWthErrors.  # noqa: E501

        :return: The status of this StatusModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StatusModel.

        Gets or sets satus for the last Sync Asset job, InProgress/Complete/CompletedWthErrors.  # noqa: E501

        :param status: The status of this StatusModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_code(self):
        """Gets the status_code of this StatusModel.  # noqa: E501

        Gets or sets status code for the last sync request,  1(In Progress)/2(Complete)/3(CompletedWthErrors).  # noqa: E501

        :return: The status_code of this StatusModel.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this StatusModel.

        Gets or sets status code for the last sync request,  1(In Progress)/2(Complete)/3(CompletedWthErrors).  # noqa: E501

        :param status_code: The status_code of this StatusModel.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def id(self):
        """Gets the id of this StatusModel.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this StatusModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StatusModel.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this StatusModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this StatusModel.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this StatusModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this StatusModel.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this StatusModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(StatusModel, dict):
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
        if not isinstance(other, StatusModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatusModel):
            return True

        return self.to_dict() != other.to_dict()
