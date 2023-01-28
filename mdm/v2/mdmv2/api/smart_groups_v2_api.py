# coding: utf-8

"""
    MDM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mdmv2.api_client import ApiClient


class SmartGroupsV2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def smart_groups_v2_partial_update_smart_group_async(self, uuid, smart_groups_operations, **kwargs):  # noqa: E501
        """New - Partially updates Smart Group criteria.  # noqa: E501

         Partially updates Smart Group criteria by adding/removing rules and/or values to rules like Organization groups, user groups, etc.                           ------------Example--------------    [    {op: \"add\", path: \"/smartGroupsOperationsV2/organizationGroups\", value: \"069DC0E2-D4E2-E611-8114-005056AF67FF, 069DC0E2-D4E2-E611-8114-005056AF67FF\"},    {op: \"remove\", path: \"/smartGroupsOperationsV2/users\", value: \"069DC0E2-D4E2-E611-8114-005056AF67FF, 069DC0E2-D4E2-E611-8114-005056AF67FF\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/devices\", value: \"069DC0E2-D4E2-E611-8114-005056AF67FF\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/tags\", value: \"123, 345\"},    {op: \"remove\", path: \"/smartGroupsOperationsV2/platforms\", value: \"WindowsMobile, Apple, BlackBerry, Android, Athena, Motorola, WindowsPhone, WindowsPc, AppleOsX, WindowsPhone8, WinRT, BlackBerry10, AppleTv, Qnx, ChromeBook, ChromeOS\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/managementTypes\", value: \"MdmEnrolled\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/enrollmentCategories\", value: \"DepEnrolled, AndroidEnterprise\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/cpuArchitectures\", value: \"049892B1-BCFE-447A-B34C-52D2BE897715, 1D88CEFE-8959-4E26-BD0C-355889B14378\"}  ]       -----------Platforms--------------    \"WindowsMobile, Apple, BlackBerry, Android, Athena, Motorola, WindowsPhone, WindowsPc, AppleOsX, WindowsPhone8, WinRT, BlackBerry10, AppleTv, Qnx, ChromeBook, ChromeOS\"  -----------Ownerships-------------         \"CorporateDedicated, CorporateShared, EmployeeOwned, AllOwnerships\"      ----------ManagementTypes-------      \"MdmEnrolled, ApplicationManaged, All\"      ----------EnrollmentCategories---      \"DepEnrolled, Supervised, UserApprovedMdmEnrolled, SharedIpad, EduShared, AndroidLegacy, AndroidEnterprise, AadEnrolled, All\"     --- Get all CPU Architectures API /processor-architectures  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.smart_groups_v2_partial_update_smart_group_async(uuid, smart_groups_operations, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Smart Group unique identifier(Required). (required)
        :param SmartGroupsOperationsV2ModelPatch smart_groups_operations: Model containing operation type, resource path and value. Supports add and remove operations.(Required). (required)
        :return: SmartGroupPatchResponseV2Model
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.smart_groups_v2_partial_update_smart_group_async_with_http_info(uuid, smart_groups_operations, **kwargs)  # noqa: E501
        else:
            (data) = self.smart_groups_v2_partial_update_smart_group_async_with_http_info(uuid, smart_groups_operations, **kwargs)  # noqa: E501
            return data

    def smart_groups_v2_partial_update_smart_group_async_with_http_info(self, uuid, smart_groups_operations, **kwargs):  # noqa: E501
        """New - Partially updates Smart Group criteria.  # noqa: E501

         Partially updates Smart Group criteria by adding/removing rules and/or values to rules like Organization groups, user groups, etc.                           ------------Example--------------    [    {op: \"add\", path: \"/smartGroupsOperationsV2/organizationGroups\", value: \"069DC0E2-D4E2-E611-8114-005056AF67FF, 069DC0E2-D4E2-E611-8114-005056AF67FF\"},    {op: \"remove\", path: \"/smartGroupsOperationsV2/users\", value: \"069DC0E2-D4E2-E611-8114-005056AF67FF, 069DC0E2-D4E2-E611-8114-005056AF67FF\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/devices\", value: \"069DC0E2-D4E2-E611-8114-005056AF67FF\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/tags\", value: \"123, 345\"},    {op: \"remove\", path: \"/smartGroupsOperationsV2/platforms\", value: \"WindowsMobile, Apple, BlackBerry, Android, Athena, Motorola, WindowsPhone, WindowsPc, AppleOsX, WindowsPhone8, WinRT, BlackBerry10, AppleTv, Qnx, ChromeBook, ChromeOS\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/managementTypes\", value: \"MdmEnrolled\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/enrollmentCategories\", value: \"DepEnrolled, AndroidEnterprise\"},    {op: \"add\", path: \"/smartGroupsOperationsV2/cpuArchitectures\", value: \"049892B1-BCFE-447A-B34C-52D2BE897715, 1D88CEFE-8959-4E26-BD0C-355889B14378\"}  ]       -----------Platforms--------------    \"WindowsMobile, Apple, BlackBerry, Android, Athena, Motorola, WindowsPhone, WindowsPc, AppleOsX, WindowsPhone8, WinRT, BlackBerry10, AppleTv, Qnx, ChromeBook, ChromeOS\"  -----------Ownerships-------------         \"CorporateDedicated, CorporateShared, EmployeeOwned, AllOwnerships\"      ----------ManagementTypes-------      \"MdmEnrolled, ApplicationManaged, All\"      ----------EnrollmentCategories---      \"DepEnrolled, Supervised, UserApprovedMdmEnrolled, SharedIpad, EduShared, AndroidLegacy, AndroidEnterprise, AadEnrolled, All\"     --- Get all CPU Architectures API /processor-architectures  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.smart_groups_v2_partial_update_smart_group_async_with_http_info(uuid, smart_groups_operations, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Smart Group unique identifier(Required). (required)
        :param SmartGroupsOperationsV2ModelPatch smart_groups_operations: Model containing operation type, resource path and value. Supports add and remove operations.(Required). (required)
        :return: SmartGroupPatchResponseV2Model
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'smart_groups_operations']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method smart_groups_v2_partial_update_smart_group_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in params or
                                                       params['uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uuid` when calling `smart_groups_v2_partial_update_smart_group_async`")  # noqa: E501
        # verify the required parameter 'smart_groups_operations' is set
        if self.api_client.client_side_validation and ('smart_groups_operations' not in params or
                                                       params['smart_groups_operations'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `smart_groups_operations` when calling `smart_groups_v2_partial_update_smart_group_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'smart_groups_operations' in params:
            body_params = params['smart_groups_operations']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=2'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/smartgroups/{uuid}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SmartGroupPatchResponseV2Model',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
