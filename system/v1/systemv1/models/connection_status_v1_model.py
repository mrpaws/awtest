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


class ConnectionStatusV1Model(object):
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
        'connection_status': 'int',
        'organization_group_uuid': 'str',
        'organization_group_name': 'str'
    }

    attribute_map = {
        'connection_status': 'connection_status',
        'organization_group_uuid': 'organization_group_uuid',
        'organization_group_name': 'organization_group_name'
    }

    def __init__(self, connection_status=None, organization_group_uuid=None, organization_group_name=None, _configuration=None):  # noqa: E501
        """ConnectionStatusV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connection_status = None
        self._organization_group_uuid = None
        self._organization_group_name = None
        self.discriminator = None

        self.connection_status = connection_status
        self.organization_group_uuid = organization_group_uuid
        self.organization_group_name = organization_group_name

    @property
    def connection_status(self):
        """Gets the connection_status of this ConnectionStatusV1Model.  # noqa: E501

        The status of the connection.  # noqa: E501

        :return: The connection_status of this ConnectionStatusV1Model.  # noqa: E501
        :rtype: int
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this ConnectionStatusV1Model.

        The status of the connection.  # noqa: E501

        :param connection_status: The connection_status of this ConnectionStatusV1Model.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and connection_status is None:
            raise ValueError("Invalid value for `connection_status`, must not be `None`")  # noqa: E501
        allowed_values = [0, 1, 2]  # noqa: E501
        if (self._configuration.client_side_validation and
                connection_status not in allowed_values):
            raise ValueError(
                "Invalid value for `connection_status` ({0}), must be one of {1}"  # noqa: E501
                .format(connection_status, allowed_values)
            )

        self._connection_status = connection_status

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this ConnectionStatusV1Model.  # noqa: E501

        The unique identifier of the organization group.  # noqa: E501

        :return: The organization_group_uuid of this ConnectionStatusV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this ConnectionStatusV1Model.

        The unique identifier of the organization group.  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this ConnectionStatusV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and organization_group_uuid is None:
            raise ValueError("Invalid value for `organization_group_uuid`, must not be `None`")  # noqa: E501

        self._organization_group_uuid = organization_group_uuid

    @property
    def organization_group_name(self):
        """Gets the organization_group_name of this ConnectionStatusV1Model.  # noqa: E501

        The name of the organization group.  # noqa: E501

        :return: The organization_group_name of this ConnectionStatusV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_name

    @organization_group_name.setter
    def organization_group_name(self, organization_group_name):
        """Sets the organization_group_name of this ConnectionStatusV1Model.

        The name of the organization group.  # noqa: E501

        :param organization_group_name: The organization_group_name of this ConnectionStatusV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and organization_group_name is None:
            raise ValueError("Invalid value for `organization_group_name`, must not be `None`")  # noqa: E501

        self._organization_group_name = organization_group_name

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
        if issubclass(ConnectionStatusV1Model, dict):
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
        if not isinstance(other, ConnectionStatusV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectionStatusV1Model):
            return True

        return self.to_dict() != other.to_dict()
