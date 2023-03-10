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


class LookupFieldsV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def lookup_fields_v1_retrieve_lookup_keys_async(self, organization_group_uuid, **kwargs):  # noqa: E501
        """New - Retrieves lookup keys for a given organization group  # noqa: E501

        Retrieve all lookup value keys for the given organization group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lookup_fields_v1_retrieve_lookup_keys_async(organization_group_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Represents the organization group to retrieve lookup value keys from(Required) (required)
        :param str language: The language code (Default en-US).
        :return: LookupFieldsV1Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lookup_fields_v1_retrieve_lookup_keys_async_with_http_info(organization_group_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.lookup_fields_v1_retrieve_lookup_keys_async_with_http_info(organization_group_uuid, **kwargs)  # noqa: E501
            return data

    def lookup_fields_v1_retrieve_lookup_keys_async_with_http_info(self, organization_group_uuid, **kwargs):  # noqa: E501
        """New - Retrieves lookup keys for a given organization group  # noqa: E501

        Retrieve all lookup value keys for the given organization group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lookup_fields_v1_retrieve_lookup_keys_async_with_http_info(organization_group_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Represents the organization group to retrieve lookup value keys from(Required) (required)
        :param str language: The language code (Default en-US).
        :return: LookupFieldsV1Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_group_uuid', 'language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lookup_fields_v1_retrieve_lookup_keys_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_group_uuid' is set
        if self.api_client.client_side_validation and ('organization_group_uuid' not in params or
                                                       params['organization_group_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `organization_group_uuid` when calling `lookup_fields_v1_retrieve_lookup_keys_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_group_uuid' in params:
            path_params['organizationGroupUuid'] = params['organization_group_uuid']  # noqa: E501

        query_params = []
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501

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
            '/lookup-value/keys/{organizationGroupUuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LookupFieldsV1Entity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lookup_fields_v1_retrieve_lookup_keys_by_type_async(self, organization_group_uuid, lookup_value_type, **kwargs):  # noqa: E501
        """New - Retrieves lookup keys for a specified lookup field type.  # noqa: E501

        Retrieve all lookup keys for the specified lookup field type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lookup_fields_v1_retrieve_lookup_keys_by_type_async(organization_group_uuid, lookup_value_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Represents the organization group to retrieve lookup value keys from(Required) (required)
        :param str lookup_value_type: Represents the category of lookup value keys to retrieve.(Required) (required)
        :return: LookupFieldsV1Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lookup_fields_v1_retrieve_lookup_keys_by_type_async_with_http_info(organization_group_uuid, lookup_value_type, **kwargs)  # noqa: E501
        else:
            (data) = self.lookup_fields_v1_retrieve_lookup_keys_by_type_async_with_http_info(organization_group_uuid, lookup_value_type, **kwargs)  # noqa: E501
            return data

    def lookup_fields_v1_retrieve_lookup_keys_by_type_async_with_http_info(self, organization_group_uuid, lookup_value_type, **kwargs):  # noqa: E501
        """New - Retrieves lookup keys for a specified lookup field type.  # noqa: E501

        Retrieve all lookup keys for the specified lookup field type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lookup_fields_v1_retrieve_lookup_keys_by_type_async_with_http_info(organization_group_uuid, lookup_value_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Represents the organization group to retrieve lookup value keys from(Required) (required)
        :param str lookup_value_type: Represents the category of lookup value keys to retrieve.(Required) (required)
        :return: LookupFieldsV1Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_group_uuid', 'lookup_value_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lookup_fields_v1_retrieve_lookup_keys_by_type_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_group_uuid' is set
        if self.api_client.client_side_validation and ('organization_group_uuid' not in params or
                                                       params['organization_group_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `organization_group_uuid` when calling `lookup_fields_v1_retrieve_lookup_keys_by_type_async`")  # noqa: E501
        # verify the required parameter 'lookup_value_type' is set
        if self.api_client.client_side_validation and ('lookup_value_type' not in params or
                                                       params['lookup_value_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `lookup_value_type` when calling `lookup_fields_v1_retrieve_lookup_keys_by_type_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_group_uuid' in params:
            path_params['organizationGroupUuid'] = params['organization_group_uuid']  # noqa: E501
        if 'lookup_value_type' in params:
            path_params['lookupValueType'] = params['lookup_value_type']  # noqa: E501

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
            '/lookup-value/keys/{organizationGroupUuid}/{lookupValueType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LookupFieldsV1Entity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
