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


class PurchasedApplicationEntity(object):
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
        'application_size': 'str',
        'application_url': 'str',
        'assignments': 'list[PurchasedAppAssignment]',
        'bundle_id': 'str',
        'external_id': 'str',
        'is_reimbursable': 'bool',
        'large_icon_uri': 'str',
        'medium_icon_uri': 'str',
        'small_icon_uri': 'str',
        'location_group_id': 'int',
        'platform': 'int',
        'redeemable_codes': 'PurchasedAppRedeemableCodesDetails_',
        'managed_distribution': 'PurchasedAppManagedDistributionDetials_',
        'deployment': 'PurchasedAppDeploymentDetails_',
        'app_version': 'str',
        'actual_file_version': 'str',
        'app_type': 'str',
        'status': 'str',
        'supported_models': 'ApplicationSupportedModels_',
        'assignment_status': 'str',
        'comments': 'str',
        'is_auto_update_enabled': 'bool',
        'categories': 'list[str]',
        'id': 'EntityId_',
        'uuid': 'str'
    }

    attribute_map = {
        'application_name': 'ApplicationName',
        'application_size': 'ApplicationSize',
        'application_url': 'ApplicationUrl',
        'assignments': 'Assignments',
        'bundle_id': 'BundleId',
        'external_id': 'ExternalId',
        'is_reimbursable': 'IsReimbursable',
        'large_icon_uri': 'LargeIconUri',
        'medium_icon_uri': 'MediumIconUri',
        'small_icon_uri': 'SmallIconUri',
        'location_group_id': 'LocationGroupId',
        'platform': 'Platform',
        'redeemable_codes': 'RedeemableCodes',
        'managed_distribution': 'ManagedDistribution',
        'deployment': 'Deployment',
        'app_version': 'AppVersion',
        'actual_file_version': 'ActualFileVersion',
        'app_type': 'AppType',
        'status': 'Status',
        'supported_models': 'SupportedModels',
        'assignment_status': 'AssignmentStatus',
        'comments': 'Comments',
        'is_auto_update_enabled': 'IsAutoUpdateEnabled',
        'categories': 'Categories',
        'id': 'Id',
        'uuid': 'Uuid'
    }

    def __init__(self, application_name=None, application_size=None, application_url=None, assignments=None, bundle_id=None, external_id=None, is_reimbursable=None, large_icon_uri=None, medium_icon_uri=None, small_icon_uri=None, location_group_id=None, platform=None, redeemable_codes=None, managed_distribution=None, deployment=None, app_version=None, actual_file_version=None, app_type=None, status=None, supported_models=None, assignment_status=None, comments=None, is_auto_update_enabled=None, categories=None, id=None, uuid=None, _configuration=None):  # noqa: E501
        """PurchasedApplicationEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_name = None
        self._application_size = None
        self._application_url = None
        self._assignments = None
        self._bundle_id = None
        self._external_id = None
        self._is_reimbursable = None
        self._large_icon_uri = None
        self._medium_icon_uri = None
        self._small_icon_uri = None
        self._location_group_id = None
        self._platform = None
        self._redeemable_codes = None
        self._managed_distribution = None
        self._deployment = None
        self._app_version = None
        self._actual_file_version = None
        self._app_type = None
        self._status = None
        self._supported_models = None
        self._assignment_status = None
        self._comments = None
        self._is_auto_update_enabled = None
        self._categories = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if application_name is not None:
            self.application_name = application_name
        if application_size is not None:
            self.application_size = application_size
        if application_url is not None:
            self.application_url = application_url
        if assignments is not None:
            self.assignments = assignments
        if bundle_id is not None:
            self.bundle_id = bundle_id
        if external_id is not None:
            self.external_id = external_id
        if is_reimbursable is not None:
            self.is_reimbursable = is_reimbursable
        if large_icon_uri is not None:
            self.large_icon_uri = large_icon_uri
        if medium_icon_uri is not None:
            self.medium_icon_uri = medium_icon_uri
        if small_icon_uri is not None:
            self.small_icon_uri = small_icon_uri
        if location_group_id is not None:
            self.location_group_id = location_group_id
        if platform is not None:
            self.platform = platform
        if redeemable_codes is not None:
            self.redeemable_codes = redeemable_codes
        if managed_distribution is not None:
            self.managed_distribution = managed_distribution
        if deployment is not None:
            self.deployment = deployment
        if app_version is not None:
            self.app_version = app_version
        if actual_file_version is not None:
            self.actual_file_version = actual_file_version
        if app_type is not None:
            self.app_type = app_type
        if status is not None:
            self.status = status
        if supported_models is not None:
            self.supported_models = supported_models
        if assignment_status is not None:
            self.assignment_status = assignment_status
        if comments is not None:
            self.comments = comments
        if is_auto_update_enabled is not None:
            self.is_auto_update_enabled = is_auto_update_enabled
        if categories is not None:
            self.categories = categories
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def application_name(self):
        """Gets the application_name of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets application Name.  # noqa: E501

        :return: The application_name of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this PurchasedApplicationEntity.

        Gets or sets application Name.  # noqa: E501

        :param application_name: The application_name of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def application_size(self):
        """Gets the application_size of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets application size.  # noqa: E501

        :return: The application_size of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._application_size

    @application_size.setter
    def application_size(self, application_size):
        """Sets the application_size of this PurchasedApplicationEntity.

        Gets or sets application size.  # noqa: E501

        :param application_size: The application_size of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._application_size = application_size

    @property
    def application_url(self):
        """Gets the application_url of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets itunes URL of the application.  # noqa: E501

        :return: The application_url of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._application_url

    @application_url.setter
    def application_url(self, application_url):
        """Sets the application_url of this PurchasedApplicationEntity.

        Gets or sets itunes URL of the application.  # noqa: E501

        :param application_url: The application_url of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._application_url = application_url

    @property
    def assignments(self):
        """Gets the assignments of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets application Assignment List.  # noqa: E501

        :return: The assignments of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: list[PurchasedAppAssignment]
        """
        return self._assignments

    @assignments.setter
    def assignments(self, assignments):
        """Sets the assignments of this PurchasedApplicationEntity.

        Gets or sets application Assignment List.  # noqa: E501

        :param assignments: The assignments of this PurchasedApplicationEntity.  # noqa: E501
        :type: list[PurchasedAppAssignment]
        """

        self._assignments = assignments

    @property
    def bundle_id(self):
        """Gets the bundle_id of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets package id.  # noqa: E501

        :return: The bundle_id of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this PurchasedApplicationEntity.

        Gets or sets package id.  # noqa: E501

        :param bundle_id: The bundle_id of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._bundle_id = bundle_id

    @property
    def external_id(self):
        """Gets the external_id of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets iD for an external application store (i.e. iTunes ID).  # noqa: E501

        :return: The external_id of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PurchasedApplicationEntity.

        Gets or sets iD for an external application store (i.e. iTunes ID).  # noqa: E501

        :param external_id: The external_id of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def is_reimbursable(self):
        """Gets the is_reimbursable of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets a value indicating whether determines if the app is reimbursable or reimbursable not defined.  # noqa: E501

        :return: The is_reimbursable of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: bool
        """
        return self._is_reimbursable

    @is_reimbursable.setter
    def is_reimbursable(self, is_reimbursable):
        """Sets the is_reimbursable of this PurchasedApplicationEntity.

        Gets or sets a value indicating whether determines if the app is reimbursable or reimbursable not defined.  # noqa: E501

        :param is_reimbursable: The is_reimbursable of this PurchasedApplicationEntity.  # noqa: E501
        :type: bool
        """

        self._is_reimbursable = is_reimbursable

    @property
    def large_icon_uri(self):
        """Gets the large_icon_uri of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets uRL to an externally hosted icon - large size.  # noqa: E501

        :return: The large_icon_uri of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._large_icon_uri

    @large_icon_uri.setter
    def large_icon_uri(self, large_icon_uri):
        """Sets the large_icon_uri of this PurchasedApplicationEntity.

        Gets or sets uRL to an externally hosted icon - large size.  # noqa: E501

        :param large_icon_uri: The large_icon_uri of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._large_icon_uri = large_icon_uri

    @property
    def medium_icon_uri(self):
        """Gets the medium_icon_uri of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets uRL to an externally hosted icon - medium size.  # noqa: E501

        :return: The medium_icon_uri of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._medium_icon_uri

    @medium_icon_uri.setter
    def medium_icon_uri(self, medium_icon_uri):
        """Sets the medium_icon_uri of this PurchasedApplicationEntity.

        Gets or sets uRL to an externally hosted icon - medium size.  # noqa: E501

        :param medium_icon_uri: The medium_icon_uri of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._medium_icon_uri = medium_icon_uri

    @property
    def small_icon_uri(self):
        """Gets the small_icon_uri of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets uRL to an externally hosted icon - small size.  # noqa: E501

        :return: The small_icon_uri of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._small_icon_uri

    @small_icon_uri.setter
    def small_icon_uri(self, small_icon_uri):
        """Sets the small_icon_uri of this PurchasedApplicationEntity.

        Gets or sets uRL to an externally hosted icon - small size.  # noqa: E501

        :param small_icon_uri: The small_icon_uri of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._small_icon_uri = small_icon_uri

    @property
    def location_group_id(self):
        """Gets the location_group_id of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets location Group id where the application is created.  # noqa: E501

        :return: The location_group_id of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: int
        """
        return self._location_group_id

    @location_group_id.setter
    def location_group_id(self, location_group_id):
        """Sets the location_group_id of this PurchasedApplicationEntity.

        Gets or sets location Group id where the application is created.  # noqa: E501

        :param location_group_id: The location_group_id of this PurchasedApplicationEntity.  # noqa: E501
        :type: int
        """

        self._location_group_id = location_group_id

    @property
    def platform(self):
        """Gets the platform of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets device Type supported by the application.  # noqa: E501

        :return: The platform of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: int
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this PurchasedApplicationEntity.

        Gets or sets device Type supported by the application.  # noqa: E501

        :param platform: The platform of this PurchasedApplicationEntity.  # noqa: E501
        :type: int
        """

        self._platform = platform

    @property
    def redeemable_codes(self):
        """Gets the redeemable_codes of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets redeemable Codes Details.  # noqa: E501

        :return: The redeemable_codes of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: PurchasedAppRedeemableCodesDetails_
        """
        return self._redeemable_codes

    @redeemable_codes.setter
    def redeemable_codes(self, redeemable_codes):
        """Sets the redeemable_codes of this PurchasedApplicationEntity.

        Gets or sets redeemable Codes Details.  # noqa: E501

        :param redeemable_codes: The redeemable_codes of this PurchasedApplicationEntity.  # noqa: E501
        :type: PurchasedAppRedeemableCodesDetails_
        """

        self._redeemable_codes = redeemable_codes

    @property
    def managed_distribution(self):
        """Gets the managed_distribution of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets managed Distribution Details.  # noqa: E501

        :return: The managed_distribution of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: PurchasedAppManagedDistributionDetials_
        """
        return self._managed_distribution

    @managed_distribution.setter
    def managed_distribution(self, managed_distribution):
        """Sets the managed_distribution of this PurchasedApplicationEntity.

        Gets or sets managed Distribution Details.  # noqa: E501

        :param managed_distribution: The managed_distribution of this PurchasedApplicationEntity.  # noqa: E501
        :type: PurchasedAppManagedDistributionDetials_
        """

        self._managed_distribution = managed_distribution

    @property
    def deployment(self):
        """Gets the deployment of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets deployment Details.  # noqa: E501

        :return: The deployment of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: PurchasedAppDeploymentDetails_
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this PurchasedApplicationEntity.

        Gets or sets deployment Details.  # noqa: E501

        :param deployment: The deployment of this PurchasedApplicationEntity.  # noqa: E501
        :type: PurchasedAppDeploymentDetails_
        """

        self._deployment = deployment

    @property
    def app_version(self):
        """Gets the app_version of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets app version.  # noqa: E501

        :return: The app_version of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this PurchasedApplicationEntity.

        Gets or sets app version.  # noqa: E501

        :param app_version: The app_version of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._app_version = app_version

    @property
    def actual_file_version(self):
        """Gets the actual_file_version of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets actual file version of the app.  # noqa: E501

        :return: The actual_file_version of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._actual_file_version

    @actual_file_version.setter
    def actual_file_version(self, actual_file_version):
        """Sets the actual_file_version of this PurchasedApplicationEntity.

        Gets or sets actual file version of the app.  # noqa: E501

        :param actual_file_version: The actual_file_version of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._actual_file_version = actual_file_version

    @property
    def app_type(self):
        """Gets the app_type of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets app type (public/purchased/internal).  # noqa: E501

        :return: The app_type of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this PurchasedApplicationEntity.

        Gets or sets app type (public/purchased/internal).  # noqa: E501

        :param app_type: The app_type of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._app_type = app_type

    @property
    def status(self):
        """Gets the status of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets status to indicate whether app is active or not.  # noqa: E501

        :return: The status of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PurchasedApplicationEntity.

        Gets or sets status to indicate whether app is active or not.  # noqa: E501

        :param status: The status of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def supported_models(self):
        """Gets the supported_models of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets device Model supported by the app.  # noqa: E501

        :return: The supported_models of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: ApplicationSupportedModels_
        """
        return self._supported_models

    @supported_models.setter
    def supported_models(self, supported_models):
        """Sets the supported_models of this PurchasedApplicationEntity.

        Gets or sets device Model supported by the app.  # noqa: E501

        :param supported_models: The supported_models of this PurchasedApplicationEntity.  # noqa: E501
        :type: ApplicationSupportedModels_
        """

        self._supported_models = supported_models

    @property
    def assignment_status(self):
        """Gets the assignment_status of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets assignemt status.  # noqa: E501

        :return: The assignment_status of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._assignment_status

    @assignment_status.setter
    def assignment_status(self, assignment_status):
        """Sets the assignment_status of this PurchasedApplicationEntity.

        Gets or sets assignemt status.  # noqa: E501

        :param assignment_status: The assignment_status of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._assignment_status = assignment_status

    @property
    def comments(self):
        """Gets the comments of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets short comments on the app.  # noqa: E501

        :return: The comments of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this PurchasedApplicationEntity.

        Gets or sets short comments on the app.  # noqa: E501

        :param comments: The comments of this PurchasedApplicationEntity.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def is_auto_update_enabled(self):
        """Gets the is_auto_update_enabled of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets a value indicating whether is auto update enabled for the particular device based VPP application.  # noqa: E501

        :return: The is_auto_update_enabled of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: bool
        """
        return self._is_auto_update_enabled

    @is_auto_update_enabled.setter
    def is_auto_update_enabled(self, is_auto_update_enabled):
        """Sets the is_auto_update_enabled of this PurchasedApplicationEntity.

        Gets or sets a value indicating whether is auto update enabled for the particular device based VPP application.  # noqa: E501

        :param is_auto_update_enabled: The is_auto_update_enabled of this PurchasedApplicationEntity.  # noqa: E501
        :type: bool
        """

        self._is_auto_update_enabled = is_auto_update_enabled

    @property
    def categories(self):
        """Gets the categories of this PurchasedApplicationEntity.  # noqa: E501

        Gets or sets get or set the Application Categories.  # noqa: E501

        :return: The categories of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this PurchasedApplicationEntity.

        Gets or sets get or set the Application Categories.  # noqa: E501

        :param categories: The categories of this PurchasedApplicationEntity.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def id(self):
        """Gets the id of this PurchasedApplicationEntity.  # noqa: E501


        :return: The id of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: EntityId_
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PurchasedApplicationEntity.


        :param id: The id of this PurchasedApplicationEntity.  # noqa: E501
        :type: EntityId_
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this PurchasedApplicationEntity.  # noqa: E501


        :return: The uuid of this PurchasedApplicationEntity.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PurchasedApplicationEntity.


        :param uuid: The uuid of this PurchasedApplicationEntity.  # noqa: E501
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
        if issubclass(PurchasedApplicationEntity, dict):
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
        if not isinstance(other, PurchasedApplicationEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PurchasedApplicationEntity):
            return True

        return self.to_dict() != other.to_dict()
