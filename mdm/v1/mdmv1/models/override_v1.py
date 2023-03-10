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


class OverrideV1(object):
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
        'resource_type': 'str',
        'status': 'str',
        'override_type': 'str',
        'override_id': 'int',
        'user_uuid': 'str',
        'device_uuid': 'str',
        'resource_uuid': 'str',
        'action_type_legacy': 'int',
        'action_type': 'str',
        'target': 'str',
        'source': 'str',
        'source_info': 'SourceInfoV1',
        'policy': 'ResourcePolicyV1',
        'meta_data': 'str',
        'version': 'str',
        'created_time': 'datetime',
        'last_modified_time': 'datetime'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'status': 'status',
        'override_type': 'override_type',
        'override_id': 'override_id',
        'user_uuid': 'user_uuid',
        'device_uuid': 'device_uuid',
        'resource_uuid': 'resource_uuid',
        'action_type_legacy': 'action_type_legacy',
        'action_type': 'action_type',
        'target': 'target',
        'source': 'source',
        'source_info': 'source_info',
        'policy': 'policy',
        'meta_data': 'meta_data',
        'version': 'version',
        'created_time': 'created_time',
        'last_modified_time': 'last_modified_time'
    }

    def __init__(self, resource_type=None, status=None, override_type=None, override_id=None, user_uuid=None, device_uuid=None, resource_uuid=None, action_type_legacy=None, action_type=None, target=None, source=None, source_info=None, policy=None, meta_data=None, version=None, created_time=None, last_modified_time=None, _configuration=None):  # noqa: E501
        """OverrideV1 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_type = None
        self._status = None
        self._override_type = None
        self._override_id = None
        self._user_uuid = None
        self._device_uuid = None
        self._resource_uuid = None
        self._action_type_legacy = None
        self._action_type = None
        self._target = None
        self._source = None
        self._source_info = None
        self._policy = None
        self._meta_data = None
        self._version = None
        self._created_time = None
        self._last_modified_time = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if status is not None:
            self.status = status
        if override_type is not None:
            self.override_type = override_type
        if override_id is not None:
            self.override_id = override_id
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if device_uuid is not None:
            self.device_uuid = device_uuid
        if resource_uuid is not None:
            self.resource_uuid = resource_uuid
        if action_type_legacy is not None:
            self.action_type_legacy = action_type_legacy
        if action_type is not None:
            self.action_type = action_type
        if target is not None:
            self.target = target
        if source is not None:
            self.source = source
        if source_info is not None:
            self.source_info = source_info
        if policy is not None:
            self.policy = policy
        if meta_data is not None:
            self.meta_data = meta_data
        if version is not None:
            self.version = version
        if created_time is not None:
            self.created_time = created_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time

    @property
    def resource_type(self):
        """Gets the resource_type of this OverrideV1.  # noqa: E501


        :return: The resource_type of this OverrideV1.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this OverrideV1.


        :param resource_type: The resource_type of this OverrideV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "APPS", "WORKFLOWS", "PROFILES", "TIME_WINDOW", "SCRIPTS", "SENSORS", "PROVISIONING_PRODUCT", "UPDATE_POLICY", "OSUPDATE", "BOOKS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                resource_type not in allowed_values):
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def status(self):
        """Gets the status of this OverrideV1.  # noqa: E501


        :return: The status of this OverrideV1.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OverrideV1.


        :param status: The status of this OverrideV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "PENDING", "COMPLETED", "FAILED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def override_type(self):
        """Gets the override_type of this OverrideV1.  # noqa: E501


        :return: The override_type of this OverrideV1.  # noqa: E501
        :rtype: str
        """
        return self._override_type

    @override_type.setter
    def override_type(self, override_type):
        """Sets the override_type of this OverrideV1.


        :param override_type: The override_type of this OverrideV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["ONE_TIME", "PERMANENT", "ONETIME_PERSISTABLE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                override_type not in allowed_values):
            raise ValueError(
                "Invalid value for `override_type` ({0}), must be one of {1}"  # noqa: E501
                .format(override_type, allowed_values)
            )

        self._override_type = override_type

    @property
    def override_id(self):
        """Gets the override_id of this OverrideV1.  # noqa: E501


        :return: The override_id of this OverrideV1.  # noqa: E501
        :rtype: int
        """
        return self._override_id

    @override_id.setter
    def override_id(self, override_id):
        """Sets the override_id of this OverrideV1.


        :param override_id: The override_id of this OverrideV1.  # noqa: E501
        :type: int
        """

        self._override_id = override_id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this OverrideV1.  # noqa: E501


        :return: The user_uuid of this OverrideV1.  # noqa: E501
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this OverrideV1.


        :param user_uuid: The user_uuid of this OverrideV1.  # noqa: E501
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def device_uuid(self):
        """Gets the device_uuid of this OverrideV1.  # noqa: E501


        :return: The device_uuid of this OverrideV1.  # noqa: E501
        :rtype: str
        """
        return self._device_uuid

    @device_uuid.setter
    def device_uuid(self, device_uuid):
        """Sets the device_uuid of this OverrideV1.


        :param device_uuid: The device_uuid of this OverrideV1.  # noqa: E501
        :type: str
        """

        self._device_uuid = device_uuid

    @property
    def resource_uuid(self):
        """Gets the resource_uuid of this OverrideV1.  # noqa: E501


        :return: The resource_uuid of this OverrideV1.  # noqa: E501
        :rtype: str
        """
        return self._resource_uuid

    @resource_uuid.setter
    def resource_uuid(self, resource_uuid):
        """Sets the resource_uuid of this OverrideV1.


        :param resource_uuid: The resource_uuid of this OverrideV1.  # noqa: E501
        :type: str
        """

        self._resource_uuid = resource_uuid

    @property
    def action_type_legacy(self):
        """Gets the action_type_legacy of this OverrideV1.  # noqa: E501


        :return: The action_type_legacy of this OverrideV1.  # noqa: E501
        :rtype: int
        """
        return self._action_type_legacy

    @action_type_legacy.setter
    def action_type_legacy(self, action_type_legacy):
        """Sets the action_type_legacy of this OverrideV1.


        :param action_type_legacy: The action_type_legacy of this OverrideV1.  # noqa: E501
        :type: int
        """

        self._action_type_legacy = action_type_legacy

    @property
    def action_type(self):
        """Gets the action_type of this OverrideV1.  # noqa: E501


        :return: The action_type of this OverrideV1.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this OverrideV1.


        :param action_type: The action_type of this OverrideV1.  # noqa: E501
        :type: str
        """

        self._action_type = action_type

    @property
    def target(self):
        """Gets the target of this OverrideV1.  # noqa: E501


        :return: The target of this OverrideV1.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this OverrideV1.


        :param target: The target of this OverrideV1.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def source(self):
        """Gets the source of this OverrideV1.  # noqa: E501


        :return: The source of this OverrideV1.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this OverrideV1.


        :param source: The source of this OverrideV1.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def source_info(self):
        """Gets the source_info of this OverrideV1.  # noqa: E501


        :return: The source_info of this OverrideV1.  # noqa: E501
        :rtype: SourceInfoV1
        """
        return self._source_info

    @source_info.setter
    def source_info(self, source_info):
        """Sets the source_info of this OverrideV1.


        :param source_info: The source_info of this OverrideV1.  # noqa: E501
        :type: SourceInfoV1
        """

        self._source_info = source_info

    @property
    def policy(self):
        """Gets the policy of this OverrideV1.  # noqa: E501


        :return: The policy of this OverrideV1.  # noqa: E501
        :rtype: ResourcePolicyV1
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this OverrideV1.


        :param policy: The policy of this OverrideV1.  # noqa: E501
        :type: ResourcePolicyV1
        """

        self._policy = policy

    @property
    def meta_data(self):
        """Gets the meta_data of this OverrideV1.  # noqa: E501


        :return: The meta_data of this OverrideV1.  # noqa: E501
        :rtype: str
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this OverrideV1.


        :param meta_data: The meta_data of this OverrideV1.  # noqa: E501
        :type: str
        """

        self._meta_data = meta_data

    @property
    def version(self):
        """Gets the version of this OverrideV1.  # noqa: E501


        :return: The version of this OverrideV1.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OverrideV1.


        :param version: The version of this OverrideV1.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def created_time(self):
        """Gets the created_time of this OverrideV1.  # noqa: E501


        :return: The created_time of this OverrideV1.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this OverrideV1.


        :param created_time: The created_time of this OverrideV1.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this OverrideV1.  # noqa: E501


        :return: The last_modified_time of this OverrideV1.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this OverrideV1.


        :param last_modified_time: The last_modified_time of this OverrideV1.  # noqa: E501
        :type: datetime
        """

        self._last_modified_time = last_modified_time

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
        if issubclass(OverrideV1, dict):
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
        if not isinstance(other, OverrideV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OverrideV1):
            return True

        return self.to_dict() != other.to_dict()
