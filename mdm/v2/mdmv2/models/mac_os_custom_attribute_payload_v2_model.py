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


class MacOsCustomAttributePayloadV2Model(object):
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
        'attribute_name': 'str',
        'attribute_script': 'str',
        'schedule': 'int',
        'events': 'list[str]'
    }

    attribute_map = {
        'attribute_name': 'AttributeName',
        'attribute_script': 'AttributeScript',
        'schedule': 'Schedule',
        'events': 'Events'
    }

    def __init__(self, attribute_name=None, attribute_script=None, schedule=None, events=None, _configuration=None):  # noqa: E501
        """MacOsCustomAttributePayloadV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attribute_name = None
        self._attribute_script = None
        self._schedule = None
        self._events = None
        self.discriminator = None

        if attribute_name is not None:
            self.attribute_name = attribute_name
        if attribute_script is not None:
            self.attribute_script = attribute_script
        if schedule is not None:
            self.schedule = schedule
        if events is not None:
            self.events = events

    @property
    def attribute_name(self):
        """Gets the attribute_name of this MacOsCustomAttributePayloadV2Model.  # noqa: E501

        Gets or sets the Custom Attribute name.  # noqa: E501

        :return: The attribute_name of this MacOsCustomAttributePayloadV2Model.  # noqa: E501
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this MacOsCustomAttributePayloadV2Model.

        Gets or sets the Custom Attribute name.  # noqa: E501

        :param attribute_name: The attribute_name of this MacOsCustomAttributePayloadV2Model.  # noqa: E501
        :type: str
        """

        self._attribute_name = attribute_name

    @property
    def attribute_script(self):
        """Gets the attribute_script of this MacOsCustomAttributePayloadV2Model.  # noqa: E501

        Gets or sets the Custom Attribute script in Base64 format.  # noqa: E501

        :return: The attribute_script of this MacOsCustomAttributePayloadV2Model.  # noqa: E501
        :rtype: str
        """
        return self._attribute_script

    @attribute_script.setter
    def attribute_script(self, attribute_script):
        """Sets the attribute_script of this MacOsCustomAttributePayloadV2Model.

        Gets or sets the Custom Attribute script in Base64 format.  # noqa: E501

        :param attribute_script: The attribute_script of this MacOsCustomAttributePayloadV2Model.  # noqa: E501
        :type: str
        """

        self._attribute_script = attribute_script

    @property
    def schedule(self):
        """Gets the schedule of this MacOsCustomAttributePayloadV2Model.  # noqa: E501

        Gets or sets the schedule in seconds.  # noqa: E501

        :return: The schedule of this MacOsCustomAttributePayloadV2Model.  # noqa: E501
        :rtype: int
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this MacOsCustomAttributePayloadV2Model.

        Gets or sets the schedule in seconds.  # noqa: E501

        :param schedule: The schedule of this MacOsCustomAttributePayloadV2Model.  # noqa: E501
        :type: int
        """

        self._schedule = schedule

    @property
    def events(self):
        """Gets the events of this MacOsCustomAttributePayloadV2Model.  # noqa: E501

        Gets or sets the events.  # noqa: E501

        :return: The events of this MacOsCustomAttributePayloadV2Model.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this MacOsCustomAttributePayloadV2Model.

        Gets or sets the events.  # noqa: E501

        :param events: The events of this MacOsCustomAttributePayloadV2Model.  # noqa: E501
        :type: list[str]
        """

        self._events = events

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
        if issubclass(MacOsCustomAttributePayloadV2Model, dict):
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
        if not isinstance(other, MacOsCustomAttributePayloadV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MacOsCustomAttributePayloadV2Model):
            return True

        return self.to_dict() != other.to_dict()
