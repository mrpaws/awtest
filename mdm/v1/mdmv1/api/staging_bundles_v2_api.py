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


class StagingBundlesV2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def staging_bundles_v2_retrieve_sideload_staging_file(self, staging_uuid, **kwargs):  # noqa: E501
        """New - Retrieves a side-load staging zip or tar.gz file  # noqa: E501

        Retrieves a side-load zip or tar.gz file used for staging a device, installing the agent, installing staging content, and enrolling, used mostly on Rugged devices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.staging_bundles_v2_retrieve_sideload_staging_file(staging_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str staging_uuid: staging bundle uuid(Required) (required)
        :param int organizationgroupid: organization group id
        :param str key: key used to encrypt some of the files in archive
        :param bool universal: when staging the device, set to true if you want the end-user to choose the organization group the device will be apart of.
        :return: Stream
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.staging_bundles_v2_retrieve_sideload_staging_file_with_http_info(staging_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.staging_bundles_v2_retrieve_sideload_staging_file_with_http_info(staging_uuid, **kwargs)  # noqa: E501
            return data

    def staging_bundles_v2_retrieve_sideload_staging_file_with_http_info(self, staging_uuid, **kwargs):  # noqa: E501
        """New - Retrieves a side-load staging zip or tar.gz file  # noqa: E501

        Retrieves a side-load zip or tar.gz file used for staging a device, installing the agent, installing staging content, and enrolling, used mostly on Rugged devices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.staging_bundles_v2_retrieve_sideload_staging_file_with_http_info(staging_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str staging_uuid: staging bundle uuid(Required) (required)
        :param int organizationgroupid: organization group id
        :param str key: key used to encrypt some of the files in archive
        :param bool universal: when staging the device, set to true if you want the end-user to choose the organization group the device will be apart of.
        :return: Stream
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['staging_uuid', 'organizationgroupid', 'key', 'universal']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method staging_bundles_v2_retrieve_sideload_staging_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'staging_uuid' is set
        if self.api_client.client_side_validation and ('staging_uuid' not in params or
                                                       params['staging_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `staging_uuid` when calling `staging_bundles_v2_retrieve_sideload_staging_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'staging_uuid' in params:
            path_params['stagingUuid'] = params['staging_uuid']  # noqa: E501

        query_params = []
        if 'organizationgroupid' in params:
            query_params.append(('organizationgroupid', params['organizationgroupid']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
        if 'universal' in params:
            query_params.append(('universal', params['universal']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/product-components/staging-bundles/{stagingUuid}/sideload', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Stream',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
