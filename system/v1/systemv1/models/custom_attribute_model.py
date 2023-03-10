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


class CustomAttributeModel(object):
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
        'id': 'int',
        'application_group': 'str',
        'collect_values_for_rule_creator': 'bool',
        'description': 'str',
        'managed_by_organization_group_id': 'str',
        'name': 'str',
        'persist': 'bool',
        'show_in_rule_creator': 'bool',
        'use_as_lookup_value': 'bool',
        'values': 'list[CustomAttributeValueModel_]',
        'uuid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'application_group': 'ApplicationGroup',
        'collect_values_for_rule_creator': 'CollectValuesForRuleCreator',
        'description': 'Description',
        'managed_by_organization_group_id': 'ManagedByOrganizationGroupID',
        'name': 'Name',
        'persist': 'Persist',
        'show_in_rule_creator': 'ShowInRuleCreator',
        'use_as_lookup_value': 'UseAsLookupValue',
        'values': 'Values',
        'uuid': 'uuid'
    }

    def __init__(self, id=None, application_group=None, collect_values_for_rule_creator=None, description=None, managed_by_organization_group_id=None, name=None, persist=None, show_in_rule_creator=None, use_as_lookup_value=None, values=None, uuid=None, _configuration=None):  # noqa: E501
        """CustomAttributeModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._application_group = None
        self._collect_values_for_rule_creator = None
        self._description = None
        self._managed_by_organization_group_id = None
        self._name = None
        self._persist = None
        self._show_in_rule_creator = None
        self._use_as_lookup_value = None
        self._values = None
        self._uuid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if application_group is not None:
            self.application_group = application_group
        if collect_values_for_rule_creator is not None:
            self.collect_values_for_rule_creator = collect_values_for_rule_creator
        if description is not None:
            self.description = description
        if managed_by_organization_group_id is not None:
            self.managed_by_organization_group_id = managed_by_organization_group_id
        if name is not None:
            self.name = name
        if persist is not None:
            self.persist = persist
        if show_in_rule_creator is not None:
            self.show_in_rule_creator = show_in_rule_creator
        if use_as_lookup_value is not None:
            self.use_as_lookup_value = use_as_lookup_value
        if values is not None:
            self.values = values
        if uuid is not None:
            self.uuid = uuid

    @property
    def id(self):
        """Gets the id of this CustomAttributeModel.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this CustomAttributeModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomAttributeModel.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this CustomAttributeModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def application_group(self):
        """Gets the application_group of this CustomAttributeModel.  # noqa: E501

        Gets or sets application Group to which Custom Attribute applicable to.  # noqa: E501

        :return: The application_group of this CustomAttributeModel.  # noqa: E501
        :rtype: str
        """
        return self._application_group

    @application_group.setter
    def application_group(self, application_group):
        """Sets the application_group of this CustomAttributeModel.

        Gets or sets application Group to which Custom Attribute applicable to.  # noqa: E501

        :param application_group: The application_group of this CustomAttributeModel.  # noqa: E501
        :type: str
        """

        self._application_group = application_group

    @property
    def collect_values_for_rule_creator(self):
        """Gets the collect_values_for_rule_creator of this CustomAttributeModel.  # noqa: E501

        Gets or sets a value indicating whether flag to indicate whether value should be collected for rule generator.  # noqa: E501

        :return: The collect_values_for_rule_creator of this CustomAttributeModel.  # noqa: E501
        :rtype: bool
        """
        return self._collect_values_for_rule_creator

    @collect_values_for_rule_creator.setter
    def collect_values_for_rule_creator(self, collect_values_for_rule_creator):
        """Sets the collect_values_for_rule_creator of this CustomAttributeModel.

        Gets or sets a value indicating whether flag to indicate whether value should be collected for rule generator.  # noqa: E501

        :param collect_values_for_rule_creator: The collect_values_for_rule_creator of this CustomAttributeModel.  # noqa: E501
        :type: bool
        """

        self._collect_values_for_rule_creator = collect_values_for_rule_creator

    @property
    def description(self):
        """Gets the description of this CustomAttributeModel.  # noqa: E501

        Gets or sets custom Attribute Description.  # noqa: E501

        :return: The description of this CustomAttributeModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomAttributeModel.

        Gets or sets custom Attribute Description.  # noqa: E501

        :param description: The description of this CustomAttributeModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def managed_by_organization_group_id(self):
        """Gets the managed_by_organization_group_id of this CustomAttributeModel.  # noqa: E501

        Gets or sets managed By Organization Group Identifier[Customer Organization Group Type].  # noqa: E501

        :return: The managed_by_organization_group_id of this CustomAttributeModel.  # noqa: E501
        :rtype: str
        """
        return self._managed_by_organization_group_id

    @managed_by_organization_group_id.setter
    def managed_by_organization_group_id(self, managed_by_organization_group_id):
        """Sets the managed_by_organization_group_id of this CustomAttributeModel.

        Gets or sets managed By Organization Group Identifier[Customer Organization Group Type].  # noqa: E501

        :param managed_by_organization_group_id: The managed_by_organization_group_id of this CustomAttributeModel.  # noqa: E501
        :type: str
        """

        self._managed_by_organization_group_id = managed_by_organization_group_id

    @property
    def name(self):
        """Gets the name of this CustomAttributeModel.  # noqa: E501

        Gets or sets custom Attrbute Name.  # noqa: E501

        :return: The name of this CustomAttributeModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomAttributeModel.

        Gets or sets custom Attrbute Name.  # noqa: E501

        :param name: The name of this CustomAttributeModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def persist(self):
        """Gets the persist of this CustomAttributeModel.  # noqa: E501

        Gets or sets a value indicating whether flag to indicate value should be persisted or not.  # noqa: E501

        :return: The persist of this CustomAttributeModel.  # noqa: E501
        :rtype: bool
        """
        return self._persist

    @persist.setter
    def persist(self, persist):
        """Sets the persist of this CustomAttributeModel.

        Gets or sets a value indicating whether flag to indicate value should be persisted or not.  # noqa: E501

        :param persist: The persist of this CustomAttributeModel.  # noqa: E501
        :type: bool
        """

        self._persist = persist

    @property
    def show_in_rule_creator(self):
        """Gets the show_in_rule_creator of this CustomAttributeModel.  # noqa: E501

        Gets or sets a value indicating whether flag to indicate whether it should be shown in Rule Generator.  # noqa: E501

        :return: The show_in_rule_creator of this CustomAttributeModel.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_rule_creator

    @show_in_rule_creator.setter
    def show_in_rule_creator(self, show_in_rule_creator):
        """Sets the show_in_rule_creator of this CustomAttributeModel.

        Gets or sets a value indicating whether flag to indicate whether it should be shown in Rule Generator.  # noqa: E501

        :param show_in_rule_creator: The show_in_rule_creator of this CustomAttributeModel.  # noqa: E501
        :type: bool
        """

        self._show_in_rule_creator = show_in_rule_creator

    @property
    def use_as_lookup_value(self):
        """Gets the use_as_lookup_value of this CustomAttributeModel.  # noqa: E501

        Gets or sets a value indicating whether flag to indicate whether Custom Attribute can be used as lookup or not.  # noqa: E501

        :return: The use_as_lookup_value of this CustomAttributeModel.  # noqa: E501
        :rtype: bool
        """
        return self._use_as_lookup_value

    @use_as_lookup_value.setter
    def use_as_lookup_value(self, use_as_lookup_value):
        """Sets the use_as_lookup_value of this CustomAttributeModel.

        Gets or sets a value indicating whether flag to indicate whether Custom Attribute can be used as lookup or not.  # noqa: E501

        :param use_as_lookup_value: The use_as_lookup_value of this CustomAttributeModel.  # noqa: E501
        :type: bool
        """

        self._use_as_lookup_value = use_as_lookup_value

    @property
    def values(self):
        """Gets the values of this CustomAttributeModel.  # noqa: E501

        Gets or sets the domains.  # noqa: E501

        :return: The values of this CustomAttributeModel.  # noqa: E501
        :rtype: list[CustomAttributeValueModel_]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this CustomAttributeModel.

        Gets or sets the domains.  # noqa: E501

        :param values: The values of this CustomAttributeModel.  # noqa: E501
        :type: list[CustomAttributeValueModel_]
        """

        self._values = values

    @property
    def uuid(self):
        """Gets the uuid of this CustomAttributeModel.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this CustomAttributeModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this CustomAttributeModel.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this CustomAttributeModel.  # noqa: E501
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
        if issubclass(CustomAttributeModel, dict):
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
        if not isinstance(other, CustomAttributeModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomAttributeModel):
            return True

        return self.to_dict() != other.to_dict()
