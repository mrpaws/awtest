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


class AppsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def apps_admin_app_details_async(self, id, **kwargs):  # noqa: E501
        """Retrieves Admin applications details for passed DeviceID.  # noqa: E501

        v1.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_admin_app_details_async(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The device ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apps_admin_app_details_async_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.apps_admin_app_details_async_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def apps_admin_app_details_async_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves Admin applications details for passed DeviceID.  # noqa: E501

        v1.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_admin_app_details_async_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The device ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_admin_app_details_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `apps_admin_app_details_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{id}/adminapps', 'GET',
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

    def apps_device_apps_by_alternate_id(self, **kwargs):  # noqa: E501
        """Retrieves application details of the device identified by alternate id.  # noqa: E501

        Fetches all application details for the device identified by alternate ID other than device ID.  Alternate device identifiers can be MAC address, IMEI, Serial number or UDID.  Example : IMEI-BCG84753GH, Serial Number-573489754.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_device_apps_by_alternate_id(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_by: The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber].
        :param str id: Device alternate id.
        :param int page: The specific page number to get.
        :param int pagesize: Max records per page.
        :return: DeviceAppsResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apps_device_apps_by_alternate_id_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.apps_device_apps_by_alternate_id_with_http_info(**kwargs)  # noqa: E501
            return data

    def apps_device_apps_by_alternate_id_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves application details of the device identified by alternate id.  # noqa: E501

        Fetches all application details for the device identified by alternate ID other than device ID.  Alternate device identifiers can be MAC address, IMEI, Serial number or UDID.  Example : IMEI-BCG84753GH, Serial Number-573489754.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_device_apps_by_alternate_id_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_by: The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber].
        :param str id: Device alternate id.
        :param int page: The specific page number to get.
        :param int pagesize: Max records per page.
        :return: DeviceAppsResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_by', 'id', 'page', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_device_apps_by_alternate_id" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_by' in params:
            query_params.append(('searchBy', params['search_by']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'pagesize' in params:
            query_params.append(('pagesize', params['pagesize']))  # noqa: E501

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
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/devices/apps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceAppsResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apps_device_apps_by_id(self, id, **kwargs):  # noqa: E501
        """Retrieves application details of the device identified by device ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_device_apps_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The device ID (Required). (required)
        :param int page: The specific page number to get.
        :param int pagesize: Max records per page.
        :return: DeviceAppsResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apps_device_apps_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.apps_device_apps_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def apps_device_apps_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves application details of the device identified by device ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_device_apps_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The device ID (Required). (required)
        :param int page: The specific page number to get.
        :param int pagesize: Max records per page.
        :return: DeviceAppsResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_device_apps_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `apps_device_apps_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'pagesize' in params:
            query_params.append(('pagesize', params['pagesize']))  # noqa: E501

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
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{id}/apps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceAppsResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)