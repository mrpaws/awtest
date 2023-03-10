# coding: utf-8

"""
    MCM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mcmv1.configuration import Configuration


class TemplateLink(object):
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
        'link': 'str',
        'repository_type': 'str',
        'denied_link': 'str'
    }

    attribute_map = {
        'link': 'link',
        'repository_type': 'repository_type',
        'denied_link': 'denied_link'
    }

    def __init__(self, link=None, repository_type=None, denied_link=None, _configuration=None):  # noqa: E501
        """TemplateLink - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._link = None
        self._repository_type = None
        self._denied_link = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if repository_type is not None:
            self.repository_type = repository_type
        if denied_link is not None:
            self.denied_link = denied_link

    @property
    def link(self):
        """Gets the link of this TemplateLink.  # noqa: E501

        Repository template link.  # noqa: E501

        :return: The link of this TemplateLink.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TemplateLink.

        Repository template link.  # noqa: E501

        :param link: The link of this TemplateLink.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def repository_type(self):
        """Gets the repository_type of this TemplateLink.  # noqa: E501

        Repository type.  # noqa: E501

        :return: The repository_type of this TemplateLink.  # noqa: E501
        :rtype: str
        """
        return self._repository_type

    @repository_type.setter
    def repository_type(self, repository_type):
        """Sets the repository_type of this TemplateLink.

        Repository type.  # noqa: E501

        :param repository_type: The repository_type of this TemplateLink.  # noqa: E501
        :type: str
        """
        allowed_values = ["FILE", "WEBDAV", "SHAREPOINT_WEBDAV", "BOX", "AMAZON_S3", "SHAREPOINT", "SHAREPOINTO365", "GOOGLEDRIVE", "SKYDRIVE", "SHAREPOINT_PERSONAL", "SHAREPOINTO365_PERSONAL", "CMIS", "REMOTE_FILE_STORAGE", "SHAREPOINT_WIN_AUTH", "SHAREPOINT_ADFS", "SHAREPOINTO365_ADFS", "SHAREPOINTO365_ADFS_PERSONAL", "DROPBOX", "SHAREPOINTO365_ADFS_PERSONAL_REST", "SHAREPOINTO365_ADFS_REST", "ONEDRIVE_FOR_BUSINESS_OAUTH", "SHAREPOINTO365_OAUTH"]  # noqa: E501
        if (self._configuration.client_side_validation and
                repository_type not in allowed_values):
            raise ValueError(
                "Invalid value for `repository_type` ({0}), must be one of {1}"  # noqa: E501
                .format(repository_type, allowed_values)
            )

        self._repository_type = repository_type

    @property
    def denied_link(self):
        """Gets the denied_link of this TemplateLink.  # noqa: E501

        Denied link.  # noqa: E501

        :return: The denied_link of this TemplateLink.  # noqa: E501
        :rtype: str
        """
        return self._denied_link

    @denied_link.setter
    def denied_link(self, denied_link):
        """Sets the denied_link of this TemplateLink.

        Denied link.  # noqa: E501

        :param denied_link: The denied_link of this TemplateLink.  # noqa: E501
        :type: str
        """

        self._denied_link = denied_link

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
        if issubclass(TemplateLink, dict):
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
        if not isinstance(other, TemplateLink):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateLink):
            return True

        return self.to_dict() != other.to_dict()
