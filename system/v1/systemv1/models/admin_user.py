# coding: utf-8

"""
    System API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv1.configuration import Configuration


class AdminUser(object):
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
        'user_name': 'str',
        'password': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'location_group': 'str',
        'location_group_id': 'str',
        'organization_group_uuid': 'str',
        'time_zone': 'str',
        'time_zone_identifier': 'str',
        'locale': 'str',
        'initial_landing_page': 'str',
        'last_login_time_stamp': 'datetime',
        'roles': 'list[RoleModel_]',
        'is_active_directory_user': 'bool',
        'requires_password_change': 'bool',
        'message_type': 'int',
        'message_template_id': 'int',
        'external_id': 'str',
        'id': 'EntityId_',
        'uuid': 'str'
    }

    attribute_map = {
        'user_name': 'UserName',
        'password': 'Password',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'email': 'Email',
        'location_group': 'LocationGroup',
        'location_group_id': 'LocationGroupId',
        'organization_group_uuid': 'OrganizationGroupUuid',
        'time_zone': 'TimeZone',
        'time_zone_identifier': 'TimeZoneIdentifier',
        'locale': 'Locale',
        'initial_landing_page': 'InitialLandingPage',
        'last_login_time_stamp': 'LastLoginTimeStamp',
        'roles': 'Roles',
        'is_active_directory_user': 'IsActiveDirectoryUser',
        'requires_password_change': 'RequiresPasswordChange',
        'message_type': 'MessageType',
        'message_template_id': 'MessageTemplateId',
        'external_id': 'ExternalId',
        'id': 'Id',
        'uuid': 'Uuid'
    }

    def __init__(self, user_name=None, password=None, first_name=None, last_name=None, email=None, location_group=None, location_group_id=None, organization_group_uuid=None, time_zone=None, time_zone_identifier=None, locale=None, initial_landing_page=None, last_login_time_stamp=None, roles=None, is_active_directory_user=None, requires_password_change=None, message_type=None, message_template_id=None, external_id=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """AdminUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_name = None
        self._password = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._location_group = None
        self._location_group_id = None
        self._organization_group_uuid = None
        self._time_zone = None
        self._time_zone_identifier = None
        self._locale = None
        self._initial_landing_page = None
        self._last_login_time_stamp = None
        self._roles = None
        self._is_active_directory_user = None
        self._requires_password_change = None
        self._message_type = None
        self._message_template_id = None
        self._external_id = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if location_group is not None:
            self.location_group = location_group
        if location_group_id is not None:
            self.location_group_id = location_group_id
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if time_zone is not None:
            self.time_zone = time_zone
        if time_zone_identifier is not None:
            self.time_zone_identifier = time_zone_identifier
        if locale is not None:
            self.locale = locale
        if initial_landing_page is not None:
            self.initial_landing_page = initial_landing_page
        if last_login_time_stamp is not None:
            self.last_login_time_stamp = last_login_time_stamp
        if roles is not None:
            self.roles = roles
        if is_active_directory_user is not None:
            self.is_active_directory_user = is_active_directory_user
        if requires_password_change is not None:
            self.requires_password_change = requires_password_change
        if message_type is not None:
            self.message_type = message_type
        if message_template_id is not None:
            self.message_template_id = message_template_id
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def user_name(self):
        """Gets the user_name of this AdminUser.  # noqa: E501

        Gets or sets user Name of admin.  # noqa: E501

        :return: The user_name of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AdminUser.

        Gets or sets user Name of admin.  # noqa: E501

        :param user_name: The user_name of this AdminUser.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this AdminUser.  # noqa: E501

        Gets or sets admin user password.  # noqa: E501

        :return: The password of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AdminUser.

        Gets or sets admin user password.  # noqa: E501

        :param password: The password of this AdminUser.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                password is not None and len(password) > 50):
            raise ValueError("Invalid value for `password`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                password is not None and len(password) < 0):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `0`")  # noqa: E501

        self._password = password

    @property
    def first_name(self):
        """Gets the first_name of this AdminUser.  # noqa: E501

        Gets or sets first Name of admin user.  # noqa: E501

        :return: The first_name of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AdminUser.

        Gets or sets first Name of admin user.  # noqa: E501

        :param first_name: The first_name of this AdminUser.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this AdminUser.  # noqa: E501

        Gets or sets last Name of admin user.  # noqa: E501

        :return: The last_name of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AdminUser.

        Gets or sets last Name of admin user.  # noqa: E501

        :param last_name: The last_name of this AdminUser.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this AdminUser.  # noqa: E501

        Gets or sets admin user email address.  # noqa: E501

        :return: The email of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AdminUser.

        Gets or sets admin user email address.  # noqa: E501

        :param email: The email of this AdminUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def location_group(self):
        """Gets the location_group of this AdminUser.  # noqa: E501

        Gets or sets location group of the admin user.  # noqa: E501

        :return: The location_group of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._location_group

    @location_group.setter
    def location_group(self, location_group):
        """Sets the location_group of this AdminUser.

        Gets or sets location group of the admin user.  # noqa: E501

        :param location_group: The location_group of this AdminUser.  # noqa: E501
        :type: str
        """

        self._location_group = location_group

    @property
    def location_group_id(self):
        """Gets the location_group_id of this AdminUser.  # noqa: E501

        Gets or sets location group id of the admin user.  # noqa: E501

        :return: The location_group_id of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._location_group_id

    @location_group_id.setter
    def location_group_id(self, location_group_id):
        """Sets the location_group_id of this AdminUser.

        Gets or sets location group id of the admin user.  # noqa: E501

        :param location_group_id: The location_group_id of this AdminUser.  # noqa: E501
        :type: str
        """

        self._location_group_id = location_group_id

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this AdminUser.  # noqa: E501

        Gets or sets organization group UUID of the admin user.  # noqa: E501

        :return: The organization_group_uuid of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this AdminUser.

        Gets or sets organization group UUID of the admin user.  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this AdminUser.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def time_zone(self):
        """Gets the time_zone of this AdminUser.  # noqa: E501

        Gets or sets time zone.  # noqa: E501

        :return: The time_zone of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this AdminUser.

        Gets or sets time zone.  # noqa: E501

        :param time_zone: The time_zone of this AdminUser.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def time_zone_identifier(self):
        """Gets the time_zone_identifier of this AdminUser.  # noqa: E501

        Gets or sets time zone label key.  # noqa: E501

        :return: The time_zone_identifier of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._time_zone_identifier

    @time_zone_identifier.setter
    def time_zone_identifier(self, time_zone_identifier):
        """Sets the time_zone_identifier of this AdminUser.

        Gets or sets time zone label key.  # noqa: E501

        :param time_zone_identifier: The time_zone_identifier of this AdminUser.  # noqa: E501
        :type: str
        """

        self._time_zone_identifier = time_zone_identifier

    @property
    def locale(self):
        """Gets the locale of this AdminUser.  # noqa: E501

        Gets or sets locale.  # noqa: E501

        :return: The locale of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this AdminUser.

        Gets or sets locale.  # noqa: E501

        :param locale: The locale of this AdminUser.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def initial_landing_page(self):
        """Gets the initial_landing_page of this AdminUser.  # noqa: E501

        Gets or sets initial landing page.  # noqa: E501

        :return: The initial_landing_page of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._initial_landing_page

    @initial_landing_page.setter
    def initial_landing_page(self, initial_landing_page):
        """Sets the initial_landing_page of this AdminUser.

        Gets or sets initial landing page.  # noqa: E501

        :param initial_landing_page: The initial_landing_page of this AdminUser.  # noqa: E501
        :type: str
        """

        self._initial_landing_page = initial_landing_page

    @property
    def last_login_time_stamp(self):
        """Gets the last_login_time_stamp of this AdminUser.  # noqa: E501

        Gets or sets last login time stamp of admin user.  # noqa: E501

        :return: The last_login_time_stamp of this AdminUser.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_time_stamp

    @last_login_time_stamp.setter
    def last_login_time_stamp(self, last_login_time_stamp):
        """Sets the last_login_time_stamp of this AdminUser.

        Gets or sets last login time stamp of admin user.  # noqa: E501

        :param last_login_time_stamp: The last_login_time_stamp of this AdminUser.  # noqa: E501
        :type: datetime
        """

        self._last_login_time_stamp = last_login_time_stamp

    @property
    def roles(self):
        """Gets the roles of this AdminUser.  # noqa: E501

        Gets or sets roles associated with the admin user.  # noqa: E501

        :return: The roles of this AdminUser.  # noqa: E501
        :rtype: list[RoleModel_]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AdminUser.

        Gets or sets roles associated with the admin user.  # noqa: E501

        :param roles: The roles of this AdminUser.  # noqa: E501
        :type: list[RoleModel_]
        """

        self._roles = roles

    @property
    def is_active_directory_user(self):
        """Gets the is_active_directory_user of this AdminUser.  # noqa: E501

        Gets or sets a value indicating whether flag to indicate whether the admin user is LDAP/AD user.  # noqa: E501

        :return: The is_active_directory_user of this AdminUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_active_directory_user

    @is_active_directory_user.setter
    def is_active_directory_user(self, is_active_directory_user):
        """Sets the is_active_directory_user of this AdminUser.

        Gets or sets a value indicating whether flag to indicate whether the admin user is LDAP/AD user.  # noqa: E501

        :param is_active_directory_user: The is_active_directory_user of this AdminUser.  # noqa: E501
        :type: bool
        """

        self._is_active_directory_user = is_active_directory_user

    @property
    def requires_password_change(self):
        """Gets the requires_password_change of this AdminUser.  # noqa: E501

        Gets or sets a value indicating whether flag to indicate whether the admin user requires to change the password on next login.  # noqa: E501

        :return: The requires_password_change of this AdminUser.  # noqa: E501
        :rtype: bool
        """
        return self._requires_password_change

    @requires_password_change.setter
    def requires_password_change(self, requires_password_change):
        """Sets the requires_password_change of this AdminUser.

        Gets or sets a value indicating whether flag to indicate whether the admin user requires to change the password on next login.  # noqa: E501

        :param requires_password_change: The requires_password_change of this AdminUser.  # noqa: E501
        :type: bool
        """

        self._requires_password_change = requires_password_change

    @property
    def message_type(self):
        """Gets the message_type of this AdminUser.  # noqa: E501

        Gets or sets message type.  # noqa: E501

        :return: The message_type of this AdminUser.  # noqa: E501
        :rtype: int
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this AdminUser.

        Gets or sets message type.  # noqa: E501

        :param message_type: The message_type of this AdminUser.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, -1]  # noqa: E501
        if (self._configuration.client_side_validation and
                message_type not in allowed_values):
            raise ValueError(
                "Invalid value for `message_type` ({0}), must be one of {1}"  # noqa: E501
                .format(message_type, allowed_values)
            )

        self._message_type = message_type

    @property
    def message_template_id(self):
        """Gets the message_template_id of this AdminUser.  # noqa: E501

        Gets or sets message template id.  # noqa: E501

        :return: The message_template_id of this AdminUser.  # noqa: E501
        :rtype: int
        """
        return self._message_template_id

    @message_template_id.setter
    def message_template_id(self, message_template_id):
        """Sets the message_template_id of this AdminUser.

        Gets or sets message template id.  # noqa: E501

        :param message_template_id: The message_template_id of this AdminUser.  # noqa: E501
        :type: int
        """

        self._message_template_id = message_template_id

    @property
    def external_id(self):
        """Gets the external_id of this AdminUser.  # noqa: E501

        Gets or sets external id.  # noqa: E501

        :return: The external_id of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this AdminUser.

        Gets or sets external id.  # noqa: E501

        :param external_id: The external_id of this AdminUser.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this AdminUser.  # noqa: E501


        :return: The id of this AdminUser.  # noqa: E501
        :rtype: EntityId_
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdminUser.


        :param id: The id of this AdminUser.  # noqa: E501
        :type: EntityId_
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this AdminUser.  # noqa: E501


        :return: The uuid of this AdminUser.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this AdminUser.


        :param uuid: The uuid of this AdminUser.  # noqa: E501
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
        if issubclass(AdminUser, dict):
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
        if not isinstance(other, AdminUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdminUser):
            return True

        return self.to_dict() != other.to_dict()
