# coding: utf-8

"""
    System API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from systemv1.api_client import ApiClient


class OperationsV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def operations_v1_get_operation_status(self, operation_uuid, **kwargs):  # noqa: E501
        """New - Retrieves status for an operation  # noqa: E501

        Given an operation identifier this API retrieves and returns its latest recorded status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.operations_v1_get_operation_status(operation_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str operation_uuid: Identifier of the operation whose status to be obtained (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.operations_v1_get_operation_status_with_http_info(operation_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.operations_v1_get_operation_status_with_http_info(operation_uuid, **kwargs)  # noqa: E501
            return data

    def operations_v1_get_operation_status_with_http_info(self, operation_uuid, **kwargs):  # noqa: E501
        """New - Retrieves status for an operation  # noqa: E501

        Given an operation identifier this API retrieves and returns its latest recorded status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.operations_v1_get_operation_status_with_http_info(operation_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str operation_uuid: Identifier of the operation whose status to be obtained (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['operation_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method operations_v1_get_operation_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'operation_uuid' is set
        if self.api_client.client_side_validation and ('operation_uuid' not in params or
                                                       params['operation_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `operation_uuid` when calling `operations_v1_get_operation_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'operation_uuid' in params:
            path_params['operation-uuid'] = params['operation_uuid']  # noqa: E501

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
            '/operations/{operation-uuid}', 'GET',
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