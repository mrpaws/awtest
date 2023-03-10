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


class OemUpdateSummaryInfoV1Model(object):
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
        'message': 'str',
        'type': 'str',
        'process': 'str',
        'release_id': 'str',
        'name': 'str',
        'version': 'str',
        'criticality': 'str',
        'update_date': 'str',
        'update_type': 'str',
        'category': 'str',
        'framework': 'str',
        'level': 'str'
    }

    attribute_map = {
        'message': 'message',
        'type': 'type',
        'process': 'process',
        'release_id': 'release_id',
        'name': 'name',
        'version': 'version',
        'criticality': 'criticality',
        'update_date': 'update_date',
        'update_type': 'update_type',
        'category': 'category',
        'framework': 'framework',
        'level': 'level'
    }

    def __init__(self, message=None, type=None, process=None, release_id=None, name=None, version=None, criticality=None, update_date=None, update_type=None, category=None, framework=None, level=None, _configuration=None):  # noqa: E501
        """OemUpdateSummaryInfoV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._type = None
        self._process = None
        self._release_id = None
        self._name = None
        self._version = None
        self._criticality = None
        self._update_date = None
        self._update_type = None
        self._category = None
        self._framework = None
        self._level = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if type is not None:
            self.type = type
        if process is not None:
            self.process = process
        if release_id is not None:
            self.release_id = release_id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if criticality is not None:
            self.criticality = criticality
        if update_date is not None:
            self.update_date = update_date
        if update_type is not None:
            self.update_type = update_type
        if category is not None:
            self.category = category
        if framework is not None:
            self.framework = framework
        if level is not None:
            self.level = level

    @property
    def message(self):
        """Gets the message of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        Message received from the device.  # noqa: E501

        :return: The message of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OemUpdateSummaryInfoV1Model.

        Message received from the device.  # noqa: E501

        :param message: The message of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def type(self):
        """Gets the type of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        Type of the update received from the device.  # noqa: E501

        :return: The type of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OemUpdateSummaryInfoV1Model.

        Type of the update received from the device.  # noqa: E501

        :param type: The type of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def process(self):
        """Gets the process of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        Process of the update received from the update  # noqa: E501

        :return: The process of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this OemUpdateSummaryInfoV1Model.

        Process of the update received from the update  # noqa: E501

        :param process: The process of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._process = process

    @property
    def release_id(self):
        """Gets the release_id of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        Release identifier of the OEM update.  # noqa: E501

        :return: The release_id of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this OemUpdateSummaryInfoV1Model.

        Release identifier of the OEM update.  # noqa: E501

        :param release_id: The release_id of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._release_id = release_id

    @property
    def name(self):
        """Gets the name of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        Name of the update received from the device.  # noqa: E501

        :return: The name of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OemUpdateSummaryInfoV1Model.

        Name of the update received from the device.  # noqa: E501

        :param name: The name of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        Version of the software update received from the device.  # noqa: E501

        :return: The version of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OemUpdateSummaryInfoV1Model.

        Version of the software update received from the device.  # noqa: E501

        :param version: The version of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def criticality(self):
        """Gets the criticality of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        Criticality of the update received from the device.  # noqa: E501

        :return: The criticality of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._criticality

    @criticality.setter
    def criticality(self, criticality):
        """Sets the criticality of this OemUpdateSummaryInfoV1Model.

        Criticality of the update received from the device.  # noqa: E501

        :param criticality: The criticality of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._criticality = criticality

    @property
    def update_date(self):
        """Gets the update_date of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        Date actually oemupdate update is available for the given summary.  # noqa: E501

        :return: The update_date of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this OemUpdateSummaryInfoV1Model.

        Date actually oemupdate update is available for the given summary.  # noqa: E501

        :param update_date: The update_date of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._update_date = update_date

    @property
    def update_type(self):
        """Gets the update_type of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        Update type received from the device.  # noqa: E501

        :return: The update_type of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """Sets the update_type of this OemUpdateSummaryInfoV1Model.

        Update type received from the device.  # noqa: E501

        :param update_type: The update_type of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._update_type = update_type

    @property
    def category(self):
        """Gets the category of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        Category of the update received from the device.  # noqa: E501

        :return: The category of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this OemUpdateSummaryInfoV1Model.

        Category of the update received from the device.  # noqa: E501

        :param category: The category of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def framework(self):
        """Gets the framework of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        Framework of the software received from the device.  # noqa: E501

        :return: The framework of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        """Sets the framework of this OemUpdateSummaryInfoV1Model.

        Framework of the software received from the device.  # noqa: E501

        :param framework: The framework of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._framework = framework

    @property
    def level(self):
        """Gets the level of this OemUpdateSummaryInfoV1Model.  # noqa: E501

        The level of the OEM update.  # noqa: E501

        :return: The level of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this OemUpdateSummaryInfoV1Model.

        The level of the OEM update.  # noqa: E501

        :param level: The level of this OemUpdateSummaryInfoV1Model.  # noqa: E501
        :type: str
        """

        self._level = level

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
        if issubclass(OemUpdateSummaryInfoV1Model, dict):
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
        if not isinstance(other, OemUpdateSummaryInfoV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OemUpdateSummaryInfoV1Model):
            return True

        return self.to_dict() != other.to_dict()
