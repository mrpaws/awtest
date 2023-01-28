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


class FilesActionsDetail(object):
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
        'name': 'str',
        'description': 'str',
        'version': 'int',
        'platform': 'str',
        'organization_group_id': 'int',
        'modified_on': 'str',
        'files': 'list[ProductFileDetials]',
        'install_manifests': 'list[ActionManifest]',
        'uninstall_manifests': 'list[ActionManifest]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'version': 'Version',
        'platform': 'Platform',
        'organization_group_id': 'OrganizationGroupId',
        'modified_on': 'ModifiedOn',
        'files': 'Files',
        'install_manifests': 'InstallManifests',
        'uninstall_manifests': 'UninstallManifests'
    }

    def __init__(self, id=None, name=None, description=None, version=None, platform=None, organization_group_id=None, modified_on=None, files=None, install_manifests=None, uninstall_manifests=None, _configuration=None):  # noqa: E501
        """FilesActionsDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._version = None
        self._platform = None
        self._organization_group_id = None
        self._modified_on = None
        self._files = None
        self._install_manifests = None
        self._uninstall_manifests = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if version is not None:
            self.version = version
        if platform is not None:
            self.platform = platform
        if organization_group_id is not None:
            self.organization_group_id = organization_group_id
        if modified_on is not None:
            self.modified_on = modified_on
        if files is not None:
            self.files = files
        if install_manifests is not None:
            self.install_manifests = install_manifests
        if uninstall_manifests is not None:
            self.uninstall_manifests = uninstall_manifests

    @property
    def id(self):
        """Gets the id of this FilesActionsDetail.  # noqa: E501

        Gets or sets files/Actions Identifier.  # noqa: E501

        :return: The id of this FilesActionsDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FilesActionsDetail.

        Gets or sets files/Actions Identifier.  # noqa: E501

        :param id: The id of this FilesActionsDetail.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FilesActionsDetail.  # noqa: E501

        Gets or sets name of Files/Actions.  # noqa: E501

        :return: The name of this FilesActionsDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FilesActionsDetail.

        Gets or sets name of Files/Actions.  # noqa: E501

        :param name: The name of this FilesActionsDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this FilesActionsDetail.  # noqa: E501

        Gets or sets description for the Files/Actions.  # noqa: E501

        :return: The description of this FilesActionsDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FilesActionsDetail.

        Gets or sets description for the Files/Actions.  # noqa: E501

        :param description: The description of this FilesActionsDetail.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def version(self):
        """Gets the version of this FilesActionsDetail.  # noqa: E501

        Gets or sets version of Files/Actions.  # noqa: E501

        :return: The version of this FilesActionsDetail.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FilesActionsDetail.

        Gets or sets version of Files/Actions.  # noqa: E501

        :param version: The version of this FilesActionsDetail.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def platform(self):
        """Gets the platform of this FilesActionsDetail.  # noqa: E501

        Gets or sets platform in which the Files/Actions will be applied.  # noqa: E501

        :return: The platform of this FilesActionsDetail.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this FilesActionsDetail.

        Gets or sets platform in which the Files/Actions will be applied.  # noqa: E501

        :param platform: The platform of this FilesActionsDetail.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def organization_group_id(self):
        """Gets the organization_group_id of this FilesActionsDetail.  # noqa: E501

        Gets or sets managed Organization Group ID.  # noqa: E501

        :return: The organization_group_id of this FilesActionsDetail.  # noqa: E501
        :rtype: int
        """
        return self._organization_group_id

    @organization_group_id.setter
    def organization_group_id(self, organization_group_id):
        """Sets the organization_group_id of this FilesActionsDetail.

        Gets or sets managed Organization Group ID.  # noqa: E501

        :param organization_group_id: The organization_group_id of this FilesActionsDetail.  # noqa: E501
        :type: int
        """

        self._organization_group_id = organization_group_id

    @property
    def modified_on(self):
        """Gets the modified_on of this FilesActionsDetail.  # noqa: E501

        Gets or sets last date time at which Files/Actions is modified.  # noqa: E501

        :return: The modified_on of this FilesActionsDetail.  # noqa: E501
        :rtype: str
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this FilesActionsDetail.

        Gets or sets last date time at which Files/Actions is modified.  # noqa: E501

        :param modified_on: The modified_on of this FilesActionsDetail.  # noqa: E501
        :type: str
        """

        self._modified_on = modified_on

    @property
    def files(self):
        """Gets the files of this FilesActionsDetail.  # noqa: E501

        Gets or sets details of Files to download to the device.  # noqa: E501

        :return: The files of this FilesActionsDetail.  # noqa: E501
        :rtype: list[ProductFileDetials]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this FilesActionsDetail.

        Gets or sets details of Files to download to the device.  # noqa: E501

        :param files: The files of this FilesActionsDetail.  # noqa: E501
        :type: list[ProductFileDetials]
        """

        self._files = files

    @property
    def install_manifests(self):
        """Gets the install_manifests of this FilesActionsDetail.  # noqa: E501

        Gets or sets the details of actions to perform in sequence when the file/action is installed on the devicem.  # noqa: E501

        :return: The install_manifests of this FilesActionsDetail.  # noqa: E501
        :rtype: list[ActionManifest]
        """
        return self._install_manifests

    @install_manifests.setter
    def install_manifests(self, install_manifests):
        """Sets the install_manifests of this FilesActionsDetail.

        Gets or sets the details of actions to perform in sequence when the file/action is installed on the devicem.  # noqa: E501

        :param install_manifests: The install_manifests of this FilesActionsDetail.  # noqa: E501
        :type: list[ActionManifest]
        """

        self._install_manifests = install_manifests

    @property
    def uninstall_manifests(self):
        """Gets the uninstall_manifests of this FilesActionsDetail.  # noqa: E501

        Gets or sets the details of actions to perform in sequence when the file/action is uninstalled from the device.  # noqa: E501

        :return: The uninstall_manifests of this FilesActionsDetail.  # noqa: E501
        :rtype: list[ActionManifest]
        """
        return self._uninstall_manifests

    @uninstall_manifests.setter
    def uninstall_manifests(self, uninstall_manifests):
        """Sets the uninstall_manifests of this FilesActionsDetail.

        Gets or sets the details of actions to perform in sequence when the file/action is uninstalled from the device.  # noqa: E501

        :param uninstall_manifests: The uninstall_manifests of this FilesActionsDetail.  # noqa: E501
        :type: list[ActionManifest]
        """

        self._uninstall_manifests = uninstall_manifests

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
        if issubclass(FilesActionsDetail, dict):
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
        if not isinstance(other, FilesActionsDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilesActionsDetail):
            return True

        return self.to_dict() != other.to_dict()
