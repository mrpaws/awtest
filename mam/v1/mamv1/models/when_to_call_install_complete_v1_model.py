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


class WhenToCallInstallCompleteV1Model(object):
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
        'use_additional_criteria': 'bool',
        'identify_application_by': 'int',
        'criteria_list': 'list[DeploymentByCriteriaV1Model_]',
        'custom_script': 'DeploymentByCustomScriptV1Model'
    }

    attribute_map = {
        'use_additional_criteria': 'use_additional_criteria',
        'identify_application_by': 'identify_application_by',
        'criteria_list': 'criteria_list',
        'custom_script': 'custom_script'
    }

    def __init__(self, use_additional_criteria=None, identify_application_by=None, criteria_list=None, custom_script=None, _configuration=None):  # noqa: E501
        """WhenToCallInstallCompleteV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._use_additional_criteria = None
        self._identify_application_by = None
        self._criteria_list = None
        self._custom_script = None
        self.discriminator = None

        if use_additional_criteria is not None:
            self.use_additional_criteria = use_additional_criteria
        if identify_application_by is not None:
            self.identify_application_by = identify_application_by
        if criteria_list is not None:
            self.criteria_list = criteria_list
        if custom_script is not None:
            self.custom_script = custom_script

    @property
    def use_additional_criteria(self):
        """Gets the use_additional_criteria of this WhenToCallInstallCompleteV1Model.  # noqa: E501

        Gets or sets a value indicating whether value indicating whether additional criteria has to be used or not.  # noqa: E501

        :return: The use_additional_criteria of this WhenToCallInstallCompleteV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._use_additional_criteria

    @use_additional_criteria.setter
    def use_additional_criteria(self, use_additional_criteria):
        """Sets the use_additional_criteria of this WhenToCallInstallCompleteV1Model.

        Gets or sets a value indicating whether value indicating whether additional criteria has to be used or not.  # noqa: E501

        :param use_additional_criteria: The use_additional_criteria of this WhenToCallInstallCompleteV1Model.  # noqa: E501
        :type: bool
        """

        self._use_additional_criteria = use_additional_criteria

    @property
    def identify_application_by(self):
        """Gets the identify_application_by of this WhenToCallInstallCompleteV1Model.  # noqa: E501

        Gets or sets the way by which an application can be identified (Supported Values: DefiningCriteria = 1, UsingCustomScript = 2).  # noqa: E501

        :return: The identify_application_by of this WhenToCallInstallCompleteV1Model.  # noqa: E501
        :rtype: int
        """
        return self._identify_application_by

    @identify_application_by.setter
    def identify_application_by(self, identify_application_by):
        """Sets the identify_application_by of this WhenToCallInstallCompleteV1Model.

        Gets or sets the way by which an application can be identified (Supported Values: DefiningCriteria = 1, UsingCustomScript = 2).  # noqa: E501

        :param identify_application_by: The identify_application_by of this WhenToCallInstallCompleteV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if (self._configuration.client_side_validation and
                identify_application_by not in allowed_values):
            raise ValueError(
                "Invalid value for `identify_application_by` ({0}), must be one of {1}"  # noqa: E501
                .format(identify_application_by, allowed_values)
            )

        self._identify_application_by = identify_application_by

    @property
    def criteria_list(self):
        """Gets the criteria_list of this WhenToCallInstallCompleteV1Model.  # noqa: E501

        Gets or sets the criteria configured to identify application.  # noqa: E501

        :return: The criteria_list of this WhenToCallInstallCompleteV1Model.  # noqa: E501
        :rtype: list[DeploymentByCriteriaV1Model_]
        """
        return self._criteria_list

    @criteria_list.setter
    def criteria_list(self, criteria_list):
        """Sets the criteria_list of this WhenToCallInstallCompleteV1Model.

        Gets or sets the criteria configured to identify application.  # noqa: E501

        :param criteria_list: The criteria_list of this WhenToCallInstallCompleteV1Model.  # noqa: E501
        :type: list[DeploymentByCriteriaV1Model_]
        """

        self._criteria_list = criteria_list

    @property
    def custom_script(self):
        """Gets the custom_script of this WhenToCallInstallCompleteV1Model.  # noqa: E501

        Gets or sets the custom script configured to identify application.  # noqa: E501

        :return: The custom_script of this WhenToCallInstallCompleteV1Model.  # noqa: E501
        :rtype: DeploymentByCustomScriptV1Model
        """
        return self._custom_script

    @custom_script.setter
    def custom_script(self, custom_script):
        """Sets the custom_script of this WhenToCallInstallCompleteV1Model.

        Gets or sets the custom script configured to identify application.  # noqa: E501

        :param custom_script: The custom_script of this WhenToCallInstallCompleteV1Model.  # noqa: E501
        :type: DeploymentByCustomScriptV1Model
        """

        self._custom_script = custom_script

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
        if issubclass(WhenToCallInstallCompleteV1Model, dict):
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
        if not isinstance(other, WhenToCallInstallCompleteV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WhenToCallInstallCompleteV1Model):
            return True

        return self.to_dict() != other.to_dict()
