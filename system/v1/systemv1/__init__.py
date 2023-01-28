# coding: utf-8

# flake8: noqa

"""
    System API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from systemv1.api.admin_identity_v1_api import AdminIdentityV1Api
from systemv1.api.admin_login_history_v1_api import AdminLoginHistoryV1Api
from systemv1.api.admins_v1_api import AdminsV1Api
from systemv1.api.advanced_ldap_sync_job_v1_api import AdvancedLdapSyncJobV1Api
from systemv1.api.android_work_api import AndroidWorkApi
from systemv1.api.apns_api import ApnsApi
from systemv1.api.app_content_api import AppContentApi
from systemv1.api.cloud_connector_api import CloudConnectorApi
from systemv1.api.cultures_v1_api import CulturesV1Api
from systemv1.api.custom_attributes_api import CustomAttributesApi
from systemv1.api.custom_gateway_settings_v1_api import CustomGatewaySettingsV1Api
from systemv1.api.custom_reports_v1_api import CustomReportsV1Api
from systemv1.api.device_registration_v1_api import DeviceRegistrationV1Api
from systemv1.api.device_wipes_api import DeviceWipesApi
from systemv1.api.enable_dropship_provisioning_v1_api import EnableDropshipProvisioningV1Api
from systemv1.api.enrollment_custom_attributes_api import EnrollmentCustomAttributesApi
from systemv1.api.enrollment_customization_settings_v1_api import EnrollmentCustomizationSettingsV1Api
from systemv1.api.event_notifications_v1_api import EventNotificationsV1Api
from systemv1.api.event_notifications_v2_api import EventNotificationsV2Api
from systemv1.api.exported_reports_v1_api import ExportedReportsV1Api
from systemv1.api.express_license_api import ExpressLicenseApi
from systemv1.api.hub_v1_api import HubV1Api
from systemv1.api.info_api import InfoApi
from systemv1.api.intelligence_eula_v1_api import IntelligenceEulaV1Api
from systemv1.api.lookup_fields_v1_api import LookupFieldsV1Api
from systemv1.api.notifications_api import NotificationsApi
from systemv1.api.operations_v1_api import OperationsV1Api
from systemv1.api.organization_group_custom_attributes_api import OrganizationGroupCustomAttributesApi
from systemv1.api.organization_groups_api import OrganizationGroupsApi
from systemv1.api.product_licenses_api import ProductLicensesApi
from systemv1.api.product_monitor_v1_api import ProductMonitorV1Api
from systemv1.api.ssl_pinning_api import SSLPinningApi
from systemv1.api.tags_api import TagsApi
from systemv1.api.time_zone_v1_api import TimeZoneV1Api
from systemv1.api.user_api import UserApi
from systemv1.api.user_groups_api import UserGroupsApi
from systemv1.api.users_batches_v1_api import UsersBatchesV1Api

# import ApiClient
from systemv1.api_client import ApiClient
from systemv1.configuration import Configuration
# import models into sdk package
from systemv1.models.action3 import Action3
from systemv1.models.admin_login_history_record import AdminLoginHistoryRecord
from systemv1.models.admin_login_history_report_v1_model import AdminLoginHistoryReportV1Model
from systemv1.models.admin_login_history_response import AdminLoginHistoryResponse
from systemv1.models.admin_login_history_search_criteria import AdminLoginHistorySearchCriteria
from systemv1.models.admin_search_result import AdminSearchResult
from systemv1.models.admin_user import AdminUser
from systemv1.models.admin_user_identity_model_v1 import AdminUserIdentityModelV1
from systemv1.models.admin_user_ import AdminUser_
from systemv1.models.advanced_ladp_sync_job_approval_request_model import AdvancedLadpSyncJobApprovalRequestModel
from systemv1.models.advanced_ladp_sync_job_request_model import AdvancedLadpSyncJobRequestModel
from systemv1.models.advanced_ldap_sync_enrollment_user_model import AdvancedLdapSyncEnrollmentUserModel
from systemv1.models.advanced_ldap_sync_job_details_model import AdvancedLdapSyncJobDetailsModel
from systemv1.models.advanced_ldap_sync_job_details_response_model import AdvancedLdapSyncJobDetailsResponseModel
from systemv1.models.advanced_ldap_sync_job_progress_response_model import AdvancedLdapSyncJobProgressResponseModel
from systemv1.models.advanced_ldap_sync_job_response_model import AdvancedLdapSyncJobResponseModel
from systemv1.models.android_work_setup_model import AndroidWorkSetupModel
from systemv1.models.apns_configuration_model import ApnsConfigurationModel
from systemv1.models.apns_setup_model import ApnsSetupModel
from systemv1.models.apns_setup_model_ import ApnsSetupModel_
from systemv1.models.app_content_storage_entity import AppContentStorageEntity
from systemv1.models.attribute_value import AttributeValue
from systemv1.models.base_exception_model import BaseExceptionModel
from systemv1.models.base_model import BaseModel
from systemv1.models.bulk_input import BulkInput
from systemv1.models.bulk_response import BulkResponse
from systemv1.models.bulk_values import BulkValues
from systemv1.models.bulk_values_ import BulkValues_
from systemv1.models.cache_control_header_value import CacheControlHeaderValue
from systemv1.models.certificate import Certificate
from systemv1.models.certificate_pinning_cert_entity import CertificatePinningCertEntity
from systemv1.models.certificate_pinning_host_entity import CertificatePinningHostEntity
from systemv1.models.certificate_ import Certificate_
from systemv1.models.configurations_about_model import ConfigurationsAboutModel
from systemv1.models.connection_status_v1_model import ConnectionStatusV1Model
from systemv1.models.control_plane_version_details import ControlPlaneVersionDetails
from systemv1.models.cultures_response_v1_model import CulturesResponseV1Model
from systemv1.models.cultures_v1_model import CulturesV1Model
from systemv1.models.custom_attribute import CustomAttribute
from systemv1.models.custom_attribute_list_model import CustomAttributeListModel
from systemv1.models.custom_attribute_model import CustomAttributeModel
from systemv1.models.custom_attribute_model_ import CustomAttributeModel_
from systemv1.models.custom_attribute_name_value_application_model import CustomAttributeNameValueApplicationModel
from systemv1.models.custom_attribute_name_value_application_model_ import CustomAttributeNameValueApplicationModel_
from systemv1.models.custom_attribute_name_value_model import CustomAttributeNameValueModel
from systemv1.models.custom_attribute_name_value_model_ import CustomAttributeNameValueModel_
from systemv1.models.custom_attribute_resource import CustomAttributeResource
from systemv1.models.custom_attribute_resource_ import CustomAttributeResource_
from systemv1.models.custom_attribute_search_result import CustomAttributeSearchResult
from systemv1.models.custom_attribute_value import CustomAttributeValue
from systemv1.models.custom_attribute_value_model import CustomAttributeValueModel
from systemv1.models.custom_attribute_value_model_ import CustomAttributeValueModel_
from systemv1.models.custom_gateway_setting_key_v1 import CustomGatewaySettingKeyV1
from systemv1.models.custom_gateway_setting_v1 import CustomGatewaySettingV1
from systemv1.models.custom_report_token_v1_model import CustomReportTokenV1Model
from systemv1.models.device_attributes_model import DeviceAttributesModel
from systemv1.models.device_count_by_enrollment_status_model import DeviceCountByEnrollmentStatusModel
from systemv1.models.device_count_by_enrollment_status_model_ import DeviceCountByEnrollmentStatusModel_
from systemv1.models.device_count_per_location_group_search_result_model import DeviceCountPerLocationGroupSearchResultModel
from systemv1.models.device_count_per_status_v1_model import DeviceCountPerStatusV1Model
from systemv1.models.device_events_model import DeviceEventsModel
from systemv1.models.device_sample_rates import DeviceSampleRates
from systemv1.models.device_wipe_model import DeviceWipeModel
from systemv1.models.device_wipe_request_v1 import DeviceWipeRequestV1
from systemv1.models.device_wipe_response_model import DeviceWipeResponseModel
from systemv1.models.dropship_provisioning_settings_details_request_v1_model import DropshipProvisioningSettingsDetailsRequestV1Model
from systemv1.models.dropship_provisioning_settings_details_response_v1_model import DropshipProvisioningSettingsDetailsResponseV1Model
from systemv1.models.enrolled_device_details import EnrolledDeviceDetails
from systemv1.models.enrolled_devices import EnrolledDevices
from systemv1.models.enrollment_customization_settings_response_v1_model import EnrollmentCustomizationSettingsResponseV1Model
from systemv1.models.enrollment_token_details_model import EnrollmentTokenDetailsModel
from systemv1.models.enrollment_tokens_model import EnrollmentTokensModel
from systemv1.models.enrollment_user_detail import EnrollmentUserDetail
from systemv1.models.entity_id import EntityId
from systemv1.models.entity_id_model import EntityIdModel
from systemv1.models.entity_id_ import EntityId_
from systemv1.models.entity_reference import EntityReference
from systemv1.models.entity_reference_ import EntityReference_
from systemv1.models.entity_tag_header_value import EntityTagHeaderValue
from systemv1.models.event_notification_model import EventNotificationModel
from systemv1.models.event_notifications_paged_search_result_model import EventNotificationsPagedSearchResultModel
from systemv1.models.event_notificatons_subscriptions_result_model import EventNotificatonsSubscriptionsResultModel
from systemv1.models.event_subscription_model import EventSubscriptionModel
from systemv1.models.export_status_model_v1 import ExportStatusModelV1
from systemv1.models.export_v1_model import ExportV1Model
from systemv1.models.fault import Fault
from systemv1.models.faults import Faults
from systemv1.models.faults_ import Faults_
from systemv1.models.get_custom_attribute_result import GetCustomAttributeResult
from systemv1.models.http_method import HttpMethod
from systemv1.models.hub_configuration_v1_model import HubConfigurationV1Model
from systemv1.models.hypermedia_model import HypermediaModel
from systemv1.models.hypermedia_model_ import HypermediaModel_
from systemv1.models.hypermedia_v2_model import HypermediaV2Model
from systemv1.models.i_action_result import IActionResult
from systemv1.models.i_request_query import IRequestQuery
from systemv1.models.i_tenant_context import ITenantContext
from systemv1.models.intelligence_eula_model_v1 import IntelligenceEulaModelV1
from systemv1.models.license_model import LicenseModel
from systemv1.models.link import Link
from systemv1.models.location_group import LocationGroup
from systemv1.models.location_group_device_count_summary_model import LocationGroupDeviceCountSummaryModel
from systemv1.models.location_group_device_count_summary_model_ import LocationGroupDeviceCountSummaryModel_
from systemv1.models.location_group_search_result import LocationGroupSearchResult
from systemv1.models.location_group_ import LocationGroup_
from systemv1.models.lookup_fields_v1_entity import LookupFieldsV1Entity
from systemv1.models.member_of import MemberOf
from systemv1.models.method_info import MethodInfo
from systemv1.models.name_value_header_value import NameValueHeaderValue
from systemv1.models.notification_count_model import NotificationCountModel
from systemv1.models.og_custom_attribute import OgCustomAttribute
from systemv1.models.operation_status_model import OperationStatusModel
from systemv1.models.pinned_certificate_model import PinnedCertificateModel
from systemv1.models.pinned_certificate_query_model import PinnedCertificateQueryModel
from systemv1.models.pinned_host_model import PinnedHostModel
from systemv1.models.pinned_host_response_model import PinnedHostResponseModel
from systemv1.models.preview_advanced_ldap_sync_job_details_model import PreviewAdvancedLdapSyncJobDetailsModel
from systemv1.models.preview_advanced_ldap_sync_job_response_model import PreviewAdvancedLdapSyncJobResponseModel
from systemv1.models.product_deployment_details_v1_model import ProductDeploymentDetailsV1Model
from systemv1.models.product_detail_v1_model import ProductDetailV1Model
from systemv1.models.product_historical_data_v1_model import ProductHistoricalDataV1Model
from systemv1.models.product_license_response_v1_model import ProductLicenseResponseV1Model
from systemv1.models.product_license_v1_model import ProductLicenseV1Model
from systemv1.models.product_status_v1_model import ProductStatusV1Model
from systemv1.models.range_header_value import RangeHeaderValue
from systemv1.models.range_item_header_value import RangeItemHeaderValue
from systemv1.models.read_notification_model import ReadNotificationModel
from systemv1.models.register_device_details_model import RegisterDeviceDetailsModel
from systemv1.models.registered_device_details import RegisteredDeviceDetails
from systemv1.models.registered_devices import RegisteredDevices
from systemv1.models.report_parameters_v1 import ReportParametersV1
from systemv1.models.reports_model import ReportsModel
from systemv1.models.request_query import RequestQuery
from systemv1.models.resource_reference import ResourceReference
from systemv1.models.role_model import RoleModel
from systemv1.models.role_model_ import RoleModel_
from systemv1.models.smime_certificate import SMIMECertificate
from systemv1.models.service_document import ServiceDocument
from systemv1.models.service_document_resources import ServiceDocumentResources
from systemv1.models.stream import Stream
from systemv1.models.sub_organization_group_v1_model import SubOrganizationGroupV1Model
from systemv1.models.tag import Tag
from systemv1.models.tag_model import TagModel
from systemv1.models.tag_model_ import TagModel_
from systemv1.models.tag_search_result import TagSearchResult
from systemv1.models.time_zone_response_v1_model import TimeZoneResponseV1Model
from systemv1.models.time_zone_v1_model import TimeZoneV1Model
from systemv1.models.token_service_idp_request_model_v1 import TokenServiceIdpRequestModelV1
from systemv1.models.user import User
from systemv1.models.user_batch_details_report_v1_model import UserBatchDetailsReportV1Model
from systemv1.models.user_group import UserGroup
from systemv1.models.user_group_model import UserGroupModel
from systemv1.models.user_group_search_detail import UserGroupSearchDetail
from systemv1.models.user_group_search_result_model import UserGroupSearchResultModel
from systemv1.models.user_group_users import UserGroupUsers
from systemv1.models.user_groups import UserGroups
from systemv1.models.user_model import UserModel
from systemv1.models.user_search_result import UserSearchResult
from systemv1.models.user_ import User_
from systemv1.models.users_batch_details_v1_model import UsersBatchDetailsV1Model
from systemv1.models.users_batch_details_v1_result_model import UsersBatchDetailsV1ResultModel
from systemv1.models.users_batches_report_v1_model import UsersBatchesReportV1Model
from systemv1.models.users_batches_v1_model import UsersBatchesV1Model
from systemv1.models.users_batches_v1_result_model import UsersBatchesV1ResultModel
from systemv1.models.wipe_lock_state_model import WipeLockStateModel
