# coding: utf-8

"""
    MAM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mamv2.configuration import Configuration


class AppTransformModel(object):
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
        'transform_id': 'int',
        'transform_file_name': 'str',
        'transform_blob_id': 'int',
        'transform_uuid': 'str'
    }

    attribute_map = {
        'transform_id': 'TransformId',
        'transform_file_name': 'TransformFileName',
        'transform_blob_id': 'TransformBlobId',
        'transform_uuid': 'TransformUuid'
    }

    def __init__(self, transform_id=None, transform_file_name=None, transform_blob_id=None, transform_uuid=None, _configuration=None):  # noqa: E501
        """AppTransformModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transform_id = None
        self._transform_file_name = None
        self._transform_blob_id = None
        self._transform_uuid = None
        self.discriminator = None

        if transform_id is not None:
            self.transform_id = transform_id
        if transform_file_name is not None:
            self.transform_file_name = transform_file_name
        if transform_blob_id is not None:
            self.transform_blob_id = transform_blob_id
        if transform_uuid is not None:
            self.transform_uuid = transform_uuid

    @property
    def transform_id(self):
        """Gets the transform_id of this AppTransformModel.  # noqa: E501

        Gets or sets the application transform id.  # noqa: E501

        :return: The transform_id of this AppTransformModel.  # noqa: E501
        :rtype: int
        """
        return self._transform_id

    @transform_id.setter
    def transform_id(self, transform_id):
        """Sets the transform_id of this AppTransformModel.

        Gets or sets the application transform id.  # noqa: E501

        :param transform_id: The transform_id of this AppTransformModel.  # noqa: E501
        :type: int
        """

        self._transform_id = transform_id

    @property
    def transform_file_name(self):
        """Gets the transform_file_name of this AppTransformModel.  # noqa: E501

        Gets or sets the uploaded transform file name.  # noqa: E501

        :return: The transform_file_name of this AppTransformModel.  # noqa: E501
        :rtype: str
        """
        return self._transform_file_name

    @transform_file_name.setter
    def transform_file_name(self, transform_file_name):
        """Sets the transform_file_name of this AppTransformModel.

        Gets or sets the uploaded transform file name.  # noqa: E501

        :param transform_file_name: The transform_file_name of this AppTransformModel.  # noqa: E501
        :type: str
        """

        self._transform_file_name = transform_file_name

    @property
    def transform_blob_id(self):
        """Gets the transform_blob_id of this AppTransformModel.  # noqa: E501

        Gets or sets the blob id for the uploaded transform file.  # noqa: E501

        :return: The transform_blob_id of this AppTransformModel.  # noqa: E501
        :rtype: int
        """
        return self._transform_blob_id

    @transform_blob_id.setter
    def transform_blob_id(self, transform_blob_id):
        """Sets the transform_blob_id of this AppTransformModel.

        Gets or sets the blob id for the uploaded transform file.  # noqa: E501

        :param transform_blob_id: The transform_blob_id of this AppTransformModel.  # noqa: E501
        :type: int
        """

        self._transform_blob_id = transform_blob_id

    @property
    def transform_uuid(self):
        """Gets the transform_uuid of this AppTransformModel.  # noqa: E501

        Gets or sets Application Transform Uuid.  # noqa: E501

        :return: The transform_uuid of this AppTransformModel.  # noqa: E501
        :rtype: str
        """
        return self._transform_uuid

    @transform_uuid.setter
    def transform_uuid(self, transform_uuid):
        """Sets the transform_uuid of this AppTransformModel.

        Gets or sets Application Transform Uuid.  # noqa: E501

        :param transform_uuid: The transform_uuid of this AppTransformModel.  # noqa: E501
        :type: str
        """

        self._transform_uuid = transform_uuid

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
        if issubclass(AppTransformModel, dict):
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
        if not isinstance(other, AppTransformModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppTransformModel):
            return True

        return self.to_dict() != other.to_dict()
