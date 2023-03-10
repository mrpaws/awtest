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


class ContentGatewayV4Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async(self, content_gateway_configuration_uuid, password, **kwargs):  # noqa: E501
        """New - Gets the content gateway configurations and the certificate details with custom settings.  # noqa: E501

        It returns content gateway configurations along with the custom settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async(content_gateway_configuration_uuid, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_gateway_configuration_uuid: Content gateway configuration id for which content gateway configurations are needed.(Required). (required)
        :param EncryptionModel password: A JSON object containing certificate password.(Required). (required)
        :return: list[ContentGatewayCustomSettingsV3]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async_with_http_info(content_gateway_configuration_uuid, password, **kwargs)  # noqa: E501
        else:
            (data) = self.content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async_with_http_info(content_gateway_configuration_uuid, password, **kwargs)  # noqa: E501
            return data

    def content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async_with_http_info(self, content_gateway_configuration_uuid, password, **kwargs):  # noqa: E501
        """New - Gets the content gateway configurations and the certificate details with custom settings.  # noqa: E501

        It returns content gateway configurations along with the custom settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async_with_http_info(content_gateway_configuration_uuid, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_gateway_configuration_uuid: Content gateway configuration id for which content gateway configurations are needed.(Required). (required)
        :param EncryptionModel password: A JSON object containing certificate password.(Required). (required)
        :return: list[ContentGatewayCustomSettingsV3]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_gateway_configuration_uuid', 'password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_gateway_configuration_uuid' is set
        if self.api_client.client_side_validation and ('content_gateway_configuration_uuid' not in params or
                                                       params['content_gateway_configuration_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `content_gateway_configuration_uuid` when calling `content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async`")  # noqa: E501
        # verify the required parameter 'password' is set
        if self.api_client.client_side_validation and ('password' not in params or
                                                       params['password'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `password` when calling `content_gateway_v4_get_content_gateway_configuration_custom_settings_by_id_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'content_gateway_configuration_uuid' in params:
            path_params['contentGatewayConfigurationUuid'] = params['content_gateway_configuration_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'password' in params:
            body_params = params['password']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/V4/groups/content-gateway/custom-settings/{contentGatewayConfigurationUuid}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ContentGatewayCustomSettingsV3]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
