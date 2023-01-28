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


class ApplicationDependencyModel(object):
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
        'application_dependency_id': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'application_dependency_id': 'ApplicationDependencyId'
    }

    def __init__(self, name=None, application_dependency_id=None, _configuration=None):  # noqa: E501
        """ApplicationDependencyModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._application_dependency_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if application_dependency_id is not None:
            self.application_dependency_id = application_dependency_id

    @property
    def name(self):
        """Gets the name of this ApplicationDependencyModel.  # noqa: E501

        Gets or sets name of the application.  # noqa: E501

        :return: The name of this ApplicationDependencyModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationDependencyModel.

        Gets or sets name of the application.  # noqa: E501

        :param name: The name of this ApplicationDependencyModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def application_dependency_id(self):
        """Gets the application_dependency_id of this ApplicationDependencyModel.  # noqa: E501

        Gets or sets application dependency Id.  # noqa: E501

        :return: The application_dependency_id of this ApplicationDependencyModel.  # noqa: E501
        :rtype: int
        """
        return self._application_dependency_id

    @application_dependency_id.setter
    def application_dependency_id(self, application_dependency_id):
        """Sets the application_dependency_id of this ApplicationDependencyModel.

        Gets or sets application dependency Id.  # noqa: E501

        :param application_dependency_id: The application_dependency_id of this ApplicationDependencyModel.  # noqa: E501
        :type: int
        """

        self._application_dependency_id = application_dependency_id

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
        if issubclass(ApplicationDependencyModel, dict):
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
        if not isinstance(other, ApplicationDependencyModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationDependencyModel):
            return True

        return self.to_dict() != other.to_dict()