# coding: utf-8

"""
    System API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv1.configuration import Configuration


class RegisterDeviceDetailsModel(object):
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
        'id': 'int',
        'location_group_id': 'int',
        'friendly_name': 'str',
        'ownership': 'str',
        'platform_id': 'int',
        'model_id': 'int',
        'operating_system_id': 'int',
        'udid': 'str',
        'serial_number': 'str',
        'imei': 'str',
        'asset_number': 'str',
        'message_type': 'int',
        'message_template_id': 'str',
        'sim': 'str',
        'to_email_address': 'str',
        'to_phone_number': 'str',
        'tags': 'list[TagModel_]',
        'custom_attributes': 'list[CustomAttributeNameValueApplicationModel_]',
        'is_migration': 'bool',
        'uuid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'location_group_id': 'LocationGroupId',
        'friendly_name': 'FriendlyName',
        'ownership': 'Ownership',
        'platform_id': 'PlatformId',
        'model_id': 'ModelId',
        'operating_system_id': 'OperatingSystemId',
        'udid': 'Udid',
        'serial_number': 'SerialNumber',
        'imei': 'Imei',
        'asset_number': 'AssetNumber',
        'message_type': 'MessageType',
        'message_template_id': 'MessageTemplateId',
        'sim': 'SIM',
        'to_email_address': 'ToEmailAddress',
        'to_phone_number': 'ToPhoneNumber',
        'tags': 'Tags',
        'custom_attributes': 'CustomAttributes',
        'is_migration': 'IsMigration',
        'uuid': 'uuid'
    }

    def __init__(self, id=None, location_group_id=None, friendly_name=None, ownership=None, platform_id=None, model_id=None, operating_system_id=None, udid=None, serial_number=None, imei=None, asset_number=None, message_type=None, message_template_id=None, sim=None, to_email_address=None, to_phone_number=None, tags=None, custom_attributes=None, is_migration=None, uuid=None, _configuration=None):  # noqa: E501
        """RegisterDeviceDetailsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._location_group_id = None
        self._friendly_name = None
        self._ownership = None
        self._platform_id = None
        self._model_id = None
        self._operating_system_id = None
        self._udid = None
        self._serial_number = None
        self._imei = None
        self._asset_number = None
        self._message_type = None
        self._message_template_id = None
        self._sim = None
        self._to_email_address = None
        self._to_phone_number = None
        self._tags = None
        self._custom_attributes = None
        self._is_migration = None
        self._uuid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if location_group_id is not None:
            self.location_group_id = location_group_id
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if ownership is not None:
            self.ownership = ownership
        if platform_id is not None:
            self.platform_id = platform_id
        if model_id is not None:
            self.model_id = model_id
        if operating_system_id is not None:
            self.operating_system_id = operating_system_id
        if udid is not None:
            self.udid = udid
        if serial_number is not None:
            self.serial_number = serial_number
        if imei is not None:
            self.imei = imei
        if asset_number is not None:
            self.asset_number = asset_number
        if message_type is not None:
            self.message_type = message_type
        if message_template_id is not None:
            self.message_template_id = message_template_id
        if sim is not None:
            self.sim = sim
        if to_email_address is not None:
            self.to_email_address = to_email_address
        if to_phone_number is not None:
            self.to_phone_number = to_phone_number
        if tags is not None:
            self.tags = tags
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes
        if is_migration is not None:
            self.is_migration = is_migration
        if uuid is not None:
            self.uuid = uuid

    @property
    def id(self):
        """Gets the id of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RegisterDeviceDetailsModel.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def location_group_id(self):
        """Gets the location_group_id of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets organization group identifier.  # noqa: E501

        :return: The location_group_id of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: int
        """
        return self._location_group_id

    @location_group_id.setter
    def location_group_id(self, location_group_id):
        """Sets the location_group_id of this RegisterDeviceDetailsModel.

        Gets or sets organization group identifier.  # noqa: E501

        :param location_group_id: The location_group_id of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: int
        """

        self._location_group_id = location_group_id

    @property
    def friendly_name(self):
        """Gets the friendly_name of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets device friendly name.  # noqa: E501

        :return: The friendly_name of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this RegisterDeviceDetailsModel.

        Gets or sets device friendly name.  # noqa: E501

        :param friendly_name: The friendly_name of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def ownership(self):
        """Gets the ownership of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets device ownership type.  # noqa: E501

        :return: The ownership of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        """Sets the ownership of this RegisterDeviceDetailsModel.

        Gets or sets device ownership type.  # noqa: E501

        :param ownership: The ownership of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: str
        """

        self._ownership = ownership

    @property
    def platform_id(self):
        """Gets the platform_id of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets device platform identifier.  # noqa: E501

        :return: The platform_id of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: int
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this RegisterDeviceDetailsModel.

        Gets or sets device platform identifier.  # noqa: E501

        :param platform_id: The platform_id of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: int
        """

        self._platform_id = platform_id

    @property
    def model_id(self):
        """Gets the model_id of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets device model identifier.  # noqa: E501

        :return: The model_id of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: int
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this RegisterDeviceDetailsModel.

        Gets or sets device model identifier.  # noqa: E501

        :param model_id: The model_id of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: int
        """

        self._model_id = model_id

    @property
    def operating_system_id(self):
        """Gets the operating_system_id of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets device operating system identifier.  # noqa: E501

        :return: The operating_system_id of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: int
        """
        return self._operating_system_id

    @operating_system_id.setter
    def operating_system_id(self, operating_system_id):
        """Sets the operating_system_id of this RegisterDeviceDetailsModel.

        Gets or sets device operating system identifier.  # noqa: E501

        :param operating_system_id: The operating_system_id of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: int
        """

        self._operating_system_id = operating_system_id

    @property
    def udid(self):
        """Gets the udid of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets device udid.  # noqa: E501

        :return: The udid of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._udid

    @udid.setter
    def udid(self, udid):
        """Sets the udid of this RegisterDeviceDetailsModel.

        Gets or sets device udid.  # noqa: E501

        :param udid: The udid of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: str
        """

        self._udid = udid

    @property
    def serial_number(self):
        """Gets the serial_number of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets device serial number.  # noqa: E501

        :return: The serial_number of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this RegisterDeviceDetailsModel.

        Gets or sets device serial number.  # noqa: E501

        :param serial_number: The serial_number of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def imei(self):
        """Gets the imei of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets device imei.  # noqa: E501

        :return: The imei of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._imei

    @imei.setter
    def imei(self, imei):
        """Sets the imei of this RegisterDeviceDetailsModel.

        Gets or sets device imei.  # noqa: E501

        :param imei: The imei of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: str
        """

        self._imei = imei

    @property
    def asset_number(self):
        """Gets the asset_number of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets device asset number.  # noqa: E501

        :return: The asset_number of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._asset_number

    @asset_number.setter
    def asset_number(self, asset_number):
        """Sets the asset_number of this RegisterDeviceDetailsModel.

        Gets or sets device asset number.  # noqa: E501

        :param asset_number: The asset_number of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: str
        """

        self._asset_number = asset_number

    @property
    def message_type(self):
        """Gets the message_type of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets type of the message.  # noqa: E501

        :return: The message_type of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: int
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this RegisterDeviceDetailsModel.

        Gets or sets type of the message.  # noqa: E501

        :param message_type: The message_type of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, -1]  # noqa: E501
        if (self._configuration.client_side_validation and
                message_type not in allowed_values):
            raise ValueError(
                "Invalid value for `message_type` ({0}), must be one of {1}"  # noqa: E501
                .format(message_type, allowed_values)
            )

        self._message_type = message_type

    @property
    def message_template_id(self):
        """Gets the message_template_id of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets nessage template identifier.  # noqa: E501

        :return: The message_template_id of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._message_template_id

    @message_template_id.setter
    def message_template_id(self, message_template_id):
        """Sets the message_template_id of this RegisterDeviceDetailsModel.

        Gets or sets nessage template identifier.  # noqa: E501

        :param message_template_id: The message_template_id of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: str
        """

        self._message_template_id = message_template_id

    @property
    def sim(self):
        """Gets the sim of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets sim details.  # noqa: E501

        :return: The sim of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._sim

    @sim.setter
    def sim(self, sim):
        """Sets the sim of this RegisterDeviceDetailsModel.

        Gets or sets sim details.  # noqa: E501

        :param sim: The sim of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: str
        """

        self._sim = sim

    @property
    def to_email_address(self):
        """Gets the to_email_address of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets email address.  # noqa: E501

        :return: The to_email_address of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._to_email_address

    @to_email_address.setter
    def to_email_address(self, to_email_address):
        """Sets the to_email_address of this RegisterDeviceDetailsModel.

        Gets or sets email address.  # noqa: E501

        :param to_email_address: The to_email_address of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: str
        """

        self._to_email_address = to_email_address

    @property
    def to_phone_number(self):
        """Gets the to_phone_number of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets phone number.  # noqa: E501

        :return: The to_phone_number of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._to_phone_number

    @to_phone_number.setter
    def to_phone_number(self, to_phone_number):
        """Sets the to_phone_number of this RegisterDeviceDetailsModel.

        Gets or sets phone number.  # noqa: E501

        :param to_phone_number: The to_phone_number of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: str
        """

        self._to_phone_number = to_phone_number

    @property
    def tags(self):
        """Gets the tags of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets tags for the device.  # noqa: E501

        :return: The tags of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: list[TagModel_]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RegisterDeviceDetailsModel.

        Gets or sets tags for the device.  # noqa: E501

        :param tags: The tags of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: list[TagModel_]
        """

        self._tags = tags

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets device custom attributes.  # noqa: E501

        :return: The custom_attributes of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: list[CustomAttributeNameValueApplicationModel_]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this RegisterDeviceDetailsModel.

        Gets or sets device custom attributes.  # noqa: E501

        :param custom_attributes: The custom_attributes of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: list[CustomAttributeNameValueApplicationModel_]
        """

        self._custom_attributes = custom_attributes

    @property
    def is_migration(self):
        """Gets the is_migration of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets a value indicating whether value indicating whether this instance is migration.  # noqa: E501

        :return: The is_migration of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_migration

    @is_migration.setter
    def is_migration(self, is_migration):
        """Sets the is_migration of this RegisterDeviceDetailsModel.

        Gets or sets a value indicating whether value indicating whether this instance is migration.  # noqa: E501

        :param is_migration: The is_migration of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: bool
        """

        self._is_migration = is_migration

    @property
    def uuid(self):
        """Gets the uuid of this RegisterDeviceDetailsModel.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this RegisterDeviceDetailsModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this RegisterDeviceDetailsModel.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this RegisterDeviceDetailsModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(RegisterDeviceDetailsModel, dict):
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
        if not isinstance(other, RegisterDeviceDetailsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisterDeviceDetailsModel):
            return True

        return self.to_dict() != other.to_dict()
