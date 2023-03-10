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


class CustomAttributesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def custom_attributes_save_custom_attribute(self, custom_attribute, **kwargs):  # noqa: E501
        """Creates a custom attribute definition in AirWatch.  # noqa: E501

        Creates a custom attibute for the organization group. Multiple values can be added to a custom attribute with this API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_attributes_save_custom_attribute(custom_attribute, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomAttributeModel_ custom_attribute: Entity defining a custom attribute to be added (Required). (required)
        :return: EntityId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_attributes_save_custom_attribute_with_http_info(custom_attribute, **kwargs)  # noqa: E501
        else:
            (data) = self.custom_attributes_save_custom_attribute_with_http_info(custom_attribute, **kwargs)  # noqa: E501
            return data

    def custom_attributes_save_custom_attribute_with_http_info(self, custom_attribute, **kwargs):  # noqa: E501
        """Creates a custom attribute definition in AirWatch.  # noqa: E501

        Creates a custom attibute for the organization group. Multiple values can be added to a custom attribute with this API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_attributes_save_custom_attribute_with_http_info(custom_attribute, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomAttributeModel_ custom_attribute: Entity defining a custom attribute to be added (Required). (required)
        :return: EntityId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['custom_attribute']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_attributes_save_custom_attribute" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'custom_attribute' is set
        if self.api_client.client_side_validation and ('custom_attribute' not in params or
                                                       params['custom_attribute'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `custom_attribute` when calling `custom_attributes_save_custom_attribute`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'custom_attribute' in params:
            body_params = params['custom_attribute']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/customattributes/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EntityId',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_attributes_search(self, **kwargs):  # noqa: E501
        """Search custom attributes.  # noqa: E501

        Searches Custom Attributes based on name, page and pagesize.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_attributes_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organizationgroupid: Organization Group Identifer.
        :param str name: Custom Attribute Name.
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximumm records per page. Default 500.
        :return: CustomAttributeSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_attributes_search_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.custom_attributes_search_with_http_info(**kwargs)  # noqa: E501
            return data

    def custom_attributes_search_with_http_info(self, **kwargs):  # noqa: E501
        """Search custom attributes.  # noqa: E501

        Searches Custom Attributes based on name, page and pagesize.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_attributes_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organizationgroupid: Organization Group Identifer.
        :param str name: Custom Attribute Name.
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximumm records per page. Default 500.
        :return: CustomAttributeSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizationgroupid', 'name', 'page', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_attributes_search" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organizationgroupid' in params:
            query_params.append(('organizationgroupid', params['organizationgroupid']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
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
            '/customattributes/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomAttributeSearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
