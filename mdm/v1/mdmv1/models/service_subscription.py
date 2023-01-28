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


class ServiceSubscription(object):
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
        'carrier_settings_versionk__backing_field': 'str',
        'current_carrierk__backing_field': 'str',
        'current_mcck__backing_field': 'int',
        'current_mnck__backing_field': 'int',
        'card_idk__backing_field': 'str',
        'imeik__backing_field': 'str',
        'is_data_preferredk__backing_field': 'bool',
        'is_voice_preferredk__backing_field': 'bool',
        'labelk__backing_field': 'str',
        'label_idk__backing_field': 'str',
        'meidk__backing_field': 'str',
        'phone_numberk__backing_field': 'str',
        'slotk__backing_field': 'str',
        'eidk__backing_field': 'str'
    }

    attribute_map = {
        'carrier_settings_versionk__backing_field': '&lt;CarrierSettingsVersion&gt;k__BackingField',
        'current_carrierk__backing_field': '&lt;CurrentCarrier&gt;k__BackingField',
        'current_mcck__backing_field': '&lt;CurrentMCC&gt;k__BackingField',
        'current_mnck__backing_field': '&lt;CurrentMNC&gt;k__BackingField',
        'card_idk__backing_field': '&lt;CardID&gt;k__BackingField',
        'imeik__backing_field': '&lt;Imei&gt;k__BackingField',
        'is_data_preferredk__backing_field': '&lt;IsDataPreferred&gt;k__BackingField',
        'is_voice_preferredk__backing_field': '&lt;IsVoicePreferred&gt;k__BackingField',
        'labelk__backing_field': '&lt;Label&gt;k__BackingField',
        'label_idk__backing_field': '&lt;LabelID&gt;k__BackingField',
        'meidk__backing_field': '&lt;Meid&gt;k__BackingField',
        'phone_numberk__backing_field': '&lt;PhoneNumber&gt;k__BackingField',
        'slotk__backing_field': '&lt;Slot&gt;k__BackingField',
        'eidk__backing_field': '&lt;Eid&gt;k__BackingField'
    }

    def __init__(self, carrier_settings_versionk__backing_field=None, current_carrierk__backing_field=None, current_mcck__backing_field=None, current_mnck__backing_field=None, card_idk__backing_field=None, imeik__backing_field=None, is_data_preferredk__backing_field=None, is_voice_preferredk__backing_field=None, labelk__backing_field=None, label_idk__backing_field=None, meidk__backing_field=None, phone_numberk__backing_field=None, slotk__backing_field=None, eidk__backing_field=None, _configuration=None):  # noqa: E501
        """ServiceSubscription - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._carrier_settings_versionk__backing_field = None
        self._current_carrierk__backing_field = None
        self._current_mcck__backing_field = None
        self._current_mnck__backing_field = None
        self._card_idk__backing_field = None
        self._imeik__backing_field = None
        self._is_data_preferredk__backing_field = None
        self._is_voice_preferredk__backing_field = None
        self._labelk__backing_field = None
        self._label_idk__backing_field = None
        self._meidk__backing_field = None
        self._phone_numberk__backing_field = None
        self._slotk__backing_field = None
        self._eidk__backing_field = None
        self.discriminator = None

        if carrier_settings_versionk__backing_field is not None:
            self.carrier_settings_versionk__backing_field = carrier_settings_versionk__backing_field
        if current_carrierk__backing_field is not None:
            self.current_carrierk__backing_field = current_carrierk__backing_field
        if current_mcck__backing_field is not None:
            self.current_mcck__backing_field = current_mcck__backing_field
        if current_mnck__backing_field is not None:
            self.current_mnck__backing_field = current_mnck__backing_field
        if card_idk__backing_field is not None:
            self.card_idk__backing_field = card_idk__backing_field
        if imeik__backing_field is not None:
            self.imeik__backing_field = imeik__backing_field
        if is_data_preferredk__backing_field is not None:
            self.is_data_preferredk__backing_field = is_data_preferredk__backing_field
        if is_voice_preferredk__backing_field is not None:
            self.is_voice_preferredk__backing_field = is_voice_preferredk__backing_field
        if labelk__backing_field is not None:
            self.labelk__backing_field = labelk__backing_field
        if label_idk__backing_field is not None:
            self.label_idk__backing_field = label_idk__backing_field
        if meidk__backing_field is not None:
            self.meidk__backing_field = meidk__backing_field
        if phone_numberk__backing_field is not None:
            self.phone_numberk__backing_field = phone_numberk__backing_field
        if slotk__backing_field is not None:
            self.slotk__backing_field = slotk__backing_field
        if eidk__backing_field is not None:
            self.eidk__backing_field = eidk__backing_field

    @property
    def carrier_settings_versionk__backing_field(self):
        """Gets the carrier_settings_versionk__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The carrier_settings_versionk__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: str
        """
        return self._carrier_settings_versionk__backing_field

    @carrier_settings_versionk__backing_field.setter
    def carrier_settings_versionk__backing_field(self, carrier_settings_versionk__backing_field):
        """Sets the carrier_settings_versionk__backing_field of this ServiceSubscription.


        :param carrier_settings_versionk__backing_field: The carrier_settings_versionk__backing_field of this ServiceSubscription.  # noqa: E501
        :type: str
        """

        self._carrier_settings_versionk__backing_field = carrier_settings_versionk__backing_field

    @property
    def current_carrierk__backing_field(self):
        """Gets the current_carrierk__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The current_carrierk__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: str
        """
        return self._current_carrierk__backing_field

    @current_carrierk__backing_field.setter
    def current_carrierk__backing_field(self, current_carrierk__backing_field):
        """Sets the current_carrierk__backing_field of this ServiceSubscription.


        :param current_carrierk__backing_field: The current_carrierk__backing_field of this ServiceSubscription.  # noqa: E501
        :type: str
        """

        self._current_carrierk__backing_field = current_carrierk__backing_field

    @property
    def current_mcck__backing_field(self):
        """Gets the current_mcck__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The current_mcck__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: int
        """
        return self._current_mcck__backing_field

    @current_mcck__backing_field.setter
    def current_mcck__backing_field(self, current_mcck__backing_field):
        """Sets the current_mcck__backing_field of this ServiceSubscription.


        :param current_mcck__backing_field: The current_mcck__backing_field of this ServiceSubscription.  # noqa: E501
        :type: int
        """

        self._current_mcck__backing_field = current_mcck__backing_field

    @property
    def current_mnck__backing_field(self):
        """Gets the current_mnck__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The current_mnck__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: int
        """
        return self._current_mnck__backing_field

    @current_mnck__backing_field.setter
    def current_mnck__backing_field(self, current_mnck__backing_field):
        """Sets the current_mnck__backing_field of this ServiceSubscription.


        :param current_mnck__backing_field: The current_mnck__backing_field of this ServiceSubscription.  # noqa: E501
        :type: int
        """

        self._current_mnck__backing_field = current_mnck__backing_field

    @property
    def card_idk__backing_field(self):
        """Gets the card_idk__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The card_idk__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: str
        """
        return self._card_idk__backing_field

    @card_idk__backing_field.setter
    def card_idk__backing_field(self, card_idk__backing_field):
        """Sets the card_idk__backing_field of this ServiceSubscription.


        :param card_idk__backing_field: The card_idk__backing_field of this ServiceSubscription.  # noqa: E501
        :type: str
        """

        self._card_idk__backing_field = card_idk__backing_field

    @property
    def imeik__backing_field(self):
        """Gets the imeik__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The imeik__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: str
        """
        return self._imeik__backing_field

    @imeik__backing_field.setter
    def imeik__backing_field(self, imeik__backing_field):
        """Sets the imeik__backing_field of this ServiceSubscription.


        :param imeik__backing_field: The imeik__backing_field of this ServiceSubscription.  # noqa: E501
        :type: str
        """

        self._imeik__backing_field = imeik__backing_field

    @property
    def is_data_preferredk__backing_field(self):
        """Gets the is_data_preferredk__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The is_data_preferredk__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._is_data_preferredk__backing_field

    @is_data_preferredk__backing_field.setter
    def is_data_preferredk__backing_field(self, is_data_preferredk__backing_field):
        """Sets the is_data_preferredk__backing_field of this ServiceSubscription.


        :param is_data_preferredk__backing_field: The is_data_preferredk__backing_field of this ServiceSubscription.  # noqa: E501
        :type: bool
        """

        self._is_data_preferredk__backing_field = is_data_preferredk__backing_field

    @property
    def is_voice_preferredk__backing_field(self):
        """Gets the is_voice_preferredk__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The is_voice_preferredk__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._is_voice_preferredk__backing_field

    @is_voice_preferredk__backing_field.setter
    def is_voice_preferredk__backing_field(self, is_voice_preferredk__backing_field):
        """Sets the is_voice_preferredk__backing_field of this ServiceSubscription.


        :param is_voice_preferredk__backing_field: The is_voice_preferredk__backing_field of this ServiceSubscription.  # noqa: E501
        :type: bool
        """

        self._is_voice_preferredk__backing_field = is_voice_preferredk__backing_field

    @property
    def labelk__backing_field(self):
        """Gets the labelk__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The labelk__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: str
        """
        return self._labelk__backing_field

    @labelk__backing_field.setter
    def labelk__backing_field(self, labelk__backing_field):
        """Sets the labelk__backing_field of this ServiceSubscription.


        :param labelk__backing_field: The labelk__backing_field of this ServiceSubscription.  # noqa: E501
        :type: str
        """

        self._labelk__backing_field = labelk__backing_field

    @property
    def label_idk__backing_field(self):
        """Gets the label_idk__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The label_idk__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: str
        """
        return self._label_idk__backing_field

    @label_idk__backing_field.setter
    def label_idk__backing_field(self, label_idk__backing_field):
        """Sets the label_idk__backing_field of this ServiceSubscription.


        :param label_idk__backing_field: The label_idk__backing_field of this ServiceSubscription.  # noqa: E501
        :type: str
        """

        self._label_idk__backing_field = label_idk__backing_field

    @property
    def meidk__backing_field(self):
        """Gets the meidk__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The meidk__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: str
        """
        return self._meidk__backing_field

    @meidk__backing_field.setter
    def meidk__backing_field(self, meidk__backing_field):
        """Sets the meidk__backing_field of this ServiceSubscription.


        :param meidk__backing_field: The meidk__backing_field of this ServiceSubscription.  # noqa: E501
        :type: str
        """

        self._meidk__backing_field = meidk__backing_field

    @property
    def phone_numberk__backing_field(self):
        """Gets the phone_numberk__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The phone_numberk__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: str
        """
        return self._phone_numberk__backing_field

    @phone_numberk__backing_field.setter
    def phone_numberk__backing_field(self, phone_numberk__backing_field):
        """Sets the phone_numberk__backing_field of this ServiceSubscription.


        :param phone_numberk__backing_field: The phone_numberk__backing_field of this ServiceSubscription.  # noqa: E501
        :type: str
        """

        self._phone_numberk__backing_field = phone_numberk__backing_field

    @property
    def slotk__backing_field(self):
        """Gets the slotk__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The slotk__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: str
        """
        return self._slotk__backing_field

    @slotk__backing_field.setter
    def slotk__backing_field(self, slotk__backing_field):
        """Sets the slotk__backing_field of this ServiceSubscription.


        :param slotk__backing_field: The slotk__backing_field of this ServiceSubscription.  # noqa: E501
        :type: str
        """

        self._slotk__backing_field = slotk__backing_field

    @property
    def eidk__backing_field(self):
        """Gets the eidk__backing_field of this ServiceSubscription.  # noqa: E501


        :return: The eidk__backing_field of this ServiceSubscription.  # noqa: E501
        :rtype: str
        """
        return self._eidk__backing_field

    @eidk__backing_field.setter
    def eidk__backing_field(self, eidk__backing_field):
        """Sets the eidk__backing_field of this ServiceSubscription.


        :param eidk__backing_field: The eidk__backing_field of this ServiceSubscription.  # noqa: E501
        :type: str
        """

        self._eidk__backing_field = eidk__backing_field

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
        if issubclass(ServiceSubscription, dict):
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
        if not isinstance(other, ServiceSubscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceSubscription):
            return True

        return self.to_dict() != other.to_dict()