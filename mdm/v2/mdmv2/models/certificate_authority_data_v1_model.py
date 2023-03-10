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


class CertificateAuthorityDataV1Model(object):
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
        'authority_uuid': 'str',
        'authority_name': 'str'
    }

    attribute_map = {
        'authority_uuid': 'authority_uuid',
        'authority_name': 'authority_name'
    }

    def __init__(self, authority_uuid=None, authority_name=None, _configuration=None):  # noqa: E501
        """CertificateAuthorityDataV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authority_uuid = None
        self._authority_name = None
        self.discriminator = None

        if authority_uuid is not None:
            self.authority_uuid = authority_uuid
        if authority_name is not None:
            self.authority_name = authority_name

    @property
    def authority_uuid(self):
        """Gets the authority_uuid of this CertificateAuthorityDataV1Model.  # noqa: E501

        Certificate authority uuid.  # noqa: E501

        :return: The authority_uuid of this CertificateAuthorityDataV1Model.  # noqa: E501
        :rtype: str
        """
        return self._authority_uuid

    @authority_uuid.setter
    def authority_uuid(self, authority_uuid):
        """Sets the authority_uuid of this CertificateAuthorityDataV1Model.

        Certificate authority uuid.  # noqa: E501

        :param authority_uuid: The authority_uuid of this CertificateAuthorityDataV1Model.  # noqa: E501
        :type: str
        """

        self._authority_uuid = authority_uuid

    @property
    def authority_name(self):
        """Gets the authority_name of this CertificateAuthorityDataV1Model.  # noqa: E501

        Certificate authority name.  # noqa: E501

        :return: The authority_name of this CertificateAuthorityDataV1Model.  # noqa: E501
        :rtype: str
        """
        return self._authority_name

    @authority_name.setter
    def authority_name(self, authority_name):
        """Sets the authority_name of this CertificateAuthorityDataV1Model.

        Certificate authority name.  # noqa: E501

        :param authority_name: The authority_name of this CertificateAuthorityDataV1Model.  # noqa: E501
        :type: str
        """

        self._authority_name = authority_name

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
        if issubclass(CertificateAuthorityDataV1Model, dict):
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
        if not isinstance(other, CertificateAuthorityDataV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertificateAuthorityDataV1Model):
            return True

        return self.to_dict() != other.to_dict()
