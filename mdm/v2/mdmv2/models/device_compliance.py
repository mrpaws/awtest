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


class DeviceCompliance(object):
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
        'compliant_status': 'bool',
        'policy_name': 'str',
        'policy_detail': 'str',
        'last_compliance_check': 'datetime',
        'next_compliance_check': 'datetime',
        'action_taken': 'list[ComplianceActionTaken]',
        'id': 'EntityId_',
        'uuid': 'str'
    }

    attribute_map = {
        'compliant_status': 'CompliantStatus',
        'policy_name': 'PolicyName',
        'policy_detail': 'PolicyDetail',
        'last_compliance_check': 'LastComplianceCheck',
        'next_compliance_check': 'NextComplianceCheck',
        'action_taken': 'ActionTaken',
        'id': 'Id',
        'uuid': 'Uuid'
    }

    def __init__(self, compliant_status=None, policy_name=None, policy_detail=None, last_compliance_check=None, next_compliance_check=None, action_taken=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """DeviceCompliance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._compliant_status = None
        self._policy_name = None
        self._policy_detail = None
        self._last_compliance_check = None
        self._next_compliance_check = None
        self._action_taken = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if compliant_status is not None:
            self.compliant_status = compliant_status
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_detail is not None:
            self.policy_detail = policy_detail
        if last_compliance_check is not None:
            self.last_compliance_check = last_compliance_check
        if next_compliance_check is not None:
            self.next_compliance_check = next_compliance_check
        if action_taken is not None:
            self.action_taken = action_taken
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def compliant_status(self):
        """Gets the compliant_status of this DeviceCompliance.  # noqa: E501

        Gets or sets a value indicating whether compliance status of the device.  # noqa: E501

        :return: The compliant_status of this DeviceCompliance.  # noqa: E501
        :rtype: bool
        """
        return self._compliant_status

    @compliant_status.setter
    def compliant_status(self, compliant_status):
        """Sets the compliant_status of this DeviceCompliance.

        Gets or sets a value indicating whether compliance status of the device.  # noqa: E501

        :param compliant_status: The compliant_status of this DeviceCompliance.  # noqa: E501
        :type: bool
        """

        self._compliant_status = compliant_status

    @property
    def policy_name(self):
        """Gets the policy_name of this DeviceCompliance.  # noqa: E501

        Gets or sets policy name.  # noqa: E501

        :return: The policy_name of this DeviceCompliance.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this DeviceCompliance.

        Gets or sets policy name.  # noqa: E501

        :param policy_name: The policy_name of this DeviceCompliance.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def policy_detail(self):
        """Gets the policy_detail of this DeviceCompliance.  # noqa: E501

        Gets or sets policy details.  # noqa: E501

        :return: The policy_detail of this DeviceCompliance.  # noqa: E501
        :rtype: str
        """
        return self._policy_detail

    @policy_detail.setter
    def policy_detail(self, policy_detail):
        """Sets the policy_detail of this DeviceCompliance.

        Gets or sets policy details.  # noqa: E501

        :param policy_detail: The policy_detail of this DeviceCompliance.  # noqa: E501
        :type: str
        """

        self._policy_detail = policy_detail

    @property
    def last_compliance_check(self):
        """Gets the last_compliance_check of this DeviceCompliance.  # noqa: E501

        Gets or sets last compliance check.  # noqa: E501

        :return: The last_compliance_check of this DeviceCompliance.  # noqa: E501
        :rtype: datetime
        """
        return self._last_compliance_check

    @last_compliance_check.setter
    def last_compliance_check(self, last_compliance_check):
        """Sets the last_compliance_check of this DeviceCompliance.

        Gets or sets last compliance check.  # noqa: E501

        :param last_compliance_check: The last_compliance_check of this DeviceCompliance.  # noqa: E501
        :type: datetime
        """

        self._last_compliance_check = last_compliance_check

    @property
    def next_compliance_check(self):
        """Gets the next_compliance_check of this DeviceCompliance.  # noqa: E501

        Gets or sets next compliance check.  # noqa: E501

        :return: The next_compliance_check of this DeviceCompliance.  # noqa: E501
        :rtype: datetime
        """
        return self._next_compliance_check

    @next_compliance_check.setter
    def next_compliance_check(self, next_compliance_check):
        """Sets the next_compliance_check of this DeviceCompliance.

        Gets or sets next compliance check.  # noqa: E501

        :param next_compliance_check: The next_compliance_check of this DeviceCompliance.  # noqa: E501
        :type: datetime
        """

        self._next_compliance_check = next_compliance_check

    @property
    def action_taken(self):
        """Gets the action_taken of this DeviceCompliance.  # noqa: E501

        Gets or sets compliance action.  # noqa: E501

        :return: The action_taken of this DeviceCompliance.  # noqa: E501
        :rtype: list[ComplianceActionTaken]
        """
        return self._action_taken

    @action_taken.setter
    def action_taken(self, action_taken):
        """Sets the action_taken of this DeviceCompliance.

        Gets or sets compliance action.  # noqa: E501

        :param action_taken: The action_taken of this DeviceCompliance.  # noqa: E501
        :type: list[ComplianceActionTaken]
        """

        self._action_taken = action_taken

    @property
    def id(self):
        """Gets the id of this DeviceCompliance.  # noqa: E501


        :return: The id of this DeviceCompliance.  # noqa: E501
        :rtype: EntityId_
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceCompliance.


        :param id: The id of this DeviceCompliance.  # noqa: E501
        :type: EntityId_
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this DeviceCompliance.  # noqa: E501


        :return: The uuid of this DeviceCompliance.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DeviceCompliance.


        :param uuid: The uuid of this DeviceCompliance.  # noqa: E501
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
        if issubclass(DeviceCompliance, dict):
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
        if not isinstance(other, DeviceCompliance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceCompliance):
            return True

        return self.to_dict() != other.to_dict()
