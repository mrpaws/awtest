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


class RepositoryFileModel(object):
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
        'file_name': 'str',
        'file_path': 'str',
        'file_size': 'int',
        'file_version': 'str',
        'content_repository_id': 'int',
        'relay_server_only': 'bool',
        'download_date': 'str',
        'live_date': 'str',
        'url': 'str'
    }

    attribute_map = {
        'file_name': 'FileName',
        'file_path': 'FilePath',
        'file_size': 'FileSize',
        'file_version': 'FileVersion',
        'content_repository_id': 'ContentRepositoryID',
        'relay_server_only': 'RelayServerOnly',
        'download_date': 'DownloadDate',
        'live_date': 'LiveDate',
        'url': 'URL'
    }

    def __init__(self, file_name=None, file_path=None, file_size=None, file_version=None, content_repository_id=None, relay_server_only=None, download_date=None, live_date=None, url=None, _configuration=None):  # noqa: E501
        """RepositoryFileModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_name = None
        self._file_path = None
        self._file_size = None
        self._file_version = None
        self._content_repository_id = None
        self._relay_server_only = None
        self._download_date = None
        self._live_date = None
        self._url = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if file_size is not None:
            self.file_size = file_size
        if file_version is not None:
            self.file_version = file_version
        if content_repository_id is not None:
            self.content_repository_id = content_repository_id
        if relay_server_only is not None:
            self.relay_server_only = relay_server_only
        if download_date is not None:
            self.download_date = download_date
        if live_date is not None:
            self.live_date = live_date
        if url is not None:
            self.url = url

    @property
    def file_name(self):
        """Gets the file_name of this RepositoryFileModel.  # noqa: E501

        Gets or sets name of the referenced file in the remote repository.  # noqa: E501

        :return: The file_name of this RepositoryFileModel.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this RepositoryFileModel.

        Gets or sets name of the referenced file in the remote repository.  # noqa: E501

        :param file_name: The file_name of this RepositoryFileModel.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def file_path(self):
        """Gets the file_path of this RepositoryFileModel.  # noqa: E501

        Gets or sets destination path on the device where the file will download.  # noqa: E501

        :return: The file_path of this RepositoryFileModel.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this RepositoryFileModel.

        Gets or sets destination path on the device where the file will download.  # noqa: E501

        :param file_path: The file_path of this RepositoryFileModel.  # noqa: E501
        :type: str
        """

        self._file_path = file_path

    @property
    def file_size(self):
        """Gets the file_size of this RepositoryFileModel.  # noqa: E501

        Gets or sets expected size of the Repository file.  # noqa: E501

        :return: The file_size of this RepositoryFileModel.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this RepositoryFileModel.

        Gets or sets expected size of the Repository file.  # noqa: E501

        :param file_size: The file_size of this RepositoryFileModel.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def file_version(self):
        """Gets the file_version of this RepositoryFileModel.  # noqa: E501

        Gets or sets version of the Repository file.  # noqa: E501

        :return: The file_version of this RepositoryFileModel.  # noqa: E501
        :rtype: str
        """
        return self._file_version

    @file_version.setter
    def file_version(self, file_version):
        """Sets the file_version of this RepositoryFileModel.

        Gets or sets version of the Repository file.  # noqa: E501

        :param file_version: The file_version of this RepositoryFileModel.  # noqa: E501
        :type: str
        """

        self._file_version = file_version

    @property
    def content_repository_id(self):
        """Gets the content_repository_id of this RepositoryFileModel.  # noqa: E501

        Gets or sets iD of the content repository that will contain the referenced file.  # noqa: E501

        :return: The content_repository_id of this RepositoryFileModel.  # noqa: E501
        :rtype: int
        """
        return self._content_repository_id

    @content_repository_id.setter
    def content_repository_id(self, content_repository_id):
        """Sets the content_repository_id of this RepositoryFileModel.

        Gets or sets iD of the content repository that will contain the referenced file.  # noqa: E501

        :param content_repository_id: The content_repository_id of this RepositoryFileModel.  # noqa: E501
        :type: int
        """

        self._content_repository_id = content_repository_id

    @property
    def relay_server_only(self):
        """Gets the relay_server_only of this RepositoryFileModel.  # noqa: E501

        Gets or sets a value indicating whether relayServerOnly.  # noqa: E501

        :return: The relay_server_only of this RepositoryFileModel.  # noqa: E501
        :rtype: bool
        """
        return self._relay_server_only

    @relay_server_only.setter
    def relay_server_only(self, relay_server_only):
        """Sets the relay_server_only of this RepositoryFileModel.

        Gets or sets a value indicating whether relayServerOnly.  # noqa: E501

        :param relay_server_only: The relay_server_only of this RepositoryFileModel.  # noqa: E501
        :type: bool
        """

        self._relay_server_only = relay_server_only

    @property
    def download_date(self):
        """Gets the download_date of this RepositoryFileModel.  # noqa: E501

        Gets or sets date that the file will be available to download to the device.  # noqa: E501

        :return: The download_date of this RepositoryFileModel.  # noqa: E501
        :rtype: str
        """
        return self._download_date

    @download_date.setter
    def download_date(self, download_date):
        """Sets the download_date of this RepositoryFileModel.

        Gets or sets date that the file will be available to download to the device.  # noqa: E501

        :param download_date: The download_date of this RepositoryFileModel.  # noqa: E501
        :type: str
        """

        self._download_date = download_date

    @property
    def live_date(self):
        """Gets the live_date of this RepositoryFileModel.  # noqa: E501

        Gets or sets date that the file version will be actively used on the device.  # noqa: E501

        :return: The live_date of this RepositoryFileModel.  # noqa: E501
        :rtype: str
        """
        return self._live_date

    @live_date.setter
    def live_date(self, live_date):
        """Sets the live_date of this RepositoryFileModel.

        Gets or sets date that the file version will be actively used on the device.  # noqa: E501

        :param live_date: The live_date of this RepositoryFileModel.  # noqa: E501
        :type: str
        """

        self._live_date = live_date

    @property
    def url(self):
        """Gets the url of this RepositoryFileModel.  # noqa: E501

        Gets or sets uRL link address of the referenced repository file.  # noqa: E501

        :return: The url of this RepositoryFileModel.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RepositoryFileModel.

        Gets or sets uRL link address of the referenced repository file.  # noqa: E501

        :param url: The url of this RepositoryFileModel.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(RepositoryFileModel, dict):
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
        if not isinstance(other, RepositoryFileModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryFileModel):
            return True

        return self.to_dict() != other.to_dict()