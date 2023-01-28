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


class MacOsSmartCardPayloadV2Model_(object):
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
        'allow_smart_card': 'bool',
        'enforce_smart_card': 'bool',
        'show_user_pairing_dialog': 'bool',
        'one_card_per_user': 'bool',
        'certificate_trust_check': 'int',
        'token_removal_action': 'int'
    }

    attribute_map = {
        'allow_smart_card': 'AllowSmartCard',
        'enforce_smart_card': 'EnforceSmartCard',
        'show_user_pairing_dialog': 'ShowUserPairingDialog',
        'one_card_per_user': 'OneCardPerUser',
        'certificate_trust_check': 'CertificateTrustCheck',
        'token_removal_action': 'TokenRemovalAction'
    }

    def __init__(self, allow_smart_card=None, enforce_smart_card=None, show_user_pairing_dialog=None, one_card_per_user=None, certificate_trust_check=None, token_removal_action=None, _configuration=None):  # noqa: E501
        """MacOsSmartCardPayloadV2Model_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_smart_card = None
        self._enforce_smart_card = None
        self._show_user_pairing_dialog = None
        self._one_card_per_user = None
        self._certificate_trust_check = None
        self._token_removal_action = None
        self.discriminator = None

        if allow_smart_card is not None:
            self.allow_smart_card = allow_smart_card
        if enforce_smart_card is not None:
            self.enforce_smart_card = enforce_smart_card
        if show_user_pairing_dialog is not None:
            self.show_user_pairing_dialog = show_user_pairing_dialog
        if one_card_per_user is not None:
            self.one_card_per_user = one_card_per_user
        if certificate_trust_check is not None:
            self.certificate_trust_check = certificate_trust_check
        if token_removal_action is not None:
            self.token_removal_action = token_removal_action

    @property
    def allow_smart_card(self):
        """Gets the allow_smart_card of this MacOsSmartCardPayloadV2Model_.  # noqa: E501

        Gets or sets a value indicating whether indicates whether to allow SmartCard authentication.  # noqa: E501

        :return: The allow_smart_card of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_smart_card

    @allow_smart_card.setter
    def allow_smart_card(self, allow_smart_card):
        """Sets the allow_smart_card of this MacOsSmartCardPayloadV2Model_.

        Gets or sets a value indicating whether indicates whether to allow SmartCard authentication.  # noqa: E501

        :param allow_smart_card: The allow_smart_card of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :type: bool
        """

        self._allow_smart_card = allow_smart_card

    @property
    def enforce_smart_card(self):
        """Gets the enforce_smart_card of this MacOsSmartCardPayloadV2Model_.  # noqa: E501

        Gets or sets a value indicating whether indicates whether to use SmartCard for all authentication.  # noqa: E501

        :return: The enforce_smart_card of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_smart_card

    @enforce_smart_card.setter
    def enforce_smart_card(self, enforce_smart_card):
        """Sets the enforce_smart_card of this MacOsSmartCardPayloadV2Model_.

        Gets or sets a value indicating whether indicates whether to use SmartCard for all authentication.  # noqa: E501

        :param enforce_smart_card: The enforce_smart_card of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :type: bool
        """

        self._enforce_smart_card = enforce_smart_card

    @property
    def show_user_pairing_dialog(self):
        """Gets the show_user_pairing_dialog of this MacOsSmartCardPayloadV2Model_.  # noqa: E501

        Gets or sets a value indicating whether indicates whether to show user pairing dialog.  # noqa: E501

        :return: The show_user_pairing_dialog of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :rtype: bool
        """
        return self._show_user_pairing_dialog

    @show_user_pairing_dialog.setter
    def show_user_pairing_dialog(self, show_user_pairing_dialog):
        """Sets the show_user_pairing_dialog of this MacOsSmartCardPayloadV2Model_.

        Gets or sets a value indicating whether indicates whether to show user pairing dialog.  # noqa: E501

        :param show_user_pairing_dialog: The show_user_pairing_dialog of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :type: bool
        """

        self._show_user_pairing_dialog = show_user_pairing_dialog

    @property
    def one_card_per_user(self):
        """Gets the one_card_per_user of this MacOsSmartCardPayloadV2Model_.  # noqa: E501

        Gets or sets a value indicating whether indicates whether to restrict one card per user.  # noqa: E501

        :return: The one_card_per_user of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :rtype: bool
        """
        return self._one_card_per_user

    @one_card_per_user.setter
    def one_card_per_user(self, one_card_per_user):
        """Sets the one_card_per_user of this MacOsSmartCardPayloadV2Model_.

        Gets or sets a value indicating whether indicates whether to restrict one card per user.  # noqa: E501

        :param one_card_per_user: The one_card_per_user of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :type: bool
        """

        self._one_card_per_user = one_card_per_user

    @property
    def certificate_trust_check(self):
        """Gets the certificate_trust_check of this MacOsSmartCardPayloadV2Model_.  # noqa: E501

        Gets or sets certificate Trust Check. Valid values are 0-3.  0 - certificate trust check is turned off.  1 - certificate trust check is turned on with no additional revocation checks.  2 - certificate trust check is turned on, plus a soft revocation check is performed.  3 - certificate trust check is turned on, plus a hard revocation check is performed.  # noqa: E501

        :return: The certificate_trust_check of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :rtype: int
        """
        return self._certificate_trust_check

    @certificate_trust_check.setter
    def certificate_trust_check(self, certificate_trust_check):
        """Sets the certificate_trust_check of this MacOsSmartCardPayloadV2Model_.

        Gets or sets certificate Trust Check. Valid values are 0-3.  0 - certificate trust check is turned off.  1 - certificate trust check is turned on with no additional revocation checks.  2 - certificate trust check is turned on, plus a soft revocation check is performed.  3 - certificate trust check is turned on, plus a hard revocation check is performed.  # noqa: E501

        :param certificate_trust_check: The certificate_trust_check of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                certificate_trust_check is not None and certificate_trust_check > 3):  # noqa: E501
            raise ValueError("Invalid value for `certificate_trust_check`, must be a value less than or equal to `3`")  # noqa: E501
        if (self._configuration.client_side_validation and
                certificate_trust_check is not None and certificate_trust_check < 0):  # noqa: E501
            raise ValueError("Invalid value for `certificate_trust_check`, must be a value greater than or equal to `0`")  # noqa: E501

        self._certificate_trust_check = certificate_trust_check

    @property
    def token_removal_action(self):
        """Gets the token_removal_action of this MacOsSmartCardPayloadV2Model_.  # noqa: E501

        Gets or sets if 1, when the SmartCard is removed, the screensaver will be enabled.  # noqa: E501

        :return: The token_removal_action of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :rtype: int
        """
        return self._token_removal_action

    @token_removal_action.setter
    def token_removal_action(self, token_removal_action):
        """Sets the token_removal_action of this MacOsSmartCardPayloadV2Model_.

        Gets or sets if 1, when the SmartCard is removed, the screensaver will be enabled.  # noqa: E501

        :param token_removal_action: The token_removal_action of this MacOsSmartCardPayloadV2Model_.  # noqa: E501
        :type: int
        """

        self._token_removal_action = token_removal_action

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
        if issubclass(MacOsSmartCardPayloadV2Model_, dict):
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
        if not isinstance(other, MacOsSmartCardPayloadV2Model_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MacOsSmartCardPayloadV2Model_):
            return True

        return self.to_dict() != other.to_dict()