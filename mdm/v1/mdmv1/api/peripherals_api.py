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


class PeripheralsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def peripherals_get_printer_by_id_async(self, device_id, **kwargs):  # noqa: E501
        """Gets the printer by identifier.  # noqa: E501

        Gets the printer properties by printer identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peripherals_get_printer_by_id_async(device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int device_id: The device identifier. (Required). (required)
        :return: Printer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.peripherals_get_printer_by_id_async_with_http_info(device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.peripherals_get_printer_by_id_async_with_http_info(device_id, **kwargs)  # noqa: E501
            return data

    def peripherals_get_printer_by_id_async_with_http_info(self, device_id, **kwargs):  # noqa: E501
        """Gets the printer by identifier.  # noqa: E501

        Gets the printer properties by printer identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peripherals_get_printer_by_id_async_with_http_info(device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int device_id: The device identifier. (Required). (required)
        :return: Printer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method peripherals_get_printer_by_id_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if self.api_client.client_side_validation and ('device_id' not in params or
                                                       params['device_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `device_id` when calling `peripherals_get_printer_by_id_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceID'] = params['device_id']  # noqa: E501

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
            '/peripherals/printer/{deviceID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Printer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def peripherals_get_printer_by_location_group_id_async(self, organization_group_id, **kwargs):  # noqa: E501
        """Gets the printer by organization group identifier.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peripherals_get_printer_by_location_group_id_async(organization_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_group_id: The organization group identifier. (Required). (required)
        :return: list[Printer]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.peripherals_get_printer_by_location_group_id_async_with_http_info(organization_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.peripherals_get_printer_by_location_group_id_async_with_http_info(organization_group_id, **kwargs)  # noqa: E501
            return data

    def peripherals_get_printer_by_location_group_id_async_with_http_info(self, organization_group_id, **kwargs):  # noqa: E501
        """Gets the printer by organization group identifier.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peripherals_get_printer_by_location_group_id_async_with_http_info(organization_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_group_id: The organization group identifier. (Required). (required)
        :return: list[Printer]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method peripherals_get_printer_by_location_group_id_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_group_id' is set
        if self.api_client.client_side_validation and ('organization_group_id' not in params or
                                                       params['organization_group_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `organization_group_id` when calling `peripherals_get_printer_by_location_group_id_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_group_id' in params:
            path_params['organizationGroupID'] = params['organization_group_id']  # noqa: E501

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
            '/peripherals/printers/{organizationGroupID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Printer]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)