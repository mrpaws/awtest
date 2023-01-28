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


class OemUpdateDeviceInfoV1Model(object):
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
        'installed_date': 'datetime',
        'update_type': 'str',
        'category': 'str',
        'framework': 'str',
        'status': 'bool'
    }

    attribute_map = {
        'message': 'message',
        'type': 'type',
        'process': 'process',
        'release_id': 'release_id',
        'name': 'name',
        'version': 'version',
        'criticality': 'criticality',
        'installed_date': 'installed_date',
        'update_type': 'update_type',
        'category': 'category',
        'framework': 'framework',
        'status': 'status'
    }

    def __init__(self, message=None, type=None, process=None, release_id=None, name=None, version=None, criticality=None, installed_date=None, update_type=None, category=None, framework=None, status=None, _configuration=None):  # noqa: E501
        """OemUpdateDeviceInfoV1Model - a model defined in Swagger"""  # noqa: E501
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
        self._installed_date = None
        self._update_type = None
        self._category = None
        self._framework = None
        self._status = None
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
        if installed_date is not None:
            self.installed_date = installed_date
        if update_type is not None:
            self.update_type = update_type
        if category is not None:
            self.category = category
        if framework is not None:
            self.framework = framework
        if status is not None:
            self.status = status

    @property
    def message(self):
        """Gets the message of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        Message received from the device.  # noqa: E501

        :return: The message of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OemUpdateDeviceInfoV1Model.

        Message received from the device.  # noqa: E501

        :param message: The message of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def type(self):
        """Gets the type of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        Type of the update received from the device.  # noqa: E501

        :return: The type of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OemUpdateDeviceInfoV1Model.

        Type of the update received from the device.  # noqa: E501

        :param type: The type of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def process(self):
        """Gets the process of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        Process of the update received from the update  # noqa: E501

        :return: The process of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this OemUpdateDeviceInfoV1Model.

        Process of the update received from the update  # noqa: E501

        :param process: The process of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._process = process

    @property
    def release_id(self):
        """Gets the release_id of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        Release identifier of the OEM update.  # noqa: E501

        :return: The release_id of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this OemUpdateDeviceInfoV1Model.

        Release identifier of the OEM update.  # noqa: E501

        :param release_id: The release_id of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._release_id = release_id

    @property
    def name(self):
        """Gets the name of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        Name of the update received from the device.  # noqa: E501

        :return: The name of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OemUpdateDeviceInfoV1Model.

        Name of the update received from the device.  # noqa: E501

        :param name: The name of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        Version of the software update received from the device.  # noqa: E501

        :return: The version of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OemUpdateDeviceInfoV1Model.

        Version of the software update received from the device.  # noqa: E501

        :param version: The version of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def criticality(self):
        """Gets the criticality of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        Criticality of the update received from the device.  # noqa: E501

        :return: The criticality of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._criticality

    @criticality.setter
    def criticality(self, criticality):
        """Sets the criticality of this OemUpdateDeviceInfoV1Model.

        Criticality of the update received from the device.  # noqa: E501

        :param criticality: The criticality of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._criticality = criticality

    @property
    def installed_date(self):
        """Gets the installed_date of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        The OEM update date.  # noqa: E501

        :return: The installed_date of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: datetime
        """
        return self._installed_date

    @installed_date.setter
    def installed_date(self, installed_date):
        """Sets the installed_date of this OemUpdateDeviceInfoV1Model.

        The OEM update date.  # noqa: E501

        :param installed_date: The installed_date of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: datetime
        """

        self._installed_date = installed_date

    @property
    def update_type(self):
        """Gets the update_type of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        Update type received from the device.  # noqa: E501

        :return: The update_type of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """Sets the update_type of this OemUpdateDeviceInfoV1Model.

        Update type received from the device.  # noqa: E501

        :param update_type: The update_type of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._update_type = update_type

    @property
    def category(self):
        """Gets the category of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        Category of the update received from the device.  # noqa: E501

        :return: The category of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this OemUpdateDeviceInfoV1Model.

        Category of the update received from the device.  # noqa: E501

        :param category: The category of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def framework(self):
        """Gets the framework of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        Framework of the software received from the device.  # noqa: E501

        :return: The framework of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        """Sets the framework of this OemUpdateDeviceInfoV1Model.

        Framework of the software received from the device.  # noqa: E501

        :param framework: The framework of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: str
        """

        self._framework = framework

    @property
    def status(self):
        """Gets the status of this OemUpdateDeviceInfoV1Model.  # noqa: E501

        Status of the OEM Update device installed status.  # noqa: E501

        :return: The status of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OemUpdateDeviceInfoV1Model.

        Status of the OEM Update device installed status.  # noqa: E501

        :param status: The status of this OemUpdateDeviceInfoV1Model.  # noqa: E501
        :type: bool
        """

        self._status = status

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
        if issubclass(OemUpdateDeviceInfoV1Model, dict):
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
        if not isinstance(other, OemUpdateDeviceInfoV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OemUpdateDeviceInfoV1Model):
            return True

        return self.to_dict() != other.to_dict()