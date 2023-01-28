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


class StagingBundleDetailsModel(object):
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
        'staging_uuid': 'str',
        'name': 'str',
        'device_platform_name': 'str',
        'enrollment_user_name': 'str',
        'organization_group_uuid': 'str',
        'organization_group_name': 'str',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'staging_uuid': 'StagingUuid',
        'name': 'Name',
        'device_platform_name': 'DevicePlatformName',
        'enrollment_user_name': 'EnrollmentUserName',
        'organization_group_uuid': 'OrganizationGroupUuid',
        'organization_group_name': 'OrganizationGroupName',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, staging_uuid=None, name=None, device_platform_name=None, enrollment_user_name=None, organization_group_uuid=None, organization_group_name=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """StagingBundleDetailsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._staging_uuid = None
        self._name = None
        self._device_platform_name = None
        self._enrollment_user_name = None
        self._organization_group_uuid = None
        self._organization_group_name = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if staging_uuid is not None:
            self.staging_uuid = staging_uuid
        if name is not None:
            self.name = name
        if device_platform_name is not None:
            self.device_platform_name = device_platform_name
        if enrollment_user_name is not None:
            self.enrollment_user_name = enrollment_user_name
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if organization_group_name is not None:
            self.organization_group_name = organization_group_name
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def staging_uuid(self):
        """Gets the staging_uuid of this StagingBundleDetailsModel.  # noqa: E501

        Unique identifier of the staging bundle.  # noqa: E501

        :return: The staging_uuid of this StagingBundleDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._staging_uuid

    @staging_uuid.setter
    def staging_uuid(self, staging_uuid):
        """Sets the staging_uuid of this StagingBundleDetailsModel.

        Unique identifier of the staging bundle.  # noqa: E501

        :param staging_uuid: The staging_uuid of this StagingBundleDetailsModel.  # noqa: E501
        :type: str
        """

        self._staging_uuid = staging_uuid

    @property
    def name(self):
        """Gets the name of this StagingBundleDetailsModel.  # noqa: E501

        Name of the staging bundle.  # noqa: E501

        :return: The name of this StagingBundleDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StagingBundleDetailsModel.

        Name of the staging bundle.  # noqa: E501

        :param name: The name of this StagingBundleDetailsModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def device_platform_name(self):
        """Gets the device_platform_name of this StagingBundleDetailsModel.  # noqa: E501

        Name of the device platform that the staging bundle is applicable to.  # noqa: E501

        :return: The device_platform_name of this StagingBundleDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._device_platform_name

    @device_platform_name.setter
    def device_platform_name(self, device_platform_name):
        """Sets the device_platform_name of this StagingBundleDetailsModel.

        Name of the device platform that the staging bundle is applicable to.  # noqa: E501

        :param device_platform_name: The device_platform_name of this StagingBundleDetailsModel.  # noqa: E501
        :type: str
        """

        self._device_platform_name = device_platform_name

    @property
    def enrollment_user_name(self):
        """Gets the enrollment_user_name of this StagingBundleDetailsModel.  # noqa: E501

        Name of the Enrollment User of the Staging bundle.  # noqa: E501

        :return: The enrollment_user_name of this StagingBundleDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_user_name

    @enrollment_user_name.setter
    def enrollment_user_name(self, enrollment_user_name):
        """Sets the enrollment_user_name of this StagingBundleDetailsModel.

        Name of the Enrollment User of the Staging bundle.  # noqa: E501

        :param enrollment_user_name: The enrollment_user_name of this StagingBundleDetailsModel.  # noqa: E501
        :type: str
        """

        self._enrollment_user_name = enrollment_user_name

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this StagingBundleDetailsModel.  # noqa: E501

        Unique Identifier of the Organization Group where the staging bundle is managed at.  # noqa: E501

        :return: The organization_group_uuid of this StagingBundleDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this StagingBundleDetailsModel.

        Unique Identifier of the Organization Group where the staging bundle is managed at.  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this StagingBundleDetailsModel.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def organization_group_name(self):
        """Gets the organization_group_name of this StagingBundleDetailsModel.  # noqa: E501

        Name of the Organization Group where the staging bundle is managed at.  # noqa: E501

        :return: The organization_group_name of this StagingBundleDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_name

    @organization_group_name.setter
    def organization_group_name(self, organization_group_name):
        """Sets the organization_group_name of this StagingBundleDetailsModel.

        Name of the Organization Group where the staging bundle is managed at.  # noqa: E501

        :param organization_group_name: The organization_group_name of this StagingBundleDetailsModel.  # noqa: E501
        :type: str
        """

        self._organization_group_name = organization_group_name

    @property
    def id(self):
        """Gets the id of this StagingBundleDetailsModel.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this StagingBundleDetailsModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StagingBundleDetailsModel.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this StagingBundleDetailsModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this StagingBundleDetailsModel.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this StagingBundleDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this StagingBundleDetailsModel.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this StagingBundleDetailsModel.  # noqa: E501
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
        if issubclass(StagingBundleDetailsModel, dict):
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
        if not isinstance(other, StagingBundleDetailsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagingBundleDetailsModel):
            return True

        return self.to_dict() != other.to_dict()
