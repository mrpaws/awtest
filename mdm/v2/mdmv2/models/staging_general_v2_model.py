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


class StagingGeneralV2Model(object):
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
        'staging_bundle_uuid': 'str',
        'name': 'str',
        'description': 'str',
        'organization_group_uuid': 'str',
        'organization_group_name': 'str',
        'enrollment_user_name': 'str',
        'password': 'str',
        'package_uuid': 'str',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'staging_bundle_uuid': 'staging_bundle_uuid',
        'name': 'name',
        'description': 'description',
        'organization_group_uuid': 'organization_group_uuid',
        'organization_group_name': 'organization_group_name',
        'enrollment_user_name': 'enrollment_user_name',
        'password': 'password',
        'package_uuid': 'package_uuid',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, staging_bundle_uuid=None, name=None, description=None, organization_group_uuid=None, organization_group_name=None, enrollment_user_name=None, password=None, package_uuid=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """StagingGeneralV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._staging_bundle_uuid = None
        self._name = None
        self._description = None
        self._organization_group_uuid = None
        self._organization_group_name = None
        self._enrollment_user_name = None
        self._password = None
        self._package_uuid = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if staging_bundle_uuid is not None:
            self.staging_bundle_uuid = staging_bundle_uuid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if organization_group_name is not None:
            self.organization_group_name = organization_group_name
        if enrollment_user_name is not None:
            self.enrollment_user_name = enrollment_user_name
        if password is not None:
            self.password = password
        if package_uuid is not None:
            self.package_uuid = package_uuid
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def staging_bundle_uuid(self):
        """Gets the staging_bundle_uuid of this StagingGeneralV2Model.  # noqa: E501

        uuid of the staging bundle  # noqa: E501

        :return: The staging_bundle_uuid of this StagingGeneralV2Model.  # noqa: E501
        :rtype: str
        """
        return self._staging_bundle_uuid

    @staging_bundle_uuid.setter
    def staging_bundle_uuid(self, staging_bundle_uuid):
        """Sets the staging_bundle_uuid of this StagingGeneralV2Model.

        uuid of the staging bundle  # noqa: E501

        :param staging_bundle_uuid: The staging_bundle_uuid of this StagingGeneralV2Model.  # noqa: E501
        :type: str
        """

        self._staging_bundle_uuid = staging_bundle_uuid

    @property
    def name(self):
        """Gets the name of this StagingGeneralV2Model.  # noqa: E501

        Name of the staging bundle.  # noqa: E501

        :return: The name of this StagingGeneralV2Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StagingGeneralV2Model.

        Name of the staging bundle.  # noqa: E501

        :param name: The name of this StagingGeneralV2Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this StagingGeneralV2Model.  # noqa: E501

        Description of the staging bundle.  # noqa: E501

        :return: The description of this StagingGeneralV2Model.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StagingGeneralV2Model.

        Description of the staging bundle.  # noqa: E501

        :param description: The description of this StagingGeneralV2Model.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this StagingGeneralV2Model.  # noqa: E501

        Uuid of the Organization Group where the staging  bundle is managed at.  # noqa: E501

        :return: The organization_group_uuid of this StagingGeneralV2Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this StagingGeneralV2Model.

        Uuid of the Organization Group where the staging  bundle is managed at.  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this StagingGeneralV2Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def organization_group_name(self):
        """Gets the organization_group_name of this StagingGeneralV2Model.  # noqa: E501

        Name of the Organization Group where the staging  bundle is manag  at.  # noqa: E501

        :return: The organization_group_name of this StagingGeneralV2Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_name

    @organization_group_name.setter
    def organization_group_name(self, organization_group_name):
        """Sets the organization_group_name of this StagingGeneralV2Model.

        Name of the Organization Group where the staging  bundle is manag  at.  # noqa: E501

        :param organization_group_name: The organization_group_name of this StagingGeneralV2Model.  # noqa: E501
        :type: str
        """

        self._organization_group_name = organization_group_name

    @property
    def enrollment_user_name(self):
        """Gets the enrollment_user_name of this StagingGeneralV2Model.  # noqa: E501

        Name of the User enrolled with the staging  bundle.  # noqa: E501

        :return: The enrollment_user_name of this StagingGeneralV2Model.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_user_name

    @enrollment_user_name.setter
    def enrollment_user_name(self, enrollment_user_name):
        """Sets the enrollment_user_name of this StagingGeneralV2Model.

        Name of the User enrolled with the staging  bundle.  # noqa: E501

        :param enrollment_user_name: The enrollment_user_name of this StagingGeneralV2Model.  # noqa: E501
        :type: str
        """

        self._enrollment_user_name = enrollment_user_name

    @property
    def password(self):
        """Gets the password of this StagingGeneralV2Model.  # noqa: E501

        Password of the User enrolled with the staging  bundle.  # noqa: E501

        :return: The password of this StagingGeneralV2Model.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this StagingGeneralV2Model.

        Password of the User enrolled with the staging  bundle.  # noqa: E501

        :param password: The password of this StagingGeneralV2Model.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def package_uuid(self):
        """Gets the package_uuid of this StagingGeneralV2Model.  # noqa: E501

        Unique identifier of the agent/hub package.  # noqa: E501

        :return: The package_uuid of this StagingGeneralV2Model.  # noqa: E501
        :rtype: str
        """
        return self._package_uuid

    @package_uuid.setter
    def package_uuid(self, package_uuid):
        """Sets the package_uuid of this StagingGeneralV2Model.

        Unique identifier of the agent/hub package.  # noqa: E501

        :param package_uuid: The package_uuid of this StagingGeneralV2Model.  # noqa: E501
        :type: str
        """

        self._package_uuid = package_uuid

    @property
    def id(self):
        """Gets the id of this StagingGeneralV2Model.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this StagingGeneralV2Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StagingGeneralV2Model.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this StagingGeneralV2Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this StagingGeneralV2Model.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this StagingGeneralV2Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this StagingGeneralV2Model.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this StagingGeneralV2Model.  # noqa: E501
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
        if issubclass(StagingGeneralV2Model, dict):
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
        if not isinstance(other, StagingGeneralV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagingGeneralV2Model):
            return True

        return self.to_dict() != other.to_dict()