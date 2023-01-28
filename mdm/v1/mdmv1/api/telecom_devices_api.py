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


class TelecomDevicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def telecom_devices_search_cell_card_daily_usage_history_by_device_async(self, **kwargs):  # noqa: E501
        """Searches for telecom device usage history by device using the query information provided.  # noqa: E501

        Searches for telecom device usage history based on the Organization Group ID, Alternate Id, Phone Number, Start Date, End Date.  <br />  *startdate and enddate* fields accept the following  Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.telecom_devices_search_cell_card_daily_usage_history_by_device_async(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organizationgroupid: Organization Group ID.
        :param str search_by: The Alternate ID type; possible values: [Macaddress, UdId, Serialnumber, ImeiNumber, EasId, DeviceId].(Formats: Macaddress: 848506B900BA, UdId: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 499NCV2JH55N5CUTR2D27GG42, DeviceId: 12345).
        :param int id: Device Alternate ID.
        :param str phonenumber: Search by device phone number.
        :param datetime startdate: Search by start date.
        :param datetime enddate: Search by end date.
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :param str orderby: Orderby column name.
        :param str sortorder: Sorting order. Values ASC or DESC. Defaults to ASC.
        :return: CellCardDailyUsagePagedSearchResultModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.telecom_devices_search_cell_card_daily_usage_history_by_device_async_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.telecom_devices_search_cell_card_daily_usage_history_by_device_async_with_http_info(**kwargs)  # noqa: E501
            return data

    def telecom_devices_search_cell_card_daily_usage_history_by_device_async_with_http_info(self, **kwargs):  # noqa: E501
        """Searches for telecom device usage history by device using the query information provided.  # noqa: E501

        Searches for telecom device usage history based on the Organization Group ID, Alternate Id, Phone Number, Start Date, End Date.  <br />  *startdate and enddate* fields accept the following  Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.telecom_devices_search_cell_card_daily_usage_history_by_device_async_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organizationgroupid: Organization Group ID.
        :param str search_by: The Alternate ID type; possible values: [Macaddress, UdId, Serialnumber, ImeiNumber, EasId, DeviceId].(Formats: Macaddress: 848506B900BA, UdId: 6bf0f04c73681fbecfc3eb4f13cbf05b, SerialNumber: LGH871c18f631a, ImeiNumber: 354833052322837, EasId: 499NCV2JH55N5CUTR2D27GG42, DeviceId: 12345).
        :param int id: Device Alternate ID.
        :param str phonenumber: Search by device phone number.
        :param datetime startdate: Search by start date.
        :param datetime enddate: Search by end date.
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :param str orderby: Orderby column name.
        :param str sortorder: Sorting order. Values ASC or DESC. Defaults to ASC.
        :return: CellCardDailyUsagePagedSearchResultModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizationgroupid', 'search_by', 'id', 'phonenumber', 'startdate', 'enddate', 'page', 'pagesize', 'orderby', 'sortorder']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method telecom_devices_search_cell_card_daily_usage_history_by_device_async" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organizationgroupid' in params:
            query_params.append(('organizationgroupid', params['organizationgroupid']))  # noqa: E501
        if 'search_by' in params:
            query_params.append(('searchBy', params['search_by']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'phonenumber' in params:
            query_params.append(('phonenumber', params['phonenumber']))  # noqa: E501
        if 'startdate' in params:
            query_params.append(('startdate', params['startdate']))  # noqa: E501
        if 'enddate' in params:
            query_params.append(('enddate', params['enddate']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'pagesize' in params:
            query_params.append(('pagesize', params['pagesize']))  # noqa: E501
        if 'orderby' in params:
            query_params.append(('orderby', params['orderby']))  # noqa: E501
        if 'sortorder' in params:
            query_params.append(('sortorder', params['sortorder']))  # noqa: E501

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
            '/telecom/devices/usagehistory', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CellCardDailyUsagePagedSearchResultModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async(self, **kwargs):  # noqa: E501
        """Searches for telecom device usage history in bulk by Organization Group using the query information provided.  # noqa: E501

        Searches for telecom device usage history in bulk based on the Organization Group ID and Date.  <br />  date* field accepts the following  Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organizationgroupid: Search by Organization Group ID.
        :param object _date: Search by date, if not provided current UTC date will be considered.
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :param str orderby: Orderby column name.
        :param str sortorder: Sorting order. Values ASC or DESC. Defaults to ASC.
        :return: CellCardDailyUsagePagedSearchResultModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async_with_http_info(**kwargs)  # noqa: E501
            return data

    def telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async_with_http_info(self, **kwargs):  # noqa: E501
        """Searches for telecom device usage history in bulk by Organization Group using the query information provided.  # noqa: E501

        Searches for telecom device usage history in bulk based on the Organization Group ID and Date.  <br />  date* field accepts the following  Valid DateTime formats : yyyy/MM/dd, yyyy-MM-dd, MM/dd/yyyy, MM-dd-yyyy, yyyy/MM/dd HH:mm:ss.fff,  yyyy-MM-dd HH:mm:ss.fff, MM/dd/yyyy HH:mm:ss.fff, MM-dd-yyyy HH:mm:ss.fff, yyyy/MM/ddTHH:mm:ss.fff,  yyyy-MM-ddTHH:mm:ss.fff, MM/dd/yyyyTHH:mm:ss.fff, MM-dd-yyyyTHH:mm:ss.fff, yyyy-MM-dd HH-mm-ss-tt, yyyy-MM-ddTHH-mm-ss-tt.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organizationgroupid: Search by Organization Group ID.
        :param object _date: Search by date, if not provided current UTC date will be considered.
        :param int page: Specific page number to get. 0 based index.
        :param int pagesize: Maximum records per page. Default 500.
        :param str orderby: Orderby column name.
        :param str sortorder: Sorting order. Values ASC or DESC. Defaults to ASC.
        :return: CellCardDailyUsagePagedSearchResultModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizationgroupid', '_date', 'page', 'pagesize', 'orderby', 'sortorder']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method telecom_devices_search_cell_card_daily_usage_history_by_organization_group_async" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organizationgroupid' in params:
            query_params.append(('organizationgroupid', params['organizationgroupid']))  # noqa: E501
        if '_date' in params:
            query_params.append(('date', params['_date']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'pagesize' in params:
            query_params.append(('pagesize', params['pagesize']))  # noqa: E501
        if 'orderby' in params:
            query_params.append(('orderby', params['orderby']))  # noqa: E501
        if 'sortorder' in params:
            query_params.append(('sortorder', params['sortorder']))  # noqa: E501

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
            '/telecom/devices/bulkusagehistory', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CellCardDailyUsagePagedSearchResultModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)