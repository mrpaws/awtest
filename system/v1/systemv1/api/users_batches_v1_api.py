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


class UsersBatchesV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def users_batches_v1_batch_import_async_async(self, organization_group_uuid, batch_name, batch_description, **kwargs):  # noqa: E501
        """New - Imports users batch.  # noqa: E501

        Imports user batch data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_batch_import_async_async(organization_group_uuid, batch_name, batch_description, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Organization Group unique identifier.(Required). (required)
        :param str batch_name: Name of the batch.(Required). (required)
        :param str batch_description: Description of the batch.(Required). (required)
        :param object batch_type: Type of the batch.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.users_batches_v1_batch_import_async_async_with_http_info(organization_group_uuid, batch_name, batch_description, **kwargs)  # noqa: E501
        else:
            (data) = self.users_batches_v1_batch_import_async_async_with_http_info(organization_group_uuid, batch_name, batch_description, **kwargs)  # noqa: E501
            return data

    def users_batches_v1_batch_import_async_async_with_http_info(self, organization_group_uuid, batch_name, batch_description, **kwargs):  # noqa: E501
        """New - Imports users batch.  # noqa: E501

        Imports user batch data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_batch_import_async_async_with_http_info(organization_group_uuid, batch_name, batch_description, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Organization Group unique identifier.(Required). (required)
        :param str batch_name: Name of the batch.(Required). (required)
        :param str batch_description: Description of the batch.(Required). (required)
        :param object batch_type: Type of the batch.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_group_uuid', 'batch_name', 'batch_description', 'batch_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_batches_v1_batch_import_async_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_group_uuid' is set
        if self.api_client.client_side_validation and ('organization_group_uuid' not in params or
                                                       params['organization_group_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `organization_group_uuid` when calling `users_batches_v1_batch_import_async_async`")  # noqa: E501
        # verify the required parameter 'batch_name' is set
        if self.api_client.client_side_validation and ('batch_name' not in params or
                                                       params['batch_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `batch_name` when calling `users_batches_v1_batch_import_async_async`")  # noqa: E501
        # verify the required parameter 'batch_description' is set
        if self.api_client.client_side_validation and ('batch_description' not in params or
                                                       params['batch_description'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `batch_description` when calling `users_batches_v1_batch_import_async_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organization_group_uuid' in params:
            query_params.append(('organizationGroupUuid', params['organization_group_uuid']))  # noqa: E501
        if 'batch_name' in params:
            query_params.append(('batchName', params['batch_name']))  # noqa: E501
        if 'batch_description' in params:
            query_params.append(('batchDescription', params['batch_description']))  # noqa: E501
        if 'batch_type' in params:
            query_params.append(('batch_type', params['batch_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users/batches', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def users_batches_v1_generate_report_async(self, report_parameters, **kwargs):  # noqa: E501
        """New - Generate report of users batch details.  # noqa: E501

        Generate report of users batch details based on the parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_generate_report_async(report_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UsersBatchesReportV1Model report_parameters: user batch details for report.(Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.users_batches_v1_generate_report_async_with_http_info(report_parameters, **kwargs)  # noqa: E501
        else:
            (data) = self.users_batches_v1_generate_report_async_with_http_info(report_parameters, **kwargs)  # noqa: E501
            return data

    def users_batches_v1_generate_report_async_with_http_info(self, report_parameters, **kwargs):  # noqa: E501
        """New - Generate report of users batch details.  # noqa: E501

        Generate report of users batch details based on the parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_generate_report_async_with_http_info(report_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UsersBatchesReportV1Model report_parameters: user batch details for report.(Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_parameters']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_batches_v1_generate_report_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_parameters' is set
        if self.api_client.client_side_validation and ('report_parameters' not in params or
                                                       params['report_parameters'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `report_parameters` when calling `users_batches_v1_generate_report_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'report_parameters' in params:
            body_params = params['report_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users/batches/report', 'POST',
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

    def users_batches_v1_generate_user_batch_details_report_async(self, user_batch_uuid, report_parameters, **kwargs):  # noqa: E501
        """New - Generate user batch details Report.  # noqa: E501

        Generate report of user batch details based on the parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_generate_user_batch_details_report_async(user_batch_uuid, report_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_batch_uuid: Unique identifier of user batch.(Required). (required)
        :param UserBatchDetailsReportV1Model report_parameters: User batch error model.(Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.users_batches_v1_generate_user_batch_details_report_async_with_http_info(user_batch_uuid, report_parameters, **kwargs)  # noqa: E501
        else:
            (data) = self.users_batches_v1_generate_user_batch_details_report_async_with_http_info(user_batch_uuid, report_parameters, **kwargs)  # noqa: E501
            return data

    def users_batches_v1_generate_user_batch_details_report_async_with_http_info(self, user_batch_uuid, report_parameters, **kwargs):  # noqa: E501
        """New - Generate user batch details Report.  # noqa: E501

        Generate report of user batch details based on the parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_generate_user_batch_details_report_async_with_http_info(user_batch_uuid, report_parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_batch_uuid: Unique identifier of user batch.(Required). (required)
        :param UserBatchDetailsReportV1Model report_parameters: User batch error model.(Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_batch_uuid', 'report_parameters']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_batches_v1_generate_user_batch_details_report_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_batch_uuid' is set
        if self.api_client.client_side_validation and ('user_batch_uuid' not in params or
                                                       params['user_batch_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_batch_uuid` when calling `users_batches_v1_generate_user_batch_details_report_async`")  # noqa: E501
        # verify the required parameter 'report_parameters' is set
        if self.api_client.client_side_validation and ('report_parameters' not in params or
                                                       params['report_parameters'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `report_parameters` when calling `users_batches_v1_generate_user_batch_details_report_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_batch_uuid' in params:
            path_params['userBatchUuid'] = params['user_batch_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'report_parameters' in params:
            body_params = params['report_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users/batches/{userBatchUuid}/details/report', 'POST',
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

    def users_batches_v1_get_users_batch_details_async_async(self, user_batch_uuid, **kwargs):  # noqa: E501
        """New - List of users batch details.  # noqa: E501

        Returns a list of users batch details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_get_users_batch_details_async_async(user_batch_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_batch_uuid: id of user batch.(Required). (required)
        :param str row_number: Filter records based on row number.
        :param str description: Filter records based on description.
        :param int page: Specific page number to get. 0 based index.
        :param int page_size: Maximum records per page. Default 500.
        :param object sort_column: Column based on which we can provide the sorting.
        :param object sort_order: The order based which on we can sort. Default value is ASC.
        :return: UsersBatchDetailsV1ResultModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.users_batches_v1_get_users_batch_details_async_async_with_http_info(user_batch_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.users_batches_v1_get_users_batch_details_async_async_with_http_info(user_batch_uuid, **kwargs)  # noqa: E501
            return data

    def users_batches_v1_get_users_batch_details_async_async_with_http_info(self, user_batch_uuid, **kwargs):  # noqa: E501
        """New - List of users batch details.  # noqa: E501

        Returns a list of users batch details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_get_users_batch_details_async_async_with_http_info(user_batch_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_batch_uuid: id of user batch.(Required). (required)
        :param str row_number: Filter records based on row number.
        :param str description: Filter records based on description.
        :param int page: Specific page number to get. 0 based index.
        :param int page_size: Maximum records per page. Default 500.
        :param object sort_column: Column based on which we can provide the sorting.
        :param object sort_order: The order based which on we can sort. Default value is ASC.
        :return: UsersBatchDetailsV1ResultModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_batch_uuid', 'row_number', 'description', 'page', 'page_size', 'sort_column', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_batches_v1_get_users_batch_details_async_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_batch_uuid' is set
        if self.api_client.client_side_validation and ('user_batch_uuid' not in params or
                                                       params['user_batch_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_batch_uuid` when calling `users_batches_v1_get_users_batch_details_async_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_batch_uuid' in params:
            path_params['userBatchUuid'] = params['user_batch_uuid']  # noqa: E501

        query_params = []
        if 'row_number' in params:
            query_params.append(('row_number', params['row_number']))  # noqa: E501
        if 'description' in params:
            query_params.append(('description', params['description']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_column' in params:
            query_params.append(('sort_column', params['sort_column']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort_order', params['sort_order']))  # noqa: E501

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
            '/users/batches/{userBatchUuid}/details', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UsersBatchDetailsV1ResultModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def users_batches_v1_get_users_batches_async_async(self, organization_group_uuid, **kwargs):  # noqa: E501
        """New - Returns a list of users batches.  # noqa: E501

        Returns a list of users batches satisfying the search criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_get_users_batches_async_async(organization_group_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object organization_group_uuid: Uuid of the Organization group to fetch the user batches for.(Required) (required)
        :param str batch_name: Filter records based on batch name.
        :param str batch_description: Filter records based on batch description.
        :param int page: Specific page number to get. 0 based index.
        :param int page_size: Maximum records per page. Default 500.
        :param object sort_column: Column based on which we can provide the sorting.
        :param object sort_order: The order based which on we can sort. Default value is ASC.
        :return: UsersBatchesV1ResultModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.users_batches_v1_get_users_batches_async_async_with_http_info(organization_group_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.users_batches_v1_get_users_batches_async_async_with_http_info(organization_group_uuid, **kwargs)  # noqa: E501
            return data

    def users_batches_v1_get_users_batches_async_async_with_http_info(self, organization_group_uuid, **kwargs):  # noqa: E501
        """New - Returns a list of users batches.  # noqa: E501

        Returns a list of users batches satisfying the search criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_get_users_batches_async_async_with_http_info(organization_group_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object organization_group_uuid: Uuid of the Organization group to fetch the user batches for.(Required) (required)
        :param str batch_name: Filter records based on batch name.
        :param str batch_description: Filter records based on batch description.
        :param int page: Specific page number to get. 0 based index.
        :param int page_size: Maximum records per page. Default 500.
        :param object sort_column: Column based on which we can provide the sorting.
        :param object sort_order: The order based which on we can sort. Default value is ASC.
        :return: UsersBatchesV1ResultModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_group_uuid', 'batch_name', 'batch_description', 'page', 'page_size', 'sort_column', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_batches_v1_get_users_batches_async_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_group_uuid' is set
        if self.api_client.client_side_validation and ('organization_group_uuid' not in params or
                                                       params['organization_group_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `organization_group_uuid` when calling `users_batches_v1_get_users_batches_async_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organization_group_uuid' in params:
            query_params.append(('organization_group_uuid', params['organization_group_uuid']))  # noqa: E501
        if 'batch_name' in params:
            query_params.append(('batch_name', params['batch_name']))  # noqa: E501
        if 'batch_description' in params:
            query_params.append(('batch_description', params['batch_description']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_column' in params:
            query_params.append(('sort_column', params['sort_column']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort_order', params['sort_order']))  # noqa: E501

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
            '/users/batches', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UsersBatchesV1ResultModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def users_batches_v1_patch_batch_async(self, user_batch_id, users_model, user_batch_id2, **kwargs):  # noqa: E501
        """New - Update Users Batch.  # noqa: E501

        Update Users Batch resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_patch_batch_async(user_batch_id, users_model, user_batch_id2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_batch_id: User batch ID(Required). (required)
        :param UsersBatchesV1Model users_model: Configuration request model(Required). (required)
        :param str user_batch_id2: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.users_batches_v1_patch_batch_async_with_http_info(user_batch_id, users_model, user_batch_id2, **kwargs)  # noqa: E501
        else:
            (data) = self.users_batches_v1_patch_batch_async_with_http_info(user_batch_id, users_model, user_batch_id2, **kwargs)  # noqa: E501
            return data

    def users_batches_v1_patch_batch_async_with_http_info(self, user_batch_id, users_model, user_batch_id2, **kwargs):  # noqa: E501
        """New - Update Users Batch.  # noqa: E501

        Update Users Batch resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_batches_v1_patch_batch_async_with_http_info(user_batch_id, users_model, user_batch_id2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_batch_id: User batch ID(Required). (required)
        :param UsersBatchesV1Model users_model: Configuration request model(Required). (required)
        :param str user_batch_id2: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_batch_id', 'users_model', 'user_batch_id2']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_batches_v1_patch_batch_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_batch_id' is set
        if self.api_client.client_side_validation and ('user_batch_id' not in params or
                                                       params['user_batch_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_batch_id` when calling `users_batches_v1_patch_batch_async`")  # noqa: E501
        # verify the required parameter 'users_model' is set
        if self.api_client.client_side_validation and ('users_model' not in params or
                                                       params['users_model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `users_model` when calling `users_batches_v1_patch_batch_async`")  # noqa: E501
        # verify the required parameter 'user_batch_id2' is set
        if self.api_client.client_side_validation and ('user_batch_id2' not in params or
                                                       params['user_batch_id2'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_batch_id2` when calling `users_batches_v1_patch_batch_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_batch_id2' in params:
            path_params['user-batch-id'] = params['user_batch_id2']  # noqa: E501

        query_params = []
        if 'user_batch_id' in params:
            query_params.append(('userBatchId', params['user_batch_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'users_model' in params:
            body_params = params['users_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users/batches/{user-batch-id}', 'PATCH',
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
