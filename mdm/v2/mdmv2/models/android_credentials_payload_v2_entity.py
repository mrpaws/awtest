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


class AndroidCredentialsPayloadV2Entity(object):
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
        'credential_source': 'str',
        'credential_name': 'str',
        'certificate_data': 'str',
        'certificate_id': 'int',
        'certificate_password': 'str',
        'certificate_thumbprint': 'str',
        'certificate_type': 'str',
        'certificate_authority': 'int',
        'certificate_template': 'int',
        'smime': 'str',
        'name': 'str',
        'key_usage': 'str',
        'certificate_metadata': 'CertificateMetadataModel_'
    }

    attribute_map = {
        'credential_source': 'CredentialSource',
        'credential_name': 'CredentialName',
        'certificate_data': 'CertificateData',
        'certificate_id': 'CertificateID',
        'certificate_password': 'CertificatePassword',
        'certificate_thumbprint': 'CertificateThumbprint',
        'certificate_type': 'CertificateType',
        'certificate_authority': 'CertificateAuthority',
        'certificate_template': 'CertificateTemplate',
        'smime': 'Smime',
        'name': 'Name',
        'key_usage': 'KeyUsage',
        'certificate_metadata': 'CertificateMetadata'
    }

    def __init__(self, credential_source=None, credential_name=None, certificate_data=None, certificate_id=None, certificate_password=None, certificate_thumbprint=None, certificate_type=None, certificate_authority=None, certificate_template=None, smime=None, name=None, key_usage=None, certificate_metadata=None, _configuration=None):  # noqa: E501
        """AndroidCredentialsPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._credential_source = None
        self._credential_name = None
        self._certificate_data = None
        self._certificate_id = None
        self._certificate_password = None
        self._certificate_thumbprint = None
        self._certificate_type = None
        self._certificate_authority = None
        self._certificate_template = None
        self._smime = None
        self._name = None
        self._key_usage = None
        self._certificate_metadata = None
        self.discriminator = None

        if credential_source is not None:
            self.credential_source = credential_source
        if credential_name is not None:
            self.credential_name = credential_name
        if certificate_data is not None:
            self.certificate_data = certificate_data
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if certificate_password is not None:
            self.certificate_password = certificate_password
        if certificate_thumbprint is not None:
            self.certificate_thumbprint = certificate_thumbprint
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if certificate_authority is not None:
            self.certificate_authority = certificate_authority
        if certificate_template is not None:
            self.certificate_template = certificate_template
        if smime is not None:
            self.smime = smime
        if name is not None:
            self.name = name
        if key_usage is not None:
            self.key_usage = key_usage
        if certificate_metadata is not None:
            self.certificate_metadata = certificate_metadata

    @property
    def credential_source(self):
        """Gets the credential_source of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the certificate source.  # noqa: E501

        :return: The credential_source of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._credential_source

    @credential_source.setter
    def credential_source(self, credential_source):
        """Sets the credential_source of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the certificate source.  # noqa: E501

        :param credential_source: The credential_source of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._credential_source = credential_source

    @property
    def credential_name(self):
        """Gets the credential_name of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the name of the certificate.  # noqa: E501

        :return: The credential_name of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """Sets the credential_name of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the name of the certificate.  # noqa: E501

        :param credential_name: The credential_name of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._credential_name = credential_name

    @property
    def certificate_data(self):
        """Gets the certificate_data of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the certificate data.  # noqa: E501

        :return: The certificate_data of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._certificate_data

    @certificate_data.setter
    def certificate_data(self, certificate_data):
        """Sets the certificate_data of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the certificate data.  # noqa: E501

        :param certificate_data: The certificate_data of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._certificate_data = certificate_data

    @property
    def certificate_id(self):
        """Gets the certificate_id of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the certificate identifier.  # noqa: E501

        :return: The certificate_id of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the certificate identifier.  # noqa: E501

        :param certificate_id: The certificate_id of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._certificate_id = certificate_id

    @property
    def certificate_password(self):
        """Gets the certificate_password of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the certificate password.  # noqa: E501

        :return: The certificate_password of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._certificate_password

    @certificate_password.setter
    def certificate_password(self, certificate_password):
        """Sets the certificate_password of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the certificate password.  # noqa: E501

        :param certificate_password: The certificate_password of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._certificate_password = certificate_password

    @property
    def certificate_thumbprint(self):
        """Gets the certificate_thumbprint of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the certificate thumbprint.  # noqa: E501

        :return: The certificate_thumbprint of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._certificate_thumbprint

    @certificate_thumbprint.setter
    def certificate_thumbprint(self, certificate_thumbprint):
        """Sets the certificate_thumbprint of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the certificate thumbprint.  # noqa: E501

        :param certificate_thumbprint: The certificate_thumbprint of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._certificate_thumbprint = certificate_thumbprint

    @property
    def certificate_type(self):
        """Gets the certificate_type of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the type of the certificate.  # noqa: E501

        :return: The certificate_type of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the type of the certificate.  # noqa: E501

        :param certificate_type: The certificate_type of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._certificate_type = certificate_type

    @property
    def certificate_authority(self):
        """Gets the certificate_authority of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the certificate authority identifier.  # noqa: E501

        :return: The certificate_authority of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._certificate_authority

    @certificate_authority.setter
    def certificate_authority(self, certificate_authority):
        """Sets the certificate_authority of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the certificate authority identifier.  # noqa: E501

        :param certificate_authority: The certificate_authority of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._certificate_authority = certificate_authority

    @property
    def certificate_template(self):
        """Gets the certificate_template of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the certificate template identifier.  # noqa: E501

        :return: The certificate_template of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._certificate_template

    @certificate_template.setter
    def certificate_template(self, certificate_template):
        """Sets the certificate_template of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the certificate template identifier.  # noqa: E501

        :param certificate_template: The certificate_template of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._certificate_template = certificate_template

    @property
    def smime(self):
        """Gets the smime of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the smime.  # noqa: E501

        :return: The smime of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._smime

    @smime.setter
    def smime(self, smime):
        """Sets the smime of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the smime.  # noqa: E501

        :param smime: The smime of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._smime = smime

    @property
    def name(self):
        """Gets the name of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the name.  # noqa: E501

        :return: The name of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the name.  # noqa: E501

        :param name: The name of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def key_usage(self):
        """Gets the key_usage of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets the key usage.  # noqa: E501

        :return: The key_usage of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._key_usage

    @key_usage.setter
    def key_usage(self, key_usage):
        """Sets the key_usage of this AndroidCredentialsPayloadV2Entity.

        Gets or sets the key usage.  # noqa: E501

        :param key_usage: The key_usage of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._key_usage = key_usage

    @property
    def certificate_metadata(self):
        """Gets the certificate_metadata of this AndroidCredentialsPayloadV2Entity.  # noqa: E501

        Gets or sets certificate metadata.  # noqa: E501

        :return: The certificate_metadata of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :rtype: CertificateMetadataModel_
        """
        return self._certificate_metadata

    @certificate_metadata.setter
    def certificate_metadata(self, certificate_metadata):
        """Sets the certificate_metadata of this AndroidCredentialsPayloadV2Entity.

        Gets or sets certificate metadata.  # noqa: E501

        :param certificate_metadata: The certificate_metadata of this AndroidCredentialsPayloadV2Entity.  # noqa: E501
        :type: CertificateMetadataModel_
        """

        self._certificate_metadata = certificate_metadata

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
        if issubclass(AndroidCredentialsPayloadV2Entity, dict):
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
        if not isinstance(other, AndroidCredentialsPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidCredentialsPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
