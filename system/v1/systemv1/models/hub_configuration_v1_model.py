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


class HubConfigurationV1Model(object):
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
        'url': 'str',
        'organization_group_uuid': 'str'
    }

    attribute_map = {
        'url': 'url',
        'organization_group_uuid': 'organizationGroupUuid'
    }

    def __init__(self, url=None, organization_group_uuid=None, _configuration=None):  # noqa: E501
        """HubConfigurationV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._url = None
        self._organization_group_uuid = None
        self.discriminator = None

        self.url = url
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid

    @property
    def url(self):
        """Gets the url of this HubConfigurationV1Model.  # noqa: E501

        Hub Services configuration URL  # noqa: E501

        :return: The url of this HubConfigurationV1Model.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HubConfigurationV1Model.

        Hub Services configuration URL  # noqa: E501

        :param url: The url of this HubConfigurationV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this HubConfigurationV1Model.  # noqa: E501

        Unique identifier of organization group  # noqa: E501

        :return: The organization_group_uuid of this HubConfigurationV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this HubConfigurationV1Model.

        Unique identifier of organization group  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this HubConfigurationV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

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
        if issubclass(HubConfigurationV1Model, dict):
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
        if not isinstance(other, HubConfigurationV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HubConfigurationV1Model):
            return True

        return self.to_dict() != other.to_dict()