# coding: utf-8

"""
    MAM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv2.configuration import Configuration


class AppAssignmentTunnelV1Model(object):
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
        'per_app_vpn_profile_uuid': 'str',
        'afw_per_app_vpn_profile_uuid': 'str'
    }

    attribute_map = {
        'per_app_vpn_profile_uuid': 'per_app_vpn_profile_uuid',
        'afw_per_app_vpn_profile_uuid': 'afw_per_app_vpn_profile_uuid'
    }

    def __init__(self, per_app_vpn_profile_uuid=None, afw_per_app_vpn_profile_uuid=None, _configuration=None):  # noqa: E501
        """AppAssignmentTunnelV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._per_app_vpn_profile_uuid = None
        self._afw_per_app_vpn_profile_uuid = None
        self.discriminator = None

        if per_app_vpn_profile_uuid is not None:
            self.per_app_vpn_profile_uuid = per_app_vpn_profile_uuid
        if afw_per_app_vpn_profile_uuid is not None:
            self.afw_per_app_vpn_profile_uuid = afw_per_app_vpn_profile_uuid

    @property
    def per_app_vpn_profile_uuid(self):
        """Gets the per_app_vpn_profile_uuid of this AppAssignmentTunnelV1Model.  # noqa: E501

         Tunnel profile UUID  Accepted formats **uuid**  E.g. 3d958f38-246e-4854-a306-189d941ab073  # noqa: E501

        :return: The per_app_vpn_profile_uuid of this AppAssignmentTunnelV1Model.  # noqa: E501
        :rtype: str
        """
        return self._per_app_vpn_profile_uuid

    @per_app_vpn_profile_uuid.setter
    def per_app_vpn_profile_uuid(self, per_app_vpn_profile_uuid):
        """Sets the per_app_vpn_profile_uuid of this AppAssignmentTunnelV1Model.

         Tunnel profile UUID  Accepted formats **uuid**  E.g. 3d958f38-246e-4854-a306-189d941ab073  # noqa: E501

        :param per_app_vpn_profile_uuid: The per_app_vpn_profile_uuid of this AppAssignmentTunnelV1Model.  # noqa: E501
        :type: str
        """

        self._per_app_vpn_profile_uuid = per_app_vpn_profile_uuid

    @property
    def afw_per_app_vpn_profile_uuid(self):
        """Gets the afw_per_app_vpn_profile_uuid of this AppAssignmentTunnelV1Model.  # noqa: E501

         AFW Tunnel profile UUID  Accepted formats **uuid**  E.g. 3d958f38-246e-4854-a306-189d941ab073  # noqa: E501

        :return: The afw_per_app_vpn_profile_uuid of this AppAssignmentTunnelV1Model.  # noqa: E501
        :rtype: str
        """
        return self._afw_per_app_vpn_profile_uuid

    @afw_per_app_vpn_profile_uuid.setter
    def afw_per_app_vpn_profile_uuid(self, afw_per_app_vpn_profile_uuid):
        """Sets the afw_per_app_vpn_profile_uuid of this AppAssignmentTunnelV1Model.

         AFW Tunnel profile UUID  Accepted formats **uuid**  E.g. 3d958f38-246e-4854-a306-189d941ab073  # noqa: E501

        :param afw_per_app_vpn_profile_uuid: The afw_per_app_vpn_profile_uuid of this AppAssignmentTunnelV1Model.  # noqa: E501
        :type: str
        """

        self._afw_per_app_vpn_profile_uuid = afw_per_app_vpn_profile_uuid

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
        if issubclass(AppAssignmentTunnelV1Model, dict):
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
        if not isinstance(other, AppAssignmentTunnelV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppAssignmentTunnelV1Model):
            return True

        return self.to_dict() != other.to_dict()
