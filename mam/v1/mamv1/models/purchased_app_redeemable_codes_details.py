# coding: utf-8

"""
    MAM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv1.configuration import Configuration


class PurchasedAppRedeemableCodesDetails(object):
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
        'purchased': 'int',
        'burned': 'int',
        'on_hold': 'int',
        'available': 'int'
    }

    attribute_map = {
        'purchased': 'Purchased',
        'burned': 'Burned',
        'on_hold': 'OnHold',
        'available': 'Available'
    }

    def __init__(self, purchased=None, burned=None, on_hold=None, available=None, _configuration=None):  # noqa: E501
        """PurchasedAppRedeemableCodesDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._purchased = None
        self._burned = None
        self._on_hold = None
        self._available = None
        self.discriminator = None

        if purchased is not None:
            self.purchased = purchased
        if burned is not None:
            self.burned = burned
        if on_hold is not None:
            self.on_hold = on_hold
        if available is not None:
            self.available = available

    @property
    def purchased(self):
        """Gets the purchased of this PurchasedAppRedeemableCodesDetails.  # noqa: E501

        Gets or sets number Of Purchased Count.  # noqa: E501

        :return: The purchased of this PurchasedAppRedeemableCodesDetails.  # noqa: E501
        :rtype: int
        """
        return self._purchased

    @purchased.setter
    def purchased(self, purchased):
        """Sets the purchased of this PurchasedAppRedeemableCodesDetails.

        Gets or sets number Of Purchased Count.  # noqa: E501

        :param purchased: The purchased of this PurchasedAppRedeemableCodesDetails.  # noqa: E501
        :type: int
        """

        self._purchased = purchased

    @property
    def burned(self):
        """Gets the burned of this PurchasedAppRedeemableCodesDetails.  # noqa: E501

        Gets or sets number Of Burned Count.  # noqa: E501

        :return: The burned of this PurchasedAppRedeemableCodesDetails.  # noqa: E501
        :rtype: int
        """
        return self._burned

    @burned.setter
    def burned(self, burned):
        """Sets the burned of this PurchasedAppRedeemableCodesDetails.

        Gets or sets number Of Burned Count.  # noqa: E501

        :param burned: The burned of this PurchasedAppRedeemableCodesDetails.  # noqa: E501
        :type: int
        """

        self._burned = burned

    @property
    def on_hold(self):
        """Gets the on_hold of this PurchasedAppRedeemableCodesDetails.  # noqa: E501

        Gets or sets number Of On Hold Count.  # noqa: E501

        :return: The on_hold of this PurchasedAppRedeemableCodesDetails.  # noqa: E501
        :rtype: int
        """
        return self._on_hold

    @on_hold.setter
    def on_hold(self, on_hold):
        """Sets the on_hold of this PurchasedAppRedeemableCodesDetails.

        Gets or sets number Of On Hold Count.  # noqa: E501

        :param on_hold: The on_hold of this PurchasedAppRedeemableCodesDetails.  # noqa: E501
        :type: int
        """

        self._on_hold = on_hold

    @property
    def available(self):
        """Gets the available of this PurchasedAppRedeemableCodesDetails.  # noqa: E501

        Gets or sets number Of Avalibale Count.  # noqa: E501

        :return: The available of this PurchasedAppRedeemableCodesDetails.  # noqa: E501
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this PurchasedAppRedeemableCodesDetails.

        Gets or sets number Of Avalibale Count.  # noqa: E501

        :param available: The available of this PurchasedAppRedeemableCodesDetails.  # noqa: E501
        :type: int
        """

        self._available = available

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
        if issubclass(PurchasedAppRedeemableCodesDetails, dict):
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
        if not isinstance(other, PurchasedAppRedeemableCodesDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PurchasedAppRedeemableCodesDetails):
            return True

        return self.to_dict() != other.to_dict()
