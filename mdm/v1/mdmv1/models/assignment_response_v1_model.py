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


class AssignmentResponseV1Model(object):
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
        'workflow_uuid': 'str',
        'organization_group_uuid': 'str',
        'name': 'str',
        'description': 'str',
        'deployment_mode': 'int',
        'show_in_catalog': 'bool',
        'priority': 'int',
        'assigned_smartgroup_uuids': 'list[str]',
        'created_on': 'datetime',
        'modified_on': 'datetime',
        'published_on': 'datetime',
        'workflow_assignment_state': 'int',
        'config_bundle_uuid': 'str'
    }

    attribute_map = {
        'assignment_uuid': 'assignment_uuid',
        'workflow_uuid': 'workflow_uuid',
        'organization_group_uuid': 'organization_group_uuid',
        'name': 'name',
        'description': 'description',
        'deployment_mode': 'deployment_mode',
        'show_in_catalog': 'show_in_catalog',
        'priority': 'priority',
        'assigned_smartgroup_uuids': 'assigned_smartgroup_uuids',
        'created_on': 'created_on',
        'modified_on': 'modified_on',
        'published_on': 'published_on',
        'workflow_assignment_state': 'workflow_assignment_state',
        'config_bundle_uuid': 'config_bundle_uuid'
    }

    def __init__(self, assignment_uuid=None, workflow_uuid=None, organization_group_uuid=None, name=None, description=None, deployment_mode=None, show_in_catalog=None, priority=None, assigned_smartgroup_uuids=None, created_on=None, modified_on=None, published_on=None, workflow_assignment_state=None, config_bundle_uuid=None, _configuration=None):  # noqa: E501
        """AssignmentResponseV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assignment_uuid = None
        self._workflow_uuid = None
        self._organization_group_uuid = None
        self._name = None
        self._description = None
        self._deployment_mode = None
        self._show_in_catalog = None
        self._priority = None
        self._assigned_smartgroup_uuids = None
        self._created_on = None
        self._modified_on = None
        self._published_on = None
        self._workflow_assignment_state = None
        self._config_bundle_uuid = None
        self.discriminator = None

        if assignment_uuid is not None:
            self.assignment_uuid = assignment_uuid
        if workflow_uuid is not None:
            self.workflow_uuid = workflow_uuid
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if deployment_mode is not None:
            self.deployment_mode = deployment_mode
        if show_in_catalog is not None:
            self.show_in_catalog = show_in_catalog
        if priority is not None:
            self.priority = priority
        if assigned_smartgroup_uuids is not None:
            self.assigned_smartgroup_uuids = assigned_smartgroup_uuids
        if created_on is not None:
            self.created_on = created_on
        if modified_on is not None:
            self.modified_on = modified_on
        if published_on is not None:
            self.published_on = published_on
        if workflow_assignment_state is not None:
            self.workflow_assignment_state = workflow_assignment_state
        if config_bundle_uuid is not None:
            self.config_bundle_uuid = config_bundle_uuid

    @property
    def assignment_uuid(self):
        """Gets the assignment_uuid of this AssignmentResponseV1Model.  # noqa: E501


        :return: The assignment_uuid of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._assignment_uuid

    @assignment_uuid.setter
    def assignment_uuid(self, assignment_uuid):
        """Sets the assignment_uuid of this AssignmentResponseV1Model.


        :param assignment_uuid: The assignment_uuid of this AssignmentResponseV1Model.  # noqa: E501
        :type: str
        """

        self._assignment_uuid = assignment_uuid

    @property
    def workflow_uuid(self):
        """Gets the workflow_uuid of this AssignmentResponseV1Model.  # noqa: E501


        :return: The workflow_uuid of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._workflow_uuid

    @workflow_uuid.setter
    def workflow_uuid(self, workflow_uuid):
        """Sets the workflow_uuid of this AssignmentResponseV1Model.


        :param workflow_uuid: The workflow_uuid of this AssignmentResponseV1Model.  # noqa: E501
        :type: str
        """

        self._workflow_uuid = workflow_uuid

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this AssignmentResponseV1Model.  # noqa: E501


        :return: The organization_group_uuid of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this AssignmentResponseV1Model.


        :param organization_group_uuid: The organization_group_uuid of this AssignmentResponseV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def name(self):
        """Gets the name of this AssignmentResponseV1Model.  # noqa: E501


        :return: The name of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssignmentResponseV1Model.


        :param name: The name of this AssignmentResponseV1Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AssignmentResponseV1Model.  # noqa: E501


        :return: The description of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssignmentResponseV1Model.


        :param description: The description of this AssignmentResponseV1Model.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def deployment_mode(self):
        """Gets the deployment_mode of this AssignmentResponseV1Model.  # noqa: E501


        :return: The deployment_mode of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._deployment_mode

    @deployment_mode.setter
    def deployment_mode(self, deployment_mode):
        """Sets the deployment_mode of this AssignmentResponseV1Model.


        :param deployment_mode: The deployment_mode of this AssignmentResponseV1Model.  # noqa: E501
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
    def show_in_catalog(self):
        """Gets the show_in_catalog of this AssignmentResponseV1Model.  # noqa: E501


        :return: The show_in_catalog of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_catalog

    @show_in_catalog.setter
    def show_in_catalog(self, show_in_catalog):
        """Sets the show_in_catalog of this AssignmentResponseV1Model.


        :param show_in_catalog: The show_in_catalog of this AssignmentResponseV1Model.  # noqa: E501
        :type: bool
        """

        self._show_in_catalog = show_in_catalog

    @property
    def priority(self):
        """Gets the priority of this AssignmentResponseV1Model.  # noqa: E501


        :return: The priority of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this AssignmentResponseV1Model.


        :param priority: The priority of this AssignmentResponseV1Model.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def assigned_smartgroup_uuids(self):
        """Gets the assigned_smartgroup_uuids of this AssignmentResponseV1Model.  # noqa: E501


        :return: The assigned_smartgroup_uuids of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._assigned_smartgroup_uuids

    @assigned_smartgroup_uuids.setter
    def assigned_smartgroup_uuids(self, assigned_smartgroup_uuids):
        """Sets the assigned_smartgroup_uuids of this AssignmentResponseV1Model.


        :param assigned_smartgroup_uuids: The assigned_smartgroup_uuids of this AssignmentResponseV1Model.  # noqa: E501
        :type: list[str]
        """

        self._assigned_smartgroup_uuids = assigned_smartgroup_uuids

    @property
    def created_on(self):
        """Gets the created_on of this AssignmentResponseV1Model.  # noqa: E501


        :return: The created_on of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this AssignmentResponseV1Model.


        :param created_on: The created_on of this AssignmentResponseV1Model.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def modified_on(self):
        """Gets the modified_on of this AssignmentResponseV1Model.  # noqa: E501


        :return: The modified_on of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this AssignmentResponseV1Model.


        :param modified_on: The modified_on of this AssignmentResponseV1Model.  # noqa: E501
        :type: datetime
        """

        self._modified_on = modified_on

    @property
    def published_on(self):
        """Gets the published_on of this AssignmentResponseV1Model.  # noqa: E501


        :return: The published_on of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: datetime
        """
        return self._published_on

    @published_on.setter
    def published_on(self, published_on):
        """Sets the published_on of this AssignmentResponseV1Model.


        :param published_on: The published_on of this AssignmentResponseV1Model.  # noqa: E501
        :type: datetime
        """

        self._published_on = published_on

    @property
    def workflow_assignment_state(self):
        """Gets the workflow_assignment_state of this AssignmentResponseV1Model.  # noqa: E501


        :return: The workflow_assignment_state of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._workflow_assignment_state

    @workflow_assignment_state.setter
    def workflow_assignment_state(self, workflow_assignment_state):
        """Sets the workflow_assignment_state of this AssignmentResponseV1Model.


        :param workflow_assignment_state: The workflow_assignment_state of this AssignmentResponseV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6]  # noqa: E501
        if (self._configuration.client_side_validation and
                workflow_assignment_state not in allowed_values):
            raise ValueError(
                "Invalid value for `workflow_assignment_state` ({0}), must be one of {1}"  # noqa: E501
                .format(workflow_assignment_state, allowed_values)
            )

        self._workflow_assignment_state = workflow_assignment_state

    @property
    def config_bundle_uuid(self):
        """Gets the config_bundle_uuid of this AssignmentResponseV1Model.  # noqa: E501


        :return: The config_bundle_uuid of this AssignmentResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._config_bundle_uuid

    @config_bundle_uuid.setter
    def config_bundle_uuid(self, config_bundle_uuid):
        """Sets the config_bundle_uuid of this AssignmentResponseV1Model.


        :param config_bundle_uuid: The config_bundle_uuid of this AssignmentResponseV1Model.  # noqa: E501
        :type: str
        """

        self._config_bundle_uuid = config_bundle_uuid

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
        if issubclass(AssignmentResponseV1Model, dict):
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
        if not isinstance(other, AssignmentResponseV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssignmentResponseV1Model):
            return True

        return self.to_dict() != other.to_dict()
