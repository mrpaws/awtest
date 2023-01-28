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


class ProductGpsCoordinate_(object):
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
        'latitude': 'str',
        'longitude': 'str',
        'elevation': 'str'
    }

    attribute_map = {
        'latitude': 'Latitude',
        'longitude': 'Longitude',
        'elevation': 'Elevation'
    }

    def __init__(self, latitude=None, longitude=None, elevation=None, _configuration=None):  # noqa: E501
        """ProductGpsCoordinate_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._latitude = None
        self._longitude = None
        self._elevation = None
        self.discriminator = None

        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if elevation is not None:
            self.elevation = elevation

    @property
    def latitude(self):
        """Gets the latitude of this ProductGpsCoordinate_.  # noqa: E501

        Gets or sets latitude.  # noqa: E501

        :return: The latitude of this ProductGpsCoordinate_.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this ProductGpsCoordinate_.

        Gets or sets latitude.  # noqa: E501

        :param latitude: The latitude of this ProductGpsCoordinate_.  # noqa: E501
        :type: str
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this ProductGpsCoordinate_.  # noqa: E501

        Gets or sets longitude.  # noqa: E501

        :return: The longitude of this ProductGpsCoordinate_.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this ProductGpsCoordinate_.

        Gets or sets longitude.  # noqa: E501

        :param longitude: The longitude of this ProductGpsCoordinate_.  # noqa: E501
        :type: str
        """

        self._longitude = longitude

    @property
    def elevation(self):
        """Gets the elevation of this ProductGpsCoordinate_.  # noqa: E501

        Gets or sets elevation.  # noqa: E501

        :return: The elevation of this ProductGpsCoordinate_.  # noqa: E501
        :rtype: str
        """
        return self._elevation

    @elevation.setter
    def elevation(self, elevation):
        """Sets the elevation of this ProductGpsCoordinate_.

        Gets or sets elevation.  # noqa: E501

        :param elevation: The elevation of this ProductGpsCoordinate_.  # noqa: E501
        :type: str
        """

        self._elevation = elevation

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
        if issubclass(ProductGpsCoordinate_, dict):
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
        if not isinstance(other, ProductGpsCoordinate_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductGpsCoordinate_):
            return True

        return self.to_dict() != other.to_dict()