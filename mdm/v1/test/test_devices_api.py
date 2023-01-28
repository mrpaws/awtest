# coding: utf-8

"""
    MDM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mdmv1
from mdmv1.api.devices_api import DevicesApi  # noqa: E501
from mdmv1.rest import ApiException


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.devices_api.DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_devices_bulk_delete_devices_async(self):
        """Test case for devices_bulk_delete_devices_async

        New - Deletes multiple devices identified by device id or alternate id.  # noqa: E501
        """
        pass

    def test_devices_bulk_get_devices_by_alternate_id_async(self):
        """Test case for devices_bulk_get_devices_by_alternate_id_async

        New - Retrieves information about multiple devices identified by the specified id type.  # noqa: E501
        """
        pass

    def test_devices_delete_async(self):
        """Test case for devices_delete_async

        New - Delete Device details by Device id.  # noqa: E501
        """
        pass

    def test_devices_delete_by_address_async(self):
        """Test case for devices_delete_by_address_async

        Deletes the device identified by MAC address.  # noqa: E501
        """
        pass

    def test_devices_delete_by_alternate_id_async(self):
        """Test case for devices_delete_by_alternate_id_async

        New - Deletes Device details by alternate id for Device.  # noqa: E501
        """
        pass

    def test_devices_device_extensive_search_async(self):
        """Test case for devices_device_extensive_search_async

        New - Extensive search of device details.  # noqa: E501
        """
        pass

    def test_devices_device_extensive_search_lite_async(self):
        """Test case for devices_device_extensive_search_lite_async

        New - Searches devices and its custom attributes.  # noqa: E501
        """
        pass

    def test_devices_edit_device_async(self):
        """Test case for devices_edit_device_async

        New - Edit the device details identified by Device id.  # noqa: E501
        """
        pass

    def test_devices_edit_device_by_alternate_id_async(self):
        """Test case for devices_edit_device_by_alternate_id_async

        New - Edit the device details identified by alternate id for Device.  # noqa: E501
        """
        pass

    def test_devices_filter_enrolled_devices_count_async(self):
        """Test case for devices_filter_enrolled_devices_count_async

        Retrieves Count of all enrolled devices based on any or all of the following OG id, Tag Name,and devices registered after 'SeenSince' datetime until the 'SeenTill' datetime.  # noqa: E501
        """
        pass

    def test_devices_get_app_status_async(self):
        """Test case for devices_get_app_status_async

        New - Gets App Status for a combination of input elements.  # noqa: E501
        """
        pass

    def test_devices_get_bulk_settings(self):
        """Test case for devices_get_bulk_settings

        Retrieve limits for bulk actions.  # noqa: E501
        """
        pass

    def test_devices_get_by_alternate_id_async(self):
        """Test case for devices_get_by_alternate_id_async

        New - Get Device details by Alternate id.  # noqa: E501
        """
        pass

    def test_devices_get_by_id_async(self):
        """Test case for devices_get_by_id_async

        New - Get Device details by Device id.  # noqa: E501
        """
        pass

    def test_devices_get_by_udid_async(self):
        """Test case for devices_get_by_udid_async

        New - Get device info based on UDID.  # noqa: E501
        """
        pass

    def test_devices_get_device_count_details(self):
        """Test case for devices_get_device_count_details

        Retrieves Device Count Information which are Categorized by Device Info like Platform, EnrollmentStatus, Ownership etc..  # noqa: E501
        """
        pass

    def test_devices_get_device_enrollment_statusby_udid_async(self):
        """Test case for devices_get_device_enrollment_statusby_udid_async

        Retrieves Device status based on the device identifier(UDID).  # noqa: E501
        """
        pass

    def test_devices_get_device_tags_async(self):
        """Test case for devices_get_device_tags_async

        New - Retrieves associated tags for a device  # noqa: E501
        """
        pass

    def test_devices_get_devices_by_id_async(self):
        """Test case for devices_get_devices_by_id_async

        New - Retrieves information about multiple devices identified by device id.  # noqa: E501
        """
        pass

    def test_devices_get_logged_in_users_async(self):
        """Test case for devices_get_logged_in_users_async

        Gets all logged in users on the device.  # noqa: E501
        """
        pass

    def test_devices_load_device_event_history(self):
        """Test case for devices_load_device_event_history

        Returns the device audit history for a device.  # noqa: E501
        """
        pass

    def test_devices_managed_settings_for_device_by_alternate_id(self):
        """Test case for devices_managed_settings_for_device_by_alternate_id

        Sets the managed settings for an iOS device based on alternate id.  # noqa: E501
        """
        pass

    def test_devices_search_async(self):
        """Test case for devices_search_async

        New - Find relevant devices using various criteria.  # noqa: E501
        """
        pass

    def test_devices_send_message(self):
        """Test case for devices_send_message

        Sends a push notification to the device identified by device ID. If not enrolled, sends an SMS message instead.  # noqa: E501
        """
        pass

    def test_devices_send_message_by_mac(self):
        """Test case for devices_send_message_by_mac

        Sends a push notification to the device identified by MAC address. If not enrolled, sends an SMS message instead.  # noqa: E501
        """
        pass

    def test_devices_send_message_by_serial_number(self):
        """Test case for devices_send_message_by_serial_number

        Sends a push notification to the device identified by serial number. If not enrolled, sends an SMS message instead.  # noqa: E501
        """
        pass

    def test_devices_send_message_by_udid(self):
        """Test case for devices_send_message_by_udid

        Sends a push notification to the device identified by UDID. If not enrolled, sends an SMS message instead.  # noqa: E501
        """
        pass

    def test_devices_update_custom_attributes_by_asset_nr(self):
        """Test case for devices_update_custom_attributes_by_asset_nr

        Updates the device custom attribute value if already present for a device, else adds the same to the device.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
