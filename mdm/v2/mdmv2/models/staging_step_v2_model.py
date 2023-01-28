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


class StagingStepV2Model(object):
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
        'execution_task_name': 'str',
        'profile_uuid': 'str',
        'profile_name': 'str',
        'application_uuid': 'str',
        'application_name': 'str',
        'file_actions_uuid': 'str',
        'file_actions_name': 'str',
        'event_action_uuid': 'str',
        'event_action_name': 'str',
        'persist_through_enterprise_reset': 'str',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'execution_task_name': 'execution_task_name',
        'profile_uuid': 'profile_uuid',
        'profile_name': 'profile_name',
        'application_uuid': 'application_uuid',
        'application_name': 'application_name',
        'file_actions_uuid': 'file_actions_uuid',
        'file_actions_name': 'file_actions_name',
        'event_action_uuid': 'event_action_uuid',
        'event_action_name': 'event_action_name',
        'persist_through_enterprise_reset': 'persist_through_enterprise_reset',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, execution_task_name=None, profile_uuid=None, profile_name=None, application_uuid=None, application_name=None, file_actions_uuid=None, file_actions_name=None, event_action_uuid=None, event_action_name=None, persist_through_enterprise_reset=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """StagingStepV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._execution_task_name = None
        self._profile_uuid = None
        self._profile_name = None
        self._application_uuid = None
        self._application_name = None
        self._file_actions_uuid = None
        self._file_actions_name = None
        self._event_action_uuid = None
        self._event_action_name = None
        self._persist_through_enterprise_reset = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if execution_task_name is not None:
            self.execution_task_name = execution_task_name
        if profile_uuid is not None:
            self.profile_uuid = profile_uuid
        if profile_name is not None:
            self.profile_name = profile_name
        if application_uuid is not None:
            self.application_uuid = application_uuid
        if application_name is not None:
            self.application_name = application_name
        if file_actions_uuid is not None:
            self.file_actions_uuid = file_actions_uuid
        if file_actions_name is not None:
            self.file_actions_name = file_actions_name
        if event_action_uuid is not None:
            self.event_action_uuid = event_action_uuid
        if event_action_name is not None:
            self.event_action_name = event_action_name
        if persist_through_enterprise_reset is not None:
            self.persist_through_enterprise_reset = persist_through_enterprise_reset
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def execution_task_name(self):
        """Gets the execution_task_name of this StagingStepV2Model.  # noqa: E501

        The execution task which is to be performed for staging  # noqa: E501

        :return: The execution_task_name of this StagingStepV2Model.  # noqa: E501
        :rtype: str
        """
        return self._execution_task_name

    @execution_task_name.setter
    def execution_task_name(self, execution_task_name):
        """Sets the execution_task_name of this StagingStepV2Model.

        The execution task which is to be performed for staging  # noqa: E501

        :param execution_task_name: The execution_task_name of this StagingStepV2Model.  # noqa: E501
        :type: str
        """

        self._execution_task_name = execution_task_name

    @property
    def profile_uuid(self):
        """Gets the profile_uuid of this StagingStepV2Model.  # noqa: E501

        The profile uuid for staging  # noqa: E501

        :return: The profile_uuid of this StagingStepV2Model.  # noqa: E501
        :rtype: str
        """
        return self._profile_uuid

    @profile_uuid.setter
    def profile_uuid(self, profile_uuid):
        """Sets the profile_uuid of this StagingStepV2Model.

        The profile uuid for staging  # noqa: E501

        :param profile_uuid: The profile_uuid of this StagingStepV2Model.  # noqa: E501
        :type: str
        """

        self._profile_uuid = profile_uuid

    @property
    def profile_name(self):
        """Gets the profile_name of this StagingStepV2Model.  # noqa: E501

        The profile name for staging  # noqa: E501

        :return: The profile_name of this StagingStepV2Model.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this StagingStepV2Model.

        The profile name for staging  # noqa: E501

        :param profile_name: The profile_name of this StagingStepV2Model.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    @property
    def application_uuid(self):
        """Gets the application_uuid of this StagingStepV2Model.  # noqa: E501

        The application uuid for staging  # noqa: E501

        :return: The application_uuid of this StagingStepV2Model.  # noqa: E501
        :rtype: str
        """
        return self._application_uuid

    @application_uuid.setter
    def application_uuid(self, application_uuid):
        """Sets the application_uuid of this StagingStepV2Model.

        The application uuid for staging  # noqa: E501

        :param application_uuid: The application_uuid of this StagingStepV2Model.  # noqa: E501
        :type: str
        """

        self._application_uuid = application_uuid

    @property
    def application_name(self):
        """Gets the application_name of this StagingStepV2Model.  # noqa: E501

        The application name for staging  # noqa: E501

        :return: The application_name of this StagingStepV2Model.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this StagingStepV2Model.

        The application name for staging  # noqa: E501

        :param application_name: The application_name of this StagingStepV2Model.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def file_actions_uuid(self):
        """Gets the file_actions_uuid of this StagingStepV2Model.  # noqa: E501

        The file action uuid for staging  # noqa: E501

        :return: The file_actions_uuid of this StagingStepV2Model.  # noqa: E501
        :rtype: str
        """
        return self._file_actions_uuid

    @file_actions_uuid.setter
    def file_actions_uuid(self, file_actions_uuid):
        """Sets the file_actions_uuid of this StagingStepV2Model.

        The file action uuid for staging  # noqa: E501

        :param file_actions_uuid: The file_actions_uuid of this StagingStepV2Model.  # noqa: E501
        :type: str
        """

        self._file_actions_uuid = file_actions_uuid

    @property
    def file_actions_name(self):
        """Gets the file_actions_name of this StagingStepV2Model.  # noqa: E501

        The file action name for staging  # noqa: E501

        :return: The file_actions_name of this StagingStepV2Model.  # noqa: E501
        :rtype: str
        """
        return self._file_actions_name

    @file_actions_name.setter
    def file_actions_name(self, file_actions_name):
        """Sets the file_actions_name of this StagingStepV2Model.

        The file action name for staging  # noqa: E501

        :param file_actions_name: The file_actions_name of this StagingStepV2Model.  # noqa: E501
        :type: str
        """

        self._file_actions_name = file_actions_name

    @property
    def event_action_uuid(self):
        """Gets the event_action_uuid of this StagingStepV2Model.  # noqa: E501

        The event action uuid for the staging  # noqa: E501

        :return: The event_action_uuid of this StagingStepV2Model.  # noqa: E501
        :rtype: str
        """
        return self._event_action_uuid

    @event_action_uuid.setter
    def event_action_uuid(self, event_action_uuid):
        """Sets the event_action_uuid of this StagingStepV2Model.

        The event action uuid for the staging  # noqa: E501

        :param event_action_uuid: The event_action_uuid of this StagingStepV2Model.  # noqa: E501
        :type: str
        """

        self._event_action_uuid = event_action_uuid

    @property
    def event_action_name(self):
        """Gets the event_action_name of this StagingStepV2Model.  # noqa: E501

        The event action name for the staging  # noqa: E501

        :return: The event_action_name of this StagingStepV2Model.  # noqa: E501
        :rtype: str
        """
        return self._event_action_name

    @event_action_name.setter
    def event_action_name(self, event_action_name):
        """Sets the event_action_name of this StagingStepV2Model.

        The event action name for the staging  # noqa: E501

        :param event_action_name: The event_action_name of this StagingStepV2Model.  # noqa: E501
        :type: str
        """

        self._event_action_name = event_action_name

    @property
    def persist_through_enterprise_reset(self):
        """Gets the persist_through_enterprise_reset of this StagingStepV2Model.  # noqa: E501

        Whether Persist through enterprise reset is allowed or not.  # noqa: E501

        :return: The persist_through_enterprise_reset of this StagingStepV2Model.  # noqa: E501
        :rtype: str
        """
        return self._persist_through_enterprise_reset

    @persist_through_enterprise_reset.setter
    def persist_through_enterprise_reset(self, persist_through_enterprise_reset):
        """Sets the persist_through_enterprise_reset of this StagingStepV2Model.

        Whether Persist through enterprise reset is allowed or not.  # noqa: E501

        :param persist_through_enterprise_reset: The persist_through_enterprise_reset of this StagingStepV2Model.  # noqa: E501
        :type: str
        """

        self._persist_through_enterprise_reset = persist_through_enterprise_reset

    @property
    def id(self):
        """Gets the id of this StagingStepV2Model.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this StagingStepV2Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StagingStepV2Model.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this StagingStepV2Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this StagingStepV2Model.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this StagingStepV2Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this StagingStepV2Model.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this StagingStepV2Model.  # noqa: E501
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
        if issubclass(StagingStepV2Model, dict):
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
        if not isinstance(other, StagingStepV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagingStepV2Model):
            return True

        return self.to_dict() != other.to_dict()