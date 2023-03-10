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


class TunnelStandaloneClientV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def tunnel_standalone_client_v1_create_one_time_token_async(self, uuid, tunnel_config_uuid, bundle_id, profile_uuid, issuer, **kwargs):  # noqa: E501
        """New - Generates one time token to allow device to obtain authentication certificate  # noqa: E501

        Generates one time token that is required for the device to make seperate request to the certificate delivery endpoint to obtain authentication certificate using SCEP  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tunnel_standalone_client_v1_create_one_time_token_async(uuid, tunnel_config_uuid, bundle_id, profile_uuid, issuer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Unique identifier (GUID) of the device(Required). (required)
        :param str tunnel_config_uuid: Unique identifier (GUID) of the device(Required). (required)
        :param str bundle_id: Application Identifier (i.e com.apple.mobilesafari)(Required). (required)
        :param str profile_uuid: Unique identifier (GUID) of the profile.(Required). (required)
        :param str issuer: Certificate issuer - uniquely identifies authority and template for the certificate(Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tunnel_standalone_client_v1_create_one_time_token_async_with_http_info(uuid, tunnel_config_uuid, bundle_id, profile_uuid, issuer, **kwargs)  # noqa: E501
        else:
            (data) = self.tunnel_standalone_client_v1_create_one_time_token_async_with_http_info(uuid, tunnel_config_uuid, bundle_id, profile_uuid, issuer, **kwargs)  # noqa: E501
            return data

    def tunnel_standalone_client_v1_create_one_time_token_async_with_http_info(self, uuid, tunnel_config_uuid, bundle_id, profile_uuid, issuer, **kwargs):  # noqa: E501
        """New - Generates one time token to allow device to obtain authentication certificate  # noqa: E501

        Generates one time token that is required for the device to make seperate request to the certificate delivery endpoint to obtain authentication certificate using SCEP  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tunnel_standalone_client_v1_create_one_time_token_async_with_http_info(uuid, tunnel_config_uuid, bundle_id, profile_uuid, issuer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Unique identifier (GUID) of the device(Required). (required)
        :param str tunnel_config_uuid: Unique identifier (GUID) of the device(Required). (required)
        :param str bundle_id: Application Identifier (i.e com.apple.mobilesafari)(Required). (required)
        :param str profile_uuid: Unique identifier (GUID) of the profile.(Required). (required)
        :param str issuer: Certificate issuer - uniquely identifies authority and template for the certificate(Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'tunnel_config_uuid', 'bundle_id', 'profile_uuid', 'issuer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tunnel_standalone_client_v1_create_one_time_token_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in params or
                                                       params['uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uuid` when calling `tunnel_standalone_client_v1_create_one_time_token_async`")  # noqa: E501
        # verify the required parameter 'tunnel_config_uuid' is set
        if self.api_client.client_side_validation and ('tunnel_config_uuid' not in params or
                                                       params['tunnel_config_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tunnel_config_uuid` when calling `tunnel_standalone_client_v1_create_one_time_token_async`")  # noqa: E501
        # verify the required parameter 'bundle_id' is set
        if self.api_client.client_side_validation and ('bundle_id' not in params or
                                                       params['bundle_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bundle_id` when calling `tunnel_standalone_client_v1_create_one_time_token_async`")  # noqa: E501
        # verify the required parameter 'profile_uuid' is set
        if self.api_client.client_side_validation and ('profile_uuid' not in params or
                                                       params['profile_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `profile_uuid` when calling `tunnel_standalone_client_v1_create_one_time_token_async`")  # noqa: E501
        # verify the required parameter 'issuer' is set
        if self.api_client.client_side_validation and ('issuer' not in params or
                                                       params['issuer'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `issuer` when calling `tunnel_standalone_client_v1_create_one_time_token_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501
        if 'tunnel_config_uuid' in params:
            path_params['tunnelConfigUuid'] = params['tunnel_config_uuid']  # noqa: E501
        if 'bundle_id' in params:
            path_params['bundleId'] = params['bundle_id']  # noqa: E501
        if 'profile_uuid' in params:
            path_params['profileUuid'] = params['profile_uuid']  # noqa: E501
        if 'issuer' in params:
            path_params['issuer'] = params['issuer']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{uuid}/tunnel/{tunnelConfigUuid}/applications/{bundleId}/profile/{profileUuid}/scep-token/{issuer}', 'POST',
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

    def tunnel_standalone_client_v1_get_tunnel_configuration_async(self, device_uuid, **kwargs):  # noqa: E501
        """New - Retrieves the tunnel configuration for the device.  # noqa: E501

        Retrieves the tunnel configuration for the specified device based on the provided tunnel configuration uuid and other query params.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tunnel_standalone_client_v1_get_tunnel_configuration_async(device_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_uuid: The device uuid(Required). (required)
        :return: TunnelStandAloneClientConfigurationV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tunnel_standalone_client_v1_get_tunnel_configuration_async_with_http_info(device_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.tunnel_standalone_client_v1_get_tunnel_configuration_async_with_http_info(device_uuid, **kwargs)  # noqa: E501
            return data

    def tunnel_standalone_client_v1_get_tunnel_configuration_async_with_http_info(self, device_uuid, **kwargs):  # noqa: E501
        """New - Retrieves the tunnel configuration for the device.  # noqa: E501

        Retrieves the tunnel configuration for the specified device based on the provided tunnel configuration uuid and other query params.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tunnel_standalone_client_v1_get_tunnel_configuration_async_with_http_info(device_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_uuid: The device uuid(Required). (required)
        :return: TunnelStandAloneClientConfigurationV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tunnel_standalone_client_v1_get_tunnel_configuration_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_uuid' is set
        if self.api_client.client_side_validation and ('device_uuid' not in params or
                                                       params['device_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `device_uuid` when calling `tunnel_standalone_client_v1_get_tunnel_configuration_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_uuid' in params:
            path_params['deviceUuid'] = params['device_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{deviceUuid}/tunnel/profile', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TunnelStandAloneClientConfigurationV1Model',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
