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


class CertificateProfileMapModel(object):
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
        'certificate_profile_map_id': 'int',
        'profile_id': 'int',
        'profile_guid': 'str',
        'certificate_authority_id': 'int',
        'certificate_template_id': 'int',
        'certificate_id': 'int',
        'certificate_name': 'str'
    }

    attribute_map = {
        'certificate_profile_map_id': 'CertificateProfileMapID',
        'profile_id': 'ProfileID',
        'profile_guid': 'ProfileGuid',
        'certificate_authority_id': 'CertificateAuthorityID',
        'certificate_template_id': 'CertificateTemplateID',
        'certificate_id': 'CertificateID',
        'certificate_name': 'CertificateName'
    }

    def __init__(self, certificate_profile_map_id=None, profile_id=None, profile_guid=None, certificate_authority_id=None, certificate_template_id=None, certificate_id=None, certificate_name=None, _configuration=None):  # noqa: E501
        """CertificateProfileMapModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._certificate_profile_map_id = None
        self._profile_id = None
        self._profile_guid = None
        self._certificate_authority_id = None
        self._certificate_template_id = None
        self._certificate_id = None
        self._certificate_name = None
        self.discriminator = None

        if certificate_profile_map_id is not None:
            self.certificate_profile_map_id = certificate_profile_map_id
        if profile_id is not None:
            self.profile_id = profile_id
        if profile_guid is not None:
            self.profile_guid = profile_guid
        if certificate_authority_id is not None:
            self.certificate_authority_id = certificate_authority_id
        if certificate_template_id is not None:
            self.certificate_template_id = certificate_template_id
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if certificate_name is not None:
            self.certificate_name = certificate_name

    @property
    def certificate_profile_map_id(self):
        """Gets the certificate_profile_map_id of this CertificateProfileMapModel.  # noqa: E501

        The certificate profile map ID  # noqa: E501

        :return: The certificate_profile_map_id of this CertificateProfileMapModel.  # noqa: E501
        :rtype: int
        """
        return self._certificate_profile_map_id

    @certificate_profile_map_id.setter
    def certificate_profile_map_id(self, certificate_profile_map_id):
        """Sets the certificate_profile_map_id of this CertificateProfileMapModel.

        The certificate profile map ID  # noqa: E501

        :param certificate_profile_map_id: The certificate_profile_map_id of this CertificateProfileMapModel.  # noqa: E501
        :type: int
        """

        self._certificate_profile_map_id = certificate_profile_map_id

    @property
    def profile_id(self):
        """Gets the profile_id of this CertificateProfileMapModel.  # noqa: E501

        The device profile ID  # noqa: E501

        :return: The profile_id of this CertificateProfileMapModel.  # noqa: E501
        :rtype: int
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this CertificateProfileMapModel.

        The device profile ID  # noqa: E501

        :param profile_id: The profile_id of this CertificateProfileMapModel.  # noqa: E501
        :type: int
        """

        self._profile_id = profile_id

    @property
    def profile_guid(self):
        """Gets the profile_guid of this CertificateProfileMapModel.  # noqa: E501

        Unique identifier for profile record  # noqa: E501

        :return: The profile_guid of this CertificateProfileMapModel.  # noqa: E501
        :rtype: str
        """
        return self._profile_guid

    @profile_guid.setter
    def profile_guid(self, profile_guid):
        """Sets the profile_guid of this CertificateProfileMapModel.

        Unique identifier for profile record  # noqa: E501

        :param profile_guid: The profile_guid of this CertificateProfileMapModel.  # noqa: E501
        :type: str
        """

        self._profile_guid = profile_guid

    @property
    def certificate_authority_id(self):
        """Gets the certificate_authority_id of this CertificateProfileMapModel.  # noqa: E501

        Unique identifier for certificate authority  # noqa: E501

        :return: The certificate_authority_id of this CertificateProfileMapModel.  # noqa: E501
        :rtype: int
        """
        return self._certificate_authority_id

    @certificate_authority_id.setter
    def certificate_authority_id(self, certificate_authority_id):
        """Sets the certificate_authority_id of this CertificateProfileMapModel.

        Unique identifier for certificate authority  # noqa: E501

        :param certificate_authority_id: The certificate_authority_id of this CertificateProfileMapModel.  # noqa: E501
        :type: int
        """

        self._certificate_authority_id = certificate_authority_id

    @property
    def certificate_template_id(self):
        """Gets the certificate_template_id of this CertificateProfileMapModel.  # noqa: E501

        Unique identifier for certificate template  # noqa: E501

        :return: The certificate_template_id of this CertificateProfileMapModel.  # noqa: E501
        :rtype: int
        """
        return self._certificate_template_id

    @certificate_template_id.setter
    def certificate_template_id(self, certificate_template_id):
        """Sets the certificate_template_id of this CertificateProfileMapModel.

        Unique identifier for certificate template  # noqa: E501

        :param certificate_template_id: The certificate_template_id of this CertificateProfileMapModel.  # noqa: E501
        :type: int
        """

        self._certificate_template_id = certificate_template_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this CertificateProfileMapModel.  # noqa: E501

        Unique identifier for certificate  # noqa: E501

        :return: The certificate_id of this CertificateProfileMapModel.  # noqa: E501
        :rtype: int
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this CertificateProfileMapModel.

        Unique identifier for certificate  # noqa: E501

        :param certificate_id: The certificate_id of this CertificateProfileMapModel.  # noqa: E501
        :type: int
        """

        self._certificate_id = certificate_id

    @property
    def certificate_name(self):
        """Gets the certificate_name of this CertificateProfileMapModel.  # noqa: E501

        Name of the certificate  # noqa: E501

        :return: The certificate_name of this CertificateProfileMapModel.  # noqa: E501
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """Sets the certificate_name of this CertificateProfileMapModel.

        Name of the certificate  # noqa: E501

        :param certificate_name: The certificate_name of this CertificateProfileMapModel.  # noqa: E501
        :type: str
        """

        self._certificate_name = certificate_name

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
        if issubclass(CertificateProfileMapModel, dict):
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
        if not isinstance(other, CertificateProfileMapModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertificateProfileMapModel):
            return True

        return self.to_dict() != other.to_dict()
