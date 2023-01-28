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


class RelayServerAssignmentModel(object):
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
        'managed_by': 'str',
        'managed_by_uuid': 'str',
        'staging_server': 'list[int]',
        'staging_server_uuid': 'list[str]',
        'production_server': 'list[int]',
        'production_server_uuid': 'list[str]'
    }

    attribute_map = {
        'managed_by': 'ManagedBy',
        'managed_by_uuid': 'ManagedByUuid',
        'staging_server': 'StagingServer',
        'staging_server_uuid': 'StagingServerUuid',
        'production_server': 'ProductionServer',
        'production_server_uuid': 'ProductionServerUuid'
    }

    def __init__(self, managed_by=None, managed_by_uuid=None, staging_server=None, staging_server_uuid=None, production_server=None, production_server_uuid=None, _configuration=None):  # noqa: E501
        """RelayServerAssignmentModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._managed_by = None
        self._managed_by_uuid = None
        self._staging_server = None
        self._staging_server_uuid = None
        self._production_server = None
        self._production_server_uuid = None
        self.discriminator = None

        if managed_by is not None:
            self.managed_by = managed_by
        if managed_by_uuid is not None:
            self.managed_by_uuid = managed_by_uuid
        if staging_server is not None:
            self.staging_server = staging_server
        if staging_server_uuid is not None:
            self.staging_server_uuid = staging_server_uuid
        if production_server is not None:
            self.production_server = production_server
        if production_server_uuid is not None:
            self.production_server_uuid = production_server_uuid

    @property
    def managed_by(self):
        """Gets the managed_by of this RelayServerAssignmentModel.  # noqa: E501

        Gets or sets the organization group identifier under which the relay server is managed.  # noqa: E501

        :return: The managed_by of this RelayServerAssignmentModel.  # noqa: E501
        :rtype: str
        """
        return self._managed_by

    @managed_by.setter
    def managed_by(self, managed_by):
        """Sets the managed_by of this RelayServerAssignmentModel.

        Gets or sets the organization group identifier under which the relay server is managed.  # noqa: E501

        :param managed_by: The managed_by of this RelayServerAssignmentModel.  # noqa: E501
        :type: str
        """

        self._managed_by = managed_by

    @property
    def managed_by_uuid(self):
        """Gets the managed_by_uuid of this RelayServerAssignmentModel.  # noqa: E501

        Gets or sets the organization unique group identifier under which the relay server is managed.  # noqa: E501

        :return: The managed_by_uuid of this RelayServerAssignmentModel.  # noqa: E501
        :rtype: str
        """
        return self._managed_by_uuid

    @managed_by_uuid.setter
    def managed_by_uuid(self, managed_by_uuid):
        """Sets the managed_by_uuid of this RelayServerAssignmentModel.

        Gets or sets the organization unique group identifier under which the relay server is managed.  # noqa: E501

        :param managed_by_uuid: The managed_by_uuid of this RelayServerAssignmentModel.  # noqa: E501
        :type: str
        """

        self._managed_by_uuid = managed_by_uuid

    @property
    def staging_server(self):
        """Gets the staging_server of this RelayServerAssignmentModel.  # noqa: E501

        Gets or sets the Staging Servers.  # noqa: E501

        :return: The staging_server of this RelayServerAssignmentModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._staging_server

    @staging_server.setter
    def staging_server(self, staging_server):
        """Sets the staging_server of this RelayServerAssignmentModel.

        Gets or sets the Staging Servers.  # noqa: E501

        :param staging_server: The staging_server of this RelayServerAssignmentModel.  # noqa: E501
        :type: list[int]
        """

        self._staging_server = staging_server

    @property
    def staging_server_uuid(self):
        """Gets the staging_server_uuid of this RelayServerAssignmentModel.  # noqa: E501

        Gets or sets the Staging Servers Unique Organization Group Uuids.  # noqa: E501

        :return: The staging_server_uuid of this RelayServerAssignmentModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._staging_server_uuid

    @staging_server_uuid.setter
    def staging_server_uuid(self, staging_server_uuid):
        """Sets the staging_server_uuid of this RelayServerAssignmentModel.

        Gets or sets the Staging Servers Unique Organization Group Uuids.  # noqa: E501

        :param staging_server_uuid: The staging_server_uuid of this RelayServerAssignmentModel.  # noqa: E501
        :type: list[str]
        """

        self._staging_server_uuid = staging_server_uuid

    @property
    def production_server(self):
        """Gets the production_server of this RelayServerAssignmentModel.  # noqa: E501

        Gets or sets the Production Servers.  # noqa: E501

        :return: The production_server of this RelayServerAssignmentModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._production_server

    @production_server.setter
    def production_server(self, production_server):
        """Sets the production_server of this RelayServerAssignmentModel.

        Gets or sets the Production Servers.  # noqa: E501

        :param production_server: The production_server of this RelayServerAssignmentModel.  # noqa: E501
        :type: list[int]
        """

        self._production_server = production_server

    @property
    def production_server_uuid(self):
        """Gets the production_server_uuid of this RelayServerAssignmentModel.  # noqa: E501

        Gets or sets the Production Servers Unique Organization Group Uuids.  # noqa: E501

        :return: The production_server_uuid of this RelayServerAssignmentModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._production_server_uuid

    @production_server_uuid.setter
    def production_server_uuid(self, production_server_uuid):
        """Sets the production_server_uuid of this RelayServerAssignmentModel.

        Gets or sets the Production Servers Unique Organization Group Uuids.  # noqa: E501

        :param production_server_uuid: The production_server_uuid of this RelayServerAssignmentModel.  # noqa: E501
        :type: list[str]
        """

        self._production_server_uuid = production_server_uuid

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
        if issubclass(RelayServerAssignmentModel, dict):
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
        if not isinstance(other, RelayServerAssignmentModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelayServerAssignmentModel):
            return True

        return self.to_dict() != other.to_dict()
