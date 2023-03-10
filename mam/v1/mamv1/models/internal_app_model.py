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


class InternalAppModel(object):
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
        'application_name': 'str',
        'app_id': 'str',
        'actual_file_version': 'str',
        'build_version': 'str',
        'airwatch_app_version': 'str',
        'status': 'str',
        'managed_by': 'str',
        'managed_by_uuid': 'str',
        'app_provisioning_profile_uuid': 'str',
        'assume_management_of_user_installed_app': 'str',
        'platform': 'str',
        'supported_models': 'list[ApplicationSupportedModelsModel]',
        'minimum_operating_system': 'str',
        'app_size_in_kb': 'int',
        'category_list': 'list[ApplicationCategoriesModel]',
        'comments': 'str',
        'application_url': 'str',
        'sdk': 'str',
        'sdk_profile_id': 'int',
        'sdk_profile_uuid': 'str',
        'devices_assigned_count': 'int',
        'devices_installed_count': 'int',
        'devices_not_installed_count': 'int',
        'rating': 'int',
        'change_log': 'str',
        'renewal_date': 'datetime',
        'assignments': 'list[ApplicationAssignmentModel]',
        'excluded_smart_group_ids': 'list[int]',
        'excluded_smart_group_guids': 'list[str]',
        'msi_deployment_parameters': 'MsiDeploymentParameterModel_',
        'deployment_options': 'AppDeploymentOptionsModel_',
        'files_options': 'AppFilesOptionsModel_',
        'mac_os_software_deployment_summary': 'MacOsSoftwareDeploymentSummaryModel_',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'application_name': 'ApplicationName',
        'app_id': 'AppId',
        'actual_file_version': 'ActualFileVersion',
        'build_version': 'BuildVersion',
        'airwatch_app_version': 'AirwatchAppVersion',
        'status': 'Status',
        'managed_by': 'ManagedBy',
        'managed_by_uuid': 'ManagedByUuid',
        'app_provisioning_profile_uuid': 'AppProvisioningProfileUuid',
        'assume_management_of_user_installed_app': 'AssumeManagementOfUserInstalledApp',
        'platform': 'Platform',
        'supported_models': 'SupportedModels',
        'minimum_operating_system': 'MinimumOperatingSystem',
        'app_size_in_kb': 'AppSizeInKB',
        'category_list': 'CategoryList',
        'comments': 'Comments',
        'application_url': 'ApplicationUrl',
        'sdk': 'Sdk',
        'sdk_profile_id': 'SdkProfileId',
        'sdk_profile_uuid': 'SdkProfileUuid',
        'devices_assigned_count': 'DevicesAssignedCount',
        'devices_installed_count': 'DevicesInstalledCount',
        'devices_not_installed_count': 'DevicesNotInstalledCount',
        'rating': 'Rating',
        'change_log': 'ChangeLog',
        'renewal_date': 'RenewalDate',
        'assignments': 'Assignments',
        'excluded_smart_group_ids': 'ExcludedSmartGroupIds',
        'excluded_smart_group_guids': 'ExcludedSmartGroupGuids',
        'msi_deployment_parameters': 'MsiDeploymentParameters',
        'deployment_options': 'DeploymentOptions',
        'files_options': 'FilesOptions',
        'mac_os_software_deployment_summary': 'MacOsSoftwareDeploymentSummary',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, application_name=None, app_id=None, actual_file_version=None, build_version=None, airwatch_app_version=None, status=None, managed_by=None, managed_by_uuid=None, app_provisioning_profile_uuid=None, assume_management_of_user_installed_app=None, platform=None, supported_models=None, minimum_operating_system=None, app_size_in_kb=None, category_list=None, comments=None, application_url=None, sdk=None, sdk_profile_id=None, sdk_profile_uuid=None, devices_assigned_count=None, devices_installed_count=None, devices_not_installed_count=None, rating=None, change_log=None, renewal_date=None, assignments=None, excluded_smart_group_ids=None, excluded_smart_group_guids=None, msi_deployment_parameters=None, deployment_options=None, files_options=None, mac_os_software_deployment_summary=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """InternalAppModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_name = None
        self._app_id = None
        self._actual_file_version = None
        self._build_version = None
        self._airwatch_app_version = None
        self._status = None
        self._managed_by = None
        self._managed_by_uuid = None
        self._app_provisioning_profile_uuid = None
        self._assume_management_of_user_installed_app = None
        self._platform = None
        self._supported_models = None
        self._minimum_operating_system = None
        self._app_size_in_kb = None
        self._category_list = None
        self._comments = None
        self._application_url = None
        self._sdk = None
        self._sdk_profile_id = None
        self._sdk_profile_uuid = None
        self._devices_assigned_count = None
        self._devices_installed_count = None
        self._devices_not_installed_count = None
        self._rating = None
        self._change_log = None
        self._renewal_date = None
        self._assignments = None
        self._excluded_smart_group_ids = None
        self._excluded_smart_group_guids = None
        self._msi_deployment_parameters = None
        self._deployment_options = None
        self._files_options = None
        self._mac_os_software_deployment_summary = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if application_name is not None:
            self.application_name = application_name
        if app_id is not None:
            self.app_id = app_id
        if actual_file_version is not None:
            self.actual_file_version = actual_file_version
        if build_version is not None:
            self.build_version = build_version
        if airwatch_app_version is not None:
            self.airwatch_app_version = airwatch_app_version
        if status is not None:
            self.status = status
        if managed_by is not None:
            self.managed_by = managed_by
        if managed_by_uuid is not None:
            self.managed_by_uuid = managed_by_uuid
        if app_provisioning_profile_uuid is not None:
            self.app_provisioning_profile_uuid = app_provisioning_profile_uuid
        if assume_management_of_user_installed_app is not None:
            self.assume_management_of_user_installed_app = assume_management_of_user_installed_app
        if platform is not None:
            self.platform = platform
        if supported_models is not None:
            self.supported_models = supported_models
        if minimum_operating_system is not None:
            self.minimum_operating_system = minimum_operating_system
        if app_size_in_kb is not None:
            self.app_size_in_kb = app_size_in_kb
        if category_list is not None:
            self.category_list = category_list
        if comments is not None:
            self.comments = comments
        if application_url is not None:
            self.application_url = application_url
        if sdk is not None:
            self.sdk = sdk
        if sdk_profile_id is not None:
            self.sdk_profile_id = sdk_profile_id
        if sdk_profile_uuid is not None:
            self.sdk_profile_uuid = sdk_profile_uuid
        if devices_assigned_count is not None:
            self.devices_assigned_count = devices_assigned_count
        if devices_installed_count is not None:
            self.devices_installed_count = devices_installed_count
        if devices_not_installed_count is not None:
            self.devices_not_installed_count = devices_not_installed_count
        if rating is not None:
            self.rating = rating
        if change_log is not None:
            self.change_log = change_log
        if renewal_date is not None:
            self.renewal_date = renewal_date
        if assignments is not None:
            self.assignments = assignments
        if excluded_smart_group_ids is not None:
            self.excluded_smart_group_ids = excluded_smart_group_ids
        if excluded_smart_group_guids is not None:
            self.excluded_smart_group_guids = excluded_smart_group_guids
        if msi_deployment_parameters is not None:
            self.msi_deployment_parameters = msi_deployment_parameters
        if deployment_options is not None:
            self.deployment_options = deployment_options
        if files_options is not None:
            self.files_options = files_options
        if mac_os_software_deployment_summary is not None:
            self.mac_os_software_deployment_summary = mac_os_software_deployment_summary
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def application_name(self):
        """Gets the application_name of this InternalAppModel.  # noqa: E501

        Gets or sets the name of the application.  # noqa: E501

        :return: The application_name of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this InternalAppModel.

        Gets or sets the name of the application.  # noqa: E501

        :param application_name: The application_name of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def app_id(self):
        """Gets the app_id of this InternalAppModel.  # noqa: E501

        Gets or sets the bundle id of the app.  # noqa: E501

        :return: The app_id of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this InternalAppModel.

        Gets or sets the bundle id of the app.  # noqa: E501

        :param app_id: The app_id of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def actual_file_version(self):
        """Gets the actual_file_version of this InternalAppModel.  # noqa: E501

        Gets or sets the actual file version of the app.  # noqa: E501

        :return: The actual_file_version of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._actual_file_version

    @actual_file_version.setter
    def actual_file_version(self, actual_file_version):
        """Sets the actual_file_version of this InternalAppModel.

        Gets or sets the actual file version of the app.  # noqa: E501

        :param actual_file_version: The actual_file_version of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._actual_file_version = actual_file_version

    @property
    def build_version(self):
        """Gets the build_version of this InternalAppModel.  # noqa: E501

        Gets or sets the build version of the app.  # noqa: E501

        :return: The build_version of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this InternalAppModel.

        Gets or sets the build version of the app.  # noqa: E501

        :param build_version: The build_version of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._build_version = build_version

    @property
    def airwatch_app_version(self):
        """Gets the airwatch_app_version of this InternalAppModel.  # noqa: E501

        Gets or sets airWatch internal application version.  # noqa: E501

        :return: The airwatch_app_version of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._airwatch_app_version

    @airwatch_app_version.setter
    def airwatch_app_version(self, airwatch_app_version):
        """Sets the airwatch_app_version of this InternalAppModel.

        Gets or sets airWatch internal application version.  # noqa: E501

        :param airwatch_app_version: The airwatch_app_version of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._airwatch_app_version = airwatch_app_version

    @property
    def status(self):
        """Gets the status of this InternalAppModel.  # noqa: E501

        Gets or sets status of the App.  # noqa: E501

        :return: The status of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InternalAppModel.

        Gets or sets status of the App.  # noqa: E501

        :param status: The status of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def managed_by(self):
        """Gets the managed_by of this InternalAppModel.  # noqa: E501

        Gets or sets the managed by Organization Group of the app.  # noqa: E501

        :return: The managed_by of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._managed_by

    @managed_by.setter
    def managed_by(self, managed_by):
        """Sets the managed_by of this InternalAppModel.

        Gets or sets the managed by Organization Group of the app.  # noqa: E501

        :param managed_by: The managed_by of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._managed_by = managed_by

    @property
    def managed_by_uuid(self):
        """Gets the managed_by_uuid of this InternalAppModel.  # noqa: E501

        Gets or sets managed By Organization Group Uuid.  # noqa: E501

        :return: The managed_by_uuid of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._managed_by_uuid

    @managed_by_uuid.setter
    def managed_by_uuid(self, managed_by_uuid):
        """Sets the managed_by_uuid of this InternalAppModel.

        Gets or sets managed By Organization Group Uuid.  # noqa: E501

        :param managed_by_uuid: The managed_by_uuid of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._managed_by_uuid = managed_by_uuid

    @property
    def app_provisioning_profile_uuid(self):
        """Gets the app_provisioning_profile_uuid of this InternalAppModel.  # noqa: E501

        Gets or sets app Provisioning UUID.  # noqa: E501

        :return: The app_provisioning_profile_uuid of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._app_provisioning_profile_uuid

    @app_provisioning_profile_uuid.setter
    def app_provisioning_profile_uuid(self, app_provisioning_profile_uuid):
        """Sets the app_provisioning_profile_uuid of this InternalAppModel.

        Gets or sets app Provisioning UUID.  # noqa: E501

        :param app_provisioning_profile_uuid: The app_provisioning_profile_uuid of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._app_provisioning_profile_uuid = app_provisioning_profile_uuid

    @property
    def assume_management_of_user_installed_app(self):
        """Gets the assume_management_of_user_installed_app of this InternalAppModel.  # noqa: E501

        Gets or sets a value indicating whether the management of user installed apps should be assumed.  # noqa: E501

        :return: The assume_management_of_user_installed_app of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._assume_management_of_user_installed_app

    @assume_management_of_user_installed_app.setter
    def assume_management_of_user_installed_app(self, assume_management_of_user_installed_app):
        """Sets the assume_management_of_user_installed_app of this InternalAppModel.

        Gets or sets a value indicating whether the management of user installed apps should be assumed.  # noqa: E501

        :param assume_management_of_user_installed_app: The assume_management_of_user_installed_app of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._assume_management_of_user_installed_app = assume_management_of_user_installed_app

    @property
    def platform(self):
        """Gets the platform of this InternalAppModel.  # noqa: E501

        Gets or sets the platform.  # noqa: E501

        :return: The platform of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this InternalAppModel.

        Gets or sets the platform.  # noqa: E501

        :param platform: The platform of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def supported_models(self):
        """Gets the supported_models of this InternalAppModel.  # noqa: E501

        Gets or sets The supported models of the app.  # noqa: E501

        :return: The supported_models of this InternalAppModel.  # noqa: E501
        :rtype: list[ApplicationSupportedModelsModel]
        """
        return self._supported_models

    @supported_models.setter
    def supported_models(self, supported_models):
        """Sets the supported_models of this InternalAppModel.

        Gets or sets The supported models of the app.  # noqa: E501

        :param supported_models: The supported_models of this InternalAppModel.  # noqa: E501
        :type: list[ApplicationSupportedModelsModel]
        """

        self._supported_models = supported_models

    @property
    def minimum_operating_system(self):
        """Gets the minimum_operating_system of this InternalAppModel.  # noqa: E501

        Gets or sets minimum Operating System Version of the application.  # noqa: E501

        :return: The minimum_operating_system of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._minimum_operating_system

    @minimum_operating_system.setter
    def minimum_operating_system(self, minimum_operating_system):
        """Sets the minimum_operating_system of this InternalAppModel.

        Gets or sets minimum Operating System Version of the application.  # noqa: E501

        :param minimum_operating_system: The minimum_operating_system of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._minimum_operating_system = minimum_operating_system

    @property
    def app_size_in_kb(self):
        """Gets the app_size_in_kb of this InternalAppModel.  # noqa: E501

        Gets or sets the size of the application in kilo bytes.  # noqa: E501

        :return: The app_size_in_kb of this InternalAppModel.  # noqa: E501
        :rtype: int
        """
        return self._app_size_in_kb

    @app_size_in_kb.setter
    def app_size_in_kb(self, app_size_in_kb):
        """Sets the app_size_in_kb of this InternalAppModel.

        Gets or sets the size of the application in kilo bytes.  # noqa: E501

        :param app_size_in_kb: The app_size_in_kb of this InternalAppModel.  # noqa: E501
        :type: int
        """

        self._app_size_in_kb = app_size_in_kb

    @property
    def category_list(self):
        """Gets the category_list of this InternalAppModel.  # noqa: E501

        Gets or sets the application category list.  # noqa: E501

        :return: The category_list of this InternalAppModel.  # noqa: E501
        :rtype: list[ApplicationCategoriesModel]
        """
        return self._category_list

    @category_list.setter
    def category_list(self, category_list):
        """Sets the category_list of this InternalAppModel.

        Gets or sets the application category list.  # noqa: E501

        :param category_list: The category_list of this InternalAppModel.  # noqa: E501
        :type: list[ApplicationCategoriesModel]
        """

        self._category_list = category_list

    @property
    def comments(self):
        """Gets the comments of this InternalAppModel.  # noqa: E501

        Gets or sets the comments for the application.  # noqa: E501

        :return: The comments of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this InternalAppModel.

        Gets or sets the comments for the application.  # noqa: E501

        :param comments: The comments of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def application_url(self):
        """Gets the application_url of this InternalAppModel.  # noqa: E501

        Gets or sets the URL of the application.  # noqa: E501

        :return: The application_url of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._application_url

    @application_url.setter
    def application_url(self, application_url):
        """Sets the application_url of this InternalAppModel.

        Gets or sets the URL of the application.  # noqa: E501

        :param application_url: The application_url of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._application_url = application_url

    @property
    def sdk(self):
        """Gets the sdk of this InternalAppModel.  # noqa: E501

        Gets or sets A value indicating whether the application uses AirWatch Software Development Kit.  # noqa: E501

        :return: The sdk of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._sdk

    @sdk.setter
    def sdk(self, sdk):
        """Sets the sdk of this InternalAppModel.

        Gets or sets A value indicating whether the application uses AirWatch Software Development Kit.  # noqa: E501

        :param sdk: The sdk of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._sdk = sdk

    @property
    def sdk_profile_id(self):
        """Gets the sdk_profile_id of this InternalAppModel.  # noqa: E501

        Gets or sets the SDK profile id of the app if it uses SDK Profile.  # noqa: E501

        :return: The sdk_profile_id of this InternalAppModel.  # noqa: E501
        :rtype: int
        """
        return self._sdk_profile_id

    @sdk_profile_id.setter
    def sdk_profile_id(self, sdk_profile_id):
        """Sets the sdk_profile_id of this InternalAppModel.

        Gets or sets the SDK profile id of the app if it uses SDK Profile.  # noqa: E501

        :param sdk_profile_id: The sdk_profile_id of this InternalAppModel.  # noqa: E501
        :type: int
        """

        self._sdk_profile_id = sdk_profile_id

    @property
    def sdk_profile_uuid(self):
        """Gets the sdk_profile_uuid of this InternalAppModel.  # noqa: E501

        Gets or sets sdk Profile Uuid of the App if it uses SDK Profile.  # noqa: E501

        :return: The sdk_profile_uuid of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._sdk_profile_uuid

    @sdk_profile_uuid.setter
    def sdk_profile_uuid(self, sdk_profile_uuid):
        """Sets the sdk_profile_uuid of this InternalAppModel.

        Gets or sets sdk Profile Uuid of the App if it uses SDK Profile.  # noqa: E501

        :param sdk_profile_uuid: The sdk_profile_uuid of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._sdk_profile_uuid = sdk_profile_uuid

    @property
    def devices_assigned_count(self):
        """Gets the devices_assigned_count of this InternalAppModel.  # noqa: E501

        Gets or sets the number of devices to which current application is Assigned.  # noqa: E501

        :return: The devices_assigned_count of this InternalAppModel.  # noqa: E501
        :rtype: int
        """
        return self._devices_assigned_count

    @devices_assigned_count.setter
    def devices_assigned_count(self, devices_assigned_count):
        """Sets the devices_assigned_count of this InternalAppModel.

        Gets or sets the number of devices to which current application is Assigned.  # noqa: E501

        :param devices_assigned_count: The devices_assigned_count of this InternalAppModel.  # noqa: E501
        :type: int
        """

        self._devices_assigned_count = devices_assigned_count

    @property
    def devices_installed_count(self):
        """Gets the devices_installed_count of this InternalAppModel.  # noqa: E501

        Gets or sets devices on which current application is installed.  # noqa: E501

        :return: The devices_installed_count of this InternalAppModel.  # noqa: E501
        :rtype: int
        """
        return self._devices_installed_count

    @devices_installed_count.setter
    def devices_installed_count(self, devices_installed_count):
        """Sets the devices_installed_count of this InternalAppModel.

        Gets or sets devices on which current application is installed.  # noqa: E501

        :param devices_installed_count: The devices_installed_count of this InternalAppModel.  # noqa: E501
        :type: int
        """

        self._devices_installed_count = devices_installed_count

    @property
    def devices_not_installed_count(self):
        """Gets the devices_not_installed_count of this InternalAppModel.  # noqa: E501

        Gets or sets number of devices to which current application is assigned, but not installed.  # noqa: E501

        :return: The devices_not_installed_count of this InternalAppModel.  # noqa: E501
        :rtype: int
        """
        return self._devices_not_installed_count

    @devices_not_installed_count.setter
    def devices_not_installed_count(self, devices_not_installed_count):
        """Sets the devices_not_installed_count of this InternalAppModel.

        Gets or sets number of devices to which current application is assigned, but not installed.  # noqa: E501

        :param devices_not_installed_count: The devices_not_installed_count of this InternalAppModel.  # noqa: E501
        :type: int
        """

        self._devices_not_installed_count = devices_not_installed_count

    @property
    def rating(self):
        """Gets the rating of this InternalAppModel.  # noqa: E501

        Gets or sets user rating of the app.  # noqa: E501

        :return: The rating of this InternalAppModel.  # noqa: E501
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this InternalAppModel.

        Gets or sets user rating of the app.  # noqa: E501

        :param rating: The rating of this InternalAppModel.  # noqa: E501
        :type: int
        """

        self._rating = rating

    @property
    def change_log(self):
        """Gets the change_log of this InternalAppModel.  # noqa: E501

        Gets or sets the change log for the application.  # noqa: E501

        :return: The change_log of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._change_log

    @change_log.setter
    def change_log(self, change_log):
        """Sets the change_log of this InternalAppModel.

        Gets or sets the change log for the application.  # noqa: E501

        :param change_log: The change_log of this InternalAppModel.  # noqa: E501
        :type: str
        """

        self._change_log = change_log

    @property
    def renewal_date(self):
        """Gets the renewal_date of this InternalAppModel.  # noqa: E501

        Gets or sets expiration date of the Device Provisioning Profile.  # noqa: E501

        :return: The renewal_date of this InternalAppModel.  # noqa: E501
        :rtype: datetime
        """
        return self._renewal_date

    @renewal_date.setter
    def renewal_date(self, renewal_date):
        """Sets the renewal_date of this InternalAppModel.

        Gets or sets expiration date of the Device Provisioning Profile.  # noqa: E501

        :param renewal_date: The renewal_date of this InternalAppModel.  # noqa: E501
        :type: datetime
        """

        self._renewal_date = renewal_date

    @property
    def assignments(self):
        """Gets the assignments of this InternalAppModel.  # noqa: E501

        Gets or sets app configs.  # noqa: E501

        :return: The assignments of this InternalAppModel.  # noqa: E501
        :rtype: list[ApplicationAssignmentModel]
        """
        return self._assignments

    @assignments.setter
    def assignments(self, assignments):
        """Sets the assignments of this InternalAppModel.

        Gets or sets app configs.  # noqa: E501

        :param assignments: The assignments of this InternalAppModel.  # noqa: E501
        :type: list[ApplicationAssignmentModel]
        """

        self._assignments = assignments

    @property
    def excluded_smart_group_ids(self):
        """Gets the excluded_smart_group_ids of this InternalAppModel.  # noqa: E501

        Gets or sets the Smart group Ids to be excluded from receiving the application.  # noqa: E501

        :return: The excluded_smart_group_ids of this InternalAppModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._excluded_smart_group_ids

    @excluded_smart_group_ids.setter
    def excluded_smart_group_ids(self, excluded_smart_group_ids):
        """Sets the excluded_smart_group_ids of this InternalAppModel.

        Gets or sets the Smart group Ids to be excluded from receiving the application.  # noqa: E501

        :param excluded_smart_group_ids: The excluded_smart_group_ids of this InternalAppModel.  # noqa: E501
        :type: list[int]
        """

        self._excluded_smart_group_ids = excluded_smart_group_ids

    @property
    def excluded_smart_group_guids(self):
        """Gets the excluded_smart_group_guids of this InternalAppModel.  # noqa: E501

        Gets or sets the Unique Guid values of the excluded smart groups.  # noqa: E501

        :return: The excluded_smart_group_guids of this InternalAppModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded_smart_group_guids

    @excluded_smart_group_guids.setter
    def excluded_smart_group_guids(self, excluded_smart_group_guids):
        """Sets the excluded_smart_group_guids of this InternalAppModel.

        Gets or sets the Unique Guid values of the excluded smart groups.  # noqa: E501

        :param excluded_smart_group_guids: The excluded_smart_group_guids of this InternalAppModel.  # noqa: E501
        :type: list[str]
        """

        self._excluded_smart_group_guids = excluded_smart_group_guids

    @property
    def msi_deployment_parameters(self):
        """Gets the msi_deployment_parameters of this InternalAppModel.  # noqa: E501

        Gets or sets msi deployment param model. This is valid only for MSI files when Software Distribution is not enabled.  # noqa: E501

        :return: The msi_deployment_parameters of this InternalAppModel.  # noqa: E501
        :rtype: MsiDeploymentParameterModel_
        """
        return self._msi_deployment_parameters

    @msi_deployment_parameters.setter
    def msi_deployment_parameters(self, msi_deployment_parameters):
        """Sets the msi_deployment_parameters of this InternalAppModel.

        Gets or sets msi deployment param model. This is valid only for MSI files when Software Distribution is not enabled.  # noqa: E501

        :param msi_deployment_parameters: The msi_deployment_parameters of this InternalAppModel.  # noqa: E501
        :type: MsiDeploymentParameterModel_
        """

        self._msi_deployment_parameters = msi_deployment_parameters

    @property
    def deployment_options(self):
        """Gets the deployment_options of this InternalAppModel.  # noqa: E501

        Gets or sets application deployment options for software distribution.  # noqa: E501

        :return: The deployment_options of this InternalAppModel.  # noqa: E501
        :rtype: AppDeploymentOptionsModel_
        """
        return self._deployment_options

    @deployment_options.setter
    def deployment_options(self, deployment_options):
        """Sets the deployment_options of this InternalAppModel.

        Gets or sets application deployment options for software distribution.  # noqa: E501

        :param deployment_options: The deployment_options of this InternalAppModel.  # noqa: E501
        :type: AppDeploymentOptionsModel_
        """

        self._deployment_options = deployment_options

    @property
    def files_options(self):
        """Gets the files_options of this InternalAppModel.  # noqa: E501

        Gets or sets application files options.  # noqa: E501

        :return: The files_options of this InternalAppModel.  # noqa: E501
        :rtype: AppFilesOptionsModel_
        """
        return self._files_options

    @files_options.setter
    def files_options(self, files_options):
        """Sets the files_options of this InternalAppModel.

        Gets or sets application files options.  # noqa: E501

        :param files_options: The files_options of this InternalAppModel.  # noqa: E501
        :type: AppFilesOptionsModel_
        """

        self._files_options = files_options

    @property
    def mac_os_software_deployment_summary(self):
        """Gets the mac_os_software_deployment_summary of this InternalAppModel.  # noqa: E501

        Gets or sets macOs software package summary.  # noqa: E501

        :return: The mac_os_software_deployment_summary of this InternalAppModel.  # noqa: E501
        :rtype: MacOsSoftwareDeploymentSummaryModel_
        """
        return self._mac_os_software_deployment_summary

    @mac_os_software_deployment_summary.setter
    def mac_os_software_deployment_summary(self, mac_os_software_deployment_summary):
        """Sets the mac_os_software_deployment_summary of this InternalAppModel.

        Gets or sets macOs software package summary.  # noqa: E501

        :param mac_os_software_deployment_summary: The mac_os_software_deployment_summary of this InternalAppModel.  # noqa: E501
        :type: MacOsSoftwareDeploymentSummaryModel_
        """

        self._mac_os_software_deployment_summary = mac_os_software_deployment_summary

    @property
    def id(self):
        """Gets the id of this InternalAppModel.  # noqa: E501

        Gets or sets identifier.  # noqa: E501

        :return: The id of this InternalAppModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InternalAppModel.

        Gets or sets identifier.  # noqa: E501

        :param id: The id of this InternalAppModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this InternalAppModel.  # noqa: E501

        Gets or sets current objects UUID.  # noqa: E501

        :return: The uuid of this InternalAppModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InternalAppModel.

        Gets or sets current objects UUID.  # noqa: E501

        :param uuid: The uuid of this InternalAppModel.  # noqa: E501
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
        if issubclass(InternalAppModel, dict):
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
        if not isinstance(other, InternalAppModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InternalAppModel):
            return True

        return self.to_dict() != other.to_dict()
