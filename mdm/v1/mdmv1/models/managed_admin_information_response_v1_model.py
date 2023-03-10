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


class ManagedAdminInformationResponseV1Model(object):
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
        'account_identifier': 'str',
        'user_name': 'str',
        'full_name': 'str',
        'current_password': 'str',
        'previous_password': 'str',
        'password_set_on': 'datetime'
    }

    attribute_map = {
        'account_identifier': 'account_identifier',
        'user_name': 'user_name',
        'full_name': 'full_name',
        'current_password': 'current_password',
        'previous_password': 'previous_password',
        'password_set_on': 'password_set_on'
    }

    def __init__(self, account_identifier=None, user_name=None, full_name=None, current_password=None, previous_password=None, password_set_on=None, _configuration=None):  # noqa: E501
        """ManagedAdminInformationResponseV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_identifier = None
        self._user_name = None
        self._full_name = None
        self._current_password = None
        self._previous_password = None
        self._password_set_on = None
        self.discriminator = None

        if account_identifier is not None:
            self.account_identifier = account_identifier
        if user_name is not None:
            self.user_name = user_name
        if full_name is not None:
            self.full_name = full_name
        if current_password is not None:
            self.current_password = current_password
        if previous_password is not None:
            self.previous_password = previous_password
        if password_set_on is not None:
            self.password_set_on = password_set_on

    @property
    def account_identifier(self):
        """Gets the account_identifier of this ManagedAdminInformationResponseV1Model.  # noqa: E501

        The unique identifier of the administrator account.  # noqa: E501

        :return: The account_identifier of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this ManagedAdminInformationResponseV1Model.

        The unique identifier of the administrator account.  # noqa: E501

        :param account_identifier: The account_identifier of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def user_name(self):
        """Gets the user_name of this ManagedAdminInformationResponseV1Model.  # noqa: E501

        The username of the administrator.  # noqa: E501

        :return: The user_name of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ManagedAdminInformationResponseV1Model.

        The username of the administrator.  # noqa: E501

        :param user_name: The user_name of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def full_name(self):
        """Gets the full_name of this ManagedAdminInformationResponseV1Model.  # noqa: E501

        The full name of the administrator.  # noqa: E501

        :return: The full_name of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ManagedAdminInformationResponseV1Model.

        The full name of the administrator.  # noqa: E501

        :param full_name: The full_name of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def current_password(self):
        """Gets the current_password of this ManagedAdminInformationResponseV1Model.  # noqa: E501

        The current password of the administrator.  # noqa: E501

        :return: The current_password of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._current_password

    @current_password.setter
    def current_password(self, current_password):
        """Sets the current_password of this ManagedAdminInformationResponseV1Model.

        The current password of the administrator.  # noqa: E501

        :param current_password: The current_password of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :type: str
        """

        self._current_password = current_password

    @property
    def previous_password(self):
        """Gets the previous_password of this ManagedAdminInformationResponseV1Model.  # noqa: E501

        Previous password of the administrator.  # noqa: E501

        :return: The previous_password of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :rtype: str
        """
        return self._previous_password

    @previous_password.setter
    def previous_password(self, previous_password):
        """Sets the previous_password of this ManagedAdminInformationResponseV1Model.

        Previous password of the administrator.  # noqa: E501

        :param previous_password: The previous_password of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :type: str
        """

        self._previous_password = previous_password

    @property
    def password_set_on(self):
        """Gets the password_set_on of this ManagedAdminInformationResponseV1Model.  # noqa: E501

        The date and time of the day on which the administrator password was last set.  # noqa: E501

        :return: The password_set_on of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :rtype: datetime
        """
        return self._password_set_on

    @password_set_on.setter
    def password_set_on(self, password_set_on):
        """Sets the password_set_on of this ManagedAdminInformationResponseV1Model.

        The date and time of the day on which the administrator password was last set.  # noqa: E501

        :param password_set_on: The password_set_on of this ManagedAdminInformationResponseV1Model.  # noqa: E501
        :type: datetime
        """

        self._password_set_on = password_set_on

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
        if issubclass(ManagedAdminInformationResponseV1Model, dict):
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
        if not isinstance(other, ManagedAdminInformationResponseV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManagedAdminInformationResponseV1Model):
            return True

        return self.to_dict() != other.to_dict()
