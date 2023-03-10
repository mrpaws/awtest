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


class CompliancePolicyInfoV1Model(object):
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
        'compliance_status': 'str',
        'compliance_timestamp': 'datetime',
        'compliance_policy': 'str'
    }

    attribute_map = {
        'compliance_status': 'compliance_status',
        'compliance_timestamp': 'compliance_timestamp',
        'compliance_policy': 'compliance_policy'
    }

    def __init__(self, compliance_status=None, compliance_timestamp=None, compliance_policy=None, _configuration=None):  # noqa: E501
        """CompliancePolicyInfoV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._compliance_status = None
        self._compliance_timestamp = None
        self._compliance_policy = None
        self.discriminator = None

        self.compliance_status = compliance_status
        self.compliance_timestamp = compliance_timestamp
        self.compliance_policy = compliance_policy

    @property
    def compliance_status(self):
        """Gets the compliance_status of this CompliancePolicyInfoV1Model.  # noqa: E501

        The compliance policy status for the application. The possible values are [NotAvailable, Compliant, NonCompliant]  # noqa: E501

        :return: The compliance_status of this CompliancePolicyInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._compliance_status

    @compliance_status.setter
    def compliance_status(self, compliance_status):
        """Sets the compliance_status of this CompliancePolicyInfoV1Model.

        The compliance policy status for the application. The possible values are [NotAvailable, Compliant, NonCompliant]  # noqa: E501

        :param compliance_status: The compliance_status of this CompliancePolicyInfoV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and compliance_status is None:
            raise ValueError("Invalid value for `compliance_status`, must not be `None`")  # noqa: E501

        self._compliance_status = compliance_status

    @property
    def compliance_timestamp(self):
        """Gets the compliance_timestamp of this CompliancePolicyInfoV1Model.  # noqa: E501

        Timestamp of the compliance policy status in YYYY-MM-DDTHH:MM:SSZ format.  # noqa: E501

        :return: The compliance_timestamp of this CompliancePolicyInfoV1Model.  # noqa: E501
        :rtype: datetime
        """
        return self._compliance_timestamp

    @compliance_timestamp.setter
    def compliance_timestamp(self, compliance_timestamp):
        """Sets the compliance_timestamp of this CompliancePolicyInfoV1Model.

        Timestamp of the compliance policy status in YYYY-MM-DDTHH:MM:SSZ format.  # noqa: E501

        :param compliance_timestamp: The compliance_timestamp of this CompliancePolicyInfoV1Model.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and compliance_timestamp is None:
            raise ValueError("Invalid value for `compliance_timestamp`, must not be `None`")  # noqa: E501

        self._compliance_timestamp = compliance_timestamp

    @property
    def compliance_policy(self):
        """Gets the compliance_policy of this CompliancePolicyInfoV1Model.  # noqa: E501

        The compliance policy name.  # noqa: E501

        :return: The compliance_policy of this CompliancePolicyInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._compliance_policy

    @compliance_policy.setter
    def compliance_policy(self, compliance_policy):
        """Sets the compliance_policy of this CompliancePolicyInfoV1Model.

        The compliance policy name.  # noqa: E501

        :param compliance_policy: The compliance_policy of this CompliancePolicyInfoV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and compliance_policy is None:
            raise ValueError("Invalid value for `compliance_policy`, must not be `None`")  # noqa: E501

        self._compliance_policy = compliance_policy

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
        if issubclass(CompliancePolicyInfoV1Model, dict):
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
        if not isinstance(other, CompliancePolicyInfoV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompliancePolicyInfoV1Model):
            return True

        return self.to_dict() != other.to_dict()
