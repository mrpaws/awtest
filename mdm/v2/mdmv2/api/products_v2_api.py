# coding: utf-8

"""
    MDM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mdmv2.api_client import ApiClient


class ProductsV2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def products_v2_assigned_product_devices_async(self, id, **kwargs):  # noqa: E501
        """Returns the details of the Device for which Provisioning is Assigned.  # noqa: E501

        Returns the details of the Device for which Provisioning is Assigned.<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_v2_assigned_product_devices_async(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identfier of the Product(Required). (required)
        :param datetime seensince: Filters devices such that devices with last seen after this date will be returned.              Valid DateTime formats includes as below:              yyyy/MM/dd,yyyy-MM-dd,MM/dd/yyyy,MM-dd-yyyy,              yyyy/MM/dd HH:mm:ss.fff,yyyy-MM-dd HH:mm:ss.fff,              MM/dd/yyyy HH:mm:ss.fff,MM-dd-yyyy HH:mm:ss.fff,              yyyy/MM/ddTHH:mm:ss.fff,yyyy-MM-ddTHH:mm:ss.fff,              MM/dd/yyyyTHH:mm:ss.fff,MM-dd-yyyyTHH:mm:ss.fff,              yyyy-MM-dd HH-mm-ss-tt,yyyy-MM-ddTHH-mm-ss-tt.
        :param datetime lastjobupdatefrom: Filters devices on lastjobstatus DateTime.              Valid DateTime formats includes as below:              yyyy/MM/dd,yyyy-MM-dd,MM/dd/yyyy,MM-dd-yyyy,              yyyy/MM/dd HH:mm:ss.fff,yyyy-MM-dd HH:mm:ss.fff,              MM/dd/yyyy HH:mm:ss.fff,MM-dd-yyyy HH:mm:ss.fff,              yyyy/MM/ddTHH:mm:ss.fff,yyyy-MM-ddTHH:mm:ss.fff,              MM/dd/yyyyTHH:mm:ss.fff,MM-dd-yyyyTHH:mm:ss.fff,              yyyy-MM-dd HH-mm-ss-tt,yyyy-MM-ddTHH-mm-ss-tt.
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :return: ProductDeviceDetailsSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_v2_assigned_product_devices_async_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.products_v2_assigned_product_devices_async_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def products_v2_assigned_product_devices_async_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns the details of the Device for which Provisioning is Assigned.  # noqa: E501

        Returns the details of the Device for which Provisioning is Assigned.<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_v2_assigned_product_devices_async_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identfier of the Product(Required). (required)
        :param datetime seensince: Filters devices such that devices with last seen after this date will be returned.              Valid DateTime formats includes as below:              yyyy/MM/dd,yyyy-MM-dd,MM/dd/yyyy,MM-dd-yyyy,              yyyy/MM/dd HH:mm:ss.fff,yyyy-MM-dd HH:mm:ss.fff,              MM/dd/yyyy HH:mm:ss.fff,MM-dd-yyyy HH:mm:ss.fff,              yyyy/MM/ddTHH:mm:ss.fff,yyyy-MM-ddTHH:mm:ss.fff,              MM/dd/yyyyTHH:mm:ss.fff,MM-dd-yyyyTHH:mm:ss.fff,              yyyy-MM-dd HH-mm-ss-tt,yyyy-MM-ddTHH-mm-ss-tt.
        :param datetime lastjobupdatefrom: Filters devices on lastjobstatus DateTime.              Valid DateTime formats includes as below:              yyyy/MM/dd,yyyy-MM-dd,MM/dd/yyyy,MM-dd-yyyy,              yyyy/MM/dd HH:mm:ss.fff,yyyy-MM-dd HH:mm:ss.fff,              MM/dd/yyyy HH:mm:ss.fff,MM-dd-yyyy HH:mm:ss.fff,              yyyy/MM/ddTHH:mm:ss.fff,yyyy-MM-ddTHH:mm:ss.fff,              MM/dd/yyyyTHH:mm:ss.fff,MM-dd-yyyyTHH:mm:ss.fff,              yyyy-MM-dd HH-mm-ss-tt,yyyy-MM-ddTHH-mm-ss-tt.
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :return: ProductDeviceDetailsSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'seensince', 'lastjobupdatefrom', 'page', 'pagesize']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method products_v2_assigned_product_devices_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `products_v2_assigned_product_devices_async`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'seensince' in params:
            query_params.append(('seensince', params['seensince']))  # noqa: E501
        if 'lastjobupdatefrom' in params:
            query_params.append(('lastjobupdatefrom', params['lastjobupdatefrom']))  # noqa: E501
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
            ['application/json;version=2', 'application/xml;version=2'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/products/{id}/assigned', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductDeviceDetailsSearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def products_v2_failed_product_devices_async(self, id, **kwargs):  # noqa: E501
        """Returns the details of the Device for which Provisioning is Failed.  # noqa: E501

        Returns the details of the Devices for which Provisioning is Failed<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_v2_failed_product_devices_async(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required). (required)
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :return: ProductDeviceDetailsSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_v2_failed_product_devices_async_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.products_v2_failed_product_devices_async_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def products_v2_failed_product_devices_async_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns the details of the Device for which Provisioning is Failed.  # noqa: E501

        Returns the details of the Devices for which Provisioning is Failed<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_v2_failed_product_devices_async_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required). (required)
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :return: ProductDeviceDetailsSearchResult
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
                    " to method products_v2_failed_product_devices_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `products_v2_failed_product_devices_async`")  # noqa: E501

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
            ['application/json;version=2', 'application/xml;version=2'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/products/{id}/failed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductDeviceDetailsSearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def products_v2_inprogress_product_devices_async(self, id, **kwargs):  # noqa: E501
        """Returns the details of the Device for which Provisioning is In-Progress.  # noqa: E501

        Returns the details of the Devices which provisioning is in-progress.<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_v2_inprogress_product_devices_async(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required). (required)
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum results which should be returned in each page.
        :return: ProductDeviceDetailsSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_v2_inprogress_product_devices_async_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.products_v2_inprogress_product_devices_async_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def products_v2_inprogress_product_devices_async_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns the details of the Device for which Provisioning is In-Progress.  # noqa: E501

        Returns the details of the Devices which provisioning is in-progress.<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_v2_inprogress_product_devices_async_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required). (required)
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum results which should be returned in each page.
        :return: ProductDeviceDetailsSearchResult
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
                    " to method products_v2_inprogress_product_devices_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `products_v2_inprogress_product_devices_async`")  # noqa: E501

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
            ['application/json;version=2', 'application/xml;version=2'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/products/{id}/inprogress', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductDeviceDetailsSearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def products_v2_product_compliant_devices_async(self, id, **kwargs):  # noqa: E501
        """Returns the details of the Devices which are Product Compliant .  # noqa: E501

        Returns the details of the Devices which are Product Compliant<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_v2_product_compliant_devices_async(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required). (required)
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :return: ProductDeviceDetailsSearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_v2_product_compliant_devices_async_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.products_v2_product_compliant_devices_async_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def products_v2_product_compliant_devices_async_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns the details of the Devices which are Product Compliant .  # noqa: E501

        Returns the details of the Devices which are Product Compliant<br />              Device details includes <br />              DeviceID,<br />              Name,<br />              LastJobStatus,<br />              LastSeen.<br />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_v2_product_compliant_devices_async_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identfier of the Product of which ProductCompliant Device details needs to be retrieved(Required). (required)
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :return: ProductDeviceDetailsSearchResult
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
                    " to method products_v2_product_compliant_devices_async" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `products_v2_product_compliant_devices_async`")  # noqa: E501

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
            ['application/json;version=2', 'application/xml;version=2'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/products/{id}/compliant', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductDeviceDetailsSearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)