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


class PolicyTreeItem(object):
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
        'uuid': 'str',
        'name': 'str',
        '_class': 'str',
        'class_name': 'str',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'uuid': 'uuid',
        'name': 'name',
        '_class': 'class',
        'class_name': 'className',
        'status': 'status'
    }

    def __init__(self, id=None, uuid=None, name=None, _class=None, class_name=None, status=None, _configuration=None):  # noqa: E501
        """PolicyTreeItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._uuid = None
        self._name = None
        self.__class = None
        self._class_name = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.uuid = uuid
        self.name = name
        if _class is not None:
            self._class = _class
        if class_name is not None:
            self.class_name = class_name
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this PolicyTreeItem.  # noqa: E501

          # noqa: E501

        :return: The id of this PolicyTreeItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyTreeItem.

          # noqa: E501

        :param id: The id of this PolicyTreeItem.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this PolicyTreeItem.  # noqa: E501

        Unique identifier of the policy  # noqa: E501

        :return: The uuid of this PolicyTreeItem.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PolicyTreeItem.

        Unique identifier of the policy  # noqa: E501

        :param uuid: The uuid of this PolicyTreeItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this PolicyTreeItem.  # noqa: E501

        Name of the policy  # noqa: E501

        :return: The name of this PolicyTreeItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyTreeItem.

        Name of the policy  # noqa: E501

        :param name: The name of this PolicyTreeItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def _class(self):
        """Gets the _class of this PolicyTreeItem.  # noqa: E501

        The classification of the policy (Machine/User/Both)  # noqa: E501

        :return: The _class of this PolicyTreeItem.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this PolicyTreeItem.

        The classification of the policy (Machine/User/Both)  # noqa: E501

        :param _class: The _class of this PolicyTreeItem.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def class_name(self):
        """Gets the class_name of this PolicyTreeItem.  # noqa: E501

        The classification of the policy (Machine/User/Both)  # noqa: E501

        :return: The class_name of this PolicyTreeItem.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this PolicyTreeItem.

        The classification of the policy (Machine/User/Both)  # noqa: E501

        :param class_name: The class_name of this PolicyTreeItem.  # noqa: E501
        :type: str
        """

        self._class_name = class_name

    @property
    def status(self):
        """Gets the status of this PolicyTreeItem.  # noqa: E501

        The configured policy status  # noqa: E501

        :return: The status of this PolicyTreeItem.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PolicyTreeItem.

        The configured policy status  # noqa: E501

        :param status: The status of this PolicyTreeItem.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

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
        if issubclass(PolicyTreeItem, dict):
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
        if not isinstance(other, PolicyTreeItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyTreeItem):
            return True

        return self.to_dict() != other.to_dict()
