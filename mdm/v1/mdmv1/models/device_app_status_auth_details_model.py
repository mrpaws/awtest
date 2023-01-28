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


class DeviceAppStatusAuthDetailsModel(object):
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
        'ssoenabled': 'bool',
        'authenticationurl': 'str'
    }

    attribute_map = {
        'ssoenabled': 'ssoenabled',
        'authenticationurl': 'authenticationurl'
    }

    def __init__(self, ssoenabled=None, authenticationurl=None, _configuration=None):  # noqa: E501
        """DeviceAppStatusAuthDetailsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ssoenabled = None
        self._authenticationurl = None
        self.discriminator = None

        if ssoenabled is not None:
            self.ssoenabled = ssoenabled
        if authenticationurl is not None:
            self.authenticationurl = authenticationurl

    @property
    def ssoenabled(self):
        """Gets the ssoenabled of this DeviceAppStatusAuthDetailsModel.  # noqa: E501

        Gets or sets a value indicating whether indicates whether SSO is enabled for the OG or not.  # noqa: E501

        :return: The ssoenabled of this DeviceAppStatusAuthDetailsModel.  # noqa: E501
        :rtype: bool
        """
        return self._ssoenabled

    @ssoenabled.setter
    def ssoenabled(self, ssoenabled):
        """Sets the ssoenabled of this DeviceAppStatusAuthDetailsModel.

        Gets or sets a value indicating whether indicates whether SSO is enabled for the OG or not.  # noqa: E501

        :param ssoenabled: The ssoenabled of this DeviceAppStatusAuthDetailsModel.  # noqa: E501
        :type: bool
        """

        self._ssoenabled = ssoenabled

    @property
    def authenticationurl(self):
        """Gets the authenticationurl of this DeviceAppStatusAuthDetailsModel.  # noqa: E501

        Gets or sets authentication Url;.  # noqa: E501

        :return: The authenticationurl of this DeviceAppStatusAuthDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._authenticationurl

    @authenticationurl.setter
    def authenticationurl(self, authenticationurl):
        """Sets the authenticationurl of this DeviceAppStatusAuthDetailsModel.

        Gets or sets authentication Url;.  # noqa: E501

        :param authenticationurl: The authenticationurl of this DeviceAppStatusAuthDetailsModel.  # noqa: E501
        :type: str
        """

        self._authenticationurl = authenticationurl

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
        if issubclass(DeviceAppStatusAuthDetailsModel, dict):
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
        if not isinstance(other, DeviceAppStatusAuthDetailsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceAppStatusAuthDetailsModel):
            return True

        return self.to_dict() != other.to_dict()