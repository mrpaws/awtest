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


class DeploymentByCriteriaModel1(object):
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
        'criteria_type': 'str',
        'app_criteria': 'AppCriteriaModel1_',
        'file_criteria': 'FileCriteriaModel1_',
        'registry_criteria': 'RegistryCriteriaModel1_',
        'logical_condition': 'str'
    }

    attribute_map = {
        'criteria_type': 'CriteriaType',
        'app_criteria': 'AppCriteria',
        'file_criteria': 'FileCriteria',
        'registry_criteria': 'RegistryCriteria',
        'logical_condition': 'LogicalCondition'
    }

    def __init__(self, criteria_type=None, app_criteria=None, file_criteria=None, registry_criteria=None, logical_condition=None, _configuration=None):  # noqa: E501
        """DeploymentByCriteriaModel1 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._criteria_type = None
        self._app_criteria = None
        self._file_criteria = None
        self._registry_criteria = None
        self._logical_condition = None
        self.discriminator = None

        if criteria_type is not None:
            self.criteria_type = criteria_type
        if app_criteria is not None:
            self.app_criteria = app_criteria
        if file_criteria is not None:
            self.file_criteria = file_criteria
        if registry_criteria is not None:
            self.registry_criteria = registry_criteria
        if logical_condition is not None:
            self.logical_condition = logical_condition

    @property
    def criteria_type(self):
        """Gets the criteria_type of this DeploymentByCriteriaModel1.  # noqa: E501

        Gets or sets criteria type. Supported values: AppExists = 1, AppDoesNotExist = 2, FileExists = 3, FileDoesNotExist = 4, RegistryExists = 5, RegistryDoesNotExist = 6.  # noqa: E501

        :return: The criteria_type of this DeploymentByCriteriaModel1.  # noqa: E501
        :rtype: str
        """
        return self._criteria_type

    @criteria_type.setter
    def criteria_type(self, criteria_type):
        """Sets the criteria_type of this DeploymentByCriteriaModel1.

        Gets or sets criteria type. Supported values: AppExists = 1, AppDoesNotExist = 2, FileExists = 3, FileDoesNotExist = 4, RegistryExists = 5, RegistryDoesNotExist = 6.  # noqa: E501

        :param criteria_type: The criteria_type of this DeploymentByCriteriaModel1.  # noqa: E501
        :type: str
        """

        self._criteria_type = criteria_type

    @property
    def app_criteria(self):
        """Gets the app_criteria of this DeploymentByCriteriaModel1.  # noqa: E501

        Gets or sets application criteria.  # noqa: E501

        :return: The app_criteria of this DeploymentByCriteriaModel1.  # noqa: E501
        :rtype: AppCriteriaModel1_
        """
        return self._app_criteria

    @app_criteria.setter
    def app_criteria(self, app_criteria):
        """Sets the app_criteria of this DeploymentByCriteriaModel1.

        Gets or sets application criteria.  # noqa: E501

        :param app_criteria: The app_criteria of this DeploymentByCriteriaModel1.  # noqa: E501
        :type: AppCriteriaModel1_
        """

        self._app_criteria = app_criteria

    @property
    def file_criteria(self):
        """Gets the file_criteria of this DeploymentByCriteriaModel1.  # noqa: E501

        Gets or sets file criteria.  # noqa: E501

        :return: The file_criteria of this DeploymentByCriteriaModel1.  # noqa: E501
        :rtype: FileCriteriaModel1_
        """
        return self._file_criteria

    @file_criteria.setter
    def file_criteria(self, file_criteria):
        """Sets the file_criteria of this DeploymentByCriteriaModel1.

        Gets or sets file criteria.  # noqa: E501

        :param file_criteria: The file_criteria of this DeploymentByCriteriaModel1.  # noqa: E501
        :type: FileCriteriaModel1_
        """

        self._file_criteria = file_criteria

    @property
    def registry_criteria(self):
        """Gets the registry_criteria of this DeploymentByCriteriaModel1.  # noqa: E501

        Gets or sets registry criteria.  # noqa: E501

        :return: The registry_criteria of this DeploymentByCriteriaModel1.  # noqa: E501
        :rtype: RegistryCriteriaModel1_
        """
        return self._registry_criteria

    @registry_criteria.setter
    def registry_criteria(self, registry_criteria):
        """Sets the registry_criteria of this DeploymentByCriteriaModel1.

        Gets or sets registry criteria.  # noqa: E501

        :param registry_criteria: The registry_criteria of this DeploymentByCriteriaModel1.  # noqa: E501
        :type: RegistryCriteriaModel1_
        """

        self._registry_criteria = registry_criteria

    @property
    def logical_condition(self):
        """Gets the logical_condition of this DeploymentByCriteriaModel1.  # noqa: E501

        Gets or sets logical condition. Supported values : End = 1, And = 2, Or = 3.  # noqa: E501

        :return: The logical_condition of this DeploymentByCriteriaModel1.  # noqa: E501
        :rtype: str
        """
        return self._logical_condition

    @logical_condition.setter
    def logical_condition(self, logical_condition):
        """Sets the logical_condition of this DeploymentByCriteriaModel1.

        Gets or sets logical condition. Supported values : End = 1, And = 2, Or = 3.  # noqa: E501

        :param logical_condition: The logical_condition of this DeploymentByCriteriaModel1.  # noqa: E501
        :type: str
        """

        self._logical_condition = logical_condition

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
        if issubclass(DeploymentByCriteriaModel1, dict):
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
        if not isinstance(other, DeploymentByCriteriaModel1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentByCriteriaModel1):
            return True

        return self.to_dict() != other.to_dict()
