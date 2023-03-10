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


class DeviceUpdateDeploymentRankingV1Model(object):
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
        'uuid': 'str',
        'ranking': 'int'
    }

    attribute_map = {
        'uuid': 'uuid',
        'ranking': 'ranking'
    }

    def __init__(self, uuid=None, ranking=None, _configuration=None):  # noqa: E501
        """DeviceUpdateDeploymentRankingV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._uuid = None
        self._ranking = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if ranking is not None:
            self.ranking = ranking

    @property
    def uuid(self):
        """Gets the uuid of this DeviceUpdateDeploymentRankingV1Model.  # noqa: E501

        Gets or sets the device update deployment uuid.  # noqa: E501

        :return: The uuid of this DeviceUpdateDeploymentRankingV1Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DeviceUpdateDeploymentRankingV1Model.

        Gets or sets the device update deployment uuid.  # noqa: E501

        :param uuid: The uuid of this DeviceUpdateDeploymentRankingV1Model.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def ranking(self):
        """Gets the ranking of this DeviceUpdateDeploymentRankingV1Model.  # noqa: E501

        Gets or sets the device update deployment ranking.  # noqa: E501

        :return: The ranking of this DeviceUpdateDeploymentRankingV1Model.  # noqa: E501
        :rtype: int
        """
        return self._ranking

    @ranking.setter
    def ranking(self, ranking):
        """Sets the ranking of this DeviceUpdateDeploymentRankingV1Model.

        Gets or sets the device update deployment ranking.  # noqa: E501

        :param ranking: The ranking of this DeviceUpdateDeploymentRankingV1Model.  # noqa: E501
        :type: int
        """

        self._ranking = ranking

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
        if issubclass(DeviceUpdateDeploymentRankingV1Model, dict):
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
        if not isinstance(other, DeviceUpdateDeploymentRankingV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceUpdateDeploymentRankingV1Model):
            return True

        return self.to_dict() != other.to_dict()
