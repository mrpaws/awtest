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


class AppFilesOptionsModel_(object):
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
        'app_dependencies_list': 'list[AppDependencyModel]',
        'app_transforms_list': 'list[AppTransformModel]',
        'app_patches_list': 'list[AppPatchModel]',
        'application_un_install_process': 'AppUnInstallProcessModel_'
    }

    attribute_map = {
        'app_dependencies_list': 'AppDependenciesList',
        'app_transforms_list': 'AppTransformsList',
        'app_patches_list': 'AppPatchesList',
        'application_un_install_process': 'ApplicationUnInstallProcess'
    }

    def __init__(self, app_dependencies_list=None, app_transforms_list=None, app_patches_list=None, application_un_install_process=None, _configuration=None):  # noqa: E501
        """AppFilesOptionsModel_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._app_dependencies_list = None
        self._app_transforms_list = None
        self._app_patches_list = None
        self._application_un_install_process = None
        self.discriminator = None

        if app_dependencies_list is not None:
            self.app_dependencies_list = app_dependencies_list
        if app_transforms_list is not None:
            self.app_transforms_list = app_transforms_list
        if app_patches_list is not None:
            self.app_patches_list = app_patches_list
        if application_un_install_process is not None:
            self.application_un_install_process = application_un_install_process

    @property
    def app_dependencies_list(self):
        """Gets the app_dependencies_list of this AppFilesOptionsModel_.  # noqa: E501

        Gets or sets list of application dependency Ids.  # noqa: E501

        :return: The app_dependencies_list of this AppFilesOptionsModel_.  # noqa: E501
        :rtype: list[AppDependencyModel]
        """
        return self._app_dependencies_list

    @app_dependencies_list.setter
    def app_dependencies_list(self, app_dependencies_list):
        """Sets the app_dependencies_list of this AppFilesOptionsModel_.

        Gets or sets list of application dependency Ids.  # noqa: E501

        :param app_dependencies_list: The app_dependencies_list of this AppFilesOptionsModel_.  # noqa: E501
        :type: list[AppDependencyModel]
        """

        self._app_dependencies_list = app_dependencies_list

    @property
    def app_transforms_list(self):
        """Gets the app_transforms_list of this AppFilesOptionsModel_.  # noqa: E501

        Gets or sets list of uploaded transform files.  # noqa: E501

        :return: The app_transforms_list of this AppFilesOptionsModel_.  # noqa: E501
        :rtype: list[AppTransformModel]
        """
        return self._app_transforms_list

    @app_transforms_list.setter
    def app_transforms_list(self, app_transforms_list):
        """Sets the app_transforms_list of this AppFilesOptionsModel_.

        Gets or sets list of uploaded transform files.  # noqa: E501

        :param app_transforms_list: The app_transforms_list of this AppFilesOptionsModel_.  # noqa: E501
        :type: list[AppTransformModel]
        """

        self._app_transforms_list = app_transforms_list

    @property
    def app_patches_list(self):
        """Gets the app_patches_list of this AppFilesOptionsModel_.  # noqa: E501

        Gets or sets list of uploaded patch files.  # noqa: E501

        :return: The app_patches_list of this AppFilesOptionsModel_.  # noqa: E501
        :rtype: list[AppPatchModel]
        """
        return self._app_patches_list

    @app_patches_list.setter
    def app_patches_list(self, app_patches_list):
        """Sets the app_patches_list of this AppFilesOptionsModel_.

        Gets or sets list of uploaded patch files.  # noqa: E501

        :param app_patches_list: The app_patches_list of this AppFilesOptionsModel_.  # noqa: E501
        :type: list[AppPatchModel]
        """

        self._app_patches_list = app_patches_list

    @property
    def application_un_install_process(self):
        """Gets the application_un_install_process of this AppFilesOptionsModel_.  # noqa: E501

        Gets or sets application uninstallation process.  # noqa: E501

        :return: The application_un_install_process of this AppFilesOptionsModel_.  # noqa: E501
        :rtype: AppUnInstallProcessModel_
        """
        return self._application_un_install_process

    @application_un_install_process.setter
    def application_un_install_process(self, application_un_install_process):
        """Sets the application_un_install_process of this AppFilesOptionsModel_.

        Gets or sets application uninstallation process.  # noqa: E501

        :param application_un_install_process: The application_un_install_process of this AppFilesOptionsModel_.  # noqa: E501
        :type: AppUnInstallProcessModel_
        """

        self._application_un_install_process = application_un_install_process

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
        if issubclass(AppFilesOptionsModel_, dict):
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
        if not isinstance(other, AppFilesOptionsModel_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppFilesOptionsModel_):
            return True

        return self.to_dict() != other.to_dict()
