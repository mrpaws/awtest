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


class InternalAppChunkTransactionV1Model(object):
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
        'transaction_id': 'str',
        'blob_id': 'int',
        'device_type': 'int',
        'application_name': 'str',
        'supported_models': 'ApplicationSupportedV1Model',
        'push_mode': 'int',
        'description': 'str',
        'support_email': 'str',
        'support_phone': 'str',
        'developer_name': 'str',
        'developer_email': 'str',
        'developer_phone': 'str',
        'auto_update_version': 'bool',
        'organization_group_uuid': 'str',
        'enable_provisioning': 'bool',
        'upload_via_link': 'bool',
        'bundle_id': 'str',
        'actual_file_version': 'str',
        'app_uem_version': 'str',
        'build_version': 'str',
        'file_name': 'str',
        'supported_processor_architecture': 'str',
        'deployment_param': 'MsiDeploymentParamV1Model',
        'dependency_file': 'bool',
        'deployment_options': 'ApplicationDeploymentOptionsV1Model',
        'files_options': 'ApplicationFilesOptionsV1Model',
        'carryover_assignments': 'bool',
        'iconblob_uuid': 'str',
        'application_source': 'int',
        'criticality': 'int',
        'category_list': 'ApplicationCategoriesV1Model',
        'ear_app_update_mode': 'int'
    }

    attribute_map = {
        'transaction_id': 'transaction_id',
        'blob_id': 'blob_id',
        'device_type': 'device_type',
        'application_name': 'application_name',
        'supported_models': 'supported_models',
        'push_mode': 'push_mode',
        'description': 'description',
        'support_email': 'support_email',
        'support_phone': 'support_phone',
        'developer_name': 'developer_name',
        'developer_email': 'developer_email',
        'developer_phone': 'developer_phone',
        'auto_update_version': 'auto_update_version',
        'organization_group_uuid': 'organization_group_uuid',
        'enable_provisioning': 'enable_provisioning',
        'upload_via_link': 'upload_via_link',
        'bundle_id': 'bundle_id',
        'actual_file_version': 'actual_file_version',
        'app_uem_version': 'app_uem_version',
        'build_version': 'build_version',
        'file_name': 'file_name',
        'supported_processor_architecture': 'supported_processor_architecture',
        'deployment_param': 'deployment_param',
        'dependency_file': 'dependency_file',
        'deployment_options': 'deployment_options',
        'files_options': 'files_options',
        'carryover_assignments': 'carryover_assignments',
        'iconblob_uuid': 'iconblob_uuid',
        'application_source': 'application_source',
        'criticality': 'criticality',
        'category_list': 'category_list',
        'ear_app_update_mode': 'ear_app_update_mode'
    }

    def __init__(self, transaction_id=None, blob_id=None, device_type=None, application_name=None, supported_models=None, push_mode=None, description=None, support_email=None, support_phone=None, developer_name=None, developer_email=None, developer_phone=None, auto_update_version=None, organization_group_uuid=None, enable_provisioning=None, upload_via_link=None, bundle_id=None, actual_file_version=None, app_uem_version=None, build_version=None, file_name=None, supported_processor_architecture=None, deployment_param=None, dependency_file=None, deployment_options=None, files_options=None, carryover_assignments=None, iconblob_uuid=None, application_source=None, criticality=None, category_list=None, ear_app_update_mode=None, _configuration=None):  # noqa: E501
        """InternalAppChunkTransactionV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_id = None
        self._blob_id = None
        self._device_type = None
        self._application_name = None
        self._supported_models = None
        self._push_mode = None
        self._description = None
        self._support_email = None
        self._support_phone = None
        self._developer_name = None
        self._developer_email = None
        self._developer_phone = None
        self._auto_update_version = None
        self._organization_group_uuid = None
        self._enable_provisioning = None
        self._upload_via_link = None
        self._bundle_id = None
        self._actual_file_version = None
        self._app_uem_version = None
        self._build_version = None
        self._file_name = None
        self._supported_processor_architecture = None
        self._deployment_param = None
        self._dependency_file = None
        self._deployment_options = None
        self._files_options = None
        self._carryover_assignments = None
        self._iconblob_uuid = None
        self._application_source = None
        self._criticality = None
        self._category_list = None
        self._ear_app_update_mode = None
        self.discriminator = None

        if transaction_id is not None:
            self.transaction_id = transaction_id
        if blob_id is not None:
            self.blob_id = blob_id
        if device_type is not None:
            self.device_type = device_type
        if application_name is not None:
            self.application_name = application_name
        if supported_models is not None:
            self.supported_models = supported_models
        if push_mode is not None:
            self.push_mode = push_mode
        if description is not None:
            self.description = description
        if support_email is not None:
            self.support_email = support_email
        if support_phone is not None:
            self.support_phone = support_phone
        if developer_name is not None:
            self.developer_name = developer_name
        if developer_email is not None:
            self.developer_email = developer_email
        if developer_phone is not None:
            self.developer_phone = developer_phone
        if auto_update_version is not None:
            self.auto_update_version = auto_update_version
        if organization_group_uuid is not None:
            self.organization_group_uuid = organization_group_uuid
        if enable_provisioning is not None:
            self.enable_provisioning = enable_provisioning
        if upload_via_link is not None:
            self.upload_via_link = upload_via_link
        if bundle_id is not None:
            self.bundle_id = bundle_id
        if actual_file_version is not None:
            self.actual_file_version = actual_file_version
        if app_uem_version is not None:
            self.app_uem_version = app_uem_version
        if build_version is not None:
            self.build_version = build_version
        if file_name is not None:
            self.file_name = file_name
        if supported_processor_architecture is not None:
            self.supported_processor_architecture = supported_processor_architecture
        if deployment_param is not None:
            self.deployment_param = deployment_param
        if dependency_file is not None:
            self.dependency_file = dependency_file
        if deployment_options is not None:
            self.deployment_options = deployment_options
        if files_options is not None:
            self.files_options = files_options
        if carryover_assignments is not None:
            self.carryover_assignments = carryover_assignments
        if iconblob_uuid is not None:
            self.iconblob_uuid = iconblob_uuid
        if application_source is not None:
            self.application_source = application_source
        if criticality is not None:
            self.criticality = criticality
        if category_list is not None:
            self.category_list = category_list
        if ear_app_update_mode is not None:
            self.ear_app_update_mode = ear_app_update_mode

    @property
    def transaction_id(self):
        """Gets the transaction_id of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets transactionId of the uploaded chunk.  # noqa: E501

        :return: The transaction_id of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this InternalAppChunkTransactionV1Model.

        Gets or sets transactionId of the uploaded chunk.  # noqa: E501

        :param transaction_id: The transaction_id of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def blob_id(self):
        """Gets the blob_id of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets id of the uploaded blob data.  # noqa: E501

        :return: The blob_id of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: int
        """
        return self._blob_id

    @blob_id.setter
    def blob_id(self, blob_id):
        """Sets the blob_id of this InternalAppChunkTransactionV1Model.

        Gets or sets id of the uploaded blob data.  # noqa: E501

        :param blob_id: The blob_id of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: int
        """

        self._blob_id = blob_id

    @property
    def device_type(self):
        """Gets the device_type of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets Device Type. Supported values : Apple = 2, Android = 5, WinRT = 12, AppleOSX = 10, AppleTv = 14, WindowsPhone8 = 11.  # noqa: E501

        :return: The device_type of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this InternalAppChunkTransactionV1Model.

        Gets or sets Device Type. Supported values : Apple = 2, Android = 5, WinRT = 12, AppleOSX = 10, AppleTv = 14, WindowsPhone8 = 11.  # noqa: E501

        :param device_type: The device_type of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 100, 101, 102, 103, 104, 105, 200, 201, 1000]  # noqa: E501
        if (self._configuration.client_side_validation and
                device_type not in allowed_values):
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def application_name(self):
        """Gets the application_name of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets application Name.  # noqa: E501

        :return: The application_name of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this InternalAppChunkTransactionV1Model.

        Gets or sets application Name.  # noqa: E501

        :param application_name: The application_name of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def supported_models(self):
        """Gets the supported_models of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets model.  # noqa: E501

        :return: The supported_models of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: ApplicationSupportedV1Model
        """
        return self._supported_models

    @supported_models.setter
    def supported_models(self, supported_models):
        """Sets the supported_models of this InternalAppChunkTransactionV1Model.

        Gets or sets model.  # noqa: E501

        :param supported_models: The supported_models of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: ApplicationSupportedV1Model
        """

        self._supported_models = supported_models

    @property
    def push_mode(self):
        """Gets the push_mode of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets push mode of the application (Required). Supported values: Auto, OnDemand.  # noqa: E501

        :return: The push_mode of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: int
        """
        return self._push_mode

    @push_mode.setter
    def push_mode(self, push_mode):
        """Sets the push_mode of this InternalAppChunkTransactionV1Model.

        Gets or sets push mode of the application (Required). Supported values: Auto, OnDemand.  # noqa: E501

        :param push_mode: The push_mode of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if (self._configuration.client_side_validation and
                push_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `push_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(push_mode, allowed_values)
            )

        self._push_mode = push_mode

    @property
    def description(self):
        """Gets the description of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets description of the application.  # noqa: E501

        :return: The description of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InternalAppChunkTransactionV1Model.

        Gets or sets description of the application.  # noqa: E501

        :param description: The description of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def support_email(self):
        """Gets the support_email of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets support email.  # noqa: E501

        :return: The support_email of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._support_email

    @support_email.setter
    def support_email(self, support_email):
        """Sets the support_email of this InternalAppChunkTransactionV1Model.

        Gets or sets support email.  # noqa: E501

        :param support_email: The support_email of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._support_email = support_email

    @property
    def support_phone(self):
        """Gets the support_phone of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets support Phone number.  # noqa: E501

        :return: The support_phone of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._support_phone

    @support_phone.setter
    def support_phone(self, support_phone):
        """Sets the support_phone of this InternalAppChunkTransactionV1Model.

        Gets or sets support Phone number.  # noqa: E501

        :param support_phone: The support_phone of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._support_phone = support_phone

    @property
    def developer_name(self):
        """Gets the developer_name of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets developer Name.  # noqa: E501

        :return: The developer_name of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._developer_name

    @developer_name.setter
    def developer_name(self, developer_name):
        """Sets the developer_name of this InternalAppChunkTransactionV1Model.

        Gets or sets developer Name.  # noqa: E501

        :param developer_name: The developer_name of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._developer_name = developer_name

    @property
    def developer_email(self):
        """Gets the developer_email of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets email address of developer.  # noqa: E501

        :return: The developer_email of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._developer_email

    @developer_email.setter
    def developer_email(self, developer_email):
        """Sets the developer_email of this InternalAppChunkTransactionV1Model.

        Gets or sets email address of developer.  # noqa: E501

        :param developer_email: The developer_email of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._developer_email = developer_email

    @property
    def developer_phone(self):
        """Gets the developer_phone of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets phone number of developer.  # noqa: E501

        :return: The developer_phone of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._developer_phone

    @developer_phone.setter
    def developer_phone(self, developer_phone):
        """Sets the developer_phone of this InternalAppChunkTransactionV1Model.

        Gets or sets phone number of developer.  # noqa: E501

        :param developer_phone: The developer_phone of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._developer_phone = developer_phone

    @property
    def auto_update_version(self):
        """Gets the auto_update_version of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets a value indicating whether auto update version in case of Ondemand mode.  # noqa: E501

        :return: The auto_update_version of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._auto_update_version

    @auto_update_version.setter
    def auto_update_version(self, auto_update_version):
        """Sets the auto_update_version of this InternalAppChunkTransactionV1Model.

        Gets or sets a value indicating whether auto update version in case of Ondemand mode.  # noqa: E501

        :param auto_update_version: The auto_update_version of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: bool
        """

        self._auto_update_version = auto_update_version

    @property
    def organization_group_uuid(self):
        """Gets the organization_group_uuid of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets organizationGroupUuid where the application will be created.  # noqa: E501

        :return: The organization_group_uuid of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._organization_group_uuid

    @organization_group_uuid.setter
    def organization_group_uuid(self, organization_group_uuid):
        """Sets the organization_group_uuid of this InternalAppChunkTransactionV1Model.

        Gets or sets organizationGroupUuid where the application will be created.  # noqa: E501

        :param organization_group_uuid: The organization_group_uuid of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._organization_group_uuid = organization_group_uuid

    @property
    def enable_provisioning(self):
        """Gets the enable_provisioning of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets a value indicating whether flag to indicate Application will be used for Product Provisioning. Valid values: true, false.  # noqa: E501

        :return: The enable_provisioning of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._enable_provisioning

    @enable_provisioning.setter
    def enable_provisioning(self, enable_provisioning):
        """Sets the enable_provisioning of this InternalAppChunkTransactionV1Model.

        Gets or sets a value indicating whether flag to indicate Application will be used for Product Provisioning. Valid values: true, false.  # noqa: E501

        :param enable_provisioning: The enable_provisioning of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: bool
        """

        self._enable_provisioning = enable_provisioning

    @property
    def upload_via_link(self):
        """Gets the upload_via_link of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets a value indicating whether gets or Sets the Value indicating if the blob was uploaded as a link.  # noqa: E501

        :return: The upload_via_link of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._upload_via_link

    @upload_via_link.setter
    def upload_via_link(self, upload_via_link):
        """Sets the upload_via_link of this InternalAppChunkTransactionV1Model.

        Gets or sets a value indicating whether gets or Sets the Value indicating if the blob was uploaded as a link.  # noqa: E501

        :param upload_via_link: The upload_via_link of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: bool
        """

        self._upload_via_link = upload_via_link

    @property
    def bundle_id(self):
        """Gets the bundle_id of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or Sets the Value indicating the Application Bundle Id.  # noqa: E501

        :return: The bundle_id of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this InternalAppChunkTransactionV1Model.

        Gets or Sets the Value indicating the Application Bundle Id.  # noqa: E501

        :param bundle_id: The bundle_id of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._bundle_id = bundle_id

    @property
    def actual_file_version(self):
        """Gets the actual_file_version of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or Sets the Value indicating the Actual File Version of the app.  # noqa: E501

        :return: The actual_file_version of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._actual_file_version

    @actual_file_version.setter
    def actual_file_version(self, actual_file_version):
        """Sets the actual_file_version of this InternalAppChunkTransactionV1Model.

        Gets or Sets the Value indicating the Actual File Version of the app.  # noqa: E501

        :param actual_file_version: The actual_file_version of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._actual_file_version = actual_file_version

    @property
    def app_uem_version(self):
        """Gets the app_uem_version of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets app Version.  # noqa: E501

        :return: The app_uem_version of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._app_uem_version

    @app_uem_version.setter
    def app_uem_version(self, app_uem_version):
        """Sets the app_uem_version of this InternalAppChunkTransactionV1Model.

        Gets or sets app Version.  # noqa: E501

        :param app_uem_version: The app_uem_version of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._app_uem_version = app_uem_version

    @property
    def build_version(self):
        """Gets the build_version of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets the build version.  # noqa: E501

        :return: The build_version of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this InternalAppChunkTransactionV1Model.

        Gets or sets the build version.  # noqa: E501

        :param build_version: The build_version of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._build_version = build_version

    @property
    def file_name(self):
        """Gets the file_name of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets name of the Application file along with its extension.  # noqa: E501

        :return: The file_name of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this InternalAppChunkTransactionV1Model.

        Gets or sets name of the Application file along with its extension.  # noqa: E501

        :param file_name: The file_name of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def supported_processor_architecture(self):
        """Gets the supported_processor_architecture of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets supported processor architecture. Ex: x86, x64. This is valid only for MSI, ZIP, EXE files with software distribution.  # noqa: E501

        :return: The supported_processor_architecture of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._supported_processor_architecture

    @supported_processor_architecture.setter
    def supported_processor_architecture(self, supported_processor_architecture):
        """Sets the supported_processor_architecture of this InternalAppChunkTransactionV1Model.

        Gets or sets supported processor architecture. Ex: x86, x64. This is valid only for MSI, ZIP, EXE files with software distribution.  # noqa: E501

        :param supported_processor_architecture: The supported_processor_architecture of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._supported_processor_architecture = supported_processor_architecture

    @property
    def deployment_param(self):
        """Gets the deployment_param of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets msi deployment param model. This is valid only for MSI files when software distribution is not enabled.  # noqa: E501

        :return: The deployment_param of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: MsiDeploymentParamV1Model
        """
        return self._deployment_param

    @deployment_param.setter
    def deployment_param(self, deployment_param):
        """Sets the deployment_param of this InternalAppChunkTransactionV1Model.

        Gets or sets msi deployment param model. This is valid only for MSI files when software distribution is not enabled.  # noqa: E501

        :param deployment_param: The deployment_param of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: MsiDeploymentParamV1Model
        """

        self._deployment_param = deployment_param

    @property
    def dependency_file(self):
        """Gets the dependency_file of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets a value indicating whether indicates whether uploaded file is a dependency file.  # noqa: E501

        :return: The dependency_file of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._dependency_file

    @dependency_file.setter
    def dependency_file(self, dependency_file):
        """Sets the dependency_file of this InternalAppChunkTransactionV1Model.

        Gets or sets a value indicating whether indicates whether uploaded file is a dependency file.  # noqa: E501

        :param dependency_file: The dependency_file of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: bool
        """

        self._dependency_file = dependency_file

    @property
    def deployment_options(self):
        """Gets the deployment_options of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets application deployment options for software distribution.  # noqa: E501

        :return: The deployment_options of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: ApplicationDeploymentOptionsV1Model
        """
        return self._deployment_options

    @deployment_options.setter
    def deployment_options(self, deployment_options):
        """Sets the deployment_options of this InternalAppChunkTransactionV1Model.

        Gets or sets application deployment options for software distribution.  # noqa: E501

        :param deployment_options: The deployment_options of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: ApplicationDeploymentOptionsV1Model
        """

        self._deployment_options = deployment_options

    @property
    def files_options(self):
        """Gets the files_options of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets application files options.  # noqa: E501

        :return: The files_options of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: ApplicationFilesOptionsV1Model
        """
        return self._files_options

    @files_options.setter
    def files_options(self, files_options):
        """Sets the files_options of this InternalAppChunkTransactionV1Model.

        Gets or sets application files options.  # noqa: E501

        :param files_options: The files_options of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: ApplicationFilesOptionsV1Model
        """

        self._files_options = files_options

    @property
    def carryover_assignments(self):
        """Gets the carryover_assignments of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets a value indicating whether should Assignment Be Carried Over From Older Version Of App.  The default value is true to not break existing contracts.  # noqa: E501

        :return: The carryover_assignments of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: bool
        """
        return self._carryover_assignments

    @carryover_assignments.setter
    def carryover_assignments(self, carryover_assignments):
        """Sets the carryover_assignments of this InternalAppChunkTransactionV1Model.

        Gets or sets a value indicating whether should Assignment Be Carried Over From Older Version Of App.  The default value is true to not break existing contracts.  # noqa: E501

        :param carryover_assignments: The carryover_assignments of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: bool
        """

        self._carryover_assignments = carryover_assignments

    @property
    def iconblob_uuid(self):
        """Gets the iconblob_uuid of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets uuid of the uploaded icon blob data.  # noqa: E501

        :return: The iconblob_uuid of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: str
        """
        return self._iconblob_uuid

    @iconblob_uuid.setter
    def iconblob_uuid(self, iconblob_uuid):
        """Sets the iconblob_uuid of this InternalAppChunkTransactionV1Model.

        Gets or sets uuid of the uploaded icon blob data.  # noqa: E501

        :param iconblob_uuid: The iconblob_uuid of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: str
        """

        self._iconblob_uuid = iconblob_uuid

    @property
    def application_source(self):
        """Gets the application_source of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets the internal application source. Supported Values- AirWatch = 1, AndroidWork = 2, WindowsPhoneMarketPlace = 3, WindowsStore = 4, WindowsBusinessStore = 5, AndroidAvenger = 6, Boxer = 7, EnterpriseAppRepository = 8.  # noqa: E501

        :return: The application_source of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: int
        """
        return self._application_source

    @application_source.setter
    def application_source(self, application_source):
        """Sets the application_source of this InternalAppChunkTransactionV1Model.

        Gets or sets the internal application source. Supported Values- AirWatch = 1, AndroidWork = 2, WindowsPhoneMarketPlace = 3, WindowsStore = 4, WindowsBusinessStore = 5, AndroidAvenger = 6, Boxer = 7, EnterpriseAppRepository = 8.  # noqa: E501

        :param application_source: The application_source of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # noqa: E501
        if (self._configuration.client_side_validation and
                application_source not in allowed_values):
            raise ValueError(
                "Invalid value for `application_source` ({0}), must be one of {1}"  # noqa: E501
                .format(application_source, allowed_values)
            )

        self._application_source = application_source

    @property
    def criticality(self):
        """Gets the criticality of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets the internal application criticality. Known usage is, Flexera SVM sets this for vulnerable apps. Supported Values: NONE, LESS, MODERATE, HIGH, EXTREME.  # noqa: E501

        :return: The criticality of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: int
        """
        return self._criticality

    @criticality.setter
    def criticality(self, criticality):
        """Sets the criticality of this InternalAppChunkTransactionV1Model.

        Gets or sets the internal application criticality. Known usage is, Flexera SVM sets this for vulnerable apps. Supported Values: NONE, LESS, MODERATE, HIGH, EXTREME.  # noqa: E501

        :param criticality: The criticality of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4]  # noqa: E501
        if (self._configuration.client_side_validation and
                criticality not in allowed_values):
            raise ValueError(
                "Invalid value for `criticality` ({0}), must be one of {1}"  # noqa: E501
                .format(criticality, allowed_values)
            )

        self._criticality = criticality

    @property
    def category_list(self):
        """Gets the category_list of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets the various categories that are associated to an application. Represented by the category Id and Description.  # noqa: E501

        :return: The category_list of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: ApplicationCategoriesV1Model
        """
        return self._category_list

    @category_list.setter
    def category_list(self, category_list):
        """Sets the category_list of this InternalAppChunkTransactionV1Model.

        Gets or sets the various categories that are associated to an application. Represented by the category Id and Description.  # noqa: E501

        :param category_list: The category_list of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: ApplicationCategoriesV1Model
        """

        self._category_list = category_list

    @property
    def ear_app_update_mode(self):
        """Gets the ear_app_update_mode of this InternalAppChunkTransactionV1Model.  # noqa: E501

        Gets or sets EAR app update preference. Supported Values: None = 0, Notify = 1, AutoUpdate = 2.  # noqa: E501

        :return: The ear_app_update_mode of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :rtype: int
        """
        return self._ear_app_update_mode

    @ear_app_update_mode.setter
    def ear_app_update_mode(self, ear_app_update_mode):
        """Sets the ear_app_update_mode of this InternalAppChunkTransactionV1Model.

        Gets or sets EAR app update preference. Supported Values: None = 0, Notify = 1, AutoUpdate = 2.  # noqa: E501

        :param ear_app_update_mode: The ear_app_update_mode of this InternalAppChunkTransactionV1Model.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if (self._configuration.client_side_validation and
                ear_app_update_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `ear_app_update_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(ear_app_update_mode, allowed_values)
            )

        self._ear_app_update_mode = ear_app_update_mode

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
        if issubclass(InternalAppChunkTransactionV1Model, dict):
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
        if not isinstance(other, InternalAppChunkTransactionV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InternalAppChunkTransactionV1Model):
            return True

        return self.to_dict() != other.to_dict()
