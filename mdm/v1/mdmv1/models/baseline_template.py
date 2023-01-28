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


class BaselineTemplate(object):
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
        'id': 'int',
        'uuid': 'str',
        'type': 'int',
        'vendor_template': 'BaselineVendorTemplateV1Model',
        'os_version': 'OSVersionV1Model',
        'security_level': 'SecurityLevelV1Model',
        'version': 'int',
        'policy_tree': 'list[CategoryTreeItem]'
    }

    attribute_map = {
        'id': 'id',
        'uuid': 'uuid',
        'type': 'type',
        'vendor_template': 'vendorTemplate',
        'os_version': 'osVersion',
        'security_level': 'securityLevel',
        'version': 'version',
        'policy_tree': 'policyTree'
    }

    def __init__(self, id=None, uuid=None, type=None, vendor_template=None, os_version=None, security_level=None, version=None, policy_tree=None, _configuration=None):  # noqa: E501
        """BaselineTemplate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._uuid = None
        self._type = None
        self._vendor_template = None
        self._os_version = None
        self._security_level = None
        self._version = None
        self._policy_tree = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid
        if type is not None:
            self.type = type
        if vendor_template is not None:
            self.vendor_template = vendor_template
        if os_version is not None:
            self.os_version = os_version
        if security_level is not None:
            self.security_level = security_level
        if version is not None:
            self.version = version
        if policy_tree is not None:
            self.policy_tree = policy_tree

    @property
    def id(self):
        """Gets the id of this BaselineTemplate.  # noqa: E501

          # noqa: E501

        :return: The id of this BaselineTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaselineTemplate.

          # noqa: E501

        :param id: The id of this BaselineTemplate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this BaselineTemplate.  # noqa: E501

        Unique identifier of the baseline  # noqa: E501

        :return: The uuid of this BaselineTemplate.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this BaselineTemplate.

        Unique identifier of the baseline  # noqa: E501

        :param uuid: The uuid of this BaselineTemplate.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def type(self):
        """Gets the type of this BaselineTemplate.  # noqa: E501

        Type of the Baseline  # noqa: E501

        :return: The type of this BaselineTemplate.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BaselineTemplate.

        Type of the Baseline  # noqa: E501

        :param type: The type of this BaselineTemplate.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def vendor_template(self):
        """Gets the vendor_template of this BaselineTemplate.  # noqa: E501

          # noqa: E501

        :return: The vendor_template of this BaselineTemplate.  # noqa: E501
        :rtype: BaselineVendorTemplateV1Model
        """
        return self._vendor_template

    @vendor_template.setter
    def vendor_template(self, vendor_template):
        """Sets the vendor_template of this BaselineTemplate.

          # noqa: E501

        :param vendor_template: The vendor_template of this BaselineTemplate.  # noqa: E501
        :type: BaselineVendorTemplateV1Model
        """

        self._vendor_template = vendor_template

    @property
    def os_version(self):
        """Gets the os_version of this BaselineTemplate.  # noqa: E501

          # noqa: E501

        :return: The os_version of this BaselineTemplate.  # noqa: E501
        :rtype: OSVersionV1Model
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this BaselineTemplate.

          # noqa: E501

        :param os_version: The os_version of this BaselineTemplate.  # noqa: E501
        :type: OSVersionV1Model
        """

        self._os_version = os_version

    @property
    def security_level(self):
        """Gets the security_level of this BaselineTemplate.  # noqa: E501

          # noqa: E501

        :return: The security_level of this BaselineTemplate.  # noqa: E501
        :rtype: SecurityLevelV1Model
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this BaselineTemplate.

          # noqa: E501

        :param security_level: The security_level of this BaselineTemplate.  # noqa: E501
        :type: SecurityLevelV1Model
        """

        self._security_level = security_level

    @property
    def version(self):
        """Gets the version of this BaselineTemplate.  # noqa: E501

        Current version of the baseline template  # noqa: E501

        :return: The version of this BaselineTemplate.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BaselineTemplate.

        Current version of the baseline template  # noqa: E501

        :param version: The version of this BaselineTemplate.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def policy_tree(self):
        """Gets the policy_tree of this BaselineTemplate.  # noqa: E501

        A hierarchical list of category and policies  # noqa: E501

        :return: The policy_tree of this BaselineTemplate.  # noqa: E501
        :rtype: list[CategoryTreeItem]
        """
        return self._policy_tree

    @policy_tree.setter
    def policy_tree(self, policy_tree):
        """Sets the policy_tree of this BaselineTemplate.

        A hierarchical list of category and policies  # noqa: E501

        :param policy_tree: The policy_tree of this BaselineTemplate.  # noqa: E501
        :type: list[CategoryTreeItem]
        """

        self._policy_tree = policy_tree

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
        if issubclass(BaselineTemplate, dict):
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
        if not isinstance(other, BaselineTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaselineTemplate):
            return True

        return self.to_dict() != other.to_dict()
