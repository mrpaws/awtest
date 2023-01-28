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


class ProductMonitorV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def product_monitor_v1_get_applications(self, **kwargs):  # noqa: E501
        """New - Gets the list of apps based on the search parameters  # noqa: E501

        Returns the list of all matching apps on the search criteria provided  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_monitor_v1_get_applications(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str searchtext: App name or part of app name used as Search text for searching applications
        :param int pagenumber: Specific page number to get. Default value is 0
        :param int pagesize: Maximumm records per page. Default value is 20
        :return: list[ProductDetailV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_monitor_v1_get_applications_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.product_monitor_v1_get_applications_with_http_info(**kwargs)  # noqa: E501
            return data

    def product_monitor_v1_get_applications_with_http_info(self, **kwargs):  # noqa: E501
        """New - Gets the list of apps based on the search parameters  # noqa: E501

        Returns the list of all matching apps on the search criteria provided  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_monitor_v1_get_applications_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str searchtext: App name or part of app name used as Search text for searching applications
        :param int pagenumber: Specific page number to get. Default value is 0
        :param int pagesize: Maximumm records per page. Default value is 20
        :return: list[ProductDetailV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['searchtext', 'pagenumber', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_monitor_v1_get_applications" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'searchtext' in params:
            query_params.append(('searchtext', params['searchtext']))  # noqa: E501
        if 'pagenumber' in params:
            query_params.append(('pagenumber', params['pagenumber']))  # noqa: E501
        if 'pagesize' in params:
            query_params.append(('pagesize', params['pagesize']))  # noqa: E501

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
            '/productmonitor/apps/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProductDetailV1Model]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product_monitor_v1_get_product_deployment_status(self, uuid, producttype, **kwargs):  # noqa: E501
        """New - Gets the deployment status of the specified app or profile on various devices  # noqa: E501

        Returns the deployment status of the specified app or profile on various devices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_monitor_v1_get_product_deployment_status(uuid, producttype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Unique Identifier for App or profile(Required) (required)
        :param str producttype: Type of the product i.e., InternalApp, PublicApp, PurchasedApp or Profile(Required) (required)
        :return: ProductDeploymentDetailsV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_monitor_v1_get_product_deployment_status_with_http_info(uuid, producttype, **kwargs)  # noqa: E501
        else:
            (data) = self.product_monitor_v1_get_product_deployment_status_with_http_info(uuid, producttype, **kwargs)  # noqa: E501
            return data

    def product_monitor_v1_get_product_deployment_status_with_http_info(self, uuid, producttype, **kwargs):  # noqa: E501
        """New - Gets the deployment status of the specified app or profile on various devices  # noqa: E501

        Returns the deployment status of the specified app or profile on various devices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_monitor_v1_get_product_deployment_status_with_http_info(uuid, producttype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Unique Identifier for App or profile(Required) (required)
        :param str producttype: Type of the product i.e., InternalApp, PublicApp, PurchasedApp or Profile(Required) (required)
        :return: ProductDeploymentDetailsV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'producttype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_monitor_v1_get_product_deployment_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in params or
                                                       params['uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uuid` when calling `product_monitor_v1_get_product_deployment_status`")  # noqa: E501
        # verify the required parameter 'producttype' is set
        if self.api_client.client_side_validation and ('producttype' not in params or
                                                       params['producttype'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `producttype` when calling `product_monitor_v1_get_product_deployment_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []
        if 'producttype' in params:
            query_params.append(('producttype', params['producttype']))  # noqa: E501

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
            '/productmonitor/products/{uuid}/deploymentstatus', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductDeploymentDetailsV1Model',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product_monitor_v1_get_profiles(self, **kwargs):  # noqa: E501
        """New - Gets the list of profiles based on the search parameters  # noqa: E501

        Returns the list of all matching profiles on the search criteria provided  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_monitor_v1_get_profiles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str searchtext: Profile name or part of profile name used as Search text for searching profiles
        :param int pagenumber: Specific page number to get. Default value is 0
        :param int pagesize: Maximumm records per page. Default value is 20
        :return: list[ProductDetailV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_monitor_v1_get_profiles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.product_monitor_v1_get_profiles_with_http_info(**kwargs)  # noqa: E501
            return data

    def product_monitor_v1_get_profiles_with_http_info(self, **kwargs):  # noqa: E501
        """New - Gets the list of profiles based on the search parameters  # noqa: E501

        Returns the list of all matching profiles on the search criteria provided  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_monitor_v1_get_profiles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str searchtext: Profile name or part of profile name used as Search text for searching profiles
        :param int pagenumber: Specific page number to get. Default value is 0
        :param int pagesize: Maximumm records per page. Default value is 20
        :return: list[ProductDetailV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['searchtext', 'pagenumber', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_monitor_v1_get_profiles" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'searchtext' in params:
            query_params.append(('searchtext', params['searchtext']))  # noqa: E501
        if 'pagenumber' in params:
            query_params.append(('pagenumber', params['pagenumber']))  # noqa: E501
        if 'pagesize' in params:
            query_params.append(('pagesize', params['pagesize']))  # noqa: E501

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
            '/productmonitor/profiles/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProductDetailV1Model]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)