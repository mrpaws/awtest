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


class DeviceSensorsV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def device_sensors_v1_assign_device_sensor(self, assignment_model, **kwargs):  # noqa: E501
        """New - Assign device sensors to smart groups.  # noqa: E501

        Device sensor to smart group assignment map.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_assign_device_sensor(assignment_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceSensorSmartGroupAssignmentV1Model assignment_model: Model to map the assignment for device sensors and smart groups.(Required) (required)
        :return: DeviceSensorSmartGroupAssignmentResponseV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_sensors_v1_assign_device_sensor_with_http_info(assignment_model, **kwargs)  # noqa: E501
        else:
            (data) = self.device_sensors_v1_assign_device_sensor_with_http_info(assignment_model, **kwargs)  # noqa: E501
            return data

    def device_sensors_v1_assign_device_sensor_with_http_info(self, assignment_model, **kwargs):  # noqa: E501
        """New - Assign device sensors to smart groups.  # noqa: E501

        Device sensor to smart group assignment map.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_assign_device_sensor_with_http_info(assignment_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceSensorSmartGroupAssignmentV1Model assignment_model: Model to map the assignment for device sensors and smart groups.(Required) (required)
        :return: DeviceSensorSmartGroupAssignmentResponseV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assignment_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_sensors_v1_assign_device_sensor" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assignment_model' is set
        if self.api_client.client_side_validation and ('assignment_model' not in params or
                                                       params['assignment_model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `assignment_model` when calling `device_sensors_v1_assign_device_sensor`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'assignment_model' in params:
            body_params = params['assignment_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/devicesensors/assign', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceSensorSmartGroupAssignmentResponseV1Model',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def device_sensors_v1_bulk_delete_device_sensors(self, bulk_delete_request_v1_model, **kwargs):  # noqa: E501
        """New - Deletes the list of device sensors based on the identifiers provided.  # noqa: E501

        This API is used to delete the list of device sensors attribute and attribute details along with the associated assignments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_bulk_delete_device_sensors(bulk_delete_request_v1_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceSensorsBulkDeleteRequestV1Model bulk_delete_request_v1_model: (Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_sensors_v1_bulk_delete_device_sensors_with_http_info(bulk_delete_request_v1_model, **kwargs)  # noqa: E501
        else:
            (data) = self.device_sensors_v1_bulk_delete_device_sensors_with_http_info(bulk_delete_request_v1_model, **kwargs)  # noqa: E501
            return data

    def device_sensors_v1_bulk_delete_device_sensors_with_http_info(self, bulk_delete_request_v1_model, **kwargs):  # noqa: E501
        """New - Deletes the list of device sensors based on the identifiers provided.  # noqa: E501

        This API is used to delete the list of device sensors attribute and attribute details along with the associated assignments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_bulk_delete_device_sensors_with_http_info(bulk_delete_request_v1_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceSensorsBulkDeleteRequestV1Model bulk_delete_request_v1_model: (Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bulk_delete_request_v1_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_sensors_v1_bulk_delete_device_sensors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bulk_delete_request_v1_model' is set
        if self.api_client.client_side_validation and ('bulk_delete_request_v1_model' not in params or
                                                       params['bulk_delete_request_v1_model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bulk_delete_request_v1_model` when calling `device_sensors_v1_bulk_delete_device_sensors`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bulk_delete_request_v1_model' in params:
            body_params = params['bulk_delete_request_v1_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/devicesensors/bulkdelete', 'POST',
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

    def device_sensors_v1_create_device_sensor(self, device_sensor_request, **kwargs):  # noqa: E501
        """New - Create a device sensor.  # noqa: E501

        Create a device sensor which includes sensor name, description, organization group identifier, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_create_device_sensor(device_sensor_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceSensorRequestV1Model device_sensor_request: Device sensor request model. Includes sensor name, description, organization group identifier, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_sensors_v1_create_device_sensor_with_http_info(device_sensor_request, **kwargs)  # noqa: E501
        else:
            (data) = self.device_sensors_v1_create_device_sensor_with_http_info(device_sensor_request, **kwargs)  # noqa: E501
            return data

    def device_sensors_v1_create_device_sensor_with_http_info(self, device_sensor_request, **kwargs):  # noqa: E501
        """New - Create a device sensor.  # noqa: E501

        Create a device sensor which includes sensor name, description, organization group identifier, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_create_device_sensor_with_http_info(device_sensor_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceSensorRequestV1Model device_sensor_request: Device sensor request model. Includes sensor name, description, organization group identifier, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_sensor_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_sensors_v1_create_device_sensor" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_sensor_request' is set
        if self.api_client.client_side_validation and ('device_sensor_request' not in params or
                                                       params['device_sensor_request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `device_sensor_request` when calling `device_sensors_v1_create_device_sensor`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'device_sensor_request' in params:
            body_params = params['device_sensor_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/devicesensors', 'POST',
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

    def device_sensors_v1_get_device_sensor(self, sensor_uuid, **kwargs):  # noqa: E501
        """New - Gets the device sensor information.  # noqa: E501

        Get a device sensor which includes sensor name, description, organization group identifier, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_get_device_sensor(sensor_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sensor_uuid: Uuid of the device sensor.(Required) (required)
        :return: DeviceSensorResponseV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_sensors_v1_get_device_sensor_with_http_info(sensor_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.device_sensors_v1_get_device_sensor_with_http_info(sensor_uuid, **kwargs)  # noqa: E501
            return data

    def device_sensors_v1_get_device_sensor_with_http_info(self, sensor_uuid, **kwargs):  # noqa: E501
        """New - Gets the device sensor information.  # noqa: E501

        Get a device sensor which includes sensor name, description, organization group identifier, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_get_device_sensor_with_http_info(sensor_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sensor_uuid: Uuid of the device sensor.(Required) (required)
        :return: DeviceSensorResponseV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sensor_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_sensors_v1_get_device_sensor" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sensor_uuid' is set
        if self.api_client.client_side_validation and ('sensor_uuid' not in params or
                                                       params['sensor_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sensor_uuid` when calling `device_sensors_v1_get_device_sensor`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sensor_uuid' in params:
            path_params['sensorUuid'] = params['sensor_uuid']  # noqa: E501

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
            '/devicesensors/{sensorUuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceSensorResponseV1Model',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def device_sensors_v1_get_device_sensors(self, organization_group_uuid, **kwargs):  # noqa: E501
        """New - Gets the list of all the device sensors for the Organization Group.  # noqa: E501

        Returns a list of device sensor(s) with sensor details for the Organization Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_get_device_sensors(organization_group_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Identifier of the Organization Group(Required) (required)
        :param int page: Specific page number to get. 0 based index
        :param int page_size: Maximum records per page. Default 500
        :return: DeviceSensorListResponseV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_sensors_v1_get_device_sensors_with_http_info(organization_group_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.device_sensors_v1_get_device_sensors_with_http_info(organization_group_uuid, **kwargs)  # noqa: E501
            return data

    def device_sensors_v1_get_device_sensors_with_http_info(self, organization_group_uuid, **kwargs):  # noqa: E501
        """New - Gets the list of all the device sensors for the Organization Group.  # noqa: E501

        Returns a list of device sensor(s) with sensor details for the Organization Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_get_device_sensors_with_http_info(organization_group_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_group_uuid: Identifier of the Organization Group(Required) (required)
        :param int page: Specific page number to get. 0 based index
        :param int page_size: Maximum records per page. Default 500
        :return: DeviceSensorListResponseV1Model
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_group_uuid', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_sensors_v1_get_device_sensors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_group_uuid' is set
        if self.api_client.client_side_validation and ('organization_group_uuid' not in params or
                                                       params['organization_group_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `organization_group_uuid` when calling `device_sensors_v1_get_device_sensors`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_group_uuid' in params:
            path_params['organizationGroupUuid'] = params['organization_group_uuid']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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
            '/devicesensors/list/{organizationGroupUuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceSensorListResponseV1Model',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def device_sensors_v1_update_device_sensor(self, sensor_uuid, device_sensor_request, **kwargs):  # noqa: E501
        """New - Update the device sensor.  # noqa: E501

        Update the device sensor which includes description, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_update_device_sensor(sensor_uuid, device_sensor_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sensor_uuid: Uuid of the device sensor.(Required) (required)
        :param DeviceSensorUpdateV1Model device_sensor_request: Device sensor update model. Includes sensor description, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_sensors_v1_update_device_sensor_with_http_info(sensor_uuid, device_sensor_request, **kwargs)  # noqa: E501
        else:
            (data) = self.device_sensors_v1_update_device_sensor_with_http_info(sensor_uuid, device_sensor_request, **kwargs)  # noqa: E501
            return data

    def device_sensors_v1_update_device_sensor_with_http_info(self, sensor_uuid, device_sensor_request, **kwargs):  # noqa: E501
        """New - Update the device sensor.  # noqa: E501

        Update the device sensor which includes description, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_sensors_v1_update_device_sensor_with_http_info(sensor_uuid, device_sensor_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sensor_uuid: Uuid of the device sensor.(Required) (required)
        :param DeviceSensorUpdateV1Model device_sensor_request: Device sensor update model. Includes sensor description, platform, query type, trigger type, execution context, timeout, script data, script blob identifier, event trigger, and schedule trigger.(Required) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sensor_uuid', 'device_sensor_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_sensors_v1_update_device_sensor" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sensor_uuid' is set
        if self.api_client.client_side_validation and ('sensor_uuid' not in params or
                                                       params['sensor_uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sensor_uuid` when calling `device_sensors_v1_update_device_sensor`")  # noqa: E501
        # verify the required parameter 'device_sensor_request' is set
        if self.api_client.client_side_validation and ('device_sensor_request' not in params or
                                                       params['device_sensor_request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `device_sensor_request` when calling `device_sensors_v1_update_device_sensor`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sensor_uuid' in params:
            path_params['sensorUuid'] = params['sensor_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'device_sensor_request' in params:
            body_params = params['device_sensor_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;version=1'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'CmsAuth']  # noqa: E501

        return self.api_client.call_api(
            '/devicesensors/{sensorUuid}', 'PUT',
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
