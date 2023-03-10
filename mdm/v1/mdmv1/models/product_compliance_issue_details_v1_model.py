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


class ProductComplianceIssueDetailsV1Model(object):
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
        'device_id': 'int',
        'friendly_name': 'str',
        'organization_group': 'str',
        'device_type_id': 'int',
        'device_type': 'str',
        'parent_proxy_device_id': 'int',
        'parent_proxy_uu_id': 'str',
        'product_id': 'int',
        'product': 'str',
        'product_compliance_status_id': 'int',
        'product_compliance_status': 'str'
    }

    attribute_map = {
        'device_id': 'DeviceId',
        'friendly_name': 'FriendlyName',
        'organization_group': 'OrganizationGroup',
        'device_type_id': 'DeviceTypeId',
        'device_type': 'DeviceType',
        'parent_proxy_device_id': 'ParentProxyDeviceId',
        'parent_proxy_uu_id': 'ParentProxyUuId',
        'product_id': 'ProductId',
        'product': 'Product',
        'product_compliance_status_id': 'ProductComplianceStatusId',
        'product_compliance_status': 'ProductComplianceStatus'
    }

    def __init__(self, device_id=None, friendly_name=None, organization_group=None, device_type_id=None, device_type=None, parent_proxy_device_id=None, parent_proxy_uu_id=None, product_id=None, product=None, product_compliance_status_id=None, product_compliance_status=None, _configuration=None):  # noqa: E501
        """ProductComplianceIssueDetailsV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_id = None
        self._friendly_name = None
        self._organization_group = None
        self._device_type_id = None
        self._device_type = None
        self._parent_proxy_device_id = None
        self._parent_proxy_uu_id = None
        self._product_id = None
        self._product = None
        self._product_compliance_status_id = None
        self._product_compliance_status = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if organization_group is not None:
            self.organization_group = organization_group
        if device_type_id is not None:
            self.device_type_id = device_type_id
        if device_type is not None:
            self.device_type = device_type
        if parent_proxy_device_id is not None:
            self.parent_proxy_device_id = parent_proxy_device_id
        if parent_proxy_uu_id is not None:
            self.parent_proxy_uu_id = parent_proxy_uu_id
        if product_id is not None:
            self.product_id = product_id
        if product is not None:
            self.product = product
        if product_compliance_status_id is not None:
            self.product_compliance_status_id = product_compliance_status_id
        if product_compliance_status is not None:
            self.product_compliance_status = product_compliance_status

    @property
    def device_id(self):
        """Gets the device_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501

        Gets or sets Device Id.  # noqa: E501

        :return: The device_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ProductComplianceIssueDetailsV1Model.

        Gets or sets Device Id.  # noqa: E501

        :param device_id: The device_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def friendly_name(self):
        """Gets the friendly_name of this ProductComplianceIssueDetailsV1Model.  # noqa: E501

        Gets or sets device friendly name.  # noqa: E501

        :return: The friendly_name of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this ProductComplianceIssueDetailsV1Model.

        Gets or sets device friendly name.  # noqa: E501

        :param friendly_name: The friendly_name of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def organization_group(self):
        """Gets the organization_group of this ProductComplianceIssueDetailsV1Model.  # noqa: E501

        Gets or sets Organization Group name.  # noqa: E501

        :return: The organization_group of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group

    @organization_group.setter
    def organization_group(self, organization_group):
        """Sets the organization_group of this ProductComplianceIssueDetailsV1Model.

        Gets or sets Organization Group name.  # noqa: E501

        :param organization_group: The organization_group of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group = organization_group

    @property
    def device_type_id(self):
        """Gets the device_type_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501

        Gets or sets device type id.  # noqa: E501

        :return: The device_type_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :rtype: int
        """
        return self._device_type_id

    @device_type_id.setter
    def device_type_id(self, device_type_id):
        """Sets the device_type_id of this ProductComplianceIssueDetailsV1Model.

        Gets or sets device type id.  # noqa: E501

        :param device_type_id: The device_type_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :type: int
        """

        self._device_type_id = device_type_id

    @property
    def device_type(self):
        """Gets the device_type of this ProductComplianceIssueDetailsV1Model.  # noqa: E501

        Gets or sets device type name.  # noqa: E501

        :return: The device_type of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ProductComplianceIssueDetailsV1Model.

        Gets or sets device type name.  # noqa: E501

        :param device_type: The device_type of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def parent_proxy_device_id(self):
        """Gets the parent_proxy_device_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501

        Gets or sets parent proxy device id.  # noqa: E501

        :return: The parent_proxy_device_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :rtype: int
        """
        return self._parent_proxy_device_id

    @parent_proxy_device_id.setter
    def parent_proxy_device_id(self, parent_proxy_device_id):
        """Sets the parent_proxy_device_id of this ProductComplianceIssueDetailsV1Model.

        Gets or sets parent proxy device id.  # noqa: E501

        :param parent_proxy_device_id: The parent_proxy_device_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :type: int
        """

        self._parent_proxy_device_id = parent_proxy_device_id

    @property
    def parent_proxy_uu_id(self):
        """Gets the parent_proxy_uu_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501

        Gets or sets parent proxy devuce uuid.  # noqa: E501

        :return: The parent_proxy_uu_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._parent_proxy_uu_id

    @parent_proxy_uu_id.setter
    def parent_proxy_uu_id(self, parent_proxy_uu_id):
        """Sets the parent_proxy_uu_id of this ProductComplianceIssueDetailsV1Model.

        Gets or sets parent proxy devuce uuid.  # noqa: E501

        :param parent_proxy_uu_id: The parent_proxy_uu_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :type: str
        """

        self._parent_proxy_uu_id = parent_proxy_uu_id

    @property
    def product_id(self):
        """Gets the product_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501

        Gets or sets Product Id.  # noqa: E501

        :return: The product_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductComplianceIssueDetailsV1Model.

        Gets or sets Product Id.  # noqa: E501

        :param product_id: The product_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def product(self):
        """Gets the product of this ProductComplianceIssueDetailsV1Model.  # noqa: E501

        Gets or sets Product Name.  # noqa: E501

        :return: The product of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ProductComplianceIssueDetailsV1Model.

        Gets or sets Product Name.  # noqa: E501

        :param product: The product of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def product_compliance_status_id(self):
        """Gets the product_compliance_status_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501

        Gets or sets product compliance status id.  # noqa: E501

        :return: The product_compliance_status_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :rtype: int
        """
        return self._product_compliance_status_id

    @product_compliance_status_id.setter
    def product_compliance_status_id(self, product_compliance_status_id):
        """Sets the product_compliance_status_id of this ProductComplianceIssueDetailsV1Model.

        Gets or sets product compliance status id.  # noqa: E501

        :param product_compliance_status_id: The product_compliance_status_id of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :type: int
        """

        self._product_compliance_status_id = product_compliance_status_id

    @property
    def product_compliance_status(self):
        """Gets the product_compliance_status of this ProductComplianceIssueDetailsV1Model.  # noqa: E501

        Gets or sets Product compliance status Name.  # noqa: E501

        :return: The product_compliance_status of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :rtype: str
        """
        return self._product_compliance_status

    @product_compliance_status.setter
    def product_compliance_status(self, product_compliance_status):
        """Sets the product_compliance_status of this ProductComplianceIssueDetailsV1Model.

        Gets or sets Product compliance status Name.  # noqa: E501

        :param product_compliance_status: The product_compliance_status of this ProductComplianceIssueDetailsV1Model.  # noqa: E501
        :type: str
        """

        self._product_compliance_status = product_compliance_status

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
        if issubclass(ProductComplianceIssueDetailsV1Model, dict):
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
        if not isinstance(other, ProductComplianceIssueDetailsV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductComplianceIssueDetailsV1Model):
            return True

        return self.to_dict() != other.to_dict()
