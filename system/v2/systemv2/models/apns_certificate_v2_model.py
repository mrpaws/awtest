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


class ApnsCertificateV2Model(object):
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
        'current_setting': 'str',
        'certificate_type': 'int',
        'issued_to': 'str',
        'issued_by': 'str',
        'valid_from': 'datetime',
        'valid_to': 'datetime',
        'thumbprint': 'str',
        'apple_id': 'str',
        'child_permission': 'str'
    }

    attribute_map = {
        'current_setting': 'current_setting',
        'certificate_type': 'certificate_type',
        'issued_to': 'issued_to',
        'issued_by': 'issued_by',
        'valid_from': 'valid_from',
        'valid_to': 'valid_to',
        'thumbprint': 'thumbprint',
        'apple_id': 'apple_id',
        'child_permission': 'child_permission'
    }

    def __init__(self, current_setting=None, certificate_type=None, issued_to=None, issued_by=None, valid_from=None, valid_to=None, thumbprint=None, apple_id=None, child_permission=None, _configuration=None):  # noqa: E501
        """ApnsCertificateV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._current_setting = None
        self._certificate_type = None
        self._issued_to = None
        self._issued_by = None
        self._valid_from = None
        self._valid_to = None
        self._thumbprint = None
        self._apple_id = None
        self._child_permission = None
        self.discriminator = None

        if current_setting is not None:
            self.current_setting = current_setting
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if issued_to is not None:
            self.issued_to = issued_to
        if issued_by is not None:
            self.issued_by = issued_by
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_to is not None:
            self.valid_to = valid_to
        if thumbprint is not None:
            self.thumbprint = thumbprint
        if apple_id is not None:
            self.apple_id = apple_id
        if child_permission is not None:
            self.child_permission = child_permission

    @property
    def current_setting(self):
        """Gets the current_setting of this ApnsCertificateV2Model.  # noqa: E501

        Gets or sets the current setting indicating whether APNs certificate is inherited or overridden.  # noqa: E501

        :return: The current_setting of this ApnsCertificateV2Model.  # noqa: E501
        :rtype: str
        """
        return self._current_setting

    @current_setting.setter
    def current_setting(self, current_setting):
        """Sets the current_setting of this ApnsCertificateV2Model.

        Gets or sets the current setting indicating whether APNs certificate is inherited or overridden.  # noqa: E501

        :param current_setting: The current_setting of this ApnsCertificateV2Model.  # noqa: E501
        :type: str
        """

        self._current_setting = current_setting

    @property
    def certificate_type(self):
        """Gets the certificate_type of this ApnsCertificateV2Model.  # noqa: E501

        Gets or sets the certificate type.  # noqa: E501

        :return: The certificate_type of this ApnsCertificateV2Model.  # noqa: E501
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this ApnsCertificateV2Model.

        Gets or sets the certificate type.  # noqa: E501

        :param certificate_type: The certificate_type of this ApnsCertificateV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6]  # noqa: E501
        if (self._configuration.client_side_validation and
                certificate_type not in allowed_values):
            raise ValueError(
                "Invalid value for `certificate_type` ({0}), must be one of {1}"  # noqa: E501
                .format(certificate_type, allowed_values)
            )

        self._certificate_type = certificate_type

    @property
    def issued_to(self):
        """Gets the issued_to of this ApnsCertificateV2Model.  # noqa: E501

        Gets or sets the subject distinguished name from the certificate.  # noqa: E501

        :return: The issued_to of this ApnsCertificateV2Model.  # noqa: E501
        :rtype: str
        """
        return self._issued_to

    @issued_to.setter
    def issued_to(self, issued_to):
        """Sets the issued_to of this ApnsCertificateV2Model.

        Gets or sets the subject distinguished name from the certificate.  # noqa: E501

        :param issued_to: The issued_to of this ApnsCertificateV2Model.  # noqa: E501
        :type: str
        """

        self._issued_to = issued_to

    @property
    def issued_by(self):
        """Gets the issued_by of this ApnsCertificateV2Model.  # noqa: E501

        Gets or sets the name of the certificate issuer.  # noqa: E501

        :return: The issued_by of this ApnsCertificateV2Model.  # noqa: E501
        :rtype: str
        """
        return self._issued_by

    @issued_by.setter
    def issued_by(self, issued_by):
        """Sets the issued_by of this ApnsCertificateV2Model.

        Gets or sets the name of the certificate issuer.  # noqa: E501

        :param issued_by: The issued_by of this ApnsCertificateV2Model.  # noqa: E501
        :type: str
        """

        self._issued_by = issued_by

    @property
    def valid_from(self):
        """Gets the valid_from of this ApnsCertificateV2Model.  # noqa: E501

        Gets or sets the effective date of the certificate in ISO 8601 format.  # noqa: E501

        :return: The valid_from of this ApnsCertificateV2Model.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this ApnsCertificateV2Model.

        Gets or sets the effective date of the certificate in ISO 8601 format.  # noqa: E501

        :param valid_from: The valid_from of this ApnsCertificateV2Model.  # noqa: E501
        :type: datetime
        """

        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this ApnsCertificateV2Model.  # noqa: E501

        Gets or sets the expiration date for the certificate in ISO 8601 format.  # noqa: E501

        :return: The valid_to of this ApnsCertificateV2Model.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this ApnsCertificateV2Model.

        Gets or sets the expiration date for the certificate in ISO 8601 format.  # noqa: E501

        :param valid_to: The valid_to of this ApnsCertificateV2Model.  # noqa: E501
        :type: datetime
        """

        self._valid_to = valid_to

    @property
    def thumbprint(self):
        """Gets the thumbprint of this ApnsCertificateV2Model.  # noqa: E501

        Gets or sets the thumbprint of the certificate.  # noqa: E501

        :return: The thumbprint of this ApnsCertificateV2Model.  # noqa: E501
        :rtype: str
        """
        return self._thumbprint

    @thumbprint.setter
    def thumbprint(self, thumbprint):
        """Sets the thumbprint of this ApnsCertificateV2Model.

        Gets or sets the thumbprint of the certificate.  # noqa: E501

        :param thumbprint: The thumbprint of this ApnsCertificateV2Model.  # noqa: E501
        :type: str
        """

        self._thumbprint = thumbprint

    @property
    def apple_id(self):
        """Gets the apple_id of this ApnsCertificateV2Model.  # noqa: E501

        Gets or sets the Apple ID used to create the certificate.  # noqa: E501

        :return: The apple_id of this ApnsCertificateV2Model.  # noqa: E501
        :rtype: str
        """
        return self._apple_id

    @apple_id.setter
    def apple_id(self, apple_id):
        """Sets the apple_id of this ApnsCertificateV2Model.

        Gets or sets the Apple ID used to create the certificate.  # noqa: E501

        :param apple_id: The apple_id of this ApnsCertificateV2Model.  # noqa: E501
        :type: str
        """

        self._apple_id = apple_id

    @property
    def child_permission(self):
        """Gets the child_permission of this ApnsCertificateV2Model.  # noqa: E501

        Gets or sets the child permission.  # noqa: E501

        :return: The child_permission of this ApnsCertificateV2Model.  # noqa: E501
        :rtype: str
        """
        return self._child_permission

    @child_permission.setter
    def child_permission(self, child_permission):
        """Sets the child_permission of this ApnsCertificateV2Model.

        Gets or sets the child permission.  # noqa: E501

        :param child_permission: The child_permission of this ApnsCertificateV2Model.  # noqa: E501
        :type: str
        """

        self._child_permission = child_permission

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
        if issubclass(ApnsCertificateV2Model, dict):
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
        if not isinstance(other, ApnsCertificateV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApnsCertificateV2Model):
            return True

        return self.to_dict() != other.to_dict()
