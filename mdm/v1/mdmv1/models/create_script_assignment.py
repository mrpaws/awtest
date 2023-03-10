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


class CreateScriptAssignment(object):
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
        'assignment_uuid': 'str',
        'version': 'str',
        'script_deployment': 'ScriptDeployment',
        'name': 'str',
        'created_by': 'str',
        'organization_group_uuid': 'str',
        'priority': 'int',
        'show_in_catalog': 'bool',
        'deployment_mode': 'int',
        'memberships': 'list[SmartGroupData]'
    }

    attribute_map = {
        'assignment_uuid': 'assignment_uuid',
        'version': 'version',
        'script_deployment': 'script_deployment',
        'name': 'name',
        'created_by': 'created_by',
        'organization_group_uuid': 'organization_group_uuid',
        'priority': 'priority',
        'show_in_catalog': 'show_in_catalog',
        'deployment_mode': 'deployment_mode',
        'memberships': 'memberships'
    }

    def __init__(self, assignment_uuid=None, version=None, script_deployment=None, name=None, created_by=None, organization_group_uuid=None, priority=None, show_in_catalog=None, deployment_mode=None, memberships=None, _configuration=None):  # noqa: E501
        """CreateScriptAssignment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assignment_uuid = None
        self._version = None
        self._script_deployment = None
        self._name = None
        self._created_by = None
        self._organization_group_uuid = None
        self._priority = None
        self._show_in_catalog = None
        self._deployment_mode = None
        self._memberships = None
        self.discriminator = None

        if assignment_uuid is not None:
            self.assignment_uuid = assignment_uuid
        if version is not None:
            self.version = version
        if script_deployment is not None:
            self.script_deployment = script_deployment
        if name is not None:
            self.name = name
        if created_by is not None:
            self.created_by = created_by
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if priority is not None:
            self.priority = priority
        if show_in_catalog is not None:
            self.show_in_catalog = show_in_catalog
        if deployment_mode is not None:
            self.deployment_mode = deployment_mode
        if memberships is not None:
            self.memberships = memberships

    @property
    def assignment_uuid(self):
        """Gets the assignment_uuid of this CreateScriptAssignment.  # noqa: E501


        :return: The assignment_uuid of this CreateScriptAssignment.  # noqa: E501
        :rtype: str
        """
        return self._assignment_uuid

    @assignment_uuid.setter
    def assignment_uuid(self, assignment_uuid):
        """Sets the assignment_uuid of this CreateScriptAssignment.


        :param assignment_uuid: The assignment_uuid of this CreateScriptAssignment.  # noqa: E501
        :type: str
        """

        self._assignment_uuid = assignment_uuid

    @property
    def version(self):
        """Gets the version of this CreateScriptAssignment.  # noqa: E501


        :return: The version of this CreateScriptAssignment.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateScriptAssignment.


        :param version: The version of this CreateScriptAssignment.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def script_deployment(self):
        """Gets the script_deployment of this CreateScriptAssignment.  # noqa: E501


        :return: The script_deployment of this CreateScriptAssignment.  # noqa: E501
        :rtype: ScriptDeployment
        """
        return self._script_deployment

    @script_deployment.setter
    def script_deployment(self, script_deployment):
        """Sets the script_deployment of this CreateScriptAssignment.


        :param script_deployment: The script_deployment of this CreateScriptAssignment.  # noqa: E501
        :type: ScriptDeployment
        """

        self._script_deployment = script_deployment

    @property
    def name(self):
        """Gets the name of this CreateScriptAssignment.  # noqa: E501


        :return: The name of this CreateScriptAssignment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateScriptAssignment.


        :param name: The name of this CreateScriptAssignment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_by(self):
        """Gets the created_by of this CreateScriptAssignment.  # noqa: E501


        :return: The created_by of this CreateScriptAssignment.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CreateScriptAssignment.


        :param created_by: The created_by of this CreateScriptAssignment.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this CreateScriptAssignment.  # noqa: E501


        :return: The organization_group_uuid of this CreateScriptAssignment.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this CreateScriptAssignment.


        :param organization_group_uuid: The organization_group_uuid of this CreateScriptAssignment.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def priority(self):
        """Gets the priority of this CreateScriptAssignment.  # noqa: E501


        :return: The priority of this CreateScriptAssignment.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateScriptAssignment.


        :param priority: The priority of this CreateScriptAssignment.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def show_in_catalog(self):
        """Gets the show_in_catalog of this CreateScriptAssignment.  # noqa: E501


        :return: The show_in_catalog of this CreateScriptAssignment.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_catalog

    @show_in_catalog.setter
    def show_in_catalog(self, show_in_catalog):
        """Sets the show_in_catalog of this CreateScriptAssignment.


        :param show_in_catalog: The show_in_catalog of this CreateScriptAssignment.  # noqa: E501
        :type: bool
        """

        self._show_in_catalog = show_in_catalog

    @property
    def deployment_mode(self):
        """Gets the deployment_mode of this CreateScriptAssignment.  # noqa: E501


        :return: The deployment_mode of this CreateScriptAssignment.  # noqa: E501
        :rtype: int
        """
        return self._deployment_mode

    @deployment_mode.setter
    def deployment_mode(self, deployment_mode):
        """Sets the deployment_mode of this CreateScriptAssignment.


        :param deployment_mode: The deployment_mode of this CreateScriptAssignment.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if (self._configuration.client_side_validation and
                deployment_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `deployment_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_mode, allowed_values)
            )

        self._deployment_mode = deployment_mode

    @property
    def memberships(self):
        """Gets the memberships of this CreateScriptAssignment.  # noqa: E501


        :return: The memberships of this CreateScriptAssignment.  # noqa: E501
        :rtype: list[SmartGroupData]
        """
        return self._memberships

    @memberships.setter
    def memberships(self, memberships):
        """Sets the memberships of this CreateScriptAssignment.


        :param memberships: The memberships of this CreateScriptAssignment.  # noqa: E501
        :type: list[SmartGroupData]
        """

        self._memberships = memberships

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
        if issubclass(CreateScriptAssignment, dict):
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
        if not isinstance(other, CreateScriptAssignment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateScriptAssignment):
            return True

        return self.to_dict() != other.to_dict()
