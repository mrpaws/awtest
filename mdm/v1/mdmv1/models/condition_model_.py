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


class ConditionModel_(object):
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
        'name': 'str',
        'description': 'str',
        'platform_id': 'int',
        'condition_type': 'str',
        'items': 'list[ConditionItem]',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'description': 'Description',
        'platform_id': 'PlatformID',
        'condition_type': 'ConditionType',
        'items': 'Items',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, name=None, description=None, platform_id=None, condition_type=None, items=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """ConditionModel_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._platform_id = None
        self._condition_type = None
        self._items = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if platform_id is not None:
            self.platform_id = platform_id
        if condition_type is not None:
            self.condition_type = condition_type
        if items is not None:
            self.items = items
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def name(self):
        """Gets the name of this ConditionModel_.  # noqa: E501

        Gets or sets name of the ConditionModel.  # noqa: E501

        :return: The name of this ConditionModel_.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConditionModel_.

        Gets or sets name of the ConditionModel.  # noqa: E501

        :param name: The name of this ConditionModel_.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ConditionModel_.  # noqa: E501

        Gets or sets description of the ConditionModel.  # noqa: E501

        :return: The description of this ConditionModel_.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConditionModel_.

        Gets or sets description of the ConditionModel.  # noqa: E501

        :param description: The description of this ConditionModel_.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def platform_id(self):
        """Gets the platform_id of this ConditionModel_.  # noqa: E501

        Gets or sets platform ID in which ConditionModel will be created for.  # noqa: E501

        :return: The platform_id of this ConditionModel_.  # noqa: E501
        :rtype: int
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this ConditionModel_.

        Gets or sets platform ID in which ConditionModel will be created for.  # noqa: E501

        :param platform_id: The platform_id of this ConditionModel_.  # noqa: E501
        :type: int
        """

        self._platform_id = platform_id

    @property
    def condition_type(self):
        """Gets the condition_type of this ConditionModel_.  # noqa: E501

        Gets or sets conditionModel to be performed.  # noqa: E501

        :return: The condition_type of this ConditionModel_.  # noqa: E501
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """Sets the condition_type of this ConditionModel_.

        Gets or sets conditionModel to be performed.  # noqa: E501

        :param condition_type: The condition_type of this ConditionModel_.  # noqa: E501
        :type: str
        """

        self._condition_type = condition_type

    @property
    def items(self):
        """Gets the items of this ConditionModel_.  # noqa: E501

        Gets or sets details of the items in ConditionModel.  # noqa: E501

        :return: The items of this ConditionModel_.  # noqa: E501
        :rtype: list[ConditionItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ConditionModel_.

        Gets or sets details of the items in ConditionModel.  # noqa: E501

        :param items: The items of this ConditionModel_.  # noqa: E501
        :type: list[ConditionItem]
        """

        self._items = items

    @property
    def id(self):
        """Gets the id of this ConditionModel_.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this ConditionModel_.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConditionModel_.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this ConditionModel_.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this ConditionModel_.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this ConditionModel_.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ConditionModel_.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this ConditionModel_.  # noqa: E501
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
        if issubclass(ConditionModel_, dict):
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
        if not isinstance(other, ConditionModel_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConditionModel_):
            return True

        return self.to_dict() != other.to_dict()
