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


class AssignmentGroupsV1Model(object):
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
        'assignment_group_id': 'int',
        'name': 'str',
        'assignment_group_type': 'str',
        'smart_group_uuid': 'str',
        'user_group_uuid': 'str',
        'organization_group_uuid': 'str',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'assignment_group_id': 'assignmentGroupId',
        'name': 'name',
        'assignment_group_type': 'assignmentGroupType',
        'smart_group_uuid': 'smartGroupUuid',
        'user_group_uuid': 'userGroupUuid',
        'organization_group_uuid': 'organizationGroupUuid',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, assignment_group_id=None, name=None, assignment_group_type=None, smart_group_uuid=None, user_group_uuid=None, organization_group_uuid=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """AssignmentGroupsV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assignment_group_id = None
        self._name = None
        self._assignment_group_type = None
        self._smart_group_uuid = None
        self._user_group_uuid = None
        self._organization_group_uuid = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if assignment_group_id is not None:
            self.assignment_group_id = assignment_group_id
        if name is not None:
            self.name = name
        if assignment_group_type is not None:
            self.assignment_group_type = assignment_group_type
        if smart_group_uuid is not None:
            self.smart_group_uuid = smart_group_uuid
        if user_group_uuid is not None:
            self.user_group_uuid = user_group_uuid
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def assignment_group_id(self):
        """Gets the assignment_group_id of this AssignmentGroupsV1Model.  # noqa: E501

        Unique Identifier for an AssignmentGroup  # noqa: E501

        :return: The assignment_group_id of this AssignmentGroupsV1Model.  # noqa: E501
        :rtype: int
        """
        return self._assignment_group_id

    @assignment_group_id.setter
    def assignment_group_id(self, assignment_group_id):
        """Sets the assignment_group_id of this AssignmentGroupsV1Model.

        Unique Identifier for an AssignmentGroup  # noqa: E501

        :param assignment_group_id: The assignment_group_id of this AssignmentGroupsV1Model.  # noqa: E501
        :type: int
        """

        self._assignment_group_id = assignment_group_id

    @property
    def name(self):
        """Gets the name of this AssignmentGroupsV1Model.  # noqa: E501

        Name of an AssignmentGroup  # noqa: E501

        :return: The name of this AssignmentGroupsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssignmentGroupsV1Model.

        Name of an AssignmentGroup  # noqa: E501

        :param name: The name of this AssignmentGroupsV1Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def assignment_group_type(self):
        """Gets the assignment_group_type of this AssignmentGroupsV1Model.  # noqa: E501

        Type of AssignmentGroup  # noqa: E501

        :return: The assignment_group_type of this AssignmentGroupsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._assignment_group_type

    @assignment_group_type.setter
    def assignment_group_type(self, assignment_group_type):
        """Sets the assignment_group_type of this AssignmentGroupsV1Model.

        Type of AssignmentGroup  # noqa: E501

        :param assignment_group_type: The assignment_group_type of this AssignmentGroupsV1Model.  # noqa: E501
        :type: str
        """

        self._assignment_group_type = assignment_group_type

    @property
    def smart_group_uuid(self):
        """Gets the smart_group_uuid of this AssignmentGroupsV1Model.  # noqa: E501

        The unique identifier (UUID) of the SmartGroup  # noqa: E501

        :return: The smart_group_uuid of this AssignmentGroupsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._smart_group_uuid

    @smart_group_uuid.setter
    def smart_group_uuid(self, smart_group_uuid):
        """Sets the smart_group_uuid of this AssignmentGroupsV1Model.

        The unique identifier (UUID) of the SmartGroup  # noqa: E501

        :param smart_group_uuid: The smart_group_uuid of this AssignmentGroupsV1Model.  # noqa: E501
        :type: str
        """

        self._smart_group_uuid = smart_group_uuid

    @property
    def user_group_uuid(self):
        """Gets the user_group_uuid of this AssignmentGroupsV1Model.  # noqa: E501

        The unique identifier (UUID) of the UserGroup  # noqa: E501

        :return: The user_group_uuid of this AssignmentGroupsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._user_group_uuid

    @user_group_uuid.setter
    def user_group_uuid(self, user_group_uuid):
        """Sets the user_group_uuid of this AssignmentGroupsV1Model.

        The unique identifier (UUID) of the UserGroup  # noqa: E501

        :param user_group_uuid: The user_group_uuid of this AssignmentGroupsV1Model.  # noqa: E501
        :type: str
        """

        self._user_group_uuid = user_group_uuid

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this AssignmentGroupsV1Model.  # noqa: E501

        The unique identifier (UUID) of the OrganizationGroup  # noqa: E501

        :return: The organization_group_uuid of this AssignmentGroupsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this AssignmentGroupsV1Model.

        The unique identifier (UUID) of the OrganizationGroup  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this AssignmentGroupsV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def id(self):
        """Gets the id of this AssignmentGroupsV1Model.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this AssignmentGroupsV1Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssignmentGroupsV1Model.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this AssignmentGroupsV1Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this AssignmentGroupsV1Model.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this AssignmentGroupsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this AssignmentGroupsV1Model.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this AssignmentGroupsV1Model.  # noqa: E501
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
        if issubclass(AssignmentGroupsV1Model, dict):
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
        if not isinstance(other, AssignmentGroupsV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssignmentGroupsV1Model):
            return True

        return self.to_dict() != other.to_dict()
