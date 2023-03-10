# coding: utf-8

"""
    MDM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mdmv1.api_client import ApiClient


class ResourcesV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resources_v1_query_resources_async(self, resources, **kwargs):  # noqa: E501
        """New - Retrieves the details about the resources  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_v1_query_resources_async(resources, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ResourceRequestV1Model] resources: The resources to retrieve details about.(Required) (required)
        :return: list[ResourceResponseV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resources_v1_query_resources_async_with_http_info(resources, **kwargs)  # noqa: E501
        else:
            (data) = self.resources_v1_query_resources_async_with_http_info(resources, **kwargs)  # noqa: E501
            return data

    def resources_v1_query_resources_async_with_http_info(self, resources, **kwargs):  # noqa: E501
        """New - Retrieves the details about the resources  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_v1_query_resources_async_with_http_info(resources, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ResourceRequestV1Model] resources: The resources to retrieve details about.(Required) (required)
        :return: list[ResourceResponseV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['resources']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resources_v1_query_resources_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resources' is set
        if self.api_client.client_side_validation and ('resources' not in params or
                                                       params['resources'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `resources` when calling `resources_v1_query_resources_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'resources' in params:
            body_params = params['resources']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/resources/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ResourceResponseV1Model]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
