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


class WorkflowDeviceSideV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def workflow_device_side_v1_get_bulk_workflow_definitions_async(self, workflow_uuids, **kwargs):  # noqa: E501
        """New - Gets the workflows for the device.  # noqa: E501

        Retrieves the workflows for a device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workflow_device_side_v1_get_bulk_workflow_definitions_async(workflow_uuids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[DeviceWorkflowBulkRequestV1Model] workflow_uuids: Uuids of the workflows to retrieve.(Required) (required)
        :return: list[DeviceWorkflowDefinitionBulkResponseV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workflow_device_side_v1_get_bulk_workflow_definitions_async_with_http_info(workflow_uuids, **kwargs)  # noqa: E501
        else:
            (data) = self.workflow_device_side_v1_get_bulk_workflow_definitions_async_with_http_info(workflow_uuids, **kwargs)  # noqa: E501
            return data

    def workflow_device_side_v1_get_bulk_workflow_definitions_async_with_http_info(self, workflow_uuids, **kwargs):  # noqa: E501
        """New - Gets the workflows for the device.  # noqa: E501

        Retrieves the workflows for a device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workflow_device_side_v1_get_bulk_workflow_definitions_async_with_http_info(workflow_uuids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[DeviceWorkflowBulkRequestV1Model] workflow_uuids: Uuids of the workflows to retrieve.(Required) (required)
        :return: list[DeviceWorkflowDefinitionBulkResponseV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workflow_uuids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workflow_device_side_v1_get_bulk_workflow_definitions_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workflow_uuids' is set
        if self.api_client.client_side_validation and ('workflow_uuids' not in params or
                                                       params['workflow_uuids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `workflow_uuids` when calling `workflow_device_side_v1_get_bulk_workflow_definitions_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'workflow_uuids' in params:
            body_params = params['workflow_uuids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/workflows/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DeviceWorkflowDefinitionBulkResponseV1Model]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workflow_device_side_v1_get_workflow_metadata_async(self, device_uuid, **kwargs):  # noqa: E501
        """New - Gets the metadata for the workflows assigned to the device.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workflow_device_side_v1_get_workflow_metadata_async(device_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object device_uuid: Uuid of the device.(Required) (required)
        :return: list[WorkflowMetadataV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workflow_device_side_v1_get_workflow_metadata_async_with_http_info(device_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.workflow_device_side_v1_get_workflow_metadata_async_with_http_info(device_uuid, **kwargs)  # noqa: E501
            return data

    def workflow_device_side_v1_get_workflow_metadata_async_with_http_info(self, device_uuid, **kwargs):  # noqa: E501
        """New - Gets the metadata for the workflows assigned to the device.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workflow_device_side_v1_get_workflow_metadata_async_with_http_info(device_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object device_uuid: Uuid of the device.(Required) (required)
        :return: list[WorkflowMetadataV1Model]
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
                    " to method workflow_device_side_v1_get_workflow_metadata_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_uuid' is set
        if self.api_client.client_side_validation and ('device_uuid' not in params or
                                                       params['device_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `device_uuid` when calling `workflow_device_side_v1_get_workflow_metadata_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'device_uuid' in params:
            query_params.append(('device_uuid', params['device_uuid']))  # noqa: E501

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
            '/workflows/metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WorkflowMetadataV1Model]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
