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


class ApplicationDeploymentParametersModel_(object):
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
        'smart_group_id': 'int',
        'assignment_id': 'int',
        'push_mode': 'str',
        'effective_date': 'datetime',
        'remove_on_un_enroll': 'bool',
        'application_backup': 'bool',
        'auto_update_devices_with_previous_version': 'bool',
        'adaptive_management': 'bool',
        'is_per_app_vpn_enabled': 'bool',
        'vpn_profile_id': 'int',
        'afw_vpn_profile_id': 'int',
        'send_application_config': 'bool',
        'whitelisted_domains': 'str',
        'nsx_security_groups': 'int',
        'application_configurations': 'list[ApplicationConfigurationModel_]',
        'application_transform_ids': 'list[int]',
        'allow_management': 'bool',
        'mac_os_desired_state_management': 'bool',
        'requires_approval': 'bool',
        'visible_in_app_catalog': 'bool',
        'app_config_blob_id': 'int',
        'send_application_attributes': 'bool',
        'prevent_removal': 'bool',
        'application_attributes': 'list[ApplicationConfigurationModel_]',
        'app_attributes_blob_id': 'int',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'smart_group_id': 'SmartGroupId',
        'assignment_id': 'AssignmentId',
        'push_mode': 'PushMode',
        'effective_date': 'EffectiveDate',
        'remove_on_un_enroll': 'RemoveOnUnEnroll',
        'application_backup': 'ApplicationBackup',
        'auto_update_devices_with_previous_version': 'AutoUpdateDevicesWithPreviousVersion',
        'adaptive_management': 'AdaptiveManagement',
        'is_per_app_vpn_enabled': 'IsPerAppVpnEnabled',
        'vpn_profile_id': 'VpnProfileId',
        'afw_vpn_profile_id': 'AfwVpnProfileId',
        'send_application_config': 'SendApplicationConfig',
        'whitelisted_domains': 'WhitelistedDomains',
        'nsx_security_groups': 'NsxSecurityGroups',
        'application_configurations': 'ApplicationConfigurations',
        'application_transform_ids': 'ApplicationTransformIds',
        'allow_management': 'AllowManagement',
        'mac_os_desired_state_management': 'MacOsDesiredStateManagement',
        'requires_approval': 'RequiresApproval',
        'visible_in_app_catalog': 'VisibleInAppCatalog',
        'app_config_blob_id': 'AppConfigBlobId',
        'send_application_attributes': 'SendApplicationAttributes',
        'prevent_removal': 'PreventRemoval',
        'application_attributes': 'ApplicationAttributes',
        'app_attributes_blob_id': 'AppAttributesBlobId',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, smart_group_id=None, assignment_id=None, push_mode=None, effective_date=None, remove_on_un_enroll=None, application_backup=None, auto_update_devices_with_previous_version=None, adaptive_management=None, is_per_app_vpn_enabled=None, vpn_profile_id=None, afw_vpn_profile_id=None, send_application_config=None, whitelisted_domains=None, nsx_security_groups=None, application_configurations=None, application_transform_ids=None, allow_management=None, mac_os_desired_state_management=None, requires_approval=None, visible_in_app_catalog=None, app_config_blob_id=None, send_application_attributes=None, prevent_removal=None, application_attributes=None, app_attributes_blob_id=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """ApplicationDeploymentParametersModel_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._smart_group_id = None
        self._assignment_id = None
        self._push_mode = None
        self._effective_date = None
        self._remove_on_un_enroll = None
        self._application_backup = None
        self._auto_update_devices_with_previous_version = None
        self._adaptive_management = None
        self._is_per_app_vpn_enabled = None
        self._vpn_profile_id = None
        self._afw_vpn_profile_id = None
        self._send_application_config = None
        self._whitelisted_domains = None
        self._nsx_security_groups = None
        self._application_configurations = None
        self._application_transform_ids = None
        self._allow_management = None
        self._mac_os_desired_state_management = None
        self._requires_approval = None
        self._visible_in_app_catalog = None
        self._app_config_blob_id = None
        self._send_application_attributes = None
        self._prevent_removal = None
        self._application_attributes = None
        self._app_attributes_blob_id = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if smart_group_id is not None:
            self.smart_group_id = smart_group_id
        if assignment_id is not None:
            self.assignment_id = assignment_id
        if push_mode is not None:
            self.push_mode = push_mode
        if effective_date is not None:
            self.effective_date = effective_date
        if remove_on_un_enroll is not None:
            self.remove_on_un_enroll = remove_on_un_enroll
        if application_backup is not None:
            self.application_backup = application_backup
        if auto_update_devices_with_previous_version is not None:
            self.auto_update_devices_with_previous_version = auto_update_devices_with_previous_version
        if adaptive_management is not None:
            self.adaptive_management = adaptive_management
        if is_per_app_vpn_enabled is not None:
            self.is_per_app_vpn_enabled = is_per_app_vpn_enabled
        if vpn_profile_id is not None:
            self.vpn_profile_id = vpn_profile_id
        if afw_vpn_profile_id is not None:
            self.afw_vpn_profile_id = afw_vpn_profile_id
        if send_application_config is not None:
            self.send_application_config = send_application_config
        if whitelisted_domains is not None:
            self.whitelisted_domains = whitelisted_domains
        if nsx_security_groups is not None:
            self.nsx_security_groups = nsx_security_groups
        if application_configurations is not None:
            self.application_configurations = application_configurations
        if application_transform_ids is not None:
            self.application_transform_ids = application_transform_ids
        if allow_management is not None:
            self.allow_management = allow_management
        if mac_os_desired_state_management is not None:
            self.mac_os_desired_state_management = mac_os_desired_state_management
        if requires_approval is not None:
            self.requires_approval = requires_approval
        if visible_in_app_catalog is not None:
            self.visible_in_app_catalog = visible_in_app_catalog
        if app_config_blob_id is not None:
            self.app_config_blob_id = app_config_blob_id
        if send_application_attributes is not None:
            self.send_application_attributes = send_application_attributes
        if prevent_removal is not None:
            self.prevent_removal = prevent_removal
        if application_attributes is not None:
            self.application_attributes = application_attributes
        if app_attributes_blob_id is not None:
            self.app_attributes_blob_id = app_attributes_blob_id
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def smart_group_id(self):
        """Gets the smart_group_id of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets smart group id.  # noqa: E501

        :return: The smart_group_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: int
        """
        return self._smart_group_id

    @smart_group_id.setter
    def smart_group_id(self, smart_group_id):
        """Sets the smart_group_id of this ApplicationDeploymentParametersModel_.

        Gets or sets smart group id.  # noqa: E501

        :param smart_group_id: The smart_group_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: int
        """

        self._smart_group_id = smart_group_id

    @property
    def assignment_id(self):
        """Gets the assignment_id of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets the assignment entity map IdSmart group id.  # noqa: E501

        :return: The assignment_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: int
        """
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, assignment_id):
        """Sets the assignment_id of this ApplicationDeploymentParametersModel_.

        Gets or sets the assignment entity map IdSmart group id.  # noqa: E501

        :param assignment_id: The assignment_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: int
        """

        self._assignment_id = assignment_id

    @property
    def push_mode(self):
        """Gets the push_mode of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets push mode for the application.  # noqa: E501

        :return: The push_mode of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: str
        """
        return self._push_mode

    @push_mode.setter
    def push_mode(self, push_mode):
        """Sets the push_mode of this ApplicationDeploymentParametersModel_.

        Gets or sets push mode for the application.  # noqa: E501

        :param push_mode: The push_mode of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: str
        """

        self._push_mode = push_mode

    @property
    def effective_date(self):
        """Gets the effective_date of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets effective date for  the application.  # noqa: E501

        :return: The effective_date of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this ApplicationDeploymentParametersModel_.

        Gets or sets effective date for  the application.  # noqa: E501

        :param effective_date: The effective_date of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: datetime
        """

        self._effective_date = effective_date

    @property
    def remove_on_un_enroll(self):
        """Gets the remove_on_un_enroll of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets whether the application should be removed on unenrollment.  # noqa: E501

        :return: The remove_on_un_enroll of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._remove_on_un_enroll

    @remove_on_un_enroll.setter
    def remove_on_un_enroll(self, remove_on_un_enroll):
        """Sets the remove_on_un_enroll of this ApplicationDeploymentParametersModel_.

        Gets or sets whether the application should be removed on unenrollment.  # noqa: E501

        :param remove_on_un_enroll: The remove_on_un_enroll of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._remove_on_un_enroll = remove_on_un_enroll

    @property
    def application_backup(self):
        """Gets the application_backup of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets whether application backup is enabled.  # noqa: E501

        :return: The application_backup of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._application_backup

    @application_backup.setter
    def application_backup(self, application_backup):
        """Sets the application_backup of this ApplicationDeploymentParametersModel_.

        Gets or sets whether application backup is enabled.  # noqa: E501

        :param application_backup: The application_backup of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._application_backup = application_backup

    @property
    def auto_update_devices_with_previous_version(self):
        """Gets the auto_update_devices_with_previous_version of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets whether the newest version of the app should be pushed to devices that have already downloaded the app.  # noqa: E501

        :return: The auto_update_devices_with_previous_version of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._auto_update_devices_with_previous_version

    @auto_update_devices_with_previous_version.setter
    def auto_update_devices_with_previous_version(self, auto_update_devices_with_previous_version):
        """Sets the auto_update_devices_with_previous_version of this ApplicationDeploymentParametersModel_.

        Gets or sets whether the newest version of the app should be pushed to devices that have already downloaded the app.  # noqa: E501

        :param auto_update_devices_with_previous_version: The auto_update_devices_with_previous_version of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._auto_update_devices_with_previous_version = auto_update_devices_with_previous_version

    @property
    def adaptive_management(self):
        """Gets the adaptive_management of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets whether device should enrolled to get the app - Only applicable for WorkspaceOne.  # noqa: E501

        :return: The adaptive_management of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._adaptive_management

    @adaptive_management.setter
    def adaptive_management(self, adaptive_management):
        """Sets the adaptive_management of this ApplicationDeploymentParametersModel_.

        Gets or sets whether device should enrolled to get the app - Only applicable for WorkspaceOne.  # noqa: E501

        :param adaptive_management: The adaptive_management of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._adaptive_management = adaptive_management

    @property
    def is_per_app_vpn_enabled(self):
        """Gets the is_per_app_vpn_enabled of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets whether per app vpn flag is enabled.  # noqa: E501

        :return: The is_per_app_vpn_enabled of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._is_per_app_vpn_enabled

    @is_per_app_vpn_enabled.setter
    def is_per_app_vpn_enabled(self, is_per_app_vpn_enabled):
        """Sets the is_per_app_vpn_enabled of this ApplicationDeploymentParametersModel_.

        Gets or sets whether per app vpn flag is enabled.  # noqa: E501

        :param is_per_app_vpn_enabled: The is_per_app_vpn_enabled of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._is_per_app_vpn_enabled = is_per_app_vpn_enabled

    @property
    def vpn_profile_id(self):
        """Gets the vpn_profile_id of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets vpn profile id associated with the application.  # noqa: E501

        :return: The vpn_profile_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: int
        """
        return self._vpn_profile_id

    @vpn_profile_id.setter
    def vpn_profile_id(self, vpn_profile_id):
        """Sets the vpn_profile_id of this ApplicationDeploymentParametersModel_.

        Gets or sets vpn profile id associated with the application.  # noqa: E501

        :param vpn_profile_id: The vpn_profile_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: int
        """

        self._vpn_profile_id = vpn_profile_id

    @property
    def afw_vpn_profile_id(self):
        """Gets the afw_vpn_profile_id of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets the ID of the AFW VPN Profile applicable to the devices in this assignment.  # noqa: E501

        :return: The afw_vpn_profile_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: int
        """
        return self._afw_vpn_profile_id

    @afw_vpn_profile_id.setter
    def afw_vpn_profile_id(self, afw_vpn_profile_id):
        """Sets the afw_vpn_profile_id of this ApplicationDeploymentParametersModel_.

        Gets or sets the ID of the AFW VPN Profile applicable to the devices in this assignment.  # noqa: E501

        :param afw_vpn_profile_id: The afw_vpn_profile_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: int
        """

        self._afw_vpn_profile_id = afw_vpn_profile_id

    @property
    def send_application_config(self):
        """Gets the send_application_config of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets whether custom application configuration keys and values should be sent to the device.  # noqa: E501

        :return: The send_application_config of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._send_application_config

    @send_application_config.setter
    def send_application_config(self, send_application_config):
        """Sets the send_application_config of this ApplicationDeploymentParametersModel_.

        Gets or sets whether custom application configuration keys and values should be sent to the device.  # noqa: E501

        :param send_application_config: The send_application_config of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._send_application_config = send_application_config

    @property
    def whitelisted_domains(self):
        """Gets the whitelisted_domains of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets whiteListed domains for the tunnel server.  # noqa: E501

        :return: The whitelisted_domains of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: str
        """
        return self._whitelisted_domains

    @whitelisted_domains.setter
    def whitelisted_domains(self, whitelisted_domains):
        """Sets the whitelisted_domains of this ApplicationDeploymentParametersModel_.

        Gets or sets whiteListed domains for the tunnel server.  # noqa: E501

        :param whitelisted_domains: The whitelisted_domains of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: str
        """

        self._whitelisted_domains = whitelisted_domains

    @property
    def nsx_security_groups(self):
        """Gets the nsx_security_groups of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets security group id for nsx.  # noqa: E501

        :return: The nsx_security_groups of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: int
        """
        return self._nsx_security_groups

    @nsx_security_groups.setter
    def nsx_security_groups(self, nsx_security_groups):
        """Sets the nsx_security_groups of this ApplicationDeploymentParametersModel_.

        Gets or sets security group id for nsx.  # noqa: E501

        :param nsx_security_groups: The nsx_security_groups of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: int
        """

        self._nsx_security_groups = nsx_security_groups

    @property
    def application_configurations(self):
        """Gets the application_configurations of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets app config entries.  # noqa: E501

        :return: The application_configurations of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: list[ApplicationConfigurationModel_]
        """
        return self._application_configurations

    @application_configurations.setter
    def application_configurations(self, application_configurations):
        """Sets the application_configurations of this ApplicationDeploymentParametersModel_.

        Gets or sets app config entries.  # noqa: E501

        :param application_configurations: The application_configurations of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: list[ApplicationConfigurationModel_]
        """

        self._application_configurations = application_configurations

    @property
    def application_transform_ids(self):
        """Gets the application_transform_ids of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets application Transforms Ids attached to the application.  # noqa: E501

        :return: The application_transform_ids of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: list[int]
        """
        return self._application_transform_ids

    @application_transform_ids.setter
    def application_transform_ids(self, application_transform_ids):
        """Sets the application_transform_ids of this ApplicationDeploymentParametersModel_.

        Gets or sets application Transforms Ids attached to the application.  # noqa: E501

        :param application_transform_ids: The application_transform_ids of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: list[int]
        """

        self._application_transform_ids = application_transform_ids

    @property
    def allow_management(self):
        """Gets the allow_management of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets flag to enable assume management for user installed iOS Apps.  # noqa: E501

        :return: The allow_management of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._allow_management

    @allow_management.setter
    def allow_management(self, allow_management):
        """Sets the allow_management of this ApplicationDeploymentParametersModel_.

        Gets or sets flag to enable assume management for user installed iOS Apps.  # noqa: E501

        :param allow_management: The allow_management of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._allow_management = allow_management

    @property
    def mac_os_desired_state_management(self):
        """Gets the mac_os_desired_state_management of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets flag to enable or disable desired state management for macOS apps.  # noqa: E501

        :return: The mac_os_desired_state_management of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._mac_os_desired_state_management

    @mac_os_desired_state_management.setter
    def mac_os_desired_state_management(self, mac_os_desired_state_management):
        """Sets the mac_os_desired_state_management of this ApplicationDeploymentParametersModel_.

        Gets or sets flag to enable or disable desired state management for macOS apps.  # noqa: E501

        :param mac_os_desired_state_management: The mac_os_desired_state_management of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._mac_os_desired_state_management = mac_os_desired_state_management

    @property
    def requires_approval(self):
        """Gets the requires_approval of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets a value indicating whether [requires approval].  # noqa: E501

        :return: The requires_approval of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._requires_approval

    @requires_approval.setter
    def requires_approval(self, requires_approval):
        """Sets the requires_approval of this ApplicationDeploymentParametersModel_.

        Gets or sets a value indicating whether [requires approval].  # noqa: E501

        :param requires_approval: The requires_approval of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._requires_approval = requires_approval

    @property
    def visible_in_app_catalog(self):
        """Gets the visible_in_app_catalog of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets a value indicating whether gets or sets the value whether to display in app catalog.  # noqa: E501

        :return: The visible_in_app_catalog of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._visible_in_app_catalog

    @visible_in_app_catalog.setter
    def visible_in_app_catalog(self, visible_in_app_catalog):
        """Sets the visible_in_app_catalog of this ApplicationDeploymentParametersModel_.

        Gets or sets a value indicating whether gets or sets the value whether to display in app catalog.  # noqa: E501

        :param visible_in_app_catalog: The visible_in_app_catalog of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._visible_in_app_catalog = visible_in_app_catalog

    @property
    def app_config_blob_id(self):
        """Gets the app_config_blob_id of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets blob ID for the office app configuration values.  # noqa: E501

        :return: The app_config_blob_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: int
        """
        return self._app_config_blob_id

    @app_config_blob_id.setter
    def app_config_blob_id(self, app_config_blob_id):
        """Sets the app_config_blob_id of this ApplicationDeploymentParametersModel_.

        Gets or sets blob ID for the office app configuration values.  # noqa: E501

        :param app_config_blob_id: The app_config_blob_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: int
        """

        self._app_config_blob_id = app_config_blob_id

    @property
    def send_application_attributes(self):
        """Gets the send_application_attributes of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets whether custom application attributes keys and values should be sent to the app.  # noqa: E501

        :return: The send_application_attributes of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._send_application_attributes

    @send_application_attributes.setter
    def send_application_attributes(self, send_application_attributes):
        """Sets the send_application_attributes of this ApplicationDeploymentParametersModel_.

        Gets or sets whether custom application attributes keys and values should be sent to the app.  # noqa: E501

        :param send_application_attributes: The send_application_attributes of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._send_application_attributes = send_application_attributes

    @property
    def prevent_removal(self):
        """Gets the prevent_removal of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets whether prevent removal application attributes key and value should be sent to the app.  # noqa: E501

        :return: The prevent_removal of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: bool
        """
        return self._prevent_removal

    @prevent_removal.setter
    def prevent_removal(self, prevent_removal):
        """Sets the prevent_removal of this ApplicationDeploymentParametersModel_.

        Gets or sets whether prevent removal application attributes key and value should be sent to the app.  # noqa: E501

        :param prevent_removal: The prevent_removal of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: bool
        """

        self._prevent_removal = prevent_removal

    @property
    def application_attributes(self):
        """Gets the application_attributes of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets app attribute entries.  # noqa: E501

        :return: The application_attributes of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: list[ApplicationConfigurationModel_]
        """
        return self._application_attributes

    @application_attributes.setter
    def application_attributes(self, application_attributes):
        """Sets the application_attributes of this ApplicationDeploymentParametersModel_.

        Gets or sets app attribute entries.  # noqa: E501

        :param application_attributes: The application_attributes of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: list[ApplicationConfigurationModel_]
        """

        self._application_attributes = application_attributes

    @property
    def app_attributes_blob_id(self):
        """Gets the app_attributes_blob_id of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets blob ID for the application attributes.  # noqa: E501

        :return: The app_attributes_blob_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: int
        """
        return self._app_attributes_blob_id

    @app_attributes_blob_id.setter
    def app_attributes_blob_id(self, app_attributes_blob_id):
        """Sets the app_attributes_blob_id of this ApplicationDeploymentParametersModel_.

        Gets or sets blob ID for the application attributes.  # noqa: E501

        :param app_attributes_blob_id: The app_attributes_blob_id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: int
        """

        self._app_attributes_blob_id = app_attributes_blob_id

    @property
    def id(self):
        """Gets the id of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationDeploymentParametersModel_.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this ApplicationDeploymentParametersModel_.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this ApplicationDeploymentParametersModel_.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ApplicationDeploymentParametersModel_.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this ApplicationDeploymentParametersModel_.  # noqa: E501
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
        if issubclass(ApplicationDeploymentParametersModel_, dict):
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
        if not isinstance(other, ApplicationDeploymentParametersModel_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationDeploymentParametersModel_):
            return True

        return self.to_dict() != other.to_dict()
