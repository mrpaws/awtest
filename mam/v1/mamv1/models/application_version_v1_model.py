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


class ApplicationVersionV1Model(object):
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
        'application_uuid': 'str',
        'unique_identifier': 'str',
        'version': 'str',
        'package_version': 'str',
        'build_package_version': 'str',
        'version_hash': 'str',
        'is_active': 'bool',
        'is_retired': 'bool',
        'version_code': 'int',
        'device_type': 'int',
        'is_provisioning_enabled': 'bool'
    }

    attribute_map = {
        'application_uuid': 'application_uuid',
        'unique_identifier': 'unique_identifier',
        'version': 'version',
        'package_version': 'package_version',
        'build_package_version': 'build_package_version',
        'version_hash': 'version_hash',
        'is_active': 'is_active',
        'is_retired': 'is_retired',
        'version_code': 'version_code',
        'device_type': 'device_type',
        'is_provisioning_enabled': 'is_provisioning_enabled'
    }

    def __init__(self, application_uuid=None, unique_identifier=None, version=None, package_version=None, build_package_version=None, version_hash=None, is_active=None, is_retired=None, version_code=None, device_type=None, is_provisioning_enabled=None, _configuration=None):  # noqa: E501
        """ApplicationVersionV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_uuid = None
        self._unique_identifier = None
        self._version = None
        self._package_version = None
        self._build_package_version = None
        self._version_hash = None
        self._is_active = None
        self._is_retired = None
        self._version_code = None
        self._device_type = None
        self._is_provisioning_enabled = None
        self.discriminator = None

        if application_uuid is not None:
            self.application_uuid = application_uuid
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier
        if version is not None:
            self.version = version
        if package_version is not None:
            self.package_version = package_version
        if build_package_version is not None:
            self.build_package_version = build_package_version
        if version_hash is not None:
            self.version_hash = version_hash
        if is_active is not None:
            self.is_active = is_active
        if is_retired is not None:
            self.is_retired = is_retired
        if version_code is not None:
            self.version_code = version_code
        if device_type is not None:
            self.device_type = device_type
        if is_provisioning_enabled is not None:
            self.is_provisioning_enabled = is_provisioning_enabled

    @property
    def application_uuid(self):
        """Gets the application_uuid of this ApplicationVersionV1Model.  # noqa: E501

        Identifier of the application.  # noqa: E501

        :return: The application_uuid of this ApplicationVersionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._application_uuid

    @application_uuid.setter
    def application_uuid(self, application_uuid):
        """Sets the application_uuid of this ApplicationVersionV1Model.

        Identifier of the application.  # noqa: E501

        :param application_uuid: The application_uuid of this ApplicationVersionV1Model.  # noqa: E501
        :type: str
        """

        self._application_uuid = application_uuid

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this ApplicationVersionV1Model.  # noqa: E501

        Application Unique Identifier.  # noqa: E501

        :return: The unique_identifier of this ApplicationVersionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this ApplicationVersionV1Model.

        Application Unique Identifier.  # noqa: E501

        :param unique_identifier: The unique_identifier of this ApplicationVersionV1Model.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

    @property
    def version(self):
        """Gets the version of this ApplicationVersionV1Model.  # noqa: E501

        This only shows the numerical version. If PackageVersion is alphanumeric instead of numeric, these will not match.  # noqa: E501

        :return: The version of this ApplicationVersionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApplicationVersionV1Model.

        This only shows the numerical version. If PackageVersion is alphanumeric instead of numeric, these will not match.  # noqa: E501

        :param version: The version of this ApplicationVersionV1Model.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def package_version(self):
        """Gets the package_version of this ApplicationVersionV1Model.  # noqa: E501

        The alphanumeric version from the application file.  # noqa: E501

        :return: The package_version of this ApplicationVersionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """Sets the package_version of this ApplicationVersionV1Model.

        The alphanumeric version from the application file.  # noqa: E501

        :param package_version: The package_version of this ApplicationVersionV1Model.  # noqa: E501
        :type: str
        """

        self._package_version = package_version

    @property
    def build_package_version(self):
        """Gets the build_package_version of this ApplicationVersionV1Model.  # noqa: E501

        Especially for IPA. The alphanumeric version of the application build.  # noqa: E501

        :return: The build_package_version of this ApplicationVersionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._build_package_version

    @build_package_version.setter
    def build_package_version(self, build_package_version):
        """Sets the build_package_version of this ApplicationVersionV1Model.

        Especially for IPA. The alphanumeric version of the application build.  # noqa: E501

        :param build_package_version: The build_package_version of this ApplicationVersionV1Model.  # noqa: E501
        :type: str
        """

        self._build_package_version = build_package_version

    @property
    def version_hash(self):
        """Gets the version_hash of this ApplicationVersionV1Model.  # noqa: E501

        Hash of Package Version and Build Package Version.  # noqa: E501

        :return: The version_hash of this ApplicationVersionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._version_hash

    @version_hash.setter
    def version_hash(self, version_hash):
        """Sets the version_hash of this ApplicationVersionV1Model.

        Hash of Package Version and Build Package Version.  # noqa: E501

        :param version_hash: The version_hash of this ApplicationVersionV1Model.  # noqa: E501
        :type: str
        """

        self._version_hash = version_hash

    @property
    def is_active(self):
        """Gets the is_active of this ApplicationVersionV1Model.  # noqa: E501

        Indicates whether or not the application is active.  # noqa: E501

        :return: The is_active of this ApplicationVersionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this ApplicationVersionV1Model.

        Indicates whether or not the application is active.  # noqa: E501

        :param is_active: The is_active of this ApplicationVersionV1Model.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_retired(self):
        """Gets the is_retired of this ApplicationVersionV1Model.  # noqa: E501

        Indicates whether or not the application is retired.  # noqa: E501

        :return: The is_retired of this ApplicationVersionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._is_retired

    @is_retired.setter
    def is_retired(self, is_retired):
        """Sets the is_retired of this ApplicationVersionV1Model.

        Indicates whether or not the application is retired.  # noqa: E501

        :param is_retired: The is_retired of this ApplicationVersionV1Model.  # noqa: E501
        :type: bool
        """

        self._is_retired = is_retired

    @property
    def version_code(self):
        """Gets the version_code of this ApplicationVersionV1Model.  # noqa: E501

        The version code of the application.  # noqa: E501

        :return: The version_code of this ApplicationVersionV1Model.  # noqa: E501
        :rtype: int
        """
        return self._version_code

    @version_code.setter
    def version_code(self, version_code):
        """Sets the version_code of this ApplicationVersionV1Model.

        The version code of the application.  # noqa: E501

        :param version_code: The version_code of this ApplicationVersionV1Model.  # noqa: E501
        :type: int
        """

        self._version_code = version_code

    @property
    def device_type(self):
        """Gets the device_type of this ApplicationVersionV1Model.  # noqa: E501

        The device type.  # noqa: E501

        :return: The device_type of this ApplicationVersionV1Model.  # noqa: E501
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ApplicationVersionV1Model.

        The device type.  # noqa: E501

        :param device_type: The device_type of this ApplicationVersionV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 100, 101, 102, 103, 104, 105, 200, 201, 1000]  # noqa: E501
        if (self._configuration.client_side_validation and
                device_type not in allowed_values):
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def is_provisioning_enabled(self):
        """Gets the is_provisioning_enabled of this ApplicationVersionV1Model.  # noqa: E501

        True if Product Provisioning is enabled for the application.  # noqa: E501

        :return: The is_provisioning_enabled of this ApplicationVersionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._is_provisioning_enabled

    @is_provisioning_enabled.setter
    def is_provisioning_enabled(self, is_provisioning_enabled):
        """Sets the is_provisioning_enabled of this ApplicationVersionV1Model.

        True if Product Provisioning is enabled for the application.  # noqa: E501

        :param is_provisioning_enabled: The is_provisioning_enabled of this ApplicationVersionV1Model.  # noqa: E501
        :type: bool
        """

        self._is_provisioning_enabled = is_provisioning_enabled

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
        if issubclass(ApplicationVersionV1Model, dict):
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
        if not isinstance(other, ApplicationVersionV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationVersionV1Model):
            return True

        return self.to_dict() != other.to_dict()
