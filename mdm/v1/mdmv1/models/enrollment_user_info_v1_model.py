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


class EnrollmentUserInfoV1Model(object):
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
        'user_email_address': 'str',
        'email_user_name': 'str',
        'organization_group_name': 'str',
        'security_type': 'str',
        'contact_number': 'str'
    }

    attribute_map = {
        'name': 'name',
        'user_email_address': 'user_email_address',
        'email_user_name': 'email_user_name',
        'organization_group_name': 'organization_group_name',
        'security_type': 'security_type',
        'contact_number': 'contact_number'
    }

    def __init__(self, name=None, user_email_address=None, email_user_name=None, organization_group_name=None, security_type=None, contact_number=None, _configuration=None):  # noqa: E501
        """EnrollmentUserInfoV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._user_email_address = None
        self._email_user_name = None
        self._organization_group_name = None
        self._security_type = None
        self._contact_number = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if user_email_address is not None:
            self.user_email_address = user_email_address
        if email_user_name is not None:
            self.email_user_name = email_user_name
        if organization_group_name is not None:
            self.organization_group_name = organization_group_name
        if security_type is not None:
            self.security_type = security_type
        if contact_number is not None:
            self.contact_number = contact_number

    @property
    def name(self):
        """Gets the name of this EnrollmentUserInfoV1Model.  # noqa: E501

        Full name of the user.  # noqa: E501

        :return: The name of this EnrollmentUserInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnrollmentUserInfoV1Model.

        Full name of the user.  # noqa: E501

        :param name: The name of this EnrollmentUserInfoV1Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user_email_address(self):
        """Gets the user_email_address of this EnrollmentUserInfoV1Model.  # noqa: E501

        User's email address.  # noqa: E501

        :return: The user_email_address of this EnrollmentUserInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._user_email_address

    @user_email_address.setter
    def user_email_address(self, user_email_address):
        """Sets the user_email_address of this EnrollmentUserInfoV1Model.

        User's email address.  # noqa: E501

        :param user_email_address: The user_email_address of this EnrollmentUserInfoV1Model.  # noqa: E501
        :type: str
        """

        self._user_email_address = user_email_address

    @property
    def email_user_name(self):
        """Gets the email_user_name of this EnrollmentUserInfoV1Model.  # noqa: E501

        Email user name.  # noqa: E501

        :return: The email_user_name of this EnrollmentUserInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._email_user_name

    @email_user_name.setter
    def email_user_name(self, email_user_name):
        """Sets the email_user_name of this EnrollmentUserInfoV1Model.

        Email user name.  # noqa: E501

        :param email_user_name: The email_user_name of this EnrollmentUserInfoV1Model.  # noqa: E501
        :type: str
        """

        self._email_user_name = email_user_name

    @property
    def organization_group_name(self):
        """Gets the organization_group_name of this EnrollmentUserInfoV1Model.  # noqa: E501

        Organization group where the user is created.  # noqa: E501

        :return: The organization_group_name of this EnrollmentUserInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_name

    @organization_group_name.setter
    def organization_group_name(self, organization_group_name):
        """Sets the organization_group_name of this EnrollmentUserInfoV1Model.

        Organization group where the user is created.  # noqa: E501

        :param organization_group_name: The organization_group_name of this EnrollmentUserInfoV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group_name = organization_group_name

    @property
    def security_type(self):
        """Gets the security_type of this EnrollmentUserInfoV1Model.  # noqa: E501

        User's security type [Uninitialized, Directory, Basic, AuthenticationProxy, TokenOnly, SAML, External, Vidm].  # noqa: E501

        :return: The security_type of this EnrollmentUserInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._security_type

    @security_type.setter
    def security_type(self, security_type):
        """Sets the security_type of this EnrollmentUserInfoV1Model.

        User's security type [Uninitialized, Directory, Basic, AuthenticationProxy, TokenOnly, SAML, External, Vidm].  # noqa: E501

        :param security_type: The security_type of this EnrollmentUserInfoV1Model.  # noqa: E501
        :type: str
        """

        self._security_type = security_type

    @property
    def contact_number(self):
        """Gets the contact_number of this EnrollmentUserInfoV1Model.  # noqa: E501

        User's contact number.  # noqa: E501

        :return: The contact_number of this EnrollmentUserInfoV1Model.  # noqa: E501
        :rtype: str
        """
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        """Sets the contact_number of this EnrollmentUserInfoV1Model.

        User's contact number.  # noqa: E501

        :param contact_number: The contact_number of this EnrollmentUserInfoV1Model.  # noqa: E501
        :type: str
        """

        self._contact_number = contact_number

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
        if issubclass(EnrollmentUserInfoV1Model, dict):
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
        if not isinstance(other, EnrollmentUserInfoV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnrollmentUserInfoV1Model):
            return True

        return self.to_dict() != other.to_dict()
