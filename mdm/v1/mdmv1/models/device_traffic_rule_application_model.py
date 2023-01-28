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


class DeviceTrafficRuleApplicationModel(object):
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
        'bundle_id': 'str',
        'application_id': 'str',
        'type': 'str',
        'friendly_name': 'str'
    }

    attribute_map = {
        'bundle_id': 'bundle_id',
        'application_id': 'application_id',
        'type': 'type',
        'friendly_name': 'friendly_name'
    }

    def __init__(self, bundle_id=None, application_id=None, type=None, friendly_name=None, _configuration=None):  # noqa: E501
        """DeviceTrafficRuleApplicationModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bundle_id = None
        self._application_id = None
        self._type = None
        self._friendly_name = None
        self.discriminator = None

        if bundle_id is not None:
            self.bundle_id = bundle_id
        if application_id is not None:
            self.application_id = application_id
        if type is not None:
            self.type = type
        if friendly_name is not None:
            self.friendly_name = friendly_name

    @property
    def bundle_id(self):
        """Gets the bundle_id of this DeviceTrafficRuleApplicationModel.  # noqa: E501

        The application bundle id.  # noqa: E501

        :return: The bundle_id of this DeviceTrafficRuleApplicationModel.  # noqa: E501
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this DeviceTrafficRuleApplicationModel.

        The application bundle id.  # noqa: E501

        :param bundle_id: The bundle_id of this DeviceTrafficRuleApplicationModel.  # noqa: E501
        :type: str
        """

        self._bundle_id = bundle_id

    @property
    def application_id(self):
        """Gets the application_id of this DeviceTrafficRuleApplicationModel.  # noqa: E501

        The application uuid.  # noqa: E501

        :return: The application_id of this DeviceTrafficRuleApplicationModel.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this DeviceTrafficRuleApplicationModel.

        The application uuid.  # noqa: E501

        :param application_id: The application_id of this DeviceTrafficRuleApplicationModel.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def type(self):
        """Gets the type of this DeviceTrafficRuleApplicationModel.  # noqa: E501

        The application type.  # noqa: E501

        :return: The type of this DeviceTrafficRuleApplicationModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceTrafficRuleApplicationModel.

        The application type.  # noqa: E501

        :param type: The type of this DeviceTrafficRuleApplicationModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["INTERNAL", "PUBLIC", "UNKNOWN"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def friendly_name(self):
        """Gets the friendly_name of this DeviceTrafficRuleApplicationModel.  # noqa: E501

        The friendly name of the application.  # noqa: E501

        :return: The friendly_name of this DeviceTrafficRuleApplicationModel.  # noqa: E501
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this DeviceTrafficRuleApplicationModel.

        The friendly name of the application.  # noqa: E501

        :param friendly_name: The friendly_name of this DeviceTrafficRuleApplicationModel.  # noqa: E501
        :type: str
        """

        self._friendly_name = friendly_name

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
        if issubclass(DeviceTrafficRuleApplicationModel, dict):
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
        if not isinstance(other, DeviceTrafficRuleApplicationModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceTrafficRuleApplicationModel):
            return True

        return self.to_dict() != other.to_dict()
