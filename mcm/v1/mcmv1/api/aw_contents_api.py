# coding: utf-8

"""
    MCM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mcmv1.api_client import ApiClient


class AwContentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def aw_contents_delete_file(self, id, **kwargs):  # noqa: E501
        """New - Delete a Managed content.  # noqa: E501

        Delete a file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_delete_file(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier of the file.(Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aw_contents_delete_file_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.aw_contents_delete_file_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def aw_contents_delete_file_with_http_info(self, id, **kwargs):  # noqa: E501
        """New - Delete a Managed content.  # noqa: E501

        Delete a file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_delete_file_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier of the file.(Required). (required)
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
                    " to method aw_contents_delete_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `aw_contents_delete_file`")  # noqa: E501

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
        auth_settings = ['BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/awcontents/{id}', 'DELETE',
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

    def aw_contents_download_file(self, id, **kwargs):  # noqa: E501
        """New - Download a Managed content.  # noqa: E501

        Download a file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_download_file(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier of the file.(Required). (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aw_contents_download_file_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.aw_contents_download_file_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def aw_contents_download_file_with_http_info(self, id, **kwargs):  # noqa: E501
        """New - Download a Managed content.  # noqa: E501

        Download a file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_download_file_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier of the file.(Required). (required)
        :return: str
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
                    " to method aw_contents_download_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `aw_contents_download_file`")  # noqa: E501

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
            ['application/octet-stream;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/awcontents/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aw_contents_get_file_metadata_async(self, id, **kwargs):  # noqa: E501
        """New - Get metadata for a Managed content.  # noqa: E501

        Get metadata for the specified managed content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_get_file_metadata_async(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier of the file.(Required). (required)
        :return: AwContentModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aw_contents_get_file_metadata_async_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.aw_contents_get_file_metadata_async_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def aw_contents_get_file_metadata_async_with_http_info(self, id, **kwargs):  # noqa: E501
        """New - Get metadata for a Managed content.  # noqa: E501

        Get metadata for the specified managed content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_get_file_metadata_async_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier of the file.(Required). (required)
        :return: AwContentModel
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
                    " to method aw_contents_get_file_metadata_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `aw_contents_get_file_metadata_async`")  # noqa: E501

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
        auth_settings = ['BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/awcontents/{id}/info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AwContentModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aw_contents_search_async(self, **kwargs):  # noqa: E501
        """New - Search managed content.  # noqa: E501

        Search managed content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_search_async(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locationgroupcode: Organization group code.
        :param int locationgroupid: Organization group id.
        :param str query_string: Searches for the string value in the File Name.
        :param object category_id: The unique identifier for the Category.
        :param str mime_type: Filter contents by Mime Type.
        :param int expires_in: Filter by Contents that are going to expire within days specified.
        :param str sort_by: Sort the result based on a property. Accepts \"Name\", \"Size\", \"Author\", \"DownloadPriority\", \"IsRequired\", \"IsActive\", \"EffectiveDate\", \"ExpirationDate\", \"ModifiedOn\", or \"ModifiedBy\". By default it sorts by \"Name\"..
        :param bool sort_ascending: Sort direction. By default it sorts Ascending.
        :param int sort_index: Start index of page.
        :param int page_size: Specifies the number of results returned per Page.
        :return: AwContentPagedResultModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aw_contents_search_async_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.aw_contents_search_async_with_http_info(**kwargs)  # noqa: E501
            return data

    def aw_contents_search_async_with_http_info(self, **kwargs):  # noqa: E501
        """New - Search managed content.  # noqa: E501

        Search managed content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_search_async_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locationgroupcode: Organization group code.
        :param int locationgroupid: Organization group id.
        :param str query_string: Searches for the string value in the File Name.
        :param object category_id: The unique identifier for the Category.
        :param str mime_type: Filter contents by Mime Type.
        :param int expires_in: Filter by Contents that are going to expire within days specified.
        :param str sort_by: Sort the result based on a property. Accepts \"Name\", \"Size\", \"Author\", \"DownloadPriority\", \"IsRequired\", \"IsActive\", \"EffectiveDate\", \"ExpirationDate\", \"ModifiedOn\", or \"ModifiedBy\". By default it sorts by \"Name\"..
        :param bool sort_ascending: Sort direction. By default it sorts Ascending.
        :param int sort_index: Start index of page.
        :param int page_size: Specifies the number of results returned per Page.
        :return: AwContentPagedResultModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['locationgroupcode', 'locationgroupid', 'query_string', 'category_id', 'mime_type', 'expires_in', 'sort_by', 'sort_ascending', 'sort_index', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aw_contents_search_async" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'locationgroupcode' in params:
            query_params.append(('locationgroupcode', params['locationgroupcode']))  # noqa: E501
        if 'locationgroupid' in params:
            query_params.append(('locationgroupid', params['locationgroupid']))  # noqa: E501
        if 'query_string' in params:
            query_params.append(('queryString', params['query_string']))  # noqa: E501
        if 'category_id' in params:
            query_params.append(('categoryId', params['category_id']))  # noqa: E501
        if 'mime_type' in params:
            query_params.append(('mimeType', params['mime_type']))  # noqa: E501
        if 'expires_in' in params:
            query_params.append(('expiresIn', params['expires_in']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))  # noqa: E501
        if 'sort_ascending' in params:
            query_params.append(('sortAscending', params['sort_ascending']))  # noqa: E501
        if 'sort_index' in params:
            query_params.append(('sortIndex', params['sort_index']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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
        auth_settings = ['BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/awcontents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AwContentPagedResultModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aw_contents_update_file_metadata_async(self, id, model, **kwargs):  # noqa: E501
        """New - Update metadata for a Managed content.  # noqa: E501

        Update metadata for the specified managed content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_update_file_metadata_async(id, model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier of the file.(Required). (required)
        :param AwContentModel model: The json for updating the content metadata.(Required). (required)
        :return: AwContentModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aw_contents_update_file_metadata_async_with_http_info(id, model, **kwargs)  # noqa: E501
        else:
            (data) = self.aw_contents_update_file_metadata_async_with_http_info(id, model, **kwargs)  # noqa: E501
            return data

    def aw_contents_update_file_metadata_async_with_http_info(self, id, model, **kwargs):  # noqa: E501
        """New - Update metadata for a Managed content.  # noqa: E501

        Update metadata for the specified managed content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_update_file_metadata_async_with_http_info(id, model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier of the file.(Required). (required)
        :param AwContentModel model: The json for updating the content metadata.(Required). (required)
        :return: AwContentModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aw_contents_update_file_metadata_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `aw_contents_update_file_metadata_async`")  # noqa: E501
        # verify the required parameter 'model' is set
        if self.api_client.client_side_validation and ('model' not in params or
                                                       params['model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `model` when calling `aw_contents_update_file_metadata_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model' in params:
            body_params = params['model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/awcontents/{id}/info', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AwContentModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aw_contents_upload_file_async(self, file_name, category_id, effective_date, location_group_id, location_group_code, **kwargs):  # noqa: E501
        """New - Upload a Managed content.  # noqa: E501

        Uploads a file to specified OG.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_upload_file_async(file_name, category_id, effective_date, location_group_id, location_group_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_name: File name for the uploaded file.(Required) (required)
        :param object category_id: The category for the file.(Required) (required)
        :param datetime effective_date: The effective date for the file.(Required) (required)
        :param int location_group_id: The ID of the organization group.(Required) (required)
        :param str location_group_code: The group code of the organization group.(Required) (required)
        :return: AwContentModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aw_contents_upload_file_async_with_http_info(file_name, category_id, effective_date, location_group_id, location_group_code, **kwargs)  # noqa: E501
        else:
            (data) = self.aw_contents_upload_file_async_with_http_info(file_name, category_id, effective_date, location_group_id, location_group_code, **kwargs)  # noqa: E501
            return data

    def aw_contents_upload_file_async_with_http_info(self, file_name, category_id, effective_date, location_group_id, location_group_code, **kwargs):  # noqa: E501
        """New - Upload a Managed content.  # noqa: E501

        Uploads a file to specified OG.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aw_contents_upload_file_async_with_http_info(file_name, category_id, effective_date, location_group_id, location_group_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_name: File name for the uploaded file.(Required) (required)
        :param object category_id: The category for the file.(Required) (required)
        :param datetime effective_date: The effective date for the file.(Required) (required)
        :param int location_group_id: The ID of the organization group.(Required) (required)
        :param str location_group_code: The group code of the organization group.(Required) (required)
        :return: AwContentModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_name', 'category_id', 'effective_date', 'location_group_id', 'location_group_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aw_contents_upload_file_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if self.api_client.client_side_validation and ('file_name' not in params or
                                                       params['file_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_name` when calling `aw_contents_upload_file_async`")  # noqa: E501
        # verify the required parameter 'category_id' is set
        if self.api_client.client_side_validation and ('category_id' not in params or
                                                       params['category_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `category_id` when calling `aw_contents_upload_file_async`")  # noqa: E501
        # verify the required parameter 'effective_date' is set
        if self.api_client.client_side_validation and ('effective_date' not in params or
                                                       params['effective_date'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `effective_date` when calling `aw_contents_upload_file_async`")  # noqa: E501
        # verify the required parameter 'location_group_id' is set
        if self.api_client.client_side_validation and ('location_group_id' not in params or
                                                       params['location_group_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `location_group_id` when calling `aw_contents_upload_file_async`")  # noqa: E501
        # verify the required parameter 'location_group_code' is set
        if self.api_client.client_side_validation and ('location_group_code' not in params or
                                                       params['location_group_code'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `location_group_code` when calling `aw_contents_upload_file_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_name' in params:
            query_params.append(('fileName', params['file_name']))  # noqa: E501
        if 'category_id' in params:
            query_params.append(('categoryId', params['category_id']))  # noqa: E501
        if 'effective_date' in params:
            query_params.append(('effectiveDate', params['effective_date']))  # noqa: E501
        if 'location_group_id' in params:
            query_params.append(('locationGroupId', params['location_group_id']))  # noqa: E501
        if 'location_group_code' in params:
            query_params.append(('locationGroupCode', params['location_group_code']))  # noqa: E501

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
        auth_settings = ['BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/awcontents', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AwContentModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)