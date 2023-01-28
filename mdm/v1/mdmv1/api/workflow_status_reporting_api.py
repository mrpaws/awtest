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


class WorkflowStatusReportingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def workflow_status_reporting_get_device_count_for_workflow_status_async(self, workflow_uuid, **kwargs):  # noqa: E501
        """New - Get the count of devices for each workflow status.  # noqa: E501

        Get the count of devices that belong to each workflow status for specified WorkflowUuid.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workflow_status_reporting_get_device_count_for_workflow_status_async(workflow_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_uuid: Unique Identifier for the workflow.(Required) (required)
        :return: list[WorkflowStatusCount]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workflow_status_reporting_get_device_count_for_workflow_status_async_with_http_info(workflow_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.workflow_status_reporting_get_device_count_for_workflow_status_async_with_http_info(workflow_uuid, **kwargs)  # noqa: E501
            return data

    def workflow_status_reporting_get_device_count_for_workflow_status_async_with_http_info(self, workflow_uuid, **kwargs):  # noqa: E501
        """New - Get the count of devices for each workflow status.  # noqa: E501

        Get the count of devices that belong to each workflow status for specified WorkflowUuid.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workflow_status_reporting_get_device_count_for_workflow_status_async_with_http_info(workflow_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_uuid: Unique Identifier for the workflow.(Required) (required)
        :return: list[WorkflowStatusCount]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workflow_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workflow_status_reporting_get_device_count_for_workflow_status_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workflow_uuid' is set
        if self.api_client.client_side_validation and ('workflow_uuid' not in params or
                                                       params['workflow_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `workflow_uuid` when calling `workflow_status_reporting_get_device_count_for_workflow_status_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workflow_uuid' in params:
            path_params['workflowUuid'] = params['workflow_uuid']  # noqa: E501

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
            '/devices/workflows/{workflowUuid}/status/device-count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WorkflowStatusCount]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workflow_status_reporting_get_workflow_status_async(self, device_uuid, workflow_uuid, **kwargs):  # noqa: E501
        """New - Gets the status of the workflow and corresponding steps for the device.  # noqa: E501

        Gets the status of the workflow and corresponding steps for the device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workflow_status_reporting_get_workflow_status_async(device_uuid, workflow_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_uuid: Unique Identifier for the device.(Required) (required)
        :param str workflow_uuid: Unique Identifier for the workflow.(Required) (required)
        :param int page: The specific page number to get.
        :param int pagesize: Maximum records per page.
        :return: WorkflowStatusV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workflow_status_reporting_get_workflow_status_async_with_http_info(device_uuid, workflow_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.workflow_status_reporting_get_workflow_status_async_with_http_info(device_uuid, workflow_uuid, **kwargs)  # noqa: E501
            return data

    def workflow_status_reporting_get_workflow_status_async_with_http_info(self, device_uuid, workflow_uuid, **kwargs):  # noqa: E501
        """New - Gets the status of the workflow and corresponding steps for the device.  # noqa: E501

        Gets the status of the workflow and corresponding steps for the device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workflow_status_reporting_get_workflow_status_async_with_http_info(device_uuid, workflow_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_uuid: Unique Identifier for the device.(Required) (required)
        :param str workflow_uuid: Unique Identifier for the workflow.(Required) (required)
        :param int page: The specific page number to get.
        :param int pagesize: Maximum records per page.
        :return: WorkflowStatusV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_uuid', 'workflow_uuid', 'page', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workflow_status_reporting_get_workflow_status_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_uuid' is set
        if self.api_client.client_side_validation and ('device_uuid' not in params or
                                                       params['device_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `device_uuid` when calling `workflow_status_reporting_get_workflow_status_async`")  # noqa: E501
        # verify the required parameter 'workflow_uuid' is set
        if self.api_client.client_side_validation and ('workflow_uuid' not in params or
                                                       params['workflow_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `workflow_uuid` when calling `workflow_status_reporting_get_workflow_status_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_uuid' in params:
            path_params['deviceUuid'] = params['device_uuid']  # noqa: E501
        if 'workflow_uuid' in params:
            path_params['workflowUuid'] = params['workflow_uuid']  # noqa: E501

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
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{deviceUuid}/workflows/{workflowUuid}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowStatusV1Model',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workflow_status_reporting_get_workflow_status_by_device_async(self, device_uuid, **kwargs):  # noqa: E501
        """New - Get the workflow status for device.  # noqa: E501

        Get the status of device workflow.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workflow_status_reporting_get_workflow_status_by_device_async(device_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_uuid: Uuid of the device.(Required) (required)
        :param str search: The text to search for in the name of the workflow.
        :param str orderby: Order the results by this attribute.
        :param int page: The specific page number to get.
        :param int pagesize: Maximum records per page.
        :param str sortorder: Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified.
        :return: list[WorkflowStatusV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workflow_status_reporting_get_workflow_status_by_device_async_with_http_info(device_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.workflow_status_reporting_get_workflow_status_by_device_async_with_http_info(device_uuid, **kwargs)  # noqa: E501
            return data

    def workflow_status_reporting_get_workflow_status_by_device_async_with_http_info(self, device_uuid, **kwargs):  # noqa: E501
        """New - Get the workflow status for device.  # noqa: E501

        Get the status of device workflow.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workflow_status_reporting_get_workflow_status_by_device_async_with_http_info(device_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_uuid: Uuid of the device.(Required) (required)
        :param str search: The text to search for in the name of the workflow.
        :param str orderby: Order the results by this attribute.
        :param int page: The specific page number to get.
        :param int pagesize: Maximum records per page.
        :param str sortorder: Sorting order. Allowed values are ASC or DESC. Defaults to ASC if this attribute is not specified.
        :return: list[WorkflowStatusV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_uuid', 'search', 'orderby', 'page', 'pagesize', 'sortorder']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workflow_status_reporting_get_workflow_status_by_device_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_uuid' is set
        if self.api_client.client_side_validation and ('device_uuid' not in params or
                                                       params['device_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `device_uuid` when calling `workflow_status_reporting_get_workflow_status_by_device_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_uuid' in params:
            path_params['deviceUuid'] = params['device_uuid']  # noqa: E501

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'orderby' in params:
            query_params.append(('orderby', params['orderby']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'pagesize' in params:
            query_params.append(('pagesize', params['pagesize']))  # noqa: E501
        if 'sortorder' in params:
            query_params.append(('sortorder', params['sortorder']))  # noqa: E501

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
            '/devices/{deviceUuid}/workflows/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WorkflowStatusV1Model]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
