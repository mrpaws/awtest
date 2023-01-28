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


class ProfilesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def profiles_execute_install_profile_commands(self, id, payloads, **kwargs):  # noqa: E501
        """Installs the profile on device.  # noqa: E501

        Queues up installation commands for interactive profiles for a device by overriding payload settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiles_execute_install_profile_commands(id, payloads, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The device ID (Required). (required)
        :param list[PayloadModel] payloads: Array of payload bodies (Required). (required)
        :param int profileid: Profile id.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profiles_execute_install_profile_commands_with_http_info(id, payloads, **kwargs)  # noqa: E501
        else:
            (data) = self.profiles_execute_install_profile_commands_with_http_info(id, payloads, **kwargs)  # noqa: E501
            return data

    def profiles_execute_install_profile_commands_with_http_info(self, id, payloads, **kwargs):  # noqa: E501
        """Installs the profile on device.  # noqa: E501

        Queues up installation commands for interactive profiles for a device by overriding payload settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiles_execute_install_profile_commands_with_http_info(id, payloads, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The device ID (Required). (required)
        :param list[PayloadModel] payloads: Array of payload bodies (Required). (required)
        :param int profileid: Profile id.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'payloads', 'profileid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profiles_execute_install_profile_commands" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `profiles_execute_install_profile_commands`")  # noqa: E501
        # verify the required parameter 'payloads' is set
        if self.api_client.client_side_validation and ('payloads' not in params or
                                                       params['payloads'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `payloads` when calling `profiles_execute_install_profile_commands`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'profileid' in params:
            query_params.append(('profileid', params['profileid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payloads' in params:
            body_params = params['payloads']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1', 'application/xml;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{id}/commands/installprofile', 'POST',
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

    def profiles_get_profiles_by_alternate_id(self, **kwargs):  # noqa: E501
        """Retrieves the profile details of the device identified by alternate ID.  # noqa: E501

        Fetches all the profiles and details for the device identified by alternate ID other than device ID.  Alternate device identifiers can be MAC address, IMEI, Serial number or UDID.  Example : IMEI-BCG84753GH, Serial Number-573489754.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiles_get_profiles_by_alternate_id(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_by: The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber].
        :param str id: Device alternate id.
        :param int page: The specific page number to get.
        :param int pagesize: Max records per page.
        :return: DeviceProfileSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profiles_get_profiles_by_alternate_id_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.profiles_get_profiles_by_alternate_id_with_http_info(**kwargs)  # noqa: E501
            return data

    def profiles_get_profiles_by_alternate_id_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves the profile details of the device identified by alternate ID.  # noqa: E501

        Fetches all the profiles and details for the device identified by alternate ID other than device ID.  Alternate device identifiers can be MAC address, IMEI, Serial number or UDID.  Example : IMEI-BCG84753GH, Serial Number-573489754.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiles_get_profiles_by_alternate_id_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_by: The alternate id type [Macaddress, Udid, Serialnumber, ImeiNumber].
        :param str id: Device alternate id.
        :param int page: The specific page number to get.
        :param int pagesize: Max records per page.
        :return: DeviceProfileSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_by', 'id', 'page', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profiles_get_profiles_by_alternate_id" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_by' in params:
            query_params.append(('searchBy', params['search_by']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
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
            '/devices/profiles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceProfileSearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def profiles_get_profiles_by_device(self, id, **kwargs):  # noqa: E501
        """Retrieves the profile details of the device by Device ID.  # noqa: E501

        Fetches all the profiles and details for the device identified by device ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiles_get_profiles_by_device(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: DeviceID is the unique identifier for devices in AirWatch (Required). (required)
        :param int page: The specific page number to get.
        :param int pagesize: Max records per page.
        :return: DeviceProfileSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profiles_get_profiles_by_device_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.profiles_get_profiles_by_device_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def profiles_get_profiles_by_device_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves the profile details of the device by Device ID.  # noqa: E501

        Fetches all the profiles and details for the device identified by device ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiles_get_profiles_by_device_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: DeviceID is the unique identifier for devices in AirWatch (Required). (required)
        :param int page: The specific page number to get.
        :param int pagesize: Max records per page.
        :return: DeviceProfileSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profiles_get_profiles_by_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `profiles_get_profiles_by_device`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/devices/{id}/profiles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceProfileSearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
