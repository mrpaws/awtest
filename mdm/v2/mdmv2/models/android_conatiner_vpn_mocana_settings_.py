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


class AndroidConatinerVPNMocanaSettings_(object):
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
        'backup_server_name': 'str',
        'default_route_enabled': 'bool',
        'ike_version': 'int',
        'dead_peer_detection': 'bool',
        'pfs_exchange': 'bool',
        'suite_b': 'str',
        'phase_one_mode': 'str',
        'dh_group': 'int'
    }

    attribute_map = {
        'backup_server_name': 'BackupServerName',
        'default_route_enabled': 'DefaultRouteEnabled',
        'ike_version': 'IKEVersion',
        'dead_peer_detection': 'DeadPeerDetection',
        'pfs_exchange': 'PFSExchange',
        'suite_b': 'SuiteB',
        'phase_one_mode': 'PhaseOneMode',
        'dh_group': 'DhGroup'
    }

    def __init__(self, backup_server_name=None, default_route_enabled=None, ike_version=None, dead_peer_detection=None, pfs_exchange=None, suite_b=None, phase_one_mode=None, dh_group=None, _configuration=None):  # noqa: E501
        """AndroidConatinerVPNMocanaSettings_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_server_name = None
        self._default_route_enabled = None
        self._ike_version = None
        self._dead_peer_detection = None
        self._pfs_exchange = None
        self._suite_b = None
        self._phase_one_mode = None
        self._dh_group = None
        self.discriminator = None

        if backup_server_name is not None:
            self.backup_server_name = backup_server_name
        if default_route_enabled is not None:
            self.default_route_enabled = default_route_enabled
        if ike_version is not None:
            self.ike_version = ike_version
        if dead_peer_detection is not None:
            self.dead_peer_detection = dead_peer_detection
        if pfs_exchange is not None:
            self.pfs_exchange = pfs_exchange
        if suite_b is not None:
            self.suite_b = suite_b
        if phase_one_mode is not None:
            self.phase_one_mode = phase_one_mode
        if dh_group is not None:
            self.dh_group = dh_group

    @property
    def backup_server_name(self):
        """Gets the backup_server_name of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501

        Gets or sets the name of the backup server.  # noqa: E501

        :return: The backup_server_name of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :rtype: str
        """
        return self._backup_server_name

    @backup_server_name.setter
    def backup_server_name(self, backup_server_name):
        """Sets the backup_server_name of this AndroidConatinerVPNMocanaSettings_.

        Gets or sets the name of the backup server.  # noqa: E501

        :param backup_server_name: The backup_server_name of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :type: str
        """

        self._backup_server_name = backup_server_name

    @property
    def default_route_enabled(self):
        """Gets the default_route_enabled of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501

        Gets or sets the default route.  # noqa: E501

        :return: The default_route_enabled of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :rtype: bool
        """
        return self._default_route_enabled

    @default_route_enabled.setter
    def default_route_enabled(self, default_route_enabled):
        """Sets the default_route_enabled of this AndroidConatinerVPNMocanaSettings_.

        Gets or sets the default route.  # noqa: E501

        :param default_route_enabled: The default_route_enabled of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :type: bool
        """

        self._default_route_enabled = default_route_enabled

    @property
    def ike_version(self):
        """Gets the ike_version of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501

        Gets or sets the ike version.  # noqa: E501

        :return: The ike_version of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :rtype: int
        """
        return self._ike_version

    @ike_version.setter
    def ike_version(self, ike_version):
        """Sets the ike_version of this AndroidConatinerVPNMocanaSettings_.

        Gets or sets the ike version.  # noqa: E501

        :param ike_version: The ike_version of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :type: int
        """

        self._ike_version = ike_version

    @property
    def dead_peer_detection(self):
        """Gets the dead_peer_detection of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501

        Gets or sets the dead peer detection.  # noqa: E501

        :return: The dead_peer_detection of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :rtype: bool
        """
        return self._dead_peer_detection

    @dead_peer_detection.setter
    def dead_peer_detection(self, dead_peer_detection):
        """Sets the dead_peer_detection of this AndroidConatinerVPNMocanaSettings_.

        Gets or sets the dead peer detection.  # noqa: E501

        :param dead_peer_detection: The dead_peer_detection of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :type: bool
        """

        self._dead_peer_detection = dead_peer_detection

    @property
    def pfs_exchange(self):
        """Gets the pfs_exchange of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501

        Gets or sets the PFS exchange.  # noqa: E501

        :return: The pfs_exchange of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :rtype: bool
        """
        return self._pfs_exchange

    @pfs_exchange.setter
    def pfs_exchange(self, pfs_exchange):
        """Sets the pfs_exchange of this AndroidConatinerVPNMocanaSettings_.

        Gets or sets the PFS exchange.  # noqa: E501

        :param pfs_exchange: The pfs_exchange of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :type: bool
        """

        self._pfs_exchange = pfs_exchange

    @property
    def suite_b(self):
        """Gets the suite_b of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501

        Gets or sets the suite b.  # noqa: E501

        :return: The suite_b of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :rtype: str
        """
        return self._suite_b

    @suite_b.setter
    def suite_b(self, suite_b):
        """Sets the suite_b of this AndroidConatinerVPNMocanaSettings_.

        Gets or sets the suite b.  # noqa: E501

        :param suite_b: The suite_b of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :type: str
        """

        self._suite_b = suite_b

    @property
    def phase_one_mode(self):
        """Gets the phase_one_mode of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501

        Gets or sets the phase1 mode.  # noqa: E501

        :return: The phase_one_mode of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :rtype: str
        """
        return self._phase_one_mode

    @phase_one_mode.setter
    def phase_one_mode(self, phase_one_mode):
        """Sets the phase_one_mode of this AndroidConatinerVPNMocanaSettings_.

        Gets or sets the phase1 mode.  # noqa: E501

        :param phase_one_mode: The phase_one_mode of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :type: str
        """

        self._phase_one_mode = phase_one_mode

    @property
    def dh_group(self):
        """Gets the dh_group of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501

        Gets or sets the dh group.  # noqa: E501

        :return: The dh_group of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :rtype: int
        """
        return self._dh_group

    @dh_group.setter
    def dh_group(self, dh_group):
        """Sets the dh_group of this AndroidConatinerVPNMocanaSettings_.

        Gets or sets the dh group.  # noqa: E501

        :param dh_group: The dh_group of this AndroidConatinerVPNMocanaSettings_.  # noqa: E501
        :type: int
        """

        self._dh_group = dh_group

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
        if issubclass(AndroidConatinerVPNMocanaSettings_, dict):
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
        if not isinstance(other, AndroidConatinerVPNMocanaSettings_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidConatinerVPNMocanaSettings_):
            return True

        return self.to_dict() != other.to_dict()
