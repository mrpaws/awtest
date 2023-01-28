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


class ProductDetailV1Model(object):
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
        'product_type': 'str',
        'name': 'str',
        'organization_group_name': 'str',
        'version': 'str',
        'device_type': 'str',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'product_type': 'productType',
        'name': 'name',
        'organization_group_name': 'organizationGroupName',
        'version': 'version',
        'device_type': 'deviceType',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, product_type=None, name=None, organization_group_name=None, version=None, device_type=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """ProductDetailV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_type = None
        self._name = None
        self._organization_group_name = None
        self._version = None
        self._device_type = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if product_type is not None:
            self.product_type = product_type
        if name is not None:
            self.name = name
        if organization_group_name is not None:
            self.organization_group_name = organization_group_name
        if version is not None:
            self.version = version
        if device_type is not None:
            self.device_type = device_type
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def product_type(self):
        """Gets the product_type of this ProductDetailV1Model.  # noqa: E501

        Type of the product i.e., InternalApp, PublicApp, PurchasedApp or Profile  # noqa: E501

        :return: The product_type of this ProductDetailV1Model.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this ProductDetailV1Model.

        Type of the product i.e., InternalApp, PublicApp, PurchasedApp or Profile  # noqa: E501

        :param product_type: The product_type of this ProductDetailV1Model.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

    @property
    def name(self):
        """Gets the name of this ProductDetailV1Model.  # noqa: E501

        Name of the product  # noqa: E501

        :return: The name of this ProductDetailV1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductDetailV1Model.

        Name of the product  # noqa: E501

        :param name: The name of this ProductDetailV1Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization_group_name(self):
        """Gets the organization_group_name of this ProductDetailV1Model.  # noqa: E501

        Organization group name of the product  # noqa: E501

        :return: The organization_group_name of this ProductDetailV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_name

    @organization_group_name.setter
    def organization_group_name(self, organization_group_name):
        """Sets the organization_group_name of this ProductDetailV1Model.

        Organization group name of the product  # noqa: E501

        :param organization_group_name: The organization_group_name of this ProductDetailV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group_name = organization_group_name

    @property
    def version(self):
        """Gets the version of this ProductDetailV1Model.  # noqa: E501

        Version of the product  # noqa: E501

        :return: The version of this ProductDetailV1Model.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProductDetailV1Model.

        Version of the product  # noqa: E501

        :param version: The version of this ProductDetailV1Model.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def device_type(self):
        """Gets the device_type of this ProductDetailV1Model.  # noqa: E501

        Device Type of the app or profile like Android Apple iOS etc.  # noqa: E501

        :return: The device_type of this ProductDetailV1Model.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ProductDetailV1Model.

        Device Type of the app or profile like Android Apple iOS etc.  # noqa: E501

        :param device_type: The device_type of this ProductDetailV1Model.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def id(self):
        """Gets the id of this ProductDetailV1Model.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this ProductDetailV1Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductDetailV1Model.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this ProductDetailV1Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this ProductDetailV1Model.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this ProductDetailV1Model.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ProductDetailV1Model.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this ProductDetailV1Model.  # noqa: E501
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
        if issubclass(ProductDetailV1Model, dict):
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
        if not isinstance(other, ProductDetailV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductDetailV1Model):
            return True

        return self.to_dict() != other.to_dict()