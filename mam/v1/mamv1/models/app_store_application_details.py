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


class AppStoreApplicationDetails(object):
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
        'application_name': 'str',
        'current_version': 'str',
        'external_id': 'str'
    }

    attribute_map = {
        'bundle_id': 'BundleID',
        'application_name': 'ApplicationName',
        'current_version': 'CurrentVersion',
        'external_id': 'ExternalID'
    }

    def __init__(self, bundle_id=None, application_name=None, current_version=None, external_id=None, _configuration=None):  # noqa: E501
        """AppStoreApplicationDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bundle_id = None
        self._application_name = None
        self._current_version = None
        self._external_id = None
        self.discriminator = None

        if bundle_id is not None:
            self.bundle_id = bundle_id
        if application_name is not None:
            self.application_name = application_name
        if current_version is not None:
            self.current_version = current_version
        if external_id is not None:
            self.external_id = external_id

    @property
    def bundle_id(self):
        """Gets the bundle_id of this AppStoreApplicationDetails.  # noqa: E501

        Gets or sets bundle ID of the application.  # noqa: E501

        :return: The bundle_id of this AppStoreApplicationDetails.  # noqa: E501
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this AppStoreApplicationDetails.

        Gets or sets bundle ID of the application.  # noqa: E501

        :param bundle_id: The bundle_id of this AppStoreApplicationDetails.  # noqa: E501
        :type: str
        """

        self._bundle_id = bundle_id

    @property
    def application_name(self):
        """Gets the application_name of this AppStoreApplicationDetails.  # noqa: E501

        Gets or sets name of Application.  # noqa: E501

        :return: The application_name of this AppStoreApplicationDetails.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this AppStoreApplicationDetails.

        Gets or sets name of Application.  # noqa: E501

        :param application_name: The application_name of this AppStoreApplicationDetails.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def current_version(self):
        """Gets the current_version of this AppStoreApplicationDetails.  # noqa: E501

        Gets or sets current version of App in AppStore.  # noqa: E501

        :return: The current_version of this AppStoreApplicationDetails.  # noqa: E501
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this AppStoreApplicationDetails.

        Gets or sets current version of App in AppStore.  # noqa: E501

        :param current_version: The current_version of this AppStoreApplicationDetails.  # noqa: E501
        :type: str
        """

        self._current_version = current_version

    @property
    def external_id(self):
        """Gets the external_id of this AppStoreApplicationDetails.  # noqa: E501

        Gets or sets external ID of the application.  # noqa: E501

        :return: The external_id of this AppStoreApplicationDetails.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this AppStoreApplicationDetails.

        Gets or sets external ID of the application.  # noqa: E501

        :param external_id: The external_id of this AppStoreApplicationDetails.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

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
        if issubclass(AppStoreApplicationDetails, dict):
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
        if not isinstance(other, AppStoreApplicationDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppStoreApplicationDetails):
            return True

        return self.to_dict() != other.to_dict()
