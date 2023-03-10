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


class AndroidConatinerVPNPayloadV2Entity(object):
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
        'client_type': 'int',
        'connection_name': 'str',
        'server_name': 'str',
        'use_authentication': 'bool',
        'username': 'str',
        'password': 'str',
        'realm': 'str',
        'role': 'str',
        'connection_type': 'int',
        'vpn_assignment': 'int',
        'vpn_applications_list': 'list[str]',
        'enable_advanced_configurations': 'bool',
        'split_tunnel_type': 'int',
        'authentication_type': 'int',
        'mocana_settings': 'AndroidConatinerVPNMocanaSettings_',
        'pulse_secure_settings': 'AndroidConatinerVPNPulseSecureSettings_',
        'net_motion_settings': 'AndroidContainerVpnNetMotionSettings_'
    }

    attribute_map = {
        'client_type': 'ClientType',
        'connection_name': 'ConnectionName',
        'server_name': 'ServerName',
        'use_authentication': 'UseAuthentication',
        'username': 'Username',
        'password': 'Password',
        'realm': 'Realm',
        'role': 'Role',
        'connection_type': 'ConnectionType',
        'vpn_assignment': 'VpnAssignment',
        'vpn_applications_list': 'VPNApplicationsList',
        'enable_advanced_configurations': 'EnableAdvancedConfigurations',
        'split_tunnel_type': 'SplitTunnelType',
        'authentication_type': 'AuthenticationType',
        'mocana_settings': 'MocanaSettings',
        'pulse_secure_settings': 'PulseSecureSettings',
        'net_motion_settings': 'NetMotionSettings'
    }

    def __init__(self, client_type=None, connection_name=None, server_name=None, use_authentication=None, username=None, password=None, realm=None, role=None, connection_type=None, vpn_assignment=None, vpn_applications_list=None, enable_advanced_configurations=None, split_tunnel_type=None, authentication_type=None, mocana_settings=None, pulse_secure_settings=None, net_motion_settings=None, _configuration=None):  # noqa: E501
        """AndroidConatinerVPNPayloadV2Entity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_type = None
        self._connection_name = None
        self._server_name = None
        self._use_authentication = None
        self._username = None
        self._password = None
        self._realm = None
        self._role = None
        self._connection_type = None
        self._vpn_assignment = None
        self._vpn_applications_list = None
        self._enable_advanced_configurations = None
        self._split_tunnel_type = None
        self._authentication_type = None
        self._mocana_settings = None
        self._pulse_secure_settings = None
        self._net_motion_settings = None
        self.discriminator = None

        if client_type is not None:
            self.client_type = client_type
        if connection_name is not None:
            self.connection_name = connection_name
        if server_name is not None:
            self.server_name = server_name
        if use_authentication is not None:
            self.use_authentication = use_authentication
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if realm is not None:
            self.realm = realm
        if role is not None:
            self.role = role
        if connection_type is not None:
            self.connection_type = connection_type
        if vpn_assignment is not None:
            self.vpn_assignment = vpn_assignment
        if vpn_applications_list is not None:
            self.vpn_applications_list = vpn_applications_list
        if enable_advanced_configurations is not None:
            self.enable_advanced_configurations = enable_advanced_configurations
        if split_tunnel_type is not None:
            self.split_tunnel_type = split_tunnel_type
        if authentication_type is not None:
            self.authentication_type = authentication_type
        if mocana_settings is not None:
            self.mocana_settings = mocana_settings
        if pulse_secure_settings is not None:
            self.pulse_secure_settings = pulse_secure_settings
        if net_motion_settings is not None:
            self.net_motion_settings = net_motion_settings

    @property
    def client_type(self):
        """Gets the client_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the client.  # noqa: E501

        :return: The client_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the client.  # noqa: E501

        :param client_type: The client_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._client_type = client_type

    @property
    def connection_name(self):
        """Gets the connection_name of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the name of the connection.  # noqa: E501

        :return: The connection_name of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        """Sets the connection_name of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the name of the connection.  # noqa: E501

        :param connection_name: The connection_name of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._connection_name = connection_name

    @property
    def server_name(self):
        """Gets the server_name of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the name of the server.  # noqa: E501

        :return: The server_name of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the name of the server.  # noqa: E501

        :param server_name: The server_name of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._server_name = server_name

    @property
    def use_authentication(self):
        """Gets the use_authentication of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether this instance is user authentication required.  # noqa: E501

        :return: The use_authentication of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._use_authentication

    @use_authentication.setter
    def use_authentication(self, use_authentication):
        """Sets the use_authentication of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets a value indicating whether this instance is user authentication required.  # noqa: E501

        :param use_authentication: The use_authentication of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._use_authentication = use_authentication

    @property
    def username(self):
        """Gets the username of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the username.  # noqa: E501

        :return: The username of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the username.  # noqa: E501

        :param username: The username of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the password.  # noqa: E501

        :return: The password of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the password.  # noqa: E501

        :param password: The password of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def realm(self):
        """Gets the realm of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the realm.  # noqa: E501

        :return: The realm of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the realm.  # noqa: E501

        :param realm: The realm of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._realm = realm

    @property
    def role(self):
        """Gets the role of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the role.  # noqa: E501

        :return: The role of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the role.  # noqa: E501

        :param role: The role of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def connection_type(self):
        """Gets the connection_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the type of the VPN.  # noqa: E501

        :return: The connection_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the type of the VPN.  # noqa: E501

        :param connection_type: The connection_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._connection_type = connection_type

    @property
    def vpn_assignment(self):
        """Gets the vpn_assignment of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the VPN assignment.  # noqa: E501

        :return: The vpn_assignment of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._vpn_assignment

    @vpn_assignment.setter
    def vpn_assignment(self, vpn_assignment):
        """Sets the vpn_assignment of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the VPN assignment.  # noqa: E501

        :param vpn_assignment: The vpn_assignment of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._vpn_assignment = vpn_assignment

    @property
    def vpn_applications_list(self):
        """Gets the vpn_applications_list of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the VPN applications list.  # noqa: E501

        :return: The vpn_applications_list of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: list[str]
        """
        return self._vpn_applications_list

    @vpn_applications_list.setter
    def vpn_applications_list(self, vpn_applications_list):
        """Sets the vpn_applications_list of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the VPN applications list.  # noqa: E501

        :param vpn_applications_list: The vpn_applications_list of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: list[str]
        """

        self._vpn_applications_list = vpn_applications_list

    @property
    def enable_advanced_configurations(self):
        """Gets the enable_advanced_configurations of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets a value indicating whether this {AirWatch.ServiceModel.Profiles.V2.Resources.Android.AndroidConatinerVPNPayloadV2Entity} is advanced.  # noqa: E501

        :return: The enable_advanced_configurations of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: bool
        """
        return self._enable_advanced_configurations

    @enable_advanced_configurations.setter
    def enable_advanced_configurations(self, enable_advanced_configurations):
        """Sets the enable_advanced_configurations of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets a value indicating whether this {AirWatch.ServiceModel.Profiles.V2.Resources.Android.AndroidConatinerVPNPayloadV2Entity} is advanced.  # noqa: E501

        :param enable_advanced_configurations: The enable_advanced_configurations of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: bool
        """

        self._enable_advanced_configurations = enable_advanced_configurations

    @property
    def split_tunnel_type(self):
        """Gets the split_tunnel_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the type of the split tunel.  # noqa: E501

        :return: The split_tunnel_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._split_tunnel_type

    @split_tunnel_type.setter
    def split_tunnel_type(self, split_tunnel_type):
        """Sets the split_tunnel_type of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the type of the split tunel.  # noqa: E501

        :param split_tunnel_type: The split_tunnel_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._split_tunnel_type = split_tunnel_type

    @property
    def authentication_type(self):
        """Gets the authentication_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the authentication method.  # noqa: E501

        :return: The authentication_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: int
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the authentication method.  # noqa: E501

        :param authentication_type: The authentication_type of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: int
        """

        self._authentication_type = authentication_type

    @property
    def mocana_settings(self):
        """Gets the mocana_settings of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the mocana settings.  # noqa: E501

        :return: The mocana_settings of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: AndroidConatinerVPNMocanaSettings_
        """
        return self._mocana_settings

    @mocana_settings.setter
    def mocana_settings(self, mocana_settings):
        """Sets the mocana_settings of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the mocana settings.  # noqa: E501

        :param mocana_settings: The mocana_settings of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: AndroidConatinerVPNMocanaSettings_
        """

        self._mocana_settings = mocana_settings

    @property
    def pulse_secure_settings(self):
        """Gets the pulse_secure_settings of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the pulse secure settings.  # noqa: E501

        :return: The pulse_secure_settings of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: AndroidConatinerVPNPulseSecureSettings_
        """
        return self._pulse_secure_settings

    @pulse_secure_settings.setter
    def pulse_secure_settings(self, pulse_secure_settings):
        """Sets the pulse_secure_settings of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the pulse secure settings.  # noqa: E501

        :param pulse_secure_settings: The pulse_secure_settings of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: AndroidConatinerVPNPulseSecureSettings_
        """

        self._pulse_secure_settings = pulse_secure_settings

    @property
    def net_motion_settings(self):
        """Gets the net_motion_settings of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501

        Gets or sets the net motion settings.  # noqa: E501

        :return: The net_motion_settings of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :rtype: AndroidContainerVpnNetMotionSettings_
        """
        return self._net_motion_settings

    @net_motion_settings.setter
    def net_motion_settings(self, net_motion_settings):
        """Sets the net_motion_settings of this AndroidConatinerVPNPayloadV2Entity.

        Gets or sets the net motion settings.  # noqa: E501

        :param net_motion_settings: The net_motion_settings of this AndroidConatinerVPNPayloadV2Entity.  # noqa: E501
        :type: AndroidContainerVpnNetMotionSettings_
        """

        self._net_motion_settings = net_motion_settings

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
        if issubclass(AndroidConatinerVPNPayloadV2Entity, dict):
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
        if not isinstance(other, AndroidConatinerVPNPayloadV2Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidConatinerVPNPayloadV2Entity):
            return True

        return self.to_dict() != other.to_dict()
