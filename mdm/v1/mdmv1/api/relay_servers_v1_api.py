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


class RelayServersV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def relay_servers_v1_add_relay_server(self, **kwargs):  # noqa: E501
        """New - Creates a new relay server provided valid values are given.  # noqa: E501

        Creates a new relay server based on the valid values given.<br>Relay server is a FTP server from where the devices can download the provisioning files.  This is done inorder to reduce the load of deviceservices.</br><br>These details include Name of relay server, Organization group under which it is managed, Username, Password, Connection details for the device and console to connect.</br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_add_relay_server(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RelayServerDetailsModel_ relay_server_details: Details of the relay server to be created.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.relay_servers_v1_add_relay_server_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.relay_servers_v1_add_relay_server_with_http_info(**kwargs)  # noqa: E501
            return data

    def relay_servers_v1_add_relay_server_with_http_info(self, **kwargs):  # noqa: E501
        """New - Creates a new relay server provided valid values are given.  # noqa: E501

        Creates a new relay server based on the valid values given.<br>Relay server is a FTP server from where the devices can download the provisioning files.  This is done inorder to reduce the load of deviceservices.</br><br>These details include Name of relay server, Organization group under which it is managed, Username, Password, Connection details for the device and console to connect.</br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_add_relay_server_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RelayServerDetailsModel_ relay_server_details: Details of the relay server to be created.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relay_server_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method relay_servers_v1_add_relay_server" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'relay_server_details' in params:
            body_params = params['relay_server_details']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/relayservers', 'POST',
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

    def relay_servers_v1_add_relay_servers_in_bulk(self, relay_server_details_list, **kwargs):  # noqa: E501
        """New - Creates new relay servers in bulk provided valid values are given.  # noqa: E501

        Creates new relay servers in bulk with valid values given.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_add_relay_servers_in_bulk(relay_server_details_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[RelayServerDetailsModel_] relay_server_details_list: List of details of the relay server to be added.(Required) (required)
        :return: RelayServerBulkResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.relay_servers_v1_add_relay_servers_in_bulk_with_http_info(relay_server_details_list, **kwargs)  # noqa: E501
        else:
            (data) = self.relay_servers_v1_add_relay_servers_in_bulk_with_http_info(relay_server_details_list, **kwargs)  # noqa: E501
            return data

    def relay_servers_v1_add_relay_servers_in_bulk_with_http_info(self, relay_server_details_list, **kwargs):  # noqa: E501
        """New - Creates new relay servers in bulk provided valid values are given.  # noqa: E501

        Creates new relay servers in bulk with valid values given.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_add_relay_servers_in_bulk_with_http_info(relay_server_details_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[RelayServerDetailsModel_] relay_server_details_list: List of details of the relay server to be added.(Required) (required)
        :return: RelayServerBulkResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relay_server_details_list']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method relay_servers_v1_add_relay_servers_in_bulk" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relay_server_details_list' is set
        if self.api_client.client_side_validation and ('relay_server_details_list' not in params or
                                                       params['relay_server_details_list'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `relay_server_details_list` when calling `relay_servers_v1_add_relay_servers_in_bulk`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'relay_server_details_list' in params:
            body_params = params['relay_server_details_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/relayservers/bulk', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RelayServerBulkResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def relay_servers_v1_delete_relay_server(self, server_id, **kwargs):  # noqa: E501
        """New - Delete the relay server.  # noqa: E501

        Deletes the existing relay server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_delete_relay_server(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: Id of the relay server. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.relay_servers_v1_delete_relay_server_with_http_info(server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.relay_servers_v1_delete_relay_server_with_http_info(server_id, **kwargs)  # noqa: E501
            return data

    def relay_servers_v1_delete_relay_server_with_http_info(self, server_id, **kwargs):  # noqa: E501
        """New - Delete the relay server.  # noqa: E501

        Deletes the existing relay server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_delete_relay_server_with_http_info(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: Id of the relay server. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method relay_servers_v1_delete_relay_server" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in params or
                                                       params['server_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `server_id` when calling `relay_servers_v1_delete_relay_server`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['serverId'] = params['server_id']  # noqa: E501

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
            '/relayservers/{serverId}', 'DELETE',
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

    def relay_servers_v1_get_server_details(self, server_id, **kwargs):  # noqa: E501
        """New - Gets details of existing relay server.  # noqa: E501

        Fetch the details of the existing relay server.<br>These details include Name of relay server, Organization group under which it is managed, Username, Password, Connection details for the device and console to connect.</br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_get_server_details(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: Relay server id. (required)
        :return: RelayServerDetailsModel_
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.relay_servers_v1_get_server_details_with_http_info(server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.relay_servers_v1_get_server_details_with_http_info(server_id, **kwargs)  # noqa: E501
            return data

    def relay_servers_v1_get_server_details_with_http_info(self, server_id, **kwargs):  # noqa: E501
        """New - Gets details of existing relay server.  # noqa: E501

        Fetch the details of the existing relay server.<br>These details include Name of relay server, Organization group under which it is managed, Username, Password, Connection details for the device and console to connect.</br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_get_server_details_with_http_info(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: Relay server id. (required)
        :return: RelayServerDetailsModel_
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method relay_servers_v1_get_server_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in params or
                                                       params['server_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `server_id` when calling `relay_servers_v1_get_server_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['serverId'] = params['server_id']  # noqa: E501

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
            '/relayservers/{serverId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RelayServerDetailsModel_',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def relay_servers_v1_posts_contents_on_relay_server_async(self, relay_server_content_input_model, **kwargs):  # noqa: E501
        """New - Posts contents for the eligible relay server for the product and og inputted.  # noqa: E501

        Posts contents for the eligible relay server for the product and og inputted when there are no devices enrolled in the organization group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_posts_contents_on_relay_server_async(relay_server_content_input_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RelayServerContentInputModel relay_server_content_input_model: Input representing product uuid and organization group uuid(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.relay_servers_v1_posts_contents_on_relay_server_async_with_http_info(relay_server_content_input_model, **kwargs)  # noqa: E501
        else:
            (data) = self.relay_servers_v1_posts_contents_on_relay_server_async_with_http_info(relay_server_content_input_model, **kwargs)  # noqa: E501
            return data

    def relay_servers_v1_posts_contents_on_relay_server_async_with_http_info(self, relay_server_content_input_model, **kwargs):  # noqa: E501
        """New - Posts contents for the eligible relay server for the product and og inputted.  # noqa: E501

        Posts contents for the eligible relay server for the product and og inputted when there are no devices enrolled in the organization group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_posts_contents_on_relay_server_async_with_http_info(relay_server_content_input_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RelayServerContentInputModel relay_server_content_input_model: Input representing product uuid and organization group uuid(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relay_server_content_input_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method relay_servers_v1_posts_contents_on_relay_server_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relay_server_content_input_model' is set
        if self.api_client.client_side_validation and ('relay_server_content_input_model' not in params or
                                                       params['relay_server_content_input_model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `relay_server_content_input_model` when calling `relay_servers_v1_posts_contents_on_relay_server_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'relay_server_content_input_model' in params:
            body_params = params['relay_server_content_input_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/relayservers/contents', 'POST',
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

    def relay_servers_v1_update_relay_server(self, **kwargs):  # noqa: E501
        """New - Update the details existing relay server.  # noqa: E501

        Update the details of existing relay server. <br>These details include Name of relay server, Organization group under which it is managed, Username, Password, Connection details for the device and console to connect. </br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_update_relay_server(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RelayServerDetailsModel relay_server_details: Details of the relay server to be updated.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.relay_servers_v1_update_relay_server_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.relay_servers_v1_update_relay_server_with_http_info(**kwargs)  # noqa: E501
            return data

    def relay_servers_v1_update_relay_server_with_http_info(self, **kwargs):  # noqa: E501
        """New - Update the details existing relay server.  # noqa: E501

        Update the details of existing relay server. <br>These details include Name of relay server, Organization group under which it is managed, Username, Password, Connection details for the device and console to connect. </br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relay_servers_v1_update_relay_server_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RelayServerDetailsModel relay_server_details: Details of the relay server to be updated.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relay_server_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method relay_servers_v1_update_relay_server" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'relay_server_details' in params:
            body_params = params['relay_server_details']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/relayservers', 'PUT',
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
