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


class TagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def tags_add_devices_to_tag_async(self, tagid, **kwargs):  # noqa: E501
        """Add devices to the tag.  # noqa: E501

        Associates the given tag to the set of devices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_add_devices_to_tag_async(tagid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tagid: Tag id. (required)
        :param BulkInput add_devices: Deviceids to be added to the tag.
        :return: BulkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tags_add_devices_to_tag_async_with_http_info(tagid, **kwargs)  # noqa: E501
        else:
            (data) = self.tags_add_devices_to_tag_async_with_http_info(tagid, **kwargs)  # noqa: E501
            return data

    def tags_add_devices_to_tag_async_with_http_info(self, tagid, **kwargs):  # noqa: E501
        """Add devices to the tag.  # noqa: E501

        Associates the given tag to the set of devices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_add_devices_to_tag_async_with_http_info(tagid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tagid: Tag id. (required)
        :param BulkInput add_devices: Deviceids to be added to the tag.
        :return: BulkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tagid', 'add_devices']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_add_devices_to_tag_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tagid' is set
        if self.api_client.client_side_validation and ('tagid' not in params or
                                                       params['tagid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tagid` when calling `tags_add_devices_to_tag_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tagid' in params:
            path_params['tagid'] = params['tagid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'add_devices' in params:
            body_params = params['add_devices']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tags/{tagid}/adddevices', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BulkResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tags_add_tag(self, **kwargs):  # noqa: E501
        """Add a new tag.  # noqa: E501

        Add a tag based on the details provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_add_tag(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagModel tag: Tag information.
        :return: EntityId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tags_add_tag_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.tags_add_tag_with_http_info(**kwargs)  # noqa: E501
            return data

    def tags_add_tag_with_http_info(self, **kwargs):  # noqa: E501
        """Add a new tag.  # noqa: E501

        Add a tag based on the details provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_add_tag_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagModel tag: Tag information.
        :return: EntityId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_add_tag" % key
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
        if 'tag' in params:
            body_params = params['tag']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tags/addtag', 'POST',
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

    def tags_delete_tag_async(self, tag_id, **kwargs):  # noqa: E501
        """Delete a tag.  # noqa: E501

        Delete a tag based on tag identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_delete_tag_async(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tag_id: The tag ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tags_delete_tag_async_with_http_info(tag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.tags_delete_tag_async_with_http_info(tag_id, **kwargs)  # noqa: E501
            return data

    def tags_delete_tag_async_with_http_info(self, tag_id, **kwargs):  # noqa: E501
        """Delete a tag.  # noqa: E501

        Delete a tag based on tag identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_delete_tag_async_with_http_info(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tag_id: The tag ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_delete_tag_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_id' is set
        if self.api_client.client_side_validation and ('tag_id' not in params or
                                                       params['tag_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tag_id` when calling `tags_delete_tag_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']  # noqa: E501

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
            '/tags/{tagId}', 'DELETE',
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

    def tags_devices_for_tag_async(self, tag_id, **kwargs):  # noqa: E501
        """Retrieves all the devices with the specified tag.  # noqa: E501

        Retrieves the list of devices that have the specified input tag assinged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_devices_for_tag_async(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tag_id: Tag identifier. (required)
        :param datetime last_seen: Date Last Seen.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tags_devices_for_tag_async_with_http_info(tag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.tags_devices_for_tag_async_with_http_info(tag_id, **kwargs)  # noqa: E501
            return data

    def tags_devices_for_tag_async_with_http_info(self, tag_id, **kwargs):  # noqa: E501
        """Retrieves all the devices with the specified tag.  # noqa: E501

        Retrieves the list of devices that have the specified input tag assinged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_devices_for_tag_async_with_http_info(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tag_id: Tag identifier. (required)
        :param datetime last_seen: Date Last Seen.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id', 'last_seen']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_devices_for_tag_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_id' is set
        if self.api_client.client_side_validation and ('tag_id' not in params or
                                                       params['tag_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tag_id` when calling `tags_devices_for_tag_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']  # noqa: E501

        query_params = []
        if 'last_seen' in params:
            query_params.append(('lastSeen', params['last_seen']))  # noqa: E501

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
            '/tags/{tagId}/devices', 'GET',
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

    def tags_remove_devices_from_tag_async(self, tagid, **kwargs):  # noqa: E501
        """Remove devices from the tag.  # noqa: E501

        Remove devices from tag based on the tag identifier and devices to be removed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_remove_devices_from_tag_async(tagid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tagid: Tag id. (required)
        :param BulkInput remove_devices: Deviceids to be removed from tag.
        :return: BulkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tags_remove_devices_from_tag_async_with_http_info(tagid, **kwargs)  # noqa: E501
        else:
            (data) = self.tags_remove_devices_from_tag_async_with_http_info(tagid, **kwargs)  # noqa: E501
            return data

    def tags_remove_devices_from_tag_async_with_http_info(self, tagid, **kwargs):  # noqa: E501
        """Remove devices from the tag.  # noqa: E501

        Remove devices from tag based on the tag identifier and devices to be removed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_remove_devices_from_tag_async_with_http_info(tagid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tagid: Tag id. (required)
        :param BulkInput remove_devices: Deviceids to be removed from tag.
        :return: BulkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tagid', 'remove_devices']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_remove_devices_from_tag_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tagid' is set
        if self.api_client.client_side_validation and ('tagid' not in params or
                                                       params['tagid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tagid` when calling `tags_remove_devices_from_tag_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tagid' in params:
            path_params['tagid'] = params['tagid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'remove_devices' in params:
            body_params = params['remove_devices']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tags/{tagid}/removedevices', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BulkResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tags_update_tag(self, tag_id, **kwargs):  # noqa: E501
        """Updates a tag name, tag type or tag avatar.  # noqa: E501

        Updates a tag based on the tag identifier and tag details. This API can be used to update the tag name, tag type and tag avatar.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_update_tag(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tag_id: Unique identifier for the tag. (required)
        :param TagModel tag: Tag details that needs to be updated.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tags_update_tag_with_http_info(tag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.tags_update_tag_with_http_info(tag_id, **kwargs)  # noqa: E501
            return data

    def tags_update_tag_with_http_info(self, tag_id, **kwargs):  # noqa: E501
        """Updates a tag name, tag type or tag avatar.  # noqa: E501

        Updates a tag based on the tag identifier and tag details. This API can be used to update the tag name, tag type and tag avatar.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_update_tag_with_http_info(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tag_id: Unique identifier for the tag. (required)
        :param TagModel tag: Tag details that needs to be updated.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id', 'tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_update_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_id' is set
        if self.api_client.client_side_validation and ('tag_id' not in params or
                                                       params['tag_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tag_id` when calling `tags_update_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tag' in params:
            body_params = params['tag']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tags/{tagId}/update', 'POST',
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
