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


class AwContentV2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def aw_content_v2_bulk_delete(self, aw_content_ids, **kwargs):  # noqa: E501
        """New - Queues the deletion of multiple files  # noqa: E501

        Queues the Deletion of multiple managed content files selected.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_content_v2_bulk_delete(aw_content_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] aw_content_ids: List of GUIDs of the managed content to be dleted(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aw_content_v2_bulk_delete_with_http_info(aw_content_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.aw_content_v2_bulk_delete_with_http_info(aw_content_ids, **kwargs)  # noqa: E501
            return data

    def aw_content_v2_bulk_delete_with_http_info(self, aw_content_ids, **kwargs):  # noqa: E501
        """New - Queues the deletion of multiple files  # noqa: E501

        Queues the Deletion of multiple managed content files selected.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_content_v2_bulk_delete_with_http_info(aw_content_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] aw_content_ids: List of GUIDs of the managed content to be dleted(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aw_content_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aw_content_v2_bulk_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aw_content_ids' is set
        if self.api_client.client_side_validation and ('aw_content_ids' not in params or
                                                       params['aw_content_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aw_content_ids` when calling `aw_content_v2_bulk_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'aw_content_ids' in params:
            body_params = params['aw_content_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml -application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/V2/awcontents/BulkDelete', 'POST',
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

    def aw_content_v2_get_content_status_counts_async(self, content_uuid, **kwargs):  # noqa: E501
        """New - Get content status counts.  # noqa: E501

        It returns the count of content status like installed, uninstalled, assigned, viewed, and acknowledged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_content_v2_get_content_status_counts_async(content_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_uuid: Content Uuid.(Required) (required)
        :return: ContentStatusModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aw_content_v2_get_content_status_counts_async_with_http_info(content_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.aw_content_v2_get_content_status_counts_async_with_http_info(content_uuid, **kwargs)  # noqa: E501
            return data

    def aw_content_v2_get_content_status_counts_async_with_http_info(self, content_uuid, **kwargs):  # noqa: E501
        """New - Get content status counts.  # noqa: E501

        It returns the count of content status like installed, uninstalled, assigned, viewed, and acknowledged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_content_v2_get_content_status_counts_async_with_http_info(content_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_uuid: Content Uuid.(Required) (required)
        :return: ContentStatusModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aw_content_v2_get_content_status_counts_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_uuid' is set
        if self.api_client.client_side_validation and ('content_uuid' not in params or
                                                       params['content_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `content_uuid` when calling `aw_content_v2_get_content_status_counts_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'content_uuid' in params:
            path_params['contentUuid'] = params['content_uuid']  # noqa: E501

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
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/V2/awcontents/status/{contentUuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContentStatusModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)