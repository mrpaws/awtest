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


class OSVersionV1Model(object):
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
        'version': 'str',
        'name': 'str',
        'levels': 'list[SecurityLevelV1Model]'
    }

    attribute_map = {
        'id': 'id',
        'uuid': 'uuid',
        'version': 'version',
        'name': 'name',
        'levels': 'levels'
    }

    def __init__(self, id=None, uuid=None, version=None, name=None, levels=None, _configuration=None):  # noqa: E501
        """OSVersionV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._uuid = None
        self._version = None
        self._name = None
        self._levels = None
        self.discriminator = None

        self.id = id
        if uuid is not None:
            self.uuid = uuid
        self.version = version
        self.name = name
        if levels is not None:
            self.levels = levels

    @property
    def id(self):
        """Gets the id of this OSVersionV1Model.  # noqa: E501

        Unique identifier for the windows version  # noqa: E501

        :return: The id of this OSVersionV1Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OSVersionV1Model.

        Unique identifier for the windows version  # noqa: E501

        :param id: The id of this OSVersionV1Model.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this OSVersionV1Model.  # noqa: E501

        Unique identifier of the operating system version  # noqa: E501

        :return: The uuid of this OSVersionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this OSVersionV1Model.

        Unique identifier of the operating system version  # noqa: E501

        :param uuid: The uuid of this OSVersionV1Model.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def version(self):
        """Gets the version of this OSVersionV1Model.  # noqa: E501

        The Windows Version  # noqa: E501

        :return: The version of this OSVersionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OSVersionV1Model.

        The Windows Version  # noqa: E501

        :param version: The version of this OSVersionV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def name(self):
        """Gets the name of this OSVersionV1Model.  # noqa: E501

        The Windows Version display name  # noqa: E501

        :return: The name of this OSVersionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OSVersionV1Model.

        The Windows Version display name  # noqa: E501

        :param name: The name of this OSVersionV1Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def levels(self):
        """Gets the levels of this OSVersionV1Model.  # noqa: E501

        The various security levels available for this windows version of the security baseline  # noqa: E501

        :return: The levels of this OSVersionV1Model.  # noqa: E501
        :rtype: list[SecurityLevelV1Model]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this OSVersionV1Model.

        The various security levels available for this windows version of the security baseline  # noqa: E501

        :param levels: The levels of this OSVersionV1Model.  # noqa: E501
        :type: list[SecurityLevelV1Model]
        """

        self._levels = levels

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
        if issubclass(OSVersionV1Model, dict):
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
        if not isinstance(other, OSVersionV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OSVersionV1Model):
            return True

        return self.to_dict() != other.to_dict()