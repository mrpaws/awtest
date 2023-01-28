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


class HubV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def hub_v1_configure_hub_services_url(self, hub_configuration_model, **kwargs):  # noqa: E501
        """New - Updates Hub Services configuration URL at given organization group.  # noqa: E501

        Updates Hub Services configuration URL at the given organization group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hub_v1_configure_hub_services_url(hub_configuration_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HubConfigurationV1Model hub_configuration_model: Model containing Hub Services configurations.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.hub_v1_configure_hub_services_url_with_http_info(hub_configuration_model, **kwargs)  # noqa: E501
        else:
            (data) = self.hub_v1_configure_hub_services_url_with_http_info(hub_configuration_model, **kwargs)  # noqa: E501
            return data

    def hub_v1_configure_hub_services_url_with_http_info(self, hub_configuration_model, **kwargs):  # noqa: E501
        """New - Updates Hub Services configuration URL at given organization group.  # noqa: E501

        Updates Hub Services configuration URL at the given organization group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hub_v1_configure_hub_services_url_with_http_info(hub_configuration_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HubConfigurationV1Model hub_configuration_model: Model containing Hub Services configurations.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hub_configuration_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hub_v1_configure_hub_services_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hub_configuration_model' is set
        if self.api_client.client_side_validation and ('hub_configuration_model' not in params or
                                                       params['hub_configuration_model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `hub_configuration_model` when calling `hub_v1_configure_hub_services_url`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hub_configuration_model' in params:
            body_params = params['hub_configuration_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/hubconfig/hubservicesurl', 'POST',
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
