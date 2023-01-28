# coding: utf-8

"""
    System API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv2.configuration import Configuration


class GroupResponse(object):
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
        'id': 'str',
        'external_id': 'str',
        'display_name': 'str',
        'schemas': 'list[str]',
        'urnscimschemasextensionworkspace1_0_group': 'GroupExtensions',
        'members': 'list[UserSummary]',
        'meta': 'Metadata'
    }

    attribute_map = {
        'id': 'id',
        'external_id': 'externalId',
        'display_name': 'displayName',
        'schemas': 'schemas',
        'urnscimschemasextensionworkspace1_0_group': 'urn:scim:schemas:extension:workspace:1.0:Group',
        'members': 'members',
        'meta': 'meta'
    }

    def __init__(self, id=None, external_id=None, display_name=None, schemas=None, urnscimschemasextensionworkspace1_0_group=None, members=None, meta=None, _configuration=None):  # noqa: E501
        """GroupResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._external_id = None
        self._display_name = None
        self._schemas = None
        self._urnscimschemasextensionworkspace1_0_group = None
        self._members = None
        self._meta = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if external_id is not None:
            self.external_id = external_id
        self.display_name = display_name
        self.schemas = schemas
        if urnscimschemasextensionworkspace1_0_group is not None:
            self.urnscimschemasextensionworkspace1_0_group = urnscimschemasextensionworkspace1_0_group
        if members is not None:
            self.members = members
        if meta is not None:
            self.meta = meta

    @property
    def id(self):
        """Gets the id of this GroupResponse.  # noqa: E501

        Unique identifier for a group.  # noqa: E501

        :return: The id of this GroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupResponse.

        Unique identifier for a group.  # noqa: E501

        :param id: The id of this GroupResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def external_id(self):
        """Gets the external_id of this GroupResponse.  # noqa: E501

        An identifier for the resource as defined by the provisioning client.    The \"externalId\" may simplify identification of a resource between the provisioning client   and the service provider by allowing the client to use a filter to locate the resource with   an identifier from the provisioning domain, obviating the need to store a local mapping   between the provisioning domain's identifier of the resource and the identifier used by the   service provider.  Each resource MAY include a non-empty \"externalId\" value.  # noqa: E501

        :return: The external_id of this GroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this GroupResponse.

        An identifier for the resource as defined by the provisioning client.    The \"externalId\" may simplify identification of a resource between the provisioning client   and the service provider by allowing the client to use a filter to locate the resource with   an identifier from the provisioning domain, obviating the need to store a local mapping   between the provisioning domain's identifier of the resource and the identifier used by the   service provider.  Each resource MAY include a non-empty \"externalId\" value.  # noqa: E501

        :param external_id: The external_id of this GroupResponse.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def display_name(self):
        """Gets the display_name of this GroupResponse.  # noqa: E501

        Name of the group.  # noqa: E501

        :return: The display_name of this GroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GroupResponse.

        Name of the group.  # noqa: E501

        :param display_name: The display_name of this GroupResponse.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def schemas(self):
        """Gets the schemas of this GroupResponse.  # noqa: E501

        Schemas used to compose a group entity.  # noqa: E501

        :return: The schemas of this GroupResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this GroupResponse.

        Schemas used to compose a group entity.  # noqa: E501

        :param schemas: The schemas of this GroupResponse.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and schemas is None:
            raise ValueError("Invalid value for `schemas`, must not be `None`")  # noqa: E501

        self._schemas = schemas

    @property
    def urnscimschemasextensionworkspace1_0_group(self):
        """Gets the urnscimschemasextensionworkspace1_0_group of this GroupResponse.  # noqa: E501

        Extension to group schema.  # noqa: E501

        :return: The urnscimschemasextensionworkspace1_0_group of this GroupResponse.  # noqa: E501
        :rtype: GroupExtensions
        """
        return self._urnscimschemasextensionworkspace1_0_group

    @urnscimschemasextensionworkspace1_0_group.setter
    def urnscimschemasextensionworkspace1_0_group(self, urnscimschemasextensionworkspace1_0_group):
        """Sets the urnscimschemasextensionworkspace1_0_group of this GroupResponse.

        Extension to group schema.  # noqa: E501

        :param urnscimschemasextensionworkspace1_0_group: The urnscimschemasextensionworkspace1_0_group of this GroupResponse.  # noqa: E501
        :type: GroupExtensions
        """

        self._urnscimschemasextensionworkspace1_0_group = urnscimschemasextensionworkspace1_0_group

    @property
    def members(self):
        """Gets the members of this GroupResponse.  # noqa: E501

        A list of users that belong to the group.  # noqa: E501

        :return: The members of this GroupResponse.  # noqa: E501
        :rtype: list[UserSummary]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this GroupResponse.

        A list of users that belong to the group.  # noqa: E501

        :param members: The members of this GroupResponse.  # noqa: E501
        :type: list[UserSummary]
        """

        self._members = members

    @property
    def meta(self):
        """Gets the meta of this GroupResponse.  # noqa: E501

        Metadata of resource.  # noqa: E501

        :return: The meta of this GroupResponse.  # noqa: E501
        :rtype: Metadata
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this GroupResponse.

        Metadata of resource.  # noqa: E501

        :param meta: The meta of this GroupResponse.  # noqa: E501
        :type: Metadata
        """

        self._meta = meta

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
        if issubclass(GroupResponse, dict):
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
        if not isinstance(other, GroupResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupResponse):
            return True

        return self.to_dict() != other.to_dict()