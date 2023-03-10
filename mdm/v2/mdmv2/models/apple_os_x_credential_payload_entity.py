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


class AppleOsXCredentialPayloadEntity(object):
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
        'certificate_id': 'int',
        'certificate_authority': 'int',
        'certificate_template': 'int',
        'allow_access_to_all_applications': 'bool',
        'name': 'str',
        'key_is_extractable': 'bool',
        'certificate_metadata': 'CertificateMetadataModel_',
        'identity_preference': 'MacOsCredentialIdentityPreferencePayloadV2Model_',
        'certificate_preference': 'MacOsCredentialCertificatePreferencePayloadV2Model_'
    }

    attribute_map = {
        'credential_source': 'CredentialSource',
        'credential_name': 'CredentialName',
        'certificate_id': 'CertificateID',
        'certificate_authority': 'CertificateAuthority',
        'certificate_template': 'CertificateTemplate',
        'allow_access_to_all_applications': 'AllowAccessToAllApplications',
        'name': 'Name',
        'key_is_extractable': 'KeyIsExtractable',
        'certificate_metadata': 'CertificateMetadata',
        'identity_preference': 'IdentityPreference',
        'certificate_preference': 'CertificatePreference'
    }

    def __init__(self, credential_source=None, credential_name=None, certificate_id=None, certificate_authority=None, certificate_template=None, allow_access_to_all_applications=None, name=None, key_is_extractable=None, certificate_metadata=None, identity_preference=None, certificate_preference=None, _configuration=None):  # noqa: E501
        """AppleOsXCredentialPayloadEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._credential_source = None
        self._credential_name = None
        self._certificate_id = None
        self._certificate_authority = None
        self._certificate_template = None
        self._allow_access_to_all_applications = None
        self._name = None
        self._key_is_extractable = None
        self._certificate_metadata = None
        self._identity_preference = None
        self._certificate_preference = None
        self.discriminator = None

        if credential_source is not None:
            self.credential_source = credential_source
        if credential_name is not None:
            self.credential_name = credential_name
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if certificate_authority is not None:
            self.certificate_authority = certificate_authority
        if certificate_template is not None:
            self.certificate_template = certificate_template
        if allow_access_to_all_applications is not None:
            self.allow_access_to_all_applications = allow_access_to_all_applications
        if name is not None:
            self.name = name
        if key_is_extractable is not None:
            self.key_is_extractable = key_is_extractable
        if certificate_metadata is not None:
            self.certificate_metadata = certificate_metadata
        if identity_preference is not None:
            self.identity_preference = identity_preference
        if certificate_preference is not None:
            self.certificate_preference = certificate_preference

    @property
    def credential_source(self):
        """Gets the credential_source of this AppleOsXCredentialPayloadEntity.  # noqa: E501

        Gets or sets the source of the credentials.  # noqa: E501

        :return: The credential_source of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :rtype: str
        """
        return self._credential_source

    @credential_source.setter
    def credential_source(self, credential_source):
        """Sets the credential_source of this AppleOsXCredentialPayloadEntity.

        Gets or sets the source of the credentials.  # noqa: E501

        :param credential_source: The credential_source of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :type: str
        """

        self._credential_source = credential_source

    @property
    def credential_name(self):
        """Gets the credential_name of this AppleOsXCredentialPayloadEntity.  # noqa: E501

        Gets or sets a human-readable name for the profile payload.  # noqa: E501

        :return: The credential_name of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """Sets the credential_name of this AppleOsXCredentialPayloadEntity.

        Gets or sets a human-readable name for the profile payload.  # noqa: E501

        :param credential_name: The credential_name of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                credential_name is not None and len(credential_name) > 255):
            raise ValueError("Invalid value for `credential_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                credential_name is not None and len(credential_name) < 0):
            raise ValueError("Invalid value for `credential_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._credential_name = credential_name

    @property
    def certificate_id(self):
        """Gets the certificate_id of this AppleOsXCredentialPayloadEntity.  # noqa: E501

        Gets or sets unique numeric identifier obtained after upload a certificate using the upload cert API.  # noqa: E501

        :return: The certificate_id of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :rtype: int
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this AppleOsXCredentialPayloadEntity.

        Gets or sets unique numeric identifier obtained after upload a certificate using the upload cert API.  # noqa: E501

        :param certificate_id: The certificate_id of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :type: int
        """

        self._certificate_id = certificate_id

    @property
    def certificate_authority(self):
        """Gets the certificate_authority of this AppleOsXCredentialPayloadEntity.  # noqa: E501

        Gets or sets specifies the unique numeric identifier of the certificate authority.  # noqa: E501

        :return: The certificate_authority of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :rtype: int
        """
        return self._certificate_authority

    @certificate_authority.setter
    def certificate_authority(self, certificate_authority):
        """Sets the certificate_authority of this AppleOsXCredentialPayloadEntity.

        Gets or sets specifies the unique numeric identifier of the certificate authority.  # noqa: E501

        :param certificate_authority: The certificate_authority of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :type: int
        """

        self._certificate_authority = certificate_authority

    @property
    def certificate_template(self):
        """Gets the certificate_template of this AppleOsXCredentialPayloadEntity.  # noqa: E501

        Gets or sets specifies the numeric identifier of the certificate template.  # noqa: E501

        :return: The certificate_template of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :rtype: int
        """
        return self._certificate_template

    @certificate_template.setter
    def certificate_template(self, certificate_template):
        """Sets the certificate_template of this AppleOsXCredentialPayloadEntity.

        Gets or sets specifies the numeric identifier of the certificate template.  # noqa: E501

        :param certificate_template: The certificate_template of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :type: int
        """

        self._certificate_template = certificate_template

    @property
    def allow_access_to_all_applications(self):
        """Gets the allow_access_to_all_applications of this AppleOsXCredentialPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether if true, apps have access to the private key.  # noqa: E501

        :return: The allow_access_to_all_applications of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._allow_access_to_all_applications

    @allow_access_to_all_applications.setter
    def allow_access_to_all_applications(self, allow_access_to_all_applications):
        """Sets the allow_access_to_all_applications of this AppleOsXCredentialPayloadEntity.

        Gets or sets a value indicating whether if true, apps have access to the private key.  # noqa: E501

        :param allow_access_to_all_applications: The allow_access_to_all_applications of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._allow_access_to_all_applications = allow_access_to_all_applications

    @property
    def name(self):
        """Gets the name of this AppleOsXCredentialPayloadEntity.  # noqa: E501

        Gets or sets the name or description of the credential.  # noqa: E501

        :return: The name of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppleOsXCredentialPayloadEntity.

        Gets or sets the name or description of the credential.  # noqa: E501

        :param name: The name of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def key_is_extractable(self):
        """Gets the key_is_extractable of this AppleOsXCredentialPayloadEntity.  # noqa: E501

        Gets or sets a value indicating whether value              Gets or sets a value indicating whether the private key can be exported from the keychain or not.  # noqa: E501

        :return: The key_is_extractable of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :rtype: bool
        """
        return self._key_is_extractable

    @key_is_extractable.setter
    def key_is_extractable(self, key_is_extractable):
        """Sets the key_is_extractable of this AppleOsXCredentialPayloadEntity.

        Gets or sets a value indicating whether value              Gets or sets a value indicating whether the private key can be exported from the keychain or not.  # noqa: E501

        :param key_is_extractable: The key_is_extractable of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :type: bool
        """

        self._key_is_extractable = key_is_extractable

    @property
    def certificate_metadata(self):
        """Gets the certificate_metadata of this AppleOsXCredentialPayloadEntity.  # noqa: E501

        Gets or sets certificate metadata.  # noqa: E501

        :return: The certificate_metadata of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :rtype: CertificateMetadataModel_
        """
        return self._certificate_metadata

    @certificate_metadata.setter
    def certificate_metadata(self, certificate_metadata):
        """Sets the certificate_metadata of this AppleOsXCredentialPayloadEntity.

        Gets or sets certificate metadata.  # noqa: E501

        :param certificate_metadata: The certificate_metadata of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :type: CertificateMetadataModel_
        """

        self._certificate_metadata = certificate_metadata

    @property
    def identity_preference(self):
        """Gets the identity_preference of this AppleOsXCredentialPayloadEntity.  # noqa: E501

        Gets or sets identity Preference payload using this credential payload.  # noqa: E501

        :return: The identity_preference of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :rtype: MacOsCredentialIdentityPreferencePayloadV2Model_
        """
        return self._identity_preference

    @identity_preference.setter
    def identity_preference(self, identity_preference):
        """Sets the identity_preference of this AppleOsXCredentialPayloadEntity.

        Gets or sets identity Preference payload using this credential payload.  # noqa: E501

        :param identity_preference: The identity_preference of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :type: MacOsCredentialIdentityPreferencePayloadV2Model_
        """

        self._identity_preference = identity_preference

    @property
    def certificate_preference(self):
        """Gets the certificate_preference of this AppleOsXCredentialPayloadEntity.  # noqa: E501

        Gets or sets certificate Preference payload using this credential payload.  # noqa: E501

        :return: The certificate_preference of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :rtype: MacOsCredentialCertificatePreferencePayloadV2Model_
        """
        return self._certificate_preference

    @certificate_preference.setter
    def certificate_preference(self, certificate_preference):
        """Sets the certificate_preference of this AppleOsXCredentialPayloadEntity.

        Gets or sets certificate Preference payload using this credential payload.  # noqa: E501

        :param certificate_preference: The certificate_preference of this AppleOsXCredentialPayloadEntity.  # noqa: E501
        :type: MacOsCredentialCertificatePreferencePayloadV2Model_
        """

        self._certificate_preference = certificate_preference

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
        if issubclass(AppleOsXCredentialPayloadEntity, dict):
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
        if not isinstance(other, AppleOsXCredentialPayloadEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleOsXCredentialPayloadEntity):
            return True

        return self.to_dict() != other.to_dict()
