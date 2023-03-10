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


class ConfigureQRCodeEnrollmentV2Model(object):
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
        'wi_fi_configuration': 'int',
        'wi_fi_ssid': 'str',
        'wi_fi_password': 'str',
        'agent_package_source': 'int',
        'package_url': 'str',
        'is_lg_configuration_enabled': 'bool',
        'enrollment_location_group_id': 'str',
        'is_login_credentials_enabled': 'bool',
        'username': 'str',
        'password': 'str',
        'is_system_apps_enabled': 'bool',
        'force_aosp_enrollment': 'bool'
    }

    attribute_map = {
        'wi_fi_configuration': 'wiFiConfiguration',
        'wi_fi_ssid': 'wiFiSsid',
        'wi_fi_password': 'wiFiPassword',
        'agent_package_source': 'agentPackageSource',
        'package_url': 'packageUrl',
        'is_lg_configuration_enabled': 'isLgConfigurationEnabled',
        'enrollment_location_group_id': 'enrollmentLocationGroupId',
        'is_login_credentials_enabled': 'isLoginCredentialsEnabled',
        'username': 'username',
        'password': 'password',
        'is_system_apps_enabled': 'isSystemAppsEnabled',
        'force_aosp_enrollment': 'forceAospEnrollment'
    }

    def __init__(self, wi_fi_configuration=None, wi_fi_ssid=None, wi_fi_password=None, agent_package_source=None, package_url=None, is_lg_configuration_enabled=None, enrollment_location_group_id=None, is_login_credentials_enabled=None, username=None, password=None, is_system_apps_enabled=None, force_aosp_enrollment=None, _configuration=None):  # noqa: E501
        """ConfigureQRCodeEnrollmentV2Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._wi_fi_configuration = None
        self._wi_fi_ssid = None
        self._wi_fi_password = None
        self._agent_package_source = None
        self._package_url = None
        self._is_lg_configuration_enabled = None
        self._enrollment_location_group_id = None
        self._is_login_credentials_enabled = None
        self._username = None
        self._password = None
        self._is_system_apps_enabled = None
        self._force_aosp_enrollment = None
        self.discriminator = None

        if wi_fi_configuration is not None:
            self.wi_fi_configuration = wi_fi_configuration
        if wi_fi_ssid is not None:
            self.wi_fi_ssid = wi_fi_ssid
        if wi_fi_password is not None:
            self.wi_fi_password = wi_fi_password
        if agent_package_source is not None:
            self.agent_package_source = agent_package_source
        if package_url is not None:
            self.package_url = package_url
        if is_lg_configuration_enabled is not None:
            self.is_lg_configuration_enabled = is_lg_configuration_enabled
        if enrollment_location_group_id is not None:
            self.enrollment_location_group_id = enrollment_location_group_id
        if is_login_credentials_enabled is not None:
            self.is_login_credentials_enabled = is_login_credentials_enabled
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if is_system_apps_enabled is not None:
            self.is_system_apps_enabled = is_system_apps_enabled
        if force_aosp_enrollment is not None:
            self.force_aosp_enrollment = force_aosp_enrollment

    @property
    def wi_fi_configuration(self):
        """Gets the wi_fi_configuration of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        Wi-Fi Configuration for Device  # noqa: E501

        :return: The wi_fi_configuration of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: int
        """
        return self._wi_fi_configuration

    @wi_fi_configuration.setter
    def wi_fi_configuration(self, wi_fi_configuration):
        """Sets the wi_fi_configuration of this ConfigureQRCodeEnrollmentV2Model.

        Wi-Fi Configuration for Device  # noqa: E501

        :param wi_fi_configuration: The wi_fi_configuration of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3]  # noqa: E501
        if (self._configuration.client_side_validation and
                wi_fi_configuration not in allowed_values):
            raise ValueError(
                "Invalid value for `wi_fi_configuration` ({0}), must be one of {1}"  # noqa: E501
                .format(wi_fi_configuration, allowed_values)
            )

        self._wi_fi_configuration = wi_fi_configuration

    @property
    def wi_fi_ssid(self):
        """Gets the wi_fi_ssid of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        WiFi SSID. This property is effective only if 'wiFiConfiguration' is set to 'Open/Secure'  # noqa: E501

        :return: The wi_fi_ssid of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: str
        """
        return self._wi_fi_ssid

    @wi_fi_ssid.setter
    def wi_fi_ssid(self, wi_fi_ssid):
        """Sets the wi_fi_ssid of this ConfigureQRCodeEnrollmentV2Model.

        WiFi SSID. This property is effective only if 'wiFiConfiguration' is set to 'Open/Secure'  # noqa: E501

        :param wi_fi_ssid: The wi_fi_ssid of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: str
        """

        self._wi_fi_ssid = wi_fi_ssid

    @property
    def wi_fi_password(self):
        """Gets the wi_fi_password of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        WiFi Password. This property is effective only if 'wiFiConfiguration' is set to 'Secure'  # noqa: E501

        :return: The wi_fi_password of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: str
        """
        return self._wi_fi_password

    @wi_fi_password.setter
    def wi_fi_password(self, wi_fi_password):
        """Sets the wi_fi_password of this ConfigureQRCodeEnrollmentV2Model.

        WiFi Password. This property is effective only if 'wiFiConfiguration' is set to 'Secure'  # noqa: E501

        :param wi_fi_password: The wi_fi_password of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: str
        """

        self._wi_fi_password = wi_fi_password

    @property
    def agent_package_source(self):
        """Gets the agent_package_source of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        The Agent Package download location.  # noqa: E501

        :return: The agent_package_source of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: int
        """
        return self._agent_package_source

    @agent_package_source.setter
    def agent_package_source(self, agent_package_source):
        """Sets the agent_package_source of this ConfigureQRCodeEnrollmentV2Model.

        The Agent Package download location.  # noqa: E501

        :param agent_package_source: The agent_package_source of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if (self._configuration.client_side_validation and
                agent_package_source not in allowed_values):
            raise ValueError(
                "Invalid value for `agent_package_source` ({0}), must be one of {1}"  # noqa: E501
                .format(agent_package_source, allowed_values)
            )

        self._agent_package_source = agent_package_source

    @property
    def package_url(self):
        """Gets the package_url of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        Agent Package URL. This property is effective only if 'AgentPackageSource' is set to 'HostedOnAnExternalUrl'  # noqa: E501

        :return: The package_url of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: str
        """
        return self._package_url

    @package_url.setter
    def package_url(self, package_url):
        """Sets the package_url of this ConfigureQRCodeEnrollmentV2Model.

        Agent Package URL. This property is effective only if 'AgentPackageSource' is set to 'HostedOnAnExternalUrl'  # noqa: E501

        :param package_url: The package_url of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: str
        """

        self._package_url = package_url

    @property
    def is_lg_configuration_enabled(self):
        """Gets the is_lg_configuration_enabled of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        Enrollment LocationGroup Enabled Flag.  # noqa: E501

        :return: The is_lg_configuration_enabled of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: bool
        """
        return self._is_lg_configuration_enabled

    @is_lg_configuration_enabled.setter
    def is_lg_configuration_enabled(self, is_lg_configuration_enabled):
        """Sets the is_lg_configuration_enabled of this ConfigureQRCodeEnrollmentV2Model.

        Enrollment LocationGroup Enabled Flag.  # noqa: E501

        :param is_lg_configuration_enabled: The is_lg_configuration_enabled of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: bool
        """

        self._is_lg_configuration_enabled = is_lg_configuration_enabled

    @property
    def enrollment_location_group_id(self):
        """Gets the enrollment_location_group_id of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        Enrollment LocationGroup ID. This property is effective only if 'IsLgConfigurationEnabled' is set to 'true'  # noqa: E501

        :return: The enrollment_location_group_id of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_location_group_id

    @enrollment_location_group_id.setter
    def enrollment_location_group_id(self, enrollment_location_group_id):
        """Sets the enrollment_location_group_id of this ConfigureQRCodeEnrollmentV2Model.

        Enrollment LocationGroup ID. This property is effective only if 'IsLgConfigurationEnabled' is set to 'true'  # noqa: E501

        :param enrollment_location_group_id: The enrollment_location_group_id of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: str
        """

        self._enrollment_location_group_id = enrollment_location_group_id

    @property
    def is_login_credentials_enabled(self):
        """Gets the is_login_credentials_enabled of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        Is Login Credentials Enabled Flag.  # noqa: E501

        :return: The is_login_credentials_enabled of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: bool
        """
        return self._is_login_credentials_enabled

    @is_login_credentials_enabled.setter
    def is_login_credentials_enabled(self, is_login_credentials_enabled):
        """Sets the is_login_credentials_enabled of this ConfigureQRCodeEnrollmentV2Model.

        Is Login Credentials Enabled Flag.  # noqa: E501

        :param is_login_credentials_enabled: The is_login_credentials_enabled of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: bool
        """

        self._is_login_credentials_enabled = is_login_credentials_enabled

    @property
    def username(self):
        """Gets the username of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        Enrollment Username. This property is effective only if 'IsLoginCredentialsEnabled' is set to 'true'  # noqa: E501

        :return: The username of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ConfigureQRCodeEnrollmentV2Model.

        Enrollment Username. This property is effective only if 'IsLoginCredentialsEnabled' is set to 'true'  # noqa: E501

        :param username: The username of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        Enrollment Password. This property is effective only if 'IsLoginCredentialsEnabled' is set to 'true'  # noqa: E501

        :return: The password of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ConfigureQRCodeEnrollmentV2Model.

        Enrollment Password. This property is effective only if 'IsLoginCredentialsEnabled' is set to 'true'  # noqa: E501

        :param password: The password of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def is_system_apps_enabled(self):
        """Gets the is_system_apps_enabled of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        Is System Apps Enabled Flag.  # noqa: E501

        :return: The is_system_apps_enabled of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: bool
        """
        return self._is_system_apps_enabled

    @is_system_apps_enabled.setter
    def is_system_apps_enabled(self, is_system_apps_enabled):
        """Sets the is_system_apps_enabled of this ConfigureQRCodeEnrollmentV2Model.

        Is System Apps Enabled Flag.  # noqa: E501

        :param is_system_apps_enabled: The is_system_apps_enabled of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: bool
        """

        self._is_system_apps_enabled = is_system_apps_enabled

    @property
    def force_aosp_enrollment(self):
        """Gets the force_aosp_enrollment of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501

        Force AOSP Enrollment  # noqa: E501

        :return: The force_aosp_enrollment of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :rtype: bool
        """
        return self._force_aosp_enrollment

    @force_aosp_enrollment.setter
    def force_aosp_enrollment(self, force_aosp_enrollment):
        """Sets the force_aosp_enrollment of this ConfigureQRCodeEnrollmentV2Model.

        Force AOSP Enrollment  # noqa: E501

        :param force_aosp_enrollment: The force_aosp_enrollment of this ConfigureQRCodeEnrollmentV2Model.  # noqa: E501
        :type: bool
        """

        self._force_aosp_enrollment = force_aosp_enrollment

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
        if issubclass(ConfigureQRCodeEnrollmentV2Model, dict):
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
        if not isinstance(other, ConfigureQRCodeEnrollmentV2Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigureQRCodeEnrollmentV2Model):
            return True

        return self.to_dict() != other.to_dict()
