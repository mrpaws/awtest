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


class StagingBundleV2Model(object):
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
        'platform_name': 'str',
        'general': 'StagingGeneralV2Model',
        'manifest': 'StagingManifestV2Model',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'platform_name': 'platform_name',
        'general': 'general',
        'manifest': 'manifest',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, platform_name=None, general=None, manifest=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """StagingBundleV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._platform_name = None
        self._general = None
        self._manifest = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if platform_name is not None:
            self.platform_name = platform_name
        if general is not None:
            self.general = general
        if manifest is not None:
            self.manifest = manifest
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def platform_name(self):
        """Gets the platform_name of this StagingBundleV2Model.  # noqa: E501

        The platform for which staging package is created For eg. 5 - Android, 1 - WindowsMobile  # noqa: E501

        :return: The platform_name of this StagingBundleV2Model.  # noqa: E501
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """Sets the platform_name of this StagingBundleV2Model.

        The platform for which staging package is created For eg. 5 - Android, 1 - WindowsMobile  # noqa: E501

        :param platform_name: The platform_name of this StagingBundleV2Model.  # noqa: E501
        :type: str
        """

        self._platform_name = platform_name

    @property
    def general(self):
        """Gets the general of this StagingBundleV2Model.  # noqa: E501

          # noqa: E501

        :return: The general of this StagingBundleV2Model.  # noqa: E501
        :rtype: StagingGeneralV2Model
        """
        return self._general

    @general.setter
    def general(self, general):
        """Sets the general of this StagingBundleV2Model.

          # noqa: E501

        :param general: The general of this StagingBundleV2Model.  # noqa: E501
        :type: StagingGeneralV2Model
        """

        self._general = general

    @property
    def manifest(self):
        """Gets the manifest of this StagingBundleV2Model.  # noqa: E501

          # noqa: E501

        :return: The manifest of this StagingBundleV2Model.  # noqa: E501
        :rtype: StagingManifestV2Model
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this StagingBundleV2Model.

          # noqa: E501

        :param manifest: The manifest of this StagingBundleV2Model.  # noqa: E501
        :type: StagingManifestV2Model
        """

        self._manifest = manifest

    @property
    def id(self):
        """Gets the id of this StagingBundleV2Model.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this StagingBundleV2Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StagingBundleV2Model.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this StagingBundleV2Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this StagingBundleV2Model.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this StagingBundleV2Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this StagingBundleV2Model.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this StagingBundleV2Model.  # noqa: E501
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
        if issubclass(StagingBundleV2Model, dict):
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
        if not isinstance(other, StagingBundleV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagingBundleV2Model):
            return True

        return self.to_dict() != other.to_dict()
