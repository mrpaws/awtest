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


class DeviceSecurityInfo(object):
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
        'is_compromised': 'bool',
        'data_protection_enabled': 'bool',
        'block_level_encryption': 'bool',
        'file_level_encryption': 'bool',
        'is_passcode_present': 'bool',
        'is_passcode_compliant': 'bool',
        'passcode_lock_grace_period': 'int',
        'passcode_lock_grace_period_enforced': 'int',
        'personal_recovery_key': 'str',
        'static_recovery_key': 'str',
        'grace_period_recovery_key': 'str',
        'percent_complete': 'int',
        'dell_ddpe_encryption_status': 'bool',
        'encryption_status': 'str',
        'drive_encryption_level': 'str',
        'is_encrypted': 'bool',
        'has_personal_recovery_key': 'bool',
        'has_institutional_recovery_key': 'bool',
        'personal_recovery_key_device_key': 'str',
        'enrolled_via_dep': 'bool',
        'user_approved_enrollment': 'bool',
        'old_personal_recovery_key_value': 'str',
        'system_integrity_protection_enabled': 'bool',
        'secure_boot': 'SecureBoot_',
        'is_activation_lock_manageable': 'bool',
        'bootstrap_token_escrow_status': 'bool',
        'authenticated_root_volume_enabled': 'bool',
        'bootstrap_token_allowed_for_authentication': 'str',
        'bootstrap_token_required_for_kernel_extension_approval': 'bool',
        'bootstrap_token_required_for_software_update': 'bool',
        'is_recovery_lock_enabled': 'bool',
        'unlock_pin': 'str'
    }

    attribute_map = {
        'is_compromised': 'IsCompromised',
        'data_protection_enabled': 'DataProtectionEnabled',
        'block_level_encryption': 'BlockLevelEncryption',
        'file_level_encryption': 'FileLevelEncryption',
        'is_passcode_present': 'IsPasscodePresent',
        'is_passcode_compliant': 'IsPasscodeCompliant',
        'passcode_lock_grace_period': 'PasscodeLockGracePeriod',
        'passcode_lock_grace_period_enforced': 'PasscodeLockGracePeriodEnforced',
        'personal_recovery_key': 'PersonalRecoveryKey',
        'static_recovery_key': 'StaticRecoveryKey',
        'grace_period_recovery_key': 'GracePeriodRecoveryKey',
        'percent_complete': 'PercentComplete',
        'dell_ddpe_encryption_status': 'DellDdpeEncryptionStatus',
        'encryption_status': 'EncryptionStatus',
        'drive_encryption_level': 'DriveEncryptionLevel',
        'is_encrypted': 'IsEncrypted',
        'has_personal_recovery_key': 'HasPersonalRecoveryKey',
        'has_institutional_recovery_key': 'HasInstitutionalRecoveryKey',
        'personal_recovery_key_device_key': 'PersonalRecoveryKeyDeviceKey',
        'enrolled_via_dep': 'EnrolledViaDEP',
        'user_approved_enrollment': 'UserApprovedEnrollment',
        'old_personal_recovery_key_value': 'OldPersonalRecoveryKeyValue',
        'system_integrity_protection_enabled': 'SystemIntegrityProtectionEnabled',
        'secure_boot': 'SecureBoot',
        'is_activation_lock_manageable': 'IsActivationLockManageable',
        'bootstrap_token_escrow_status': 'BootstrapTokenEscrowStatus',
        'authenticated_root_volume_enabled': 'AuthenticatedRootVolumeEnabled',
        'bootstrap_token_allowed_for_authentication': 'BootstrapTokenAllowedForAuthentication',
        'bootstrap_token_required_for_kernel_extension_approval': 'BootstrapTokenRequiredForKernelExtensionApproval',
        'bootstrap_token_required_for_software_update': 'BootstrapTokenRequiredForSoftwareUpdate',
        'is_recovery_lock_enabled': 'IsRecoveryLockEnabled',
        'unlock_pin': 'UnlockPin'
    }

    def __init__(self, is_compromised=None, data_protection_enabled=None, block_level_encryption=None, file_level_encryption=None, is_passcode_present=None, is_passcode_compliant=None, passcode_lock_grace_period=None, passcode_lock_grace_period_enforced=None, personal_recovery_key=None, static_recovery_key=None, grace_period_recovery_key=None, percent_complete=None, dell_ddpe_encryption_status=None, encryption_status=None, drive_encryption_level=None, is_encrypted=None, has_personal_recovery_key=None, has_institutional_recovery_key=None, personal_recovery_key_device_key=None, enrolled_via_dep=None, user_approved_enrollment=None, old_personal_recovery_key_value=None, system_integrity_protection_enabled=None, secure_boot=None, is_activation_lock_manageable=None, bootstrap_token_escrow_status=None, authenticated_root_volume_enabled=None, bootstrap_token_allowed_for_authentication=None, bootstrap_token_required_for_kernel_extension_approval=None, bootstrap_token_required_for_software_update=None, is_recovery_lock_enabled=None, unlock_pin=None, _configuration=None):  # noqa: E501
        """DeviceSecurityInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_compromised = None
        self._data_protection_enabled = None
        self._block_level_encryption = None
        self._file_level_encryption = None
        self._is_passcode_present = None
        self._is_passcode_compliant = None
        self._passcode_lock_grace_period = None
        self._passcode_lock_grace_period_enforced = None
        self._personal_recovery_key = None
        self._static_recovery_key = None
        self._grace_period_recovery_key = None
        self._percent_complete = None
        self._dell_ddpe_encryption_status = None
        self._encryption_status = None
        self._drive_encryption_level = None
        self._is_encrypted = None
        self._has_personal_recovery_key = None
        self._has_institutional_recovery_key = None
        self._personal_recovery_key_device_key = None
        self._enrolled_via_dep = None
        self._user_approved_enrollment = None
        self._old_personal_recovery_key_value = None
        self._system_integrity_protection_enabled = None
        self._secure_boot = None
        self._is_activation_lock_manageable = None
        self._bootstrap_token_escrow_status = None
        self._authenticated_root_volume_enabled = None
        self._bootstrap_token_allowed_for_authentication = None
        self._bootstrap_token_required_for_kernel_extension_approval = None
        self._bootstrap_token_required_for_software_update = None
        self._is_recovery_lock_enabled = None
        self._unlock_pin = None
        self.discriminator = None

        if is_compromised is not None:
            self.is_compromised = is_compromised
        if data_protection_enabled is not None:
            self.data_protection_enabled = data_protection_enabled
        if block_level_encryption is not None:
            self.block_level_encryption = block_level_encryption
        if file_level_encryption is not None:
            self.file_level_encryption = file_level_encryption
        if is_passcode_present is not None:
            self.is_passcode_present = is_passcode_present
        if is_passcode_compliant is not None:
            self.is_passcode_compliant = is_passcode_compliant
        if passcode_lock_grace_period is not None:
            self.passcode_lock_grace_period = passcode_lock_grace_period
        if passcode_lock_grace_period_enforced is not None:
            self.passcode_lock_grace_period_enforced = passcode_lock_grace_period_enforced
        if personal_recovery_key is not None:
            self.personal_recovery_key = personal_recovery_key
        if static_recovery_key is not None:
            self.static_recovery_key = static_recovery_key
        if grace_period_recovery_key is not None:
            self.grace_period_recovery_key = grace_period_recovery_key
        if percent_complete is not None:
            self.percent_complete = percent_complete
        if dell_ddpe_encryption_status is not None:
            self.dell_ddpe_encryption_status = dell_ddpe_encryption_status
        if encryption_status is not None:
            self.encryption_status = encryption_status
        if drive_encryption_level is not None:
            self.drive_encryption_level = drive_encryption_level
        if is_encrypted is not None:
            self.is_encrypted = is_encrypted
        if has_personal_recovery_key is not None:
            self.has_personal_recovery_key = has_personal_recovery_key
        if has_institutional_recovery_key is not None:
            self.has_institutional_recovery_key = has_institutional_recovery_key
        if personal_recovery_key_device_key is not None:
            self.personal_recovery_key_device_key = personal_recovery_key_device_key
        if enrolled_via_dep is not None:
            self.enrolled_via_dep = enrolled_via_dep
        if user_approved_enrollment is not None:
            self.user_approved_enrollment = user_approved_enrollment
        if old_personal_recovery_key_value is not None:
            self.old_personal_recovery_key_value = old_personal_recovery_key_value
        if system_integrity_protection_enabled is not None:
            self.system_integrity_protection_enabled = system_integrity_protection_enabled
        if secure_boot is not None:
            self.secure_boot = secure_boot
        if is_activation_lock_manageable is not None:
            self.is_activation_lock_manageable = is_activation_lock_manageable
        if bootstrap_token_escrow_status is not None:
            self.bootstrap_token_escrow_status = bootstrap_token_escrow_status
        if authenticated_root_volume_enabled is not None:
            self.authenticated_root_volume_enabled = authenticated_root_volume_enabled
        if bootstrap_token_allowed_for_authentication is not None:
            self.bootstrap_token_allowed_for_authentication = bootstrap_token_allowed_for_authentication
        if bootstrap_token_required_for_kernel_extension_approval is not None:
            self.bootstrap_token_required_for_kernel_extension_approval = bootstrap_token_required_for_kernel_extension_approval
        if bootstrap_token_required_for_software_update is not None:
            self.bootstrap_token_required_for_software_update = bootstrap_token_required_for_software_update
        if is_recovery_lock_enabled is not None:
            self.is_recovery_lock_enabled = is_recovery_lock_enabled
        if unlock_pin is not None:
            self.unlock_pin = unlock_pin

    @property
    def is_compromised(self):
        """Gets the is_compromised of this DeviceSecurityInfo.  # noqa: E501


        :return: The is_compromised of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_compromised

    @is_compromised.setter
    def is_compromised(self, is_compromised):
        """Sets the is_compromised of this DeviceSecurityInfo.


        :param is_compromised: The is_compromised of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._is_compromised = is_compromised

    @property
    def data_protection_enabled(self):
        """Gets the data_protection_enabled of this DeviceSecurityInfo.  # noqa: E501


        :return: The data_protection_enabled of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._data_protection_enabled

    @data_protection_enabled.setter
    def data_protection_enabled(self, data_protection_enabled):
        """Sets the data_protection_enabled of this DeviceSecurityInfo.


        :param data_protection_enabled: The data_protection_enabled of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._data_protection_enabled = data_protection_enabled

    @property
    def block_level_encryption(self):
        """Gets the block_level_encryption of this DeviceSecurityInfo.  # noqa: E501


        :return: The block_level_encryption of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._block_level_encryption

    @block_level_encryption.setter
    def block_level_encryption(self, block_level_encryption):
        """Sets the block_level_encryption of this DeviceSecurityInfo.


        :param block_level_encryption: The block_level_encryption of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._block_level_encryption = block_level_encryption

    @property
    def file_level_encryption(self):
        """Gets the file_level_encryption of this DeviceSecurityInfo.  # noqa: E501


        :return: The file_level_encryption of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._file_level_encryption

    @file_level_encryption.setter
    def file_level_encryption(self, file_level_encryption):
        """Sets the file_level_encryption of this DeviceSecurityInfo.


        :param file_level_encryption: The file_level_encryption of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._file_level_encryption = file_level_encryption

    @property
    def is_passcode_present(self):
        """Gets the is_passcode_present of this DeviceSecurityInfo.  # noqa: E501


        :return: The is_passcode_present of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_passcode_present

    @is_passcode_present.setter
    def is_passcode_present(self, is_passcode_present):
        """Sets the is_passcode_present of this DeviceSecurityInfo.


        :param is_passcode_present: The is_passcode_present of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._is_passcode_present = is_passcode_present

    @property
    def is_passcode_compliant(self):
        """Gets the is_passcode_compliant of this DeviceSecurityInfo.  # noqa: E501


        :return: The is_passcode_compliant of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_passcode_compliant

    @is_passcode_compliant.setter
    def is_passcode_compliant(self, is_passcode_compliant):
        """Sets the is_passcode_compliant of this DeviceSecurityInfo.


        :param is_passcode_compliant: The is_passcode_compliant of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._is_passcode_compliant = is_passcode_compliant

    @property
    def passcode_lock_grace_period(self):
        """Gets the passcode_lock_grace_period of this DeviceSecurityInfo.  # noqa: E501


        :return: The passcode_lock_grace_period of this DeviceSecurityInfo.  # noqa: E501
        :rtype: int
        """
        return self._passcode_lock_grace_period

    @passcode_lock_grace_period.setter
    def passcode_lock_grace_period(self, passcode_lock_grace_period):
        """Sets the passcode_lock_grace_period of this DeviceSecurityInfo.


        :param passcode_lock_grace_period: The passcode_lock_grace_period of this DeviceSecurityInfo.  # noqa: E501
        :type: int
        """

        self._passcode_lock_grace_period = passcode_lock_grace_period

    @property
    def passcode_lock_grace_period_enforced(self):
        """Gets the passcode_lock_grace_period_enforced of this DeviceSecurityInfo.  # noqa: E501


        :return: The passcode_lock_grace_period_enforced of this DeviceSecurityInfo.  # noqa: E501
        :rtype: int
        """
        return self._passcode_lock_grace_period_enforced

    @passcode_lock_grace_period_enforced.setter
    def passcode_lock_grace_period_enforced(self, passcode_lock_grace_period_enforced):
        """Sets the passcode_lock_grace_period_enforced of this DeviceSecurityInfo.


        :param passcode_lock_grace_period_enforced: The passcode_lock_grace_period_enforced of this DeviceSecurityInfo.  # noqa: E501
        :type: int
        """

        self._passcode_lock_grace_period_enforced = passcode_lock_grace_period_enforced

    @property
    def personal_recovery_key(self):
        """Gets the personal_recovery_key of this DeviceSecurityInfo.  # noqa: E501


        :return: The personal_recovery_key of this DeviceSecurityInfo.  # noqa: E501
        :rtype: str
        """
        return self._personal_recovery_key

    @personal_recovery_key.setter
    def personal_recovery_key(self, personal_recovery_key):
        """Sets the personal_recovery_key of this DeviceSecurityInfo.


        :param personal_recovery_key: The personal_recovery_key of this DeviceSecurityInfo.  # noqa: E501
        :type: str
        """

        self._personal_recovery_key = personal_recovery_key

    @property
    def static_recovery_key(self):
        """Gets the static_recovery_key of this DeviceSecurityInfo.  # noqa: E501


        :return: The static_recovery_key of this DeviceSecurityInfo.  # noqa: E501
        :rtype: str
        """
        return self._static_recovery_key

    @static_recovery_key.setter
    def static_recovery_key(self, static_recovery_key):
        """Sets the static_recovery_key of this DeviceSecurityInfo.


        :param static_recovery_key: The static_recovery_key of this DeviceSecurityInfo.  # noqa: E501
        :type: str
        """

        self._static_recovery_key = static_recovery_key

    @property
    def grace_period_recovery_key(self):
        """Gets the grace_period_recovery_key of this DeviceSecurityInfo.  # noqa: E501


        :return: The grace_period_recovery_key of this DeviceSecurityInfo.  # noqa: E501
        :rtype: str
        """
        return self._grace_period_recovery_key

    @grace_period_recovery_key.setter
    def grace_period_recovery_key(self, grace_period_recovery_key):
        """Sets the grace_period_recovery_key of this DeviceSecurityInfo.


        :param grace_period_recovery_key: The grace_period_recovery_key of this DeviceSecurityInfo.  # noqa: E501
        :type: str
        """

        self._grace_period_recovery_key = grace_period_recovery_key

    @property
    def percent_complete(self):
        """Gets the percent_complete of this DeviceSecurityInfo.  # noqa: E501


        :return: The percent_complete of this DeviceSecurityInfo.  # noqa: E501
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this DeviceSecurityInfo.


        :param percent_complete: The percent_complete of this DeviceSecurityInfo.  # noqa: E501
        :type: int
        """

        self._percent_complete = percent_complete

    @property
    def dell_ddpe_encryption_status(self):
        """Gets the dell_ddpe_encryption_status of this DeviceSecurityInfo.  # noqa: E501


        :return: The dell_ddpe_encryption_status of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._dell_ddpe_encryption_status

    @dell_ddpe_encryption_status.setter
    def dell_ddpe_encryption_status(self, dell_ddpe_encryption_status):
        """Sets the dell_ddpe_encryption_status of this DeviceSecurityInfo.


        :param dell_ddpe_encryption_status: The dell_ddpe_encryption_status of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._dell_ddpe_encryption_status = dell_ddpe_encryption_status

    @property
    def encryption_status(self):
        """Gets the encryption_status of this DeviceSecurityInfo.  # noqa: E501


        :return: The encryption_status of this DeviceSecurityInfo.  # noqa: E501
        :rtype: str
        """
        return self._encryption_status

    @encryption_status.setter
    def encryption_status(self, encryption_status):
        """Sets the encryption_status of this DeviceSecurityInfo.


        :param encryption_status: The encryption_status of this DeviceSecurityInfo.  # noqa: E501
        :type: str
        """

        self._encryption_status = encryption_status

    @property
    def drive_encryption_level(self):
        """Gets the drive_encryption_level of this DeviceSecurityInfo.  # noqa: E501


        :return: The drive_encryption_level of this DeviceSecurityInfo.  # noqa: E501
        :rtype: str
        """
        return self._drive_encryption_level

    @drive_encryption_level.setter
    def drive_encryption_level(self, drive_encryption_level):
        """Sets the drive_encryption_level of this DeviceSecurityInfo.


        :param drive_encryption_level: The drive_encryption_level of this DeviceSecurityInfo.  # noqa: E501
        :type: str
        """

        self._drive_encryption_level = drive_encryption_level

    @property
    def is_encrypted(self):
        """Gets the is_encrypted of this DeviceSecurityInfo.  # noqa: E501


        :return: The is_encrypted of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """Sets the is_encrypted of this DeviceSecurityInfo.


        :param is_encrypted: The is_encrypted of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._is_encrypted = is_encrypted

    @property
    def has_personal_recovery_key(self):
        """Gets the has_personal_recovery_key of this DeviceSecurityInfo.  # noqa: E501


        :return: The has_personal_recovery_key of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_personal_recovery_key

    @has_personal_recovery_key.setter
    def has_personal_recovery_key(self, has_personal_recovery_key):
        """Sets the has_personal_recovery_key of this DeviceSecurityInfo.


        :param has_personal_recovery_key: The has_personal_recovery_key of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._has_personal_recovery_key = has_personal_recovery_key

    @property
    def has_institutional_recovery_key(self):
        """Gets the has_institutional_recovery_key of this DeviceSecurityInfo.  # noqa: E501


        :return: The has_institutional_recovery_key of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_institutional_recovery_key

    @has_institutional_recovery_key.setter
    def has_institutional_recovery_key(self, has_institutional_recovery_key):
        """Sets the has_institutional_recovery_key of this DeviceSecurityInfo.


        :param has_institutional_recovery_key: The has_institutional_recovery_key of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._has_institutional_recovery_key = has_institutional_recovery_key

    @property
    def personal_recovery_key_device_key(self):
        """Gets the personal_recovery_key_device_key of this DeviceSecurityInfo.  # noqa: E501


        :return: The personal_recovery_key_device_key of this DeviceSecurityInfo.  # noqa: E501
        :rtype: str
        """
        return self._personal_recovery_key_device_key

    @personal_recovery_key_device_key.setter
    def personal_recovery_key_device_key(self, personal_recovery_key_device_key):
        """Sets the personal_recovery_key_device_key of this DeviceSecurityInfo.


        :param personal_recovery_key_device_key: The personal_recovery_key_device_key of this DeviceSecurityInfo.  # noqa: E501
        :type: str
        """

        self._personal_recovery_key_device_key = personal_recovery_key_device_key

    @property
    def enrolled_via_dep(self):
        """Gets the enrolled_via_dep of this DeviceSecurityInfo.  # noqa: E501


        :return: The enrolled_via_dep of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enrolled_via_dep

    @enrolled_via_dep.setter
    def enrolled_via_dep(self, enrolled_via_dep):
        """Sets the enrolled_via_dep of this DeviceSecurityInfo.


        :param enrolled_via_dep: The enrolled_via_dep of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._enrolled_via_dep = enrolled_via_dep

    @property
    def user_approved_enrollment(self):
        """Gets the user_approved_enrollment of this DeviceSecurityInfo.  # noqa: E501


        :return: The user_approved_enrollment of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._user_approved_enrollment

    @user_approved_enrollment.setter
    def user_approved_enrollment(self, user_approved_enrollment):
        """Sets the user_approved_enrollment of this DeviceSecurityInfo.


        :param user_approved_enrollment: The user_approved_enrollment of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._user_approved_enrollment = user_approved_enrollment

    @property
    def old_personal_recovery_key_value(self):
        """Gets the old_personal_recovery_key_value of this DeviceSecurityInfo.  # noqa: E501


        :return: The old_personal_recovery_key_value of this DeviceSecurityInfo.  # noqa: E501
        :rtype: str
        """
        return self._old_personal_recovery_key_value

    @old_personal_recovery_key_value.setter
    def old_personal_recovery_key_value(self, old_personal_recovery_key_value):
        """Sets the old_personal_recovery_key_value of this DeviceSecurityInfo.


        :param old_personal_recovery_key_value: The old_personal_recovery_key_value of this DeviceSecurityInfo.  # noqa: E501
        :type: str
        """

        self._old_personal_recovery_key_value = old_personal_recovery_key_value

    @property
    def system_integrity_protection_enabled(self):
        """Gets the system_integrity_protection_enabled of this DeviceSecurityInfo.  # noqa: E501


        :return: The system_integrity_protection_enabled of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._system_integrity_protection_enabled

    @system_integrity_protection_enabled.setter
    def system_integrity_protection_enabled(self, system_integrity_protection_enabled):
        """Sets the system_integrity_protection_enabled of this DeviceSecurityInfo.


        :param system_integrity_protection_enabled: The system_integrity_protection_enabled of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._system_integrity_protection_enabled = system_integrity_protection_enabled

    @property
    def secure_boot(self):
        """Gets the secure_boot of this DeviceSecurityInfo.  # noqa: E501


        :return: The secure_boot of this DeviceSecurityInfo.  # noqa: E501
        :rtype: SecureBoot_
        """
        return self._secure_boot

    @secure_boot.setter
    def secure_boot(self, secure_boot):
        """Sets the secure_boot of this DeviceSecurityInfo.


        :param secure_boot: The secure_boot of this DeviceSecurityInfo.  # noqa: E501
        :type: SecureBoot_
        """

        self._secure_boot = secure_boot

    @property
    def is_activation_lock_manageable(self):
        """Gets the is_activation_lock_manageable of this DeviceSecurityInfo.  # noqa: E501


        :return: The is_activation_lock_manageable of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_activation_lock_manageable

    @is_activation_lock_manageable.setter
    def is_activation_lock_manageable(self, is_activation_lock_manageable):
        """Sets the is_activation_lock_manageable of this DeviceSecurityInfo.


        :param is_activation_lock_manageable: The is_activation_lock_manageable of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._is_activation_lock_manageable = is_activation_lock_manageable

    @property
    def bootstrap_token_escrow_status(self):
        """Gets the bootstrap_token_escrow_status of this DeviceSecurityInfo.  # noqa: E501


        :return: The bootstrap_token_escrow_status of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._bootstrap_token_escrow_status

    @bootstrap_token_escrow_status.setter
    def bootstrap_token_escrow_status(self, bootstrap_token_escrow_status):
        """Sets the bootstrap_token_escrow_status of this DeviceSecurityInfo.


        :param bootstrap_token_escrow_status: The bootstrap_token_escrow_status of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._bootstrap_token_escrow_status = bootstrap_token_escrow_status

    @property
    def authenticated_root_volume_enabled(self):
        """Gets the authenticated_root_volume_enabled of this DeviceSecurityInfo.  # noqa: E501


        :return: The authenticated_root_volume_enabled of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._authenticated_root_volume_enabled

    @authenticated_root_volume_enabled.setter
    def authenticated_root_volume_enabled(self, authenticated_root_volume_enabled):
        """Sets the authenticated_root_volume_enabled of this DeviceSecurityInfo.


        :param authenticated_root_volume_enabled: The authenticated_root_volume_enabled of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._authenticated_root_volume_enabled = authenticated_root_volume_enabled

    @property
    def bootstrap_token_allowed_for_authentication(self):
        """Gets the bootstrap_token_allowed_for_authentication of this DeviceSecurityInfo.  # noqa: E501


        :return: The bootstrap_token_allowed_for_authentication of this DeviceSecurityInfo.  # noqa: E501
        :rtype: str
        """
        return self._bootstrap_token_allowed_for_authentication

    @bootstrap_token_allowed_for_authentication.setter
    def bootstrap_token_allowed_for_authentication(self, bootstrap_token_allowed_for_authentication):
        """Sets the bootstrap_token_allowed_for_authentication of this DeviceSecurityInfo.


        :param bootstrap_token_allowed_for_authentication: The bootstrap_token_allowed_for_authentication of this DeviceSecurityInfo.  # noqa: E501
        :type: str
        """

        self._bootstrap_token_allowed_for_authentication = bootstrap_token_allowed_for_authentication

    @property
    def bootstrap_token_required_for_kernel_extension_approval(self):
        """Gets the bootstrap_token_required_for_kernel_extension_approval of this DeviceSecurityInfo.  # noqa: E501


        :return: The bootstrap_token_required_for_kernel_extension_approval of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._bootstrap_token_required_for_kernel_extension_approval

    @bootstrap_token_required_for_kernel_extension_approval.setter
    def bootstrap_token_required_for_kernel_extension_approval(self, bootstrap_token_required_for_kernel_extension_approval):
        """Sets the bootstrap_token_required_for_kernel_extension_approval of this DeviceSecurityInfo.


        :param bootstrap_token_required_for_kernel_extension_approval: The bootstrap_token_required_for_kernel_extension_approval of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._bootstrap_token_required_for_kernel_extension_approval = bootstrap_token_required_for_kernel_extension_approval

    @property
    def bootstrap_token_required_for_software_update(self):
        """Gets the bootstrap_token_required_for_software_update of this DeviceSecurityInfo.  # noqa: E501


        :return: The bootstrap_token_required_for_software_update of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._bootstrap_token_required_for_software_update

    @bootstrap_token_required_for_software_update.setter
    def bootstrap_token_required_for_software_update(self, bootstrap_token_required_for_software_update):
        """Sets the bootstrap_token_required_for_software_update of this DeviceSecurityInfo.


        :param bootstrap_token_required_for_software_update: The bootstrap_token_required_for_software_update of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._bootstrap_token_required_for_software_update = bootstrap_token_required_for_software_update

    @property
    def is_recovery_lock_enabled(self):
        """Gets the is_recovery_lock_enabled of this DeviceSecurityInfo.  # noqa: E501


        :return: The is_recovery_lock_enabled of this DeviceSecurityInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_recovery_lock_enabled

    @is_recovery_lock_enabled.setter
    def is_recovery_lock_enabled(self, is_recovery_lock_enabled):
        """Sets the is_recovery_lock_enabled of this DeviceSecurityInfo.


        :param is_recovery_lock_enabled: The is_recovery_lock_enabled of this DeviceSecurityInfo.  # noqa: E501
        :type: bool
        """

        self._is_recovery_lock_enabled = is_recovery_lock_enabled

    @property
    def unlock_pin(self):
        """Gets the unlock_pin of this DeviceSecurityInfo.  # noqa: E501


        :return: The unlock_pin of this DeviceSecurityInfo.  # noqa: E501
        :rtype: str
        """
        return self._unlock_pin

    @unlock_pin.setter
    def unlock_pin(self, unlock_pin):
        """Sets the unlock_pin of this DeviceSecurityInfo.


        :param unlock_pin: The unlock_pin of this DeviceSecurityInfo.  # noqa: E501
        :type: str
        """

        self._unlock_pin = unlock_pin

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
        if issubclass(DeviceSecurityInfo, dict):
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
        if not isinstance(other, DeviceSecurityInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceSecurityInfo):
            return True

        return self.to_dict() != other.to_dict()
