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


class DeviceInventoryEntity(object):
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
        'i_type': 'str',
        'name': 'str',
        'version_installed': 'str',
        'install_state': 'int',
        'device_id': 'int',
        'bundle_identifier': 'str',
        'custom_attribute_name': 'str',
        'custom_attribute_value': 'str',
        'custom_attribute_app_group': 'str',
        'profile_identifier': 'str',
        'inventory_type': 'int',
        'uuid': 'str',
        'table_name': 'str',
        'id_field': 'int'
    }

    attribute_map = {
        'id': 'ID',
        'i_type': 'IType',
        'name': 'Name',
        'version_installed': 'VersionInstalled',
        'install_state': 'InstallState',
        'device_id': 'DeviceID',
        'bundle_identifier': 'BundleIdentifier',
        'custom_attribute_name': 'CustomAttributeName',
        'custom_attribute_value': 'CustomAttributeValue',
        'custom_attribute_app_group': 'CustomAttributeAppGroup',
        'profile_identifier': 'ProfileIdentifier',
        'inventory_type': 'InventoryType',
        'uuid': 'Uuid',
        'table_name': 'TableName',
        'id_field': 'IDField'
    }

    def __init__(self, id=None, i_type=None, name=None, version_installed=None, install_state=None, device_id=None, bundle_identifier=None, custom_attribute_name=None, custom_attribute_value=None, custom_attribute_app_group=None, profile_identifier=None, inventory_type=None, uuid=None, table_name=None, id_field=None, _configuration=None):  # noqa: E501
        """DeviceInventoryEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._i_type = None
        self._name = None
        self._version_installed = None
        self._install_state = None
        self._device_id = None
        self._bundle_identifier = None
        self._custom_attribute_name = None
        self._custom_attribute_value = None
        self._custom_attribute_app_group = None
        self._profile_identifier = None
        self._inventory_type = None
        self._uuid = None
        self._table_name = None
        self._id_field = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if i_type is not None:
            self.i_type = i_type
        if name is not None:
            self.name = name
        if version_installed is not None:
            self.version_installed = version_installed
        if install_state is not None:
            self.install_state = install_state
        if device_id is not None:
            self.device_id = device_id
        if bundle_identifier is not None:
            self.bundle_identifier = bundle_identifier
        if custom_attribute_name is not None:
            self.custom_attribute_name = custom_attribute_name
        if custom_attribute_value is not None:
            self.custom_attribute_value = custom_attribute_value
        if custom_attribute_app_group is not None:
            self.custom_attribute_app_group = custom_attribute_app_group
        if profile_identifier is not None:
            self.profile_identifier = profile_identifier
        if inventory_type is not None:
            self.inventory_type = inventory_type
        if uuid is not None:
            self.uuid = uuid
        if table_name is not None:
            self.table_name = table_name
        if id_field is not None:
            self.id_field = id_field

    @property
    def id(self):
        """Gets the id of this DeviceInventoryEntity.  # noqa: E501


        :return: The id of this DeviceInventoryEntity.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceInventoryEntity.


        :param id: The id of this DeviceInventoryEntity.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def i_type(self):
        """Gets the i_type of this DeviceInventoryEntity.  # noqa: E501


        :return: The i_type of this DeviceInventoryEntity.  # noqa: E501
        :rtype: str
        """
        return self._i_type

    @i_type.setter
    def i_type(self, i_type):
        """Sets the i_type of this DeviceInventoryEntity.


        :param i_type: The i_type of this DeviceInventoryEntity.  # noqa: E501
        :type: str
        """

        self._i_type = i_type

    @property
    def name(self):
        """Gets the name of this DeviceInventoryEntity.  # noqa: E501


        :return: The name of this DeviceInventoryEntity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceInventoryEntity.


        :param name: The name of this DeviceInventoryEntity.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version_installed(self):
        """Gets the version_installed of this DeviceInventoryEntity.  # noqa: E501


        :return: The version_installed of this DeviceInventoryEntity.  # noqa: E501
        :rtype: str
        """
        return self._version_installed

    @version_installed.setter
    def version_installed(self, version_installed):
        """Sets the version_installed of this DeviceInventoryEntity.


        :param version_installed: The version_installed of this DeviceInventoryEntity.  # noqa: E501
        :type: str
        """

        self._version_installed = version_installed

    @property
    def install_state(self):
        """Gets the install_state of this DeviceInventoryEntity.  # noqa: E501


        :return: The install_state of this DeviceInventoryEntity.  # noqa: E501
        :rtype: int
        """
        return self._install_state

    @install_state.setter
    def install_state(self, install_state):
        """Sets the install_state of this DeviceInventoryEntity.


        :param install_state: The install_state of this DeviceInventoryEntity.  # noqa: E501
        :type: int
        """

        self._install_state = install_state

    @property
    def device_id(self):
        """Gets the device_id of this DeviceInventoryEntity.  # noqa: E501


        :return: The device_id of this DeviceInventoryEntity.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceInventoryEntity.


        :param device_id: The device_id of this DeviceInventoryEntity.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def bundle_identifier(self):
        """Gets the bundle_identifier of this DeviceInventoryEntity.  # noqa: E501


        :return: The bundle_identifier of this DeviceInventoryEntity.  # noqa: E501
        :rtype: str
        """
        return self._bundle_identifier

    @bundle_identifier.setter
    def bundle_identifier(self, bundle_identifier):
        """Sets the bundle_identifier of this DeviceInventoryEntity.


        :param bundle_identifier: The bundle_identifier of this DeviceInventoryEntity.  # noqa: E501
        :type: str
        """

        self._bundle_identifier = bundle_identifier

    @property
    def custom_attribute_name(self):
        """Gets the custom_attribute_name of this DeviceInventoryEntity.  # noqa: E501


        :return: The custom_attribute_name of this DeviceInventoryEntity.  # noqa: E501
        :rtype: str
        """
        return self._custom_attribute_name

    @custom_attribute_name.setter
    def custom_attribute_name(self, custom_attribute_name):
        """Sets the custom_attribute_name of this DeviceInventoryEntity.


        :param custom_attribute_name: The custom_attribute_name of this DeviceInventoryEntity.  # noqa: E501
        :type: str
        """

        self._custom_attribute_name = custom_attribute_name

    @property
    def custom_attribute_value(self):
        """Gets the custom_attribute_value of this DeviceInventoryEntity.  # noqa: E501


        :return: The custom_attribute_value of this DeviceInventoryEntity.  # noqa: E501
        :rtype: str
        """
        return self._custom_attribute_value

    @custom_attribute_value.setter
    def custom_attribute_value(self, custom_attribute_value):
        """Sets the custom_attribute_value of this DeviceInventoryEntity.


        :param custom_attribute_value: The custom_attribute_value of this DeviceInventoryEntity.  # noqa: E501
        :type: str
        """

        self._custom_attribute_value = custom_attribute_value

    @property
    def custom_attribute_app_group(self):
        """Gets the custom_attribute_app_group of this DeviceInventoryEntity.  # noqa: E501


        :return: The custom_attribute_app_group of this DeviceInventoryEntity.  # noqa: E501
        :rtype: str
        """
        return self._custom_attribute_app_group

    @custom_attribute_app_group.setter
    def custom_attribute_app_group(self, custom_attribute_app_group):
        """Sets the custom_attribute_app_group of this DeviceInventoryEntity.


        :param custom_attribute_app_group: The custom_attribute_app_group of this DeviceInventoryEntity.  # noqa: E501
        :type: str
        """

        self._custom_attribute_app_group = custom_attribute_app_group

    @property
    def profile_identifier(self):
        """Gets the profile_identifier of this DeviceInventoryEntity.  # noqa: E501


        :return: The profile_identifier of this DeviceInventoryEntity.  # noqa: E501
        :rtype: str
        """
        return self._profile_identifier

    @profile_identifier.setter
    def profile_identifier(self, profile_identifier):
        """Sets the profile_identifier of this DeviceInventoryEntity.


        :param profile_identifier: The profile_identifier of this DeviceInventoryEntity.  # noqa: E501
        :type: str
        """

        self._profile_identifier = profile_identifier

    @property
    def inventory_type(self):
        """Gets the inventory_type of this DeviceInventoryEntity.  # noqa: E501


        :return: The inventory_type of this DeviceInventoryEntity.  # noqa: E501
        :rtype: int
        """
        return self._inventory_type

    @inventory_type.setter
    def inventory_type(self, inventory_type):
        """Sets the inventory_type of this DeviceInventoryEntity.


        :param inventory_type: The inventory_type of this DeviceInventoryEntity.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4]  # noqa: E501
        if (self._configuration.client_side_validation and
                inventory_type not in allowed_values):
            raise ValueError(
                "Invalid value for `inventory_type` ({0}), must be one of {1}"  # noqa: E501
                .format(inventory_type, allowed_values)
            )

        self._inventory_type = inventory_type

    @property
    def uuid(self):
        """Gets the uuid of this DeviceInventoryEntity.  # noqa: E501


        :return: The uuid of this DeviceInventoryEntity.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DeviceInventoryEntity.


        :param uuid: The uuid of this DeviceInventoryEntity.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def table_name(self):
        """Gets the table_name of this DeviceInventoryEntity.  # noqa: E501


        :return: The table_name of this DeviceInventoryEntity.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this DeviceInventoryEntity.


        :param table_name: The table_name of this DeviceInventoryEntity.  # noqa: E501
        :type: str
        """

        self._table_name = table_name

    @property
    def id_field(self):
        """Gets the id_field of this DeviceInventoryEntity.  # noqa: E501


        :return: The id_field of this DeviceInventoryEntity.  # noqa: E501
        :rtype: int
        """
        return self._id_field

    @id_field.setter
    def id_field(self, id_field):
        """Sets the id_field of this DeviceInventoryEntity.


        :param id_field: The id_field of this DeviceInventoryEntity.  # noqa: E501
        :type: int
        """

        self._id_field = id_field

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
        if issubclass(DeviceInventoryEntity, dict):
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
        if not isinstance(other, DeviceInventoryEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceInventoryEntity):
            return True

        return self.to_dict() != other.to_dict()
