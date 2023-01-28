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


class UpdateScript(object):
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
        'script_uuid': 'str',
        'version': 'str',
        'name': 'str',
        'description': 'str',
        'platform': 'int',
        'organization_group_uuid': 'str',
        'is_idempotent': 'bool',
        'allowed_in_catalog': 'bool',
        'script_data': 'str',
        'timeout': 'int',
        'script_type': 'int',
        'execution_context': 'int',
        'platform_architecture': 'int',
        'catalog_display': 'CatalogDisplay',
        'script_variables': 'list[ScriptVariables]',
        'created_by': 'str',
        'user_interaction': 'bool'
    }

    attribute_map = {
        'script_uuid': 'script_uuid',
        'version': 'version',
        'name': 'name',
        'description': 'description',
        'platform': 'platform',
        'organization_group_uuid': 'organization_group_uuid',
        'is_idempotent': 'is_idempotent',
        'allowed_in_catalog': 'allowed_in_catalog',
        'script_data': 'script_data',
        'timeout': 'timeout',
        'script_type': 'script_type',
        'execution_context': 'execution_context',
        'platform_architecture': 'platform_architecture',
        'catalog_display': 'catalog_display',
        'script_variables': 'script_variables',
        'created_by': 'created_by',
        'user_interaction': 'user_interaction'
    }

    def __init__(self, script_uuid=None, version=None, name=None, description=None, platform=None, organization_group_uuid=None, is_idempotent=None, allowed_in_catalog=None, script_data=None, timeout=None, script_type=None, execution_context=None, platform_architecture=None, catalog_display=None, script_variables=None, created_by=None, user_interaction=None, _configuration=None):  # noqa: E501
        """UpdateScript - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._script_uuid = None
        self._version = None
        self._name = None
        self._description = None
        self._platform = None
        self._organization_group_uuid = None
        self._is_idempotent = None
        self._allowed_in_catalog = None
        self._script_data = None
        self._timeout = None
        self._script_type = None
        self._execution_context = None
        self._platform_architecture = None
        self._catalog_display = None
        self._script_variables = None
        self._created_by = None
        self._user_interaction = None
        self.discriminator = None

        if script_uuid is not None:
            self.script_uuid = script_uuid
        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if platform is not None:
            self.platform = platform
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if is_idempotent is not None:
            self.is_idempotent = is_idempotent
        if allowed_in_catalog is not None:
            self.allowed_in_catalog = allowed_in_catalog
        if script_data is not None:
            self.script_data = script_data
        if timeout is not None:
            self.timeout = timeout
        if script_type is not None:
            self.script_type = script_type
        if execution_context is not None:
            self.execution_context = execution_context
        if platform_architecture is not None:
            self.platform_architecture = platform_architecture
        if catalog_display is not None:
            self.catalog_display = catalog_display
        if script_variables is not None:
            self.script_variables = script_variables
        if created_by is not None:
            self.created_by = created_by
        if user_interaction is not None:
            self.user_interaction = user_interaction

    @property
    def script_uuid(self):
        """Gets the script_uuid of this UpdateScript.  # noqa: E501


        :return: The script_uuid of this UpdateScript.  # noqa: E501
        :rtype: str
        """
        return self._script_uuid

    @script_uuid.setter
    def script_uuid(self, script_uuid):
        """Sets the script_uuid of this UpdateScript.


        :param script_uuid: The script_uuid of this UpdateScript.  # noqa: E501
        :type: str
        """

        self._script_uuid = script_uuid

    @property
    def version(self):
        """Gets the version of this UpdateScript.  # noqa: E501


        :return: The version of this UpdateScript.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateScript.


        :param version: The version of this UpdateScript.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this UpdateScript.  # noqa: E501


        :return: The name of this UpdateScript.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateScript.


        :param name: The name of this UpdateScript.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateScript.  # noqa: E501


        :return: The description of this UpdateScript.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateScript.


        :param description: The description of this UpdateScript.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def platform(self):
        """Gets the platform of this UpdateScript.  # noqa: E501


        :return: The platform of this UpdateScript.  # noqa: E501
        :rtype: int
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this UpdateScript.


        :param platform: The platform of this UpdateScript.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 5, 6, 8, 9, 10, 11, 12, 15, 16, 18, 21]  # noqa: E501
        if (self._configuration.client_side_validation and
                platform not in allowed_values):
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"  # noqa: E501
                .format(platform, allowed_values)
            )

        self._platform = platform

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this UpdateScript.  # noqa: E501


        :return: The organization_group_uuid of this UpdateScript.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this UpdateScript.


        :param organization_group_uuid: The organization_group_uuid of this UpdateScript.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def is_idempotent(self):
        """Gets the is_idempotent of this UpdateScript.  # noqa: E501


        :return: The is_idempotent of this UpdateScript.  # noqa: E501
        :rtype: bool
        """
        return self._is_idempotent

    @is_idempotent.setter
    def is_idempotent(self, is_idempotent):
        """Sets the is_idempotent of this UpdateScript.


        :param is_idempotent: The is_idempotent of this UpdateScript.  # noqa: E501
        :type: bool
        """

        self._is_idempotent = is_idempotent

    @property
    def allowed_in_catalog(self):
        """Gets the allowed_in_catalog of this UpdateScript.  # noqa: E501


        :return: The allowed_in_catalog of this UpdateScript.  # noqa: E501
        :rtype: bool
        """
        return self._allowed_in_catalog

    @allowed_in_catalog.setter
    def allowed_in_catalog(self, allowed_in_catalog):
        """Sets the allowed_in_catalog of this UpdateScript.


        :param allowed_in_catalog: The allowed_in_catalog of this UpdateScript.  # noqa: E501
        :type: bool
        """

        self._allowed_in_catalog = allowed_in_catalog

    @property
    def script_data(self):
        """Gets the script_data of this UpdateScript.  # noqa: E501


        :return: The script_data of this UpdateScript.  # noqa: E501
        :rtype: str
        """
        return self._script_data

    @script_data.setter
    def script_data(self, script_data):
        """Sets the script_data of this UpdateScript.


        :param script_data: The script_data of this UpdateScript.  # noqa: E501
        :type: str
        """

        self._script_data = script_data

    @property
    def timeout(self):
        """Gets the timeout of this UpdateScript.  # noqa: E501


        :return: The timeout of this UpdateScript.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this UpdateScript.


        :param timeout: The timeout of this UpdateScript.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def script_type(self):
        """Gets the script_type of this UpdateScript.  # noqa: E501


        :return: The script_type of this UpdateScript.  # noqa: E501
        :rtype: int
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this UpdateScript.


        :param script_type: The script_type of this UpdateScript.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4]  # noqa: E501
        if (self._configuration.client_side_validation and
                script_type not in allowed_values):
            raise ValueError(
                "Invalid value for `script_type` ({0}), must be one of {1}"  # noqa: E501
                .format(script_type, allowed_values)
            )

        self._script_type = script_type

    @property
    def execution_context(self):
        """Gets the execution_context of this UpdateScript.  # noqa: E501


        :return: The execution_context of this UpdateScript.  # noqa: E501
        :rtype: int
        """
        return self._execution_context

    @execution_context.setter
    def execution_context(self, execution_context):
        """Sets the execution_context of this UpdateScript.


        :param execution_context: The execution_context of this UpdateScript.  # noqa: E501
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
    def platform_architecture(self):
        """Gets the platform_architecture of this UpdateScript.  # noqa: E501


        :return: The platform_architecture of this UpdateScript.  # noqa: E501
        :rtype: int
        """
        return self._platform_architecture

    @platform_architecture.setter
    def platform_architecture(self, platform_architecture):
        """Sets the platform_architecture of this UpdateScript.


        :param platform_architecture: The platform_architecture of this UpdateScript.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 4, 8, 16]  # noqa: E501
        if (self._configuration.client_side_validation and
                platform_architecture not in allowed_values):
            raise ValueError(
                "Invalid value for `platform_architecture` ({0}), must be one of {1}"  # noqa: E501
                .format(platform_architecture, allowed_values)
            )

        self._platform_architecture = platform_architecture

    @property
    def catalog_display(self):
        """Gets the catalog_display of this UpdateScript.  # noqa: E501


        :return: The catalog_display of this UpdateScript.  # noqa: E501
        :rtype: CatalogDisplay
        """
        return self._catalog_display

    @catalog_display.setter
    def catalog_display(self, catalog_display):
        """Sets the catalog_display of this UpdateScript.


        :param catalog_display: The catalog_display of this UpdateScript.  # noqa: E501
        :type: CatalogDisplay
        """

        self._catalog_display = catalog_display

    @property
    def script_variables(self):
        """Gets the script_variables of this UpdateScript.  # noqa: E501


        :return: The script_variables of this UpdateScript.  # noqa: E501
        :rtype: list[ScriptVariables]
        """
        return self._script_variables

    @script_variables.setter
    def script_variables(self, script_variables):
        """Sets the script_variables of this UpdateScript.


        :param script_variables: The script_variables of this UpdateScript.  # noqa: E501
        :type: list[ScriptVariables]
        """

        self._script_variables = script_variables

    @property
    def created_by(self):
        """Gets the created_by of this UpdateScript.  # noqa: E501


        :return: The created_by of this UpdateScript.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UpdateScript.


        :param created_by: The created_by of this UpdateScript.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def user_interaction(self):
        """Gets the user_interaction of this UpdateScript.  # noqa: E501


        :return: The user_interaction of this UpdateScript.  # noqa: E501
        :rtype: bool
        """
        return self._user_interaction

    @user_interaction.setter
    def user_interaction(self, user_interaction):
        """Sets the user_interaction of this UpdateScript.


        :param user_interaction: The user_interaction of this UpdateScript.  # noqa: E501
        :type: bool
        """

        self._user_interaction = user_interaction

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
        if issubclass(UpdateScript, dict):
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
        if not isinstance(other, UpdateScript):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateScript):
            return True

        return self.to_dict() != other.to_dict()