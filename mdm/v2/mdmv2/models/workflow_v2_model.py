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


class WorkflowV2Model(object):
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
        'organization_group_uuid': 'str',
        'applicability_rules': 'str',
        'payload': 'WorkflowPayloadModel',
        'type': 'str',
        'device_type': 'int',
        'structured_payload_version': 'int',
        'catalog_display': 'CatalogDisplayInfo',
        'implicit_workflow': 'bool',
        'change_log_description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'organization_group_uuid': 'organization_group_uuid',
        'applicability_rules': 'applicability_rules',
        'payload': 'payload',
        'type': 'type',
        'device_type': 'device_type',
        'structured_payload_version': 'structured_payload_version',
        'catalog_display': 'catalog_display',
        'implicit_workflow': 'implicit_workflow',
        'change_log_description': 'change_log_description'
    }

    def __init__(self, name=None, description=None, organization_group_uuid=None, applicability_rules=None, payload=None, type=None, device_type=None, structured_payload_version=None, catalog_display=None, implicit_workflow=None, change_log_description=None, _configuration=None):  # noqa: E501
        """WorkflowV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._organization_group_uuid = None
        self._applicability_rules = None
        self._payload = None
        self._type = None
        self._device_type = None
        self._structured_payload_version = None
        self._catalog_display = None
        self._implicit_workflow = None
        self._change_log_description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if applicability_rules is not None:
            self.applicability_rules = applicability_rules
        if payload is not None:
            self.payload = payload
        if type is not None:
            self.type = type
        if device_type is not None:
            self.device_type = device_type
        if structured_payload_version is not None:
            self.structured_payload_version = structured_payload_version
        if catalog_display is not None:
            self.catalog_display = catalog_display
        if implicit_workflow is not None:
            self.implicit_workflow = implicit_workflow
        if change_log_description is not None:
            self.change_log_description = change_log_description

    @property
    def name(self):
        """Gets the name of this WorkflowV2Model.  # noqa: E501


        :return: The name of this WorkflowV2Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowV2Model.


        :param name: The name of this WorkflowV2Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this WorkflowV2Model.  # noqa: E501


        :return: The description of this WorkflowV2Model.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowV2Model.


        :param description: The description of this WorkflowV2Model.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this WorkflowV2Model.  # noqa: E501


        :return: The organization_group_uuid of this WorkflowV2Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this WorkflowV2Model.


        :param organization_group_uuid: The organization_group_uuid of this WorkflowV2Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def applicability_rules(self):
        """Gets the applicability_rules of this WorkflowV2Model.  # noqa: E501


        :return: The applicability_rules of this WorkflowV2Model.  # noqa: E501
        :rtype: str
        """
        return self._applicability_rules

    @applicability_rules.setter
    def applicability_rules(self, applicability_rules):
        """Sets the applicability_rules of this WorkflowV2Model.


        :param applicability_rules: The applicability_rules of this WorkflowV2Model.  # noqa: E501
        :type: str
        """

        self._applicability_rules = applicability_rules

    @property
    def payload(self):
        """Gets the payload of this WorkflowV2Model.  # noqa: E501


        :return: The payload of this WorkflowV2Model.  # noqa: E501
        :rtype: WorkflowPayloadModel
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this WorkflowV2Model.


        :param payload: The payload of this WorkflowV2Model.  # noqa: E501
        :type: WorkflowPayloadModel
        """

        self._payload = payload

    @property
    def type(self):
        """Gets the type of this WorkflowV2Model.  # noqa: E501


        :return: The type of this WorkflowV2Model.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WorkflowV2Model.


        :param type: The type of this WorkflowV2Model.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def device_type(self):
        """Gets the device_type of this WorkflowV2Model.  # noqa: E501


        :return: The device_type of this WorkflowV2Model.  # noqa: E501
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this WorkflowV2Model.


        :param device_type: The device_type of this WorkflowV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 100, 101, 102, 103, 104, 105, 200, 201]  # noqa: E501
        if (self._configuration.client_side_validation and
                device_type not in allowed_values):
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def structured_payload_version(self):
        """Gets the structured_payload_version of this WorkflowV2Model.  # noqa: E501


        :return: The structured_payload_version of this WorkflowV2Model.  # noqa: E501
        :rtype: int
        """
        return self._structured_payload_version

    @structured_payload_version.setter
    def structured_payload_version(self, structured_payload_version):
        """Sets the structured_payload_version of this WorkflowV2Model.


        :param structured_payload_version: The structured_payload_version of this WorkflowV2Model.  # noqa: E501
        :type: int
        """

        self._structured_payload_version = structured_payload_version

    @property
    def catalog_display(self):
        """Gets the catalog_display of this WorkflowV2Model.  # noqa: E501


        :return: The catalog_display of this WorkflowV2Model.  # noqa: E501
        :rtype: CatalogDisplayInfo
        """
        return self._catalog_display

    @catalog_display.setter
    def catalog_display(self, catalog_display):
        """Sets the catalog_display of this WorkflowV2Model.


        :param catalog_display: The catalog_display of this WorkflowV2Model.  # noqa: E501
        :type: CatalogDisplayInfo
        """

        self._catalog_display = catalog_display

    @property
    def implicit_workflow(self):
        """Gets the implicit_workflow of this WorkflowV2Model.  # noqa: E501


        :return: The implicit_workflow of this WorkflowV2Model.  # noqa: E501
        :rtype: bool
        """
        return self._implicit_workflow

    @implicit_workflow.setter
    def implicit_workflow(self, implicit_workflow):
        """Sets the implicit_workflow of this WorkflowV2Model.


        :param implicit_workflow: The implicit_workflow of this WorkflowV2Model.  # noqa: E501
        :type: bool
        """

        self._implicit_workflow = implicit_workflow

    @property
    def change_log_description(self):
        """Gets the change_log_description of this WorkflowV2Model.  # noqa: E501


        :return: The change_log_description of this WorkflowV2Model.  # noqa: E501
        :rtype: str
        """
        return self._change_log_description

    @change_log_description.setter
    def change_log_description(self, change_log_description):
        """Sets the change_log_description of this WorkflowV2Model.


        :param change_log_description: The change_log_description of this WorkflowV2Model.  # noqa: E501
        :type: str
        """

        self._change_log_description = change_log_description

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
        if issubclass(WorkflowV2Model, dict):
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
        if not isinstance(other, WorkflowV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowV2Model):
            return True

        return self.to_dict() != other.to_dict()