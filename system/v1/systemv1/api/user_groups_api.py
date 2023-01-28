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


class UserGroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def user_groups_add_user_to_user_group_async(self, usergroupid, enrollmentuserid, **kwargs):  # noqa: E501
        """Adds the user to custom User Group.  # noqa: E501

        Adds user to custom User Group based on its enrollment user id and user group id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_add_user_to_user_group_async(usergroupid, enrollmentuserid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int usergroupid: User Group identifier (Required). (required)
        :param int enrollmentuserid: Enrollment user identifier (Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_groups_add_user_to_user_group_async_with_http_info(usergroupid, enrollmentuserid, **kwargs)  # noqa: E501
        else:
            (data) = self.user_groups_add_user_to_user_group_async_with_http_info(usergroupid, enrollmentuserid, **kwargs)  # noqa: E501
            return data

    def user_groups_add_user_to_user_group_async_with_http_info(self, usergroupid, enrollmentuserid, **kwargs):  # noqa: E501
        """Adds the user to custom User Group.  # noqa: E501

        Adds user to custom User Group based on its enrollment user id and user group id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_add_user_to_user_group_async_with_http_info(usergroupid, enrollmentuserid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int usergroupid: User Group identifier (Required). (required)
        :param int enrollmentuserid: Enrollment user identifier (Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['usergroupid', 'enrollmentuserid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_groups_add_user_to_user_group_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'usergroupid' is set
        if self.api_client.client_side_validation and ('usergroupid' not in params or
                                                       params['usergroupid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `usergroupid` when calling `user_groups_add_user_to_user_group_async`")  # noqa: E501
        # verify the required parameter 'enrollmentuserid' is set
        if self.api_client.client_side_validation and ('enrollmentuserid' not in params or
                                                       params['enrollmentuserid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `enrollmentuserid` when calling `user_groups_add_user_to_user_group_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'usergroupid' in params:
            path_params['usergroupid'] = params['usergroupid']  # noqa: E501
        if 'enrollmentuserid' in params:
            path_params['enrollmentuserid'] = params['enrollmentuserid']  # noqa: E501

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
            '/usergroups/{usergroupid}/user/{enrollmentuserid}/addusertogroup', 'POST',
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

    def user_groups_create_custom_user_group(self, usergroup, **kwargs):  # noqa: E501
        """Creates a Custom User Group.  # noqa: E501

        Creates a custom User Group using request body containing group name, description, and the id of the              organization group that will manage the User Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_create_custom_user_group(usergroup, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserGroup usergroup: The custom User Group resource (Required). (required)
        :return: EntityIdModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_groups_create_custom_user_group_with_http_info(usergroup, **kwargs)  # noqa: E501
        else:
            (data) = self.user_groups_create_custom_user_group_with_http_info(usergroup, **kwargs)  # noqa: E501
            return data

    def user_groups_create_custom_user_group_with_http_info(self, usergroup, **kwargs):  # noqa: E501
        """Creates a Custom User Group.  # noqa: E501

        Creates a custom User Group using request body containing group name, description, and the id of the              organization group that will manage the User Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_create_custom_user_group_with_http_info(usergroup, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserGroup usergroup: The custom User Group resource (Required). (required)
        :return: EntityIdModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['usergroup']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_groups_create_custom_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'usergroup' is set
        if self.api_client.client_side_validation and ('usergroup' not in params or
                                                       params['usergroup'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `usergroup` when calling `user_groups_create_custom_user_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'usergroup' in params:
            body_params = params['usergroup']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/usergroups/createcustomusergroup', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EntityIdModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_groups_delete_user_group_id_users(self, usergroupid, **kwargs):  # noqa: E501
        """Delete custom User Group.  # noqa: E501

        Deletes a custom User Group based on the user group id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_delete_user_group_id_users(usergroupid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int usergroupid: User Group Identifier (Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_groups_delete_user_group_id_users_with_http_info(usergroupid, **kwargs)  # noqa: E501
        else:
            (data) = self.user_groups_delete_user_group_id_users_with_http_info(usergroupid, **kwargs)  # noqa: E501
            return data

    def user_groups_delete_user_group_id_users_with_http_info(self, usergroupid, **kwargs):  # noqa: E501
        """Delete custom User Group.  # noqa: E501

        Deletes a custom User Group based on the user group id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_delete_user_group_id_users_with_http_info(usergroupid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int usergroupid: User Group Identifier (Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['usergroupid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_groups_delete_user_group_id_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'usergroupid' is set
        if self.api_client.client_side_validation and ('usergroupid' not in params or
                                                       params['usergroupid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `usergroupid` when calling `user_groups_delete_user_group_id_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'usergroupid' in params:
            path_params['usergroupid'] = params['usergroupid']  # noqa: E501

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
            '/usergroups/{usergroupid}/delete', 'DELETE',
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

    def user_groups_remove_user_from_user_group_async(self, usergroupid, enrollmentuserid, **kwargs):  # noqa: E501
        """Removes the user from custom User Group.  # noqa: E501

        Removes the user from custom User Group based on its enrollment user id and user group id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_remove_user_from_user_group_async(usergroupid, enrollmentuserid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int usergroupid: User group identifier (Required). (required)
        :param int enrollmentuserid: Enrollment user identifier (Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_groups_remove_user_from_user_group_async_with_http_info(usergroupid, enrollmentuserid, **kwargs)  # noqa: E501
        else:
            (data) = self.user_groups_remove_user_from_user_group_async_with_http_info(usergroupid, enrollmentuserid, **kwargs)  # noqa: E501
            return data

    def user_groups_remove_user_from_user_group_async_with_http_info(self, usergroupid, enrollmentuserid, **kwargs):  # noqa: E501
        """Removes the user from custom User Group.  # noqa: E501

        Removes the user from custom User Group based on its enrollment user id and user group id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_remove_user_from_user_group_async_with_http_info(usergroupid, enrollmentuserid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int usergroupid: User group identifier (Required). (required)
        :param int enrollmentuserid: Enrollment user identifier (Required). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['usergroupid', 'enrollmentuserid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_groups_remove_user_from_user_group_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'usergroupid' is set
        if self.api_client.client_side_validation and ('usergroupid' not in params or
                                                       params['usergroupid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `usergroupid` when calling `user_groups_remove_user_from_user_group_async`")  # noqa: E501
        # verify the required parameter 'enrollmentuserid' is set
        if self.api_client.client_side_validation and ('enrollmentuserid' not in params or
                                                       params['enrollmentuserid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `enrollmentuserid` when calling `user_groups_remove_user_from_user_group_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'usergroupid' in params:
            path_params['usergroupid'] = params['usergroupid']  # noqa: E501
        if 'enrollmentuserid' in params:
            path_params['enrollmentuserid'] = params['enrollmentuserid']  # noqa: E501

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
            '/usergroups/{usergroupid}/user/{enrollmentuserid}/removeuserfromgroup', 'POST',
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

    def user_groups_retrieve_user_group_id_users(self, usergroupid, **kwargs):  # noqa: E501
        """Retrieves list of users from provided custom user group id.  # noqa: E501

        Retrieves a list of users that are members of custom User Group based on the user group id and a request query containing              page number and page size.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_retrieve_user_group_id_users(usergroupid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int usergroupid: User Group Identifier (Required). (required)
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :return: UserGroupUsers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_groups_retrieve_user_group_id_users_with_http_info(usergroupid, **kwargs)  # noqa: E501
        else:
            (data) = self.user_groups_retrieve_user_group_id_users_with_http_info(usergroupid, **kwargs)  # noqa: E501
            return data

    def user_groups_retrieve_user_group_id_users_with_http_info(self, usergroupid, **kwargs):  # noqa: E501
        """Retrieves list of users from provided custom user group id.  # noqa: E501

        Retrieves a list of users that are members of custom User Group based on the user group id and a request query containing              page number and page size.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_retrieve_user_group_id_users_with_http_info(usergroupid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int usergroupid: User Group Identifier (Required). (required)
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :return: UserGroupUsers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['usergroupid', 'page', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_groups_retrieve_user_group_id_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'usergroupid' is set
        if self.api_client.client_side_validation and ('usergroupid' not in params or
                                                       params['usergroupid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `usergroupid` when calling `user_groups_retrieve_user_group_id_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'usergroupid' in params:
            path_params['usergroupid'] = params['usergroupid']  # noqa: E501

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
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/usergroups/{usergroupid}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserGroupUsers',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_groups_search(self, **kwargs):  # noqa: E501
        """Search User Groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str groupname: Name of the group.
        :param int organizationgroupid: Organization Group Identifier.
        :param str usergrouptype: User Group Type.
        :param str syncstatus: Sync Status of the User Group.
        :param str mergestatus: Merge Status of the User Group.
        :param int page: It specifies the page number.
        :param int pagesize: Maximum records per page.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_groups_search_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.user_groups_search_with_http_info(**kwargs)  # noqa: E501
            return data

    def user_groups_search_with_http_info(self, **kwargs):  # noqa: E501
        """Search User Groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str groupname: Name of the group.
        :param int organizationgroupid: Organization Group Identifier.
        :param str usergrouptype: User Group Type.
        :param str syncstatus: Sync Status of the User Group.
        :param str mergestatus: Merge Status of the User Group.
        :param int page: It specifies the page number.
        :param int pagesize: Maximum records per page.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['groupname', 'organizationgroupid', 'usergrouptype', 'syncstatus', 'mergestatus', 'page', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_groups_search" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'groupname' in params:
            query_params.append(('groupname', params['groupname']))  # noqa: E501
        if 'organizationgroupid' in params:
            query_params.append(('organizationgroupid', params['organizationgroupid']))  # noqa: E501
        if 'usergrouptype' in params:
            query_params.append(('usergrouptype', params['usergrouptype']))  # noqa: E501
        if 'syncstatus' in params:
            query_params.append(('syncstatus', params['syncstatus']))  # noqa: E501
        if 'mergestatus' in params:
            query_params.append(('mergestatus', params['mergestatus']))  # noqa: E501
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
            '/usergroups/search', 'GET',
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

    def user_groups_search_user_group(self, groupname, **kwargs):  # noqa: E501
        """Search custom User Group with given parameters.  # noqa: E501

        Search for a custom User Group with given request query containing the following parameters:              the group name, the organizaiton group identifier, page number, and page size.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_search_user_group(groupname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str groupname: Name of User Group (Required). (required)
        :param int organizationgroupid: Organization Group Identifier.
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :return: UserGroups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_groups_search_user_group_with_http_info(groupname, **kwargs)  # noqa: E501
        else:
            (data) = self.user_groups_search_user_group_with_http_info(groupname, **kwargs)  # noqa: E501
            return data

    def user_groups_search_user_group_with_http_info(self, groupname, **kwargs):  # noqa: E501
        """Search custom User Group with given parameters.  # noqa: E501

        Search for a custom User Group with given request query containing the following parameters:              the group name, the organizaiton group identifier, page number, and page size.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_groups_search_user_group_with_http_info(groupname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str groupname: Name of User Group (Required). (required)
        :param int organizationgroupid: Organization Group Identifier.
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :return: UserGroups
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['groupname', 'organizationgroupid', 'page', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_groups_search_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'groupname' is set
        if self.api_client.client_side_validation and ('groupname' not in params or
                                                       params['groupname'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `groupname` when calling `user_groups_search_user_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'groupname' in params:
            query_params.append(('groupname', params['groupname']))  # noqa: E501
        if 'organizationgroupid' in params:
            query_params.append(('organizationgroupid', params['organizationgroupid']))  # noqa: E501
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
            '/usergroups/custom/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserGroups',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
