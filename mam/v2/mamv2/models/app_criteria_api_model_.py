# coding: utf-8

"""
    MAM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv2.configuration import Configuration


class AppCriteriaApiModel_(object):
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
        'application_identifier': 'str',
        'version_condition': 'str',
        'major_version': 'int',
        'minor_version': 'int',
        'revision_number': 'int',
        'build_number': 'int'
    }

    attribute_map = {
        'application_identifier': 'ApplicationIdentifier',
        'version_condition': 'VersionCondition',
        'major_version': 'MajorVersion',
        'minor_version': 'MinorVersion',
        'revision_number': 'RevisionNumber',
        'build_number': 'BuildNumber'
    }

    def __init__(self, application_identifier=None, version_condition=None, major_version=None, minor_version=None, revision_number=None, build_number=None, _configuration=None):  # noqa: E501
        """AppCriteriaApiModel_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_identifier = None
        self._version_condition = None
        self._major_version = None
        self._minor_version = None
        self._revision_number = None
        self._build_number = None
        self.discriminator = None

        if application_identifier is not None:
            self.application_identifier = application_identifier
        if version_condition is not None:
            self.version_condition = version_condition
        if major_version is not None:
            self.major_version = major_version
        if minor_version is not None:
            self.minor_version = minor_version
        if revision_number is not None:
            self.revision_number = revision_number
        if build_number is not None:
            self.build_number = build_number

    @property
    def application_identifier(self):
        """Gets the application_identifier of this AppCriteriaApiModel_.  # noqa: E501

        Gets or sets the identifier of the application.  # noqa: E501

        :return: The application_identifier of this AppCriteriaApiModel_.  # noqa: E501
        :rtype: str
        """
        return self._application_identifier

    @application_identifier.setter
    def application_identifier(self, application_identifier):
        """Sets the application_identifier of this AppCriteriaApiModel_.

        Gets or sets the identifier of the application.  # noqa: E501

        :param application_identifier: The application_identifier of this AppCriteriaApiModel_.  # noqa: E501
        :type: str
        """

        self._application_identifier = application_identifier

    @property
    def version_condition(self):
        """Gets the version_condition of this AppCriteriaApiModel_.  # noqa: E501

        Gets or sets the version condition. Supported values- Any, EqualTo, NotEqualTo, GreaterThan, GreaterThanEqualTo, LessThan, LessThanEqualTo.  # noqa: E501

        :return: The version_condition of this AppCriteriaApiModel_.  # noqa: E501
        :rtype: str
        """
        return self._version_condition

    @version_condition.setter
    def version_condition(self, version_condition):
        """Sets the version_condition of this AppCriteriaApiModel_.

        Gets or sets the version condition. Supported values- Any, EqualTo, NotEqualTo, GreaterThan, GreaterThanEqualTo, LessThan, LessThanEqualTo.  # noqa: E501

        :param version_condition: The version_condition of this AppCriteriaApiModel_.  # noqa: E501
        :type: str
        """

        self._version_condition = version_condition

    @property
    def major_version(self):
        """Gets the major_version of this AppCriteriaApiModel_.  # noqa: E501

        Gets or sets the major version of the application.  # noqa: E501

        :return: The major_version of this AppCriteriaApiModel_.  # noqa: E501
        :rtype: int
        """
        return self._major_version

    @major_version.setter
    def major_version(self, major_version):
        """Sets the major_version of this AppCriteriaApiModel_.

        Gets or sets the major version of the application.  # noqa: E501

        :param major_version: The major_version of this AppCriteriaApiModel_.  # noqa: E501
        :type: int
        """

        self._major_version = major_version

    @property
    def minor_version(self):
        """Gets the minor_version of this AppCriteriaApiModel_.  # noqa: E501

        Gets or sets the minor version of the application.  # noqa: E501

        :return: The minor_version of this AppCriteriaApiModel_.  # noqa: E501
        :rtype: int
        """
        return self._minor_version

    @minor_version.setter
    def minor_version(self, minor_version):
        """Sets the minor_version of this AppCriteriaApiModel_.

        Gets or sets the minor version of the application.  # noqa: E501

        :param minor_version: The minor_version of this AppCriteriaApiModel_.  # noqa: E501
        :type: int
        """

        self._minor_version = minor_version

    @property
    def revision_number(self):
        """Gets the revision_number of this AppCriteriaApiModel_.  # noqa: E501

        Gets or sets the fix version of the application.  # noqa: E501

        :return: The revision_number of this AppCriteriaApiModel_.  # noqa: E501
        :rtype: int
        """
        return self._revision_number

    @revision_number.setter
    def revision_number(self, revision_number):
        """Sets the revision_number of this AppCriteriaApiModel_.

        Gets or sets the fix version of the application.  # noqa: E501

        :param revision_number: The revision_number of this AppCriteriaApiModel_.  # noqa: E501
        :type: int
        """

        self._revision_number = revision_number

    @property
    def build_number(self):
        """Gets the build_number of this AppCriteriaApiModel_.  # noqa: E501

        Gets or sets the build version of the application.  # noqa: E501

        :return: The build_number of this AppCriteriaApiModel_.  # noqa: E501
        :rtype: int
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this AppCriteriaApiModel_.

        Gets or sets the build version of the application.  # noqa: E501

        :param build_number: The build_number of this AppCriteriaApiModel_.  # noqa: E501
        :type: int
        """

        self._build_number = build_number

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
        if issubclass(AppCriteriaApiModel_, dict):
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
        if not isinstance(other, AppCriteriaApiModel_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppCriteriaApiModel_):
            return True

        return self.to_dict() != other.to_dict()
