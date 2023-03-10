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


class OemUpdatesSearchV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def oem_updates_search_v1_get_oem_updates_by_device_uuid_async(self, uuid, device_uuid, **kwargs):  # noqa: E501
        """New - Getting OEM updates for a device.  # noqa: E501

        Getting OEM updates for a device of a given device Uuid.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oem_updates_search_v1_get_oem_updates_by_device_uuid_async(uuid, device_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Organization group UUID to perform the operation on.(Required). (required)
        :param str device_uuid: Device UUID to perform the operation on.(Required). (required)
        :param str search_text: OemUpdate is searched on Name, Message, Criticality, Category and UpdateType
        :param int page_number: Specific page number to get. 0 based index.
        :param int page_size: Maximum number of records per page. Default value is 50.
        :param str sort_order: The order based on which we can sort, supported values are ASC, DESC. Default value is ASC.
        :param str sort_column: Column based on which we can provide the sorting.
        :param bool status: The installed status of the OEM update. Supported values true, and false.
        :return: OemUpdateDeviceSearchResultInfoV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oem_updates_search_v1_get_oem_updates_by_device_uuid_async_with_http_info(uuid, device_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.oem_updates_search_v1_get_oem_updates_by_device_uuid_async_with_http_info(uuid, device_uuid, **kwargs)  # noqa: E501
            return data

    def oem_updates_search_v1_get_oem_updates_by_device_uuid_async_with_http_info(self, uuid, device_uuid, **kwargs):  # noqa: E501
        """New - Getting OEM updates for a device.  # noqa: E501

        Getting OEM updates for a device of a given device Uuid.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oem_updates_search_v1_get_oem_updates_by_device_uuid_async_with_http_info(uuid, device_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Organization group UUID to perform the operation on.(Required). (required)
        :param str device_uuid: Device UUID to perform the operation on.(Required). (required)
        :param str search_text: OemUpdate is searched on Name, Message, Criticality, Category and UpdateType
        :param int page_number: Specific page number to get. 0 based index.
        :param int page_size: Maximum number of records per page. Default value is 50.
        :param str sort_order: The order based on which we can sort, supported values are ASC, DESC. Default value is ASC.
        :param str sort_column: Column based on which we can provide the sorting.
        :param bool status: The installed status of the OEM update. Supported values true, and false.
        :return: OemUpdateDeviceSearchResultInfoV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'device_uuid', 'search_text', 'page_number', 'page_size', 'sort_order', 'sort_column', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oem_updates_search_v1_get_oem_updates_by_device_uuid_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in params or
                                                       params['uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uuid` when calling `oem_updates_search_v1_get_oem_updates_by_device_uuid_async`")  # noqa: E501
        # verify the required parameter 'device_uuid' is set
        if self.api_client.client_side_validation and ('device_uuid' not in params or
                                                       params['device_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `device_uuid` when calling `oem_updates_search_v1_get_oem_updates_by_device_uuid_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501
        if 'device_uuid' in params:
            path_params['deviceUuid'] = params['device_uuid']  # noqa: E501

        query_params = []
        if 'search_text' in params:
            query_params.append(('search_text', params['search_text']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page_number', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort_order', params['sort_order']))  # noqa: E501
        if 'sort_column' in params:
            query_params.append(('sort_column', params['sort_column']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

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
            '/oem-updates/v1/groups/{uuid}/device/{deviceUuid}/updates-list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OemUpdateDeviceSearchResultInfoV1Model',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oem_updates_search_v1_get_summary_devices_async(self, uuid, release_id, version, status, **kwargs):  # noqa: E501
        """New - Gets the devices where OEM Update Summary is installed(status would be either failed or success).  # noqa: E501

        Returns the devices where the OEM Update is installed(status would be either failed or success).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oem_updates_search_v1_get_summary_devices_async(uuid, release_id, version, status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Organization group UUID to perform the operation on.(Required). (required)
        :param str release_id: Release identifier of the OEM update.(Required) (required)
        :param str version: Version of the OEM update.(Required) (required)
        :param bool status: The installed status of the OEM update.(Required). Supported values true, and false. (required)
        :param str search_text: OemUpdate is searched on Name, Message, Criticality, Category and UpdateType
        :param int page_number: Specific page number to get. 0 based index.
        :param int page_size: Maximum number of records per page. Default value is 50.
        :param str sort_order: The order based on which we can sort, supported values are ASC, DESC. Default value is ASC.
        :param str sort_column: Column based on which we can provide the sorting. Default OemupdateName(Example:OemupdateName, OemupdateCategory)
        :return: list[OemUpdateSummaryInstalledDeviceInfoResponseV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oem_updates_search_v1_get_summary_devices_async_with_http_info(uuid, release_id, version, status, **kwargs)  # noqa: E501
        else:
            (data) = self.oem_updates_search_v1_get_summary_devices_async_with_http_info(uuid, release_id, version, status, **kwargs)  # noqa: E501
            return data

    def oem_updates_search_v1_get_summary_devices_async_with_http_info(self, uuid, release_id, version, status, **kwargs):  # noqa: E501
        """New - Gets the devices where OEM Update Summary is installed(status would be either failed or success).  # noqa: E501

        Returns the devices where the OEM Update is installed(status would be either failed or success).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oem_updates_search_v1_get_summary_devices_async_with_http_info(uuid, release_id, version, status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Organization group UUID to perform the operation on.(Required). (required)
        :param str release_id: Release identifier of the OEM update.(Required) (required)
        :param str version: Version of the OEM update.(Required) (required)
        :param bool status: The installed status of the OEM update.(Required). Supported values true, and false. (required)
        :param str search_text: OemUpdate is searched on Name, Message, Criticality, Category and UpdateType
        :param int page_number: Specific page number to get. 0 based index.
        :param int page_size: Maximum number of records per page. Default value is 50.
        :param str sort_order: The order based on which we can sort, supported values are ASC, DESC. Default value is ASC.
        :param str sort_column: Column based on which we can provide the sorting. Default OemupdateName(Example:OemupdateName, OemupdateCategory)
        :return: list[OemUpdateSummaryInstalledDeviceInfoResponseV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'release_id', 'version', 'status', 'search_text', 'page_number', 'page_size', 'sort_order', 'sort_column']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oem_updates_search_v1_get_summary_devices_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in params or
                                                       params['uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uuid` when calling `oem_updates_search_v1_get_summary_devices_async`")  # noqa: E501
        # verify the required parameter 'release_id' is set
        if self.api_client.client_side_validation and ('release_id' not in params or
                                                       params['release_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `release_id` when calling `oem_updates_search_v1_get_summary_devices_async`")  # noqa: E501
        # verify the required parameter 'version' is set
        if self.api_client.client_side_validation and ('version' not in params or
                                                       params['version'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `version` when calling `oem_updates_search_v1_get_summary_devices_async`")  # noqa: E501
        # verify the required parameter 'status' is set
        if self.api_client.client_side_validation and ('status' not in params or
                                                       params['status'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `status` when calling `oem_updates_search_v1_get_summary_devices_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []
        if 'release_id' in params:
            query_params.append(('release_id', params['release_id']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'search_text' in params:
            query_params.append(('search_text', params['search_text']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page_number', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort_order', params['sort_order']))  # noqa: E501
        if 'sort_column' in params:
            query_params.append(('sort_column', params['sort_column']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

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
            '/oem-updates/v1/groups/{uuid}/summary/devices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OemUpdateSummaryInstalledDeviceInfoResponseV1Model]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oem_updates_search_v1_get_summary_status_async(self, uuid, release_id, version, **kwargs):  # noqa: E501
        """New - Gets the count of OemUpdate Summary installed in devices for a given release_id + version.  # noqa: E501

        It will return the summary with installed success and failed count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oem_updates_search_v1_get_summary_status_async(uuid, release_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Organization group UUID to perform the operation on.(Required). (required)
        :param str release_id: Release identifier of the OEM update.(Required) (required)
        :param str version: Version of the OEM update.(Required) (required)
        :return: list[OemUpdateSummaryInstalledStatusInfoResponseV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oem_updates_search_v1_get_summary_status_async_with_http_info(uuid, release_id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.oem_updates_search_v1_get_summary_status_async_with_http_info(uuid, release_id, version, **kwargs)  # noqa: E501
            return data

    def oem_updates_search_v1_get_summary_status_async_with_http_info(self, uuid, release_id, version, **kwargs):  # noqa: E501
        """New - Gets the count of OemUpdate Summary installed in devices for a given release_id + version.  # noqa: E501

        It will return the summary with installed success and failed count.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oem_updates_search_v1_get_summary_status_async_with_http_info(uuid, release_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Organization group UUID to perform the operation on.(Required). (required)
        :param str release_id: Release identifier of the OEM update.(Required) (required)
        :param str version: Version of the OEM update.(Required) (required)
        :return: list[OemUpdateSummaryInstalledStatusInfoResponseV1Model]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'release_id', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oem_updates_search_v1_get_summary_status_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in params or
                                                       params['uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uuid` when calling `oem_updates_search_v1_get_summary_status_async`")  # noqa: E501
        # verify the required parameter 'release_id' is set
        if self.api_client.client_side_validation and ('release_id' not in params or
                                                       params['release_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `release_id` when calling `oem_updates_search_v1_get_summary_status_async`")  # noqa: E501
        # verify the required parameter 'version' is set
        if self.api_client.client_side_validation and ('version' not in params or
                                                       params['version'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `version` when calling `oem_updates_search_v1_get_summary_status_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []
        if 'release_id' in params:
            query_params.append(('release_id', params['release_id']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501

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
            '/oem-updates/v1/groups/{uuid}/summary/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OemUpdateSummaryInstalledStatusInfoResponseV1Model]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oem_updates_search_v1_search_async(self, uuid, **kwargs):  # noqa: E501
        """New - Returns a collection of OemUpdateSummary details based on the search criteria.  # noqa: E501

        Returns a collection of OemUpdate summary details based on the search criteria specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oem_updates_search_v1_search_async(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Organization group UUID to perform the operation on.(Required). (required)
        :param str search_text: OemUpdate is searched on Name, Message, Criticality, Category and UpdateType
        :param int page_number: Specific page number to get. 0 based index.
        :param int page_size: Maximum number of records per page. Default value is 50.
        :param str sort_order: The order based on which we can sort, supported values are ASC, DESC. Default value is ASC.
        :param str sort_column: Column based on which we can provide the sorting. Default OemupdateName(Example:OemupdateName, OemupdateCategory)
        :return: OemUpdateSummarySearchResultInfoV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oem_updates_search_v1_search_async_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.oem_updates_search_v1_search_async_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def oem_updates_search_v1_search_async_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """New - Returns a collection of OemUpdateSummary details based on the search criteria.  # noqa: E501

        Returns a collection of OemUpdate summary details based on the search criteria specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oem_updates_search_v1_search_async_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Organization group UUID to perform the operation on.(Required). (required)
        :param str search_text: OemUpdate is searched on Name, Message, Criticality, Category and UpdateType
        :param int page_number: Specific page number to get. 0 based index.
        :param int page_size: Maximum number of records per page. Default value is 50.
        :param str sort_order: The order based on which we can sort, supported values are ASC, DESC. Default value is ASC.
        :param str sort_column: Column based on which we can provide the sorting. Default OemupdateName(Example:OemupdateName, OemupdateCategory)
        :return: OemUpdateSummarySearchResultInfoV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'search_text', 'page_number', 'page_size', 'sort_order', 'sort_column']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oem_updates_search_v1_search_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in params or
                                                       params['uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uuid` when calling `oem_updates_search_v1_search_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []
        if 'search_text' in params:
            query_params.append(('search_text', params['search_text']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page_number', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort_order', params['sort_order']))  # noqa: E501
        if 'sort_column' in params:
            query_params.append(('sort_column', params['sort_column']))  # noqa: E501

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
            '/oem-updates/v1/groups/{uuid}/summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OemUpdateSummarySearchResultInfoV1Model',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
