# coding: utf-8

"""
    MCM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mcmv1.api_client import ApiClient


class ContentRepositoryV2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def content_repository_v2_content_repository_bulk_delete_async(self, content_repository_uuids, **kwargs):  # noqa: E501
        """New - Bulk delete content repositories.  # noqa: E501

        Deletes the content repository for multiple content repository uuids.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_repository_v2_content_repository_bulk_delete_async(content_repository_uuids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] content_repository_uuids: Content repository uuids to be deleted.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_repository_v2_content_repository_bulk_delete_async_with_http_info(content_repository_uuids, **kwargs)  # noqa: E501
        else:
            (data) = self.content_repository_v2_content_repository_bulk_delete_async_with_http_info(content_repository_uuids, **kwargs)  # noqa: E501
            return data

    def content_repository_v2_content_repository_bulk_delete_async_with_http_info(self, content_repository_uuids, **kwargs):  # noqa: E501
        """New - Bulk delete content repositories.  # noqa: E501

        Deletes the content repository for multiple content repository uuids.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_repository_v2_content_repository_bulk_delete_async_with_http_info(content_repository_uuids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] content_repository_uuids: Content repository uuids to be deleted.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_repository_uuids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method content_repository_v2_content_repository_bulk_delete_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_repository_uuids' is set
        if self.api_client.client_side_validation and ('content_repository_uuids' not in params or
                                                       params['content_repository_uuids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `content_repository_uuids` when calling `content_repository_v2_content_repository_bulk_delete_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'content_repository_uuids' in params:
            body_params = params['content_repository_uuids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/V2/contents/repositories/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def content_repository_v2_content_repository_delete_async(self, content_repository_uuid, **kwargs):  # noqa: E501
        """New - Deletes a content repository.  # noqa: E501

        Deletes the content repository for a content repository uuid.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_repository_v2_content_repository_delete_async(content_repository_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_repository_uuid: Uuid of the content repository to be deleted(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_repository_v2_content_repository_delete_async_with_http_info(content_repository_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.content_repository_v2_content_repository_delete_async_with_http_info(content_repository_uuid, **kwargs)  # noqa: E501
            return data

    def content_repository_v2_content_repository_delete_async_with_http_info(self, content_repository_uuid, **kwargs):  # noqa: E501
        """New - Deletes a content repository.  # noqa: E501

        Deletes the content repository for a content repository uuid.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_repository_v2_content_repository_delete_async_with_http_info(content_repository_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_repository_uuid: Uuid of the content repository to be deleted(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_repository_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method content_repository_v2_content_repository_delete_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_repository_uuid' is set
        if self.api_client.client_side_validation and ('content_repository_uuid' not in params or
                                                       params['content_repository_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `content_repository_uuid` when calling `content_repository_v2_content_repository_delete_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'content_repository_uuid' in params:
            path_params['contentRepositoryUuid'] = params['content_repository_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/V2/contents/repositories/{contentRepositoryUuid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def content_repository_v2_create_content_repository_async(self, content_repository_v2_model, **kwargs):  # noqa: E501
        """New - Creates an Admin Content Repository.  # noqa: E501

        It creates an admin content repository and has options for adding assignment, deployment, and security.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_repository_v2_create_content_repository_async(content_repository_v2_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContentRepositoryV2Model content_repository_v2_model: Content gateway configuration details to be created.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_repository_v2_create_content_repository_async_with_http_info(content_repository_v2_model, **kwargs)  # noqa: E501
        else:
            (data) = self.content_repository_v2_create_content_repository_async_with_http_info(content_repository_v2_model, **kwargs)  # noqa: E501
            return data

    def content_repository_v2_create_content_repository_async_with_http_info(self, content_repository_v2_model, **kwargs):  # noqa: E501
        """New - Creates an Admin Content Repository.  # noqa: E501

        It creates an admin content repository and has options for adding assignment, deployment, and security.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_repository_v2_create_content_repository_async_with_http_info(content_repository_v2_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContentRepositoryV2Model content_repository_v2_model: Content gateway configuration details to be created.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_repository_v2_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method content_repository_v2_create_content_repository_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_repository_v2_model' is set
        if self.api_client.client_side_validation and ('content_repository_v2_model' not in params or
                                                       params['content_repository_v2_model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `content_repository_v2_model` when calling `content_repository_v2_create_content_repository_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'content_repository_v2_model' in params:
            body_params = params['content_repository_v2_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/V2/contents/repositories', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def content_repository_v2_personal_content_repository_bulk_delete_async(self, organization_group_uuid, **kwargs):  # noqa: E501
        """New - Deletes personal content related metadata.  # noqa: E501

        Deletes all personal content repository for the provided Organization Group and its children Organization Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_repository_v2_personal_content_repository_bulk_delete_async(organization_group_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Organization Group Uuid.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_repository_v2_personal_content_repository_bulk_delete_async_with_http_info(organization_group_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.content_repository_v2_personal_content_repository_bulk_delete_async_with_http_info(organization_group_uuid, **kwargs)  # noqa: E501
            return data

    def content_repository_v2_personal_content_repository_bulk_delete_async_with_http_info(self, organization_group_uuid, **kwargs):  # noqa: E501
        """New - Deletes personal content related metadata.  # noqa: E501

        Deletes all personal content repository for the provided Organization Group and its children Organization Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_repository_v2_personal_content_repository_bulk_delete_async_with_http_info(organization_group_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Organization Group Uuid.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_group_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method content_repository_v2_personal_content_repository_bulk_delete_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_group_uuid' is set
        if self.api_client.client_side_validation and ('organization_group_uuid' not in params or
                                                       params['organization_group_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `organization_group_uuid` when calling `content_repository_v2_personal_content_repository_bulk_delete_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_group_uuid' in params:
            path_params['organizationGroupUuid'] = params['organization_group_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/V2/contents/groups/{organizationGroupUuid}/personal-content', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
