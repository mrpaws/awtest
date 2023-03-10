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
from mdmv1.api.gps_api import GPSApi  # noqa: E501
from mdmv1.rest import ApiException


class TestGPSApi(unittest.TestCase):
    """GPSApi unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.gps_api.GPSApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_g_ps_bulk_gps_coordinates_search_by_device_identifiers(self):
        """Test case for g_ps_bulk_gps_coordinates_search_by_device_identifiers

        Retrieves the GPS coordinates of multiple devices within the specified day range.  # noqa: E501
        """
        pass

    def test_g_ps_execute_bulk_gps_coordinates_by_device_by_alternate_id(self):
        """Test case for g_ps_execute_bulk_gps_coordinates_by_device_by_alternate_id

        Executes bulk gps coordinates by device and alternate id.  # noqa: E501
        """
        pass

    def test_g_ps_get_gps_coordinates_by_alternate_id(self):
        """Test case for g_ps_get_gps_coordinates_by_alternate_id

        Retrieves the GPS coordinates of the device identified by alternate id.  # noqa: E501
        """
        pass

    def test_g_ps_get_gps_coordinates_by_device(self):
        """Test case for g_ps_get_gps_coordinates_by_device

        Retrieves the GPS coordinates of the device identified by device ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
