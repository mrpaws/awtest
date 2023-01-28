# coding: utf-8

# flake8: noqa
"""
    MAM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from mamv2.models.action3 import Action3
from mamv2.models.app_assignment_bsp_v1_model import AppAssignmentBspV1Model
from mamv2.models.app_assignment_distribution_v2_model import AppAssignmentDistributionV2Model
from mamv2.models.app_assignment_restriction_v1_model import AppAssignmentRestrictionV1Model
from mamv2.models.app_assignment_rule_v2_model import AppAssignmentRuleV2Model
from mamv2.models.app_assignment_tunnel_v1_model import AppAssignmentTunnelV1Model
from mamv2.models.app_assignment_v2_model import AppAssignmentV2Model
from mamv2.models.app_assignment_vpp_v1_model import AppAssignmentVppV1Model
from mamv2.models.app_config_template_v2_model import AppConfigTemplateV2Model
from mamv2.models.app_configuration_v1_model import AppConfigurationV1Model
from mamv2.models.app_criteria_api_model import AppCriteriaApiModel
from mamv2.models.app_criteria_api_model_ import AppCriteriaApiModel_
from mamv2.models.app_dependency_model import AppDependencyModel
from mamv2.models.app_deployment_options_model import AppDeploymentOptionsModel
from mamv2.models.app_deployment_options_model_ import AppDeploymentOptionsModel_
from mamv2.models.app_files_options_model import AppFilesOptionsModel
from mamv2.models.app_files_options_model_ import AppFilesOptionsModel_
from mamv2.models.app_patch_model import AppPatchModel
from mamv2.models.app_transform_model import AppTransformModel
from mamv2.models.app_un_install_process_model import AppUnInstallProcessModel
from mamv2.models.app_un_install_process_model_ import AppUnInstallProcessModel_
from mamv2.models.application_assignment_model import ApplicationAssignmentModel
from mamv2.models.application_branch_cache_statistics_model import ApplicationBranchCacheStatisticsModel
from mamv2.models.application_categories_model import ApplicationCategoriesModel
from mamv2.models.application_configuration_model import ApplicationConfigurationModel
from mamv2.models.application_configuration_v2_model import ApplicationConfigurationV2Model
from mamv2.models.application_deployment_profile_map_v1_model import ApplicationDeploymentProfileMapV1Model
from mamv2.models.application_supported_models_model import ApplicationSupportedModelsModel
from mamv2.models.applications_provision_profile_model import ApplicationsProvisionProfileModel
from mamv2.models.assignment_license_usage_v1_model import AssignmentLicenseUsageV1Model
from mamv2.models.base_exception_model import BaseExceptionModel
from mamv2.models.branch_cache_statistics_summary_model import BranchCacheStatisticsSummaryModel
from mamv2.models.cache_control_header_value import CacheControlHeaderValue
from mamv2.models.custom_script_api_model import CustomScriptApiModel
from mamv2.models.custom_script_api_model_ import CustomScriptApiModel_
from mamv2.models.deployment_by_criteria_api_model import DeploymentByCriteriaApiModel
from mamv2.models.deployment_by_custom_script_api_model import DeploymentByCustomScriptApiModel
from mamv2.models.deployment_by_custom_script_api_model_ import DeploymentByCustomScriptApiModel_
from mamv2.models.device_branch_cache_statistics_model import DeviceBranchCacheStatisticsModel
from mamv2.models.entity_id import EntityId
from mamv2.models.entity_tag_header_value import EntityTagHeaderValue
from mamv2.models.file_criteria_api_model import FileCriteriaApiModel
from mamv2.models.file_criteria_api_model_ import FileCriteriaApiModel_
from mamv2.models.how_to_install_api_model import HowToInstallApiModel
from mamv2.models.how_to_install_api_model_ import HowToInstallApiModel_
from mamv2.models.http_method import HttpMethod
from mamv2.models.i_action_result import IActionResult
from mamv2.models.i_request_query import IRequestQuery
from mamv2.models.i_tenant_context import ITenantContext
from mamv2.models.internal_app_model import InternalAppModel
from mamv2.models.licenses_summary_v2_model import LicensesSummaryV2Model
from mamv2.models.link import Link
from mamv2.models.mac_os_software_deployment_summary_model import MacOsSoftwareDeploymentSummaryModel
from mamv2.models.mac_os_software_deployment_summary_model_ import MacOsSoftwareDeploymentSummaryModel_
from mamv2.models.method_info import MethodInfo
from mamv2.models.msi_deployment_options_v1_model import MsiDeploymentOptionsV1Model
from mamv2.models.msi_deployment_parameter_model import MsiDeploymentParameterModel
from mamv2.models.msi_deployment_parameter_model_ import MsiDeploymentParameterModel_
from mamv2.models.name_value_header_value import NameValueHeaderValue
from mamv2.models.purchased_application_v2_model import PurchasedApplicationV2Model
from mamv2.models.range_header_value import RangeHeaderValue
from mamv2.models.range_item_header_value import RangeItemHeaderValue
from mamv2.models.registry_criteria_api_model import RegistryCriteriaApiModel
from mamv2.models.registry_criteria_api_model_ import RegistryCriteriaApiModel_
from mamv2.models.request_query import RequestQuery
from mamv2.models.stream import Stream
from mamv2.models.vpp_assignment_v2_model import VppAssignmentV2Model
from mamv2.models.vpp_deployment_parameters_v2_model import VppDeploymentParametersV2Model
from mamv2.models.when_to_call_install_complete_api_model import WhenToCallInstallCompleteApiModel
from mamv2.models.when_to_call_install_complete_api_model_ import WhenToCallInstallCompleteApiModel_
from mamv2.models.when_to_install_api_model import WhenToInstallApiModel
from mamv2.models.when_to_install_api_model_ import WhenToInstallApiModel_