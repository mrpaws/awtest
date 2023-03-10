# coding: utf-8

"""
    MAM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mamv1.api_client import ApiClient


class ChunkApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def chunk_chunk_async(self, chunk_sequence_number, total_application_size, chunk_size, **kwargs):  # noqa: E501
        """New - upload the chunks.  # noqa: E501

        - Create a chunk at the specified path  - Supported file types are 'ipa',   'apk', 'xap', 'appx', 'msi', 'app', 'zip', 'xml', 'pem', 'exe', 'pkg',   'dmg', 'plist', 'mpkg', 'js', 'jse', 'ps1', 'ps1xml', 'psc1', 'psd1',   'psm1', 'pssc', 'cdxml', 'vbs', 'vbe', 'wsf', 'wsc', 'msp', 'mst',   'p12', 'pfx', 'p7b', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'p7m', 'ppkg', 'cat', 'apf'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chunk_chunk_async(chunk_sequence_number, total_application_size, chunk_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chunk_sequence_number: chunk sequence number being uploaded.(Required) (required)
        :param object total_application_size: total application size to be uploaded.(Required) (required)
        :param object chunk_size: total chunk size to be uploaded.(Required) (required)
        :param str transaction_id: UUID of the chunk file being uploaded.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chunk_chunk_async_with_http_info(chunk_sequence_number, total_application_size, chunk_size, **kwargs)  # noqa: E501
        else:
            (data) = self.chunk_chunk_async_with_http_info(chunk_sequence_number, total_application_size, chunk_size, **kwargs)  # noqa: E501
            return data

    def chunk_chunk_async_with_http_info(self, chunk_sequence_number, total_application_size, chunk_size, **kwargs):  # noqa: E501
        """New - upload the chunks.  # noqa: E501

        - Create a chunk at the specified path  - Supported file types are 'ipa',   'apk', 'xap', 'appx', 'msi', 'app', 'zip', 'xml', 'pem', 'exe', 'pkg',   'dmg', 'plist', 'mpkg', 'js', 'jse', 'ps1', 'ps1xml', 'psc1', 'psd1',   'psm1', 'pssc', 'cdxml', 'vbs', 'vbe', 'wsf', 'wsc', 'msp', 'mst',   'p12', 'pfx', 'p7b', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'p7m', 'ppkg', 'cat', 'apf'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chunk_chunk_async_with_http_info(chunk_sequence_number, total_application_size, chunk_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int chunk_sequence_number: chunk sequence number being uploaded.(Required) (required)
        :param object total_application_size: total application size to be uploaded.(Required) (required)
        :param object chunk_size: total chunk size to be uploaded.(Required) (required)
        :param str transaction_id: UUID of the chunk file being uploaded.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['chunk_sequence_number', 'total_application_size', 'chunk_size', 'transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chunk_chunk_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'chunk_sequence_number' is set
        if self.api_client.client_side_validation and ('chunk_sequence_number' not in params or
                                                       params['chunk_sequence_number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `chunk_sequence_number` when calling `chunk_chunk_async`")  # noqa: E501
        # verify the required parameter 'total_application_size' is set
        if self.api_client.client_side_validation and ('total_application_size' not in params or
                                                       params['total_application_size'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `total_application_size` when calling `chunk_chunk_async`")  # noqa: E501
        # verify the required parameter 'chunk_size' is set
        if self.api_client.client_side_validation and ('chunk_size' not in params or
                                                       params['chunk_size'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `chunk_size` when calling `chunk_chunk_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'chunk_sequence_number' in params:
            query_params.append(('chunk_sequence_number', params['chunk_sequence_number']))  # noqa: E501
        if 'transaction_id' in params:
            query_params.append(('transaction_id', params['transaction_id']))  # noqa: E501
        if 'total_application_size' in params:
            query_params.append(('total_application_size', params['total_application_size']))  # noqa: E501
        if 'chunk_size' in params:
            query_params.append(('chunk_size', params['chunk_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/blobs/chunk', 'POST',
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
