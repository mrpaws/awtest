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


class Metadata(object):
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
        'created': 'datetime',
        'last_modified': 'datetime',
        'location': 'str',
        'resource_type': 'int',
        'version': 'str'
    }

    attribute_map = {
        'created': 'created',
        'last_modified': 'lastModified',
        'location': 'location',
        'resource_type': 'resourceType',
        'version': 'version'
    }

    def __init__(self, created=None, last_modified=None, location=None, resource_type=None, version=None, _configuration=None):  # noqa: E501
        """Metadata - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._last_modified = None
        self._location = None
        self._resource_type = None
        self._version = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if last_modified is not None:
            self.last_modified = last_modified
        if location is not None:
            self.location = location
        if resource_type is not None:
            self.resource_type = resource_type
        if version is not None:
            self.version = version

    @property
    def created(self):
        """Gets the created of this Metadata.  # noqa: E501

        The \"DateTime\" that the resource was added to the service provider.  # noqa: E501

        :return: The created of this Metadata.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Metadata.

        The \"DateTime\" that the resource was added to the service provider.  # noqa: E501

        :param created: The created of this Metadata.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_modified(self):
        """Gets the last_modified of this Metadata.  # noqa: E501

        The most recent DateTime that the details of this resource were updated at the service provider.  If this resource has never been modified since its initial creation, the value MUST be the same as the value of \"created\".  # noqa: E501

        :return: The last_modified of this Metadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Metadata.

        The most recent DateTime that the details of this resource were updated at the service provider.  If this resource has never been modified since its initial creation, the value MUST be the same as the value of \"created\".  # noqa: E501

        :param last_modified: The last_modified of this Metadata.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def location(self):
        """Gets the location of this Metadata.  # noqa: E501

        The URI of the resource being returned.  # noqa: E501

        :return: The location of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Metadata.

        The URI of the resource being returned.  # noqa: E501

        :param location: The location of this Metadata.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def resource_type(self):
        """Gets the resource_type of this Metadata.  # noqa: E501

        The name of the resource type of the resource.  # noqa: E501

        :return: The resource_type of this Metadata.  # noqa: E501
        :rtype: int
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Metadata.

        The name of the resource type of the resource.  # noqa: E501

        :param resource_type: The resource_type of this Metadata.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if (self._configuration.client_side_validation and
                resource_type not in allowed_values):
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def version(self):
        """Gets the version of this Metadata.  # noqa: E501

        The version of the resource being returned.  # noqa: E501

        :return: The version of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Metadata.

        The version of the resource being returned.  # noqa: E501

        :param version: The version of this Metadata.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(Metadata, dict):
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
        if not isinstance(other, Metadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Metadata):
            return True

        return self.to_dict() != other.to_dict()
