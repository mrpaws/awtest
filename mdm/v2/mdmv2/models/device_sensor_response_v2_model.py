# coding: utf-8

"""
    MDM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv2.configuration import Configuration


class DeviceSensorResponseV2Model(object):
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
        'description': 'str',
        'organization_group_name': 'str',
        'is_read_only': 'bool',
        'organization_group_uuid': 'str',
        'platform': 'int',
        'query_type': 'int',
        'query_response_type': 'int',
        'execution_context': 'int',
        'execution_architecture': 'int',
        'script_data': 'str',
        'timeout': 'int',
        'script_environment_variables': 'list[DeviceSensorScriptEnvironmentVariableV1]',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'organization_group_name': 'organization_group_name',
        'is_read_only': 'is_read_only',
        'organization_group_uuid': 'organization_group_uuid',
        'platform': 'platform',
        'query_type': 'query_type',
        'query_response_type': 'query_response_type',
        'execution_context': 'execution_context',
        'execution_architecture': 'execution_architecture',
        'script_data': 'script_data',
        'timeout': 'timeout',
        'script_environment_variables': 'script_environment_variables',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, name=None, description=None, organization_group_name=None, is_read_only=None, organization_group_uuid=None, platform=None, query_type=None, query_response_type=None, execution_context=None, execution_architecture=None, script_data=None, timeout=None, script_environment_variables=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """DeviceSensorResponseV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._organization_group_name = None
        self._is_read_only = None
        self._organization_group_uuid = None
        self._platform = None
        self._query_type = None
        self._query_response_type = None
        self._execution_context = None
        self._execution_architecture = None
        self._script_data = None
        self._timeout = None
        self._script_environment_variables = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if organization_group_name is not None:
            self.organization_group_name = organization_group_name
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if platform is not None:
            self.platform = platform
        if query_type is not None:
            self.query_type = query_type
        if query_response_type is not None:
            self.query_response_type = query_response_type
        if execution_context is not None:
            self.execution_context = execution_context
        if execution_architecture is not None:
            self.execution_architecture = execution_architecture
        if script_data is not None:
            self.script_data = script_data
        if timeout is not None:
            self.timeout = timeout
        if script_environment_variables is not None:
            self.script_environment_variables = script_environment_variables
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def name(self):
        """Gets the name of this DeviceSensorResponseV2Model.  # noqa: E501

        Name of the device sensor.  # noqa: E501

        :return: The name of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceSensorResponseV2Model.

        Name of the device sensor.  # noqa: E501

        :param name: The name of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this DeviceSensorResponseV2Model.  # noqa: E501

        Description of the device sensor.  # noqa: E501

        :return: The description of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceSensorResponseV2Model.

        Description of the device sensor.  # noqa: E501

        :param description: The description of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def organization_group_name(self):
        """Gets the organization_group_name of this DeviceSensorResponseV2Model.  # noqa: E501

        Organization Group name the device sensor is managed by.  # noqa: E501

        :return: The organization_group_name of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_name

    @organization_group_name.setter
    def organization_group_name(self, organization_group_name):
        """Sets the organization_group_name of this DeviceSensorResponseV2Model.

        Organization Group name the device sensor is managed by.  # noqa: E501

        :param organization_group_name: The organization_group_name of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: str
        """

        self._organization_group_name = organization_group_name

    @property
    def is_read_only(self):
        """Gets the is_read_only of this DeviceSensorResponseV2Model.  # noqa: E501

        Specifies if the sensor is read only with respect to the current Organization Group.  # noqa: E501

        :return: The is_read_only of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this DeviceSensorResponseV2Model.

        Specifies if the sensor is read only with respect to the current Organization Group.  # noqa: E501

        :param is_read_only: The is_read_only of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: bool
        """

        self._is_read_only = is_read_only

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this DeviceSensorResponseV2Model.  # noqa: E501

        Identifier of the Organization Group.  # noqa: E501

        :return: The organization_group_uuid of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this DeviceSensorResponseV2Model.

        Identifier of the Organization Group.  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def platform(self):
        """Gets the platform of this DeviceSensorResponseV2Model.  # noqa: E501

        Platform for which the device sensor will be created.  # noqa: E501

        :return: The platform of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: int
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this DeviceSensorResponseV2Model.

        Platform for which the device sensor will be created.  # noqa: E501

        :param platform: The platform of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 17, 21]  # noqa: E501
        if (self._configuration.client_side_validation and
                platform not in allowed_values):
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"  # noqa: E501
                .format(platform, allowed_values)
            )

        self._platform = platform

    @property
    def query_type(self):
        """Gets the query_type of this DeviceSensorResponseV2Model.  # noqa: E501

        Query type of the script.  # noqa: E501

        :return: The query_type of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: int
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this DeviceSensorResponseV2Model.

        Query type of the script.  # noqa: E501

        :param query_type: The query_type of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4]  # noqa: E501
        if (self._configuration.client_side_validation and
                query_type not in allowed_values):
            raise ValueError(
                "Invalid value for `query_type` ({0}), must be one of {1}"  # noqa: E501
                .format(query_type, allowed_values)
            )

        self._query_type = query_type

    @property
    def query_response_type(self):
        """Gets the query_response_type of this DeviceSensorResponseV2Model.  # noqa: E501

        Response type of the data.  # noqa: E501

        :return: The query_response_type of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: int
        """
        return self._query_response_type

    @query_response_type.setter
    def query_response_type(self, query_response_type):
        """Sets the query_response_type of this DeviceSensorResponseV2Model.

        Response type of the data.  # noqa: E501

        :param query_response_type: The query_response_type of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4]  # noqa: E501
        if (self._configuration.client_side_validation and
                query_response_type not in allowed_values):
            raise ValueError(
                "Invalid value for `query_response_type` ({0}), must be one of {1}"  # noqa: E501
                .format(query_response_type, allowed_values)
            )

        self._query_response_type = query_response_type

    @property
    def execution_context(self):
        """Gets the execution_context of this DeviceSensorResponseV2Model.  # noqa: E501

        Execution context under which the script would be run on the device.  # noqa: E501

        :return: The execution_context of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: int
        """
        return self._execution_context

    @execution_context.setter
    def execution_context(self, execution_context):
        """Sets the execution_context of this DeviceSensorResponseV2Model.

        Execution context under which the script would be run on the device.  # noqa: E501

        :param execution_context: The execution_context of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3]  # noqa: E501
        if (self._configuration.client_side_validation and
                execution_context not in allowed_values):
            raise ValueError(
                "Invalid value for `execution_context` ({0}), must be one of {1}"  # noqa: E501
                .format(execution_context, allowed_values)
            )

        self._execution_context = execution_context

    @property
    def execution_architecture(self):
        """Gets the execution_architecture of this DeviceSensorResponseV2Model.  # noqa: E501

        Execution architecture under which the script would be run on the device.  # noqa: E501

        :return: The execution_architecture of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: int
        """
        return self._execution_architecture

    @execution_architecture.setter
    def execution_architecture(self, execution_architecture):
        """Sets the execution_architecture of this DeviceSensorResponseV2Model.

        Execution architecture under which the script would be run on the device.  # noqa: E501

        :param execution_architecture: The execution_architecture of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4]  # noqa: E501
        if (self._configuration.client_side_validation and
                execution_architecture not in allowed_values):
            raise ValueError(
                "Invalid value for `execution_architecture` ({0}), must be one of {1}"  # noqa: E501
                .format(execution_architecture, allowed_values)
            )

        self._execution_architecture = execution_architecture

    @property
    def script_data(self):
        """Gets the script_data of this DeviceSensorResponseV2Model.  # noqa: E501

        Base64 encoded script to be executed on the device.  # noqa: E501

        :return: The script_data of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: str
        """
        return self._script_data

    @script_data.setter
    def script_data(self, script_data):
        """Sets the script_data of this DeviceSensorResponseV2Model.

        Base64 encoded script to be executed on the device.  # noqa: E501

        :param script_data: The script_data of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: str
        """

        self._script_data = script_data

    @property
    def timeout(self):
        """Gets the timeout of this DeviceSensorResponseV2Model.  # noqa: E501

        Defines timeout(in seconds) for the script execution.  # noqa: E501

        :return: The timeout of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this DeviceSensorResponseV2Model.

        Defines timeout(in seconds) for the script execution.  # noqa: E501

        :param timeout: The timeout of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def script_environment_variables(self):
        """Gets the script_environment_variables of this DeviceSensorResponseV2Model.  # noqa: E501

        Key Value pairs for the environment variables used in scripts.  # noqa: E501

        :return: The script_environment_variables of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: list[DeviceSensorScriptEnvironmentVariableV1]
        """
        return self._script_environment_variables

    @script_environment_variables.setter
    def script_environment_variables(self, script_environment_variables):
        """Sets the script_environment_variables of this DeviceSensorResponseV2Model.

        Key Value pairs for the environment variables used in scripts.  # noqa: E501

        :param script_environment_variables: The script_environment_variables of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: list[DeviceSensorScriptEnvironmentVariableV1]
        """

        self._script_environment_variables = script_environment_variables

    @property
    def id(self):
        """Gets the id of this DeviceSensorResponseV2Model.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceSensorResponseV2Model.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this DeviceSensorResponseV2Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this DeviceSensorResponseV2Model.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this DeviceSensorResponseV2Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DeviceSensorResponseV2Model.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this DeviceSensorResponseV2Model.  # noqa: E501
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
        if issubclass(DeviceSensorResponseV2Model, dict):
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
        if not isinstance(other, DeviceSensorResponseV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceSensorResponseV2Model):
            return True

        return self.to_dict() != other.to_dict()
