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


class TunnelDeviceV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def tunnel_device_v1_get_device_details_async(self, udid, **kwargs):  # noqa: E501
        """New - Retrieves list of devices that are clients to Airwatch Tunnel.  # noqa: E501

        This retrieves list of devices that are clients to Airwatch Tunnel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tunnel_device_v1_get_device_details_async(udid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str udid: Device udid. (required)
        :return: DevicesDataV2Model
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tunnel_device_v1_get_device_details_async_with_http_info(udid, **kwargs)  # noqa: E501
        else:
            (data) = self.tunnel_device_v1_get_device_details_async_with_http_info(udid, **kwargs)  # noqa: E501
            return data

    def tunnel_device_v1_get_device_details_async_with_http_info(self, udid, **kwargs):  # noqa: E501
        """New - Retrieves list of devices that are clients to Airwatch Tunnel.  # noqa: E501

        This retrieves list of devices that are clients to Airwatch Tunnel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tunnel_device_v1_get_device_details_async_with_http_info(udid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str udid: Device udid. (required)
        :return: DevicesDataV2Model
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['udid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tunnel_device_v1_get_device_details_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'udid' is set
        if self.api_client.client_side_validation and ('udid' not in params or
                                                       params['udid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `udid` when calling `tunnel_device_v1_get_device_details_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'udid' in params:
            path_params['udid'] = params['udid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml;version=1', 'application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tunnel/devices/udid/{udid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DevicesDataV2Model',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tunnel_device_v1_get_devices_details_async(self, **kwargs):  # noqa: E501
        """New - Retrieves list of devices that are clients to Airwatch Tunnel.  # noqa: E501

        This retrieves list of devices that are clients to Airwatch Tunnel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tunnel_device_v1_get_devices_details_async(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str udid: The device udid.
        :param int page_number: 
        :param int page_size: The size of the page.
        :return: DevicesDataV2Model
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tunnel_device_v1_get_devices_details_async_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.tunnel_device_v1_get_devices_details_async_with_http_info(**kwargs)  # noqa: E501
            return data

    def tunnel_device_v1_get_devices_details_async_with_http_info(self, **kwargs):  # noqa: E501
        """New - Retrieves list of devices that are clients to Airwatch Tunnel.  # noqa: E501

        This retrieves list of devices that are clients to Airwatch Tunnel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tunnel_device_v1_get_devices_details_async_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str udid: The device udid.
        :param int page_number: 
        :param int page_size: The size of the page.
        :return: DevicesDataV2Model
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['udid', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tunnel_device_v1_get_devices_details_async" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'udid' in params:
            query_params.append(('udid', params['udid']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page_number', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml;version=1', 'application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tunnel/devices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DevicesDataV2Model',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)