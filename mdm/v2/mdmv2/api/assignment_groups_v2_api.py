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


class AssignmentGroupsV2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def assignment_groups_v2_get_assignment_groups_by_search_context_async(self, organization_group_uuid, assignment_type, **kwargs):  # noqa: E501
        """New - Returns a list of Assignment Groups matching the search criteria  # noqa: E501

        Get List of Assignment Groups based on the Organization Group, Search Text, AssignmentType. Search text should not be more than 255 characters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.assignment_groups_v2_get_assignment_groups_by_search_context_async(organization_group_uuid, assignment_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Unique Identifier for the Organization Group(Required). (required)
        :param int assignment_type: Type of Assignment Group to search               All types of Assignment Groups (Smart Group, User Group, Organization Group)                SmartGroups                UserGroups                OrganizationGroups (Required) (required)
        :param str name: Name of the Assignment Group by which result will be filtered (Optional). When not passed, all Assignment Groups present in that organization will be returned.
        :param str order_by: The column used for sorting.
        :param object sort_order: The sort order ascending/decending. Default value is ASC.
        :param int page: The page number for the paged result.
        :param int page_size: The number of records per page.
        :return: list[AssignmentGroupsPagedResultsModelV1]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.assignment_groups_v2_get_assignment_groups_by_search_context_async_with_http_info(organization_group_uuid, assignment_type, **kwargs)  # noqa: E501
        else:
            (data) = self.assignment_groups_v2_get_assignment_groups_by_search_context_async_with_http_info(organization_group_uuid, assignment_type, **kwargs)  # noqa: E501
            return data

    def assignment_groups_v2_get_assignment_groups_by_search_context_async_with_http_info(self, organization_group_uuid, assignment_type, **kwargs):  # noqa: E501
        """New - Returns a list of Assignment Groups matching the search criteria  # noqa: E501

        Get List of Assignment Groups based on the Organization Group, Search Text, AssignmentType. Search text should not be more than 255 characters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.assignment_groups_v2_get_assignment_groups_by_search_context_async_with_http_info(organization_group_uuid, assignment_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Unique Identifier for the Organization Group(Required). (required)
        :param int assignment_type: Type of Assignment Group to search               All types of Assignment Groups (Smart Group, User Group, Organization Group)                SmartGroups                UserGroups                OrganizationGroups (Required) (required)
        :param str name: Name of the Assignment Group by which result will be filtered (Optional). When not passed, all Assignment Groups present in that organization will be returned.
        :param str order_by: The column used for sorting.
        :param object sort_order: The sort order ascending/decending. Default value is ASC.
        :param int page: The page number for the paged result.
        :param int page_size: The number of records per page.
        :return: list[AssignmentGroupsPagedResultsModelV1]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_group_uuid', 'assignment_type', 'name', 'order_by', 'sort_order', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method assignment_groups_v2_get_assignment_groups_by_search_context_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_group_uuid' is set
        if self.api_client.client_side_validation and ('organization_group_uuid' not in params or
                                                       params['organization_group_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `organization_group_uuid` when calling `assignment_groups_v2_get_assignment_groups_by_search_context_async`")  # noqa: E501
        # verify the required parameter 'assignment_type' is set
        if self.api_client.client_side_validation and ('assignment_type' not in params or
                                                       params['assignment_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `assignment_type` when calling `assignment_groups_v2_get_assignment_groups_by_search_context_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_group_uuid' in params:
            path_params['organizationGroupUuid'] = params['organization_group_uuid']  # noqa: E501

        query_params = []
        if 'assignment_type' in params:
            query_params.append(('assignmentType', params['assignment_type']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort_order', params['sort_order']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=2'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{organizationGroupUuid}/assignmentgroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AssignmentGroupsPagedResultsModelV1]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
