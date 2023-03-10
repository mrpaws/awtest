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


class DeviceWorkflowDefinitionBulkResponseV1Model(object):
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
        'workflow_uuid': 'str',
        'current_version': 'str',
        'name': 'str',
        'type': 'str',
        'applicability_rules': 'str',
        'payload': 'str',
        'deployment_mode': 'int',
        'organization_group_uuid': 'str'
    }

    attribute_map = {
        'workflow_uuid': 'workflow_uuid',
        'current_version': 'current_version',
        'name': 'name',
        'type': 'type',
        'applicability_rules': 'applicability_rules',
        'payload': 'payload',
        'deployment_mode': 'deployment_mode',
        'organization_group_uuid': 'organization_group_uuid'
    }

    def __init__(self, workflow_uuid=None, current_version=None, name=None, type=None, applicability_rules=None, payload=None, deployment_mode=None, organization_group_uuid=None, _configuration=None):  # noqa: E501
        """DeviceWorkflowDefinitionBulkResponseV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._workflow_uuid = None
        self._current_version = None
        self._name = None
        self._type = None
        self._applicability_rules = None
        self._payload = None
        self._deployment_mode = None
        self._organization_group_uuid = None
        self.discriminator = None

        if workflow_uuid is not None:
            self.workflow_uuid = workflow_uuid
        if current_version is not None:
            self.current_version = current_version
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if applicability_rules is not None:
            self.applicability_rules = applicability_rules
        if payload is not None:
            self.payload = payload
        if deployment_mode is not None:
            self.deployment_mode = deployment_mode
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid

    @property
    def workflow_uuid(self):
        """Gets the workflow_uuid of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501


        :return: The workflow_uuid of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._workflow_uuid

    @workflow_uuid.setter
    def workflow_uuid(self, workflow_uuid):
        """Sets the workflow_uuid of this DeviceWorkflowDefinitionBulkResponseV1Model.


        :param workflow_uuid: The workflow_uuid of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :type: str
        """

        self._workflow_uuid = workflow_uuid

    @property
    def current_version(self):
        """Gets the current_version of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501


        :return: The current_version of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this DeviceWorkflowDefinitionBulkResponseV1Model.


        :param current_version: The current_version of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :type: str
        """

        self._current_version = current_version

    @property
    def name(self):
        """Gets the name of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501


        :return: The name of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceWorkflowDefinitionBulkResponseV1Model.


        :param name: The name of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501


        :return: The type of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceWorkflowDefinitionBulkResponseV1Model.


        :param type: The type of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def applicability_rules(self):
        """Gets the applicability_rules of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501


        :return: The applicability_rules of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._applicability_rules

    @applicability_rules.setter
    def applicability_rules(self, applicability_rules):
        """Sets the applicability_rules of this DeviceWorkflowDefinitionBulkResponseV1Model.


        :param applicability_rules: The applicability_rules of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :type: str
        """

        self._applicability_rules = applicability_rules

    @property
    def payload(self):
        """Gets the payload of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501


        :return: The payload of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this DeviceWorkflowDefinitionBulkResponseV1Model.


        :param payload: The payload of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def deployment_mode(self):
        """Gets the deployment_mode of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501


        :return: The deployment_mode of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :rtype: int
        """
        return self._deployment_mode

    @deployment_mode.setter
    def deployment_mode(self, deployment_mode):
        """Sets the deployment_mode of this DeviceWorkflowDefinitionBulkResponseV1Model.


        :param deployment_mode: The deployment_mode of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
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
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501


        :return: The organization_group_uuid of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this DeviceWorkflowDefinitionBulkResponseV1Model.


        :param organization_group_uuid: The organization_group_uuid of this DeviceWorkflowDefinitionBulkResponseV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

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
        if issubclass(DeviceWorkflowDefinitionBulkResponseV1Model, dict):
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
        if not isinstance(other, DeviceWorkflowDefinitionBulkResponseV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceWorkflowDefinitionBulkResponseV1Model):
            return True

        return self.to_dict() != other.to_dict()
