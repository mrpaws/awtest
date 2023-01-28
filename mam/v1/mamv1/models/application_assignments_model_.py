# coding: utf-8

"""
    MAM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv1.configuration import Configuration


class ApplicationAssignmentsModel_(object):
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
        'smart_group_ids': 'list[int]',
        'smart_group_ids_for_deletion': 'list[int]',
        'excluded_smart_group_ids_for_deletion': 'list[int]',
        'deployment_parameters': 'ApplicationDeploymentParametersModel_',
        'uuid': 'str'
    }

    attribute_map = {
        'smart_group_ids': 'SmartGroupIds',
        'smart_group_ids_for_deletion': 'SmartGroupIdsForDeletion',
        'excluded_smart_group_ids_for_deletion': 'ExcludedSmartGroupIdsForDeletion',
        'deployment_parameters': 'DeploymentParameters',
        'uuid': 'uuid'
    }

    def __init__(self, smart_group_ids=None, smart_group_ids_for_deletion=None, excluded_smart_group_ids_for_deletion=None, deployment_parameters=None, uuid=None, _configuration=None):  # noqa: E501
        """ApplicationAssignmentsModel_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._smart_group_ids = None
        self._smart_group_ids_for_deletion = None
        self._excluded_smart_group_ids_for_deletion = None
        self._deployment_parameters = None
        self._uuid = None
        self.discriminator = None

        if smart_group_ids is not None:
            self.smart_group_ids = smart_group_ids
        if smart_group_ids_for_deletion is not None:
            self.smart_group_ids_for_deletion = smart_group_ids_for_deletion
        if excluded_smart_group_ids_for_deletion is not None:
            self.excluded_smart_group_ids_for_deletion = excluded_smart_group_ids_for_deletion
        if deployment_parameters is not None:
            self.deployment_parameters = deployment_parameters
        if uuid is not None:
            self.uuid = uuid

    @property
    def smart_group_ids(self):
        """Gets the smart_group_ids of this ApplicationAssignmentsModel_.  # noqa: E501

        Gets or sets array of smart group ids to be associated with the app.  # noqa: E501

        :return: The smart_group_ids of this ApplicationAssignmentsModel_.  # noqa: E501
        :rtype: list[int]
        """
        return self._smart_group_ids

    @smart_group_ids.setter
    def smart_group_ids(self, smart_group_ids):
        """Sets the smart_group_ids of this ApplicationAssignmentsModel_.

        Gets or sets array of smart group ids to be associated with the app.  # noqa: E501

        :param smart_group_ids: The smart_group_ids of this ApplicationAssignmentsModel_.  # noqa: E501
        :type: list[int]
        """

        self._smart_group_ids = smart_group_ids

    @property
    def smart_group_ids_for_deletion(self):
        """Gets the smart_group_ids_for_deletion of this ApplicationAssignmentsModel_.  # noqa: E501

        Gets or sets array of smart group ids to be deleted.  # noqa: E501

        :return: The smart_group_ids_for_deletion of this ApplicationAssignmentsModel_.  # noqa: E501
        :rtype: list[int]
        """
        return self._smart_group_ids_for_deletion

    @smart_group_ids_for_deletion.setter
    def smart_group_ids_for_deletion(self, smart_group_ids_for_deletion):
        """Sets the smart_group_ids_for_deletion of this ApplicationAssignmentsModel_.

        Gets or sets array of smart group ids to be deleted.  # noqa: E501

        :param smart_group_ids_for_deletion: The smart_group_ids_for_deletion of this ApplicationAssignmentsModel_.  # noqa: E501
        :type: list[int]
        """

        self._smart_group_ids_for_deletion = smart_group_ids_for_deletion

    @property
    def excluded_smart_group_ids_for_deletion(self):
        """Gets the excluded_smart_group_ids_for_deletion of this ApplicationAssignmentsModel_.  # noqa: E501

        Gets or sets array of the already excluded smart group Ids to be removed.  # noqa: E501

        :return: The excluded_smart_group_ids_for_deletion of this ApplicationAssignmentsModel_.  # noqa: E501
        :rtype: list[int]
        """
        return self._excluded_smart_group_ids_for_deletion

    @excluded_smart_group_ids_for_deletion.setter
    def excluded_smart_group_ids_for_deletion(self, excluded_smart_group_ids_for_deletion):
        """Sets the excluded_smart_group_ids_for_deletion of this ApplicationAssignmentsModel_.

        Gets or sets array of the already excluded smart group Ids to be removed.  # noqa: E501

        :param excluded_smart_group_ids_for_deletion: The excluded_smart_group_ids_for_deletion of this ApplicationAssignmentsModel_.  # noqa: E501
        :type: list[int]
        """

        self._excluded_smart_group_ids_for_deletion = excluded_smart_group_ids_for_deletion

    @property
    def deployment_parameters(self):
        """Gets the deployment_parameters of this ApplicationAssignmentsModel_.  # noqa: E501

        Gets or sets application deployment parameters.  # noqa: E501

        :return: The deployment_parameters of this ApplicationAssignmentsModel_.  # noqa: E501
        :rtype: ApplicationDeploymentParametersModel_
        """
        return self._deployment_parameters

    @deployment_parameters.setter
    def deployment_parameters(self, deployment_parameters):
        """Sets the deployment_parameters of this ApplicationAssignmentsModel_.

        Gets or sets application deployment parameters.  # noqa: E501

        :param deployment_parameters: The deployment_parameters of this ApplicationAssignmentsModel_.  # noqa: E501
        :type: ApplicationDeploymentParametersModel_
        """

        self._deployment_parameters = deployment_parameters

    @property
    def uuid(self):
        """Gets the uuid of this ApplicationAssignmentsModel_.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this ApplicationAssignmentsModel_.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ApplicationAssignmentsModel_.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this ApplicationAssignmentsModel_.  # noqa: E501
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
        if issubclass(ApplicationAssignmentsModel_, dict):
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
        if not isinstance(other, ApplicationAssignmentsModel_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationAssignmentsModel_):
            return True

        return self.to_dict() != other.to_dict()
