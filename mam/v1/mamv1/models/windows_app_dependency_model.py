# coding: utf-8

"""
    MAM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv1.configuration import Configuration


class WindowsAppDependencyModel(object):
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
        'location_group_id': 'int',
        'organization_group_uuid': 'str',
        'is_system_app': 'bool',
        'blob_id': 'int',
        'version': 'str',
        'processor_architecture': 'str',
        'package_family_name': 'str',
        'package_id': 'str',
        'deployment_options': 'AppDeploymentOptionsModel_',
        'files_options': 'AppFilesOptionsModel_',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'location_group_id': 'LocationGroupId',
        'organization_group_uuid': 'OrganizationGroupUuid',
        'is_system_app': 'IsSystemApp',
        'blob_id': 'BlobId',
        'version': 'Version',
        'processor_architecture': 'ProcessorArchitecture',
        'package_family_name': 'PackageFamilyName',
        'package_id': 'PackageId',
        'deployment_options': 'DeploymentOptions',
        'files_options': 'FilesOptions',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, name=None, location_group_id=None, organization_group_uuid=None, is_system_app=None, blob_id=None, version=None, processor_architecture=None, package_family_name=None, package_id=None, deployment_options=None, files_options=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """WindowsAppDependencyModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._location_group_id = None
        self._organization_group_uuid = None
        self._is_system_app = None
        self._blob_id = None
        self._version = None
        self._processor_architecture = None
        self._package_family_name = None
        self._package_id = None
        self._deployment_options = None
        self._files_options = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if location_group_id is not None:
            self.location_group_id = location_group_id
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if is_system_app is not None:
            self.is_system_app = is_system_app
        if blob_id is not None:
            self.blob_id = blob_id
        if version is not None:
            self.version = version
        if processor_architecture is not None:
            self.processor_architecture = processor_architecture
        if package_family_name is not None:
            self.package_family_name = package_family_name
        if package_id is not None:
            self.package_id = package_id
        if deployment_options is not None:
            self.deployment_options = deployment_options
        if files_options is not None:
            self.files_options = files_options
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def name(self):
        """Gets the name of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets application Name.  # noqa: E501

        :return: The name of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WindowsAppDependencyModel.

        Gets or sets application Name.  # noqa: E501

        :param name: The name of this WindowsAppDependencyModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def location_group_id(self):
        """Gets the location_group_id of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets location Group Id.  # noqa: E501

        :return: The location_group_id of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: int
        """
        return self._location_group_id

    @location_group_id.setter
    def location_group_id(self, location_group_id):
        """Sets the location_group_id of this WindowsAppDependencyModel.

        Gets or sets location Group Id.  # noqa: E501

        :param location_group_id: The location_group_id of this WindowsAppDependencyModel.  # noqa: E501
        :type: int
        """

        self._location_group_id = location_group_id

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets organization Group UUID.  # noqa: E501

        :return: The organization_group_uuid of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this WindowsAppDependencyModel.

        Gets or sets organization Group UUID.  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this WindowsAppDependencyModel.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def is_system_app(self):
        """Gets the is_system_app of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets a value indicating whether bool to check if the app is system app.  # noqa: E501

        :return: The is_system_app of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_system_app

    @is_system_app.setter
    def is_system_app(self, is_system_app):
        """Sets the is_system_app of this WindowsAppDependencyModel.

        Gets or sets a value indicating whether bool to check if the app is system app.  # noqa: E501

        :param is_system_app: The is_system_app of this WindowsAppDependencyModel.  # noqa: E501
        :type: bool
        """

        self._is_system_app = is_system_app

    @property
    def blob_id(self):
        """Gets the blob_id of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets application Blob Id.  # noqa: E501

        :return: The blob_id of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: int
        """
        return self._blob_id

    @blob_id.setter
    def blob_id(self, blob_id):
        """Sets the blob_id of this WindowsAppDependencyModel.

        Gets or sets application Blob Id.  # noqa: E501

        :param blob_id: The blob_id of this WindowsAppDependencyModel.  # noqa: E501
        :type: int
        """

        self._blob_id = blob_id

    @property
    def version(self):
        """Gets the version of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets app Verison.  # noqa: E501

        :return: The version of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WindowsAppDependencyModel.

        Gets or sets app Verison.  # noqa: E501

        :param version: The version of this WindowsAppDependencyModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def processor_architecture(self):
        """Gets the processor_architecture of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets processor Architecture.  # noqa: E501

        :return: The processor_architecture of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: str
        """
        return self._processor_architecture

    @processor_architecture.setter
    def processor_architecture(self, processor_architecture):
        """Sets the processor_architecture of this WindowsAppDependencyModel.

        Gets or sets processor Architecture.  # noqa: E501

        :param processor_architecture: The processor_architecture of this WindowsAppDependencyModel.  # noqa: E501
        :type: str
        """

        self._processor_architecture = processor_architecture

    @property
    def package_family_name(self):
        """Gets the package_family_name of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets package Family Name.  # noqa: E501

        :return: The package_family_name of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: str
        """
        return self._package_family_name

    @package_family_name.setter
    def package_family_name(self, package_family_name):
        """Sets the package_family_name of this WindowsAppDependencyModel.

        Gets or sets package Family Name.  # noqa: E501

        :param package_family_name: The package_family_name of this WindowsAppDependencyModel.  # noqa: E501
        :type: str
        """

        self._package_family_name = package_family_name

    @property
    def package_id(self):
        """Gets the package_id of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets package Id.  # noqa: E501

        :return: The package_id of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this WindowsAppDependencyModel.

        Gets or sets package Id.  # noqa: E501

        :param package_id: The package_id of this WindowsAppDependencyModel.  # noqa: E501
        :type: str
        """

        self._package_id = package_id

    @property
    def deployment_options(self):
        """Gets the deployment_options of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets application deployment options for software distribution.  # noqa: E501

        :return: The deployment_options of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: AppDeploymentOptionsModel_
        """
        return self._deployment_options

    @deployment_options.setter
    def deployment_options(self, deployment_options):
        """Sets the deployment_options of this WindowsAppDependencyModel.

        Gets or sets application deployment options for software distribution.  # noqa: E501

        :param deployment_options: The deployment_options of this WindowsAppDependencyModel.  # noqa: E501
        :type: AppDeploymentOptionsModel_
        """

        self._deployment_options = deployment_options

    @property
    def files_options(self):
        """Gets the files_options of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets application files options.  # noqa: E501

        :return: The files_options of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: AppFilesOptionsModel_
        """
        return self._files_options

    @files_options.setter
    def files_options(self, files_options):
        """Sets the files_options of this WindowsAppDependencyModel.

        Gets or sets application files options.  # noqa: E501

        :param files_options: The files_options of this WindowsAppDependencyModel.  # noqa: E501
        :type: AppFilesOptionsModel_
        """

        self._files_options = files_options

    @property
    def id(self):
        """Gets the id of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WindowsAppDependencyModel.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this WindowsAppDependencyModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this WindowsAppDependencyModel.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this WindowsAppDependencyModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this WindowsAppDependencyModel.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this WindowsAppDependencyModel.  # noqa: E501
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
        if issubclass(WindowsAppDependencyModel, dict):
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
        if not isinstance(other, WindowsAppDependencyModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WindowsAppDependencyModel):
            return True

        return self.to_dict() != other.to_dict()
